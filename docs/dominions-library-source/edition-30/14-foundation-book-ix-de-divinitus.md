# Foundation Book IX - Dominions Enhanced and Divinitus

## The Technical Encyclopaedia of the Frozen Combined Ruleset

Dominions 6.35  
Dominions Enhanced 2.16  
Divinitus 1.15.3 DE edition  
Frozen load order: Dominions Enhanced first, Divinitus second  
Research edition: 31 July 2026

This is a frozen source-defined ruleset built against the recorded 6.35 baseline. The live unmodded game is now 6.36; combined runtime compatibility remains unverified and is not implied by the source analysis.

## 1. Purpose

Dominions Enhanced and Divinitus reach into almost every major system in Dominions 6: Pretender design, scales, battle gems, blessings, recruitment, research, underwater play, items, spells, sites, events, and dominion. Together they behave less like a pair of optional add-ons and more like a distinct edition of the game.

Book IX turns 238,821 lines of source into something that can be consulted during play and reused in later nation dossiers. It does this by following a few strict boundaries:

- the two mods are described separately before their combined result;
- every rule is tied to the exact supplied release;
- explicit definitions are distinguished from inherited vanilla fields;
- the loader and load order are treated as part of the ruleset;
- support spells, sites, items, and event variables are separated from ordinary player-facing content;
- source collisions and unresolved runtime questions remain visible;
- strategic consequences are stated as doctrine rather than disguised as facts;
- machine-readable indices support later website search and exact object pages.

The summaries and checklists provide the practical route. Command inventories, ID registries, event structure, collision analysis, and provenance records are there for deeper investigation.

## 2. Frozen Baseline and Evidence

### 2.1 Exact files

| Layer | Exact file | Declared version |
| --- | --- | ---: |
| First mod | `DomEnhanced2_16.dm` | 2.16 |
| Second mod | `Divinitus_1.15.3_DE.dm` | 1.15.3 |

The file fingerprints are:

- Dominions Enhanced: `72558697f8dae3a1fccf8fb57b3faccde56c7fe6c05dac6403cefe153faf6c1b`
- Divinitus DE: `cf7f21900a3812b66edddd831df779743eaf33080aef983f9bdea8ec47642809`

These hashes define the ruleset more precisely than a Workshop title. A guide written for another DE or Divinitus release is historical evidence, not automatic evidence for this game.

### 2.2 Authority order

Claims in Book IX use the following practical hierarchy:

1. the exact supplied source files for what the mods command;
2. Illwinter's official manuals for what those commands mean;
3. the active load order for which later command has the final opportunity to change a field;
4. the mod authors' repositories and release descriptions for stated design intention;
5. current reproducible public tests where engine behaviour is not completely documented;
6. strategic derivation from confirmed inputs.

Source code proves that a command is present. It does not always prove the final in-game card. A selected object inherits every vanilla or earlier-mod field that is not cleared or replaced. A repeated `#newmonster` on an occupied ID is especially important: the official manual warns that two mods should not modify the same object because the result can be unpredictable. The correct label for such a case is source collision until a reliable resolved card or live reproduction exists.

### 2.3 Public author sources

The principal public project pages are:

- Dominions Enhanced repository: https://github.com/BlueFeuer/DominionsEnhanced6
- Divinitus repository: https://github.com/RonhulMaggot/Divinitus
- Illwinter documentation index: https://illwinter.com/dom6/docs.html

The current DE repository describes the project as a DLC-sized overhaul with thousands of spells, items, and monsters; new nations; changes to almost every vanilla nation; cheaper and expanded Pretender design; broad cavalry and underwater revisions; and a large national-magic programme. The supplied file confirms that scope at command level.

Public load-order wording has not been perfectly consistent. The public Divinitus 1.15.2 DE file contains the words "Load first," while the project description and version 1.15.0 changelog instruct players to enable the DE edition after Dominions Enhanced. The supplied 1.15.3 DE header no longer states either instruction. The later project-level wording settles the intended order for this ruleset: DE first, Divinitus second. The older contradictory header remains in the historical record because it can still mislead anyone using an archived file without the release context.

## 3. Finding What Is Needed

### 3.1 First game with both mods

For a first game, read Sections 4, 7, 8, 14-16, and 22, then use the pregame checklist in Section 26. That covers the rules that change ordinary decisions without requiring a full reading of the source structure.

### 3.2 Pretender design

Read Sections 8, 11, 14–18, 21–22, and Essay II. A chassis may now act as an economic institution, temple network, seasonal engine, recruitment programme, or global-risk mechanism. The visible card is only the beginning.

### 3.3 Mod compatibility or debugging

Read Sections 5, 6, 19-21, 24, and 25. Consult the machine-readable summary and object catalogue before drawing a conclusion from a name search.

### 3.4 Website construction

Read Sections 23-25 and Appendix B. The website should preserve separate vanilla, DE, Divinitus, and combined layers. It should never flatten them into one unversioned card.

## 4. What the Combined Modpack Changes

### 4.1 Dominions Enhanced is the broad ruleset

DE is the foundation layer. It changes global economic constants, blessings, units, mounts, weapons, armour, Pretenders, sites, nations, spells, items, poptypes, name lists, and events. It also supplies extensive national content and several new nations.

Its strategic effect goes beyond adding more content. It changes the density of useful options:

- more national research branches compete for early research;
- more summons convert gems into nation-specific force;
- low-path mages gain more battlefield and ritual jobs;
- underwater entry and underwater warfare become less isolated;
- cavalry and mounts become more credible;
- new and revised Pretenders enlarge design space;
- hidden future sites reveal national summons and heroes;
- informative site-search events reduce uncertainty;
- scale choices carry altered economic and event consequences.

### 4.2 Divinitus is the divine-system layer

Divinitus concentrates on Pretender identity. It modifies or rebuilds hundreds of chassis and supplies the machinery needed to make their descriptions operational:

- pregame starting armies and capital sites;
- automatic items;
- temple-generated units, commanders, gems, gold, and sites;
- dominion-scaled effects;
- seasonal and terrain-dependent effects;
- order-dependent abilities;
- national priesthood changes;
- battlefield spells and summoned escorts;
- global event chains;
- ownership-state variables;
- punishments when an immobile god leaves its appointed place;
- relationships with global enchantments, heroes, or unique units.

Divinitus changes what “the Pretender” means. A god may become a distributed part of the state whose effects continue across dozens of provinces. The physical chassis may be only the control key for that larger presence.

### 4.3 Combined result

Under the frozen order, DE establishes the world and Divinitus has the later word on the fields it changes. This produces three classes of final object:

1. **DE-only object:** created or selected by DE and untouched by Divinitus.
2. **Divinitus-only object:** introduced or changed only by Divinitus.
3. **Combined object:** inherited from vanilla, changed by DE, then changed or rebuilt by Divinitus.

The Grand Hierophant is the clearest example of the third class. DE supplies its revised foundation. Divinitus later changes cost, magic, event protection, description, and monthly event systems. Neither source alone describes the combined god.

## 5. How the Dominions Loader Must Be Read

Book VIII owns the general loader explanation: whole mods load separately, command categories have an internal parser order, selected objects inherit unstated fields, numeric identities matter across files, and descriptions are not executable specifications. Four consequences matter here:

1. DE is the first object layer and Divinitus the second.
2. A Divinitus block may inherit vanilla and DE fields that it never restates.
3. Source adjacency does not override parser-category order.
4. A divine description may summarize an event family without listing every gate, delay, or cleanup step.

A complete divine system is traced as:

`chassis -> support item/site/spell -> event requirement -> event effect -> delay or variable -> cleanup event`

### 5.1 Allocation profile

Fixed IDs improve stability inside a coordinated project but create collision risk between projects. Automatic IDs depend on the engine's occupied range and cannot be resolved from these two text files alone.

The supplied DE file uses fixed IDs for every new weapon, armour, monster, and site. Divinitus uses a mixture:

- all 34 new-weapon blocks use a fixed number, though ID 3034 appears twice;
- both new armour blocks use fixed IDs;
- 277 of 346 new-monster blocks use fixed IDs and 69 use automatic allocation;
- all 112 new sites use fixed IDs;
- 4 of 26 new spells use fixed IDs and 22 use automatic allocation;
- its one new item uses fixed ID 1072.

This mix is a source fact, not a defect by itself. It simply marks which identities can be checked statically and which require a resolved game state.

## 6. Exact Source Inventory

### 6.1 File scale

