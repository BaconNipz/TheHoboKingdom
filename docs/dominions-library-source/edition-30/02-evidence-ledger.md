# Dominions 6 Evidence Ledger

## Function

This ledger prevents a familiar problem in Dominions writing: an old forum answer, a Dominions 5 mechanic, a modded value, and a current manual rule can all look equally authoritative once they are copied into the same paragraph.

The public guides should remain readable. The detailed provenance belongs here.

## Evidence hierarchy

1. **Current in-game result or exported current game data**
2. **Current Illwinter manual or official change note**
3. **Exact mod source for the stated version and load order**
4. **Reproducible controlled test**
5. **Maintainer explanation**
6. **Detailed community test or tournament account**
7. **General guide, video, forum advice, or historical conversation**

Higher does not always mean more complete. The manual is authoritative but intentionally omits some hidden commands and edge cases. When a rule is absent, the answer is a documented test rather than confident interpolation.

## Preserved official files

| Source | Version/revision | Size | SHA-256 or status | Role |
| --- | --- | ---: | --- | --- |
| Dominions 6 Manual | Revision 2 | 449 pages | `65f430fd97c9f27285d63b797b43bc7fe3844241fdf40230b1d25a901ab9f33f` | Core rules, tables, lore, nations, spells, items |
| Dominions 6 Modding Manual | 6.34 | 65 pages | `5ac40698e05703f5628db123548c4e6a57fe0ed9bbcb65fb8f72fc589ab309ab` | `.dm` capabilities, IDs, units, spells, items, nations, AI templates |
| Dominions 6 Event Modding Manual | 6.29 | 20 pages | Official online source checked | Event requirements, effects, variables, orders, and chains |
| Dominions 6 Map Making Manual | 6.26 | 11 pages | Preserved | Maps, provinces, terrain, starts, and scenario structure |
| Dominions 6 File Formats | Unnumbered | 1 page | Preserved | Binary map recipe format |

The official documentation page describes the main manual as the rules-and-tables reference and explicitly separates the modding, event, map, and file-format documents.

Illwinter's public update record identifies Dominions 6.36, released on 17 August 2026 UTC, as the current base-game release checked on 25 August 2026. The main manual remains revision 2, while the auxiliary modding manuals carry their own interface versions. The large structured object register remains pinned separately to the 6.35 Inspector commit dated 26 May 2026.

## Current online source map

### Official

- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 changes](https://www.illwinter.com/dom6/changes.html)
- [Illwinter Dominions 6 page](https://www.illwinter.com/dom6/)
- [Dominions 6 Steam store](https://store.steampowered.com/app/2511500/Dominions_6__Rise_of_the_Pantokrator/)

### Structured game data

- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Mod Inspector source](https://github.com/larzm42/dom6inspector)

The inspector lists units, spells, items, sites, mercenaries, events, weapons, and armour and can load `.dm` files. Its own documentation warns that it remains under development and may contain missing or incorrect data. Important values must therefore be checked against the game or source.

### Community reference

- [Dominions 6 section of Illwiki](https://illwiki.com/dom5/dom6/start)
- [Dominions 6 subreddit](https://www.reddit.com/r/Dominions6/)
- [Illwinter Dominions subreddit](https://www.reddit.com/r/IllwintersDominions/)

Illwiki has useful topic pages for pretenders, dominion, combat, magic, communions, gems, sites, armies, testing, and nations. It is a research index, not a substitute for versioned verification.

Edition 23 specifically rechecked the current [unrest](https://illwiki.com/dom5/dom6/unrest), [supplies](https://illwiki.com/dom5/dom6/supplies), [starvation](https://illwiki.com/dom5/dom6/starving), and [Pretender-design](https://illwiki.com/dom5/dom6/pretenders) pages. Their useful formulas and terminology retain the Current Community Reference tier unless a linked reproduction supplies stronger evidence.

### Dominions Enhanced

- [Dominions Enhanced v2.16 Workshop page](https://steamcommunity.com/workshop/filedetails/?id=3539874770)
- [Dominions Enhanced source](https://github.com/BlueFeuer/DominionsEnhanced6)
- [Dominions Enhanced change notes](https://steamcommunity.com/sharedfiles/filedetails/changelog/3539874770)

Current facts captured on 28 July 2026:

- public version name: v2.16;
- Workshop last update shown: 16 June 2026;
- adds thousands of spells, items, and monsters, new nations, and changes across nearly every part of the unmodded game;
- the maintainer says compatibility with other mods should not be assumed unless explicitly stated;
- MA Arcoscephale is described as a mild overhaul with a rebuilt troop roster and sacred recruits in pairs;
- MA R’lyeh is marked updated;
- v2.16 fixes MA R’lyeh Void Power so it properly horror marks;
- current source says pretenders are broadly cheaper, Titans gain two paths, and Monsters/Rainbows gain one.

### Divinitus

- [Divinitus source](https://github.com/RonhulMaggot/Divinitus)
- Former Workshop page: `https://steamcommunity.com/sharedfiles/filedetails/?id=3404094034`

Current conflict captured on 28 July 2026:

- the Workshop page is marked removed and incompatible;
- its description still says a DE-compatible version exists, should load after DE, and is not fully integrated or balanced;
- comments refer to v1.15.3;
- the visible main branch contains regular and DE files through v1.15.2;
- recent Workshop comments report a combined DE + Divinitus recruitment problem for EA R’lyeh.

Public Divinitus sources remain inconsistent, so general claims about the "current stable version" should still be avoided. This project can now bypass that ambiguity by naming and hashing the exact supplied file.

### Frozen active mod snapshot

The exact files supplied for the working library are:

| File | Declared version | SHA-256 |
| --- | --- | --- |
| `DomEnhanced2_16.dm` | Dominions Enhanced 2.16 | `72558697f8dae3a1fccf8fb57b3faccde56c7fe6c05dac6403cefe153faf6c1b` |
| `Divinitus_1.15.3_DE.dm` | Divinitus 1.15.3 DE | `cf7f21900a3812b66edddd831df779743eaf33080aef983f9bdea8ec47642809` |

Both are complete `.dm` sources with no active include directives. This is enough to analyse rules and load-order overwrites; artwork is unnecessary for mechanical comparison.

## Claims already verified against official manuals

### Turn resolution

**Status: Official**

The Dominions 6 Manual revision 2 lists a 63-step hosting sequence on pages 55-57. Foundation Book I now preserves and explains every step.

High-value timing rules confirmed directly:

- messages and attached resources are sent at step 1;
- research resolves at step 2, and a researcher killed later still contributes;
- recruitment resolves at step 3 before attacks and movement;
- rituals resolve at step 10 in random caster order;
- remote attacks resolve at step 11;
- magic battles resolve at step 12;
- site searching resolves at step 14;
- assassinations resolve at step 20 before conventional movement;
- friendly movement resolves at step 24 and other movement at step 25;
- conventional movement battles resolve at step 26 and castle storming at step 27;
- global world effects resolve at step 28 after their casting at step 10;
- random events resolve at step 29;
- building construction resolves at step 35;
- special-order allies resolve at step 36 and are explicitly too late for that month's battles;
- Pillage resolves at step 37 before income at step 38;
- starvation resolves at step 40 after battles;
- upkeep resolves at step 41 after income;
- general dominion spread resolves at step 42 and dominion effects at step 43;
- healing and disease resolve at step 48;
- elimination resolves at step 56 and victory at step 57;
- due immortals reform at step 60.

The sequence is official. Strategic consequences derived from it are labelled separately in Foundation Book I, and ambiguous same-turn interactions have been assigned controlled tests.

### Province income and tax trace

**Status: Official**

The main manual revision 2 gives:

```text
Income base = Population / 100

Modified Income =
  (Population / 100)
  * dominion scale modifiers
  * (1 + fort administration / 200)

Final Income =
  Modified Income / (1 + unrest * 0.02)
```

A province produces no income if it cannot trace an unbroken friendly province line to a friendly fort. In disciple games the trace can pass through allied territory.

Income is collected at hosting step 38 after ordinary battles, construction, and Pillage, but before ordinary unrest alterations and upkeep.

### Resources and fort draw

**Status: Official, with rounding tests pending**

- An unfortified province uses half its potential resources locally.
- A fortified province uses its full local potential.
- A fort draws its Administration percentage from eligible adjacent provinces' potential resources.
- Land and sea do not donate across their boundary.
- A fort does not draw from an enemy province or an adjacent province containing another fort.
- A shared unfortified neighbour can contribute to more than one fort.
- Unrest modifies the final pool as `Resources / (1 + unrest * 0.01)`.
- Unrest 100 halves resources and prohibits recruitment.

The manual's worked example supports drawing from potential rather than the neighbour's displayed half pool. It explicitly rounds one 13.8 contribution down to 13, but its aggregate arithmetic does not reconcile cleanly enough to establish every rounding stage. Exact rounding and overlapping-draw edge cases remain assigned to reproduction.

### Recruitment Points and recruitment gates

**Status: Official formula; rounding pending**

Recruitment Points begin at 20 and add population-band contributions:

- first 5,000 population at one point per 100;
- 5,001-10,000 at one per 200;
- 10,001-20,000 at one per 300;
- 20,001-40,000 at one per 400;
- population above 40,000 at one per 500.

The fort recruitment bonus is applied afterward. Order or Turmoil changes Recruitment Points by 10% per step. The official 6,000-population example is `20 + 5,000/100 + 1,000/200 = 75`.

The manual separately establishes gold, resources, Recruitment Points, Commander Points, Holy Points, and limited recruitment as possible gates. Older community pages preserving a different Recruitment Point formula are treated as historical, not current proof.

### Commander Points

**Status: Official fort ladder plus current Community-tested base**

The ordinary local pool is one base point plus the current fort bonus:

- no fort or Palisades: 1;
- Fortress or Castle: 2;
- Citadel or Grand Citadel: 3.

The official manual provides the fort bonuses and states that fort statistics replace rather than stack. The current commander reference, last revised under 6.35, supplies the unfortified base and multi-turn accumulation rule. The Modding Manual establishes that `#slowrec` doubles a commander's point cost and that explicit recruitment-point costs can be assigned. The main manual explicitly excludes Commander Points and Holy Points from AI difficulty bonuses. No 6.36 announcement changes this model.

R-009 is complete at the stated mixed evidence tier. Exact unrest reductions remain the separate R-011 question.

### Unrest and recruitment capacity

**Status: Official shutdown; current community formula; integer boundaries pending**

The revision-2 manual establishes that unrest 100 or greater prevents ordinary unit and commander recruitment. It does not state a below-100 formula for Recruitment Points or Commander Points.

The current community unrest reference says each unrest point removes one percent of Recruitment Points and that Commander Points are affected similarly, with the effect rounded down. It does not publish a version-labelled save, boundary table, or procedure, and the phrase "effect rounded down" does not identify whether the engine rounds the amount lost or the capacity remaining.

Under the loss-floor interpretation, ordinary Commander Point pools of one, two, and three first lose a point at unrest 100, 50, and 34 respectively; a three-point pool would lose a second point at 67. These are candidate predictions for R-011, not current laws. The recruitment interface remains authoritative below the official shutdown.

### Upkeep

**Status: Official core; Sacred-Slave and mounted cases Community-tested; shapes pending**

- Most non-summoned gold-recruited units cost gold cost divided by 15 each month.
- Sacred units and slaves cost gold cost divided by 30.
- Most summoned units have no ordinary upkeep.
- Upkeep is charged at hosting step 41 after income.

A 6.33 in-game observation reports that Sacred and Slave reductions stack to a divisor of 60. The same report gives Logrian Cavalry as an exact component check: the 10-gold rider displays 8 annual upkeep and the 20-gold War Horse displays 16, for 24 total. The pinned 6.35 object rows independently preserve separate rider and mount base costs and separate Sacred or Slave tags. No general upkeep change appears in 6.34-6.36.

The same observation records annual values of 6 for a 7-gold ordinary unit and 13 for a 16-gold ordinary unit. Exact annual equivalents are 5.6 and 12.8, so a simple final floor is excluded for those samples. They do not distinguish a ceiling from ordinary nearest-integer rounding and do not reveal monthly treasury aggregation.

The Modding Manual defines `#addupkeep` as adding to the gold basis used for upkeep. Monthly fractional aggregation and the basis used across every shape type remain pending under R-010.

### Supplies and starvation

**Status: Official core; one internal manual conflict**

Population supply:

- first 15,000 population at one supply per 30;
- additional population at one per 60;
- Growth/Death applied first;
- temperature applied second.

Fort supply is stated as `(Administration * 6)/(Distance + 1)`, to a maximum distance of four, with only the highest fort contribution used.

The printed distance-multiplier table instead corresponds to `(Administration * 4)/(Distance + 1)`. Its Administration-30, distance-three example gives 30 and agrees with that second formula; a separate Administration-50 adjacent example gives 150 and agrees with the multiplier of six. All distances require a controlled 6.36 reproduction.

The starvation rules are official:

- selected troops consume approximately the supply deficit;
- first starvation applies -4 morale and 5% disease chance;
- repeated starvation raises disease chance to 50%;
- appropriate survival gives a 50% chance to be unaffected and another 50% chance to avoid disease;
- restored supply ends Starving but not existing disease.

The official `#neednoteat` definition means the unit consumes no supplies and cannot starve; the same passage proves that consumption and starvation eligibility can be separated. Official update 6.18 confirms that transformation into a non-eating entity removes Starving. The 6.35 structured snapshot contains 985 Need Not Eat rows and 47 rows combining Need Not Eat with Appetite, reinforcing the separation.

Generic commander immunity is not official. Community sources describe feeding priority, but a current selection-boundary reproduction remains pending under R-013.

Official update 6.35 fixed Supply Usage not refreshing after magic-item changes. This makes the current display the intended operational total after equipment changes and makes older equipment-change screenshots version-sensitive; it does not settle starvation priority.

### Forts, buildings, and sieges

**Status: Official**

Standard fort statistics:

| Fort | Cost | Time | Admin | Commander Points | Recruitment bonus | Storage | Wall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Palisades | 1000 | 5 | 15 | +0 | +50% | 150 | 200 |
| Fortress | 600 | 3 | 30 | +1 | +75% | 750 | 500 |
| Castle | 600 | 3 | 45 | +1 | +100% | 2500 | 1000 |
| Citadel | 600 | 3 | 60 | +2 | +125% | 7500 | 1500 |
| Grand Citadel | 1000 | 5 | 70 | +2 | +150% | 10000 | 2000 |

Costs and times apply to each stage; statistics replace rather than stack.

Construction and demolition resolve at step 35. Any commander can build a fort; sacred commanders build temples; mages build labs. Any commander can demolish a fort or lab in one month. Temples cannot be demolished by order and are automatically destroyed on enemy capture. A fort cannot be demolished while besieged.

Siege formulas:

```text
Reduction strength = Strength squared
Repair strength = Strength squared / 2
```

Flying doubles contribution. Mindless defenders receive one-eighth repair value; Animals and Undisciplined units receive half. Only Maintain Siege forces contribute. A storm becomes available after zero wall integrity and resolves after movement battles.

Siege storage is divided by consecutive siege turn: 300 storage provides 300, 150, 100, 75, 60 in the first five months.

### Province Defence

**Status: Official**

- First PD is free.
- Each later point costs gold equal to the level purchased.
- Total cost to level `n` is `n(n+1)/2 - 1`.
- PD 10 costs 54 gold.
- Maximum is 100.
- It has no upkeep and restores after battle when control is retained.
- Every full 10 PD reduces unrest by 1 each turn.
- Stealth detection begins at 15.
- The manual's numerical example supports patrol strength `PD - 14`.
- Each point requires 10 population.
- PD cannot voluntarily be reduced.
- Capture wipes PD; disciple relinquishment reduces it by 25%.

Specific national combat value and commonly recommended breakpoints are strategic or community claims, not universal rules.

### Magic sites and Blood Hunting

**Status: Official**

Magic sites:

- have search difficulty 1 through 4;
- require equal path level for manual discovery;
- never require more than path 4 for ordinary searching;
- are more common in several resource-poor or unusual terrains and less common in farms and plains;
- can produce gems, gold, recruits, access orders, benefits, or harms;
- may operate while undiscovered;
- may require a lab for some functions;
- do not necessarily grant foreign national recruits after capture.

Blood Hunting:

```text
Blood success = 10 + Blood level * 30 percent
Population success = population / 75 percent
Unrest failure = unrest / 4 percent

Success: slaves = d6 + Blood level
         unrest += d(slaves * 3 + 4)

Failure: no slaves
         unrest += d6 - 1
```

Every five percentage points of site frequency changes average yield by 0.5 slaves. Strong friendly dominion reduces commoner retaliation; dominion 10 makes it almost disappear according to the manual.

### Scale economy baseline and remaining conflicts

**Status: Two values resolved from current official documentation; other boundaries remain open**

| Rule | Main manual revision 2 | Modding Manual 6.34 or other evidence | Publication state |
| --- | ---: | ---: | --- |
| Growth/Death income | 1% per step | `#deathincome` default 2 | Use 2% for unmodded 6.36; newer explicit official default governs |
| Order/Turmoil resources | 2% per step | No later official change through 6.36 | Use 2% for unmodded 6.36 |
| Order/Turmoil income | 3% per step | A main-manual prose example implies 2% per step | Repeated tables win; example treated as typo |
| Fort supply distance | Formula, multiplier table, and example disagree | No higher official resolution found | Reproduce every distance |

### Pretender design

**Status: Official**

- Each nation begins with 450 design points before the physical-form cost.
- Purchased magic levels cost 8, 16, 24, 32, 40, 48, 56, 64, 72, and 80 points in sequence.
- The sequence counts levels added by the player, not the final displayed path.
- Opening an absent path uses the form's New Path Cost for the first level, then resumes at 16 for the second added level.
- Added dominion candles cost 7, 14, 21, 28, 35, 42, 49, 56, and 63 points.
- Each favourable scale step costs 40 points and each unfavourable step grants 40.
- Only the first three temperature clicks away from national preference grant design points.
- Dormant grants 150 points and ordinarily awakens around turns 10-13.
- Imprisoned grants 350 points and ordinarily awakens around turns 28-42.
- Disciples awaken in approximately half the corresponding Pretender time.

The manual deliberately gives awakening ranges. A surviving reverse-engineering page for Dominions 5 proposes repeated exploding-die checks and identifies exact historical formulas, but the page ties its mechanics to an older Dominions 5 patch. It is retained only as a candidate model for a current test. Exact Dominions 6 distributions remain assigned to R-014.

A Dominions 6 community Pretender page revised on 16 June 2026 now republishes the same `9 + d4!`, `27 + d20!`, `4 + d4!`, and `13 + d20!` model. Source tracing finds the same wording and constants in Loggy's older miscellaneous notes and in copies published before Dominions 6. The current page supplies no 6.x raw outcomes or engine trace and gives usual displayed ranges one turn later than the revision-2 manual for Dormant and the early Imprisoned boundary. Its republication advances source visibility, not the evidence tier. R-014 remains queued.

### Dominion

**Status: Official core**

Dominion sources:

- Pretender: one automatic increase and two temple checks;
- home province: one temple check;
- Prophet: one temple check;
- temple: one temple check;
- Disciple: one temple check;
- claimed Throne: one to seven checks, depending on the Throne.

Maximum dominion:

```text
initial Pretender dominion
+ floor(temples / (5 * players on team))
```

Temple-check trigger chance:

```text
50% + 5% * maximum dominion
```

For a successful check in friendly dominion `U`, the chance of a local increase is:

```text
30% - 3% * U
```

Failure propagates the check to a random neighbour.

For enemy dominion `E`, the chance to reduce one candle is:

```text
50% + 5% * maximum dominion - 5% * E
```

A randomly selected destination crossing the land-sea boundary has a 50% chance to be rerolled.

Preaching:

```text
neutral or friendly chance = 30% * effective Holy
enemy chance = 30% * effective Holy - 5% * enemy candles
minimum enemy chance = 5%
local cap = 2 * effective Holy
```

A local temple adds 0.5 effective Holy for chance and cap. Inquisitors double Holy level only in enemy dominion. Heretics have a `Heretic value * 20%` chance to reduce local dominion.

Blood-sacrificing priests in temples may consume slaves up to Holy level, with each slave producing one temple check.

Dominion is separate from province ownership. A nation with no friendly candles anywhere is eliminated even if it retains provinces, forts, armies, or a living god.

**Tests pending:**

- whether chances above 100% in scale convergence produce two steps;
- exact fractional-Holy and above-100% preaching handling;
- whether claimed-Throne checks are guaranteed in current 6.36;
- precise check targeting under unusual adjacency and multiple planes.

### Dominion effects

**Status: Official**

- All units receive +1 Morale in friendly dominion and -1 in enemy dominion.
- Pretenders and Prophets receive +1 Strength, +0.5 MR, and +10% Hit Points per friendly candle, reversed in enemy dominion.
- Hit Points cannot fall below 10% through hostile dominion.
- Each scale has a monthly chance to move toward the god's design equal to `5% * local candles + 10% * absolute difference`.
- Scales at 4 or 5 can spread into neighbouring provinces even outside the originating god's dominion.

### Bless-point and activation rules

**Status: Official core**

- Each path level above 1 grants one bless point.
- An effect's bless-point cost normally equals the sum of its path requirements.
- Scale prerequisites add no bless-point cost.
- Some effects can be bought repeatedly and stack.
- Blessing a sacred grants +1 Morale, the Pretender's selected blessing, and claimed-Throne blessing effects available to the nation or team.
- Pretenders and Disciples are automatically blessed in friendly dominion.
- The main manual states that Pretenders and Disciples are not ordinarily blessed outside friendly dominion; priests do not supply an outside-dominion bypass.
- Sacred troops fighting alongside the Pretender are automatically blessed when the battle is in friendly dominion.
- The main manual does not extend that troop-wide rule merely for fighting beside a Disciple; broader community wording is not promoted without stronger evidence.
- Passive or innate effects do not require battlefield blessing.
- Incarnate effects operate only while the Pretender is active on the map and alive; same province, same battle, and friendly dominion are not additional Incarnate requirements.
- Fear and Dread do not stack; Displacement supersedes Blur, and invisibility no longer stacks with Blur or Displacement.
- Weapon blessings have distinct trigger classes: Magic Weapons changes the parent weapon, several riders trigger on hit, Withering/Poison/Vampiric require a damaging hit, Frost Mist creates an attack-generated cloud, and Reanimators follows its own probabilistic rule.
- Item commands distinguish unconditional item blessing from sacred-only automatic blessing; supported item effects may separately propagate to a mount.
- Rider and mount Sacred states are independent records. No universal state-transfer rule is inferred from a mounted card.

The revision-2 printed blessing list is no longer a fully current numerical source.

| Blessing | Revision-2 manual | Current evidence | Status |
| --- | --- | --- | --- |
| Heroism | +50% experience | Official update 6.08 changed it to +35% | Officially superseded |
| Inspirational Presence | Fire 4 in printed table | The 6.35 structured data reference uses Fire 3 and treats it as innate, stackable, non-Incarnate; no 6.36 announcement changes it | Current data reference with official 6.36 overlay; reproduce if a runtime dispute arises |
| Frost Mist Weapons | Water 7 and Cold 1 | Current reference agrees | Earlier unsupported removal of the Cold requirement was reversed |
| Cancel loaded Pretender | Cancel should discard the unwanted design | 6.36 fixed cancelled designs leaving bless effects loaded | Officially corrected |

Foundation Book III preserves the complete 6.35 structured bless table with official changes through 6.36 while keeping its status distinct from rules directly confirmed by the revision-2 manual. R-016 is complete at this scope; cross-source stacking and transformation lifetime remain R-049, R-040, and R-052.

### Divine Magic

**Status: Official**

- Divine spells use Holy skill rather than ordinary magic paths and require no research.
- Banishment and Smite are replaced by path-themed versions when the Pretender has a path at level 4 or higher.
- The highest qualifying path determines the family; ties use the priority order printed in the manual.
- Blood has a Smite replacement, Claim Life, but no Banishment replacement.

The replacement families are:

| Path | Banishment | Smite |
| --- | --- | --- |
| Fire | Ashes to Ashes | Heavenly Fire |
| Air | Wind of Memories | Heavenly Strike |
| Water | Purifying Water | Watery Death |
| Earth | Pull from the Grave | Word of Stone |
| Astral | Stellar Decree | Word of Power |
| Death | Decree of the Underworld | Syllable of Death |
| Nature | Final Rest | Word of Thorns |
| Glamour | Return of the Past | Word of Bewilderment |
| Blood | None | Claim Life |

### Pretender death and recovery

**Status: Official core**

- Each ordinary death removes either one magic-path level or one dominion-strength point.
- The chance to lose magic is `50% + 10% * Nature level at death`.
- If no magic is lost, dominion falls by one; dominion cannot fall below 1.
- Nature is the most exposed path and Death the least; small chances exist to gain Death and smaller chances to gain Astral or Blood.
- Dominion Immortals normally reform after death in friendly dominion.
- Immortals normally reform on the ordinary plane regardless of dominion.
- Soul destruction and death on a remote plane can bypass ordinary immortality and require Call God.
- Reform is often about three months but can vary by form.
- Normal immortal reform removes most afflictions.

The revision-2 manual describes Call God as accumulating around 50 points, with each priest contributing Holy level per month, and increases the main Pretender's requirement by 50% in a Disciple game. It deliberately locates uncertainty in the total. The Modding Manual adds the unit's Elegist value and applicable nation or claimed-Throne `#recallgod` value to effective priest level; the main manual says a dead Trinity member returns in half the normal time.

Published controlled research resolves the ordinary discrepancy at **Community-tested** tier: the base target is fixed at 50, while each priest contributes effective recall rating `-1`, the rating itself, or `+1` per month, with the three outcomes observed at equal or nearly equal weight. An H1 therefore contributes 0-2, H2 contributes 1-3, and H3 contributes 2-4. The manual's Disciple-game increase gives a 75-point main-Pretender target when combined with the tested base. Current community documentation supplies cross-team Disciple routing and detailed capital/fort return placement; those details remain **Current Community Reference** rather than official text.

Call God resolves at hosting step 16. Priests removed before that step cannot safely be counted; deaths in later assassinations or ordinary battles cannot retroactively remove the month's contribution. Official update 6.28 repaired issuing the order without its shortcut and did not change the formula. R-017 is complete at this mixed evidence tier, with direct 6.36 regression testing retained as an upgrade path.

### Special dominions

**Status: Official category map; exact nation tests pending**

The manual establishes special dominion systems including:

- Arcoscephale's dominion scrying;
- Mictlan's dying dominion and blood-sacrifice dependence;
- Yomi's temple Oni;
- MA Ermor and MA Asphodel population conversion;
- MA C'tis's Miasma;
- MA Agartha's Golem Cult;
- LA R'lyeh's Dreamlands;
- Phaeacia's dominion-enabled dark ships;
- EA Therodos's population death and fort ghosts;
- Mekone's dominion-conflict modifier;
- Phlegra's dominion unrest;
- dominion-based information hiding for Ubar, Na'Ba, Ind, and Feminie.

Disciple inheritance, underwater operation, candle scaling, and friendly-versus-hostile targeting require nation-specific tests before publication as exact formulas.

### Active mod Pretender, scale, and blessing overrides

**Status: Source-confirmed**

Dominions Enhanced 2.16 changes global scale defaults:

```text
#slothincome 4
#turmoilincome 4
#deathincome 2
#deathdeath 25
#luckevents 7
```

It also directly selects 46 base blessings. Major changes include cheaper survival blessings, numerous reduced costs, several cross-path requirements, and the removal of Incarnate dependence from Death Explosion, Flaming Weapons, Wind Walker, Weightlessness, Slowing Weapons, Vitriol Weapons, Water Breathing, Frost Mist Weapons, Reanimators, Recuperation, Berserker, and Barkskin.

The supplied Divinitus 1.15.3 DE file contains no direct blessing selection or creation commands. It does contain hundreds of form-level `#startdom`, `#pathcost`, awakening-restriction, and scale-limit commands. Under the frozen load order, DE supplies the global blessing table while later Divinitus selections can override matching Pretender objects.

Command counts are evidence of rewrite scope, not counts of unique final objects.

### Active mod economy overrides

**Status: Source-confirmed**

Dominions Enhanced 2.16 contains:

```text
#slothincome 4
#turmoilincome 4
#deathincome 2
#deathdeath 25
#luckevents 7
```

For the exact supplied file this means:

- Order/Turmoil income: 4% per step;
- Productivity/Sloth income: 4% per step;
- Growth/Death income: 2% per step;
- Growth/Death population change: 0.25% per month per step;
- Fortune/Misfortune event-frequency change: 7% per step.

Divinitus 1.15.3 DE does not redefine those global commands, so its later load position does not reset them.

Neither supplied file globally changes population per gold, resource multiplier, supply multiplier, unrest needed to halve income, or unrest needed to halve resources. Both files contain many object-level economic commands, so nation-specific conclusions still require object and load-order analysis.

### Communions

**Status: Official**

- A valid communion needs at least one master effect and one slave effect.
- Masters gain levels only in paths they already possess.
- Two slaves grant +1; four grant +2; further bonuses follow powers of two.
- Spell fatigue is divided among all participants, then modified by relative path levels.
- Slaves cannot act independently while in the communion.
- Slaves benefit from single-target range-0 self-buffs cast by communion masters.
- Loss of every master produces slave backlash: about one round of stun and 3d50 fatigue per slave.

### Wish

**Status: Partly official**

- Alteration 9.
- Astral 9.
- 100 pearls.
- The result can be harmful.
- Artifacts and magic gems are suggested as relatively safe wishes.

The command vocabulary and quantities are not confirmed by the manual.

### Nexus Gate

**Status: Official**

- Thaumaturgy 9.
- Astral 5 Earth 3.
- 40 pearls.
- Creates a permanent gate to Nexus.
- Cannot be dispelled.
- Nexus links all active Nexus Gates and is located in the Void.

### Tartarian Gate

**Status: Official**

- Conjuration 9.
- Death 7.
- 7 death gems.
- Releases a dead Titan or Monstrum whose imprisonment may have destroyed its mind.

### Divine Name

**Status: Official**

- Thaumaturgy 7.
- Astral 5.
- 25 pearls.
- Can give a mindless target an artificial mind and command.
- Can give a willing target commanding ability and improved mental faculties.

### AI templates

**Status: Official**

The modding manual exposes:

- nation-specific AI templates;
- pretender form, awakening, paths, dominion, scales, and blesses;
- ordered research targets through `#researchgoal`;
- ritual and item priorities through `#favrit`.

The manual warns that research will mostly, but not exactly, follow the requested goals.

### Event response orders

**Status: Official**

The event manual exposes:

- `#order <bitmask>`;
- Investigate 1;
- Continue 2;
- Accept 4;
- Decline 8;
- Withdraw 16;
- Attack 32;
- Diplomacy 64;
- Subterfuge 128;
- Magic 256;
- target-order numbers 100, 101, 102, 103, 105, 106, 107, and 108 respectively, with no target-order entry shown for Withdraw.

This proves that event-driven choices can be built. It does not prove that formal diplomacy itself can be expanded.

### Formation-related modding

**Status: Official limits plus negative finding**

Confirmed commands:

- `#formationfighter <xsize>` changes square density;
- `#undisciplined` restricts the unit to Skirmish and prevents ordinary battle orders;
- `#skirmisher` modifies skirmishing behaviour.

No command for creating an additional selectable formation has been found in the current modding manual. This is a negative finding, not proof that no executable-level method could ever exist.

### Battle termination and long-battle limits

**Status: Official**

- A squad routs after failing a morale check.
- Eligible troops rout when all eligible commanders have been killed or routed.
- An army automatically routs at 75% weighted total-HP casualties.
- At battle turn 100, Twilight removes battle enchantments and temporary magic effects and ends berserk.
- At turn 150, the attacker routs.
- At turn 170, the defender routs.
- At turn 200, remaining units die.

Mounts and Province Defence contribute 25% of HP to the army total; slaves contribute 50%.

### Leadership, squads, and formation

**Status: Official**

- One commander can control five squads.
- A square normally holds ten size points.
- Base Leadership 10, 50, 100, 150, and 200 use different squad-count morale bands.
- Experience increases capacity but does not change the base leadership band used for the morale modifier.
- Mixing undisciplined with ordinary troops makes the squad undisciplined and imposes -1 morale.
- Mixing undead with living or demons with ordinary troops imposes -1 morale.
- Sparse line and skirmish impose -1 morale unless an applicable ability removes it.
- Undisciplined units are normally restricted to skirmish and cannot receive ordinary specific orders.
- Tight Rein removes those undisciplined restrictions for the commander's units.

### Melee and shields

**Status: Official**

```text
Attack roll  = Attack + DRN - fatigue penalty
Defence roll = Defence + DRN - fatigue penalty
Damage roll  = Strength + weapon Damage + DRN
Protection   = relevant Protection + DRN
               + shield Protection on a shield hit
```

The attacker must exceed Defence. A shield hit occurs when the attack defeats Defence but not Defence plus Parry. The shield then adds Protection.

Fatigue reduces Defence by one per ten points and Attack by one per twenty. Protection die results 2, 2-3, and 2-4 can bypass 25% Protection against targets below 50, at least 50, and at least 100 fatigue respectively. Immobilised and unconscious units count as 100 fatigue for this purpose.

Piercing reduces Protection 15%; Armour Piercing reduces it 50%; the two stack to 65%. Blunt, slashing, shield-breaking, reach, underwater, two-handed, and multiweapon rules are recorded in Foundation Book IV.

### Harassment and repel

**Status: Official core; decay test pending**

- Every directed melee attack gives one harassment point and -1 Defence.
- Weapon multiattacks give one point per attack.
- Ranged and area attacks do not give harassment.
- Rider and mount are separate harassment targets.
- A longer defending weapon automatically attempts repel.
- Repel combines an attack check, a morale comparison, and possible one-point damage.
- Size-6 or larger giants count their weapon as one length longer for repel.

The manual says harassment and the repeated-repel penalty decay over time but does not expose complete decay functions.

### Missile attacks

**Status: Official**

```text
deviation = range x 1.25 / Precision

square-hit attacker
= DRN + half size points in square + 2 if magical

square-hit defender
= DRN + twice shield Parry - Fatigue / 20
```

Precision above ten counts double for the excess. Individual targets within a square are selected with size weighting. Missiles can hit friendly units.

### Mounted units and trampling

**Status: Official core with current official corrections**

- Rider and mount are separate targets and both can attack.
- Area effects and lightning can hit both.
- Trample targets the mount.
- A two-handed rider has -3 Attack while mounted.
- Riders, mounts, morale, falling, post-battle matching, rerecruitment, and commander mount recovery have separate rules.
- Automatic mount recovery occurs at end of turn as of 6.35.
- Floating mounts are no longer impeded by non-floating riders as of 6.23.

Trample displaces smaller units. Victims check `Defence - Fatigue/10` against `3d6`. Failure causes `7 + trampler Size` armour-piercing damage; success still causes displacement and one damage. Ethereal tramplers deal half trample damage.

### Fatigue

**Status: Official core; active recovery test pending**

- Melee attacks add current Encumbrance.
- Defence loses one per ten fatigue.
- Attack loses one per twenty.
- At 100 fatigue a unit falls unconscious.
- An unconscious unit recovers five fatigue per turn until below 100.
- Fatigue is capped at 200; further fatigue damage converts to HP damage.
- Spell fatigue is divided by one plus path skill above minimum.
- Casting also adds base Encumbrance plus twice armour Encumbrance, which excess path skill does not reduce.

Current official corrections:

- non-mounted flying and trample fatigue were corrected in 6.25;
- spellcasters no longer pay the multiple-weapon fatigue penalty as of 6.23.

The manual does not fully settle ordinary active-unit recovery outside the explicit unconscious rule.

### Morale, fear, and retreat

**Status: Official core; survivor-bonus formula test pending**

Morale checks compare:

```text
squad Morale + DRN + survivor bonus from 0 to 5
against
14 + DRN
```

The squad routs only if the second result is greater. Triggers include heavy losses with at least 20% total casualties, damage to a squad of four or fewer, Fear, forced fear effects, and army casualties of at least 50% weighted HP.

Current Fear can lower morale by no more than the effect's value and never by more than ten.

Commanders have a 75% chance of smart retreat, with a second 50% chance in native terrain. Smart retreat prioritises a friendly local fort, then a random friendly adjacent province. Troops check to follow; undisciplined troops suffer -3. Retreat into enemy territory kills the unit.

### Resistances and special damage

**Status: Official core**

- Resistance acts as an additional protection layer followed by twice-resistance percentage reduction; 50 gives immunity.
- Elemental resistance counts double against elemental fatigue effects.
- Fire, burning, freezing, bleeding, poison, shock, acid, rust, life drain, paralysis, fatigue damage, false damage, and battlefield clouds have separate rules.
- False damage causes no ordinary afflictions, is not healed normally, does not trigger several retaliation or bond effects, and dissipates when hostile Glamour mages are gone.
- Current official rules count false damage toward HP-based rout.

Foundation Book IV preserves the formulas and assigns uncertain rounding to controlled tests.

### Afflictions and regeneration

**Status: Official core with current official correction**

- Basic affliction chance equals the percentage of maximum HP lost to the blow.
- Major-affliction chance is the affliction chance divided by 1.5, capped at 33%.
- Hit location controls the affliction pool.
- Regeneration reduces affliction risk.
- Regeneration follows its displayed percentage accurately as of 6.31 rather than the previous HP brackets.

### Battle magic

**Status: Official core with current official corrections**

- Battle spells have preparation and recovery time.
- Interruption chance from a hit during preparation is percentage of maximum HP lost plus 25%.
- Combat Caster and Mindless halve interruption chance.
- Innate casters have no preparation time and ignore ordinary casting times.
- Spell Precision adds to caster Precision.
- MR-negates effects compare `11 + DRN + half excess caster skill` against `MR + DRN + half target skill in the spell path`; the caster wins ties.
- Battle enchantments end when their caster dies and at Twilight.
- Battlefield-wide spells cannot normally be cast indoors as of 6.25, except holy spells.
- Innate casters correctly resume their script after unconsciousness as of 6.35.

### Magic access, paths, and research

**Status: Official core**

- A spell requires the necessary school research, every listed path, and any required gems or slaves.
- Multi-path spells use the first listed path as primary for excess-skill fatigue; rituals use the primary gem type.
- Boosters and battlefield path-boost spells require at least level 1 already.
- A combat gem can raise a known path by one for one spell, never more than one and never from zero.
- Empowerment is the general route to a new path: 50 gems for the first level and `15 x target level` thereafter.
- Ordinary research is `5 + 2 x total magic levels +/- bonuses or penalties`, minimum 1.
- Dementia halves research.
- Divine Insights is capped at the province's friendly dominion candles per laboratory.
- Philosophers gain from Sloth and ignore Magic/Drain.
- Level 9 of each school except Construction contains individually selected legendary spells.

### Gems, rituals, and alchemy

**Status: Official core; combat AI and rounding test pending**

- Sites contribute gems to the treasury while connected through friendly territory to a friendly laboratory.
- Pool gathers carried gems from commanders in a laboratory province.
- Combat gems provide a one-spell path increase and/or fatigue relief.
- A mage cannot spend more gems in a combat turn than current skill in the path.
- Conservative gem use restricts spending to sparing scripted use.
- Rituals require a laboratory, consume a monthly order, and draw gems automatically from the treasury.
- Rituals resolve at hosting step 10 in random caster order; remote attacks are step 11, magic battles step 12, site searches step 14, and globals take world effect at step 28.
- Ordinary treasury alchemy converts non-Astral gems to pearls or pearls to another type at 2:1, making non-Astral-to-non-Astral conversion 4:1.

### Global enchantments

**Status: Official core**

- Game setup permits 3, 5, 7, or 9 global slots.
- An open slot accepts a differently named global; a same-name cast contests the incumbent; a full board makes a different global contest a random incumbent and may select the caster's own.
- Casting order among mages is random.
- Ritual gem spending is capped at path level times 100.
- Global or Dispel contest strength gains +1 per extra gem and +5 per caster path above the requirement, then adds a DRN.
- Most globals end on caster death; immortality does not preserve them through death.
- Some globals also end when their origin province is conquered.
- Domes can protect units against many globals, but strikeback domes do not retaliate against the global caster.
- Dominion-limited globals can be countered in a province by removing hostile dominion.

### Forging, artifacts, and path access

**Status: Official core; stacking and rounding test pending**

- Forging requires a qualified mage in a friendly laboratory, sufficient Construction, paths, and gems.
- Ordinary item tiers are Construction 1, 3, 5, and 7; Construction 9 unlocks unique artifacts.
- Base item cost per required path is 5, 10, 15, 20, 30, 40, 55, and 70 gems for requirements 1 through 8.
- Multi-path items charge each required gem type.
- Unique artifacts have one world copy.
- Yearning halves artifact cost. Construction 9, Forge of the Ancients, the Throne of Creation, and the Throne of the Artificer each add 50 percentage points to the monthly yearning rate.
- Master Smith changes forging eligibility; Forge Bonus changes cost. Exact combined stacking and rounding remain test pending.

### Legendary and late-game magic

**Status: Official requirements; command vocabularies and outcome distributions test pending**

- Wish is Alteration 9, S9, and 100 pearls in the revision-2 manual.
- Nexus Gate is Thaumaturgy 9, S5E3, and 40 pearls; the gate is permanent and joins the shared Nexus network.
- Tartarian Gate is Conjuration 9, D7, and 7 Death gems; results can have destroyed or impaired minds.
- Arcane Nexus is Enchantment 9, S8, and 150 pearls; it gathers pearls equal to one quarter of non-Astral, non-Blood gems spent on rituals, forging, and empowerment, plus its stated ambient effect.
- Exact current Wish strings, aliases, random results, and mod restrictions require controlled tests.

### Active mod magic scope

**Status: Source-confirmed**

The supplied files contain extensive magic-object commands:

| Command family | DE 2.16 | Divinitus 1.15.3 DE |
| --- | ---: | ---: |
| `#newspell` | 0 | 26 |
| `#selectspell` | 2,816 | 17 |
| `#copyspell` | 1,230 | 12 |
| `#school` | 1,403 | 38 |
| `#researchlevel` | 1,820 | 35 |
| `#path` | 2,594 | 121 |
| `#pathlevel` | 2,293 | 7 |
| `#fatiguecost` | 1,769 | 21 |
| `#damage` | 1,742 | 36 |
| `#effect` | 1,092 | 34 |
| `#aoe` | 627 | 23 |
| `#nreff` | 1,297 | 33 |
| `#selectitem` | 631 | 75 |
| `#magicboost` | 416 | 244 |
| `#researchbonus` | 238 | 75 |
| `#masterrit` | 37 | 26 |
| `#newsite` | 504 | 112 |
| `#selectsite` | 684 | 5 |

Counts are syntactic occurrences rather than distinct final objects. DE must be resolved first and Divinitus second.

### Active mod combat scope

**Status: Source-confirmed**

Syntactic command counts in the supplied files show extensive object-level combat edits:

| Command family | DE 2.16 | Divinitus 1.15.3 DE |
| --- | ---: | ---: |
| `#newmonster` | 3,553 | 346 |
| `#selectmonster` | 4,227 | 373 |
| `#newweapon` | 389 | 34 |
| `#selectweapon` | 142 | 0 |
| `#selectspell` | 2,816 | 17 |
| `#att` | 2,038 | 276 |
| `#def` | 2,114 | 278 |
| `#prot` | 1,612 | 238 |
| `#mor` | 1,692 | 229 |
| `#enc` | 1,186 | 163 |
| `#mountmnr` | 178 | 9 |
| `#skilledrider` | 437 | 1 |
| `#trample` | 39 | 12 |

These are occurrences, not distinct final objects. The files do not expose a global replacement for the engine's ordinary DRN, Attack-versus-Defence formula, square capacity, army-rout threshold, or retreat algorithm. Foundation mechanics remain applicable, but every effective unit, weapon, spell, and mount must be resolved through DE and then the later Divinitus overwrite.

### Game settings, hidden maps, and strategic interface

**Status:** Official and current official correction.

- Higher independent strength slows expansion and first contact.
- Increased magic or research settings favour nations able to convert magical access and mage recruitment efficiently.
- Score graphs can strongly affect threat assessment; games with graphs disabled place more weight on scouts, spies, scrying, battle reports, and diplomacy.
- A spy in an enemy capital can reveal that enemy's score-graph data even if graphs are disabled.
- Hidden maps require provinces and routes to be explored.
- Dominions 6 maps may contain multiple planes.
- Claimed Thrones visibly light on the strategic map.
- Map army arrows scale with reported army size.
- Moving-army setup can include magic-phase teleporting forces.
- Many global enchantments are centred on an origin province that must remain protected.

**Primary references:** Dominions 6 Manual, revision 2; Illwinter Dominions 6 changes and new-features page.

### Scouting and provincial information

**Status:** Official.

| Channel | Official information |
| --- | --- |
| Scout | Owner, military estimate, fort construction, history, current and neighbouring temperature |
| Priest | Scout information plus dominion strength and owner |
| Spy | Scout information plus income, supplies, sites, unrest, PD, and improved military accuracy |
| Dominion | Owner, income, temperature, and neighbouring dominion |
| Scrying | Owner, highly accurate military information, income, supplies, sites, PD, history, temperature, dominion, forts, and unrest |
| Ownership | Full provincial information and age-dependent map-name exploration |
| Adjacent ownership | Owner, temperature, and unreliable military information |

Scrying in friendly dominion can detect glamoured units under current Dominions 6 rules.

### Movement and operational access

**Status:** Official.

- Movement uses exit and entry half-steps.
- Ground half-step costs are Plains 3, Forest 5, Waste 5, Highlands 6, Swamp 7, Sea 5, Cave 4, Cave Forest 6, Crystal Cave 6, and Drip Cave 7.
- Enemy non-stealthy forces add 4; enemy stealthy forces add 3; snow adds 1; roads subtract 2 to a minimum of 2.
- Relevant terrain survival subtracts 2. Forest Survival also helps in Cave Forest, Mountain Survival in Crystal Cave, and Swamp Survival in Drip Cave.
- Flying normally costs 3 per half-step, 5 in caves, with +1 for enemy presence.
- General Map Move examples are heavy infantry 8, light infantry 14, light cavalry 20, unicorn 26, slow flier 14, ordinary flier 20, fast flier 26; commanders normally add 2.
- Rivers require Cold +1 on both sides unless an applicable crossing ability exists.
- Mountain passes require Heat +1 on both sides unless flight, floating, or Mountain Survival applies.
- The slowest unit controls army movement, and troops require commanders.
- All relevant troops normally require the special movement ability, except under the specific sailing and granted-water-breathing rules.
- Friendly movement resolves before hostile movement.
- Hostile armies swapping provinces may meet in either province or miss; exact interception selection remains test pending.
- Entering a friendly fort normally places an army inside; Move and Patrol is needed to arrive outside.
- An order arrow can remain even if later state makes movement illegal.

### Patrol, stealth, raid, and pillage

**Status:** Official, with output details test pending.

Stealth detection compares:

```text
Patrol Strength + 2d25 open-ended
versus
Stealth Strength + 2d25 open-ended
```

- Stealth strength begins with commander stealth and is reduced per troop, with a smaller penalty for troops with at least +50 Stealth.
- Patrol strength is the sum of unit patrol values, reduced by half unrest up to the listed cap, and gains from PD at 15 or more.
- Individual patrol strength depends on Precision and Map Move, with flying treated specially, plus Patrol Bonus.
- Commander contribution is doubled; Mindless and Undisciplined contribution is halved.
- A discovered stealth force fights outside defenders; ordinary fort defenders not patrolling remain inside.
- Move and Patrol does not search for stealth units on its arrival turn.
- Pillage kills population, raises unrest, reduces supplies, and produces temporary gold and one-month food.
- The Raid order requires a Pillager commander and Map Move 20 or more.
- Raid moves, fights if necessary, then pillages without returning.
- Only Pillager units contribute and they do so at half strength.

### Assassination

**Status:** Official, with distributions test pending.

- An assassination selects a random enemy commander.
- Each assigned bodyguard has a base 50% chance to appear, modified by Bodyguard and Patience.
- The target is unprepared and ignores its ordinary script.
- Province context can create guards, bystanders, or surprise conditions.
- Ordinary assassins cannot operate into or out of a besieged fort without Scale Walls, flight, teleportation, or equivalent access.
- Similar access applies to related special attacks.
- Mounted targets are often dismounted, and a successful assassin may kill the mount.

### Siege operations

**Status:** Official for the core formula and sequence; community-tested for qualitative wall bands and selected edge cases.

- Siege reduction uses Strength squared; flying doubles contribution.
- Repair uses Strength squared divided by two; flying doubles contribution.
- Mindless, Animal, and Undisciplined penalties apply.
- The difference between reduction and repair damages or restores walls.
- Only Maintain Siege contributes; a commander's other order replaces siege work.
- The defender sees wall condition; the besieger receives qualitative reports.
- An unbesieged damaged fort repairs fully.
- Fort-interior supply declines with siege duration; the manual sequence begins 300, 150, 100, 75, 60 for a 300-supply example.
- Two consecutive starvation turns can cause disease.
- A legal storm order requires walls at zero when orders are issued.
- Relief occurs before the storm and can cancel it.
- If a storming commander dies before the gate battle, its squads do not participate.
- Break Siege retreat can return inside or move to a friendly adjacent province, with a 50/50 choice where both exist.
- Retreat from a storm kills besieged commanders.

The community siege reference assigns approximate remaining-wall ranges to qualitative messages and reports selected stealth and magic-phase edge cases. These remain secondary until reproduced under 6.36.

### Formal diplomacy and NAPs

**Status:** Official for the system; community convention for social terms.

- Dominions 6 supports formal diplomacy and NAPs with humans and AI.
- Game settings can make formal agreements binding or nonbinding.
- Binding enforcement does not define every social expectation involving remotes, stealth staging, harmful globals, dominion, third-party access, accidental bumps, or imminent victory.
- Community counting conventions differ. A treaty should state the first legal order-submission turn and first legal contact turn rather than relying on `NAP3` or another label alone.
- Trades are generally treated as binding in organised community play.

### Thrones, claiming, and Cataclysm

**Status:** Official for the victory structure and claim rules; current object data and final Cataclysm wording partly test pending.

- Throne level equals Ascension Point value from 1 to 3.
- The host sets total points and points required to win.
- A Throne can be claimed by a Pretender, Prophet, or H3+ priest.
- The nation must own the province; a besieger cannot claim through a fort, while the besieged owner can.
- Claiming resolves during hosting step 8.
- Claimed Thrones spread dominion and activate their claimed effects.
- Conquest makes a Throne unclaimed.
- Cataclysm begins after the configured turn and causes horrors to destroy Thrones.
- Each destroyed Throne reduces the points required to win.
- The manual states that if no player owns a Throne when the last is destroyed, the horrors win.
- A current community reference describes the all-Thrones-destroyed outcome as a draw. The exact 6.36 result remains assigned to test S15.

The official step-8 claim and step-57 victory order combines with the current ownership rule and a published same-turn report to settle R-018 at **Official plus Community-tested** tier. Later claimant death does not undo a completed claim. Conquest of an unfortified Throne, or successful storming of its fort, makes it unclaimed before victory and removes its Ascension Points. Merely placing a fortified Throne under siege leaves the defending fort and claim intact. Exact simultaneous winning-total ties remain a separate unresolved branch.

The community throne-rush reference provides a useful operational hypothesis: move and crack at T+0/T+1, storm at T+1/T+2, then claim before the following hosting. Exact branches still depend on walls, battle order, claimant movement, and counter-capture.

### AI difficulty and current capability

**Status:** Official and current official correction.

AI bonuses to gold, resources, Recruitment Points, and magic income:

| Difficulty | Modifier |
| --- | ---: |
| Easy | -30% |
| Normal | 0% |
| Difficult | +30% |
| Mighty | +60% |
| Master | +100% |
| Impossible | +150% |

These bonuses do not increase commander recruitment rate or Holy Points. The AI has omniscient province-ownership information. Dominions 6 AI builds forts, recruits better national troops, plans high-level rituals and globals, uses Dispel, and can participate in formal diplomacy. Patch 6.34 corrected attempts to cast rituals without a lab, research when impossible, and preach with non-priests.

## Claims needing controlled tests

### Armies and battle tests

Foundation Book IV defines sixteen suites covering:

1. tie direction for Attack, MR, and morale;
2. harassment decay;
3. cooldown and Combat Speed;
4. Formation Fighter density;
5. repel sequence and decay;
6. shield damage and repair;
7. mounted targeting;
8. trample and flying fatigue;
9. morale survivor bonus;
10. army HP rout weighting;
11. retreat intelligence;
12. active-unit fatigue recovery;
13. regeneration and rounding;
14. false damage and rout;
15. indoor battlefield magic;
16. DE and Divinitus regression battles.

### Economy and state tests

Priority tests for the 6.36 unmodded live ruleset and frozen combined mod rulesets:

1. Income, resource, Recruitment Point, and fort-draw rounding.
2. Recruitment Point boundaries at 5,000, 10,000, 20,000, and 40,000 population.
3. Commander Point base, multi-point commanders, and exceptional bonuses.
4. Holy Point refresh and queue behaviour under changed maximum dominion.
5. Sacred-slave upkeep stacking, mounts, summons, and `#addupkeep`.
6. Fort supply at distance zero through four and competing fort contributions.
7. Unrest effects on Recruitment Points and Commander Points.
8. Commander starvation, survival checks, mounts, and siege-interior supply.
9. Strength-squared siege rounding and combined Mindless, Animal, Undisciplined, Flying, and siege bonuses.
10. Construction completion effects on same-month tax trace and Administration income.

Growth/Death income and Order/Turmoil resources were removed from the open test list in Progress Edition 19 after R-006 and R-007 were resolved at the current official-documentation tier. A controlled reproduction may still be useful as a regression check, but it is no longer required to choose the published percentages.

Foundation Book II contains the detailed setup and record format for E1-E10.

### Wish test suite

For each ruleset:

1. create or acquire an S9 caster;
2. record game patch, mod files, and load order;
3. back up the turn before casting;
4. enter every candidate string exactly;
5. record message text, treasury changes, unit or item IDs, commander status, afflictions, horror marks, and global effects;
6. repeat random results enough times to measure variation;
7. check aliases separately;
8. inspect mod source for `NO_WISH` or changed unit restrictions.

Priority wishes:

- gems;
- gold and synonyms;
- blood slaves and synonyms;
- artifact/artefact;
- weapon;
- power;
- strength;
- experience;
- dominion;
- population;
- exact unit names;
- commander/hero;
- dangerous and destructive wishes.

### Communion tests

The core rule is official, but tests should illustrate:

- Personal Regeneration cast before and after joining;
- masters with different personal buffs;
- masters leaving or dying;
- slaves with equal, lower, half, and higher path levels;
- fatigue rounding;
- interaction with matrices and automatic communion abilities;
- DE changes to communion items and Grand Communion items.

### Magic-system tests

Foundation Book V defines twenty suites covering:

1. research arithmetic;
2. research hosting timing;
3. combat gem spending;
4. spell-fatigue rounding;
5. penetration;
6. communion thresholds;
7. communion fatigue;
8. communion self-buffs;
9. communion collapse;
10. automatic communion items;
11. ritual order;
12. dome interaction;
13. global contests;
14. forge-cost stacking;
15. booster access;
16. artifact races and yearning;
17. legendary research;
18. Wish;
19. indoor magic;
20. combined-mod regression.

### Strategy and campaign tests

Foundation Book VI defines twenty suites covering:

1. expansion reliability;
2. expansion matchups;
3. movement boundaries;
4. hostile swaps and interception;
5. patrol detection;
6. Raid and pillage;
7. intelligence channels;
8. siege arithmetic;
9. relief and storm order;
10. fort starvation;
11. assassination and bodyguards;
12. formal-NAP edge cases;
13. Throne claim timing;
14. one-turn Throne operations;
15. Cataclysm;
16. AI difficulty economy;
17. raider-response exchange;
18. recovery scenarios;
19. information-deception scenarios;
20. combined-mod campaign regression.

### Formation tests

- units of equal size with and without Formation Fighter;
- every standard formation at several squad sizes;
- obstacle-heavy and open battlefields;
- cavalry, giants, and mixed-size squads;
- `#skirmisher` values;
- commander and squad placement used to imitate wedges, reserves, and screens.

### Grand Hierophant tests

- exact Divinitus source definition captured;
- verify every path, scale, tag, and displayed ability;
- test the monthly Mystic anointment;
- test teaching chance by candle count;
- test the maximum path cap;
- test site-search rewards and whether “elemental gems” means Fire, Air, Water, and Earth only;
- test combined DE load order.

## Book VII: Nation dossiers and MA Arcoscephale

### Nation-dossier standard

**Status:** Research framework completed.

Every nation dossier now separates:

- rules;
- capacity;
- strategic doctrine;
- verification evidence;
- unmodded and modded layers.

Required components include roster jobs, constrained commander turns, mage-random probability, native/boosted/bootstrapped/imported access, response-tree research, deployable army packages, matchup classes, Pretender families, campaign phases, controlled tests, and a source register.

### Unmodded MA Arcoscephale roster

**Status:** Official, revision-2 manual; current structured data used as a cross-check.

- Race: humans.
- Military: heavy spear infantry, chariots, elephants.
- Magic: Astral, Fire, Earth, Water, some Nature.
- Priests: H1 and H2 healers.
- Dominion: accurate automatic military reports inside dominion.
- Order limit +1.
- Standard forts; laboratories cost 300 gold.
- Capital income: 1 Nature gem and 4 Astral pearls.
- Hiereia is recruitable outside forts.
- Astrologer is capital-only.

The full commander, troop, rider, and mount tables are recorded in Foundation Book VII.

### Mystic randoms

**Status:** Official/structured object definition; probabilities derived; live sampling pending.

The Mystic has:

- S1;
- one guaranteed uniform F/W/E/S random;
- independent 50% F;
- independent 50% W;
- independent 50% E;
- Research +1.

Derived:

- F2, W2, and E2 each occur at 12.5%;
- S2 occurs at 25%;
- any named element occurs at level 1+ with probability 62.5%;
- all F/W/E occur at level 1+ with probability 21.875%;
- E2S2 and two level-2 elements cannot occur naturally on the same Mystic.

### Astrologer randoms

**Status:** Official/structured object definition; probabilities derived; live sampling pending.

The Astrologer has:

- S3;
- one guaranteed uniform F/W/E/S random;
- a 10% extra F/W/E/S random;
- Fortune Teller 10;
- capital-only, recruitment cost 4.

Derived under independent-roll interpretation:

- S3: 73.125%;
- S4: 26.25%;
- S5: 0.625%.

### Unmodded national magic

**Status:** Official.

MA Arcoscephale owns:

- Sow Dragon Teeth;
- Forge Brass Bull;
- Summon Hound of Twilight;
- Craft Keledone;
- Bind Keres;
- Procession of the Underworld;
- Awaken Hamadryad;
- Monster Boar.

The normal recruitable roster can directly cast Sow Dragon Teeth through an E2 Mystic. Several other nationals require path bridging because the nation has no recruitable Death, only N1, and cannot roll E2S2 on one Mystic.

### Dominions Enhanced 2.16 MA Arcoscephale

**Status:** Source-confirmed; inherited live cards partly test pending.

DE 2.16:

- clears and rebuilds nation 50 recruitment;
- adds Phalangite 9316, Prodromoi 9317, Hetairoi 9318, Hipparchus 9319, and paired Heart Companions 9322/9323;
- improves and reprices Hoplites and Hypaspists;
- makes Archousa N2 at 265 gold;
- gives Mystics Poor Magic Leadership;
- authorises Astrologers for restricted-item group 10;
- rewrites the Tower of a Thousand Stars and Gymnasium;
- replaces Anthromachus with Aleksandros and adds Muse multiheroes;
- adds constellation magic, nymph and Titan summon ladders, adventurers, Divine Heroes, and national items.

Hetairoi, Hipparchus, and copied spells retain some inherited fields that must be captured from the final live card.

### Grand Hierophant under DE then Divinitus

**Status:** Source-confirmed load-order result; Pretender-screen verification pending.

DE establishes S2, path cost 20, humanoid slots, MR 18, and other base properties. Divinitus later overwrites the design cost to 150, raises bad-event prevention to 75, adds all-known-non-priest-paths +1, and attaches anointing, teaching, and site-search events.

The visible teaching event:

- targets Mystic Prophet 382;
- requires positive dominion;
- uses `#req_domchance 5`;
- adds Fire, Water, Earth, and Astral simultaneously;
- gates on an Astral-path threshold.

The prose says every affected path has maximum 3. Because the source gate is visibly tied to Astral while all four paths are boosted, elemental over-cap behaviour is test pending.

The site-search treasure event:

- uses candles times 5% as described;
- grants 150 gold;
- grants 1d6 Fire, Air, Water, and Earth gems.

Derived conditional value is 14 total elemental gems per success. At \(c\) candles, expected value per eligible search month is \(7.5c\) gold and \(0.7c\) total elemental gems, subject to confirmation of event semantics.

### Book VII controlled tests

Foundation Book VII defines twenty-five suites covering:

1. Mystic randoms;
2. Astrologer rare randoms;
3. starting-army expansion;
4. elephant sizing;
5. chariot versus elephant;
6. Hoplite versus Hypaspist;
7. formation density;
8. independent casting versus communion;
9. communion collapse;
10. shared self-buffs;
11. Magic Duel;
12. Mind Hunt and healing;
13. scrying and glamour;
14. outside-fort Hiereiai;
15. healing allocation;
16. paired Heart Companions;
17. inherited DE unit cards;
18. constellation exclusivity;
19. summon geography;
20. Oceanid randoms;
21. Grand Hierophant inheritance;
22. Mystic anointing;
23. teaching caps;
24. site-search treasure;
25. combined trained-caster timing.

### MA R’lyeh comparison

Build four data snapshots:

1. unmodded;
2. DE only;
3. Divinitus only;
4. DE then Divinitus.

Diff:

- national summary;
- recruitable units and commanders;
- shapes and recruitment-enabler relationships;
- paths and randoms;
- national spells and items;
- sites and freespawn;
- pretenders and bless implications;
- land and underwater recruitment;
- known bugs.

## Publication rules

- Never write “latest” without a date and version.
- Never mix unmodded and modded numbers in one table without separate columns.
- Never turn a single multiplayer anecdote into a universal law.
- Never cite a Dominions 5 page as proof of a Dominions 6 edge case.
- Never conceal uncertainty with vague wording.
- Do not clutter the public prose with the entire research trail; link a compact source note instead.
- Preserve corrections visibly in the private archive so an old error cannot return during later rewrites.

## Book VIII — Modding and Scenario Design

### Official manual baseline

**Status:** Official/current official.

The official Dominions 6 documentation page currently distributes:

- Modding Manual version 6.34;
- Event Modding Manual labelled version 6.29;
- Map Making Manual version 6.26;
- the one-page `d6m` file-format specification.

The public game baseline is 6.36. Later official patch notes are required where they add commands or correct behaviour after a manual revision. The structured object baseline remains explicitly pinned to 6.35 until a new export is audited.

### Mod parser order

**Status:** Official.

Within one mod, categories are parsed in this order:

1. mod information;
2. weapons;
3. armour;
4. units;
5. names;
6. blessings;
7. sites;
8. nations;
9. spells;
10. magic items;
11. general rules;
12. population types;
13. mercenaries;
14. events.

Entire mods are loaded separately. The manual states that objects created in other mods cannot be referenced reliably by name and warns against two mods modifying the same object.

### Current consolidated object limits

**Status:** Official with internal-manual discrepancy noted.

The final 6.34 manual table records:

- weapons 0-3999, mod range 1000+;
- armour 0-1999, mod range 400+;
- monsters 0-19999, mod range 5000+;
- nametypes 100-399, mod range 170+;
- spells 0-7999, mod range 2000+;
- enchantments 0-9999, mod range 200+;
- items 0-1999, mod range 700+;
- sites 0-3999, mod range 1700+;
- nations 0-499, mod range 150+;
- population types 0-249, mod range 125+.

Individual chapters retain narrower older-looking limits, including monsters 5000-8999 and spells 1300-3999. Book VIII treats the consolidated table as current capacity, retains collision warnings, and assigns high-boundary questions to versioned verification.

### Event codes and variables

**Status:** Official.

- Province event codes should use negative values from -300 to -5000; zero is the default/reset.
- Event variables are global integers 0-9999.
- Special variable -1 maps to the receiving nation.
- Special variable -2 maps to 500 plus player number.
- Special variable -3 maps to 1000 plus province number.
- Special variable -4 maps to 3000 plus province number.

These spaces are global across enabled event mods and require explicit registries.

### Event rarity

**Status:** Official.

The documented classes are:

- 0 always;
- 1 common bad;
- 2 uncommon bad;
- 5 always unlimited;
- -1 common good;
- -2 uncommon good;
- 10 always global;
- 11 common global;
- 12 uncommon global;
- 13 always immediate global.

Most global events are planned seven months ahead; rarity 13 is immediate.

### Map requirements and planes

**Status:** Official.

Hand-drawn map images use Targa, at least 256x256, with provinces marked by single pure-white pixels. Required map commands are `#dom2title`, `#imagefile`, and `#mapsize`. Dominions 6 supports one primary plane plus seven additional planes.

Map terrain masks are distinct from modding-manual site masks.

### Current 6.35 site-event correction

**Status:** Current official correction.

Dominions 6.35 fixed `#revealsite` and `#removesite` for cases where several sites share the same name.

### Supplied-source overlap

**Status:** Source-confirmed/derived.

A numeric-selector comparison between the supplied files finds:

- 357 monster identities selected by both DE 2.16 and Divinitus 1.15.3 DE;
- two item identities selected by both;
- extensive event compatibility exposure that cannot be measured through selectors alone.

Overlap is not proof of an error. It proves that the combined order is a separate ruleset requiring final-object reconstruction.

### Grand Hierophant compatibility example

**Status:** Source-confirmed.

DE establishes the Grand Hierophant's Astral, path cost, MR, slots, disease resistance, and initial design properties. Divinitus later changes cost, all-path boost, bad-event prevention, description, and event integration without clearing every DE property. The combined result therefore inherits and overwrites different fields.

### AI modding boundary

**Status:** Official/design doctrine.

The official language exposes:

- nation path and bless hints;
- mage and heavy-unit recruitment preferences;
- unit no-recruit and single-recruit hints;
- Pretender templates;
- ordered research goals;
- favourite rituals and items;
- spell preferences.

It does not document a general rewrite of strategic diplomacy or arbitrary reasoning. Book VIII describes event-driven diplomacy as a bounded reaction layer rather than a new AI mind.

### Book VIII open verification

Book VIII retains tests for:

1. automatic allocation at current high ceilings;
2. cross-mod name references by category;
3. hidden copied attributes absent from detail cards;
4. event-variable edge cases;
5. execution order among events changing the same state;
6. large event-library performance;
7. multi-plane AI pathing;
8. AI template distributions;
9. automatic object insertion and save compatibility;
10. transformation preservation;
11. target selection among equal candidates;
12. network filename and dependency edge cases.

## Book IX - DE and Divinitus Technical Encyclopaedia

### Deterministic source index

**Status:** Source-confirmed and mechanically reproduced.

The exact supplied files contain 17,348 active new/select object blocks:

- 14,842 in DE 2.16;
- 2,506 in Divinitus 1.15.3 DE.

The index preserves the active command stream, object action, type, selector, name where stated, nearest source heading, and physical line range. Its SHA-256 values reproduce the frozen snapshot.

The index is not a final-card resolver. It does not import vanilla inheritance, execute copy and clear semantics, allocate numberless objects, or simulate the game engine.

### DE global commands

**Status:** Source-confirmed; command meanings official.

DE applies:

| Command | Value |
| --- | ---: |
| `#gemlongevity` | 2 |
| `#slothincome` | 4 |
| `#turmoilincome` | 4 |
| `#deathincome` | 2 |
| `#deathdeath` | 25 |
| `#luckevents` | 7 |

The official Modding Manual defines gem-longevity level 2 as gems lasting the entire month. It gives defaults of 3, 3, 2, 20, and 5 for the five scale commands respectively.

### Complete DE blessing inventory

**Status:** Source-confirmed.

DE contains 46 active blessing blocks covering 38 distinct blessings. Eight are selected twice to separate path or scale changes from cost changes. The complete table is preserved in Book IX. Earlier partial blessing lists are superseded by it.

### Divinitus event architecture

**Status:** Source-confirmed; rarity and probability semantics official.

Divinitus contains:

- 1,514 new events;
- 1,492 rarity-5 events;
- 12 rarity-13 events;
- 9 rarity-0 events;
- 557 `#req_domchance` commands;
- 602 minimum-dominion requirements;
- 311 temple requirements;
- 179 pregame-only events;
- 370 own-capital requirements.

The Event Manual defines rarity 5 as an unlimited always-event class and `#req_domchance X` as absolute dominion strength multiplied by X percent after other gates are met.

### Corrected monster compatibility surface

**Status:** Source-confirmed/derived.

The earlier selected-selector comparison was incomplete. The full cross-action screen finds:

| Relationship | Shared numeric IDs |
| --- | ---: |
| DE new / Divinitus new | 235 |
| DE new / Divinitus selected | 10 |
| DE selected / Divinitus new | 114 |
| DE selected / Divinitus selected | 357 |

Divinitus touches 650 distinct fixed monster identities; 600 also appear in a DE new or selected monster action. Some groups overlap because DE can create and later select the same identity.

### Event-code and variable registry

**Status:** Source-confirmed/derived.

DE uses nonzero event codes -540, -312 to -308, and -302 to -300. Divinitus uses -3333 and -513. Both use zero as the official default/reset. No nonzero collision was found.

DE uses event variables 6001-6007 and 6011. Divinitus uses 325, 326, and 328-331. No variable collision was found.

### Monster 8616

**Status:** Source-confirmed high-risk collision; pinned-Inspector result recorded; engine result pending.

DE creates 8616 as a hidden land bulk-crafting inventory depositer. Divinitus later creates 8616 as an E2G2H2 Crystal Priest and makes it recruitable from The Crystal Cavern.

The same Divinitus assignment is visible in the public 1.15.2 DE source, so it predates the supplied 1.15.3 file. The official manual warns that two mods should not modify the same object because the result can be unpredictable. The independent integrity report records the pinned Inspector retaining DE's `inventory.` object at 8616, but does not promote that parser result to an engine-confirmed card. A separate repaired edition removes Divinitus's numeric claim while leaving both uploads unchanged.

### Automatic Divinitus objects

**Status:** Source-confirmed definitions; complete pinned-Inspector resolution recorded; engine confirmation pending.

Divinitus contains 69 automatically allocated new monsters and 26 automatically allocated new spells under the current official syntax. The independent integrity report records all resolved IDs for the exact Inspector build and frozen order. Those numbers remain versioned secondary keys because their engine allocation and stability are not independently confirmed.

### Divinitus weapon 3034

**Status:** Source-confirmed.

Weapon 3034 is defined twice. The later block copies Stellar Bolt and later items and units reference 3034 as Stellar Bolt. The earlier Gaze of Death block does not survive as a separate fixed identity.

### Load-order wording

**Status:** Intended order author-confirmed; older embedded contradiction preserved historically.

The public Divinitus 1.15.2 DE file says "Load first." The later project description and version 1.15.0 changelog say to enable the DE edition after Dominions Enhanced, while the supplied 1.15.3 header is silent. The intended frozen order is therefore DE first and Divinitus second. The older header remains recorded because archived files can still reproduce the contradiction.

### Book IX open verification

1. Final in-game monster 8616 and affected DE bulk-crafting behaviour.
2. General occupied-ID behaviour when a later mod repeats `#newmonster`.
3. Final IDs for automatic Divinitus monsters and spells.
4. Mystic Prophet elemental-path cap.
5. Event ordering in the hurricane, winter, earthquake, and quest state machines.
6. Any runtime effect of the five adjacent event starts lacking `#end`.
7. Exact author-intended 1.15.3 DE load-order wording.

## Editorial consolidation record

**Status:** Completed for Progress Edition 11.

Foundation Books I-IX and the field reference were compared at paragraph and subject level. Five exact cross-book paragraph groups existed before editing; semantic repetition was concentrated in baseline blocks, evidence keys, reading routes, mod tables, battle-magic arithmetic, siege formulas, compatibility examples, essays, and completion summaries.

After consolidation, one exact cross-book paragraph remains: the modified-income formula deliberately repeated in Book II and the Turn and Economy Quick Reference. Subject ownership, deliberate recaps, removed material, and human-editing changes are recorded in `15-editorial-consolidation-audit.md`.

## Retrieval and publication record

**Status: Generated and internally validated, 1 August 2026**

Progress Edition 12 adds a retrieval layer without changing the authority of the underlying chapters. The generated catalogue contains 11 reader documents and 1,846 stable heading destinations. The Reader's Guide contributes six reading paths, 192 alphabetical subject entries, 92 glossary records, and 45 prioritised research questions. A redirect table retains 151 semantic aliases.

The website schema treats factual claims separately from strategic doctrine. It supports exact ruleset scopes, mod versions and load order, evidence labels, sources, formulas, examples, cross-references, verification dates, and supersession. The heading index deliberately leaves claim-level ruleset and evidence arrays empty until prose is parsed and reviewed at that finer level. This prevents automatic topic extraction from being mistaken for verification.

Validation requirements are:

- every internal link and semantic alias resolves;
- every generated JSON file parses;
- the JSON Schema passes Draft 2020-12 structural validation;
- the article template validates against that schema;
- PDF outlines use stable heading IDs;
- linked destinations produce PDF link annotations;
- the latest edition is visually inspected at the cover, guide, concordance, glossary, research register, several book openings, and final page.

The active research queue accepts official documentation, official patch records, exact mod source, current structured data tied to a version, and published reproducible evidence. It does not ask the player to perform controlled tests. Questions with no reliable non-player route are retained as blocked publication limits.

Final Edition 12 validation recorded 541 pages, 1,846 outline entries, 3,011 link annotations, no empty pages, no unresolved authored links, and no exact or high-similarity cross-document prose duplication. All eight website JSON files parse, and the article template validates against the Draft 2020-12 schema. The detailed result is preserved in `17-retrieval-publication-audit.md`.

The master plan, prior-conversation archive, evidence ledger, and active-mod snapshot remain persistent internal records but are excluded from the reader-facing PDF.

## First verification priorities

1. Exact installed DE and Divinitus files - completed.
2. Deterministic command, object, event, and overlap index - completed.
3. Freeze current unmodded game data and official manuals.
4. Resolve monster 8616 from an exact-version inspector or reliable reproduction.
5. Build the website's layered object schema from the new source index.
6. Resume nation dossiers only when requested.
7. Run the Wish and communion demonstrations when reliable exact-version evidence is available.

## Progress Edition 28 perception and ability evidence

**Status:** R-048 completed; R-047, R-049, and R-058 in progress.  
**Verified:** 30 August 2026.  
**Ruleset:** unmodded Dominions 6.36.

The live Modding Manual identifies itself as version 6.36 and has SHA-256 `9d4a7d2c5101679de7080455ceebed41b25a1e9beba275985e293183269399cf`. The revision-2 main manual used in the same pass has SHA-256 `65f430fd97c9f27285d63b797b43bc7fe3844241fdf40230b1d25a901ab9f33f`. Current spell and item descriptions are pinned to Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`; the 6.36 official announcement was checked and contains no perception-family correction.

### Established perception division

- Glamour is strategic concealment plus Mirror Image, not Invisibility.
- Invisibility is a strategic patrol-detection rule and a live −10 melee Attack penalty without Spirit Sight. The main manual's −9 value is retained as superseded wording.
- Unseen uses Invisible behaviour and ends when hit.
- Blur and Displacement are melee Attack-penalty states. True Sight, Spirit Sight, and blindness ignore both. Displacement does not stack with Blur or Invisibility.
- Mirror Image is an image-selection defence, and its current spell description says True Sight does not negate it.
- Illusion and Spiritform are technical creature classes. Neither supplies generic strategic concealment or the Invisibility Attack penalty.
- Darkvision affects darkness. It is not a general anti-concealment ability and does not help a blind unit.

R-058 isolates the remaining runtime edges: Spirit Sight or blindness against innate Glamour's images, and information channels against Glamour concealment in friendly provinces. The official strategic branch now has two narrow answers. Arcoscephale's special dominion scrying reveals enemy Glamour units under its dominion, while The Eyes of God detects non-stealthing glamoured or invisible troops inside the caster's dominion. Generic scrying, Spy reports, and the stated boundaries of those permissions remain test-pending.

### Established stacking cases

The effect, not the source category, owns the stacking rule. Standard and Inspiring Researcher are highest-only. Experience and Horror Mark accumulate in their documented ways. Displacement explicitly excludes stacking with Blur and Invisibility. Unlike defensive layers remain separate resolution gates unless a specific rule merges or replaces them.

No general form-item-bless-spell priority has been inferred. All unlisted interactions remain ability-specific.

### Hall-of-Fame boundary

The official sources do not publish score weights, tie ordering, heroic-family selection weights, or growth formulas. The Edition 28 observation template records exact version, seed, commander identity, before-and-after Hall state, battles, kills, survival, heroic family, displayed values, and evidence locators. Formula publication remains blocked until a controlled 6.36 series or engine-backed trace can reproduce the result.
