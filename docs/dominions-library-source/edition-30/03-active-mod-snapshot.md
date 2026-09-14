# Active Mod Snapshot

## Frozen ruleset

The working modded library is now tied to two exact files rather than an uncertain Workshop state:

1. `DomEnhanced2_16.dm`
2. `Divinitus_1.15.3_DE.dm`

Dominions Enhanced is loaded first and Divinitus 1.15.3 DE second. Later commands can overwrite earlier definitions, so the combined result must be calculated in that order.

## File fingerprints

| File | Declared mod name | Declared version | Lines | Bytes | SHA-256 |
| --- | --- | ---: | ---: | ---: | --- |
| `DomEnhanced2_16.dm` | Dominions Enhanced v2.16 (Latest) | 2.16 | 194,385 | 5,675,140 | `72558697f8dae3a1fccf8fb57b3faccde56c7fe6c05dac6403cefe153faf6c1b` |
| `Divinitus_1.15.3_DE.dm` | Divinitus_1.15.3_DE | 1.15.3 | 44,436 | 1,348,538 | `cf7f21900a3812b66edddd831df779743eaf33080aef983f9bdea8ec47642809` |

Both files are UTF-8 text with CRLF line endings. Neither contains an active `#include` or `#includefile` directive. They are therefore mechanically self-contained even though referenced graphics remain in their normal mod folders.

## Scale of the supplied sources

An initial command inventory found:

### Divinitus 1.15.3 DE

- 1,514 new events;
- 373 selected monsters;
- 346 new monsters;
- 112 new sites;
- 75 selected items;
- 34 new weapons;
- 26 new spells;
- 17 selected spells;
- 5 selected sites;
- 2 new armours.

### Dominions Enhanced 2.16

- 4,227 selected monsters;
- 3,553 new monsters;
- 2,816 selected spells;
- 1,564 new events;
- 684 selected sites;
- 631 selected items;
- 504 new sites;
- 389 new weapons;
- 142 selected weapons;
- 132 selected nations;
- 81 new armours;
- 39 selected armours.

These counts describe active command occurrences, not necessarily the final number of distinct objects. A single object may be selected and modified several times.

## Load-order consequence

Dominions Enhanced first establishes the broad overhaul. Divinitus then revises pretenders and adds its event machinery on top.

This distinction matters whenever both files select the same object. For example:

1. Dominions Enhanced selects monster 3053, the Grand Hierophant.
2. DE gives it the base description, disease resistance 100, gold cost 30, path cost 20, Astral 2, Magic Resistance 18, Fortune Teller protection, and robes.
3. Divinitus later selects the same monster.
4. Divinitus replaces the description, raises gold cost to 150, applies `#magicboost 53 1`, increases bad-event protection to 75, retains disease resistance, and connects the pretender to new monthly events.

The combined Grand Hierophant is therefore not adequately described by either source in isolation.

## Grand Hierophant source confirmation

### Base established by Dominions Enhanced

Dominions Enhanced selects monster 3053 and establishes:

- base Astral 2;
- path cost 20;
- gold/design cost 30 before the later Divinitus overwrite;
- Magic Resistance 18;
- disease resistance 100;
- bad-event protection 50;
- humanoid item slots;
- robes.

### Final Divinitus layer

Divinitus 1.15.3 DE then applies:

- gold/design cost 150;
- `#magicboost 53 1`;
- bad-event protection 75;
- disease resistance 100;
- expanded description and four event systems.

Path number 53 means all non-priest magic paths. The displayed statement "Paths known are increased by 1" is therefore mechanically supported.

### Mystic anointment

A rarity-5 event:

- requires the Pretender to be monster 3053;
- targets a Mystic or Erytheian Mystic;
- requires a temple;
- applies a Holy boost;
- transforms the target into monster 382, the Mystic Prophet.

The description's monthly anointment claim is source-confirmed. The event has no ordinary message or log entry.

### Site-search treasure

A rarity-5 event:

- requires the Grand Hierophant to be the Pretender and the target;
- requires land;
- requires the Site Search order;
- requires positive dominion;
- uses `#req_domchance 5`;
- grants 150 gold;
- grants `#1d6vis 51`.

Gem-path group 51 is Elemental. A successful event therefore grants 1d6 Fire, 1d6 Air, 1d6 Water, and 1d6 Earth gems.

### Teaching Mystics

The main teaching event:

- requires the Grand Hierophant to be present;
- targets the transformed Mystic Prophet;
- visibly gates on the target's Astral threshold;
- requires land and positive dominion;
- uses `#req_domchance 5`;
- applies Astral, Fire, Water, and Earth boosts.

A separate Orphic Mystic event uses a slightly different path threshold and `#req_domchance 4`.