| File | Lines | Bytes | Active commands |
| --- | ---: | ---: | ---: |
| DE 2.16 | 194,385 | 5,675,140 | 173,499 |
| Divinitus 1.15.3 DE | 44,436 | 1,348,538 | 38,834 |

### 6.2 Object-block inventory

| Object action | DE blocks | Divinitus blocks |
| --- | ---: | ---: |
| New weapon | 389 | 34 |
| Selected weapon | 142 | 0 |
| New armour | 81 | 2 |
| Selected armour | 39 | 0 |
| New monster | 3,553 | 346 |
| Selected monster | 4,227 | 373 |
| New site | 504 | 112 |
| Selected site | 684 | 5 |
| New spell | 0 | 26 |
| Selected spell | 2,816 | 17 |
| New item | 0 | 1 |
| Selected item | 631 | 75 |
| Selected nation | 132 | 0 |
| Selected blessing | 46 | 0 |
| New event | 1,564 | 1,514 |

These are active block occurrences, not unique final identities. DE selects 3,185 distinct monster identities, 2,737 distinct spell identities, 629 distinct item identities, 572 distinct site identities, and 128 distinct nations. Repeated blocks are common and often intentional.

### 6.3 Fixed ranges

| Object | DE fixed range | Divinitus fixed range |
| --- | --- | --- |
| Weapon | 1501-1925 | 3001-3035 |
| Armour | 501-581 | 998-999 |
| Monster | 6510-13571 | 5018-10001 |
| Site | 2101-2917 | 1885-2005 |
| Spell | selected IDs 1-4365 | fixed new IDs 183, 197-199 |
| Item | selected IDs 1-899 | new ID 1072 |

Ranges are bounds, not proof that every number inside is used.

### 6.4 Important implementation facts

- DE contains no active `#newspell` block. It builds its spell layer through 2,816 `#selectspell` blocks, including high numbered slots.
- DE contains no active `#newitem` block. It builds its item layer through selected slots.
- DE explicit monster IDs exceed the 5000-8999 recommendation printed in the 6.34 Modding Manual, reaching 13,571. The source proves that the active game accepts or at least parses a wider contemporary space than that older recommendation describes.
- Divinitus uses 1,492 rarity-5 events, 12 rarity-13 events, and 9 rarity-0 events. One event lacks an explicit rarity.
- DE and Divinitus each contain a small number of adjacent event blocks without an intervening `#end`. The next `#newevent` implicitly begins a new block in source analysis, but this remains a lint finding.
- Divinitus defines weapon ID 3034 twice. The later definition copies Stellar Bolt and is the effective intended source for the Stellar Staff references. The earlier Gaze of Death definition does not survive as an independent fixed identity.

## 7. The Six Global DE Rules

DE issues six active general commands outside object blocks.

| Command | DE value | Official meaning |
| --- | ---: | --- |
| `#gemlongevity` | 2 | battle gems last for the entire month |
| `#slothincome` | 4 | each Productivity/Sloth step changes income by 4% |
| `#turmoilincome` | 4 | each Order/Turmoil step changes income by 4% |
| `#deathincome` | 2 | each Growth/Death step changes income by 2% |
| `#deathdeath` | 25 | Growth/Death population effect uses 0.25% units |
| `#luckevents` | 7 | Luck/Misfortune changes event frequency by 7% per step |

The official defaults printed in the Modding Manual are 3 for Sloth income, 3 for Turmoil income, 2 for Death income, 20 for the population constant, and 5 for Luck event frequency. `#deathincome 2` pins the existing default; it does not change it.

### 7.1 Gem longevity

This is the most operationally important global change. Under level 2, combat gems last for the entire month rather than only their ordinary single use. The practical value of a gem-bearing mage now depends on the number of battles the mage can survive and enter during that month.

Consequences include:

- a single gem allocation can support several engagements;
- counter-raiding and sequential defence become more gem-efficient;
- teleporters and other multi-battle pieces gain endurance;
- killing or routing the mage before later battles becomes more important;
- battle-gem accounting must be conducted by mage-month, not only by battle;
- scripts that assume a gem was consumed in an earlier battle require revision.

This rule does not eliminate the need for reserve policy. A mage without the necessary gems at the beginning of the month still lacks them, and a dead, routed, or isolated mage cannot exploit persistence.

### 7.2 Order and Productivity

Order and Productivity each move income by 4% per step instead of 3%. Their combined influence on income is stronger before national modifiers and rounding. The scales keep their other effects, so the change does not reduce them to simple gold choices.

At symmetric extremes, the direct trace differs substantially:

- Order 3 contributes a nominal +12% instead of +9%;
- Turmoil 3 contributes a nominal -12% instead of -9%;
- Productivity 3 contributes a nominal +12% instead of +9%;
- Sloth 3 contributes a nominal -12% instead of -9%.

These percentages are inputs to the engine's provincial economy, not guarantees of an exact treasury difference in every province. Population, terrain, unrest, national rules, taxation, rounding, and special income modifiers remain relevant.

### 7.3 Growth and Death

The gold-income constant remains 2%, while the population-change constant rises from 20 to 25 hundredths of a percent. Death destroys the tax base more quickly and Growth compounds it more quickly, subject to the engine's sign and rounding implementation.

The strategic lesson is temporal:

> Growth and Death do more than alter current income. They change the future base to which many other modifiers apply.

### 7.4 Luck and Misfortune

The event-frequency influence rises from 5% to 7% per scale step. This does not guarantee a particular event result. It changes the number of opportunities, while event quality, rarity, national event sets, and special event mechanics determine what those opportunities become.

Luck becomes more valuable to nations and Pretenders that add strong good-event pools. Misfortune becomes more dangerous where a modded nation or divine system adds harmful events or already has fragile infrastructure.

## 8. Complete DE Blessing Revision

DE modifies 38 distinct blessings through 46 blocks. Eight blessings are selected twice because one block changes path or scale requirements and another changes cost.

Path letters are F Fire, A Air, W Water, E Earth, S Astral, D Death, N Nature, G Glamour, and B Blood.

| Blessing | DE cost | Additional change |
| --- | ---: | --- |
| Wasteland Survival | 1 | reduced from 2 |
| Death Explosion | F4+D2 | crosspath; non-Incarnate structure |
| Fire Shield | F5 | reduced from 6 |
| Flaming Weapons | F4 | Heat 1 required; non-Incarnate |
| Farshot | 1 | reduced from 2 |
| Awareness | 2 | reduced from 3 |
| Swiftness | 3 | reduced from 4 |
| Storm Flight | 3 | reduced from 4 |
| Wind Walker | A4+S2 | crosspath; non-Incarnate |
| Weightlessness | 4 | reduced from 6; primary requirement becomes 3 |
| Air Shield | 5 | reduced from 6 |
| Charged Bodies | 7 | reduced from 8 |
| Flight | 6 | reduced from 9 |
| Swamp Survival | 1 | reduced from 2 |
| Swimming | 1 | reduced from 2 |
| Slowing Weapons | W4+G2 | crosspath; non-Incarnate |
| Vitriol Weapons | 6 | reduced from 8; primary requirement becomes 4 |
| Water Breathing | 2 | non-Incarnate |
| Frost Mist Weapons | W4+A1 | crosspath; non-Incarnate |
| Unbreakable | 3 | reduced from 4 |
| Resilience of the Earth | 5 | reduced from 6 |
| Solar Weapons | 3 | reduced from 4; primary requirement becomes 2 |
| Twist Fate | 5 | reduced from 6 |
| Fateweaving | 6 | reduced from 7 |
| Withering Weapons | 3 | reduced from 4 |
| Reanimators | D4+E2 | crosspath; non-Incarnate |
| Death Weapons | 5 | reduced from 8 |
| Fear | 8 | reduced from 9 |
| Forest Survival | 1 | reduced from 2 |
| Poison Weapons | 3 | reduced from 4 |
| Recuperation | 4 | non-Incarnate |
| Berserker | N4+B1 | crosspath; non-Incarnate |
| Barkskin | N4+N2 | Growth 1 required; non-Incarnate structure |
| Obfuscate | 5 | reduced from 6 |
| Awe | 7 | reduced from 8; primary requirement becomes 5 |
| Displacement | 6 | reduced from 7 |
| Dread | 7 | reduced from 8 |
| Vampiric Weapons | 6+3 | two-path total 9, reduced from 12 |

### 8.1 How to read the cost fields

The modding commands store primary and optional secondary path requirements. The minimum path skill and blessing-point cost use the same numbers. Thus `#cost0 4` and `#cost1 2` produce a six-point crosspath blessing requiring the stated levels in both paths.

