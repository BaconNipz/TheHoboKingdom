#!/usr/bin/env python3
"""Build the source-backed compact dossiers for every unfinished MA nation."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
DATA = WORK / "inspector-src" / "gamedata"
BOOK = ROOT / "12-foundation-book-vii-nations-arcoscephale.md"
START = "<!-- GENERATED REMAINING MA DOSSIERS START -->"
END = "<!-- GENERATED REMAINING MA DOSSIERS END -->"
PATHS = ["F", "A", "W", "E", "S", "D", "N", "G", "B", "H"]
PATH_NAMES = dict(zip(PATHS, ["Fire", "Air", "Water", "Earth", "Astral", "Death", "Nature", "Glamour", "Blood", "Holy"]))
SCHOOLS = {0: "Conjuration", 1: "Alteration", 2: "Evocation", 3: "Construction", 4: "Enchantment", 5: "Thaumaturgy", 6: "Blood", 7: "Divine"}
PATH_NUMBERS = {str(i): p for i, p in enumerate(PATHS)}

NATIONS = [
    (51, "XXXIII", "Phlegra", "Deformed Giants", "enslaved human levies and scarce giant elites", "giant recruitment limits, unrest, and replacement speed"),
    (53, "XXXIV", "Asphodel", "Carrion Woods", "Carrion Woods freespawn, stealth, and Death–Nature magic", "population decline, freespawn composition, and living infrastructure"),
    (54, "XXXV", "Ermor", "Ashen Empire", "dominion-created undead and powerful Death magic", "population destruction, freespawn control, and hostile dominion"),
    (55, "XXXVI", "Sceleria", "The Reformed Empire", "Roman infantry, communions, and deliberate undead production", "communion safety, upkeep, and mage-turn pressure"),
    (65, "XXXVII", "Na'Ba", "Queens of the Desert", "desert recruitment, human armies, and Jinn-backed magic", "terrain access, rare paths, and elite replacement"),
    (67, "XXXVIII", "Ind", "Magnificent Kingdom of Exalted Virtue", "capital authority and geographically divided tributary recruitment", "regional availability, slow concentration, and sacred replacement"),
    (68, "XXXIX", "Bandar Log", "Land of the Apes", "mass ape infantry, sacred White Ones, and Astral–Nature mages", "morale, armour, rare path rolls, and expensive sacreds"),
    (72, "XL", "Nazca", "Kingdom of the Sun", "flying armies, sacred Sun Guards, and reanimation", "fragile bodies, corpse supply, leadership, and capital pressure"),
    (73, "XLI", "Mictlan", "Reign of the Lawgiver", "broad elemental priests, sacred warriors, and Blood access", "blood-hunting opportunity cost, priest turns, and lightly protected troops"),
    (74, "XLII", "Xibalba", "Flooded Caves", "cave recruitment, flying Zotz, amphibious forces, and Blood magic", "terrain splits, weak bodies, underwater logistics, and random paths"),
    (77, "XLIII", "Phaeacia", "Isle of the Dark Ships", "sailing, Colossi, and a broad island mage corps", "gold-intensive elites, sailing boundaries, and coastal replacement"),
    (79, "XLIV", "Vanarus", "Land of the Chuds", "human infantry, Chud elites, stealth, and forest-linked magic", "mixed troop quality, limited armour, and dispersed specialist roles"),
    (80, "XLV", "Jotunheim", "Iron Woods", "giant infantry, sacred Jotuns, and Death–Nature magic", "high gold per body, low formation width, and replacement tempo"),
    (81, "XLVI", "Nidavangr", "Bear, Wolf and Crow", "Dwarven smiths, skinshifters, and terrain-linked recruitment", "expensive specialists, transformation behaviour, and regional access"),
    (85, "XLVII", "Ys", "Morgen Queens", "amphibious Morgen nobility, sacred knights, and coastal mobility", "land–sea transitions, glamour interactions, and elite replacement"),
    (86, "XLVIII", "Pelagia", "Triton Kings", "deep-water recruitment, Triton armies, and Water–Astral magic", "aquatic geography, land projection, and commander coverage"),
    (87, "XLIX", "Oceania", "Mermidons", "aquatic armies, Capricorns, and Water–Nature magic", "sea expansion variance, land access, and mixed habitat limits"),
    (88, "L", "Atlantis", "Kings of the Deep", "armoured amphibious troops and Water–Earth–Death magic", "resource-heavy troops, cold-water geography, and land transition"),
    (89, "LI", "R'lyeh", "Fallen Star", "mind control, aquatic slave troops, and powerful Astral magic", "slave morale, magic leadership, land access, and friendly-fire risk"),
]


def rows(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


UNITS = {int(x["id"]): x for x in rows("BaseU.csv")}
SITES = {int(x["id"]): x for x in rows("MagicSites.csv")}
SPELLS = {int(x["id"]): x for x in rows("spells.csv")}
ITEMS = rows("BaseI.csv")
NATION_ATTRS = rows("attributes_by_nation.csv")
SPELL_ATTRS = rows("attributes_by_spell.csv")


def member_ids(filename: str, nation: int) -> list[int]:
    return [int(x["monster_number"]) for x in rows(filename) if int(x["nation_number"]) == nation]


def uniq(values: list[int]) -> list[int]:
    return list(dict.fromkeys(values))


def site_ids(nation: int) -> list[int]:
    return [int(x["raw_value"]) for x in NATION_ATTRS if int(x["nation_number"]) == nation and x["attribute"] == "52"]


def site_members(nation: int, commander: bool) -> list[int]:
    fields = [f"hcom{i}" for i in range(1, 6)] + [f"com{i}" for i in range(1, 6)] if commander else [f"hmon{i}" for i in range(1, 6)] + [f"mon{i}" for i in range(1, 6)]
    result: list[int] = []
    for sid in site_ids(nation):
        site = SITES.get(sid, {})
        result.extend(int(site[f]) for f in fields if site.get(f, "").lstrip("-").isdigit() and int(site[f]) > 0)
    return uniq(result)


def path_text(unit: dict[str, str]) -> str:
    fixed = " ".join(f"{p}{unit[p]}" for p in PATHS if unit.get(p)) or "none"
    randoms = []
    for i in range(1, 5):
        if unit.get(f"rand{i}"):
            randoms.append(f"{unit[f'rand{i}']}% ×{unit.get(f'nbr{i}') or '1'} mask {unit.get(f'mask{i}') or '?'} link {unit.get(f'link{i}') or '0'}")
    return fixed + ("; random: " + "; ".join(randoms) if randoms else "")


def traits(unit: dict[str, str]) -> str:
    names = []
    for field, label in [("holy", "sacred"), ("undead", "undead"), ("demon", "demon"), ("magicbeing", "magic being"), ("flying", "flying"), ("aquatic", "aquatic"), ("amphibian", "amphibious"), ("pooramphibian", "poor amphibian"), ("mounted", "mounted"), ("stealthy", "stealthy")]:
        if unit.get(field) not in {None, "", "0"}: names.append(label)
    return ", ".join(names) or "ordinary body"


def unit_table(ids: list[int], mage: bool = False) -> str:
    if not ids:
        return "No ordinary membership rows are present in the pinned snapshot; site, freespawn, event, or special recruitment must be read separately.\n"
    if mage:
        lines = ["| ID | Commander | Fixed and random magic | Leadership |", "| ---: | --- | --- | ---: |"]
        for uid in ids:
            u = UNITS[uid]
            lines.append(f"| {uid} | {u['name']} | {path_text(u)} | {u.get('leader') or '0'} |")
    else:
        lines = ["| ID | Unit | HP | Protection | Morale | Traits |", "| ---: | --- | ---: | ---: | ---: | --- |"]
        for uid in ids:
            u = UNITS[uid]
            lines.append(f"| {uid} | {u['name']} | {u.get('hp') or '?'} | {u.get('prot') or '?'} | {u.get('mor') or '?'} | {traits(u)} |")
    return "\n".join(lines) + "\n"


def national_spells(nation: int) -> list[dict[str, str]]:
    ids = uniq([int(x["spell_number"]) for x in SPELL_ATTRS if x["attribute"] == "278" and x["raw_value"] == str(nation)])
    return [SPELLS[x] for x in ids if x in SPELLS and SPELLS[x]["name"].lower() != "xxx"]


def spell_table(nation: int) -> str:
    spells = national_spells(nation)
    if not spells: return "No active nation-restricted spell row was found for this nation in the pinned snapshot. Absence here is a metadata boundary, not proof that no shared or special spell exists.\n"
    lines = ["| ID | Spell | School | Requirement | Cost field |", "| ---: | --- | --- | --- | ---: |"]
    for s in spells:
        req_parts = []
        for path_field, level_field in [("path1", "pathlevel1"), ("path2", "pathlevel2")]:
            path = PATH_NUMBERS.get(s.get(path_field, ""))
            level = s.get(level_field, "")
            if path and level.lstrip("-").isdigit() and int(level) >= 0:
                req_parts.append(f"{path}{level}")
        req = " ".join(req_parts) or "special"
        school = SCHOOLS.get(int(s["school"]), f"school {s['school']}") if s.get("school", "").lstrip("-").isdigit() else "special"
        level = s.get("researchlevel") or "—"
        cost = s.get("gemcost") or s.get("fatiguecost") or "—"
        lines.append(f"| {s['id']} | {s['name']} | {school} {level} | {req} | {cost} |")
    return "\n".join(lines) + "\n"


def item_table(nation: int) -> str:
    found = []
    for item in ITEMS:
        restricted = nation in [int(item[x]) for x in [f"restricted{i}" for i in range(1, 7)] if item.get(x, "").isdigit()]
        rebate = nation in [int(item[x]) for x in ["nationrebate1", "nationrebate2"] if item.get(x, "").isdigit()]
        if restricted or rebate: found.append((item, "restricted" if restricted else "rebate"))
    if not found: return "No nation restriction or rebate link appears in the pinned item rows. This does not establish live forge pricing or exclude undocumented behaviour.\n"
    lines = ["| ID | Item | Construction | Paths | Link |", "| ---: | --- | ---: | --- | --- |"]
    for x, kind in found:
        req = " ".join(y for y in [f"{x['mainpath']}{x['mainlevel']}" if x.get('mainpath') else "", f"{x['secondarypath']}{x['secondarylevel']}" if x.get('secondarypath') else ""] if y) or "special"
        lines.append(f"| {x['id']} | {x['name']} | {x.get('constlevel') or '—'} | {req} | {kind} |")
    return "\n".join(lines) + "\n"


def hero_table(nation: int) -> str:
    ids = uniq([int(x["raw_value"]) for x in NATION_ATTRS if int(x["nation_number"]) == nation and x["attribute"].isdigit() and 139 <= int(x["attribute"]) <= 149])
    ids = [x for x in ids if x in UNITS]
    if not ids: return "No fixed hero-slot identity was resolved from attributes 139–149. Hero arrival and timing remain unscheduled.\n"
    lines = ["| ID | Hero record | Magic | Boundary |", "| ---: | --- | --- | --- |"]
    for uid in ids:
        u = UNITS[uid]
        lines.append(f"| {uid} | {u['name']} | {path_text(u)} | assignment only; timing unresolved |")
    return "\n".join(lines) + "\n"


def site_table(nation: int) -> str:
    ids = site_ids(nation)
    if not ids: return "No capital-site association row was found. Hidden, generated, or special national effects are not inferred.\n"
    lines = ["| ID | Site | Monthly fields | Recruits recorded |", "| ---: | --- | --- | --- |"]
    for sid in ids:
        s = SITES.get(sid)
        if not s: continue
        gems = ", ".join(f"{p}{s[p]}" for p in PATHS[:-1] if s.get(p)) or "no gem field"
        members = [UNITS[int(s[f])]["name"] for f in [*(f"hcom{i}" for i in range(1, 6)), *(f"com{i}" for i in range(1, 6)), *(f"hmon{i}" for i in range(1, 6)), *(f"mon{i}" for i in range(1, 6))] if s.get(f, "").isdigit() and int(s[f]) in UNITS]
        lines.append(f"| {sid} | {s['name']} | {gems} | {', '.join(members) or 'none in explicit recruit fields'} |")
    return "\n".join(lines) + "\n"


def path_summary(commanders: list[int]) -> str:
    maxima = {p: 0 for p in PATHS}
    for uid in commanders:
        u = UNITS[uid]
        for p in PATHS:
            if u.get(p, "").isdigit(): maxima[p] = max(maxima[p], int(u[p]))
    shown = [f"{PATH_NAMES[p]} {n}" for p, n in maxima.items() if n]
    return ", ".join(shown) or "no fixed recruitable path in the ordinary/site commander rows"


def dossier(nation: int, roman: str, name: str, epithet: str, identity: str, risk: str) -> str:
    ordinary_com = member_ids("fort_leader_types_by_nation.csv", nation)
    regional_com = uniq(member_ids("nonfort_leader_types_by_nation.csv", nation) + member_ids("coast_leader_types_by_nation.csv", nation))
    capital_com = site_members(nation, True)
    commanders = uniq(ordinary_com + regional_com + capital_com)
    ordinary_mon = member_ids("fort_troop_types_by_nation.csv", nation)
    regional_mon = uniq(member_ids("nonfort_troop_types_by_nation.csv", nation) + member_ids("coast_troop_types_by_nation.csv", nation))
    capital_mon = site_members(nation, False)
    troops = uniq(ordinary_mon + regional_mon + capital_mon)
    mage_ids = [uid for uid in commanders if any(UNITS[uid].get(p) for p in PATHS) or any(UNITS[uid].get(f"rand{i}") for i in range(1, 5))]
    sacred = [UNITS[x]["name"] for x in troops if UNITS[x].get("holy") not in {None, "", "0"}]
    mobile = [UNITS[x]["name"] for x in troops if UNITS[x].get("flying") not in {None, "", "0"}]
    aquatic = [UNITS[x]["name"] for x in troops if any(UNITS[x].get(k) not in {None, "", "0"} for k in ["aquatic", "amphibian", "pooramphibian"])]
    spells = national_spells(nation)
    brief = f"Middle Age {name} converts {identity} into expansion, research, and strategic pressure. The pinned roster resolves {len(commanders)} commander identities and {len(troops)} troop identities across ordinary, regional, coastal, and site-linked recruitment, plus {len(spells)} active nation-restricted spell records. Its chief planning risks are {risk}."
    return f"""# Part {roman}: Middle Age {name}, {epithet}