The broad description states a maximum of three, but the visible event gate is tied to Astral while all four paths are boosted. A Mystic beginning with a doubled element and S1 may therefore expose an elemental over-cap edge case. This is not asserted as engine behaviour; it is assigned to controlled testing. The Grand Hierophant guide explains the Mystic Prophet transformation and Orphic Mystic exception separately.

## Dominions Enhanced bless corrections

The supplied DE file directly confirms these opening changes:

| Bless | Unmodded/earlier cost | DE 2.16 cost or structure |
| --- | ---: | --- |
| Wasteland Survival | 2 | 1 |
| Death Explosion | 5 | 6, no longer Incarnate, Fire/Death |
| Fire Shield | 6 | 5 |
| Flaming Weapons | 7 | 4, no longer Incarnate, requires Heat 1 |
| Farshot | 2 | 1 |
| Awareness | 3 | 2 |
| Swiftness | 4 | 3 |
| Storm Flight | 4 | 3 |
| Wind Walker | 5 | 6, no longer Incarnate, Air/Astral |
| Weightlessness | 6 | 4, no longer Incarnate |
| Air Shield | 6 | 5 |
| Flight | 9 | 6 |
| Water Breathing | 6 | 2, no longer Incarnate |
| Recuperation | 5 | 4, no longer Incarnate |
| Vampiric Weapons | 12 | 9 |

These values supersede the older conversation summaries.

## What this unlocks

The supplied sources now make the following work possible:

- exact vanilla-to-DE object comparison;
- exact DE-to-DE-plus-Divinitus comparison;
- final Grand Hierophant and other pretender definitions after load order;
- complete MA Arcoscephale and MA R'lyeh modded deltas;
- bless and chassis legality checks;
- event-chain inspection;
- identification of overlapping IDs and compatibility problems;
- creation of a local mod-aware data index for later website tools.

## Cross-mod selector overlap

A first distinct-selector comparison found:

| Type | DE selected identities | Divinitus selected identities | Shared identities |
| --- | ---: | ---: | ---: |
| Monster | 3,185 | 373 | 357 |
| Item | 629 | 75 | 2 |
| Spell | 2,737 | 17 | 0 numeric selector overlap |
| Site | 572 | 5 | 0 numeric selector overlap |
| Nation | 128 | 0 | 0 |
| Weapon | 142 | 0 | 0 |
| Armour | 38 | 0 | 0 |

This table counts direct selected identities only. It does not capture the extensive cases where one or both mods use `#newmonster` on the same numeric identity.

## Corrected cross-action monster overlap

The complete numeric action screen finds:

| Relationship | Shared IDs |
| --- | ---: |
| DE new / Divinitus new | 235 |
| DE new / Divinitus selected | 10 |
| DE selected / Divinitus new | 114 |
| DE selected / Divinitus selected | 357 |

The groups are not disjoint because DE can create and later select the same monster. Divinitus touches 650 distinct fixed monster identities; 600 also appear in a DE monster action.

Divinitus also contains 69 automatically allocated new monsters and 26 automatically allocated new spells under the current documented `#newspell` syntax. Their numeric identities cannot be obtained from the two source texts alone; the independent integrity report records the complete pinned-Inspector resolution as versioned secondary evidence.

## Event registries

No nonzero event-code collision was found:

- DE: -540, -312 to -308, -302 to -300;
- Divinitus: -3333 and -513;
- both use zero as the official default/reset.

No event-variable collision was found:

- DE: 6001-6007 and 6011;
- Divinitus: 325, 326, 328-331.

## Global DE layer

DE applies six active global commands:

- `#gemlongevity 2`;
- `#slothincome 4`;
- `#turmoilincome 4`;
- `#deathincome 2`;
- `#deathdeath 25`;
- `#luckevents 7`.

The official Modding Manual defines gem-longevity level 2 as combat gems lasting the entire month.

## High-risk monster 8616 collision

DE creates monster 8616 as a hidden land bulk-crafting inventory depositer. Divinitus later creates 8616 as the Crystal Priest recruited from The Crystal Cavern.

This is a direct fixed-ID collision with divergent purposes. The official manual warns that two mods changing the same object can behave unpredictably. The runtime result remains pending rather than being described as a guaranteed overwrite.

## Divinitus source lint

- Fixed weapon ID 3034 is defined twice. Later references treat the second, Stellar Bolt definition as effective.
- Four Annunaki event blocks begin a new event without an intervening `#end`.
- One event has no explicit rarity.
- The public Divinitus 1.15.2 DE file said "Load first," while a later Workshop description said to enable it after DE; the supplied 1.15.3 header is silent.

## Next source-analysis tasks

1. Machine-readable command index - completed.
2. Event-code and variable registries - completed.
3. Cross-action fixed-ID screen - completed.
4. Resolve monster 8616 through exact-version inspector data or a reliable published reproduction.
5. Build resolved layered object cards on top of the source index.
6. Resolve nation-specific material only when the dossier programme resumes.
7. Compare a future source only when its release identity and hash can be pinned.