Some source comments describe a blessing as "no longer Incarnate" without a separate `#incarnate` command. The new path-cost structure places the requirements below the threshold that made the older single-path version Incarnate. The effect follows the rewritten requirements rather than a standalone toggle.

### 8.2 Strategic families

The revisions create five broad families.

**Cheap mobility and survival.** Terrain survival, Swimming, Water Breathing, Farshot, Awareness, Swiftness, and Weightlessness become easier to add to a broader design.

**Accessible weapon blessings.** Flaming, Slowing, Frost Mist, Solar, Withering, Death, Poison, and Vitriol effects become cheaper or crosspath. A design can purchase a functional weapon effect without committing its entire budget to one extreme path.

**Lower Incarnate dependence.** Several effects remain available while the Pretender is dormant, imprisoned, dead, or otherwise absent. This increases the viability of delayed chassis and reduces the all-or-nothing cost of divine death.

**Crosspath identity.** Death Explosion, Wind Walker, Slowing Weapons, Frost Mist Weapons, Reanimators, Berserker, Barkskin, and Vampiric Weapons require a more specific magical identity. Their nominal cost is only part of the design cost; path entry and opportunity cost matter.

**Scale contracts.** Flaming Weapons requires Heat 1 and Barkskin requires Growth 1. The blessing is tied to national scales and cannot be purchased in isolation.

### 8.3 Bless evaluation method

A blessing should be valued against five quantities:

1. the number of sacred bodies affected;
2. the number and importance of sacred attacks;
3. the turns on which sacred recruitment is constrained;
4. the probability that the effect changes an actual matchup;
5. the design points and paths displaced.

A cheap blessing is not automatically efficient. A one-point terrain blessing may be decisive for a mobility plan and worthless in another. A nine-point Vampiric Weapons package may be extraordinary on durable multi-attacking sacreds and extravagant on fragile, recruitment-limited elites.

## 9. Dominions Enhanced as an Object Ecosystem

### 9.1 Weapons, armour, mounts, and units

DE adds 389 fixed-ID weapons and modifies 142 existing weapons. It adds 81 armours and modifies 39 armour blocks. It creates 3,553 monster blocks and selects 4,227 more.

This density supports connected programmes, not isolated novelties:

- bows gain damage and precision and use 24 ammunition in the stated DE design;
- slings use full strength, gain damage at ordinary human strength, and use 30 ammunition;
- javelins receive underwater rules;
- horse Magic Resistance rises on average;
- weak barding improves and formerly unbarded horses gain barding;
- Skilled Rider increases across riders;
- forgeable barding becomes cheaper and broader;
- many units gain DE-specific shapes, mounts, equipment, or supporting spells.

A unit must be read through its relationships. A rider card belongs with its mount. A weapon belongs with its secondary effects and ammunition. A unit belongs with its national recruitment site, spell support, and cost commands.

### 9.2 Sites

DE creates 504 sites and selects 684 site blocks. Sites perform several different jobs:

- national capital and terrain recruitment;
- future-site documentation;
- summon and hero previews;
- hidden national mechanics;
- event and ritual anchors;
- gem, gold, resource, and supply production;
- fort and defence units;
- divine or scripted transformation infrastructure.

A source count of "504 new sites" does not mean 504 ordinary searchable magic sites. Many are rarity 5, level 0, national, hidden, or event-managed support objects.

### 9.3 Spells

DE's 2,816 selected spell blocks cover IDs from 1 to 4,365. They include:

- ordinary researchable spells;
- national rituals and summons;
- hidden effect spells;
- item-granted spells;
- transformation chains;
- battlefield wrappers;
- temporary buffs and helper effects;
- prayer families;
- underwater access and water-breathing systems;
- fort damage and siege support;
- national late-game capstones.

The source uses high selected slots instead of active `#newspell` commands. A catalogue must classify each spell by its final school, research level, path, restriction, and visibility. Whether the source keyword says "new" does not settle the question.

### 9.4 Items

DE selects 631 item blocks covering 629 distinct identities. The programme includes repricing, path changes, national rebates, underwater tools, barding, temporary gem effects, auto-spells, restricted items, and new high-slot definitions.

Item value changes twice:

1. the forge cost and path gate may change;
2. the environment contains more reasons to want the item.

Cheaper water-breathing equipment matters more because underwater entry is a central DE project. Cheaper barding matters more because mounts are stronger. Siege items matter more where magical fort pressure is deliberately expanded.

### 9.5 Nations

DE selects 128 distinct nations in 132 blocks. Its changes go well beyond recruit costs. Nation blocks can:

- clear and rebuild recruitment;
- change terrain recruitment;
- change capital and starting armies;
- add or remove Pretenders;
- replace heroes and multiheroes;
- set scale preferences or forced modifiers;
- change fort, temple, or dominion rules;
- add future sites;
- add AI hints;
- replace an entire nation in a reserved slot.

The current DE project summary identifies major or mild changes across all ages and several new nations. The supplied source includes complete custom nation definitions in slots 181-207 alongside extensive changes to vanilla nation IDs.

## 10. The DE Design Programme

### 10.1 Pretenders

The principal DE Pretender source region spans approximately lines 72,487-90,112 and contains 591 monster blocks:

- 266 new-monster blocks;
- 325 selected-monster blocks;
- 268 blocks with a `#startdom` command;
- 561 blocks with a `#pathcost` command.

The wider file also defines shapes, summons, divine servants, and later corrections. The region is a useful authorial boundary, not a complete resolved Pretender database.

The public project description states the main design direction:

- Pretenders are repriced from the ground up and are generally cheaper;
- Titans receive two more paths;
- monsters and rainbows receive one more path;
- monsters are broadly stronger;
- more scale modifiers appear;
- the roster of Pretenders is larger, especially underwater and in Polynesian realms;
- Pretenders can heal in the capital or while preaching outside it under the stated holy-level chance.

These changes mean that vanilla design heuristics cannot simply be carried across. Path-entry costs, chassis costs, built-in scales, and jobs must be read from DE data.

### 10.2 Magic

DE expands summons and national magic, shifts some effects into Glamour or crosspaths, enlarges many battlefield areas, improves the jobs available to level-one mages, and adds siege tools. The hostile battlefield-wide spell policy limits effects such as Wind of Death to one cast per round per side.

The strategic result is portfolio pressure. More viable spells make a fixed queue less reliable, not more. A nation should maintain:

- an expansion and first-war branch;
- an anti-armour branch;
- an anti-mass branch;
- a defensive and counter-raid branch;
- a path-access and forging branch;
- a national-summon branch;
- a water-access branch where geography requires it;
- a late-game transition.

### 10.3 Underwater play

DE treats the sea as a connected theatre:

- Gift of Water Breathing becomes cheaper and earlier;
- more items and spells grant water access;
- more monsters carry water-breathing support;
- underwater population rises;
- coastal and underwater independent mages improve;
- more spells work underwater;
- underwater-only spells expand;
- javelins function underwater under modified range and damage;
- many aquatic nations receive specific overhauls.

This reduces the old binary distinction between land and sea. It does not make amphibious war free. Command capacity, breathing capacity, hostile currents, poor amphibians, laboratory networks, fort access, and return routes remain logistical constraints.

### 10.4 Information

DE's informative site-search events report when a searching mage detects traces of a stronger hidden site in a path but lacks the level to reveal it. All nations also receive future sites in their overview to display summons and heroes.

These systems reduce memory and inspection burden, but they do not remove it. The player still needs to distinguish:

- a site that has been found;
- a clue that a stronger site remains;
- a future-site documentation entry;
- an event-managed support site;
- a national site that is present only under a specific ruleset.

## 11. Dominions Enhanced Pretender Analysis

### 11.1 Design cards must be rebuilt

The ordinary design screen remains useful, but a serious DE design record needs more fields:

| Field | Question |
| --- | --- |
| Chassis price | What does the exact DE card cost? |
| Path entry | Which paths are built in, and what is each new level's marginal price? |
| Dominion | What is the starting dominion and cost of increasing it? |
| Scales | Which forced or bonus scales change the national plan? |
| Mobility | Can the god expand, raid, teleport, sail, or cross water? |
| Survival | Which threats defeat the chassis before research support? |
| Divine job | Is its main purpose expansion, blessing, access, research, ritual, combat, or scales? |
| National availability | Which nations or realms can choose it after DE's `#addgod` and `#delgod` changes? |
| Divinitus layer | Does the second mod add an economy, event, priesthood, site, or battle system? |