## {name} one-page command brief

{brief}

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## {name} evidence and ruleset

This dossier covers unmodded Middle Age {name} on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID {nation}, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any {name} object without a named official record. No runtime test, replay, save, or new test asset was used.

## {name} conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## {name} recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | {len(ordinary_com)} | {len(ordinary_mon)} | Direct pinned membership rows |
| Regional or coastal | {len(regional_com)} | {len(regional_mon)} | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | {len(capital_com)} | {len(capital_mon)} | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## {name} commander roster

{unit_table(commanders, True)}

## {name} troop roster

{unit_table(troops)}

## {name} mage and priest portfolio

{unit_table(mage_ids, True)}

The highest fixed recruitable paths resolved in these rows are {path_summary(commanders)}. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## {name} capital and national sites

{site_table(nation)}

Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## {name} national spell map

{spell_table(nation)}

Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## {name} national item boundary

{item_table(nation)}

Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## {name} hero boundary

{hero_table(nation)}

Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## {name} army identities

- Sacred roster: {', '.join(sacred) if sacred else 'no sacred troop identified in the reconciled recruit rows'}.
- Flying roster: {', '.join(mobile) if mobile else 'no flying troop identified in the reconciled recruit rows'}.
- Aquatic or amphibious roster: {', '.join(aquatic) if aquatic else 'no aquatic or amphibious troop identified in the reconciled recruit rows'}.
- Core identity: {identity}.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## {name} opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## {name} fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For {name}, the most likely planning failure is {risk}. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## {name} research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## {name} magic-access ladder

The fixed-path ceiling is {path_summary(commanders)}. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## {name} battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## {name} Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## {name} matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## {name} monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## {name} unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## {name} source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.
"""


def main() -> None:
    generated = START + "\n\n" + "\n\n".join(dossier(*n) for n in NATIONS) + "\n\n" + END
    text = BOOK.read_text(encoding="utf-8")
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), generated, text, flags=re.S)
    else:
        marker = "## Dossier source register"
        if marker not in text: raise ValueError("Dossier source register marker not found")
        text = text.replace(marker, generated + "\n\n" + marker, 1)
    BOOK.write_text(text, encoding="utf-8")
    print(f"Wrote {len(NATIONS)} dossiers to {BOOK}")


if __name__ == "__main__":
    main()
