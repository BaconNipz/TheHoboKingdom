#!/usr/bin/env python3
"""Build the official Dominions 6 command and terminology lexicon.

The source manuals are treated as locators rather than prose to reproduce.
Command spellings, syntax lines, pages, versions, section labels, and patch
provenance are retained.  Long explanatory passages remain in Illwinter's
manuals and are not copied into the public register.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import pdfplumber


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PROJECT_ROOT.parent
OUTPUT = PROJECT_ROOT / "website" / "command-lexicon.json"
SCHEMA = PROJECT_ROOT / "website" / "command-lexicon.schema.json"
PATCH_LEDGER = PROJECT_ROOT / "website" / "official-patch-ledger.json"

GENERATED_ON = "2026-08-28"
EDITION = "Progress Edition 27"
GAME_VERSION = "6.36"

MANUALS = (
    {
        "id": "dom6-modding-manual-6.34",
        "title": "Dominions 6 Modding Manual",
        "version": "6.34",
        "path": WORKSPACE_ROOT / "sources" / "dom6modman.pdf",
        "url": "https://illwinter.com/dom6/dom6modman.pdf",
        "manual_kind": "modding",
    },
    {
        "id": "dom6-event-modding-manual-6.29",
        "title": "Dominions 6 Event Modding Manual",
        "version": "6.29",
        "path": WORKSPACE_ROOT / "sources" / "dom6eventman.pdf",
        "url": "https://illwinter.com/dom6/dom6eventman.pdf",
        "manual_kind": "event",
    },
    {
        "id": "dom6-map-making-manual-6.26",
        "title": "Dominions 6 Map Making Manual",
        "version": "6.26",
        "path": WORKSPACE_ROOT / "sources" / "dom6mapman.pdf",
        "url": "https://illwinter.com/dom6/dom6mapman.pdf",
        "manual_kind": "map",
    },
)

TOKEN_RE = re.compile(
    r"##[A-Za-z0-9_]+##"
    r"|#\([A-Za-z]+\)[A-Za-z0-9_]+"
    r"|#[A-Za-z0-9][A-Za-z0-9_]*(?:\.\.\.[A-Za-z0-9]+)?"
)
NUMERIC_TEMPLATE_RE = re.compile(r"^(#[A-Za-z_]*?)(\d+)\.\.\.(\d+)$")
NUMERIC_SUFFIX_TEMPLATE_RE = re.compile(
    r"^(#[A-Za-z_]*?)(\d+)([A-Za-z][A-Za-z0-9_]*)\.\.\.(\d+)\3$"
)

TERRAINS = (
    "plain",
    "forest",
    "mountain",
    "swamp",
    "waste",
    "farm",
    "cave",
    "drip",
    "coast",
    "sea",
    "deep",
    "kelp",
    "foreign",
)

SPELLING_RECONCILIATIONS = {
    "#addseduction": {
        "resolves_to": ["#addseductions"],
        "status": "manual-spelling-mismatch",
        "note": "The update announcement uses the singular form; the Event Modding Manual defines the plural command.",
    },
    "#illusionimmune": {
        "resolves_to": ["#illusionsimmune"],
        "status": "manual-spelling-mismatch",
        "note": "The update announcement uses the singular form; the Modding Manual defines #illusionsimmune.",
    },
    "#res_mnrbs": {
        "resolves_to": ["#req_mnrbs"],
        "status": "manual-spelling-mismatch",
        "note": "The 6.34 announcement says #res_mnrbs; the Event Modding Manual defines #req_mnrbs.",
    },
}

PATCH_EXPRESSIONS = {
    "#not": {
        "resolves_to": ["#notmounted", "#notdismounted"],
        "status": "family-shorthand",
        "note": "Extracted from the official expression #not(dis)mounted; it is not a literal #not command.",
    },
    "#force": {
        "resolves_to": [],
        "status": "family-shorthand",
        "note": "Extracted from #force...vis; resolve to the documented forced-gem event-effect family.",
    },
    "#battlesum1dx": {
        "resolves_to": ["#battlesum1d2", "#battlesum1d3"],
        "status": "family-shorthand",
        "note": "The capital X denotes the dice-size family rather than a literal lower-case command.",
    },
    "#varxxx": {
        "resolves_to": [],
        "status": "message-placeholder",
        "note": "This is the ##varXXX## event-message substitution pattern, not a hash command.",
    },
}

POST_MANUAL_OFFICIAL_COMMANDS = {
    "#gainaffmount": {
        "resolves_to": [],
        "status": "official-patch-only",
        "note": "Introduced by the official 6.36 announcement after the current Event Modding Manual; the announcement establishes the spelling but does not supply full syntax.",
    },
    "#healaffmount": {
        "resolves_to": [],
        "status": "official-patch-only",
        "note": "Introduced by the official 6.36 announcement after the current Event Modding Manual; the announcement establishes the spelling but does not supply full syntax.",
    },
    "#newnbor": {
        "resolves_to": [],
        "status": "official-patch-only",
        "note": "Introduced by the official 6.36 announcement after the current Event Modding Manual; the announcement establishes the spelling but does not supply full syntax.",
    },
    "#remnbor": {
        "resolves_to": [],
        "status": "official-patch-only",
        "note": "Introduced by the official 6.36 announcement after the current Event Modding Manual; the announcement establishes the spelling but does not supply full syntax.",
    },
    "#req_provnbr": {
        "resolves_to": [],
        "status": "official-patch-only",
        "note": "Introduced by the official 6.36 announcement after the current Event Modding Manual; the announcement establishes the spelling but does not supply full syntax.",
    },
}


def ascii_text(value: str) -> str:
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
        "\u2026": "...",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return re.sub(r"\s+", " ", value).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_hash(record: dict[str, Any]) -> str:
    payload = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def slug(command: str) -> str:
    if command.startswith("##"):
        inner = command.strip("#")
        base = re.sub(r"[^a-z0-9]+", "-", inner.lower()).strip("-")
        if inner != inner.lower():
            case_hash = hashlib.sha256(inner.encode("utf-8")).hexdigest()[:6]
            return f"term-{base}-case-{case_hash}"
        return f"term-{base}"
    value = command.lower().lstrip("#")
    value = value.replace("(terrain)", "terrain-template")
    value = value.replace("...", "-through-")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return f"cmd-{value}"


def line_groups(page) -> list[dict[str, Any]]:
    words = page.extract_words(extra_attrs=["fontname", "size"])
    groups: dict[tuple[int, float], list[dict[str, Any]]] = defaultdict(list)
    for word in words:
        column = 0 if word["x0"] < page.width / 2 else 1
        groups[(column, round(float(word["top"]), 1))].append(word)
    lines = []
    for (column, top), group in groups.items():
        ordered = sorted(group, key=lambda word: word["x0"])
        lines.append(
            {
                "column": column,
                "top": top,
                "words": ordered,
                "text": ascii_text(" ".join(word["text"] for word in ordered)),
                "max_size": max(float(word["size"]) for word in ordered),
            }
        )
    return sorted(lines, key=lambda line: (line["column"], line["top"]))


def heading_level(line: dict[str, Any]) -> int | None:
    text = line["text"]
    if not text or "#" in text or len(text) > 100:
        return None
    size = line["max_size"]
    if size >= 13.0:
        return 1
    if size >= 11.2:
        return 2
    return None


def evidence_type(word: dict[str, Any]) -> str:
    font = word["fontname"]
    if "Bold" in font:
        return "definition"
    if "Mono" in font:
        return "reference-only"
    return "mention"


def domain_for(manual_kind: str, section: str | None, subsection: str | None, page: int) -> str:
    if manual_kind == "event":
        return "event-modding"
    if manual_kind == "map":
        return "map-making"
    label = f"{section or ''} {subsection or ''}".lower()
    rules = (
        ("sound", "sound-modding"),
        ("weapon", "weapon-modding"),
        ("armor", "armor-modding"),
        ("monster", "monster-modding"),
        ("leadership", "monster-modding"),
        ("name modding", "name-modding"),
        ("bless", "bless-modding"),
        ("site", "site-modding"),
        ("nation", "nation-modding"),
        ("spell", "spell-modding"),
        ("magic item", "item-modding"),
        ("poptype", "population-type-modding"),
        ("mercenary", "mercenary-modding"),
        ("ai modding", "ai-modding"),
        ("general modding", "general-modding"),
        ("mod info", "mod-metadata"),
    )
    for needle, domain in rules:
        if needle in label:
            return domain
    if 6 <= page <= 11:
        return "weapon-modding"
    if page == 12:
        return "armor-modding"
    if 13 <= page <= 36:
        return "monster-modding"
    if 37 <= page <= 40:
        return "site-modding"
    if 41 <= page <= 49:
        return "nation-modding"
    if 50 <= page <= 54:
        return "spell-modding"
    if 55 <= page <= 58:
        return "item-modding"
    return "general-modding"


def families(command: str, domains: list[str]) -> list[str]:
    name = command.lower()
    result = set()
    if name.startswith("##"):
        result.add("message-substitution")
    if name.startswith("#req_") or name.startswith("#req"):
        result.add("requirement")
    if name.startswith(("#select", "#new", "#copy", "#clear")) or name == "#end":
        result.add("object-lifecycle")
    if name.startswith("#ai"):
        result.add("artificial-intelligence")
    if any(part in name for part in ("spr", "sprite", "icon", "image", "sound")):
        result.add("presentation-assets")
    if any(part in name for part in ("shape", "mount", "rider")):
        result.add("forms-and-mounts")
    if any(part in name for part in ("spell", "magic", "path", "gem")):
        result.add("magic")
    if any(domain in domains for domain in ("nation-modding", "population-type-modding")):
        result.add("nation-and-recruitment")
    if "event-modding" in domains:
        result.add("events")
    if "map-making" in domains:
        result.add("maps")
    return sorted(result or {"general"})


def canonical_sections(domains: list[str]) -> list[str]:
    result = {"b14-command-lexicon"}
    for domain in domains:
        if domain == "event-modding":
            result.add("b8-event-language")
        elif domain == "map-making":
            result.add("b8-map-language")
        elif domain == "ai-modding":
            result.add("b8-ai-language")
        elif domain == "nation-modding":
            result.add("b8-nation-language")
        elif domain in {"weapon-modding", "armor-modding"}:
            result.add("b8-combat-object-language")
        elif domain in {"spell-modding", "item-modding", "bless-modding"}:
            result.add("b8-magic-object-language")
        elif domain == "site-modding":
            result.add("b8-site-language")
        else:
            result.add("b8-object-language")
    return sorted(result)


def extract_manual(manual: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    occurrences: list[dict[str, Any]] = []
    section = None
    subsection = None
    with pdfplumber.open(manual["path"]) as pdf:
        page_count = len(pdf.pages)
        for page_number, page in enumerate(pdf.pages, 1):
            for line in line_groups(page):
                level = heading_level(line)
                if level == 1:
                    section = line["text"]
                    subsection = None
                    continue
                if level == 2:
                    subsection = line["text"]
                    continue
                matches = list(TOKEN_RE.finditer(line["text"]))
                if not matches:
                    continue
                token_words = [word for word in line["words"] if TOKEN_RE.search(word["text"])]
                for match_index, match in enumerate(matches):
                    command = match.group(0)
                    word = token_words[min(match_index, len(token_words) - 1)]
                    evidence = evidence_type(word)
                    syntax = command
                    if evidence == "definition" and len(matches) == 1:
                        syntax = line["text"][match.start() :]
                    occurrences.append(
                        {
                            "command": command,
                            "manual_id": manual["id"],
                            "manual_version": manual["version"],
                            "manual_kind": manual["manual_kind"],
                            "page": page_number,
                            "section": section,
                            "subsection": subsection,
                            "evidence": evidence,
                            "syntax": syntax,
                            "domain": domain_for(
                                manual["manual_kind"], section, subsection, page_number
                            ),
                        }
                    )
    source = {
        "id": manual["id"],
        "title": manual["title"],
        "version": manual["version"],
        "manual_kind": manual["manual_kind"],
        "page_count": page_count,
        "url": manual["url"],
        "sha256": sha256(manual["path"]),
    }
    return occurrences, source


def dedupe_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rank = {"definition": 0, "reference-only": 1, "mention": 2}
    entries = sorted(
        entries,
        key=lambda entry: (
            rank[entry["evidence"]],
            entry["manual_id"],
            entry["page"],
            entry["syntax"],
        ),
    )
    strong = [entry for entry in entries if entry["evidence"] != "mention"]
    chosen = strong if strong else entries[:5]
    seen = set()
    result = []
    for entry in chosen:
        key = (
            entry["manual_id"],
            entry["page"],
            entry["evidence"],
            entry["section"],
            entry["subsection"],
            entry["syntax"],
        )
        if key in seen:
            continue
        seen.add(key)
        result.append({key: value for key, value in entry.items() if key not in {"command", "manual_kind", "domain"}})
    return result


def template_aliases(commands: set[str]) -> list[dict[str, Any]]:
    aliases: dict[str, dict[str, Any]] = {}
    for command in sorted(commands):
        lowered = command.lower()
        if "(terrain)" in lowered:
            suffix = lowered.split(")", 1)[1]
            terrains = list(TERRAINS)
            if suffix in {"fortrec", "fortcom"}:
                terrains = [terrain for terrain in terrains if terrain not in {"sea", "deep", "kelp"}]
            for terrain in terrains:
                alias = f"#{terrain}{suffix}"
                aliases[alias] = {
                    "alias": alias,
                    "target_command": lowered,
                    "basis": "official-terrain-template",
                    "synthetic": True,
                }
        match = NUMERIC_TEMPLATE_RE.match(lowered)
        if match:
            prefix, start, end = match.groups()
            for number in range(int(start), int(end) + 1):
                alias = f"{prefix}{number}"
                aliases[alias] = {
                    "alias": alias,
                    "target_command": lowered,
                    "basis": "official-numeric-template",
                    "synthetic": True,
                }
        suffix_match = NUMERIC_SUFFIX_TEMPLATE_RE.match(lowered)
        if suffix_match:
            prefix, start, suffix, end = suffix_match.groups()
            for number in range(int(start), int(end) + 1):
                alias = f"{prefix}{number}{suffix}"
                aliases[alias] = {
                    "alias": alias,
                    "target_command": lowered,
                    "basis": "official-numeric-template",
                    "synthetic": True,
                }
    return sorted(aliases.values(), key=lambda row: row["alias"])


def patch_command_map(patch_ledger: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in patch_ledger["records"]:
        for command in record.get("commands", []):
            result[command.lower()].append(
                {
                    "version": record["version"],
                    "record_id": record["id"],
                    "source_id": record["source_id"],
                    "source_locator": record["source_locator"],
                    "classification": record["classification"],
                    "direction": record["direction"],
                }
            )
    return result


def reconciliation(
    patch_commands: dict[str, list[dict[str, Any]]],
    command_records: dict[str, dict[str, Any]],
    aliases: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    alias_map = {entry["alias"]: entry["target_command"] for entry in aliases}
    force_family = sorted(
        command for command in command_records if command.startswith("#force") and command.endswith("vis")
    )
    result = []
    for token, provenance in sorted(patch_commands.items()):
        if token in SPELLING_RECONCILIATIONS:
            resolution = SPELLING_RECONCILIATIONS[token]
        elif token in PATCH_EXPRESSIONS:
            resolution = dict(PATCH_EXPRESSIONS[token])
            if token == "#force":
                resolution["resolves_to"] = force_family
        elif token in POST_MANUAL_OFFICIAL_COMMANDS:
            resolution = POST_MANUAL_OFFICIAL_COMMANDS[token]
        elif token in command_records:
            status = command_records[token]["documentation_status"]
            resolution = {
                "resolves_to": [token],
                "status": f"exact-{status}",
                "note": "The token has an exact current-manual locator.",
            }
        elif token in alias_map:
            resolution = {
                "resolves_to": [alias_map[token]],
                "status": "template-alias",
                "note": "The literal form is generated by an official terrain or numeric command template.",
            }
        else:
            resolution = {
                "resolves_to": [],
                "status": "patch-only-unresolved",
                "note": "No exact definition, reference-list entry, template alias, or controlled reconciliation was found.",
            }
        result.append(
            {
                "patch_token": token,
                "status": resolution["status"],
                "resolves_to": resolution["resolves_to"],
                "note": resolution["note"],
                "patch_records": provenance,
            }
        )
    return result


def schema_document() -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://thehobokingdom.com/dominions/library/schemas/command-lexicon.schema.json",
        "title": "Dominions 6 command lexicon",
        "type": "object",
        "required": [
            "schema_version",
            "edition",
            "ruleset",
            "sources",
            "summary",
            "commands",
            "aliases",
            "patch_reconciliation",
        ],
        "properties": {
            "schema_version": {"type": "string"},
            "edition": {"type": "string"},
            "generated_on": {"type": "string", "format": "date"},
            "ruleset": {"type": "object"},
            "scope": {"type": "object"},
            "sources": {"type": "array", "items": {"type": "object"}},
            "summary": {"type": "object"},
            "commands": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": [
                        "id",
                        "command",
                        "documentation_status",
                        "domains",
                        "manual_entries",
                        "record_hash",
                    ],
                    "properties": {
                        "id": {"type": "string", "pattern": "^(cmd|term)-"},
                        "command": {"type": "string", "pattern": "^#"},
                        "documentation_status": {
                            "enum": ["defined", "reference-only", "mentioned-only"]
                        },
                        "domains": {"type": "array", "items": {"type": "string"}},
                        "manual_entries": {"type": "array", "items": {"type": "object"}},
                        "record_hash": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                    },
                    "additionalProperties": True,
                },
            },
            "aliases": {"type": "array", "items": {"type": "object"}},
            "patch_reconciliation": {"type": "array", "items": {"type": "object"}},
        },
        "additionalProperties": True,
    }


def build() -> dict[str, Any]:
    all_occurrences = []
    sources = []
    for manual in MANUALS:
        occurrences, source = extract_manual(manual)
        all_occurrences.extend(occurrences)
        sources.append(source)

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    display: dict[str, str] = {}
    for occurrence in all_occurrences:
        key = (
            occurrence["command"]
            if occurrence["command"].startswith("##")
            else occurrence["command"].lower()
        )
        grouped[key].append(occurrence)
        display.setdefault(key, occurrence["command"])

    patch_ledger = json.loads(PATCH_LEDGER.read_text(encoding="utf-8"))
    patch_commands = patch_command_map(patch_ledger)
    command_records: dict[str, dict[str, Any]] = {}
    for key, entries in sorted(grouped.items()):
        evidence = {entry["evidence"] for entry in entries}
        if "definition" in evidence:
            status = "defined"
        elif "reference-only" in evidence:
            status = "reference-only"
        else:
            status = "mentioned-only"
        domains = sorted({entry["domain"] for entry in entries})
        manual_entries = dedupe_entries(entries)
        record = {
            "id": slug(display[key]),
            "command": display[key],
            "normalized_command": key,
            "command_kind": (
                "message-placeholder"
                if key.startswith("##")
                else "template"
                if "(terrain)" in key or "..." in key
                else "literal"
            ),
            "documentation_status": status,
            "domains": domains,
            "families": families(key, domains),
            "manual_entries": manual_entries,
            "patch_records": patch_commands.get(key, []),
            "canonical_section_ids": canonical_sections(domains),
            "cautions": sorted(
                {
                    *(["Context-sensitive: the same spelling is defined for more than one object type."] if len({entry["domain"] for entry in entries if entry["evidence"] == "definition"}) > 1 else []),
                    *(["Template spelling: use a documented literal expansion rather than the parentheses or ellipsis form."] if "(terrain)" in key or "..." in key else []),
                    *(["The current manuals mention this token but do not provide a full definition line."] if status == "mentioned-only" else []),
                }
            ),
        }
        record["record_hash"] = stable_hash(record)
        command_records[key] = record

    aliases = template_aliases(set(command_records))
    patch_reconciliation = reconciliation(patch_commands, command_records, aliases)
    unresolved = [row for row in patch_reconciliation if row["status"] == "patch-only-unresolved"]
    if unresolved:
        raise ValueError(f"Unresolved patch tokens: {[row['patch_token'] for row in unresolved]}")

    status_counts = defaultdict(int)
    kind_counts = defaultdict(int)
    for record in command_records.values():
        status_counts[record["documentation_status"]] += 1
        kind_counts[record["command_kind"]] += 1
    reconciliation_counts = defaultdict(int)
    for row in patch_reconciliation:
        reconciliation_counts[row["status"]] += 1

    result = {
        "schema_version": "1.0.0",
        "edition": EDITION,
        "generated_on": GENERATED_ON,
        "ruleset": {
            "game": "Dominions 6",
            "game_version": GAME_VERSION,
            "mods": [],
            "ruleset_id": "dom6-6.36",
        },
        "scope": {
            "description": "Every hash-token located in the current official Modding, Event Modding, and Map Making manuals, plus controlled reconciliation of every hash-token extracted from official 6.01-6.36 update announcements.",
            "manual_baseline_note": "The manuals carry their own versions and may lag the executable. Patch provenance is retained separately rather than silently merged into manual syntax.",
            "excludes": [
                "long verbatim manual descriptions",
                "unverified community syntax",
                "DE-only commands",
                "Divinitus-only commands",
                "runtime behaviour not established by the official sources",
            ],
        },
        "evidence_model": {
            "defined": "Bold command definition or syntax line in a current official manual.",
            "reference-only": "Official manual reference-list or example-code occurrence without a detailed definition line.",
            "mentioned-only": "Official manual prose mention without a definition or reference-list line.",
            "template-alias": "Literal lookup form derived from an official terrain or numeric template.",
            "patch-reconciliation": "Historical token retained from an official update announcement and mapped without altering the source record.",
            "official-patch-only": "Officially announced after the current manuals; spelling and provenance are known, but full syntax awaits an updated official manual.",
        },
        "sources": sources
        + [
            {
                "id": "official-patch-ledger-edition-27",
                "title": "Official Dominions 6 update announcement ledger",
                "version_range": "6.01-6.36",
                "record_count": len(patch_ledger["records"]),
                "sha256": sha256(PATCH_LEDGER),
                "source_url": "https://steamcommunity.com/app/2511500/announcements/",
            }
        ],
        "summary": {
            "unique_manual_tokens": len(command_records),
            "manual_occurrences_examined": len(all_occurrences),
            "documentation_status_counts": dict(sorted(status_counts.items())),
            "token_kind_counts": dict(sorted(kind_counts.items())),
            "generated_alias_count": len(aliases),
            "patch_token_count": len(patch_commands),
            "patch_reconciliation_counts": dict(sorted(reconciliation_counts.items())),
            "unresolved_patch_token_count": len(unresolved),
        },
        "commands": list(command_records.values()),
        "aliases": aliases,
        "patch_reconciliation": patch_reconciliation,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    SCHEMA.write_text(json.dumps(schema_document(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    data = build()
    print(json.dumps(data["summary"], indent=2))