The last two fields are mandatory under the combined ruleset. A strong generic chassis may not be legal for a nation. A mediocre-looking chassis may be the key to a powerful Divinitus infrastructure.

### 11.2 Chassis families

DE's large roster is best understood by job family.

**Immobile monuments.** These often exchange movement for high dominion, low design cost, strong paths, exceptional durability, or national effects. Divinitus frequently turns them into site and temple engines.

**Monsters.** DE's broad buffs make monsters more credible expanders and combatants. Their value still depends on attack density, protection, regeneration, resistances, item slots, affliction risk, and the first counter an opponent can deploy.

**Titans.** Additional paths and lower design prices make Titans more flexible. They can combine expansion with a serious blessing or late ritual access, but their size and investment make death costly.

**Rainbows and sages.** Cheaper designs and expanded paths improve access packages. Divinitus often adds libraries, apprentices, ritual range, items, or research-linked production.

**Aquatic and amphibious gods.** DE expands this roster and the strategic value of water access. A water god must still be assessed against the nation's starting theatre and ability to operate on land.

**Transforming gods.** Shape chains can separate map form, battle form, dominion form, death form, and ritual form. Every shape must be resolved; a source block for one form is not the complete god.

### 11.3 Expansion is an assignment, not a label

A chassis should be called an expander only after a repeatable test against the actual independent settings and terrain mix. DE changes weapons, mounts, and units as well as the Pretender, so a vanilla test result is not portable.

A minimum record includes:

- design and awakening;
- target province and defenders;
- script;
- hit points and afflictions after battle;
- fatigue at decisive moments;
- rout or morale incidents;
- number of provinces taken before support was required;
- first available counter;
- cost of losing one expansion turn.

### 11.4 Healing doctrine

The stated DE programme allows Pretenders to heal in the capital or to receive a 10% chance per Holy level while actively preaching outside the capital. This creates three recovery modes:

1. capital convalescence;
2. field preaching with probabilistic recovery;
3. magical or item-based healing.

The second is not free. Preaching consumes the monthly order and places the god in a predictable province. A wounded god that could forge, research, claim a Throne, cast a ritual, or fight is paying an opportunity cost to heal.

## 12. DE Magic, Items, and National Power

### 12.1 A spell is a delivery system

The expanded spell list should be indexed by function rather than memorized as one long sequence.

| Function | Examples of the question to ask |
| --- | --- |
| Access | Does the spell raise paths, create a mage, or unlock a form? |
| Army creation | What body, commander, upkeep, and leadership does a summon provide? |
| Force multiplication | Which troops receive the buff, at what area, fatigue, and research? |
| Control | Does it disable by MR, defence, size, morale, or terrain? |
| Damage | What protection layer, resistance, and density does it attack? |
| Mobility | Does it solve land, water, plane, range, or fort access? |
| Siege | Does it damage walls, defenders, infrastructure, or relief timing? |
| Economy | Does it convert gems, gold, population, blood slaves, or mage-turns? |
| Transformation | Is the result reversible, unique, cursed, or tied to another object? |

The same spell may occupy several rows. A summon can be path access, siege mass, and a combat package. An underwater ritual can be mobility and recruitment access.

### 12.2 National summons

DE generally raises the efficiency of national summons and updates older designs to Dominions 6 scale. A summon should be evaluated by:

`total cost = gems + caster-turn + research delay + laboratory position + command burden`

The result should be evaluated by:

`total return = body value + magic access + strategic movement + siege value + future turns`

A cheap body that requires a rare cap-only caster may be expensive. A moderate summon that creates a reusable mage can be an access breakthrough.

### 12.3 Items as logistics

The repriced item list changes the minimum infrastructure needed to execute a plan. The relevant categories are:

- path boosters and ritual access;
- reinvigoration and fatigue control;
- resistance packages;
- thug and supercombatant protection;
- underwater transport and breathing;
- mount and rider equipment;
- siege and wall pressure;
- temporary gems;
- battlefield auto-spells;
- restricted national or divine items.

An item catalogue should state the exact mod layer because the same named item may have different paths, costs, effects, or national rebates in vanilla and DE.

### 12.4 Future sites as an interface

Future sites are documentation objects embedded in the nation overview. They make national summons and heroes discoverable without revealing every tactical conclusion. For a website, these should be represented as overview records, not ordinary province sites.

## 13. DE Nations Without Nation Dossiers

Book IX does not replace the nation monographs. It establishes the questions each one must answer.

### 13.1 Recruitment reconstruction

DE can clear and rebuild a nation roster. A vanilla unit list may be only a historical starting point. The resolved recruitment table needs:

- capital, fort, unforted, coastal, underwater, cave, forest, mountain, swamp, waste, farm, and foreign recruitment;
- recruitment limits;
- command-point and resource gates;
- paired or event-created recruits;
- site-dependent commanders and troops;
- starting commander and army;
- province defence, walls, and fort defenders.

### 13.2 Magic reconstruction

The mage table needs:

- deterministic paths;
- random masks and probability distributions;
- temporary gems;
- path boosts and shape effects;
- cap-only and terrain limits;
- national spells and item rebates;
- communion, chorus, or other network roles;
- the cost of consuming a commander recruitment turn.

### 13.3 National strategic reconstruction

The public DE summary indicates four degrees of change:

1. **light balance correction** - costs, statistics, hero updates, or one new spell;
2. **mild overhaul** - roster or magic identity changes while the national concept remains;
3. **systemic overhaul** - new economy, recruitment, or dominion mechanics;
4. **new or DEified nation** - custom roster and full support package.

Advice should state the degree. A "mild overhaul" can still invalidate an opening if the old cap unit, random distribution, or sacred is gone.

### 13.4 New nations in the supplied source

The source contains full named nation blocks in reserved IDs 181-207, including Chaco, Ongtupqa, Sitecah, Albion, Zion, Bhöd, and later DE additions such as Bantay Tubig, Dirgen, and Houssa. Some public notes mark particular nations unfinished, removed, or pending. A source definition proves presence in the file; it does not prove current balance or recommended multiplayer inclusion.

## 14. Divinitus: Design Philosophy and Scope

### 14.1 The card becomes a constitution

Divinitus describes its purpose as making Pretender Gods more unique and lore-consistent without presumed excessive power creep. Its implementation gives a chassis rules that can affect the entire state.

The dominant patterns are:

- **starting covenant:** a capital site, item, army, commander, or scale package;
- **living dominion:** effects scale with candles or require positive dominion;
- **temple network:** each temple becomes a production or transformation node;
- **priesthood:** certain national mages or units gain Holy levels;
- **divine presence:** an effect requires the god alive, awake, present, preaching, searching, or performing another order;
- **seasonal office:** winter, summer, or another calendar condition changes production;
- **terrain office:** caves, forests, coasts, wastes, mountains, or water enable an effect;
- **relationship state:** control of a named unit or global enchantment unlocks a benefit;
- **cosmic consequence:** moving or losing a monument triggers a world event;
- **battle manifestation:** a spell, escort, blessing-site effect, or divine shape appears in combat.

### 14.2 The four source tiers

The main Pretender body is divided by starting dominion headings.

| Source tier | Object blocks | Events | Monster blocks | Sites |
| --- | ---: | ---: | ---: | ---: |
| Dominion 4 | 542 | 385 | 134 | 21 |
| Dominion 3 | 768 | 510 | 217 | 40 |
| Dominion 2 | 633 | 383 | 216 | 34 |
| Dominion 1 | 401 | 236 | 143 | 22 |

Monster blocks combine selected and new definitions. Site totals include new and selected sites. The file then applies eight small DE-tail monster selections, principally home-realm compatibility.

These headings organize authorial work. The final starting dominion should still be read from the active object's fields because a selected block may not restate it and a shape may not be a selectable root.

### 14.3 Chassis scale

Among 320 Divinitus monster blocks carrying at least one Pretender-like field:

- 305 carry descriptions;
- 297 state a gold or design cost;
- 258 state a path cost;
- 201 state starting dominion;
- 181 state a home realm;
- 132 use `#magicboost`;
- 167 use healing;
- 66 use ordinary `#domsummon`;
- many add one-battle spells, start items, scale modifiers, or shape relationships.

This does not mean exactly 320 independently selectable gods. The set includes forms and support definitions. It proves the density of divine reconstruction.

## 15. The Divinitus Event Engine

### 15.1 Why 1,514 events exist

Dominions has no single command meaning "every temple in friendly dominion has a candle-scaled chance to recruit a special priest while the god is awake." Such a power is assembled from small declarative events.

A typical system needs:

