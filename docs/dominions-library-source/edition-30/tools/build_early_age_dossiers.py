#!/usr/bin/env python3
"""Build the source-backed Early Age nation dossiers."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
DATA = WORK / "inspector-src" / "gamedata"
BOOK = ROOT / "12-foundation-book-vii-nations-arcoscephale.md"
START = "<!-- GENERATED EARLY AGE DOSSIERS START -->"
END = "<!-- GENERATED EARLY AGE DOSSIERS END -->"
PATHS = ["F", "A", "W", "E", "S", "D", "N", "G", "B", "H"]
PATH_NAMES = dict(zip(PATHS, ["Fire", "Air", "Water", "Earth", "Astral", "Death", "Nature", "Glamour", "Blood", "Holy"]))
SCHOOLS = {0: "Conjuration", 1: "Alteration", 2: "Evocation", 3: "Construction", 4: "Enchantment", 5: "Thaumaturgy", 6: "Blood", 7: "Divine"}
PATH_NUMBERS = {str(i): p for i, p in enumerate(PATHS)}

NATIONS = [
    (5, "LII", "Arcoscephale", "Golden Era", "bronze-age combined arms, gifted philosophers, Mystics, Icarids, and sacred Pegasus Riders", "capital pressure, expensive specialists, random-path dependence, and keeping research aligned with field support"),
    (6, "LIII", "Mekone", "Brazen Giants", "a small core of Exalted Gigantes and Cyclope smiths supported by numerous human helots", "giant replacement speed, unrest and administration, gold concentration, and the gap between elite and slave troops"),
    (7, "LIV", "Pangaea", "Age of Revelry", "forest recruitment, plentiful revelers, centaurs and minotaurs, and strong Nature magic from the Panii", "undisciplined troops, forest dependence, supply, blood-hunting opportunity cost, and protecting expensive mages"),
    (8, "LV", "Ermor", "New Faith", "disciplined legionnaires, lizard auxiliaries, Augurs, and a powerful priesthood divided between old and new religious traditions", "mage and priest turn pressure, communion safety, capital recruitment, and keeping the army supplied as it expands"),
    (9, "LVI", "Sauromatia", "Amazon Queens", "mobile tribal armies, Amazon commanders, serpent and lizard riders, hydras, and Death–Nature–Blood magic", "light protection, poison exposure, blood-hunting costs, and coordinating several distinct troop families"),
    (10, "LVII", "Fomoria", "The Cursed Ones", "Fomorian giants, Fir Bolg infantry, Nemedian specialists, sailing, and strong Air–Death magic", "expensive giant replacement, afflictions, storm planning, and maintaining enough ordinary bodies"),
    (11, "LVIII", "Tir na n'Og", "Land of the Ever Young", "Fir Bolg ranks supporting glamour-shrouded Tuatha and Sidhe sacreds with Water–Nature–Glamour magic", "elite scarcity, glamour counters, gold concentration, and preserving stealthy mage turns"),
    (12, "LIX", "Marverni", "Time of Druids", "tribal infantry, sacred boars, noble cavalry, and Druids spanning Earth, Astral, Nature, and Water", "light armour, morale, communion safety, random access, and turning broad magic into timely research"),
    (13, "LX", "Ulm", "Enigma of Steel", "stealthy forest warriors, warrior-smiths, resource-efficient equipment, and unusually strong forging", "limited magical breadth, old-age attrition, forest recruitment, and translating forged equipment into field value"),
    (14, "LXI", "Pyrène", "Kingdom of the Bekrydes", "cave-linked Bekrydes, ancient giants, Cyclopes, storm-witches, and Earth–Air magic", "regional recruitment, giant replacement, mixed body sizes, and rare-path dependence"),
    (15, "LXII", "Agartha", "Pale Ones", "amphibious Pale Ones, sacred Ancient Ones, deep recruitment, and Earth–Fire–Death magic", "low attack and defence, expensive sacred replacement, cave logistics, and moving effectively between land and sea"),
    (16, "LXIII", "Abysia", "Children of Flame", "heavily armoured heat-radiating infantry, salamanders, Anathemants, and powerful Fire–Blood magic", "old age, heat management, limited mobility, blood-hunting costs, and answering fire resistance"),
    (17, "LXIV", "Hinnom", "Sons of the Fallen", "Rephaite and Avvite giants, human and Enkidu support, chariots, and exceptionally broad giant mage-priests", "population and unrest damage, immense gold costs, giant upkeep, and controlling dangerous sacred elites"),
    (18, "LXV", "Ubar", "Kingdom of the Unseen", "human desert forces, Ghuls, Jinnun, invisible sacred Ifrit, and a dominion that hides the capital", "desert recruitment, invisible-unit leadership, expensive elites, and dependence on terrain and rare magic"),
    (19, "LXVI", "Ur", "The First City", "city and nomadic Enkidu, terrain-dependent recruitment, strong shamans, and sacred Mushussu", "regional availability, weak armour, commander coverage, and assembling forces drawn from different terrain"),
    (20, "LXVII", "Kailasa", "Rise of the Ape Kings", "large numbers of light apes directed by rare Yakshas with strong Astral–Nature–Glamour magic", "low morale and protection, expensive sacred mages, magic leadership, and making numerous troops hold together"),
    (21, "LXVIII", "Lanka", "Land of Demons", "sacred Rakshasa, light ape troops, reanimated servants, and Blood–Death–Nature magic", "blood economy, unrest, demon leadership, fire vulnerability, and expensive sacred replacement"),
    (22, "LXIX", "T'ien Ch'i", "Spring and Autumn", "human combined arms, noble commanders, Masters of the Way, and broad but distributed elemental magic", "mage-path fragmentation, capital pressure, army coordination, and matching research to the casters actually recruited"),
    (23, "LXX", "Yomi", "Oni Kings", "Oni commanders and freespawn, Bakemono and human servants, and a dominion shaped by Turmoil", "freespawn composition, unrest, demon leadership, weak mundane troops, and the opportunity cost of order and temperature choices"),
    (24, "LXXI", "Caelum", "Eagle Kings", "flying winged troops, strong archery, cold-forged ice equipment, mammoths, and powerful Air magic", "temperature-dependent protection, fragile troops, storm interactions, supply, and coordinating flyers with slower forces"),
    (25, "LXXII", "Mictlan", "Reign of Blood", "cheap tribal armies, sacred Jaguar and Eagle Warriors, mage-priests, and dominion sustained through blood sacrifice", "blood-slave supply, priest turns, weak protection, dominion maintenance, and preventing expansion from outrunning sacrifice coverage"),
    (26, "LXXIII", "Xibalba", "Vigil of the Sun", "numerous stealthy flying Zotz, cave recruitment, blood hunting, and dark Water–Earth–Death–Blood magic", "very fragile troops, cave and surface logistics, blood economy, leadership, and surviving missile fire"),
    (27, "LXXIV", "C'tis", "Lizard Kings", "cold-blooded lizard infantry, chariots, sacred serpents, and accomplished Death–Nature mages", "temperature, low defence, supply, poison use, and keeping expensive Sauromancers available for their competing jobs"),
    (28, "LXXV", "Machaka", "Lion Kings", "totemic human clans, poison archers, spider riders, war lions, elephants, and semi-divine Colossi", "mixed recruitment, animal morale, poison exposure, trampling control, and scarce top-end commanders"),
    (29, "LXXVI", "Berytos", "The Phoenix Empire", "coastal trade, sailing human forces, Colossi, and sorcerer-queens with unusually wide magical access", "capital dependence, expensive mages, coastal staging, sailing limits, and balancing trade income against military replacement"),
    (30, "LXXVII", "Vanheim", "Age of Vanir", "glamour-protected Vanir, sacred cavalry, sailing, blood priests, and Air–Earth dwarven smiths", "elite scarcity, glamour counters, blood-hunting costs, sailing boundaries, and ordinary frontage"),
    (31, "LXXVIII", "Helheim", "Dusk and Death", "Valkyries, Helhirding cavalry, stealth and glamour, backed by Death–Air mages", "small elite armies, glamour counters, fragile support troops, expensive recruitment, and raiding without losing strategic concentration"),
    (32, "LXXIX", "Rus", "Sons of Heaven", "human hunters and berserkers, Chud elites, sacred bear skinshifters, and Air–Nature–Fire magic", "mixed troop quality, transformation behaviour, forest recruitment, limited armour, and distributing expensive mages"),
    (33, "LXXX", "Niefelheim", "Sons of Winter", "frost giants, Jotun infantry, skinshifters, and Water–Death–Blood magic under a cold dominion", "extreme gold costs, low model count, temperature, blood hunting, and replacing giants after attritional battles"),
    (34, "LXXXI", "Muspelheim", "Sons of Fire", "fire giants, Jotun support, and broad Fire–Air–Death–Glamour–Blood magic in a hot dominion", "extreme gold costs, temperature, scarce bodies, blood economy, and answering fire-resistant enemies"),
    (40, "LXXXII", "Pelagia", "Pearl Kings", "aquatic Triton clans, amphibious mermen, sacred Pearl Kings, and Water–Astral–Nature magic", "deep-water geography, limited land projection, commander coverage, and separating aquatic from amphibious replacement"),
    (41, "LXXXIII", "Oceania", "Coming of the Capricorns", "shapechanging Capricorns and aquatic forest forces able to work between sea and coast", "shape resolution, coastal transition, turmoil, land reinforcement, and mixed habitat requirements"),
    (42, "LXXXIV", "Therodos", "Telkhine Spectre", "spectral armies, Daktyloi smiths, island survivors, and a dominion that trades living population for ghosts", "population collapse, fort placement, ghost generation, mundane infrastructure, and moving from islands into living territory"),
    (43, "LXXXV", "Atlantis", "Emergence of the Deep Ones", "long-lived amphibious Deep Ones, Basalt Kings, heavy basalt weapons, and Earth–Water–Fire magic", "resource-heavy troops, slow movement, cold-water preferences, land transition, and expensive commanders"),
    (44, "LXXXVI", "R'lyeh", "Time of Aboleths", "Aboleth mind lords, enslaved aquatic peoples, mental domination, and powerful Astral–Water magic", "magic leadership, slave morale, mindless and enslaved troop control, land access, and friendly-fire risk"),
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
    brief = f"Early Age {name} converts {identity} into expansion, research, and strategic pressure. The pinned roster resolves {len(commanders)} commander identities and {len(troops)} troop identities across ordinary, regional, coastal, and site-linked recruitment, plus {len(spells)} active nation-restricted spell records. Its chief planning risks are {risk}."
    content = f"""# Part {roman}: Early Age {name}, {epithet}

## {name} one-page command brief

{brief}

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## {name} evidence and ruleset

This dossier covers unmodded Early Age {name} on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID {nation}, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

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
    return content.replace(f"\n## {name}", f"\n## Early Age {name}")


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
