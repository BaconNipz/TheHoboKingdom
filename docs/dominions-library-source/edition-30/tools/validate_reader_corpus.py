#!/usr/bin/env python3
"""Run structural and editorial checks across the published reader corpus."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from navigation import DESTINATION_ALIASES, SOURCE_SPECS, heading_catalog  # noqa: E402


CHATTER = (
    "as an ai",
    "i'd be happy to",
    "i would be happy to",
    "i can't help with",
    "i cannot help with",
    "the user asked",
    "here is the requested",
    "here's the requested",
)


def prose_paragraphs(text: str):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for block in re.split(r"\n\s*\n", text):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines or any(line.startswith(("#", "|", "- ", "* ", ">")) for line in lines):
            continue
        value = " ".join(lines)
        if len(re.findall(r"\b[\w'-]+\b", value)) >= 40:
            yield re.sub(r"\s+", " ", value).strip()


def main() -> None:
    errors: list[str] = []
    catalog = heading_catalog(ROOT)
    anchors = {record.anchor for records in catalog.values() for record in records}
    anchors.update(DESTINATION_ALIASES)
    paragraph_sources: defaultdict[str, set[str]] = defaultdict(set)
    total_words = 0
    total_links = 0

    for spec in SOURCE_SPECS:
        path = ROOT / spec.filename
        text = path.read_text(encoding="utf-8")
        total_words += len(re.findall(r"\b[\w'-]+\b", text))
        if text.count("```") % 2:
            errors.append(f"unbalanced code fence: {spec.filename}")

        local_heading_titles: Counter[tuple[int, str]] = Counter(
            (record.level, record.title.casefold())
            for record in catalog[spec.filename]
            if record.level <= 2
        )
        for (level, title), count in local_heading_titles.items():
            if count > 1:
                errors.append(f"repeated H{level} heading {title!r} in {spec.filename}")

        for target in re.findall(r"\]\(#([^)]+)\)", text):
            total_links += 1
            if target not in anchors and target not in DESTINATION_ALIASES.values():
                errors.append(f"unknown internal target #{target} in {spec.filename}")

        lowered = text.casefold()
        for phrase in CHATTER:
            if phrase in lowered:
                errors.append(f"drafting phrase {phrase!r} in {spec.filename}")

        for paragraph in prose_paragraphs(text):
            paragraph_sources[paragraph].add(spec.filename)

    duplicate_groups = {
        paragraph: files for paragraph, files in paragraph_sources.items() if len(files) > 1
    }
    if duplicate_groups:
        for paragraph, files in list(duplicate_groups.items())[:10]:
            errors.append(
                f"cross-document duplicate in {', '.join(sorted(files))}: {paragraph[:100]}"
            )

    json_files = sorted((ROOT / "website").glob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {path.name}: {exc}")

    print(
        json.dumps(
            {
                "documents": len(SOURCE_SPECS),
                "headings": sum(len(records) for records in catalog.values()),
                "words": total_words,
                "internal_links_checked": total_links,
                "cross_document_duplicate_groups_40_words": len(duplicate_groups),
                "json_files_checked": len(json_files),
                "errors": errors,
            },
            indent=2,
        )
    )
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
