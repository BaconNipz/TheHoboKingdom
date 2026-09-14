#!/usr/bin/env python3
"""Build a deterministic source index for Dominions 6 .dm files.

The index deliberately records source blocks rather than pretending to be a
complete simulation of the Dominions loader.  It is suitable for provenance,
collision screening, website search, and selecting objects for closer manual
resolution.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


COMMAND_RE = re.compile(r"^\s*#([A-Za-z0-9_]+)(?:\s+(.*?))?\s*$", re.DOTALL)
BLOCK_START_RE = re.compile(r"^(new|select)([A-Za-z0-9_]+)$")
NUMBER_RE = re.compile(r"^-?\d+$")


def split_inline_comment(text: str) -> tuple[str, str]:
    """Split a command argument from a -- comment, respecting quoted strings."""
    quoted = False
    escaped = False
    for index in range(len(text) - 1):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            quoted = not quoted
            continue
        if not quoted and text[index : index + 2] == "--":
            return text[:index].rstrip(), text[index + 2 :].strip()
    return text.rstrip(), ""


def unquote(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def first_argument(value: str | None) -> str | None:
    """Return one quoted token or the first whitespace-delimited token."""
    if not value:
        return None
    value = value.strip()
    if value.startswith('"'):
        escaped = False
        for index in range(1, len(value)):
            char = value[index]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                return value[: index + 1]
    return value.split(maxsplit=1)[0]


def heading_from_comment(raw: str) -> str | None:
    stripped = raw.strip()
    if not stripped.startswith("--"):
        return None
    body = stripped.lstrip("-").strip()
    body = body.rstrip("-").strip()
    if not body or body.startswith("#") or len(body) > 110:
        return None
    letters = [char for char in body if char.isalpha()]
    upper_ratio = (
        sum(char.isupper() for char in letters) / len(letters) if letters else 0
    )
    framed = stripped.endswith("--") or stripped.startswith("---")
    heading_words = {
        "weapon",
        "weapons",
        "armor",
        "armors",
        "armour",
        "armours",
        "monster",
        "monsters",
        "unit",
        "units",
        "pretender",
        "pretenders",
        "spell",
        "spells",
        "site",
        "sites",
        "item",
        "items",
        "event",
        "events",
        "nation",
        "nations",
        "bless",
        "blesses",
        "general",
    }
    normalized_words = set(re.findall(r"[a-z]+", body.lower()))
    if framed or upper_ratio >= 0.72 or normalized_words & heading_words:
        return body
    return None


def has_open_quote(text: str) -> bool:
    """Return True when a logical command still has an unclosed quote."""
    quoted = False
    escaped = False
    for char in text:
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
    return quoted


@dataclass
class Command:
    name: str
    argument: str | None
    comment: str
    line: int

    def as_dict(self) -> dict:
        return {
            "command": self.name,
            "argument": self.argument,
            "comment": self.comment or None,
            "line": self.line,
        }


@dataclass
class Block:
    source: str
    sequence: int
    action: str
    kind: str
    selector: str | None
    line_start: int
    heading: str | None
    commands: list[Command] = field(default_factory=list)
    line_end: int | None = None

    def values(self, command: str) -> list[str | None]:
        return [item.argument for item in self.commands if item.name == command]

    @property
    def name(self) -> str | None:
        names = self.values("name")
        if names:
            return unquote(names[-1])
        return unquote(self.selector)

    @property
    def fixed_numeric_selector(self) -> int | None:
        if self.selector is not None and NUMBER_RE.fullmatch(self.selector):
            return int(self.selector)
        return None

    def as_dict(self) -> dict:
        command_map: dict[str, list[str | None]] = defaultdict(list)
        for item in self.commands:
            command_map[item.name].append(item.argument)
        return {
            "source": self.source,
            "sequence": self.sequence,
            "action": self.action,
            "kind": self.kind,
            "selector": self.selector,
            "numeric_selector": self.fixed_numeric_selector,
            "name": self.name,
            "heading": self.heading,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "commands": dict(command_map),
            "command_stream": [item.as_dict() for item in self.commands],
        }


@dataclass
class ModIndex:
    path: Path
    metadata: dict
    blocks: list[Block]
    globals: list[Command]
    command_counts: Counter
    line_count: int
    byte_count: int
    sha256: str
    warnings: list[str]

    @property
    def label(self) -> str:
        return str(self.metadata.get("modname") or self.path.stem)


def parse_mod(path: Path) -> ModIndex:
    payload = path.read_bytes()
    text = payload.decode("utf-8-sig")
    lines = text.splitlines()
    metadata: dict[str, str | float | None] = {}
    blocks: list[Block] = []
    globals_: list[Command] = []
    counts: Counter = Counter()
    warnings: list[str] = []
    current: Block | None = None
    heading: str | None = None

    line_index = 0
    while line_index < len(lines):
        raw = lines[line_index]
        line_number = line_index + 1
        possible_heading = heading_from_comment(raw)
        if possible_heading:
            heading = possible_heading

        if not raw.lstrip().startswith("#"):
            line_index += 1
            continue

        logical = raw
        while has_open_quote(logical) and line_index + 1 < len(lines):
            line_index += 1
            logical += "\n" + lines[line_index]

        match = COMMAND_RE.match(logical)
        if not match:
            warnings.append(f"Unparsed command-like line {line_number}")
            line_index += 1
            continue
        command_name = match.group(1).lower()
        argument_text, comment = split_inline_comment(match.group(2) or "")
        argument = argument_text or None
        counts[command_name] += 1

        start_match = BLOCK_START_RE.match(command_name)
        if start_match:
            if current is not None:
                warnings.append(
                    f"Implicitly closed {current.action}{current.kind} from "
                    f"line {current.line_start} at line {line_number}"
                )
                current.line_end = line_number - 1
                blocks.append(current)
            action, kind = start_match.groups()
            selector_token = first_argument(argument)
            current = Block(
                source=path.name,
                sequence=len(blocks) + 1,
                action=action,
                kind=kind.lower(),
                selector=unquote(selector_token),
                line_start=line_number,
                heading=heading,
            )
            current.commands.append(
                Command(command_name, argument, comment, line_number)
            )
            line_index += 1
            continue

        command = Command(command_name, argument, comment, line_number)
        if command_name == "end" and current is not None:
            current.commands.append(command)
            current.line_end = line_number
            blocks.append(current)
            current = None
            line_index += 1
            continue

        if current is not None:
            current.commands.append(command)
        else:
            globals_.append(command)
            if command_name in {"modname", "description", "icon"}:
                metadata[command_name] = unquote(argument)
            elif command_name in {"version", "domversion"}:
                metadata[command_name] = unquote(argument)
        line_index += 1

    if current is not None:
        current.line_end = len(lines)
        blocks.append(current)
        warnings.append(
            f"Unterminated {current.action}{current.kind} from line "
            f"{current.line_start}"
        )

    return ModIndex(
        path=path,
        metadata=metadata,
        blocks=blocks,
        globals=globals_,
        command_counts=counts,
        line_count=len(lines),
        byte_count=len(payload),
        sha256=hashlib.sha256(payload).hexdigest(),
        warnings=warnings,
    )


def distinct_selectors(mod: ModIndex) -> dict[str, set[str]]:
    output: dict[str, set[str]] = defaultdict(set)
    for block in mod.blocks:
        if block.action == "select" and block.selector is not None:
            output[block.kind].add(block.selector)
    return output


def fixed_new_ids(mod: ModIndex) -> dict[str, set[int]]:
    output: dict[str, set[int]] = defaultdict(set)
    for block in mod.blocks:
        if block.action == "new" and block.fixed_numeric_selector is not None:
            output[block.kind].add(block.fixed_numeric_selector)
    return output


def integer_arguments(mod: ModIndex, names: Iterable[str]) -> dict[str, set[int]]:
    wanted = set(names)
    output: dict[str, set[int]] = defaultdict(set)
    for block in mod.blocks:
        for command in block.commands:
            if command.name not in wanted or not command.argument:
                continue
            token = first_argument(command.argument)
            if token and NUMBER_RE.fullmatch(token):
                output[command.name].add(int(token))
    return output


def summarize(mod: ModIndex) -> dict:
    block_counts = Counter(f"{block.action}{block.kind}" for block in mod.blocks)
    kind_counts = Counter(block.kind for block in mod.blocks)
    automatic = Counter(
        block.kind
        for block in mod.blocks
        if block.action == "new" and block.selector is None
    )
    fixed_ids_by_kind: dict[str, list[int]] = defaultdict(list)
    for block in mod.blocks:
        if block.action == "new" and block.fixed_numeric_selector is not None:
            fixed_ids_by_kind[block.kind].append(block.fixed_numeric_selector)
    duplicate_fixed_ids = {}
    for kind, identifiers in fixed_ids_by_kind.items():
        duplicates = sorted(
            identifier
            for identifier, count in Counter(identifiers).items()
            if count > 1
        )
        if duplicates:
            duplicate_fixed_ids[kind] = duplicates
    pretender_candidates = [
        block
        for block in mod.blocks
        if block.kind == "monster"
        and any(
            command.name in {"startdom", "pathcost", "homerealm"}
            for command in block.commands
        )
    ]
    global_counts = Counter(command.name for command in mod.globals)
    return {
        "file": mod.path.name,
        "metadata": mod.metadata,
        "line_count": mod.line_count,
        "byte_count": mod.byte_count,
        "sha256": mod.sha256,
        "active_command_count": sum(mod.command_counts.values()),
        "command_counts": dict(sorted(mod.command_counts.items())),
        "block_count": len(mod.blocks),
        "block_counts": dict(sorted(block_counts.items())),
        "kind_counts": dict(sorted(kind_counts.items())),
        "automatic_new_objects": dict(sorted(automatic.items())),
        "distinct_fixed_new_ids": {
            kind: len(set(identifiers))
            for kind, identifiers in sorted(fixed_ids_by_kind.items())
        },
        "duplicate_fixed_new_ids": duplicate_fixed_ids,
        "pretender_candidate_blocks": len(pretender_candidates),
        "global_command_counts": dict(sorted(global_counts.items())),
        "warnings": mod.warnings,
    }


def compatibility(a: ModIndex, b: ModIndex) -> dict:
    a_selected = distinct_selectors(a)
    b_selected = distinct_selectors(b)
    selected_overlap = {}
    for kind in sorted(set(a_selected) | set(b_selected)):
        shared = sorted(
            a_selected.get(kind, set()) & b_selected.get(kind, set()),
            key=lambda value: (not NUMBER_RE.fullmatch(value), value),
        )
        selected_overlap[kind] = {
            "first_distinct": len(a_selected.get(kind, set())),
            "second_distinct": len(b_selected.get(kind, set())),
            "shared_count": len(shared),
            "shared": shared,
        }

    a_new = fixed_new_ids(a)
    b_new = fixed_new_ids(b)
    new_id_overlap = {}
    for kind in sorted(set(a_new) | set(b_new)):
        shared_ids = sorted(a_new.get(kind, set()) & b_new.get(kind, set()))
        new_id_overlap[kind] = {
            "first_fixed_ids": len(a_new.get(kind, set())),
            "second_fixed_ids": len(b_new.get(kind, set())),
            "shared_count": len(shared_ids),
            "shared_ids": shared_ids,
        }

    cross_action_overlap = {}
    all_kinds = sorted(
        {block.kind for block in a.blocks} | {block.kind for block in b.blocks}
    )
    for kind in all_kinds:
        first_new = {
            block.fixed_numeric_selector
            for block in a.blocks
            if block.kind == kind
            and block.action == "new"
            and block.fixed_numeric_selector is not None
        }
        first_selected = {
            block.fixed_numeric_selector
            for block in a.blocks
            if block.kind == kind
            and block.action == "select"
            and block.fixed_numeric_selector is not None
        }
        second_new = {
            block.fixed_numeric_selector
            for block in b.blocks
            if block.kind == kind
            and block.action == "new"
            and block.fixed_numeric_selector is not None
        }
        second_selected = {
            block.fixed_numeric_selector
            for block in b.blocks
            if block.kind == kind
            and block.action == "select"
            and block.fixed_numeric_selector is not None
        }
        combinations = {
            "first_new_second_new": sorted(first_new & second_new),
            "first_new_second_selected": sorted(first_new & second_selected),
            "first_selected_second_new": sorted(first_selected & second_new),
            "first_selected_second_selected": sorted(
                first_selected & second_selected
            ),
        }
        if any(combinations.values()):
            cross_action_overlap[kind] = {
                key: {"count": len(values), "ids": values}
                for key, values in combinations.items()
            }

    event_commands = {
        "code",
        "req_code",
        "req_notcode",
        "req_anycode",
        "req_notanycode",
        "req_nearbycode",
        "req_nearowncode",
        "resetcode",
        "resetcodedelay",
        "resetcodedelay2",
    }
    variable_commands = {
        "req_varpos",
        "req_varneg",
        "req_varzero",
        "req_varone",
        "req_var",
        "incvar",
        "decvar",
        "clearvar",
    }
    event_a = integer_arguments(a, event_commands)
    event_b = integer_arguments(b, event_commands)
    var_a = integer_arguments(a, variable_commands)
    var_b = integer_arguments(b, variable_commands)
    all_event_a = set().union(*event_a.values()) if event_a else set()
    all_event_b = set().union(*event_b.values()) if event_b else set()
    all_var_a = set().union(*var_a.values()) if var_a else set()
    all_var_b = set().union(*var_b.values()) if var_b else set()

    return {
        "load_order": [a.path.name, b.path.name],
        "selected_object_overlap": selected_overlap,
        "fixed_new_id_overlap": new_id_overlap,
        "cross_action_numeric_overlap": cross_action_overlap,
        "event_code_usage": {
            "first": sorted(all_event_a),
            "second": sorted(all_event_b),
            "shared": sorted(all_event_a & all_event_b),
        },
        "event_variable_usage": {
            "first": sorted(all_var_a),
            "second": sorted(all_var_b),
            "shared": sorted(all_var_a & all_var_b),
        },
        "interpretive_warning": (
            "This is a source-level collision screen, not a simulation of the "
            "Dominions loader. Automatic IDs, name references, inherited "
            "fields, cross-category parsing, and engine runtime effects still "
            "require resolved-object or in-game verification."
        ),
    }


def write_catalogue(path: Path, mods: list[ModIndex]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "source",
                "sequence",
                "action",
                "kind",
                "selector",
                "name",
                "heading",
                "line_start",
                "line_end",
                "command_count",
            ]
        )
        for mod in mods:
            for block in mod.blocks:
                writer.writerow(
                    [
                        block.source,
                        block.sequence,
                        block.action,
                        block.kind,
                        block.selector or "",
                        block.name or "",
                        block.heading or "",
                        block.line_start,
                        block.line_end,
                        len(block.commands),
                    ]
                )


def write_jsonl(path: Path, mods: list[ModIndex]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        for mod in mods:
            for block in mod.blocks:
                stream.write(json.dumps(block.as_dict(), ensure_ascii=False))
                stream.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("first_mod", type=Path)
    parser.add_argument("second_mod", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    mods = [parse_mod(args.first_mod), parse_mod(args.second_mod)]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = args.output_dir / "mod-index-summary.json"
    catalogue_path = args.output_dir / "mod-object-catalogue.tsv"
    jsonl_path = args.output_dir / "mod-object-blocks.jsonl"

    payload = {
        "schema_version": 1,
        "scope": (
            "Source blocks from the supplied Dominions Enhanced and Divinitus "
            "files; not resolved vanilla inheritance."
        ),
        "mods": [summarize(mod) for mod in mods],
        "compatibility": compatibility(*mods),
    }
    summary_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_catalogue(catalogue_path, mods)
    write_jsonl(jsonl_path, mods)
    print(summary_path)
    print(catalogue_path)
    print(jsonl_path)


if __name__ == "__main__":
    main()