1. an event identifying the correct Pretender;
2. a province, terrain, site, temple, fort, dominion, or order requirement;
3. a probability gate;
4. an effect;
5. sometimes a variable or event code;
6. sometimes a delayed cleanup;
7. often a silent message configuration.

The large event count is working infrastructure, not 1,514 ordinary random narratives.

### 15.2 Event profile

| Command or pattern | Occurrences |
| --- | ---: |
| New events | 1,514 |
| `#req_godismnr` | 1,641 |
| Province-owner events (`#nation -2`) | 1,504 |
| Silent log suppression (`#nolog`) | 1,446 |
| Population-zero permitted | 1,183 |
| No displayed text | 1,023 |
| Dominion minimum | 602 |
| Candle-scaled chance | 557 |
| Land requirement | 543 |
| Target monster | 434 |
| Own capital | 370 |
| Temple | 311 |
| Pregame only | 179 |
| Fort | 173 |
| Free site slots | 157 |
| Site required | 148 |

The multiple `#req_godismnr` commands in one event are alternatives: several related gods can share one effect.

### 15.3 Rarity 5

The official Event Manual states that rarity 5 is an unlimited always-event class: any number can occur in one province in the same month. It is suitable for global-enchantment and special-dominion machinery.

Divinitus uses rarity 5 for 1,492 events. This permits many independent divine checks to run without consuming an ordinary random-event slot.

### 15.4 Candle-scaled probability

The official meaning of `#req_domchance X` is:

`chance = absolute dominion strength x X percent`

The event must already satisfy its other requirements. The command itself does not care who owns the dominion, so correct systems combine it with ownership or Pretender requirements where friendly dominion is intended.

Examples:

- `#req_domchance 1` gives 1% per candle;
- `#req_domchance 5` gives 5% per candle;
- `#req_domchance 10` gives 10% per candle.

At ten candles these become 10%, 50%, and 100% respectively before other gates. A description that says “candles x 5%” has a direct mechanical basis.

### 15.5 Event probability is conditional

A 50% candle check is not a 50% monthly yield if the event also requires:

- the god to be awake;
- the god or target to be in the province;
- a temple or fort;
- a free site slot;
- a season;
- a particular order;
- a path threshold;
- a unique event not already used;
- a variable in the correct state.

Expected value should multiply the conditional probabilities or explicitly state that it is conditioned on every non-random gate being true.

### 15.6 Pregame events

The official manual states that `#req_pregame` events happen during game creation and appear in the first turn's messages. Divinitus uses 179 such events for starting armies, sites, items, commanders, and initial state.

Pregame content is part of Pretender design value even though it does not appear in the chassis statistics. Losing or duplicating one of these events can alter an opening materially.

## 16. Divinitus Power Families

### 16.1 Capital institutions

Many gods create a capital site or add one when awakening. Common returns include:

- gem income;
- gold and resources;
- recruitable mages;
- apprentices;
- divine servants;
- ritual discounts;
- a special bless effect;
- national path access.

A capital institution should be valued as a stream:

`present value = starting grant + monthly income + recruitment options + strategic access - site-slot and opportunity costs`

The exact duration matters. A site present from game creation is more valuable than one appearing only when a dormant god awakens.

### 16.2 Temple networks

Temple events turn religious infrastructure into production infrastructure. A temple may:

- create units or commanders;
- produce gems, blood slaves, or gold;
- apply a blessing site;
- change scales or dominion;
- grant recruitment;
- transform or ordain priests;
- host a terrain-specific resource.

The value of one more temple becomes:

`ordinary temple value + expected divine output + dominion projection + local strategic value`

This can justify earlier and wider temple construction, but only if the expected output exceeds construction cost, opportunity cost, and capture risk.

### 16.3 Priesthood transformations

Divinitus uses 203 `#holyboost` effects and many target gates to ordain national mages, commanders, or thematic servants. A mage who becomes H1 or H3 changes:

- preaching;
- banishment;
- blessing access;
- temple construction eligibility;
- leadership in sacred armies;
- communion or spell interactions where Holy matters;
- upkeep and recruitment opportunity only indirectly.

The event may occur immediately after recruitment, require a temple, or depend on the god. The exact gate must be recorded.

### 16.4 Dominion summons

Built-in `#domsummon`, `#domsummon2`, `#domsummon20`, and rare dominion summons produce followers around the god. Event-based temple summons distribute production across the map.

The distinction matters:

- chassis dominion summons usually require the god's physical presence;
- temple events require qualifying provinces;
- capital events concentrate output;
- some systems require the god awake or alive;
- some descriptions cap production by candle count.

### 16.5 Scale ceilings and extreme scales

Some gods carry `#moreorder`, `#moreprod`, `#moregrowth`, `#moreluck`, `#moremagic`, or temperature modifiers. Divinitus descriptions sometimes attach additional effects to scales beyond the ordinary limit, such as income, unrest reduction, or special events.

The design value has two parts:

1. design-point and national-scale consequences;
2. event or province consequences once the higher scale exists.

### 16.6 Built-in battlefield policy

Divinitus uses one-battle spells and hidden support spells for effects such as:

- army blessing by creature type;
- battlefield-wide path boosts;
- Solar Brilliance;
- Relief;
- Wind Guide;
- animal blessing;
- mass regeneration;
- control or serenity effects;
- divine earthquakes;
- special summons.

These spells often use school -1 and research level 0. They are internal tools, not ordinary research targets.

### 16.7 Orders as divine labour

Some powers require the Pretender to:

- preach;
- search for sites;
- research;
- remain in the capital;
- occupy a fort;
- stand on a Throne;
- perform another target order.

The god's monthly order is a scarce resource. A power that pays 150 gold when site searching is not free income; it competes with every other use of the god.

## 17. Representative Divinitus Systems

### 17.1 Golden Pillar: geographic catastrophe

The Golden Pillar gains strong Earth magic, dominion summons, additional scale reach, and cave-temple production. The exceptional mechanic is triggered when the Pillar is absent from its own capital.

The source chain:

1. an immediate global rarity-13 event requires the Golden Pillar Pretender, its own capital, and the Pillar's absence;
2. a unique gate prevents repetition;
3. event code `-3333` is set;
4. world unrest rises by 15;
5. surface provinces receive follow-up earthquake checks;
6. population, temples, and laboratories can suffer;
7. troglodyte attacks and a capital force can appear;
8. a later global event resets the code to zero.

This is a strategic constraint, not flavour. Moving, teleporting, or otherwise displacing the god can impose worldwide costs.

### 17.2 Father of Winters: seasonal global state

The Father of Winters uses variables 329, 330, and 331 to track successive winter-month effects. Monthly events increment and decrement the correct variable, while follow-up events can kill population and worsen Cold outside the protected ownership state.

The design lesson is that a seasonal power may be implemented as several synchronized state machines. Reading only one event produces a false picture.

### 17.3 Kami of Storms: ownership relationship

The Kami of Storms checks whether the nation controls Aella, Queen of Storms. Event variable 325 records that state.

- control sets the variable;
- loss or defection clears it;
- while the variable is positive, temples in qualifying dominion can spawn large Air Elementals;
- a separate capital site grants the innate Air Shield blessing effect.

This power rewards a specific world-state rather than a fixed chassis statistic.

### 17.4 Divine Feathered Serpent: delayed global offensive

The Divine Feathered Serpent can initiate a hurricane state using variable 326. The source:

- makes a capital, dominion-scaled check;
- sets a global state in an immediate event;
- permits up to three enemy-fort hurricane events per month;
- applies population loss and unrest;
- ends and clears the state through later events.

This is strategic remote pressure. Its actual target distribution and engine event ordering still deserve live verification before exact expected-damage claims.

### 17.5 Great Stag: global enchantment relationship

The Great Stag interacts with The Wild Hunt:

- the active friendly enchantment can bring a Horned One;
- variable 328 tracks whether the state is active;
- the Horned One receives path and priest boosts;
- temple events produce Cu Sidhe;
- cleanup events kill the Horned One and clear the variable when the enchantment is absent.

The power has a research and global-enchantment dependency. It is not fully online at game creation.

### 17.6 Once and Future King: province quest chain

The Once and Future King uses event code `-513`:

1. a qualifying province receives rumours;
2. the province is flagged;
3. a Holy Knight can resolve the quest;
4. outcomes include combat, gold, gems, or a magic item;
5. successful resolution resets the code to zero.

The event code is province-local. A world or nation may have several quest provinces, subject to the event gates.

### 17.7 Grand Hierophant: divine labour and mage development

The combined Grand Hierophant:

