#!/usr/bin/env python3
"""Build the versioned Dominions 6 official patch ledger.

The public output does not reproduce the official announcements. It records one
derived classification per official bullet, a source locator, hashes, affected
domains, canonical homes, commands, named terms, and a concise impact summary.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
API_URL = (
    "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
    "?appid=2511500&count=100&maxlength=0&format=json"
)
BASELINE = "6.36"
EDITION = "Progress Edition 27"
GENERATED_ON = "2026-08-28"


CLASS_LABELS = {
    "content_addition": "Content addition",
    "balance_change": "Balance adjustment",
    "rules_change": "Rule or permission change",
    "bug_fix": "Bug correction",
    "interface_qol": "Interface or quality-of-life change",
    "artificial_intelligence": "AI behaviour change",
    "performance_stability": "Performance or stability change",
    "network_hosting": "Network or hosting change",
    "mod_command_addition": "Mod-command addition",
    "modding_change": "Modding behaviour change",
    "map_making_change": "Map-making change",
    "presentation": "Graphics, audio, text, or presentation change",
    "data_correction": "Statistics or data correction",
    "security_integrity": "Security or integrity correction",
}


DOMAIN_RULES = {
    "economy": ["income", "gold", "resource", "upkeep", "supply", "population", "tax", "unrest", "pillage"],
    "recruitment": ["recruit", "commander point", "holy point", "fort defence", "province defence", " pd "],
    "pretenders": ["pretender", "god cost", "awakening", "call god", "twiceborn"],
    "dominion_blessings": ["dominion", "bless", "sacred", "prophet", "preach", "temple", "candle"],
    "combat": ["battle", "damage", "weapon", "armor", "armour", "shield", "attack", "defence", "defense", "rout", "retreat", "morale", "fatigue", "trample", "repel"],
    "magic_spells": ["spell", "ritual", "global enchantment", "magic path", "communion", "gem", "blood slave", "dome", "magic duel", "cast"],
    "items_artifacts": ["item", "artifact", "barding", "treasury", "forge"],
    "summons_transformations": ["summon", "shape", "transform", "rebirth", "reanimation", "life after death", "mount", "rider"],
    "sites_thrones": ["site", "throne", "ascension point", " ap "],
    "movement_logistics": ["map move", "movement", "sailing", "teleport", "gateway", "faery trod", "terrain", "underwater", "cave", "indoors"],
    "multiplayer_diplomacy": ["nap", "diplomacy", "disciple", "team", "allied", "arena"],
    "operations_interface": ["screen", "popup", "message", "shortcut", "key ", "ctrl", "alt+", "display", "overview", "tooltip", "icon", "filter", "right-click", "click"],
    "hosting_network": ["host", "network", "lobby", "server", "turn file", "upload", "download", "multiplayer"],
    "artificial_intelligence": [" ai ", "spell ai", "aibad", "computer player"],
    "units_abilities_conditions": ["ability", "affliction", "disease", "poison", "sleep", "curse", "horror mark", "regeneration", "recuperation", "darkvision", "truesight", "invisibility"],
    "nations_rosters": ["nation", "national", "foreign recruit", "start army", "roster"],
    "events": ["event", "arena", "random event"],
    "modding": ["modding", "mod command", "#", " mod ", "drawsize"],
    "maps_scenarios": ["map making", "map editor", "map generator", "province", "plane", "gate", "cave layer"],
    "performance": ["performance", "faster", "cpu", "memory", "rendering", "loading"],
    "presentation": ["sprite", "graphics", "sound", "music", "text", "typo", "animation", "particle", "look"],
    "security_integrity": ["cheat", "exploit", "corrupt", "illegal", "validation"],
    "research_experience": ["research", " rp ", "experience", " xp ", "heroic"],
}


CANONICAL_HOME = {
    "economy": ["b2-foundation-book-ii-economy-provinces-and-the-machinery-of-state"],
    "recruitment": ["b2-part-iv-resources-and-recruitment"],
    "pretenders": ["b3-part-i-pretender-design-as-a-national-system", "b12-pretenders"],
    "dominion_blessings": ["b3-foundation-book-iii-pretenders-dominion-scales-and-blesses"],
    "combat": ["b4-foundation-book-iv-armies-and-battle"],
    "magic_spells": ["b5-foundation-book-v-magic", "b12-spells"],
    "items_artifacts": ["b5-part-xi-forging-items-and-artifacts", "b12-items"],
    "summons_transformations": ["b5-summoning", "b12-summons"],
    "sites_thrones": ["b12-thrones-sites", "b6-part-xii-thrones-cataclysm-and-endgame-conversion"],
    "movement_logistics": ["b6-part-vi-movement-logistics-and-force-projection"],
    "multiplayer_diplomacy": ["b6-part-xi-diplomacy-treaties-and-reputation"],
    "operations_interface": ["b10-interface"],
    "hosting_network": ["b10-hosting"],
    "artificial_intelligence": ["b6-current-ai-capabilities"],
    "units_abilities_conditions": ["b11-ability-register"],
    "nations_rosters": ["b7-part-i-the-nation-dossier-method"],
    "events": ["b8-part-vii-event-modding-as-a-state-machine"],
    "modding": ["b8-foundation-book-viii-modding-scenario-design-and-system-engineering"],
    "maps_scenarios": ["b8-part-ix-maps-and-scenario-design"],
    "performance": ["b13-performance-and-stability"],
    "presentation": ["b13-presentation-and-data-maintenance"],
    "security_integrity": ["b10-part-x-hosting-as-a-competitive-institution"],
    "research_experience": ["b5-part-iii-research-as-strategic-planning", "b11-experience"],
    "game_objects": ["b12-object-register"],
    "general_gameplay": ["b13-official-patch-ledger"],
}


SUBJECT_TERMS = [
    "Call God", "Province Defence", "Recruitment Points", "Commander Points",
    "Holy Points", "Life after Death", "Ritual of Rebirth", "Arcane Decree",
    "Astral Disruption", "Sea of Ice", "Haunted Forest", "Utterdark",
    "Magic Duel", "Twilight", "Carrion Reanimation", "Blood Vengeance",
    "Fay Royalty", "Regeneration", "Communion", "Dominion", "Pretender",
    "Throne", "Barding", "Mount", "Rider", "Retreat", "Sailing",
]


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def strip_bbcode(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\[url=[^\]]+\](.*?)\[/url\]", r"\1", value, flags=re.I | re.S)
    value = re.sub(r"\[/?[^\]]+\]", " ", value)
    value = value.replace("\u2018", "'").replace("\u2019", "'").replace("\u2013", "-").replace("\u2014", "-")
    return " ".join(value.split())


def parse_sections(contents: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    pattern = re.compile(r"\[b\](.*?)\[/b\]\s*\[list\](.*?)\[/list\]", re.I | re.S)
    for heading, body in pattern.findall(contents):
        bullets = []
        for raw in re.findall(r"\[\*\]\s*(.*?)(?=\[\*\]|$)", body, re.I | re.S):
            cleaned = strip_bbcode(raw)
            if cleaned:
                bullets.append(cleaned)
        sections.append((strip_bbcode(heading), bullets))
    return sections


def classify(text: str, section: str) -> str:
    lowered = f" {text.lower()} "
    section_lower = section.lower()
    if "modding" in section_lower or "map making" in section_lower:
        if re.search(r"\bnew\b.*\bcommand", lowered) or re.search(r"#[a-z0-9_]", lowered):
            return "mod_command_addition" if "new" in lowered else "modding_change"
        if "map" in section_lower and "modding" not in section_lower:
            return "map_making_change"
        return "modding_change"
    if any(word in lowered for word in ["cheat", "exploit", "illegal order", "corrupt"]):
        return "security_integrity"
    if any(word in lowered for word in [" ai ", "spell ai", "aibad", "computer player"]):
        return "artificial_intelligence"
    if any(word in lowered for word in ["crash", "performance", "faster", "cpu usage", "memory leak", "host freeze"]):
        return "performance_stability"
    if any(word in lowered for word in ["network", "lobby", "server", "turn file", "upload", "download"]):
        return "network_hosting"
    if re.search(r"\bnew (nation|unit|units|commander|commanders|hero|heroes|spell|spells|ritual|rituals|item|items|ability|abilities|pretender|pretenders|throne|thrones|site|sites|weapon|weapons|summon|summons|shape|shapes|chassis|music)\b", lowered):
        return "content_addition"
    if any(word in lowered for word in ["stat and typo", "stat & typo", "typo and stat", "stat fixes", "typo fixes"]):
        return "data_correction"
    if any(word in lowered for word in ["sprite", "graphics", "sound", "animation", "particle", "text clipping", "looked", "visual"]):
        return "presentation"
    if any(word in lowered for word in ["screen", "popup", "message", "shortcut", "ctrl-", "ctrl+", "alt+", "icon", "overview", "tooltip", "display", "right-click", "right click", "up/down key", "press '", "filter"]):
        return "interface_qol"
    if any(word in lowered for word in ["fixed", " fix ", "fixes", "didn't", "did not", "couldn't", "could not", "could fail", "could sometime", "inconsistency", "wasn't", "weren't", "was not", "were not", "missing", "wrong", "incorrect", "no longer worked", "was unable", "not able", "duplicate", "were off", "was off", "failing to"]):
        return "bug_fix"
    if re.search(r"\b(cost|price|rate|chance|damage|range|strength|morale|fatigue|size|gold)\b", lowered) and any(
        word in lowered for word in ["increased", "reduced", "cheaper", "expensive", "tweaked", "->", "more", "less"]
    ):
        return "balance_change"
    if any(word in lowered for word in [" now ", " no longer ", " can now ", " cannot ", " immune", "requires", "will always"]):
        return "rules_change"
    return "balance_change"


def domains_for(text: str, section: str, classification: str) -> list[str]:
    lowered = f" {text.lower()} "
    result = [domain for domain, terms in DOMAIN_RULES.items() if any(term in lowered for term in terms)]
    if "modding" in section.lower() and "modding" not in result:
        result.append("modding")
    if "map making" in section.lower() and "maps_scenarios" not in result:
        result.append("maps_scenarios")
    fallback = {
        "performance_stability": "performance",
        "network_hosting": "hosting_network",
        "artificial_intelligence": "artificial_intelligence",
        "presentation": "presentation",
        "security_integrity": "security_integrity",
        "mod_command_addition": "modding",
        "modding_change": "modding",
        "map_making_change": "maps_scenarios",
    }.get(classification)
    if fallback and fallback not in result:
        result.append(fallback)
    if not result:
        terms = extract_terms(text)
        if terms or classification in {"content_addition", "balance_change", "rules_change", "bug_fix", "data_correction"}:
            result.append("game_objects")
        else:
            result.append("general_gameplay")
    return sorted(result)


def classification_confidence(text: str, section: str, classification: str) -> str:
    lowered = f" {text.lower()} "
    if "modding" in section.lower() or "map making" in section.lower():
        return "high"
    signals = [
        " fixed", " fix ", "fixes", "could fail", "inconsistency", " new ", " now ", " no longer ", " cannot ", " can now ",
        " increased", " reduced", " cheaper", " more expensive", " performance", " crash",
        " ai ", " shortcut", " popup", " message", " sprite", " typo", " exploit", " cheat",
    ]
    if any(signal in lowered for signal in signals):
        return "high"
    if classification in {"presentation", "data_correction", "network_hosting", "performance_stability"}:
        return "medium"
    return "editorial-review"


def extract_commands(text: str) -> list[str]:
    return sorted(set(re.findall(r"#[A-Za-z0-9_]+", text)), key=str.lower)


def extract_terms(text: str) -> list[str]:
    terms = {term for term in SUBJECT_TERMS if term.lower() in text.lower()}
    for match in re.findall(r"(?<!#)\b(?:[A-Z][A-Za-z'’-]+(?:\s+|$)){1,5}", text):
        cleaned = " ".join(match.split()).strip(" .,:;()")
        if cleaned and cleaned.lower() not in {"general", "modding", "map making", "new", "fixed", "fix"}:
            terms.add(cleaned)
    return sorted(terms, key=str.lower)[:12]


def object_mentions(text: str) -> list[dict[str, str]]:
    mentions = []
    match = re.search(
        r"\bNew\s+(nation|unit|units|spell|spells|ritual|rituals|magic item|item|items|ability|abilities|pretender|pretenders|throne|thrones|site|sites|summon|summons)\b(?:\s+for\s+[^:]+)?\s*:\s*(.+)$",
        text,
        re.I,
    )
    if not match:
        return mentions
    kind = match.group(1).lower().replace("magic ", "").rstrip("s")
    names = re.split(r",|\s+and\s+|\s*;\s*", match.group(2))
    for name in names:
        cleaned = name.strip(" .")
        if cleaned:
            mentions.append({"kind": kind, "name": cleaned})
    return mentions[:20]


def direction_for(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ["increased", "more expensive", "raised", "larger", "faster"]):
        return "increased-or-expanded"
    if any(word in lowered for word in ["reduced", "cheaper", "lowered", "smaller", "less likely"]):
        return "reduced-or-restricted"
    if any(word in lowered for word in ["no longer", "cannot", "can't", "immune"]):
        return "removed-or-prohibited"
    if any(word in lowered for word in ["can now", "new ", "added", "enabled"]):
        return "added-or-enabled"
    if any(word in lowered for word in ["fixed", " fix", "didn't", "missing", "wrong", "incorrect"]):
        return "corrected"
    return "changed"


def concise_summary(classification: str, domains: list[str], terms: list[str], commands: list[str], direction: str) -> str:
    subjects = commands or terms[:3] or [d.replace("_", " ") for d in domains[:2]]
    subject_text = ", ".join(subjects)
    return f"{CLASS_LABELS[classification]} affecting {subject_text}; direction: {direction}."


def materiality(classification: str, text: str) -> str:
    lowered = text.lower()
    if "new nation" in lowered or any(word in lowered for word in ["exploit", "cheat detection", "host crash", "crash the game"]):
        return "major"
    if classification in {"rules_change", "balance_change", "content_addition", "security_integrity", "network_hosting"}:
        return "notable"
    return "maintenance"


def build(source: dict, source_bytes: bytes) -> dict:
    news = []
    for item in source["appnews"]["newsitems"]:
        match = re.fullmatch(r"Dominions 6\.(\d+)", item.get("title", ""))
        if item.get("feedname") != "steam_community_announcements" or not match:
            continue
        version = f"6.{int(match.group(1)):02d}"
        news.append((int(match.group(1)), version, item))
    news.sort(key=lambda row: (row[0], row[1], str(row[2].get("gid", ""))))

    records = []
    releases = []
    for _, version, item in news:
        sections = parse_sections(item["contents"])
        release_ids = []
        section_counts = Counter()
        class_counts = Counter()
        domain_counts = Counter()
        sequence = 0
        for section, bullets in sections:
            for bullet_index, bullet in enumerate(bullets, 1):
                sequence += 1
                classification = classify(bullet, section)
                domains = domains_for(bullet, section, classification)
                confidence = classification_confidence(bullet, section, classification)
                commands = extract_commands(bullet)
                terms = extract_terms(bullet)
                direction = direction_for(bullet)
                homes = []
                for domain in domains:
                    for home in CANONICAL_HOME.get(domain, []):
                        if home not in homes:
                            homes.append(home)
                if not homes:
                    homes = ["b13-unassigned-review-queue"]
                record_id = f"patch-{version.replace('.', '-')}-{sequence:03d}"
                base = {
                    "id": record_id,
                    "version": version,
                    "published_on": datetime.fromtimestamp(item["date"], timezone.utc).date().isoformat(),
                    "official_section": section,
                    "source_bullet_index": bullet_index,
                    "source_sequence": sequence,
                    "classification": classification,
                    "classification_confidence": confidence,
                    "domains": domains,
                    "materiality": materiality(classification, bullet),
                    "direction": direction,
                    "player_facing": not (classification in {"mod_command_addition", "modding_change", "map_making_change"}),
                    "commands": commands,
                    "named_terms": terms,
                    "object_mentions": object_mentions(bullet),
                    "impact_summary": concise_summary(classification, domains, terms, commands, direction),
                    "canonical_section_ids": ["b13-official-patch-ledger"] + homes,
                    "evidence_status": "official-source-with-derived-classification",
                    "review_status": "mapped" if confidence != "editorial-review" else "mapped-review-recommended",
                    "source_id": f"official-update-{version}",
                    "source_locator": f"{section}, bullet {bullet_index}",
                    "source_text_sha256": sha256_bytes(bullet.encode("utf-8")),
                    "source_word_count": len(re.findall(r"\b[\w#'’-]+\b", bullet)),
                }
                base["record_hash"] = sha256_bytes(canonical_json(base))
                records.append(base)
                release_ids.append(record_id)
                section_counts[section] += 1
                class_counts[classification] += 1
                domain_counts.update(domains)
        release = {
            "version": version,
            "published_on": datetime.fromtimestamp(item["date"], timezone.utc).date().isoformat(),
            "title": item["title"],
            "source_id": f"official-update-{version}",
            "source_url": item["url"],
            "source_gid": item["gid"],
            "source_content_sha256": sha256_bytes(item["contents"].encode("utf-8")),
            "change_records": len(release_ids),
            "record_ids": release_ids,
            "section_counts": dict(sorted(section_counts.items())),
            "classification_counts": dict(sorted(class_counts.items())),
            "leading_domains": [name for name, _ in domain_counts.most_common(8)],
        }
        release["release_hash"] = sha256_bytes(canonical_json(release))
        releases.append(release)

    announced_numbers = {int(v.split(".")[1]) for _, v, _ in news}
    missing_numbers = [f"6.{n:02d}" for n in range(1, int(BASELINE.split(".")[1]) + 1) if n not in announced_numbers]
    class_counts = Counter(record["classification"] for record in records)
    domain_counts = Counter(domain for record in records for domain in record["domains"])
    command_counts = Counter(command for record in records for command in record["commands"])
    confidence_counts = Counter(record["classification_confidence"] for record in records)
    source_manifest = [{
        "id": release["source_id"],
        "title": release["title"],
        "kind": "official-update-announcement",
        "published_on": release["published_on"],
        "url": release["source_url"],
        "gid": release["source_gid"],
        "content_sha256": release["source_content_sha256"],
    } for release in releases]
    result = {
        "schema_version": "1.0.0",
        "edition": EDITION,
        "generated_on": GENERATED_ON,
        "ruleset": {"game": "Dominions 6", "game_version": BASELINE, "mods": []},
        "scope": {
            "description": f"Every bullet in every official Dominions 6 update announcement from 6.01 through {BASELINE}, classified and mapped without reproducing the announcements.",
            "announcement_count": len(releases),
            "change_record_count": len(records),
            "first_version": releases[0]["version"],
            "last_version": releases[-1]["version"],
            "unannounced_version_numbers": missing_numbers,
            "excluded": ["marketing articles", "community comments", "undocumented builds", "full official patch-note text"],
        },
        "evidence_key": {
            "official-source-with-derived-classification": "The source bullet is official; classification, domains, materiality, terms, and canonical links are editorial derivations.",
        },
        "classification_key": CLASS_LABELS,
        "source": {
            "api_endpoint": API_URL,
            "api_response_sha256": sha256_bytes(source_bytes),
            "retrieved_on": GENERATED_ON,
            "announcements": source_manifest,
        },
        "summary": {
            "classification_counts": dict(sorted(class_counts.items())),
            "classification_confidence_counts": dict(sorted(confidence_counts.items())),
            "domain_counts": dict(sorted(domain_counts.items())),
            "unique_commands": len(command_counts),
            "most_repeated_commands": [{"command": command, "records": count} for command, count in command_counts.most_common(20)],
        },
        "releases": releases,
        "records": records,
    }
    return result


def schema_document() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://thehobokingdom.com/schemas/dominions-official-patch-ledger.schema.json",
        "title": "Dominions 6 Official Patch Ledger",
        "type": "object",
        "required": ["schema_version", "edition", "generated_on", "ruleset", "scope", "source", "summary", "releases", "records"],
        "properties": {
            "schema_version": {"const": "1.0.0"},
            "edition": {"type": "string"},
            "generated_on": {"type": "string", "format": "date"},
            "ruleset": {"type": "object"},
            "scope": {"type": "object"},
            "evidence_key": {"type": "object"},
            "classification_key": {"type": "object"},
            "source": {"type": "object"},
            "summary": {"type": "object"},
            "releases": {"type": "array", "items": {"$ref": "#/$defs/release"}},
            "records": {"type": "array", "items": {"$ref": "#/$defs/record"}},
        },
        "additionalProperties": False,
        "$defs": {
            "release": {
                "type": "object",
                "required": ["version", "published_on", "source_url", "source_content_sha256", "change_records", "record_ids", "release_hash"],
                "properties": {
                    "version": {"type": "string", "pattern": "^6\\.\\d{2}$"},
                    "published_on": {"type": "string", "format": "date"},
                    "title": {"type": "string"},
                    "source_id": {"type": "string"},
                    "source_url": {"type": "string", "format": "uri"},
                    "source_gid": {"type": "string"},
                    "source_content_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                    "change_records": {"type": "integer", "minimum": 1},
                    "record_ids": {"type": "array", "items": {"type": "string"}},
                    "section_counts": {"type": "object"},
                    "classification_counts": {"type": "object"},
                    "leading_domains": {"type": "array", "items": {"type": "string"}},
                    "release_hash": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                },
                "additionalProperties": False,
            },
            "record": {
                "type": "object",
                "required": ["id", "version", "published_on", "official_section", "source_sequence", "classification", "classification_confidence", "domains", "materiality", "impact_summary", "canonical_section_ids", "evidence_status", "review_status", "source_id", "source_locator", "source_text_sha256", "record_hash"],
                "properties": {
                    "id": {"type": "string", "pattern": "^patch-6-\\d{2}-\\d{3}$"},
                    "version": {"type": "string", "pattern": "^6\\.\\d{2}$"},
                    "published_on": {"type": "string", "format": "date"},
                    "official_section": {"type": "string"},
                    "source_bullet_index": {"type": "integer", "minimum": 1},
                    "source_sequence": {"type": "integer", "minimum": 1},
                    "classification": {"enum": sorted(CLASS_LABELS)},
                    "classification_confidence": {"enum": ["high", "medium", "editorial-review"]},
                    "domains": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                    "materiality": {"enum": ["major", "notable", "maintenance"]},
                    "direction": {"type": "string"},
                    "player_facing": {"type": "boolean"},
                    "commands": {"type": "array", "items": {"type": "string"}},
                    "named_terms": {"type": "array", "items": {"type": "string"}},
                    "object_mentions": {"type": "array", "items": {"type": "object"}},
                    "impact_summary": {"type": "string"},
                    "canonical_section_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                    "evidence_status": {"const": "official-source-with-derived-classification"},
                    "review_status": {"enum": ["mapped", "mapped-review-recommended"]},
                    "source_id": {"type": "string"},
                    "source_locator": {"type": "string"},
                    "source_text_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                    "source_word_count": {"type": "integer", "minimum": 1},
                    "record_hash": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                },
                "additionalProperties": False,
            },
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-json", type=Path, help="Previously downloaded Steam ISteamNews JSON")
    parser.add_argument(
        "--supplemental-json",
        type=Path,
        action="append",
        default=[],
        help="Additional ISteamNews JSON captured after the primary source snapshot",
    )
    parser.add_argument("--output", type=Path, default=WEBSITE / "official-patch-ledger.json")
    parser.add_argument("--schema", type=Path, default=WEBSITE / "official-patch-ledger.schema.json")
    args = parser.parse_args()

    if args.source_json:
        source_bytes = args.source_json.read_bytes()
    else:
        request = urllib.request.Request(API_URL, headers={"User-Agent": "TheHoboKingdom-Dominions-Research/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            source_bytes = response.read()
    source = json.loads(source_bytes)
    source_parts = [source_bytes]
    known_gids = {item.get("gid") for item in source["appnews"]["newsitems"]}
    known_titles = {item.get("title") for item in source["appnews"]["newsitems"]}
    for supplemental_path in args.supplemental_json:
        supplemental_bytes = supplemental_path.read_bytes()
        supplemental = json.loads(supplemental_bytes)
        source_parts.append(supplemental_bytes)
        for item in supplemental["appnews"]["newsitems"]:
            if item.get("gid") not in known_gids and item.get("title") not in known_titles:
                source["appnews"]["newsitems"].append(item)
                known_gids.add(item.get("gid"))
                known_titles.add(item.get("title"))
    ledger = build(source, b"\n".join(source_parts))

    ids = [record["id"] for record in ledger["records"]]
    assert len(ids) == len(set(ids)) == ledger["scope"]["change_record_count"]
    assert ledger["scope"]["announcement_count"] == 32
    assert ledger["scope"]["change_record_count"] == 1090
    assert ledger["scope"]["unannounced_version_numbers"] == ["6.10", "6.20", "6.22", "6.26"]
    assert all(len(record["record_hash"]) == 64 for record in ledger["records"])
    assert sum(release["change_records"] for release in ledger["releases"]) == len(ledger["records"])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.schema.write_text(json.dumps(schema_document(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "schema": str(args.schema),
        "announcements": len(ledger["releases"]),
        "records": len(ledger["records"]),
        "unannounced_numbers": ledger["scope"]["unannounced_version_numbers"],
    }))


if __name__ == "__main__":
    main()
