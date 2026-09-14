#!/usr/bin/env python3
"""Refresh the generated command-locator appendices in Foundation Book XIV."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "28-foundation-book-xiv-command-terminology-lexicon.md"
LEXICON = ROOT / "website" / "command-lexicon.json"

MANUAL_CODES = {
    "dom6-modding-manual-6.34": "M6.34",
    "dom6-event-modding-manual-6.29": "E6.29",
    "dom6-map-making-manual-6.26": "P6.26",
}

DOMAIN_CODES = {
    "ai-modding": "AI",
    "armor-modding": "Armour",
    "bless-modding": "Bless",
    "event-modding": "Event",
    "general-modding": "General",
    "item-modding": "Item",
    "map-making": "Map",
    "mercenary-modding": "Mercenary",
    "mod-metadata": "Metadata",
    "monster-modding": "Monster",
    "name-modding": "Names",
    "nation-modding": "Nation",
    "population-type-modding": "Poptype",
    "site-modding": "Site",
    "sound-modding": "Sound",
    "spell-modding": "Spell",
    "weapon-modding": "Weapon",
}

STATUS_LABELS = {
    "defined": "Defined",
    "reference-only": "Reference",
    "mentioned-only": "Mention",
}


def code(value: str) -> str:
    return f"`{value.replace('|', r'\|')}`"


def group_label(command: str) -> str:
    stripped = command.lstrip("#")
    if stripped.startswith("("):
        return "Templates"
    first = stripped[:1].upper()
    if first.isdigit():
        return "0-9"
    return first or "Other"


def manual_locator(entries: list[dict]) -> str:
    locators = []
    for entry in entries:
        locator = f"{MANUAL_CODES[entry['manual_id']]} p{entry['page']}"
        if locator not in locators:
            locators.append(locator)
    if len(locators) > 5:
        remaining = len(locators) - 5
        locators = locators[:5] + [f"+{remaining}"]
    return "; ".join(locators)


def strongest_syntax(entries: list[dict], fallback: str) -> str:
    for evidence in ("definition", "reference-only", "mention"):
        for entry in entries:
            if entry["evidence"] == evidence:
                return entry["syntax"]
    return fallback


def command_locator(data: dict) -> str:
    groups: dict[str, list[dict]] = defaultdict(list)
    for record in data["commands"]:
        groups[group_label(record["command"])].append(record)
    order = ["Templates", "0-9"] + [chr(number) for number in range(ord("A"), ord("Z") + 1)]
    chunks = []
    for label in order:
        records = groups.get(label, [])
        if not records:
            continue
        chunks.extend(
            [
                f"### {label}",
                "",
                "| Token | Status | Domain | Official locator | Strongest syntax |",
                "|---|---|---|---|---|",
            ]
        )
        for record in sorted(records, key=lambda row: row["command"].lower()):
            status = STATUS_LABELS[record["documentation_status"]]
            if record["command_kind"] == "template":
                status += "; template"
            elif record["command_kind"] == "message-placeholder":
                status += "; message"
            domains = ", ".join(DOMAIN_CODES[domain] for domain in record["domains"])
            chunks.append(
                "| "
                + " | ".join(
                    [
                        code(record["command"]),
                        status,
                        domains,
                        manual_locator(record["manual_entries"]),
                        code(strongest_syntax(record["manual_entries"], record["command"])),
                    ]
                )
                + " |"
            )
        chunks.append("")
    return "\n".join(chunks).rstrip()


def template_aliases(data: dict) -> str:
    lines = [
        "| Search alias | Official template | Derivation |",
        "|---|---|---|",
    ]
    basis = {
        "official-terrain-template": "Terrain substitution",
        "official-numeric-template": "Numeric range",
    }
    for row in data["aliases"]:
        lines.append(
            f"| {code(row['alias'])} | {code(row['target_command'])} | {basis[row['basis']]} |"
        )
    return "\n".join(lines)


def patch_exceptions(data: dict) -> str:
    lines = [
        "| Patch token | Reconciliation | Resolves to | Version | Editorial note |",
        "|---|---|---|---:|---|",
    ]
    for row in data["patch_reconciliation"]:
        if row["status"].startswith("exact-"):
            continue
        versions = sorted({record["version"] for record in row["patch_records"]}, key=lambda x: tuple(map(int, x.split("."))))
        if row["resolves_to"]:
            target = ", ".join(code(value) for value in row["resolves_to"])
        elif row["status"] == "official-patch-only":
            target = "Official announcement only; syntax pending"
        else:
            target = "Message grammar; no command target"
        lines.append(
            f"| {code(row['patch_token'])} | {row['status'].replace('-', ' ')} | {target} | {', '.join(versions)} | {row['note']} |"
        )
    return "\n".join(lines)


def patch_token_index(data: dict) -> str:
    lines = [
        "| Patch token | Present resolution | First version | Patch records |",
        "|---|---|---:|---:|",
    ]
    for row in data["patch_reconciliation"]:
        versions = sorted({record["version"] for record in row["patch_records"]}, key=lambda x: tuple(map(int, x.split("."))))
        if row["resolves_to"]:
            target = ", ".join(code(value) for value in row["resolves_to"])
        else:
            target = row["status"].replace("-", " ")
        lines.append(
            f"| {code(row['patch_token'])} | {target} | {versions[0]} | {len(row['patch_records'])} |"
        )
    return "\n".join(lines)


def replace_marker(text: str, name: str, content: str) -> str:
    pattern = re.compile(
        rf"<!-- GENERATED:BEGIN {re.escape(name)} -->.*?<!-- GENERATED:END {re.escape(name)} -->",
        re.S,
    )
    replacement = (
        f"<!-- GENERATED:BEGIN {name} -->\n{content}\n<!-- GENERATED:END {name} -->"
    )
    updated, count = pattern.subn(replacement, text)
    if count != 1:
        raise ValueError(f"Expected one generated marker for {name}, found {count}")
    return updated


def main() -> None:
    data = json.loads(LEXICON.read_text(encoding="utf-8"))
    text = BOOK.read_text(encoding="utf-8")
    replacements = {
        "patch-exceptions": patch_exceptions(data),
        "command-locator": command_locator(data),
        "template-aliases": template_aliases(data),
        "patch-token-index": patch_token_index(data),
    }
    for name, content in replacements.items():
        text = replace_marker(text, name, content)
    BOOK.write_text(text, encoding="utf-8")
    print(
        f"Updated {BOOK.name}: {len(data['commands'])} manual tokens, "
        f"{len(data['aliases'])} aliases, {len(data['patch_reconciliation'])} patch tokens"
    )


if __name__ == "__main__":
    main()