- begins from DE's revised monster 3053;
- receives Divinitus cost 150;
- gains +1 to all non-priest magic paths through `#magicboost 53 1`;
- has 75 bad-event protection and disease resistance 100;
- can anoint a Mystic or Erytheian Mystic into a Mystic Prophet;
- can teach the transformed mage;
- can gain 150 gold and elemental gems while site searching under a candle-scaled event.

The site-search reward uses `#1d6vis 51`. Path group 51 is Elemental, so a successful event grants 1d6 each of Fire, Air, Water, and Earth gems: an expected 14 total elemental gems on success.

With `#req_domchance 5`, the conditional success chance at `c` candles is `0.05c`. Conditional expected output per eligible month is:

- gold: `150 x 0.05c = 7.5c`;
- total elemental gems: `14 x 0.05c = 0.7c`.

These values assume every other gate is satisfied and do not subtract the opportunity cost of the Site Search order.

The teaching event visibly gates the target's Astral threshold while increasing Astral, Fire, Water, and Earth. The broad description states a maximum of three. Whether an elemental path can pass the stated cap under all Mystic randoms remains unresolved without a reliable engine reproduction.

## 18. Divinitus Support Objects

### 18.1 Hidden spells

Divinitus contains 26 new-spell blocks and 17 selected-spell blocks. Almost all set school -1 and research level 0, showing that they are components of divine powers and not additions to the ordinary research tree.

Major families include:

| Family | Examples |
| --- | --- |
| Permanent gifts | Gift of Rebirth, Forge Skill, Healing Power, Demonic Ascendance |
| Training rituals | Teachings of the Cyclops, Imbue with Medicine, Lore of Dreams |
| Divine control | Master Enslave Sacreds, Void Enslave, Demon Enslave |
| Army blessing | Master Magic Blessing, Master Demon Blessing, Master Beast Blessing |
| Battlefield policy | God Quake, Boar Frenzy, Desert Guidance, Honed Steel |
| Path and enchantment | Guidance of the Spheres, Power of the Northern Star, Star Power |
| Mind and creation | Divine Spark, Spark of Intellect, Imbue Astral Power |
| Item or chassis effects | Plague Arrow, Inhabit Grove, Judge of Life and Death |

The 43 blocks include helper effects such as Major Insanity and Caster Confusion. A website should mark these as hidden or granted mechanics unless the resolved school and restrictions make them ordinarily accessible.

### 18.2 Divine items

Divinitus selects item slots 1000-1073 and creates item 1072. Most use Construction level 11. The official manual defines level 11 as unforgeable. Level 13 means an unforgeable unique artifact.

These items are commonly:

- start items carried by a specific god;
- event-created priesthood tools;
- cursed and non-transferable signatures;
- spell containers;
- unique expressions of divine lore;
- mechanisms for granting an ability that the chassis command set cannot express directly.

The family includes Void Pearl, Orb of the Nerid, Calathos, Kusanagi-no-Tsurugi, Feather of the Phoenix, Hammer of the Cyclops, Bowl of Blood, Medicine Bag, Fate Charm, Tome of Lore, Bow of Plagues, Golden Arm, Staff of Beasts, Windborne Sail, Rain Stick, Horn of Vanhalla, Staff of the Geyser, Mirror of Dreams, The Last Wish, and Fish Scale Mail.

The source also modifies Soul Contract and Lifelong Protection with `#undcommand 15`, supporting an Infernal Spirit priesthood system.

### 18.3 Divine sites

Divinitus adds 112 sites and selects 5 existing sites. They are predominantly level-0, rarity-5 support sites managed by events.

Functional groups include:

- blessing sites such as Blessing of Winter, Wind, Earth, Vitality, and Brilliance;
- temple sites such as Temple of the Warrior, Solar Temple, Temple of Storms, and Temple of the Sacred Band;
- recruitment sites such as Apprentice Quarters, Grove of Enchantment, Library of Lore, and Grand College;
- economic sites such as Riches of the Underworld, Jewelled Cavern, and The Crystal Cavern;
- state markers such as Ritual Aftermath, Empty Plinth, Empty Vault, and Unusual Crystal Formation;
- terrain institutions such as Coral Barracks, Deep Forest Clearing, Frozen Barrow, and Bottomless Lake.

A site can be player-facing, a hidden marker, a recruitment interface, or all three. The catalogue must record how it enters and leaves play.

### 18.4 Weapons and armour

Divinitus adds special weapons numbered 3001-3035 and two armours. These principally serve gods and their items. Examples include Kusanagi-no-Tsurugi, Magic Lariat, Caduceus, Golden Bow, Burning Ray, Lightning Blade, and Perfect Fist.

Weapon 3034 is defined twice. The later definition copies Stellar Bolt and is referenced as Stellar Bolt by the Stellar Staff and related units. Source references establish the later practical role.

## 19. Combined Load Order and Collision Matrix

### 19.1 Direct selected-object overlap

| Type | DE distinct selected | Divinitus distinct selected | Shared |
| --- | ---: | ---: | ---: |
| Monster | 3,185 | 373 | 357 |
| Item | 629 | 75 | 2 |
| Spell | 2,737 | 17 | 0 |
| Site | 572 | 5 | 0 |
| Nation | 128 | 0 | 0 |
| Weapon | 142 | 0 | 0 |
| Armour | 38 | 0 | 0 |

The two shared selected items are Soul Contract 348 and Lifelong Protection 396.

### 19.2 Cross-action monster overlap

The earlier direct-selector table understated the integration because Divinitus frequently uses `#newmonster` on a fixed ID that DE also created or selected.

| Relationship | Shared numeric IDs |
| --- | ---: |
| DE new / Divinitus new | 235 |
| DE new / Divinitus selected | 10 |
| DE selected / Divinitus new | 114 |
| DE selected / Divinitus selected | 357 |

These groups overlap with one another because DE may both create and later select the same monster. Divinitus touches 650 distinct fixed monster identities; 600 of them also appear in a DE monster action. In addition, Divinitus creates 69 automatically numbered monsters.

This proves that the DE edition is deeply integrated. It also creates a large compatibility surface.

### 19.3 Event codes and variables

| Registry | DE | Divinitus | Shared |
| --- | --- | --- | --- |
| Event codes | -540, -312 to -308, -302 to -300, 0 | -3333, -513, 0 | 0 |
| Event variables | 6001-6007, 6011 | 325, 326, 328-331 | none |

Code 0 is the official default and reset state, so its use in both mods is expected. No nonzero event-code collision and no variable collision were found.

### 19.4 Automatic allocation

Automatic events are ordinary because `#newevent` has no fixed event ID in the same sense as a monster. Automatic monsters and spells are a different concern. Divinitus contains:

- 69 numberless new monsters;
- 26 automatically allocated new spells under the current official `#newspell` syntax.

Their final IDs depend on the occupied space after earlier mods. The supplied text proves definition order and content but not resolved numeric identities. The independent integrity publication records one exact-version Data Inspector resolution for all 69 monsters and 26 spells; those numbers remain versioned secondary keys rather than permanent object identities.

## 20. The 8616 Collision

### 20.1 Exact source facts

DE creates monster 8616 as a hidden "Bulk crafting land depositer." It has a deliberately generic `inventory.` name, zero gold cost, two miscellaneous slots, extreme stealth, land damage 99, and DE water-overhaul graphics.

Divinitus later creates monster 8616 as "Crystal Priest," copying Crystal Mage 340, adding E2G2H2, commander-master status, and recruitment cost fields. The Crystal Cavern then recruits monster 8616.

This collision is not a parser inference. Both exact blocks explicitly claim the same fixed ID. The public Divinitus 1.15.2 DE source also used 8616 for Crystal Priest, so the pattern predates the supplied 1.15.3 file.

### 20.2 Likely consequence

Under the frozen order, the later Divinitus definition has the final opportunity to occupy or alter 8616. DE references intended to create or manipulate the hidden bulk-crafting depositer may resolve to the Crystal Priest or to an engine-dependent merged state.

The official manual warns that two mods changing the same object can behave unpredictably. Without a reliable in-engine reproduction, the library does not assert an exact runtime card. It classifies this as:

**Source-confirmed high-risk compatibility collision; runtime resolution pending.**

### 20.3 Practical policy

For the unmodified supplied files:

- do not assume DE bulk crafting that depends on monster 8616 is safe;
- do not remove or renumber the Divinitus Crystal Priest casually, because its site and events reference it;
- treat any unexpected land bulk-crafting inventory, Crystal Priest, or item-deposit behaviour as related evidence;
- preserve the exact two files when reproducing;
- record which mod the game actually loaded first.

