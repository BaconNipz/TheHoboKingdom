#!/usr/bin/env python3
"""Build website-ready indexes and data exports from the reader corpus."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
sys.path.insert(0, str(ROOT))

from navigation import (  # noqa: E402
    DESTINATION_ALIASES,
    SOURCE_SPECS,
    heading_catalog,
)


EDITION = {
    "name": "Progress Edition 30",
    "status": "review",
    "published_on": None,
    "last_edited": "2026-09-14",
    "source_verified_on": "2026-09-14",
    "game_baseline": "Dominions 6.37",
    "mod_baselines": ["Dominions Enhanced 2.16", "Divinitus 1.15.3 DE"],
    "combined_load_order": ["Dominions Enhanced 2.16", "Divinitus 1.15.3 DE"],
}

NATION_DOSSIER_RANGES = [
    {
        "start": "b7-part-ii-middle-age-arcoscephale-the-old-kingdom",
        "end": "b7-part-xvi-middle-age-marignon-fiery-justice",
        "tags": ["nations", "nation-arcoscephale", "age-middle"],
        "rulesets": [],
    },
    {
        "start": "b7-part-xvi-middle-age-marignon-fiery-justice",
        "end": "b7-part-xvii-middle-age-pyrene-time-of-the-akelarre",
        "tags": ["nations", "nation-marignon", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xvii-middle-age-pyrene-time-of-the-akelarre",
        "end": "b7-part-xviii-middle-age-ulm-forges-of-ulm",
        "tags": ["nations", "nation-pyrene", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xviii-middle-age-ulm-forges-of-ulm",
        "end": "b7-part-xix-middle-age-man-tower-of-avalon",
        "tags": ["nations", "nation-ulm", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xix-middle-age-man-tower-of-avalon",
        "end": "b7-part-xx-middle-age-abysia-blood-and-fire",
        "tags": ["nations", "nation-man", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xx-middle-age-abysia-blood-and-fire",
        "end": "b7-part-xxi-middle-age-pythium-emerald-empire",
        "tags": ["nations", "nation-abysia", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxi-middle-age-pythium-emerald-empire",
        "end": "b7-part-xxii-middle-age-eriu-last-of-the-tuatha",
        "tags": ["nations", "nation-pythium", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxii-middle-age-eriu-last-of-the-tuatha",
        "end": "b7-part-xxiii-middle-age-agartha-golem-cult",
        "tags": ["nations", "nation-eriu", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxiii-middle-age-agartha-golem-cult",
        "end": "b7-part-xxiv-middle-age-uruk-city-states",
        "tags": ["nations", "nation-agartha", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxiv-middle-age-uruk-city-states",
        "end": "b7-part-xxv-middle-age-ashdod-reign-of-the-anakim",
        "tags": ["nations", "nation-uruk", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxv-middle-age-ashdod-reign-of-the-anakim",
        "end": "b7-part-xxvi-middle-age-t-ien-ch-i-imperial-bureaucracy",
        "tags": ["nations", "nation-ashdod", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxvi-middle-age-t-ien-ch-i-imperial-bureaucracy",
        "end": "b7-part-xxvii-middle-age-machaka-reign-of-sorcerors",
        "tags": ["nations", "nation-tien-chi", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxvii-middle-age-machaka-reign-of-sorcerors",
        "end": "b7-part-xxviii-middle-age-shinuyama-land-of-the-bakemono",
        "tags": ["nations", "nation-machaka", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxviii-middle-age-shinuyama-land-of-the-bakemono",
        "end": "b7-part-xxix-middle-age-c-tis-miasma",
        "tags": ["nations", "nation-shinuyama", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxix-middle-age-c-tis-miasma",
        "end": "b7-part-xxx-middle-age-pangaea-age-of-bronze",
        "tags": ["nations", "nation-ctis", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxx-middle-age-pangaea-age-of-bronze",
        "end": "b7-part-xxxi-middle-age-vanheim-arrival-of-man",
        "tags": ["nations", "nation-pangaea", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxxi-middle-age-vanheim-arrival-of-man",
        "end": "b7-part-xxxii-middle-age-caelum-reign-of-the-seraphim",
        "tags": ["nations", "nation-vanheim", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
    {
        "start": "b7-part-xxxii-middle-age-caelum-reign-of-the-seraphim",
        "end": "b7-part-xxxiii-middle-age-phlegra-deformed-giants",
        "tags": ["nations", "nation-caelum", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    },
]

_REMAINING_MA_RANGES = [
    ("b7-part-xxxiii-middle-age-phlegra-deformed-giants", "b7-part-xxxiv-middle-age-asphodel-carrion-woods", "phlegra"),
    ("b7-part-xxxiv-middle-age-asphodel-carrion-woods", "b7-part-xxxv-middle-age-ermor-ashen-empire", "asphodel"),
    ("b7-part-xxxv-middle-age-ermor-ashen-empire", "b7-part-xxxvi-middle-age-sceleria-the-reformed-empire", "ermor"),
    ("b7-part-xxxvi-middle-age-sceleria-the-reformed-empire", "b7-part-xxxvii-middle-age-na-ba-queens-of-the-desert", "sceleria"),
    ("b7-part-xxxvii-middle-age-na-ba-queens-of-the-desert", "b7-part-xxxviii-middle-age-ind-magnificent-kingdom-of-exalted-virtue", "na-ba"),
    ("b7-part-xxxviii-middle-age-ind-magnificent-kingdom-of-exalted-virtue", "b7-part-xxxix-middle-age-bandar-log-land-of-the-apes", "ind"),
    ("b7-part-xxxix-middle-age-bandar-log-land-of-the-apes", "b7-part-xl-middle-age-nazca-kingdom-of-the-sun", "bandar-log"),
    ("b7-part-xl-middle-age-nazca-kingdom-of-the-sun", "b7-part-xli-middle-age-mictlan-reign-of-the-lawgiver", "nazca"),
    ("b7-part-xli-middle-age-mictlan-reign-of-the-lawgiver", "b7-part-xlii-middle-age-xibalba-flooded-caves", "mictlan"),
    ("b7-part-xlii-middle-age-xibalba-flooded-caves", "b7-part-xliii-middle-age-phaeacia-isle-of-the-dark-ships", "xibalba"),
    ("b7-part-xliii-middle-age-phaeacia-isle-of-the-dark-ships", "b7-part-xliv-middle-age-vanarus-land-of-the-chuds", "phaeacia"),
    ("b7-part-xliv-middle-age-vanarus-land-of-the-chuds", "b7-part-xlv-middle-age-jotunheim-iron-woods", "vanarus"),
    ("b7-part-xlv-middle-age-jotunheim-iron-woods", "b7-part-xlvi-middle-age-nidavangr-bear-wolf-and-crow", "jotunheim"),
    ("b7-part-xlvi-middle-age-nidavangr-bear-wolf-and-crow", "b7-part-xlvii-middle-age-ys-morgen-queens", "nidavangr"),
    ("b7-part-xlvii-middle-age-ys-morgen-queens", "b7-part-xlviii-middle-age-pelagia-triton-kings", "ys"),
    ("b7-part-xlviii-middle-age-pelagia-triton-kings", "b7-part-xlix-middle-age-oceania-mermidons", "pelagia"),
    ("b7-part-xlix-middle-age-oceania-mermidons", "b7-part-l-middle-age-atlantis-kings-of-the-deep", "oceania"),
    ("b7-part-l-middle-age-atlantis-kings-of-the-deep", "b7-part-li-middle-age-r-lyeh-fallen-star", "atlantis"),
    ("b7-part-li-middle-age-r-lyeh-fallen-star", "b7-dossier-source-register", "rlyeh"),
]
NATION_DOSSIER_RANGES.extend(
    {
        "start": start,
        "end": end,
        "tags": ["nations", f"nation-{tag}", "age-middle", "ruleset-unmodded"],
        "rulesets": ["dom6-6.37-unmodded"],
    }
    for start, end, tag in _REMAINING_MA_RANGES
)

TOPIC_RULES = {
    "timing": ["turn", "hosting", "phase", "order", "timing", "resolution"],
    "economy": ["income", "gold", "resource", "recruit", "upkeep", "population"],
    "infrastructure": ["fort", "laboratory", "temple", "construction", "siege"],
    "pretenders": ["pretender", "chassis", "awakening", "call god"],
    "dominion": ["dominion", "candle", "preach", "throne"],
    "scales": ["scale", "order", "turmoil", "growth", "death", "magic", "drain"],
    "blessings": ["bless", "sacred", "incarnate"],
    "combat": ["battle", "melee", "missile", "damage", "protection", "armour"],
    "morale": ["morale", "rout", "retreat", "fear"],
    "fatigue": ["fatigue", "reinvigoration", "encumbrance"],
    "magic": ["magic", "spell", "path", "ritual", "gem", "communion", "forge"],
    "strategy": ["strategy", "campaign", "expansion", "raid", "diplomacy", "war"],
    "nations": ["nation", "arcoscephale", "marignon", "pyrène", "pyrene", "mystic", "astrologer", "witch hunter", "grand master", "sorgina", "akerbeltz", "tower of avalon", "mother of avalon", "crone of avalon", "logrian wise man", "abysia", "abysian", "warlock", "smouldercone", "salamander", "rhuax", "hellscape", "infernal breeding", "o'al kan", "pythium", "pythian", "theurg", "arch theurg", "communicant", "cathedral of the spheres", "swamps of pythia", "serpent cataphract", "grand communion", "contact lar", "angelic choir", "eriu", "milesian", "fir bolg", "bean sidhe", "sidhe lord", "tuatha", "daoine sidhe", "mound of ancient kings", "summon cu sidhe", "gossamer cloth", "singing sword", "agartha", "agarthan", "golem cult", "golem crafter", "oracle of the ancients", "roots of the earth", "halls of the oracles", "broken seal", "olm conclave", "attentive statues", "shard wight", "penumbral", "umbral", "machaka", "sorcerer", "spider sorceress", "black sorcerer", "anansi", "bane spider", "god forest", "god mountain", "god brood", "weavers of the wood", "shinuyama", "bakemono", "bakemono sorcerer", "uba", "shuten-doji", "noppera-bo", "kappa", "dai bakemono", "mount shinuyama", "summon dai oni", "contact dai tengu", "contact kitsune", "c'tis", "ctis", "c'tissian", "miasma", "marshmaster", "empoisoner", "sobek", "temple marsh", "jade mask", "sacred crocodile", "monster toads", "contact couatl", "contact scorpion man", "pangaea", "pangaean", "pan", "pandemoniac", "dryad", "hierophant", "white centaur", "grove of gaia", "hidden grove", "magical tune", "tune of fear", "tune of growth", "tune of dancing death", "monster boar", "awaken hamadryad", "fort of the ancients", "vanheim", "vanherse", "vanjarl", "vanadrott", "dwarven smith", "halls of andvare", "vanhalla", "fay boar", "valkyrie", "skinshifter", "awaken draugar", "summon valkyries", "four directions"],
    "modding": ["mod", "object", "parser", "event", "map", "ai", "compatibility"],
    "de-divinitus": ["dominions enhanced", "divinitus", "de ", "hierophant"],
    "research-control": ["test", "evidence", "source", "open question", "verification"],
    "operations": ["interface", "shortcut", "setup", "lobby", "submission", "player operations", "troubleshooting"],
    "units-abilities": ["unit class", "ability", "aura", "recovery", "leadership", "movement"],
    "experience-conditions": ["experience", "heroic", "condition", "affliction", "disease", "curse", "horror mark"],
    "base-objects": ["object reference", "spell row", "magic item", "artifact", "summon", "pretender form", "throne", "magic site", "mercenary", "special dominion"],
    "patch-history": ["patch", "version history", "release", "chronology", "stale guide", "update announcement"],
    "command-lexicon": ["command", "syntax", "template", "manual locator", "message substitution", "documentation status"],
}

TOPIC_RULES["nations"].extend([
    "caelum", "caelian", "seraphine", "high seraph", "ice crafter", "spire horn",
    "citadel of frozen crystal", "ravens vale", "guardian spirit", "ice fort",
    "blizzard warrior", "parting of the soul", "ahurani", "yazata", "daeva", "drugvant",
])
TOPIC_RULES["nations"].extend([
    "phlegra", "asphodel", "ermor", "sceleria", "na'ba", "ind", "bandar log",
    "nazca", "mictlan", "xibalba", "phaeacia", "vanarus", "jotunheim",
    "nidavangr", "ys", "pelagia", "oceania", "atlantis", "r'lyeh",
])


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def topics(title: str) -> list[str]:
    lowered = f" {title.lower()} "
    result = [topic for topic, words in TOPIC_RULES.items() if any(word in lowered for word in words)]
    return result or ["general"]


def audience(title: str) -> list[str]:
    lowered = title.lower()
    result = []
    if any(word in lowered for word in ["new player", "plain language", "first", "basic"]):
        result.append("beginner")
    if any(word in lowered for word in ["expert", "formula", "exact", "audit", "test", "source"]):
        result.append("expert")
    return result or ["all"]


def section_word_counts(path: Path, records) -> dict[str, int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    counts: dict[str, int] = {}
    for index, record in enumerate(records):
        end = len(lines)
        for later in records[index + 1 :]:
            if later.level <= record.level:
                end = later.line - 1
                break
        body = "\n".join(lines[record.line:end])
        body = re.sub(r"[`*#>|\[\](){}]", " ", body)
        counts[record.anchor] = len(re.findall(r"\b[\w'-]+\b", body))
    return counts


def nation_metadata(record, records) -> tuple[list[str], list[str]]:
    """Return dossier-specific tags and rulesets for a Book VII heading."""
    ordinal_by_anchor = {item.anchor: item.ordinal for item in records}
    for dossier in NATION_DOSSIER_RANGES:
        start = ordinal_by_anchor.get(dossier["start"])
        end = ordinal_by_anchor.get(dossier["end"])
        if start is None or end is None:
            raise ValueError(
                f"Missing nation-dossier range boundary: {dossier['start']} -> {dossier['end']}"
            )
        if start <= record.ordinal < end:
            return list(dossier["tags"]), list(dossier["rulesets"])
    return [], []


def build_content_index(catalog):
    specs = {spec.filename: spec for spec in SOURCE_SPECS}
    aliases_for_target: dict[str, list[str]] = defaultdict(list)
    for alias, target in DESTINATION_ALIASES.items():
        aliases_for_target[target].append(alias)
    documents = []
    sections = []
    for order, spec in enumerate(SOURCE_SPECS, 1):
        path = ROOT / spec.filename
        records = catalog.get(spec.filename, [])
        counts = section_word_counts(path, records)
        documents.append(
            {
                "id": spec.code,
                "title": spec.label,
                "source_file": spec.filename,
                "website_path": spec.website_path,
                "display_order": order,
                "section_count": len(records),
                "word_count": len(re.findall(r"\b[\w'-]+\b", path.read_text(encoding="utf-8"))),
            }
        )
        for record in records:
            section_topics = topics(record.title)
            section_rulesets: list[str] = []
            if spec.code == "b7":
                extra_topics, section_rulesets = nation_metadata(record, records)
                section_topics = list(dict.fromkeys(section_topics + extra_topics))
            sections.append(
                {
                    "id": record.anchor,
                    "title": record.title,
                    "document_id": spec.code,
                    "source_file": record.source_file,
                    "source_line": record.line,
                    "heading_level": record.level,
                    "display_order": record.ordinal,
                    "parent_id": record.parent_anchor,
                    "website_url": f"{spec.website_path}#{record.anchor}",
                    "pdf_destination": record.anchor,
                    "aliases": sorted(aliases_for_target.get(record.anchor, [])),
                    "topics": section_topics,
                    "audience": audience(record.title),
                    "rulesets": section_rulesets,
                    "evidence_status": [],
                    "related_section_ids": [],
                    "word_count": counts[record.anchor],
                    "last_edited": EDITION["last_edited"],
                    "last_verified": None,
                }
            )
    return {
        "schema_version": "1.0.0",
        "edition": EDITION,
        "documents": documents,
        "sections": sections,
    }


def marked_table(text: str, name: str) -> list[list[str]]:
    match = re.search(
        rf"<!-- DATA:BEGIN {re.escape(name)} -->(.*?)<!-- DATA:END {re.escape(name)} -->",
        text,
        re.S,
    )
    if not match:
        raise ValueError(f"Missing marked table: {name}")
    rows = []
    for line in match.group(1).splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def build_glossary(guide_text: str):
    rows = marked_table(guide_text, "glossary")
    header = rows[0]
    expected = ["Term", "Working definition", "Primary anchor", "Related anchors"]
    if header != expected:
        raise ValueError(f"Unexpected glossary columns: {header}")
    return {
        "schema_version": "1.0.0",
        "edition": EDITION["name"],
        "entries": [
            {
                "term": row[0],
                "definition": row[1],
                "primary_section_id": row[2],
                "related_section_ids": [x.strip() for x in row[3].split(";") if x.strip()],
                "aliases": [],
            }
            for row in rows[1:]
        ],
    }


def build_research_register(guide_text: str):
    rows = marked_table(guide_text, "research")
    header = rows[0]
    expected = [
        "ID",
        "Priority",
        "Domain",
        "Question",
        "Why it matters",
        "Reliable route",
        "Primary anchor",
        "Status",
    ]
    if header != expected:
        raise ValueError(f"Unexpected research columns: {header}")
    items = []
    for row in rows[1:]:
        items.append(
            {
                "id": row[0],
                "priority": row[1],
                "domain": row[2],
                "question": row[3],
                "why_it_matters": row[4],
                "reliable_resolution_route": row[5],
                "primary_section_id": row[6],
                "status": row[7],
                "requires_player_testing": False,
            }
        )
    return {
        "schema_version": "1.0.0",
        "edition": EDITION["name"],
        "priority_order": ["P0", "P1", "P2", "P3"],
        "items": items,
    }


def build_ability_register(book_text: str):
    rows = marked_table(book_text, "abilities")
    expected = [
        "Name",
        "Category",
        "Core function",
        "Principal caveat or counter",
        "Evidence",
        "Primary anchor",
    ]
    if rows[0] != expected:
        raise ValueError(f"Unexpected ability-register columns: {rows[0]}")
    evidence_map = {
        "OM": "official-manual",
        "MM": "official-mod-manual",
        "OP": "official-patch",
        "UI": "current-ui-check",
        "CT": "community-tested",
        "D": "derived",
        "TP": "test-pending",
    }
    records = []
    for index, row in enumerate(rows[1:], 1):
        codes = [code.strip() for code in row[4].split(",") if code.strip()]
        unknown = set(codes) - set(evidence_map)
        if unknown:
            raise ValueError(f"Unknown ability evidence codes: {sorted(unknown)}")
        records.append(
            {
                "id": f"ability-{index:03d}",
                "name": row[0],
                "category": row[1],
                "core_function": row[2],
                "principal_caveat_or_counter": row[3],
                "evidence": [evidence_map[code] for code in codes],
                "primary_section_id": row[5],
                "game_baseline": EDITION["game_baseline"],
                "verified_on": EDITION["source_verified_on"] if "CT" not in codes and "TP" not in codes else None,
            }
        )
    return {
        "schema_version": "1.0.0",
        "edition": EDITION["name"],
        "game_baseline": EDITION["game_baseline"],
        "evidence_key": evidence_map,
        "records": records,
    }


def build_reading_paths(guide_text: str):
    part = re.search(r"# Part I: Reading Paths\n(.*?)\n# Part II:", guide_text, re.S)
    if not part:
        raise ValueError("Reading-path section not found")
    blocks = re.split(r"(?=^## Path [A-Z]:)", part.group(1), flags=re.M)
    paths = []
    for block in blocks:
        heading = re.match(r"^## (Path ([A-Z]):[^\n]+)", block)
        if not heading:
            continue
        title = heading.group(1)
        code = heading.group(2)
        prose = re.sub(r"\n\|.*", "", block.split("\n\n", 2)[1] if "\n\n" in block else "").strip()
        seen = set()
        steps = []
        for label, anchor in re.findall(r"\[([^\]]+)\]\(#([A-Za-z0-9_.:-]+)\)", block):
            if anchor in seen:
                continue
            seen.add(anchor)
            steps.append({"label": label, "section_id": anchor})
        paths.append(
            {
                "id": f"path-{code.lower()}",
                "title": title,
                "summary": prose,
                "steps": steps,
            }
        )
    return {"schema_version": "1.0.0", "edition": EDITION["name"], "paths": paths}


def build_subject_index(guide_text: str):
    part = re.search(
        r"# Part III: Alphabetical Subject Concordance\n(.*?)\n# Part IV:",
        guide_text,
        re.S,
    )
    if not part:
        raise ValueError("Subject concordance not found")
    letter = None
    entries = []
    for line in part.group(1).splitlines():
        h = re.match(r"## ([A-Z])$", line)
        if h:
            letter = h.group(1)
            continue
        item = re.match(r"- \*\*([^*]+):\*\*\s+(.+)$", line)
        if not item:
            continue
        links = re.findall(r"\[([^\]]+)\]\(#([A-Za-z0-9_.:-]+)\)", item.group(2))
        entries.append(
            {
                "letter": letter,
                "term": item.group(1),
                "destinations": [
                    {"label": label, "section_id": anchor} for label, anchor in links
                ],
            }
        )
    return {"schema_version": "1.0.0", "edition": EDITION["name"], "entries": entries}


def schema_document():
    evidence = [
        "official",
        "source-confirmed",
        "reproduced",
        "community-tested",
        "derived",
        "strategic-doctrine",
        "test-pending",
    ]
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://thehobokingdom.com/schemas/dominions-library-content.schema.json",
        "title": "TheHoboKingdom Dominions 6 Library Content",
        "description": "Versioned articles, sections, claims, formulas, sources, and navigation for the Dominions 6 Knowledge Library.",
        "type": "object",
        "required": ["schema_version", "article"],
        "properties": {
            "schema_version": {"type": "string"},
            "article": {"$ref": "#/$defs/article"},
        },
        "additionalProperties": False,
        "$defs": {
            "ruleset_scope": {
                "type": "object",
                "required": ["game", "game_version", "mods"],
                "properties": {
                    "game": {"const": "Dominions 6"},
                    "game_version": {"type": "string"},
                    "mods": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["name", "version", "load_order"],
                            "properties": {
                                "name": {"type": "string"},
                                "version": {"type": "string"},
                                "load_order": {"type": "integer", "minimum": 1},
                                "sha256": {"type": ["string", "null"], "pattern": "^[0-9a-f]{64}$"},
                            },
                            "additionalProperties": False,
                        },
                    },
                    "map": {"type": ["string", "null"]},
                    "age": {"enum": ["EA", "MA", "LA", "mixed", None]},
                    "notes": {"type": ["string", "null"]},
                },
                "additionalProperties": False,
            },
            "source": {
                "type": "object",
                "required": ["id", "title", "kind"],
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "kind": {"enum": ["official-manual", "official-patch", "game-data", "mod-source", "published-reproduction", "community-reference", "derived-work"]},
                    "url": {"type": ["string", "null"], "pattern": "^https?://"},
                    "version": {"type": ["string", "null"]},
                    "accessed_on": {"type": ["string", "null"], "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "locator": {"type": ["string", "null"]},
                    "sha256": {"type": ["string", "null"], "pattern": "^[0-9a-f]{64}$"},
                },
                "additionalProperties": False,
            },
            "claim": {
                "type": "object",
                "required": ["id", "text", "evidence_status", "ruleset_ids", "source_ids"],
                "properties": {
                    "id": {"type": "string"},
                    "text": {"type": "string"},
                    "evidence_status": {"enum": evidence},
                    "ruleset_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                    "source_ids": {"type": "array", "items": {"type": "string"}},
                    "derivation": {"type": ["string", "null"]},
                    "confidence_note": {"type": ["string", "null"]},
                    "verified_on": {"type": ["string", "null"], "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "supersedes_claim_id": {"type": ["string", "null"]},
                    "research_question_ids": {"type": "array", "items": {"type": "string"}},
                },
                "additionalProperties": False,
            },
            "content_block": {
                "type": "object",
                "required": ["id", "type"],
                "properties": {
                    "id": {"type": "string"},
                    "type": {"enum": ["prose", "callout", "formula", "table", "list", "worked-example", "checklist", "quotation", "source-note", "research-question"]},
                    "markdown": {"type": ["string", "null"]},
                    "claim_ids": {"type": "array", "items": {"type": "string"}},
                    "caption": {"type": ["string", "null"]},
                    "formula": {
                        "type": ["object", "null"],
                        "properties": {
                            "expression": {"type": "string"},
                            "variables": {"type": "array", "items": {"type": "object"}},
                            "rounding": {"type": ["string", "null"]},
                            "units": {"type": ["string", "null"]},
                        },
                        "additionalProperties": False,
                    },
                    "data": {
                        "anyOf": [
                            {"type": "array"},
                            {"type": "object"},
                            {"type": "null"},
                        ]
                    },
                },
                "additionalProperties": False,
            },
            "section": {
                "type": "object",
                "required": ["id", "title", "slug", "order", "audience", "topic_tags", "blocks"],
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "short_title": {"type": ["string", "null"]},
                    "slug": {"type": "string"},
                    "order": {"type": "integer"},
                    "audience": {"type": "array", "items": {"enum": ["beginner", "intermediate", "expert", "modder", "all"]}},
                    "topic_tags": {"type": "array", "items": {"type": "string"}},
                    "ruleset_ids": {"type": "array", "items": {"type": "string"}},
                    "related_section_ids": {"type": "array", "items": {"type": "string"}},
                    "aliases": {"type": "array", "items": {"type": "string"}},
                    "blocks": {"type": "array", "items": {"$ref": "#/$defs/content_block"}},
                },
                "additionalProperties": False,
            },
            "article": {
                "type": "object",
                "required": ["id", "title", "slug", "status", "rulesets", "sources", "claims", "sections", "created_on", "last_edited"],
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": ["string", "null"]},
                    "slug": {"type": "string"},
                    "status": {"enum": ["draft", "review", "published", "deprecated"]},
                    "rulesets": {"type": "array", "items": {"$ref": "#/$defs/ruleset_scope"}},
                    "sources": {"type": "array", "items": {"$ref": "#/$defs/source"}},
                    "claims": {"type": "array", "items": {"$ref": "#/$defs/claim"}},
                    "sections": {"type": "array", "items": {"$ref": "#/$defs/section"}},
                    "created_on": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "last_edited": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "last_verified": {"type": ["string", "null"], "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "supersedes_article_id": {"type": ["string", "null"]},
                },
                "additionalProperties": False,
            },
        },
    }


def validate_references(catalog, *datasets) -> None:
    actual = {record.anchor for records in catalog.values() for record in records}
    valid = actual | set(DESTINATION_ALIASES)
    bad_alias_targets = set(DESTINATION_ALIASES.values()) - actual
    if bad_alias_targets:
        raise ValueError(f"Alias targets do not exist: {sorted(bad_alias_targets)}")
    references = set()
    for dataset in datasets:
        if "entries" in dataset:
            for entry in dataset["entries"]:
                references.add(entry.get("primary_section_id", ""))
                references.update(entry.get("related_section_ids", []))
                references.update(x.get("section_id", "") for x in entry.get("destinations", []))
        if "items" in dataset:
            references.update(item["primary_section_id"] for item in dataset["items"])
        if "paths" in dataset:
            for path in dataset["paths"]:
                references.update(step["section_id"] for step in path["steps"])
        if "records" in dataset:
            references.update(record["primary_section_id"] for record in dataset["records"])
    missing = sorted(reference for reference in references if reference and reference not in valid)
    if missing:
        raise ValueError(f"Unresolved section references: {missing}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=WEBSITE,
        help="Directory for generated JSON exports (default: website/).",
    )
    parser.add_argument(
        "--draft-name",
        help="Label exports as an unpublished working draft with this edition name.",
    )
    parser.add_argument(
        "--edited-on",
        help="ISO date for a draft rebuild; required with --draft-name.",
    )
    return parser.parse_args()


def main() -> None:
    global WEBSITE
    args = parse_args()
    WEBSITE = args.output_dir.resolve()
    if bool(args.draft_name) != bool(args.edited_on):
        raise ValueError("--draft-name and --edited-on must be supplied together")
    if args.edited_on and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.edited_on):
        raise ValueError("--edited-on must use YYYY-MM-DD")
    if args.draft_name:
        baseline = {
            "name": EDITION["name"],
            "published_on": EDITION["published_on"],
        }
        EDITION.update(
            {
                "name": args.draft_name,
                "status": "draft",
                "published_on": None,
                "last_edited": args.edited_on,
                "based_on": baseline,
            }
        )

    catalog = heading_catalog(ROOT)
    guide_text = (ROOT / "16-reader-guide-concordance.md").read_text(encoding="utf-8")
    content_index = build_content_index(catalog)
    glossary = build_glossary(guide_text)
    research = build_research_register(guide_text)
    reading_paths = build_reading_paths(guide_text)
    subject_index = build_subject_index(guide_text)
    ability_book_text = (ROOT / "21-foundation-book-xi-unit-ability-reference.md").read_text(encoding="utf-8")
    ability_register = build_ability_register(ability_book_text)
    validate_references(catalog, glossary, research, reading_paths, subject_index, ability_register)

    dump(WEBSITE / "content.schema.json", schema_document())
    dump(
        WEBSITE / "article-template.json",
        {
            "schema_version": "1.0.0",
            "article": {
                "id": "replace-me",
                "title": "Replace Me",
                "description": None,
                "slug": "replace-me",
                "status": "draft",
                "rulesets": [
                    {
                        "game": "Dominions 6",
                        "game_version": "6.37",
                        "mods": [],
                        "map": None,
                        "age": "mixed",
                        "notes": None,
                    }
                ],
                "sources": [],
                "claims": [],
                "sections": [],
                "created_on": EDITION["last_edited"],
                "last_edited": EDITION["last_edited"],
                "last_verified": None,
                "supersedes_article_id": None,
            },
        },
    )
    dump(WEBSITE / "content-index.json", content_index)
    dump(WEBSITE / "glossary.json", glossary)
    dump(WEBSITE / "reading-paths.json", reading_paths)
    dump(WEBSITE / "research-register.json", research)
    dump(WEBSITE / "subject-index.json", subject_index)
    dump(WEBSITE / "ability-register.json", ability_register)
    dump(
        WEBSITE / "redirects.json",
        {
            "schema_version": "1.0.0",
            "edition": EDITION["name"],
            "redirects": [
                {"from": alias, "to": target}
                for alias, target in sorted(DESTINATION_ALIASES.items())
            ],
        },
    )
    print(
        json.dumps(
            {
                "edition": EDITION["name"],
                "status": EDITION["status"],
                "output_dir": str(WEBSITE),
                "documents": len(content_index["documents"]),
                "sections": len(content_index["sections"]),
                "glossary_entries": len(glossary["entries"]),
                "reading_paths": len(reading_paths["paths"]),
                "research_items": len(research["items"]),
                "subject_entries": len(subject_index["entries"]),
                "ability_records": len(ability_register["records"]),
                "redirects": len(DESTINATION_ALIASES),
            }
        )
    )


if __name__ == "__main__":
    main()
