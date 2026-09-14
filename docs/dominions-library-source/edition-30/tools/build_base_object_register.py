#!/usr/bin/env python3
"""Build the versioned Dominions 6.35 base-game object register.

The register is a publication layer, not a verbatim mirror.  It preserves
mechanical fields and source identifiers while deliberately excluding the
game's long descriptive prose.  The default source is the public Dominions 6
Data Inspector checkout pinned in the project audit.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = PROJECT_ROOT.parent / "tmp" / "external" / "dom6inspector"
DEFAULT_OUTPUT = PROJECT_ROOT / "website" / "base-object-register.json"
DEFAULT_SCHEMA = PROJECT_ROOT / "website" / "base-object-register.schema.json"

GAME_VERSION = "6.35"
GENERATED_ON = "2026-08-05"
EXPECTED_COMMIT = "cfac4311bc0b58053b8dead7bffbc036ba9bd5dc"

SCHOOLS = {
    -1: "Unresearchable",
    0: "Conjuration",
    1: "Alteration",
    2: "Evocation",
    3: "Construction",
    4: "Enchantment",
    5: "Thaumaturgy",
    6: "Blood",
    7: "Divine",
}
PATHS = {
    -1: None,
    0: "F",
    1: "A",
    2: "W",
    3: "E",
    4: "S",
    5: "D",
    6: "N",
    7: "G",
    8: "B",
    9: "H",
    255: None,
}
PATH_NAMES = {
    "F": "Fire",
    "A": "Air",
    "W": "Water",
    "E": "Earth",
    "S": "Astral",
    "D": "Death",
    "N": "Nature",
    "G": "Glamour",
    "B": "Blood",
    "H": "Holy",
}
ERA_BITS = {1: "EA", 2: "MA", 4: "LA"}

DIRECT_SUMMON_EFFECTS = {1, 21, 26, 31, 37, 38, 43, 50, 93, 119, 137, 141}
SPECIAL_SUMMON_EFFECTS = {76, 89, 100, 114, 120}
ROLE_BY_EFFECT = {
    1: "summon-unit",
    21: "summon-commander",
    26: "rebirth",
    27: "magic-duel",
    28: "control",
    29: "control",
    30: "dispel",
    31: "horror-summon",
    37: "remote-summon",
    38: "remote-summon",
    39: "enlightenment",
    40: "remote-attack",
    43: "battlefield-summon",
    44: "transformation",
    48: "site-search",
    49: "remote-movement",
    50: "remote-assassination",
    53: "remote-attack",
    57: "remote-attack",
    62: "remote-assassination",
    63: "fort-construction",
    64: "disease-attack",
    76: "variable-summon",
    77: "strategic-movement",
    79: "strategic-movement",
    80: "strategic-movement",
    81: "enchantment",
    82: "province-enchantment",
    83: "province-enchantment",
    84: "province-enchantment",
    85: "remote-enchantment",
    86: "remote-enchantment",
    89: "unique-summon",
    91: "remote-attack",
    93: "unique-summon",
    95: "strategic-movement",
    100: "terrain-summon",
    114: "unique-summon",
    120: "variable-summon",
}

SUMMON_GROUPS = {
    "tartarian-gate": [771, 772, 773, 774, 775, 776, 777],
    "yazads": [2620, 2621, 2622, 2623, 2624, 2625],
    "yatas": [2632, 2633, 2634, 2636],
    "dwarfs": [3425, 3426, 3427, 3428],
    "unleash-imprisoned-ones": [2498, 2499, 2500],
    "angelic-host": [465, 543],
    "horde-from-hell": [304, 303],
    "ghost-ship-armada": [3348, 3349, 3350, 3351, 3352],
}
UNIQUE_SUMMONS = {
    1: [306, 821, 822, 823, 824, 825],
    2: [305, 826, 827, 828, 829],
    3: [492, 818, 819, 820],
    4: [906, 469],
    5: [470],
    6: [359, 907, 908],
    7: [563, 911, 912],
    8: [631, 910],
    9: [909],
    10: [446, 810, 900, 1405, 2277, 2278],
    11: [621, 980, 981],
    12: [1375, 1376, 1377, 1492, 1493, 1494],
    13: [1484, 1485, 1486, 1487],
    14: [2063, 2065, 2066, 2067, 2064, 2062],
    15: [],
    16: [2612, 2613, 2614, 2615, 2616, 2617],
    17: [2765, 2768, 2771, 2774],
    18: [2778, 2779, 2780, 2781],
    19: [1019, 1035, 3244, 3245, 3251, 3252, 3253, 3255],
    20: [1748, 3635, 3636],
}
TERRAIN_SUMMONS = {
    1: [1201, 1200, 1202, 1203],
    2: [1979, 1978, 1980, 1981],
    3: [2522, 2523, 2524, 2525],
}

SPELL_CORE_FIELDS = {
    "id", "name", "school", "researchlevel", "path1", "pathlevel1",
    "path2", "pathlevel2", "effect_record_id", "effects_count",
    "precision", "fatiguecost", "gemcost", "next_spell", "damage", "end",
}
ITEM_CORE_FIELDS = {
    "id", "name", "type", "constlevel", "mainpath", "mainlevel",
    "secondarypath", "secondarylevel", "weapon", "armor", "end",
}
UNIT_CORE_FIELDS = {
    "id", "name", "wpn1", "wpn2", "wpn3", "wpn4", "wpn5", "wpn6",
    "wpn7", "armor1", "armor2", "armor3", "armor4", "rt", "reclimit",
    "basecost", "rcost", "size", "ressize", "hp", "prot", "mr", "mor",
    "str", "att", "def", "prec", "enc", "mapmove", "ap", "pathcost",
    "startdom", "bonusspells", "F", "A", "W", "E", "S", "D", "N",
    "G", "B", "H", "rand1", "nbr1", "link1", "mask1", "rand2",
    "nbr2", "link2", "mask2", "rand3", "nbr3", "link3", "mask3",
    "rand4", "nbr4", "link4", "mask4", "rand5", "nbr5", "link5",
    "mask5", "rand6", "nbr6", "link6", "mask6", "minprison", "end",
}
SITE_CORE_FIELDS = {
    "id", "name", "rarity", "loc", "level", "path", "F", "A", "W",
    "E", "S", "D", "N", "G", "B", "F2", "A2", "W2", "E2", "S2",
    "D2", "N2", "B2", "hmon1", "hmon2", "hmon3", "hmon4", "hmon5",
    "hcom1", "hcom2", "hcom3", "hcom4", "hcom5", "mon1", "mon2",
    "mon3", "mon4", "mon5", "com1", "com2", "com3", "com4", "com5",
    "sum1", "n_sum1", "sum2", "n_sum2", "sum3", "n_sum3", "sum4",
    "n_sum4", "end",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--allow-unpinned", action="store_true")
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def integer(value: str | None) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(value)
    except ValueError:
        return None


def scalar(value: str) -> int | float | str:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def sparse(row: dict[str, str], excluded: set[str]) -> dict[str, Any]:
    return {
        key: scalar(value)
        for key, value in row.items()
        if key not in excluded and value not in (None, "")
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_hash(record: dict[str, Any]) -> str:
    payload = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def with_hash(record: dict[str, Any]) -> dict[str, Any]:
    record["record_hash"] = stable_hash(record)
    return record


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True
    ).strip()


def path_requirement(row: dict[str, str]) -> list[dict[str, Any]]:
    result = []
    for path_key, level_key in (("path1", "pathlevel1"), ("path2", "pathlevel2")):
        path_number = integer(row.get(path_key))
        code = PATHS.get(path_number if path_number is not None else -1)
        level = integer(row.get(level_key)) or 0
        if code and level:
            result.append({"path": code, "path_name": PATH_NAMES[code], "level": level})
    return result


def item_path_requirement(row: dict[str, str]) -> list[dict[str, Any]]:
    result = []
    for path_key, level_key in (("mainpath", "mainlevel"), ("secondarypath", "secondarylevel")):
        code = row.get(path_key) or None
        level = integer(row.get(level_key)) or 0
        if code and level:
            result.append({"path": code, "path_name": PATH_NAMES.get(code, code), "level": level})
    return result


def innate_paths(row: dict[str, str]) -> list[dict[str, Any]]:
    return [
        {"path": code, "path_name": PATH_NAMES[code], "level": integer(row[code])}
        for code in PATH_NAMES
        if integer(row.get(code))
    ]


def random_paths(row: dict[str, str]) -> list[dict[str, Any]]:
    result = []
    for index in range(1, 7):
        chance = integer(row.get(f"rand{index}"))
        count = integer(row.get(f"nbr{index}"))
        link = integer(row.get(f"link{index}"))
        mask = integer(row.get(f"mask{index}"))
        if any(value is not None for value in (chance, count, link, mask)):
            result.append(
                {
                    "slot": index,
                    "chance_raw": chance,
                    "draws_raw": count,
                    "linked_raw": link,
                    "path_mask_raw": mask,
                }
            )
    return result


def names_for_units(ids: Iterable[int], unit_lookup: dict[int, dict[str, str]]) -> list[dict[str, Any]]:
    result = []
    for unit_id in ids:
        unit = unit_lookup.get(unit_id)
        result.append({"unit_id": unit_id, "name": unit.get("name") if unit else None})
    return result


def summon_targets(
    root_spell: dict[str, str],
    spell_lookup: dict[int, dict[str, str]],
    effect_lookup: dict[int, dict[str, str]],
) -> tuple[list[int], list[str], list[dict[str, Any]]]:
    targets: list[int] = []
    groups: list[str] = []
    unresolved: list[dict[str, Any]] = []
    seen_spells: set[int] = set()
    current = root_spell

    while current:
        spell_id = integer(current.get("id"))
        if spell_id is None or spell_id in seen_spells:
            break
        seen_spells.add(spell_id)
        effect = effect_lookup.get(integer(current.get("effect_record_id")) or -1)
        if effect:
            effect_number = integer(effect.get("effect_number")) or 0
            argument = integer(effect.get("raw_argument"))
            damage = integer(current.get("damage"))
            argument = damage if damage not in (None, 0) else argument
            if effect_number in DIRECT_SUMMON_EFFECTS and argument is not None:
                if argument > 0:
                    targets.append(argument)
                elif argument == -16:
                    groups.append("yazads")
                    targets.extend(SUMMON_GROUPS["yazads"])
                elif argument == -17:
                    groups.append("yatas")
                    targets.extend(SUMMON_GROUPS["yatas"])
                elif argument == -21:
                    groups.append("dwarfs")
                    targets.extend(SUMMON_GROUPS["dwarfs"])
                elif spell_id == 380:
                    groups.append("angelic-host")
                    targets.extend(SUMMON_GROUPS["angelic-host"])
                elif spell_id == 1081:
                    groups.append("horde-from-hell")
                    targets.extend(SUMMON_GROUPS["horde-from-hell"])
                else:
                    unresolved.append(
                        {
                            "spell_id": spell_id,
                            "effect_number": effect_number,
                            "raw_argument": argument,
                            "reason": "negative monster-tag or engine-selected summon group",
                        }
                    )
            elif effect_number == 76:
                groups.append("tartarian-gate")
                targets.extend(SUMMON_GROUPS["tartarian-gate"])
            elif effect_number == 81 and argument == 43:
                groups.append("ghost-ship-armada")
                targets.extend(SUMMON_GROUPS["ghost-ship-armada"])
            elif effect_number in {89, 114} and argument is not None:
                groups.append(f"unique-summon-{argument}")
                targets.extend(UNIQUE_SUMMONS.get(argument, []))
                if argument not in UNIQUE_SUMMONS or not UNIQUE_SUMMONS[argument]:
                    unresolved.append(
                        {
                            "spell_id": spell_id,
                            "effect_number": effect_number,
                            "raw_argument": argument,
                            "reason": "unique summon table has no resolved unit list",
                        }
                    )
            elif effect_number == 100 and argument is not None:
                groups.append(f"terrain-summon-{argument}")
                targets.extend(TERRAIN_SUMMONS.get(argument, []))
                if argument not in TERRAIN_SUMMONS:
                    unresolved.append(
                        {
                            "spell_id": spell_id,
                            "effect_number": effect_number,
                            "raw_argument": argument,
                            "reason": "terrain summon table has no resolved unit list",
                        }
                    )
            elif effect_number == 120:
                groups.append("unleash-imprisoned-ones")
                targets.extend(SUMMON_GROUPS["unleash-imprisoned-ones"])

        next_id = integer(current.get("next_spell"))
        current = spell_lookup.get(next_id) if next_id else None

    return sorted(set(targets)), sorted(set(groups)), unresolved


def effect_record(
    spell: dict[str, str],
    effect_lookup: dict[int, dict[str, str]],
    effect_names: dict[int, str],
) -> dict[str, Any] | None:
    effect = effect_lookup.get(integer(spell.get("effect_record_id")) or -1)
    if not effect:
        return None
    number = integer(effect.get("effect_number")) or 0
    return {
        "record_id": integer(effect.get("record_id")),
        "effect_number": number,
        "effect_name": effect_names.get(number, f"Unknown effect {number}"),
        "ritual": integer(effect.get("ritual")) == 1,
        "duration_raw": integer(effect.get("duration")),
        "raw_argument": integer(effect.get("raw_argument")),
        "modifiers_mask_raw": integer(effect.get("modifiers_mask")),
        "range_base": integer(effect.get("range_base")),
        "range_per_level": integer(effect.get("range_per_level")),
        "range_strength_divisor": integer(effect.get("range_strength_divisor")),
        "area_base": integer(effect.get("area_base")),
        "area_per_level": integer(effect.get("area_per_level")),
        "area_battlefield_percent": integer(effect.get("area_battlefield_pct")),
    }


def build_spells(
    data: Path,
    unit_lookup: dict[int, dict[str, str]],
    nations: dict[int, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    spells = read_tsv(data / "spells.csv")
    spell_lookup = {integer(row["id"]): row for row in spells}
    effect_rows = read_tsv(data / "effects_spells.csv")
    effect_lookup = {integer(row["record_id"]): row for row in effect_rows}
    effect_names = {
        integer(row["number"]): row["name"]
        for row in read_tsv(data / "effects_info.csv")
        if integer(row["number"]) is not None
    }
    attribute_names = {
        integer(row["number"]): row["name"]
        for row in read_tsv(data / "attribute_keys.csv")
        if integer(row["number"]) is not None
    }
    attributes: dict[int, list[dict[str, Any]]] = defaultdict(list)
    restrictions: dict[int, set[int]] = defaultdict(set)
    for row in read_tsv(data / "attributes_by_spell.csv"):
        spell_id = integer(row["spell_number"])
        attribute_id = integer(row["attribute"])
        raw_value = scalar(row["raw_value"])
        if spell_id is None or attribute_id is None:
            continue
        attributes[spell_id].append(
            {
                "attribute_id": attribute_id,
                "name": attribute_names.get(attribute_id, "<Unknown Attribute>"),
                "raw_value": raw_value,
            }
        )
        if attribute_id == 278 and isinstance(raw_value, int):
            restrictions[spell_id].add(raw_value)

    result = []
    summon_relations = []
    for row in spells:
        spell_id = integer(row["id"])
        if spell_id is None:
            continue
        effect = effect_record(row, effect_lookup, effect_names)
        school_number = integer(row.get("school"))
        published = school_number in range(0, 8)
        targets, groups, unresolved = summon_targets(row, spell_lookup, effect_lookup)
        roles = set()
        if effect:
            role = ROLE_BY_EFFECT.get(effect["effect_number"])
            if role:
                roles.add(role)
            if effect["effect_number"] in {2, 3, 7, 11, 24, 25, 32, 33, 36, 46, 66, 67, 70, 73, 74, 75, 91, 96}:
                roles.add("damage-or-disable")
            if effect["effect_number"] in {10, 13, 17, 23, 72}:
                roles.add("buff-or-restoration")
        if targets or groups or unresolved:
            roles.add("summon")
        restricted_nations = [
            {
                "nation_id": nation_id,
                "name": nations.get(nation_id, {}).get("name"),
                "era": nations.get(nation_id, {}).get("era"),
            }
            for nation_id in sorted(restrictions.get(spell_id, set()))
        ]
        record = {
            "id": f"spell-{spell_id:04d}",
            "object_type": "spell",
            "engine_id": spell_id,
            "name": row["name"],
            "public_status": "researchable-or-divine" if published else "unresearchable-or-internal",
            "school": SCHOOLS.get(school_number, f"Unknown school {school_number}"),
            "school_number": school_number,
            "research_level": integer(row.get("researchlevel")),
            "path_requirements": path_requirement(row),
            "spell_kind": "ritual" if effect and effect["ritual"] else "combat",
            "fatigue_cost_raw": integer(row.get("fatiguecost")),
            "gem_or_slave_cost_raw": integer(row.get("gemcost")),
            "precision_modifier": integer(row.get("precision")),
            "effects_count_raw": integer(row.get("effects_count")),
            "damage_override_raw": integer(row.get("damage")),
            "next_spell_id": integer(row.get("next_spell")) or None,
            "effect": effect,
            "role_tags": sorted(roles),
            "national_restrictions": restricted_nations,
            "extra_attributes": attributes.get(spell_id, []),
            "summon_target_units": names_for_units(targets, unit_lookup),
            "summon_groups": groups,
            "summon_resolution_notes": unresolved,
            "legendary_or_level_nine": published and integer(row.get("researchlevel")) == 9,
            "ruleset": "vanilla-6.35",
            "evidence_status": "source-confirmed",
            "source_ids": ["dom6-data-inspector-6.35"],
            "canonical_section_id": "b12-part-ii-spells",
            "verified_on": GENERATED_ON,
        }
        result.append(with_hash(record))
        if targets or groups or unresolved:
            relation = {
                "id": f"summon-relation-{spell_id:04d}",
                "object_type": "summon-relation",
                "spell_id": f"spell-{spell_id:04d}",
                "spell_engine_id": spell_id,
                "spell_name": row["name"],
                "target_units": names_for_units(targets, unit_lookup),
                "selection_groups": groups,
                "unresolved_selection": unresolved,
                "effects_count_raw": integer(row.get("effects_count")),
                "ruleset": "vanilla-6.35",
                "evidence_status": "source-confirmed" if not unresolved else "source-confirmed-with-unresolved-selection",
                "source_ids": ["dom6-data-inspector-6.35"],
                "canonical_section_id": "b12-part-iv-summons",
                "verified_on": GENERATED_ON,
            }
            summon_relations.append(with_hash(relation))
    return result, summon_relations


def build_items(data: Path) -> list[dict[str, Any]]:
    result = []
    for row in read_tsv(data / "BaseI.csv"):
        item_id = integer(row["id"])
        level = integer(row.get("constlevel"))
        if item_id is None:
            continue
        if level == 9:
            tier_class = "unique-artifact"
        elif level is not None and level <= 7:
            tier_class = "ordinary-forgeable"
        else:
            tier_class = "special-or-engine-managed"
        record = {
            "id": f"item-{item_id:04d}",
            "object_type": "magic-item",
            "engine_id": item_id,
            "name": row["name"],
            "slot_type": row.get("type") or None,
            "construction_level": level,
            "tier_class": tier_class,
            "path_requirements": item_path_requirement(row),
            "weapon_id": integer(row.get("weapon")),
            "armor_id": integer(row.get("armor")),
            "mechanical_properties": sparse(row, ITEM_CORE_FIELDS),
            "ruleset": "vanilla-6.35",
            "evidence_status": "source-confirmed",
            "source_ids": ["dom6-data-inspector-6.35", "dom6-manual-revision-2"],
            "canonical_section_id": "b12-part-iii-magic-items-artifacts-and-barding",
            "verified_on": GENERATED_ON,
        }
        result.append(with_hash(record))
    return result


def collect_unit_ids(row: dict[str, str], prefix: str, count: int = 5) -> list[int]:
    return [
        value
        for index in range(1, count + 1)
        if (value := integer(row.get(f"{prefix}{index}"))) is not None
    ]


def build_sites(
    data: Path,
    unit_lookup: dict[int, dict[str, str]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    terrain_bits = {
        integer(row["bit_value"]): row["bit_name"]
        for row in read_tsv(data / "site_terrain_types.csv")
        if integer(row["bit_value"]) is not None
    }
    sites = []
    thrones = []
    for row in read_tsv(data / "MagicSites.csv"):
        site_id = integer(row["id"])
        if site_id is None:
            continue
        rarity = integer(row.get("rarity")) or 0
        location_mask = integer(row.get("loc")) or 0
        locations = [name for bit, name in terrain_bits.items() if location_mask & bit]
        gem_income = {
            code: value
            for code in ["F", "A", "W", "E", "S", "D", "N", "G", "B"]
            if (value := integer(row.get(code))) is not None and value != 0
        }
        claimed_income = {
            code: value
            for code in ["F", "A", "W", "E", "S", "D", "N", "B"]
            if (value := integer(row.get(f"{code}2"))) is not None and value != 0
        }
        recruit_units = collect_unit_ids(row, "hmon") + collect_unit_ids(row, "mon")
        recruit_commanders = collect_unit_ids(row, "hcom") + collect_unit_ids(row, "com")
        summon_units = collect_unit_ids(row, "sum", 4)
        base = {
            "id": f"site-{site_id:04d}",
            "engine_id": site_id,
            "name": row["name"],
            "site_path": row.get("path") or None,
            "search_level": integer(row.get("level")),
            "rarity_code": rarity,
            "location_mask_raw": location_mask,
            "locations": locations,
            "gem_income": gem_income,
            "claimed_gem_income": claimed_income,
            "recruitable_units": names_for_units(recruit_units, unit_lookup),
            "recruitable_commanders": names_for_units(recruit_commanders, unit_lookup),
            "summoned_units": names_for_units(summon_units, unit_lookup),
            "mechanical_properties": sparse(row, SITE_CORE_FIELDS),
            "ruleset": "vanilla-6.35",
            "evidence_status": "source-confirmed",
            "source_ids": ["dom6-data-inspector-6.35"],
            "verified_on": GENERATED_ON,
        }
        if rarity in {11, 12, 13}:
            base.update(
                {
                    "object_type": "throne",
                    "throne_level": rarity - 10,
                    "canonical_section_id": "b12-part-vi-thrones-and-magic-sites",
                }
            )
            thrones.append(with_hash(base))
        else:
            if rarity in {0, 1, 2}:
                site_class = "random-discoverable"
            elif rarity == 5:
                site_class = "special-capital-or-event"
            else:
                site_class = "other"
            base.update(
                {
                    "object_type": "magic-site",
                    "site_class": site_class,
                    "canonical_section_id": "b12-part-vi-thrones-and-magic-sites",
                }
            )
            sites.append(with_hash(base))
    return sites, thrones


def build_mercenaries(
    data: Path,
    unit_lookup: dict[int, dict[str, str]],
    item_lookup: dict[int, dict[str, Any]],
) -> list[dict[str, Any]]:
    result = []
    for row in read_tsv(data / "Mercenary.csv"):
        merc_id = integer(row["id"])
        if merc_id is None:
            continue
        commander_id = integer(row.get("com"))
        troop_id = integer(row.get("unit"))
        era_mask = integer(row.get("eramask")) or 0
        eras = [era for bit, era in ERA_BITS.items() if era_mask & bit]
        item_ids = [value for key in ("item1", "item2") if (value := integer(row.get(key))) is not None]
        record = {
            "id": f"mercenary-{merc_id:03d}",
            "object_type": "mercenary-company",
            "engine_id": merc_id,
            "name": row["name"],
            "commander_name": row.get("bossname") or None,
            "commander_unit": names_for_units([commander_id], unit_lookup)[0] if commander_id else None,
            "troop_unit": names_for_units([troop_id], unit_lookup)[0] if troop_id else None,
            "starting_troops": integer(row.get("nrunits")),
            "company_level_raw": integer(row.get("level")),
            "minimum_survivors": integer(row.get("minmen")),
            "minimum_bid_gold": integer(row.get("minpay")),
            "starting_experience": integer(row.get("xp")),
            "random_equipment_raw": integer(row.get("randequip")),
            "recruitment_recovery_rate_raw": integer(row.get("recrate")),
            "fixed_items": [
                {"item_id": item_id, "name": item_lookup.get(item_id, {}).get("name")}
                for item_id in item_ids
            ],
            "era_mask_raw": era_mask,
            "eras": eras,
            "ruleset": "vanilla-6.35",
            "evidence_status": "source-confirmed",
            "source_ids": ["dom6-data-inspector-6.35", "dom6-manual-revision-2"],
            "canonical_section_id": "b12-part-vii-mercenaries-and-independent-recruitment",
            "verified_on": GENERATED_ON,
        }
        result.append(with_hash(record))
    return result


def nation_reference(nation: dict[str, Any]) -> dict[str, Any]:
    return {
        "nation_id": nation["id"],
        "name": nation["name"],
        "epithet": nation["epithet"],
        "era": nation["era"],
    }


def build_pretenders(
    data: Path,
    unit_lookup: dict[int, dict[str, str]],
    nations: dict[int, dict[str, Any]],
) -> list[dict[str, Any]]:
    available: dict[int, set[int]] = defaultdict(set)
    removed: dict[int, set[int]] = defaultdict(set)
    home_realms: dict[int, set[int]] = defaultdict(set)
    cheap20: dict[int, set[int]] = defaultdict(set)
    cheap40: dict[int, set[int]] = defaultdict(set)

    for row in read_tsv(data / "pretender_types_by_nation.csv"):
        nation_id = integer(row["nation_number"])
        monster_id = integer(row["monster_number"])
        if nation_id is not None and monster_id not in (None, 134):
            available[monster_id].add(nation_id)
    for row in read_tsv(data / "unpretender_types_by_nation.csv"):
        nation_id = integer(row["nation_number"])
        monster_id = integer(row["monster_number"])
        if nation_id is not None and monster_id is not None:
            removed[monster_id].add(nation_id)
    for row in read_tsv(data / "attributes_by_nation.csv"):
        nation_id = integer(row["nation_number"])
        attribute = integer(row["attribute"])
        raw_value = integer(row["raw_value"])
        if nation_id is None or raw_value is None:
            continue
        if attribute == 289:
            home_realms[nation_id].add(raw_value)
        elif attribute == 314:
            cheap20[raw_value].add(nation_id)
        elif attribute == 315:
            cheap40[raw_value].add(nation_id)
    realm_members: dict[int, set[int]] = defaultdict(set)
    for row in read_tsv(data / "realms.csv"):
        realm = integer(row["realm"])
        monster_id = integer(row["monster_number"])
        if realm is not None and monster_id is not None:
            realm_members[realm].add(monster_id)
    for nation_id, realms in home_realms.items():
        for realm in realms:
            for monster_id in realm_members.get(realm, set()):
                available[monster_id].add(nation_id)
    for monster_id, nation_ids in removed.items():
        available[monster_id].difference_update(nation_ids)

    result = []
    for monster_id in sorted(available):
        row = unit_lookup.get(monster_id)
        if not row:
            continue
        nation_ids = sorted(n for n in available[monster_id] if n in nations)
        if not nation_ids:
            continue
        weapons = [integer(row.get(f"wpn{i}")) for i in range(1, 8)]
        armors = [integer(row.get(f"armor{i}")) for i in range(1, 5)]
        record = {
            "id": f"pretender-{monster_id:04d}",
            "object_type": "pretender-form",
            "engine_id": monster_id,
            "name": row["name"],
            "starting_dominion": integer(row.get("startdom")),
            "new_path_cost": integer(row.get("pathcost")),
            "minimum_imprisonment_raw": integer(row.get("minprison")),
            "innate_paths": innate_paths(row),
            "random_magic": random_paths(row),
            "base_statistics": {
                key: integer(row.get(source))
                for key, source in {
                    "size": "size", "hit_points": "hp", "protection": "prot",
                    "magic_resistance": "mr", "morale": "mor", "strength": "str",
                    "attack": "att", "defence": "def", "precision": "prec",
                    "encumbrance": "enc", "map_move": "mapmove", "combat_speed": "ap",
                }.items()
            },
            "equipment_ids": {
                "weapons": [value for value in weapons if value is not None],
                "armour": [value for value in armors if value is not None],
            },
            "available_to": [nation_reference(nations[nation_id]) for nation_id in nation_ids],
            "availability_count": len(nation_ids),
            "cheap_god_20_for": [nation_reference(nations[n]) for n in sorted(cheap20.get(monster_id, set())) if n in nations],
            "cheap_god_40_for": [nation_reference(nations[n]) for n in sorted(cheap40.get(monster_id, set())) if n in nations],
            "shape_links": {
                key: integer(row.get(key))
                for key in ["shapechange", "firstshape", "secondshape", "secondtmpshape", "landshape", "watershape", "forestshape", "plainshape", "homeshape"]
                if integer(row.get(key)) is not None
            },
            "mechanical_properties": sparse(row, UNIT_CORE_FIELDS),
            "ruleset": "vanilla-6.35",
            "evidence_status": "source-confirmed",
            "source_ids": ["dom6-data-inspector-6.35", "dom6-manual-revision-2"],
            "canonical_section_id": "b12-part-v-pretender-forms",
            "verified_on": GENERATED_ON,
        }
        result.append(with_hash(record))
    return result


def resolve_nations(
    nations: dict[int, dict[str, Any]],
    selectors: list[tuple[str, str | None]],
) -> list[dict[str, Any]]:
    matches = []
    for nation in nations.values():
        for name, epithet in selectors:
            if nation["name"] == name and (epithet is None or nation["epithet"] == epithet):
                matches.append(nation_reference(nation))
                break
    return sorted(matches, key=lambda item: (item["era"], item["nation_id"]))


def build_special_dominions(nations: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
    definitions = [
        (
            "dominion-scrying",
            "Arcoscephale dominion scrying",
            [("Arcoscephale", None)],
            ["Automatically supplies accurate reports for provinces inside the nation's dominion.", "Reveals enemy units concealed by Glamour."],
            "Information is available to disciple players.",
        ),
        (
            "dying-dominion-mictlan",
            "Mictlan dying dominion",
            [("Mictlan", "Reign of Blood"), ("Mictlan", "Blood and Rain")],
            ["Temples and ordinary passive sources do not spread dominion in the normal way.", "Blood sacrifice is available and becomes the principal religious expansion method."],
            "Dying dominion is nation-specific and does not transfer through disciple status.",
        ),
        (
            "yomi-oni-temples",
            "Yomi temple Oni",
            [("Yomi", None)],
            ["Temples inside Yomi's dominion generate Oni.", "Turmoil changes quantity; terrain and temperature change the available Oni types.", "At least one friendly candle is required, but higher local dominion strength does not itself raise the temple spawn rate."],
            "The temple-generation feature does not transfer to disciples.",
        ),
        (
            "dreamlands",
            "R'lyeh Dreamlands",
            [("R'lyeh", "Dreamlands")],
            ["Spreads insanity to non-Void beings.", "Generates madmen and can transform them into Void Dreamers over time."],
            "The effects extend into disciple lands; disciple protection from madness is only partial.",
        ),
        (
            "ashen-empire",
            "Ermor Ashen Empire",
            [("Ermor", "Ashen Empire")],
            ["Kills living population and raises undead replacements.", "Detects unburied corpses in covered provinces."],
            "Population death and obedient undead generation also occur for disciples.",
        ),
        (
            "carrion-woods",
            "Asphodel Carrion Woods",
            [("Asphodel", None)],
            ["Kills living population.", "Animates corpses and living remains as Manikins and Carrion creatures."],
            "The population and animation effects also apply to disciples.",
        ),
        (
            "ctis-miasma",
            "C'tis Miasma",
            [("C'tis", "Miasma")],
            ["Creates persistent rain, disease pressure, and wet terrain.", "Warm-blooded units without Swamp Survival are vulnerable.", "Enemy income is heavily reduced while C'tis receives a smaller positive income effect.", "Non-sea land slowly changes toward swamp or drip-cave terrain."],
            "Disciples are treated like enemies except that their sacred troops are immune; underwater provinces are unaffected.",
        ),
        (
            "golem-cult",
            "Agartha Golem Cult",
            [("Agartha", "Golem Cult")],
            ["Constructs receive increased hit points inside the dominion."],
            "The benefit applies to disciple constructs and also to enemy constructs in the dominion.",
        ),
        (
            "blood-sacrifice-family",
            "Additional blood-sacrifice nations",
            [
                ("Abysia", None), ("Marverni", "Time of Druids"), ("Sauromatia", None),
                ("Pangaea", "Age of Revelry"), ("Vanheim", None), ("Hinnom", None),
                ("Berytos", None), ("Xibalba", "Vigil of the Sun"),
                ("Pyrène", "Time of the Akelarre"), ("Nidavangr", None),
                ("Marignon", "Conquerors of the Sea"), ("Midgård", None),
                ("Gath", None), ("Xibalba", "Return of the Zotz"),
            ],
            ["May perform blood sacrifices to increase dominion while retaining ordinary passive dominion spread."],
            "The ability does not transfer to a disciple nation, although a disciple nation that already possesses it keeps it.",
        ),
        (
            "dark-ships",
            "Phaeacia Dark Ships",
            [("Phaeacia", None)],
            ["Phaeacian commanders may sail when both origin and destination are inside friendly dominion."],
            "The ability does not transfer to another nation; disciple-led Phaeacia can still use it under the master's dominion.",
        ),
        (
            "therodos-ghosts",
            "Therodos spectral dominion",
            [("Therodos", None)],
            ["Population slowly dies under friendly dominion.", "Friendly forts under the dominion generate ghosts."],
            "Both effects also apply in disciple games.",
        ),
        (
            "mekone-conflict",
            "Mekone dominion conflict",
            [("Mekone", None)],
            ["Mekone's maximum dominion is counted as one higher when suppressing enemy faith."],
            "The manual does not state a transferred disciple effect for this rule.",
        ),
        (
            "phlegra-unrest",
            "Phlegra dominion unrest",
            [("Phlegra", None)],
            ["Every covered province gains unrest each turn.", "Higher local dominion strength produces a larger unrest increase."],
            "In a disciple game the effect operates only when Phlegra is the Pretender nation, then also affects disciples.",
        ),
        (
            "concealed-provinces",
            "Dominion-concealed provinces",
            [("Ubar", None), ("Na'Ba", None), ("Ind", None), ("Feminie", None)],
            ["Hides province name and ownership from enemies who have not investigated closely.", "A nearby observer sees a false independent province; a scout must enter to pierce the deception."],
            "Disciples also receive the concealment benefit.",
        ),
    ]
    result = []
    for index, (slug, name, selectors, mechanics, disciple_rule) in enumerate(definitions, 1):
        record = {
            "id": f"special-dominion-{index:02d}-{slug}",
            "object_type": "special-dominion-system",
            "name": name,
            "nations": resolve_nations(nations, selectors),
            "mechanics": mechanics,
            "disciple_rule": disciple_rule,
            "ruleset": "vanilla-6.35",
            "evidence_status": "official",
            "source_ids": ["dom6-manual-revision-2"],
            "source_locator": "Special Dominions, manual pp. 87-88",
            "canonical_section_id": "b12-part-viii-special-dominion-systems",
            "verified_on": GENERATED_ON,
        }
        result.append(with_hash(record))
    return result


def independent_coverage_marker() -> list[dict[str, Any]]:
    record = {
        "id": "independent-coverage-001",
        "object_type": "coverage-marker",
        "name": "Independent population-type recruitment",
        "coverage_status": "not-yet-verifiably-exhaustive",
        "available_now": "Current 6.35 unit statistics are present in the upstream unit table and can be joined once population-type membership is verified.",
        "excluded_claim": "The available 6.35 inspector extract does not expose a population-type table, so it cannot prove which units each independent province type recruits.",
        "reliable_resolution_route": "A version-matched engine population-type export or a published 6.35 reproduction with unit IDs.",
        "ruleset": "vanilla-6.35",
        "evidence_status": "test-pending",
        "source_ids": ["dom6-data-inspector-6.35", "dom6-mod-manual-6.34"],
        "canonical_section_id": "b12-part-vii-mercenaries-and-independent-recruitment",
        "verified_on": None,
    }
    return [with_hash(record)]


def source_manifest(data: Path, repo: Path, commit: str, commit_date: str) -> list[dict[str, Any]]:
    files = [
        "spells.csv", "effects_spells.csv", "effects_info.csv", "attributes_by_spell.csv",
        "BaseI.csv", "BaseU.csv", "MagicSites.csv", "Mercenary.csv", "nations.csv",
        "pretender_types_by_nation.csv", "unpretender_types_by_nation.csv",
        "attributes_by_nation.csv", "realms.csv", "site_terrain_types.csv",
    ]
    return [
        {
            "id": "dom6-data-inspector-6.35",
            "title": "Dominions 6 Data Inspector extracted game data",
            "kind": "game-data",
            "url": "https://github.com/larzm42/dom6inspector",
            "repository_commit": commit,
            "repository_commit_date": commit_date,
            "repository_subject": git_value(repo, "log", "-1", "--format=%s"),
            "license": "GPL-3.0 (repository); game-derived factual fields remain attributed to Illwinter",
            "files": [
                {"path": f"gamedata/{name}", "sha256": sha256(data / name)}
                for name in files
            ],
        },
        {
            "id": "dom6-manual-revision-2",
            "title": "Dominions 6 Manual",
            "kind": "official-manual",
            "url": "https://www.illwinter.com/dom6/dom6manual.pdf",
            "version": "revision 2",
            "local_sha256": "ea51ab6911a4feb1e8bf6f8ac678455d8b3cd65ef6c3a237bd446bce91780f84",
        },
        {
            "id": "dom6-mod-manual-6.34",
            "title": "Dominions 6 Modding Manual",
            "kind": "official-mod-manual",
            "url": "https://www.illwinter.com/dom6/dom6modman.pdf",
            "version": "6.34",
        },
    ]


def schema_document() -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://thehobokingdom.com/schemas/dominions-base-object-register.schema.json",
        "title": "TheHoboKingdom Dominions 6 Base-Game Object Register",
        "type": "object",
        "required": ["schema_version", "edition", "ruleset", "sources", "counts", "records"],
        "properties": {
            "schema_version": {"const": "1.0.0"},
            "edition": {"type": "string"},
            "generated_on": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
            "ruleset": {
                "type": "object",
                "required": ["game", "game_version", "mods"],
                "properties": {
                    "game": {"const": "Dominions 6"},
                    "game_version": {"const": "6.35"},
                    "mods": {"type": "array", "maxItems": 0},
                },
                "additionalProperties": False,
            },
            "evidence_key": {"type": "object"},
            "scope": {"type": "object"},
            "sources": {"type": "array", "minItems": 2},
            "counts": {
                "type": "object",
                "required": ["spells", "items", "summons", "pretenders", "thrones", "sites", "mercenaries", "independents", "special_dominions"],
                "additionalProperties": {"type": "integer", "minimum": 0},
            },
            "records": {
                "type": "object",
                "required": ["spells", "items", "summons", "pretenders", "thrones", "sites", "mercenaries", "independents", "special_dominions"],
                "properties": {
                    key: {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "object_type", "name", "ruleset", "evidence_status", "source_ids", "canonical_section_id", "record_hash"],
                        },
                    }
                    for key in ["spells", "items", "pretenders", "thrones", "sites", "mercenaries", "independents", "special_dominions"]
                } | {
                    "summons": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "object_type", "spell_id", "spell_name", "ruleset", "evidence_status", "source_ids", "canonical_section_id", "record_hash"],
                        },
                    }
                },
                "additionalProperties": False,
            },
        },
        "additionalProperties": False,
    }


def main() -> None:
    args = parse_args()
    repo = args.source.resolve()
    data = repo / "gamedata"
    if not data.is_dir():
        raise SystemExit(f"Data directory not found: {data}")
    commit = git_value(repo, "rev-parse", "HEAD")
    commit_date = git_value(repo, "log", "-1", "--format=%aI")
    if commit != EXPECTED_COMMIT and not args.allow_unpinned:
        raise SystemExit(
            f"Expected pinned 6.35 commit {EXPECTED_COMMIT}, found {commit}. "
            "Use --allow-unpinned only for an intentional refresh."
        )

    unit_rows = read_tsv(data / "BaseU.csv")
    unit_lookup = {integer(row["id"]): row for row in unit_rows if integer(row["id"]) is not None}
    nation_rows = read_tsv(data / "nations.csv")
    era_codes = {1: "EA", 2: "MA", 3: "LA", 0: None}
    nations = {
        integer(row["id"]): {
            "id": integer(row["id"]),
            "name": row["name"],
            "epithet": row["epithet"],
            "era": era_codes.get(integer(row["era"])),
        }
        for row in nation_rows
        if integer(row["id"]) is not None
    }

    spells, summons = build_spells(data, unit_lookup, nations)
    items = build_items(data)
    item_lookup = {record["engine_id"]: record for record in items}
    sites, thrones = build_sites(data, unit_lookup)
    pretenders = build_pretenders(data, unit_lookup, nations)
    mercenaries = build_mercenaries(data, unit_lookup, item_lookup)
    independents = independent_coverage_marker()
    special_dominions = build_special_dominions(nations)

    records = {
        "spells": spells,
        "items": items,
        "summons": summons,
        "pretenders": pretenders,
        "thrones": thrones,
        "sites": sites,
        "mercenaries": mercenaries,
        "independents": independents,
        "special_dominions": special_dominions,
    }
    counts = {key: len(value) for key, value in records.items()}
    document = {
        "schema_version": "1.0.0",
        "edition": "Progress Edition 15",
        "generated_on": GENERATED_ON,
        "ruleset": {"game": "Dominions 6", "game_version": GAME_VERSION, "mods": []},
        "evidence_key": {
            "official": "Directly supported by current official documentation.",
            "source-confirmed": "Present in the pinned 6.35 extracted data source; confirm contentious display semantics in the game UI.",
            "source-confirmed-with-unresolved-selection": "The summoning effect is identified but an engine-selected target group is not fully resolved.",
            "test-pending": "The available sources cannot yet support a complete current-version catalogue.",
        },
        "scope": {
            "description": "Mechanical, filterable base-game records for the reusable website layer.",
            "includes": ["spells", "items", "summons", "Pretender forms", "Thrones", "magic sites", "mercenaries", "special dominions"],
            "deliberate_exclusions": ["long game descriptions", "sprite assets", "strategy prose already owned by Books II-VI", "modded overrides"],
            "known_gap": "Independent population-type membership remains blocked because the pinned 6.35 extract has no population-type table.",
        },
        "sources": source_manifest(data, repo, commit, commit_date),
        "counts": counts,
        "records": records,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.schema.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.schema.write_text(json.dumps(schema_document(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "schema": str(args.schema), "counts": counts, "commit": commit}))


if __name__ == "__main__":
    main()