### 20.4 Independent compatibility publication

After Progress Edition 17, the collision was taken into a separate technical publication rather than expanded into another encyclopedia chapter. *The DE-Divinitus Compatibility and Integrity Report* confirms the intended order, traces the complete 8616 dependency chain, records the 69 automatic monsters and 26 automatic spells under the pinned Data Inspector build, and classifies every active command token against the official manuals, patch history, and current parser.

A separate repaired edition, `Divinitus_1.15.3_DE_compat_8616.dm`, removes Crystal Priest's fixed claim on 8616 and changes The Crystal Cavern to recruit it by name. The two uploaded originals remain unchanged. The repair passed its static and Inspector validation suite, but live-engine acceptance remains pending and a new game is required.

That work is deliberately independent. Book IX continues to describe the original frozen files and points outward for the remediation record; it does not silently replace the original Divinitus layer or absorb the repair package as Foundation Book XV.

## 21. Combined Pretender Resolution

### 21.1 Field-by-field method

For a selected chassis:

1. extract the vanilla card;
2. apply every DE block for that identity in DE parse-category order;
3. follow shapes and copied statistics;
4. apply every Divinitus block;
5. attach Divinitus items, sites, spells, and events;
6. attach national legality from the DE nation blocks;
7. classify unresolved inherited or engine-dependent fields.

For a fixed new ID shared by both mods, add a collision warning before assuming a simple overwrite.

### 21.2 Final-card schema

Every combined Pretender page should contain:

- identity and all forms;
- ruleset and hashes;
- nations and realms;
- design cost, path cost, starting dominion, and awakening limits;
- paths and path boosts;
- forced scales;
- physical and leadership statistics;
- item slots and starting items;
- battle spells and escorts;
- dominion summons;
- pregame grants;
- temple, fort, terrain, season, and order powers;
- event codes and variables;
- failure and cleanup conditions;
- source provenance by layer;
- unresolved runtime questions;
- strategic jobs and counters.

### 21.3 Do not sum every line

Not every repeated numeric field is additive. A later `#gcost` replaces the prior value. A `#magicboost` adds or subtracts paths under its own semantics. A clear command erases inherited fields. A copied object imports a base before later edits. An event effect occurs conditionally in play rather than changing the design card.

Resolution is typed, not arithmetic.

## 22. Strategic Doctrine for the Combined Ruleset

### 22.1 Pretender value has four ledgers

**Design ledger.** Points, paths, dominion, awakening, and scales.

**Body ledger.** Expansion, combat, movement, survival, slots, and healing.

**State ledger.** Sites, units, commanders, gems, gold, priesthood, and temple output.

**Risk ledger.** Catastrophic triggers, dependence on divine life or location, event exposure, and counters.

A god that is mediocre in the body ledger can dominate the state ledger. A powerful expander can be a poor design if death disables a national engine.

### 22.2 Dominion is productive capacity

Divinitus turns candles into probabilities and thresholds. Dominion now influences:

- ordinary religious survival;
- blessing projection;
- temple-event frequency;
- commander and unit production;
- economic events;
- terrain conversion or settlement;
- global attacks;
- scale changes;
- divine relationships.

Dominion investment should be assessed by marginal output as well as religious security.

### 22.3 Temples are an industrial network

Where a god has temple powers, the optimal temple count may rise sharply. The calculation should use:

`monthly expected output per temple x expected safe months`

against:

`temple gold + priest turn + defence cost + capture risk + alternative investment`

The network also has geometry. A border temple may project dominion and produce troops but be easy to capture. An interior cave temple may be safer and satisfy terrain gates.

### 22.4 Awakening changes institution timing

An imprisoned god may provide a non-Incarnate blessing immediately but delay a Divinitus capital site, priesthood, or temple network. An awake god may start the institution early but consume design points and face battlefield risk.

The correct question is:

> On which turn does each part of the design begin paying?

### 22.5 Gems are monthly endurance

DE gem longevity changes battle planning. A gem stock on a mage is a reusable monthly combat allowance. This favours:

- mobile defensive casters;
- sequential fort relief;
- several small battles with the same mage;
- survival gear and retreat planning;
- intelligence about later battles in the same month.

It also rewards the opponent for forcing a poor early battle, routing the mage, blocking movement, or killing the gem carrier.

### 22.6 Research has more branches

DE expands viable national spells, summons, underwater tools, and siege options. Divinitus adds hidden chassis effects but usually not ordinary research goals. The queue should be built around national DE breakpoints and the Pretender's requirements, not the Divinitus helper-spell list.

### 22.7 Counter the system, not only the body

Possible counters include:

- killing or imprisoning the god;
- forcing it away from a required capital or terrain;
- raiding temple provinces;
- denying a key global enchantment or unique unit;
- occupying the site that grants recruitment;
- exhausting site slots;
- disrupting a specific monthly order;
- capturing high-dominion provinces;
- attacking before an awakening-gated institution appears;
- exploiting a catastrophic movement trigger.

## 23. Website Architecture

### 23.1 Core entities

The website should use typed entities rather than one undifferentiated text index:

- ruleset;
- source file;
- object block;
- resolved object;
- monster form;
- nation;
- spell;
- item;
- site;
- blessing;
- event;
- event code;
- event variable;
- relationship;
- claim;
- test;
- article.

### 23.2 Layered object identity

One visible object page should offer tabs:

1. vanilla 6.35;
2. DE 2.16;
3. Divinitus 1.15.3 on vanilla, where meaningful;
4. DE 2.16 plus Divinitus 1.15.3;
5. historical versions.

Each field needs provenance. A cost may come from Divinitus while item slots come from DE and base protection remains vanilla.

### 23.3 Event relationships

Events should not be displayed as 1,514 isolated cards. They should be grouped into systems:

`Pretender -> event family -> gate -> effect -> state -> cleanup`

The Once and Future King quest chain, Golden Pillar earthquake, Father of Winters calendar, and Great Stag Wild Hunt relationship are ideal graph views.

### 23.4 Search facets

Useful filters include:

- source layer and version;
- object type and ID;
- nation and age;
- path and school;
- research level;
- terrain;
- temple, fort, capital, and dominion requirements;
- awakening dependency;
- order dependency;
- starting dominion tier;
- scale modification;
- event code or variable;
- direct source, derived, or pending status;
- known collision.

### 23.5 Data already produced

This research edition includes:

- `mod-index-summary.json` - hashes, counts, ranges, overlaps, event registries, and warnings;
- `mod-object-catalogue.tsv` - one row per active source block;
- `mod-object-blocks.jsonl` - full command streams and source lines;
- `extract_mod_index.py` - reproducible extractor.

The JSONL is a source index, not a resolved database. That distinction should appear in the website interface.

## 24. Verification Protocol

Book VIII contains the reusable validation ladder. Applied to this ruleset, every source claim must capture the complete object history across vanilla, DE, and Divinitus, then follow support items, sites, spells, shapes, and events before a final card is asserted.

A collision-sensitive card is reliable only when it comes from the exact files and order through a current inspector, controlled game, or documented engine export. An unversioned screenshot is useful as a clue, not as resolution.

Divinitus event tests must also preserve the Pretender, nation, turn, season, terrain, dominion, sites, order, target, relevant code or variable state, eligible province-months, and delayed effects. Candle-scaled probability should be compared with eligible trials rather than with anecdotal successes.

## 25. Open and Resolved Compatibility Register

### 25.1 Resolved from source

- The exact file hashes and versions are fixed.
- DE's six global commands are known.
- The complete DE blessing change set is known.
- Event-code registries have no nonzero cross-mod collision.
- Event-variable registries do not collide.
- Shared selected items are IDs 348 and 396.
- DE and Divinitus share 235 fixed new-monster IDs.
- Divinitus touches 600 fixed monster identities also touched by DE.
- Divinitus weapon 3034 is assigned twice, with the later Stellar Bolt definition used by later references.
- Monster 8616 is claimed by incompatible-looking DE and Divinitus definitions.
- Later author-facing project wording establishes DE first and Divinitus second as the intended order.
- The source contains 69 automatic monster declarations and 26 automatic spell declarations under current documented syntax.
- The pinned Inspector resolves every original automatic monster and spell for the exact frozen order; those numbers remain structured-tool evidence rather than engine exports.
- The independent command audit separates officially documented tokens, later parser-recognised tokens, Inspector annotations, likely spelling errors, and genuinely unresolved commands.
- A separate compatibility edition removes the 8616 collision without altering either uploaded original.

### 25.2 Pending reliable resolution

- exact engine behaviour when a later mod issues `#newmonster` on an occupied fixed ID;
- engine confirmation of the Inspector-resolved 8616 behaviour in the unmodified stack;
- live-engine acceptance of Crystal Cavern recruitment and DE's Ring, Amulet, and Blood Vial helper chains under the repaired edition;
- engine confirmation of the Inspector-resolved automatic identities;
- the Mystic Prophet elemental-path cap edge case;
- exact event scheduling order for several global state machines;
- whether all broad description claims match every rare gate and cleanup path;
- runtime semantics for the small set of commands left unresolved by the independent command audit.

### 25.3 Deliberately not requested from the player

This project does not require the player to perform these tests. They remain pending until a reliable published reproduction, exact inspector export, or local Dominions executable is available.

## 26. Operational Checklists

### 26.1 Before creating a game

- Verify Dominions 6.35 or record the actual patch.
- Verify both exact mod filenames.
- Verify hashes where multiplayer reproducibility matters.
- Enable DE before Divinitus under this library's frozen ruleset.
- Do not add another overhaul without a collision screen.
- Record map, age, thrones, research, independents, event frequency, and diplomacy rules.
- Design Pretenders under the active mods, not vanilla.

### 26.2 Before finalizing a Pretender

- Confirm the chassis is legal for the nation after DE.
- Record every forced scale and path cost.
- Read every form.
- Read the full Divinitus description.
- Identify starting items, sites, armies, and commanders.
- Identify awakening gates.
- Identify temple, terrain, season, and order gates.
- Identify any catastrophe or cleanup condition.
- Recalculate blessing activation under DE.
- Check whether the design depends on a collision-marked object.

### 26.3 First twelve turns

- Confirm pregame grants arrived.
- Inspect capital sites and recruitment.
- Check starting items and commanders.
- Note which powers require the god awake.
- Build temples only after valuing their divine output.
- Track gem-bearing mages by month under gem longevity.
- Use DE's site-search clues.
- Record unexpected units, sites, or events with province and turn.

### 26.4 Multiplayer host

- Distribute exact versions, not only Workshop names.
- Publish load order.
- Prohibit silent midgame mod updates.
- Archive the `.dm` files.
- State whether known collisions are accepted.
- Record any house ruling for an exploit or broken divine chain.

## 27. Essays

### Essay I - Dominions Enhanced Is a Ruleset, Not a Content Pack

Calling Dominions Enhanced a content mod understates it. Content can be added while the surrounding grammar remains stable; DE changes the grammar.

A stronger bow is not only another weapon. It changes how light infantry trade with armour, how shields are valued, how much battlefield space missile troops deserve, and when arrow protection becomes urgent. Better mounts do not only improve cavalry. They change charge exchanges, magical vulnerability, rider survival, and the value of barding. Cheaper water breathing does not only add convenience. It changes which borders are real.

The six global commands demonstrate the same point at the highest level. Order, Productivity, population change, Luck event frequency, and battle-gem persistence alter calculations that every nation makes. Even a nation with no special DE roster change lives under these laws.

The magic programme expands the number of credible research branches. That reduces the reliability of memorized queues. A player who knew the vanilla breakpoint for an opponent now faces additional summons, battlefield effects, transformations, and siege tools. Information becomes more valuable because the option tree is wider.

The nation programme confirms the scale. Some nations receive corrections; others receive new rosters, economies, dominion rules, or successors. New nations occupy the same world and participate in the same Pretender and spell ecosystem.

The useful way to read the combined game is:

> DE is an alternate edition of Dominions 6 built through the modding language.

That model produces better habits. Version numbers appear on guides. Vanilla and DE advice remain separate. Object pages show provenance. Multiplayer hosts freeze files. Strategy begins with the active rules rather than with memory.

### Essay II - The Pretender as a Distributed Institution

In ordinary analysis, a Pretender has a body, paths, dominion, scales, and a blessing. Divinitus adds a fifth category: institutions.

A library that recruits sages is not part of the god's hit-point total, but it may generate more research than another path level. A temple that creates sacred units is not printed in attack density, but it can transform the nation's force structure. A priesthood event can give existing national mages a second strategic role. A seasonal engine can reshape population and scales across many provinces.

This changes the meaning of divine death. If a power requires only the chosen chassis identity and continues while the god is dead, the institution may be resilient. If every event requires `#req_pretawake`, physical presence, or a target order, death shuts down the state.

It changes the meaning of dominion. Candles become production multipliers. It changes the meaning of temples. They become factories and access nodes. It changes the meaning of awakening. Delayed arrival may postpone an entire economy.

A distributed institution can also be countered indirectly. Raiders can burn temples. A unique relationship unit can be killed. A global enchantment can be dispelled. A required terrain can be denied. A site can be captured. The god need not be defeated in battle to dismantle the system.

The best design analysis draws a network:

`god -> dominion -> temples/sites -> output -> army/research/economy`

and then marks every dependency. A body card shows power. A dependency graph shows resilience.

### Essay III - Monthly Gem Persistence Changes Operational Art

In a one-battle accounting model, a combat gem is spent at the moment of use. Under DE's monthly longevity rule, the gem is better understood as a license to cast during all eligible battles that month.

This changes the unit of planning from battle to itinerary.

A mage defending a fort, teleporting to a second battle, and participating in a third interception may reuse the same initial allocation. Survival and position become part of gem efficiency. A two-gem script on a fragile mage is no longer only a two-gem risk; it is the potential loss of several battles of access.

The rule also changes how an opponent should apply pressure. Several battles do not necessarily exhaust the gem carrier. The effective counters are to kill, rout, immobilize, isolate, or force the wrong early script. Intelligence about movement order and likely sequential battles gains value.

Economically, the marginal value of a battle gem rises with the number of useful battles per month. Strategically, this favours interior lines and mobile casters. Tactically, it rewards scripts that remain useful across varied fights, or careful rescripting when the game permits it before hosting.

The rule does not make gems infinite. Ritual expenditure, forging, global enchantments, and treasury allocation remain real. It makes battlefield allocation persistent within a calendar boundary. That boundary belongs in every operational plan.

### Essay IV - Versioned Knowledge Is the Real Encyclopaedia

An encyclopaedia is often imagined as one perfected description. Dominions does not permit that simplicity.

Patches change spells and units. DE changes the patch again. Divinitus changes DE. Load order changes the combination. A later release may repair an ID collision while adding a new event gate. A correct article can become wrong without any sentence changing.

The solution is not constant rewriting without history. It is versioned knowledge.

Each claim needs:

- a ruleset;
- a source date;
- an evidence label;
- object provenance;
- an optional supersession link.

The public article can remain easy to read. The complexity belongs in its metadata and source panel. A visitor choosing "DE 2.16 + Divinitus 1.15.3" should see the correct Grand Hierophant. A visitor choosing vanilla should not.

Versioned knowledge also improves strategy. Old tournament advice can remain valuable when its assumptions are visible. A build that failed under one blessing cost can be reconsidered under another. A nation overhaul can be studied as design history rather than erased.

The real encyclopaedia cannot be a book of static answers. It needs to answer:

> Correct under which world?

### Related essays kept in their original homes

Book III's "A Bless Is a Roster Contract" owns the blessing argument. Book VIII's essays on load order, event systems, and compatibility own the general modding arguments. Book IX applies those ideas to the exact DE/Divinitus ruleset without printing a second version of the same essay.

## Appendix A - Source-Lint Findings

1. DE contains one extra `#rarity 5` and `#end` after site 2372 outside an active object block.
2. DE contains one adjacent event start without an intervening `#end`.
3. Divinitus contains four adjacent event starts without intervening `#end` commands in the Annunaki population chain.
4. Divinitus defines weapon 3034 twice.
5. Divinitus contains one event without an explicit rarity.
6. DE and Divinitus both create 235 of the same fixed monster IDs.
7. Monster 8616 has an especially divergent cross-mod purpose.

These are source observations. They do not by themselves prove a user-visible defect.

## Appendix B - Data Schema Warning

The generated object catalogue stores source blocks. It does not:

- import vanilla object cards;
- execute clear and copy semantics into a final card;
- allocate numberless objects;
- simulate category parsing;
- evaluate event probability;
- follow every name reference;
- reproduce the engine.

It is a provenance and discovery layer. A resolved website database should be built on top of it, never silently substitute it for final game data. The source summary remains in Section 2, the compatibility checklist in Section 26, and the library-wide evidence key in Book I.
