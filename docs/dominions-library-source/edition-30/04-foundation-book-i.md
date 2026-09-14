# Foundation Book I: Rulesets, Language, and the Anatomy of a Turn

## Why this volume comes first

Most rules in Dominions 6 are manageable on their own. The difficulty comes from having hundreds of them interact during the same turn. A player may understand recruitment, movement, rituals, battles, dominion, and upkeep separately, then still misread a result because they resolved in an unexpected order.

Book I sets out the language and turn order used throughout the library. It works at three levels:

- **New-player level:** enough explanation to understand what an order does, when it happens, and why an apparent failure occurred.
- **Experienced-player level:** exact timing relationships, failure points, and strategic consequences.
- **Research level:** a versioned record of sources, interpretations, and unresolved edge cases.

Nation-specific builds are left for later books. The examples use ordinary commanders, troops, provinces, rituals, and forts so the same conclusions can be used in any age.

> **Foundation rule:** A strategy should never depend on an unexplained timing assumption. When a plan works only because one action resolves before another, that timing needs to be stated here.

## How to read the library

There is no need to read the whole library before playing. The boxed rules, plain-language summaries, and checklists are enough to support a first campaign. The full chapters become useful when a turn behaves strangely, a multiplayer plan depends on exact timing, or a rule needs to be checked for publication. Source notes and unresolved tests sit alongside the rules so that doubtful points remain visible instead of becoming folklore.

### Where each subject lives

Each rule has one main home. Later books may give a short reminder when the subject crosses into another system, but the full explanation should not be repeated.

| Subject | Authoritative home |
| --- | --- |
| terminology, evidence labels, ruleset versions, and hosting order | Book I |
| order-writing formulas needed at a glance | Turn and Economy Quick Reference |
| provinces, income, recruitment, infrastructure, supply, PD, and siege economy | Book II |
| Pretenders, dominion, scales, blessings, and religious systems | Book III |
| formations, combat arithmetic, morale, fatigue, and battle resolution | Book IV |
| research, paths, gems, communions, rituals, items, and magical strategy | Book V |
| expansion, intelligence, logistics, war, diplomacy, and victory conversion | Book VI |
| nation-dossier method and faction-specific application | Book VII onward |
| mod construction, events, AI scaffolding, maps, testing, and compatibility method | Book VIII |
| exact Dominions Enhanced and Divinitus definitions and combined-load-order findings | Book IX |

The quick reference is the one deliberate exception. It repeats a small number of formulas and timing facts from Books I and II because its purpose is to remain open while orders are written. It should never become the source of a new rule.

## The baseline used by this edition

### Public unmodded baseline

The current public game release recorded by Illwinter on 25 August 2026 is **Dominions 6.36**, released on 17 August 2026 UTC. The principal rules source remains the **Dominions 6 Manual, revision 2**. The official documentation page presents that manual as the main reference for the rules and tables of the game.

The preserved manual is 449 PDF pages and has this fingerprint:

`65f430fd97c9f27285d63b797b43bc7fe3844241fdf40230b1d25a901ab9f33f`

The preserved **Dominions 6 Modding Manual, version 6.34**, is 65 PDF pages and has this fingerprint:

`5ac40698e05703f5628db123548c4e6a57fe0ed9bbcb65fb8f72fc589ab309ab`

The official **Event Modding Manual, version 6.29**, remains relevant for event timing, requirements, event chains, and mod-added monthly effects.

### Frozen modded baseline

The working modded library uses:

1. `DomEnhanced2_16.dm` - Dominions Enhanced 2.16.
2. `Divinitus_1.15.3_DE.dm` - Divinitus 1.15.3 DE edition.

Dominions Enhanced is loaded first and Divinitus second.

Neither supplied file declares `#domversion`, so neither states a minimum compatible game version. Their source can be analysed exactly. Complete compatibility with Dominions 6.36 still needs to be tested and cannot be assumed.

### Ruleset labels

Every future article must display one of the following labels.

| Label | Meaning |
| --- | --- |
| **Unmodded 6.36** | The public base game as of 25 August 2026 |
| **DE 2.16** | Dominions Enhanced 2.16 without Divinitus |
| **Divinitus 1.15.3 DE** | The supplied Divinitus DE file considered by itself |
| **DE 2.16 + Divinitus 1.15.3 DE** | The exact two-file ruleset in the recorded load order |
| **Historical** | Material retained from an older game or mod version |
| **Experimental** | A proposed mechanic, test mod, or result not yet part of a published ruleset |

The label applies to the whole article unless a subsection explicitly overrides it.

## Evidence and confidence

### The five evidence labels

| Label | Meaning | Suitable public wording |
| --- | --- | --- |
| **Official** | Directly stated by Illwinter or visible in current in-game data | State as a rule and cite the source |
| **Source-confirmed** | Directly encoded in the exact relevant mod source | State as a rule for that mod version |
| **Reproduced** | Repeated in a documented controlled test | State with the tested setup and result |
| **Community-tested** | Supported by a detailed outside investigation but not yet reproduced here | Attribute and preserve the test conditions |
| **Unverified** | Plausible, incomplete, contradictory, historical, or unsupported | Present only as an open question or hypothesis |

### Evidence priority

The evidence ledger uses the following general hierarchy:

1. Current in-game result or exported current game data.
2. Current Illwinter manual or official change note.
3. Exact mod source for the named version and load order.
4. Reproducible controlled test.
5. Maintainer explanation.
6. Detailed community test or tournament account.
7. General guide, video, forum advice, or historical conversation.

The manual does not contain every rule. It is authoritative where it is explicit, while implementation details, targeting decisions, hidden limits, and unusual interactions may still need testing. If an official statement disagrees with repeatable current-game behaviour, both sides of the discrepancy must be recorded.

### Fact, consequence, recommendation

Three different kinds of statement must not be blended together.

- **Fact:** the hosting sequence resolves recruitment at step 3.
- **Consequence:** recruited units exist before movement battles at step 26.
- **Recommendation:** recruiting emergency defenders may save a province that is attacked during the same hosting cycle.

The first statement is an official rule. The second is a direct timing consequence. The third is strategic advice whose value depends on gold, recruitment capacity, the attacking force, and whether the province can recruit an effective defence.

## Citation standard

Every finished chapter should include:

- ruleset and version;
- last verified date;
- primary source;
- manual page or relevant source location;
- evidence label;
- mod-file hash where applicable;
- test record for reproduced claims;
- unresolved questions.

The public TheHoboKingdom edition can keep citations compact. The private research edition retains full fingerprints, links, source extracts, and test conditions.

## Core notation

### Magic paths

| Symbol | Path |
| --- | --- |
| **F** | Fire |
| **A** | Air |
| **W** | Water |
| **E** | Earth |
| **S** | Astral |
| **D** | Death |
| **N** | Nature |
| **G** | Glamour |
| **B** | Blood |
| **H** | Holy or priest level |

Path level follows the symbol. `S3` means Astral 3. `F2A1` means Fire 2 and Air 1. A requirement written as `S5E3` requires both Astral 5 and Earth 3 unless stated otherwise.

The letter `G` is reserved for Glamour. Gems are written in words or with their path, such as `15 fire gems` or `15F gems`, when the context cannot be mistaken for a path level.

### Research schools

| Short form | School |
| --- | --- |
| **Conj** | Conjuration |
| **Alt** | Alteration |
| **Evo** | Evocation |
| **Const** | Construction |
| **Ench** | Enchantment |
| **Thaum** | Thaumaturgy |
| **Blood** | Blood Magic |
| **Divine** | Divine spell list rather than an ordinary research school |

`Alt 5` means Alteration level 5. `Thaum 9, S5E3` means a Thaumaturgy 9 spell requiring Astral 5 and Earth 3.

### Common statistics

| Symbol | Meaning |
| --- | --- |
| **HP** | Hit points |
| **STR** | Strength |
| **ATT** | Attack skill |
| **DEF** | Defence skill |
| **PROT** | Protection |
| **MR** | Magic Resistance |
| **MOR** | Morale |
| **PREC** | Precision |
| **ENC** | Encumbrance |
| **AP** | Armour-piercing |
| **AN** | Armour-negating |
| **AoE** | Area of effect |
| **PD** | Province Defence |
| **RP** | Research points or recruitment points; the full term must be written when ambiguous |

### Randomness

`DRN` means the Dominions Random Number roll. Dominions commonly uses an open-ended roll built from two six-sided dice, with more rolls after high results. The later mathematics material deals with the full probability system. Here, `attribute + DRN` means the visible attribute does not decide the final result by itself.

Chance statements must distinguish:

- a fixed percentage;
- a percentage per path or priest level;
- a percentage per dominion candle;
- a chance checked once per unit;
- a chance checked once per province;
- a chance checked once per turn;
- an open-ended opposed roll.

### Time

Dominions commonly uses **turn**, **month**, and **hosting** for closely related ideas.

- A **turn** is the set of orders submitted by all players and the resulting game state.
- A **month** is the in-world time represented by one turn.
- **Hosting** is the process that resolves all submitted orders.
- A **battle round** is a tactical interval inside a battle and must not be confused with a strategic turn.

### Spatial terms

- **Province:** a territory on the strategic map.
- **Location:** a distinct place within a province, such as the open province or the interior of a fortress.
- **Adjacent:** connected by a valid province border or other relevant link.
- **Plane:** a separate strategic layer such as the main world, cave plane, or Nexus/Void plane.
- **Square:** a tactical grid space on a battlefield.
- **Size point:** part of the capacity used by units occupying a battlefield square.

## Essential glossary

### Army

A group of commanders and their assigned troops. The word is convenient but not always a single rules object: different commanders in the same province may have different orders and may fail, move, or fight separately.

### Battle magic

Spells cast during tactical combat. Battle magic is governed by scripting, fatigue, range, targeting, battlefield conditions, and the spellcasting AI.

### Bless

The set of effects granted to blessed sacred units and commanders. Some bless effects are always available when the unit is blessed; Incarnate effects generally depend on the Pretender being active.

### Capital-only

A recruitment or availability restriction tied to the nation's original capital. Conquering another nation's capital does not normally convert its capital-only roster into the conqueror's roster.

### Commander

A unit capable of receiving strategic orders and leading troops. Leadership type and capacity determine which troops can be assigned and what morale effects may apply.

### Communion

A magical network in which masters receive path bonuses and slaves absorb distributed spell fatigue and certain master-cast personal buffs. The exact mechanics belong in the magic volume.

### Dominion

The religious influence of a Pretender, shown as candles in provinces. Dominion is both territorial pressure and a carrier for scales, bless conditions, Pretender hit-point modification, special national effects, and elimination.

### Event

A hosting-time occurrence selected from event rules. Events may depend on scales, dominion, population, terrain, commanders, sites, orders, globals, variables, and many other conditions. Modded events can form chains and can imitate systems that the ordinary interface does not expose.

### Fort

A fortified location within a province. A besieging force may control the province while the defender retains the fort, creating partial ownership.

### Gem

A magical resource associated with Fire, Air, Water, Earth, Astral, Death, Nature, or Glamour. Blood slaves fill a similar strategic role for Blood magic but are units/resources with distinct rules.

### Global enchantment

A ritual whose ongoing effect applies broadly to the world or to a large strategic system. Casting occurs during the ritual step, while the continuing world effect is processed later in the hosting sequence.

### Host

As a verb, to resolve submitted turns. As a noun, the computer or service processing a multiplayer game.

### Laboratory

The infrastructure required for research, most forging, and most ritual casting. A new laboratory is completed late in the turn, after that month's research and ritual steps have already passed.

### Magic phase

Community shorthand for the early part of hosting in which rituals, magical movement, remote attacks, and resulting battles occur before ordinary movement. It is useful shorthand, but the official sequence divides it into several distinct steps.

### Magic Resistance

A defence statistic used by many spells and supernatural effects. An MR check is not automatically a simple percentage; it may involve opposed DRN rolls, penetration bonuses, and path-based modifiers.

### Mage

A commander with one or more magic paths or another ability that permits research, ritual casting, forging, or battle magic. Not every researcher is a conventional mage, and not every mage can perform every magical order.

### Mod

A `.dm`-based modification loaded by the game. A mod can add or alter many data objects but cannot necessarily rewrite executable-level systems.

### Movement phase

Community shorthand for the part of hosting in which conventional map movement resolves. The official sequence distinguishes friendly movement, other movement, movement battles, and castle storming.

### Path

A level of magical skill in Fire, Air, Water, Earth, Astral, Death, Nature, Glamour, Blood, or Holy magic. Paths determine spell access, research value, item access, and many special interactions.

### Pretender

The god designed for a nation or team. The Pretender supplies dominion, scales, bless design, magic access, and a physical chassis that may be awake, dormant, or imprisoned.

### Province Defence

Locally purchased defence that appears automatically when a province is attacked. It is not a standing army that can move. Its composition and commander structure depend on the nation and investment.

### Recruitment point

A local capacity used when recruiting units. It is distinct from gold and resources, and it can prevent recruitment even when the other costs are affordable.

### Research point

A contribution toward a school of magical research. Research is processed very early during hosting, before assassinations and most forms of death.

### Ritual

A strategic spell ordered outside battle. Rituals can summon units, alter provinces, move commanders, attack remotely, create globals, search, scry, or cause other world-map effects.

### Rout

The state in which a unit or squad attempts to flee battle. Dominions battles are normally decided by morale collapse rather than the literal death of every unit.

### Sacred

A unit capable of receiving a blessing and often subject to recruitment or upkeep advantages. Sacred does not mean permanently blessed; a blessing still needs to be active.

### Scale

One side of the dominion-scale pairs: Order/Turmoil, Production/Sloth, Heat/Cold, Growth/Death, Fortune/Misfortune, and Magic/Drain. Scales affect the world through dominion and can also interact with units, events, sites, and spells.

### Site

A magical or special feature located in a province. Sites may provide gems, gold, recruitment, unrest, disease, discounts, ritual access, or other effects. Some are hidden until found.

### Squad

A tactical group assigned to a commander. Morale, formation, scripting, and leadership penalties are often evaluated at squad level rather than across the entire army.

### Throne of Ascension

A special site that can be claimed by an appropriate priest. Claimed Thrones provide Ascension Points and may grant other effects. The game can end when the configured Ascension requirement is met.

### Unrest

A province condition that reduces effective administration and income and interacts with events, recruitment, patrolling, pillaging, and Blood Hunting.

### Upkeep

The recurring gold cost of maintaining units and commanders. Upkeep is paid after income is collected in the official hosting sequence.

## The central idea: orders are simultaneous, resolution is sequential

Players submit orders without watching the other nations' orders resolve. Hosting then processes every nation's orders through a fixed sequence.

This creates three different kinds of time:

1. **Planning time:** all players choose orders from the same pre-host game state.
2. **Resolution time:** the engine processes different kinds of orders in a fixed sequence.
3. **Battle time:** tactical battles resolve internally after their triggering strategic step.

Players submit their decisions simultaneously, but the engine resolves them in sequence.

This distinction explains many apparently contradictory outcomes:

- a mage contributes research before being assassinated;
- units are recruited before an attacking army arrives;
- a remote attack can strike an army before ordinary movement;
- a new laboratory finishes too late to support research or rituals that month;
- starvation is applied after battles;
- income is collected before upkeep;
- general dominion spread happens after most battles;
- an immortal can be due to return after the victory check has already ended the game.

## A six-phase model of hosting

The official manual lists 63 separate steps. For practical reading, those steps can be grouped into six phases. These phase names are editorial tools; the numbered order remains the authority.

| Phase | Steps | Main contents |
| --- | ---: | --- |
| **I. Commitments and production** | 1-9 | Messages, research, recruitment, empowerment, forging, preaching, Thrones, quick orders |
| **II. Magic and special threats** | 10-23 | Rituals, remote attacks, magic battles, searching, awakening, Blood Hunting, Horrors, assassinations |
| **III. Movement and conquest** | 24-27 | Friendly movement, other movement, field battles, castle storming |
| **IV. World effects and hidden conflict** | 28-33 | Global effects, random events, item/monster effects, event battles, sneak discovery |
| **V. State, economy, and dominion** | 34-45 | Besiegers, construction, special orders, pillage, income, unrest, starvation, upkeep, dominion, sites |
| **VI. Attrition and end-state** | 46-63 | Aging, disease, insanity, mercenaries, heroes, elimination, victory, immortality, aftermath |

The six-phase model is useful for memory. It must not replace the full sequence when exact timing matters.

## The complete 63-step hosting sequence

**Evidence:** Official.  
**Primary source:** Dominions 6 Manual, revision 2, pages 55-57.  
**Verified:** 25 August 2026.

The following table paraphrases the official sequence and adds timing consequences. The step names and order follow the manual; the explanations are written for this library.

| Step | Resolution | What happens | Why the timing matters |
| ---: | --- | --- | --- |
| 1 | Send messages | Diplomatic messages and attached gold, gems, or items are dispatched. | Transfers occur before events that could kill a courier, capture a province, or remove a commander. The manual states that the early timing makes sent resources reliable. |
| 2 | Research | Assigned researchers contribute research points. | A researcher killed later in the same hosting cycle still contributes for that month. |
| 3 | Recruitment | Paid troops and commanders are created. | New defenders exist before movement battles. They cannot receive new orders during the hosting cycle in which they appear. |
| 4 | Empowerment | Ordered permanent path increases are applied. | The path exists before forging and ritual steps, although the empowering commander cannot also perform a second ordinary order that month. |
| 5 | Forge items | Completed items enter the nation's magic-item inventory. | Forging occurs before rituals, but an item in the treasury is not the same as an item already equipped by a caster. |
| 6 | Preach | Priests resolve ordinary preaching and adjust dominion. | Preaching can alter dominion before movement battles, unlike general dominion spread at step 42. |
| 7 | Heretic preaching | Heretics, insane commanders, and shattered-soul commanders apply their religious influence. | These changes also occur before movement and most battles. |
| 8 | Claim Thrones | Eligible priests claim Thrones of Ascension. | A claim is processed before rituals and battles that might remove the claimant later in the month. |
| 9 | Quick special orders | Fast special orders such as entering a site to scry or cultivating pearls resolve. | These orders precede the main ritual step; their precise value depends on the named order. |
| 10 | Magic rituals | Ritual casters perform their rituals in random caster order. | Competing or interacting rituals cannot be assumed to follow nation number, player order, or script order. |
| 11 | Remote attacks | Rituals that strike hostile armies in remote provinces are applied. | An army can be damaged before it performs ordinary movement. |
| 12 | Magic battles | Battles created by magic resolve, including hostile teleportation and certain movement rituals. | Magical movement can fight before conventional armies move. Retreats from the group of magic battles are placed after all such battles finish. |
| 13 | Lost in other planes | Units become lost in other planes and relevant other-plane battles resolve. | Planar displacement is settled before site searching, ordinary movement, and field battles. |
| 14 | Site searches | Magical site-search orders resolve. | A commander can search a province before conventional movement changes the province later in hosting. |
| 15 | Prophets | New prophets are declared. | The prophet exists before Call God, awakening, Blood Hunting, assassinations, and ordinary battles, but after ritual and magic-battle steps. |
| 16 | Call God | Priests assigned to Call God contribute to returning a banished Pretender. | The recall attempt occurs before ordinary battles can kill those priests that month. |
| 17 | Awakening | Dormant or imprisoned Pretenders that are due to awaken enter play. | A newly awakened Pretender exists before ordinary movement battles but received no normal order from the prior map state. |
| 18 | Blood hunting | Blood Hunt orders resolve and slaves are collected according to the Blood Hunting rules. | Blood hunters are exposed to the results before assassinations and conventional movement. |
| 19 | Horrors | Units due to be visited by Horrors are attacked or affected. | Horror attacks can remove a commander before assassination and movement steps. |
| 20 | Assassinations | Assassination, seduction, corruption, and similar attempts resolve immediately. | Killing a commander here can prevent that commander's army from moving later. The research contribution at step 2 has already been secured. |
| 21 | Relinquish province | A province may be transferred to a qualifying non-stealthed ally already present. | Transfer happens before movement, so an ally arriving later in the turn does not satisfy the presence requirement for this order. |
| 22 | Claim mounts | Riders without mounts attempt to obtain suitable mounts. | Mount status is updated before ordinary movement and battles. |
| 23 | Lone mounts | Riderless intelligent mounts or mountless riders may return home or disperse. | Mount cleanup occurs before movement, preventing stale mount states from persisting into field battles. |
| 24 | Friendly movement | Movement ending in a friendly province resolves. | Reinforcement of an already friendly destination receives priority over hostile arrivals unless an earlier effect intervenes. |
| 25 | Other movement | Remaining conventional movement resolves, including Break Siege. | Hostile movement and movements that change control are processed after friendly movement. |
| 26 | Resolve battles | Field battles caused by conventional movement are fought. | Province control established here can affect storming, pillage, income, ownership, and later events. |
| 27 | Castle storming | Storm Castle battles resolve. | Storming occurs after movement battles. Retreats from the movement and storming groups are placed only after the relevant battles finish. |
| 28 | Global enchantments | Ongoing global enchantment effects are applied to the world. | A global is cast at step 10, but its continuing world effect begins here, after movement and castle-storming battles for the month. |
| 29 | Random events | Ordinary Fortune, Misfortune, and other eligible random events occur. | These events see the world state produced by magic, movement, battles, storming, and global effects. |
| 30 | Resolve battles | Battles created by random events are fought. | Event-created attackers do not fight during the earlier movement battle step. |
| 31 | Magic item and monster effects | Special monthly effects generated by items or monsters occur. | Items were forged at step 5, while special monthly effects are delayed until this stage. Item-assisted rituals still belong to step 10. |
| 32 | Resolve battles | Battles created by the preceding special effects are fought. | These battles form a separate retreat group after random-event battles. |
| 33 | Sneak discovery | Detected stealthy units fight for survival. | A stealth force can avoid the ordinary movement battle and still be discovered and attacked later. |
| 34 | Change besieger | When allied forces share a siege, the game determines which ally is the active besieger, favouring the larger force. | Siege ownership and control are settled after field, storming, event, and sneak-discovery battles. |
| 35 | Building construction | Forts, temples, and laboratories finish construction or demolition; fort melting also occurs. | New infrastructure is too late for this month's recruitment, research, forging, rituals, preaching, or movement. It becomes useful from the next order phase onward. |
| 36 | Special orders | Orders such as Reanimate and Summon Allies resolve. | The manual explicitly notes that allies created here are too late for this month's battles. |
| 37 | Pillage | Pillaging increases unrest and kills population. | Pillage occurs immediately before income, so the damage can reduce or remove income from a province captured earlier that month. |
| 38 | Income | Nations collect provincial income. | New ownership and pillage have already been resolved. Income arrives before upkeep is charged. |
| 39 | Unrest alterations | Unrest changes from dominion, scales, patrolling, and related systems are applied. | Income was already collected using the earlier state; the new unrest primarily affects the following month. |
| 40 | Starvation | Units without sufficient supplies suffer starvation effects. | Battles are already over. An army newly without supply fights this month's battles before the new starvation penalties are applied. |
| 41 | Upkeep and desertion | Unit upkeep is charged and desertion occurs. | Income is collected first, so the treasury has this month's income available when upkeep is assessed. |
| 42 | Dominion spread | General dominion spread from temples and other sources resolves. | Most battles have already occurred. New candles from ordinary spread do not retroactively alter those battles. |
| 43 | Dominion effects | Population loss, insanity pressure, temperature movement, and other special dominion effects are applied. | Dominion first spreads, then its special world effects are calculated from the resulting state. |
| 44 | Site effects | Sites generate disease, unrest, or other monthly effects. | Site effects happen after income, upkeep, and dominion effects but before healing and disease resolution. |
| 45 | Overpopulation | If global unit or commander limits are approached, the game removes some common entities. | This is an emergency engine-maintenance step rather than ordinary strategic attrition. |
| 46 | Aging | In midwinter, units age and may acquire age-related afflictions such as disease. | Aging is seasonal and occurs before the healing/disease step. |
| 47 | Resolve battles | Remaining battles generated by previous effects are fought. | Late world effects can create battles after normal movement, event, and sneak battles. |
| 48 | Heal and disease | Units heal lost hit points; diseased units instead suffer disease damage and may gain afflictions. | A surviving unit may recover after all ordinary battles, while disease can turn survival into a later death. |
| 49 | Insanity | Eligible units may become insane. | Insanity for the next order phase is determined after battles and healing. |
| 50 | Mercenaries | Mercenary bids, purchases, and continued contracts are resolved. | Mercenary availability is decided after income, upkeep, disease, and insanity. |
| 51 | New random heroes | Eligible national heroes may appear at the capital. | A new hero arrives after all battles and cannot act during the month of arrival. |
| 52 | Kill lone units | Non-commanders stranded in enemy territory without a commander are removed. | Troops left behind by commander death or separation cannot persist indefinitely as an uncontrolled hostile stack. |
| 53 | Reclaim provinces | A fort can restore province ownership to its owner or allied team under the stated conditions. | Partial ownership can be corrected late in hosting if the fort is not under siege. |
| 54 | Conscription | Province Defence is raised to at least one where applicable, and dominion or commander effects that add PD resolve. | Automatic PD appears after battles and therefore protects future turns, not the battle that caused the ownership change. |
| 55 | Scouting | Fresh scouting reports are generated. | Reports show the end-of-hosting state rather than the exact state seen during earlier movement or battles. |
| 56 | Elimination | Nations meeting elimination conditions are removed. | Elimination is checked after dominion spread and effects, but before the victory check and before immortals reform. |
| 57 | Victory | Configured victory conditions are checked and the game may end. | Later administrative steps cannot rescue a position once victory has been declared. |
| 58 | Update stats | Hall of Fame and scoregraph information is updated. | Public statistics reflect the completed turn after victory evaluation. |
| 59 | Heroic abilities | Eligible units gain or improve heroic abilities. | A unit's new heroic benefit is normally available from the following turn. |
| 60 | Reform Immortals | Immortals due to return reform their bodies. | The victory check has already occurred. An imminent immortal return cannot prevent a game that ended at step 57. |
| 61 | Reduce PD | Province Defence is reduced where population cannot support it; the manual gives a requirement of at least 10 population per PD point. | Unsustainable PD can disappear after the victory and scouting checks, altering the next turn's defence. |
| 62 | Yearning artifacts | Artifacts that newly become yearning change state. | Artifact yearning is an end-of-turn transition rather than an effect applied during forging or battle. |
| 63 | Aftermath | The engine validates orders and items, applies necessary shape changes, and performs final cleanup. | The next player turn opens only after these consistency checks and state transitions finish. |

## Phase I: commitments and production

### Messages resolve before danger

Messages and attached resources are dispatched at step 1. The rule has an important diplomatic consequence: a trade agreed during the order phase is not interrupted because the sending capital is captured or the supposed courier dies later in hosting.

This makes the act of sending reliable. It does not make the agreement honest. A player can still send less than promised, send the wrong item, or accept payment while making hostile orders.

**New-player rule:** Resource transfers are processed before almost anything can interfere.

**Expert consequence:** A nation expecting to be eliminated can still transfer resources before the elimination check. Multiplayer rules may need to address kingmaking or last-turn treasury transfers explicitly.

### Research is secured early

Research occurs at step 2. The official manual explicitly states that a researcher killed or assassinated later in the turn still contributes that month's research.

This timing separates **research production** from **researcher survival**:

- the current month's points are earned;
- the researcher may still be lost before the next order phase;
- research enabled at step 2 may make new spells available for later battles in the same hosting cycle, subject to casting orders already submitted and the game's handling of scripted availability.

The last point requires care. A script submitted before hosting cannot safely be assumed to select a spell that was unavailable when orders were written. Research can complete early, but practical same-turn spell use depends on scripting and spell-selection behaviour. That interaction belongs in the magic test suite.

### Recruitment occurs before invasion

Recruitment resolves at step 3. Units paid for in the preceding order phase exist before magic attacks, assassinations, ordinary movement, field battles, and storming.

Practical consequences:

- emergency recruits can defend a province attacked that month;
- newly recruited commanders can be present as battlefield commanders;
- new units cannot receive a new strategic order until the following player turn;
- a province captured later does not cancel recruitment already completed;
- a recruitment queue still depends on the gold, resources, recruitment points, and local eligibility checked by the game.

Recruitment timing is one reason a projected attack cannot rely solely on last turn's scouting report. A fort or capital can add another month of defenders before the attack lands.

### Empowerment and forging are separate commitments

Empowerment resolves at step 4 and forging at step 5. The sequence does not normally let one commander empower and forge in the same month because both require the commander's order. It does establish that permanent path changes exist before later systems inspect the commander.

A newly forged item enters the national item inventory. It is not automatically equipped by a commander whose orders were already submitted. If a battle or ritual needs a booster, the commander must have it equipped before hosting. Forging it during that hosting is too late.

### Preaching is not ordinary dominion spread

Ordinary preaching resolves at step 6 and heretic preaching at step 7. General dominion spread waits until step 42.

This is strategically significant:

- successful preaching can change dominion before battles;
- general temple spread cannot change earlier battle conditions that month;
- heretic and insanity-related religious effects are also early;
- blood sacrifice is a different special order and should not be silently treated as ordinary preaching.

Dominion-dependent hit points, morale, scales, sacred effects, and special national mechanics make this distinction worth testing in controlled battles.

### Throne claims are early

Thrones are claimed at step 8, long before the victory check at step 57. A priest who successfully performs the order can establish the claim even if later killed.

The claim does not cause an immediate mid-sequence victory. The remaining hosting steps still resolve before victory is checked.

This creates a dangerous endgame pattern:

1. a Throne is claimed at step 8;
2. the claimant may lose battles or territory later;
3. the game evaluates the configured victory condition at step 57.

Book III resolves the ownership branch at an Official plus Community-tested tier. Killing the claimant after step 8 does not undo the claim. Conquering an unfortified Throne, or storming and conquering the fort that contains one, makes it unclaimed before step 57 and removes its points from the winning total. Merely besieging a fortified Throne does not conquer the fort or unclaim the Throne. Book III retains the evidence and complete state matrix; this chapter owns only the shared turn order.

## Phase II: magic and special threats

### Rituals have random caster order

All ritual casters resolve at step 10 in random order. This is one of the most important expert-level timing rules.

When two rituals interact, no plan should depend on one particular mage resolving first unless the game provides a separate explicit priority. Examples include:

- two commanders attempting to affect the same unique target;
- competing globals;
- rituals that move, kill, transform, or empower a target;
- rituals that alter a province before another ritual checks it;
- ritual combinations that depend on gem availability or a surviving caster.

Random caster order means that a multi-ritual plan should be robust in every plausible order or should be tested to determine whether the particular rituals belong to separate substeps.

> **Expert rule:** "Both happen during the magic phase" does not mean "they happen simultaneously." It often means "the engine resolves them one at a time in an order the player cannot choose."

### Casting a global and receiving its world effect are different steps

A global enchantment is cast during rituals at step 10. The global's continuing world effect is applied at step 28.

This division creates a clear dependency:

- the global can be established before ordinary movement;
- its normal world-processing stage occurs after movement battles and castle storming;
- the spell's immediate casting effect, if any, must be distinguished from its later monthly effect;
- losing a province or caster after step 10 may or may not end a province-centred global before step 28, depending on that global's rules.

Every global guide should record:

1. casting requirements;
2. immediate casting result;
3. ongoing effect step;
4. dispel rules;
5. termination condition;
6. whether it is centred on a province, caster, site, or global slot.

### Remote attacks strike before ordinary movement

Remote army attacks resolve at step 11. A conventional army ordered to leave the targeted province has not yet performed ordinary movement.

This creates several practical uses:

- damage a stack before it marches;
- kill or disable a commander and strand troops;
- force attrition before a later conventional attack;
- attack a force whose destination is uncertain while it is still at its starting location.

There is one important qualification. A commander may leave or arrive through magical movement at step 10, and magic battles occur at step 12. In this context, "before movement" needs to mean "before conventional movement."

### Magic battles are their own battle group

Battles created by magic resolve at step 12. This includes examples such as hostile teleportation and units moved by certain rituals.

Retreats are placed after all battles in the group have resolved. That detail matters when multiple magic battles use adjacent provinces or when a retreat destination is itself affected by another magic battle.

"A battle" is too broad to be a safe unit of analysis. The useful sequence is:

- the step that created the battle;
- the battle group to which it belongs;
- the point at which retreats from that group are placed.

### Site searching precedes conventional conquest

Site searches resolve at step 14. A mage searching a province can complete the order before an enemy conventional army arrives.

The newly found site then exists for later steps, but each site benefit has its own timing:

- gem income is not necessarily granted immediately upon discovery;
- a site effect may be processed at step 44;
- recruitment unlocked by the site cannot be ordered retroactively;
- a conqueror may take control of the newly discovered site later in the same turn.

The distinction between **discovering a site** and **receiving every benefit of that site** should be preserved.

### Prophets, recalled gods, and awakening

Prophets are declared at step 15. Call God resolves at step 16. Dormant and imprisoned Pretenders awaken at step 17.

All three occur before ordinary movement and field battles, but after magic battles.

This ordering produces several boundaries:

- a new prophet can defend against a later conventional attack;
- a prophet is not available for an earlier magic battle;
- an awakening Pretender can exist for later defence but generally has no fresh order that month;
- priests calling a god make their contribution before conventional attackers arrive;
- the returned god's exact availability and location must be checked under the Call God rules.

### Blood Hunting is early enough to be dangerous

Blood Hunting occurs at step 18, before assassinations and movement. The hunt can generate slaves and unrest before later state-processing steps.

The full economic consequences require the Blood Hunting chapter, but the timing model already establishes that:

- hunters remain in their starting province while hunting;
- a hunter can be assassinated after contributing to the hunt;
- unrest alterations from the broader turn are processed later;
- newly collected slaves exist before later upkeep and income steps, although their immediate availability for already-submitted rituals should not be assumed without testing.

### Horrors and assassinations can remove movement leaders

Horror visits occur at step 19 and assassinations at step 20. Both can kill a commander before conventional movement.

An army's movement order belongs to a commander. If that commander dies before step 24 or 25, assigned troops may remain behind, become uncommanded, or eventually be removed if stranded in hostile territory.

A resilient army-movement plan considers:

- redundant commanders;
- bodyguards;
- stealth and assassination threats;
- Horror Marks;
- whether critical troops can be reassigned before hosting;
- whether the loss of a single leader invalidates an entire movement chain.

### Relinquishing requires an ally already present

Relinquish Province resolves at step 21. The official description requires the receiving non-stealthed allied commander to already be in the province.

An ally moving into the province at step 24 is too late. A stealthy allied commander does not satisfy the stated condition.

This is a good example of why a plain-language order description is not enough. The order's position in hosting determines which board state it can see.

## Phase III: movement and conquest

### Friendly movement receives its own step

Movement ending in a friendly province resolves at step 24. Other conventional movement resolves at step 25.

The manual explains the practical purpose: a force trying to enter a friendly province before an enemy arrives normally succeeds unless an earlier event prevents it.

This is not a universal guarantee that every reinforcement arrives safely. Earlier dangers include:

- remote attacks;
- magic battles;
- planar loss;
- Horrors;
- assassination;
- failed movement requirements;
- commander death;
- terrain or movement limitations.

It does mean that an ordinary hostile arrival does not normally prevent valid friendly reinforcement from reaching the province first.

### "Other movement" contains several different intentions

Step 25 covers the remaining conventional movements, including Break Siege. It can include:

- invasion of hostile territory;
- movement into independent provinces;
- armies crossing toward a province that changes ownership;
- breaking out of a siege;
- opposing movements that produce a meeting or province battle.

Movement validity depends on the movement rules: map-move allowance, terrain costs, roads, rivers, survival abilities, flying, sailing, planes, army composition, and the slowest or otherwise limiting elements of the force.

Book I records when movement resolves. The movement and logistics material handles the detailed calculation of whether a move is valid.

### Field battles occur after both movement steps

Battles created by conventional movement resolve at step 26. The defender seen in battle may include:

- the pre-existing garrison;
- recruited units from step 3;
- friendly reinforcements from step 24;
- Province Defence;
- commanders or units that did not move;
- magical arrivals from earlier steps, if they survived;
- units altered by early effects.

It may exclude:

- conventional reinforcements whose movement failed;
- commanders killed by Horrors or assassinations;
- allies summoned later at step 36;
- infrastructure completed later at step 35;
- dominion changes that wait for step 42.

### Castle storming is later than field battle

Castle storming resolves at step 27. A storming force must survive the month's preceding events and battles before entering the assault.

This ordering matters when:

- a relief army arrives;
- the besiegers fight a field battle;
- an army attempts to break siege;
- assassinations remove storm leaders;
- remote attacks weaken the besiegers;
- multiple allied forces are involved.

Storming is a separate battle step, resolved later than movement battles and governed by its own deployment, wall, gate, and defender rules.

### Retreats belong to battle groups

The manual repeatedly notes that retreats to adjacent provinces occur after all battles in a relevant group have resolved.

This prevents an oversimplified model in which a routed army immediately appears in a neighbouring province while other same-step battles are still being processed.

For expert analysis, a retreat question should record:

- which step caused the battle;
- which other battles shared the step;
- candidate retreat provinces at the time retreats are placed;
- control and hostile forces in those provinces;
- whether the unit was inside or outside a fort;
- whether the route crossed planes or special connections.

## Phase IV: world effects and hidden conflict

### Global effects are late relative to conquest

Ongoing global enchantment effects resolve at step 28, after conventional movement and castle storming.

This means a global cast at step 10 may be visible and active as an enchantment before its normal monthly world effect is processed. If the effect depends on a province, site, caster, or global state that can be lost during movement, the exact spell wording and tests become important.

No global should be described merely as "going off in the magic phase." Its casting and its world tick may be separated by most of the month's major battles.

### Random events see a heavily updated world

Random events occur at step 29. By then, the game has already processed:

- research and recruitment;
- preaching and Throne claims;
- rituals and magical attacks;
- assassinations;
- conventional movement;
- field battles and storming;
- global world effects.

Events can react to a state that did not exist when orders were submitted.

The Event Modding Manual confirms that events can test a wide range of conditions, including:

- era and turn;
- season and month;
- nation;
- treasury and gems;
- research;
- population;
- unrest and PD;
- buildings;
- terrain and plane;
- sites and Thrones;
- dominion and scales;
- particular monsters, Pretenders, priests, mages, and orders;
- global enchantments;
- event codes and variables.

This is why event systems can simulate diplomacy, doctrine, religious activity, or evolving stories without directly rewriting the strategic AI.

### Event battles resolve separately

Battles created by random events occur at step 30. A nation can win its movement battle and then face a later event battle in the same province.

Reports should be read in timing order. Two battles in one province during the same month may be caused by different systems and may see different surviving forces.

### Item and monster effects have a separate monthly tick

Monthly effects from magic items and monsters resolve at step 31, followed by any battles they cause at step 32.

The manual distinguishes:

- item forging at step 5;
- item-assisted ritual casting at step 10;
- special monthly item or monster effects at step 31.

This prevents a common category error in which every effect attached to an item is assumed to occur when the item is forged or when rituals resolve.

### Stealth failure can produce a late battle

Sneak discovery occurs at step 33. A stealthy force may avoid conventional combat because it remained undiscovered, then be exposed and forced to fight later.

Stealth changes what triggers combat. It does not make a force immune to hostile troops.

Expert stealth analysis should distinguish:

- successful sneaking movement;
- patrol detection;
- event-based detection;
- Glamour visibility;
- assassination or spy actions;
- late sneak-discovery battles;
- retreat and survival after discovery.

## Phase V: state, economy, and dominion

### Allied siege leadership is determined after combat

At step 34, the game selects the active besieger when allied armies share a siege. Larger armies take precedence according to the manual.

This decision occurs after the major battle groups. Losses suffered earlier in the month can change which ally counts as the besieger.

### Buildings finish after the month's active systems

Construction and demolition occur at step 35.

A building ordered this month is too late to support:

- step 2 research;
- step 3 recruitment;
- step 5 forging;
- step 6 preaching requirements where a temple matters;
- step 10 ritual casting;
- step 14 site-search orders;
- earlier battles.

The completed structure is principally an investment in the following turn.

This is the first major principle of infrastructure timing:

> **A building consumes resources in the present to unlock actions in the future.**

The economy volume will extend this into fort construction time, administration, recruitment access, laboratory networks, temple spread, and opportunity cost.

### Special-order summons arrive after battle

Special orders such as Reanimate and Summon Allies occur at step 36. The manual explicitly states that allies summoned here do not participate in this month's battles.

This differs from:

- recruitment at step 3;
- ritual summons at step 10;
- event-created units at their event step;
- units arriving through movement.

When a unit appears is as important as how it is created.

### Pillage damages the same month's income

Pillage occurs at step 37, immediately before income at step 38. The official manual explicitly warns that pillaging a newly conquered province can reduce or remove the income collected from it.

This creates a direct trade:

- immediate pillage effects;
- increased unrest;
- population loss;
- reduced current income;
- reduced future economic value;
- possible strategic denial if the province cannot be held.

Pillage should never be evaluated only by its immediate gold or damage result.

### Income precedes upkeep

Income is collected at step 38. Upkeep is paid at step 41.

This means the month's provincial income is available before the game assesses unit maintenance. A treasury that appears unable to cover upkeep at the end of the order phase may survive if sufficient income is collected.

Income may already have been altered by:

- conquest;
- pillage;
- ownership;
- unrest existing before step 39;
- population;
- scales and dominion already present;
- sites and other modifiers;
- events or earlier effects.

### Unrest changes after income

The broad unrest-alteration step is 39, after income. Patrolling, dominion, scales, and related changes are reflected here.

This suggests a timing distinction between:

- unrest already present when income is collected;
- unrest created directly by pillage at step 37;
- general unrest alterations processed at step 39.

Each unrest source should be tested against income on its own. One slogan cannot safely describe all of them.

### Starvation follows battle

Starvation is processed at step 40. The manual states that an army newly without supplies fights its battles before starvation effects are applied.

This does not make supply unimportant. Existing starvation penalties and afflictions may already be present. The rule means that the first new month of shortage does not retroactively weaken battles that occurred earlier in that hosting cycle.

For campaign planning, supply is a delayed threat that compounds over time:

1. the army enters or remains in a low-supply situation;
2. it fights before the new starvation tick;
3. starvation is applied afterward;
4. the weakened army enters the next order phase with penalties, disease risk, or afflictions.

### Upkeep and desertion follow income

At step 41, upkeep is charged and desertion occurs.

This timing means conquest and income may fund the army before payment is due. It also means pillage, income loss, or treasury transfers can contribute to a shortfall.

The exact desertion priority and behaviour require a dedicated economy test. A reliable guide should not claim which units desert first without current evidence.

### Dominion spread, then dominion effects

General dominion spread occurs at step 42. Dominion effects follow at step 43.

This produces a clear two-stage model:

1. candles spread or contest one another;
2. special effects of the resulting dominion state are applied.

Possible effects include:

- population loss;
- insanity;
- temperature movement;
- national or Pretender-specific dominion effects;
- event eligibility;
- other mechanics tied to friendly or hostile candles.

Most conventional battles are already over. Preaching at steps 6 and 7 is the major earlier religious exception.

### Sites apply their monthly effects

Magic-site effects occur at step 44. Disease, unrest, and other site-driven changes are applied after dominion effects.

Site-search discovery occurred at step 14. A newly found site may apply an effect later in the same month, although the timing still needs to be checked for the specific site and effect.

## Phase VI: attrition and end-state

### Aging is seasonal

Aging occurs at step 46 and only during midwinter. Units gain a year and may receive age-related afflictions.

The seasonal condition matters when planning:

- old mages;
- rejuvenation or age modification;
- disease management;
- transformation;
- long campaigns;
- effects that trigger at a particular month.

The Event Modding Manual identifies month 10 as midwinter in its month numbering, but a full calendar reference should be verified in the dedicated time-and-seasons appendix.

### Healing and disease share a late step

At step 48, ordinary units regain lost hit points while diseased units instead suffer disease damage and may gain more afflictions.

This occurs after ordinary battles, global effects, events, item effects, site effects, aging, and any late battles.

Surviving the battle report does not always mean surviving until the next player turn.

### Insanity is determined after healing

Insanity changes occur at step 49. An affected unit enters the next order phase with the resulting behaviour or lost control.

Insanity also appears in earlier steps, including heretic preaching at step 7. It is not confined to one moment in the turn. The step 49 check establishes or changes the condition that will affect later orders.

### Mercenaries and heroes arrive too late to act

Mercenary resolution occurs at step 50 and new random heroes at step 51.

Neither can receive an order or join an earlier battle during the month of arrival. They become assets for the following order phase.

### Lone troops are cleaned up

At step 52, non-commanders left alone in enemy territory are removed.

This can be the delayed consequence of:

- assassination;
- commander death in an earlier battle;
- failed or split movement;
- a commander retreating separately;
- ownership changes;
- units being created without a valid leader.

The lesson goes beyond the cleanup rule. Commander redundancy protects logistics as well as morale.

### End-of-turn ownership can still change

At step 53, a fort can reclaim province ownership under the conditions stated in the manual, including the absence of an active siege.

This reflects the distinction between:

- ownership of the open province;
- ownership of the fortress;
- partial ownership;
- full ownership.

Any guide to events, income, recruitment, or province transfer that says only "owner" must specify which kind of ownership the rule requires.

### Conscription is for the next attack

At step 54, Province Defence can be raised to a minimum and PD-adding dominion or commander effects occur.

This is after every ordinary battle. The new defence cannot save the province from the attack that caused its creation or transfer.

### Scouting reports are end-state reports

Scouting updates at step 55. A report is a view of the state after most monthly transformations, not a recording of every force that passed through the province.

This explains why scouting can omit:

- an army that moved onward;
- units killed in an earlier battle;
- a stealth force not discovered;
- a temporary magical arrival;
- infrastructure or ownership that changed again later.

Intelligence should be dated and treated as a snapshot.

### Elimination precedes victory

Elimination is checked at step 56 and victory at step 57.

Dominion spread and effects have already resolved, so a dominion collapse can matter immediately. Immortal return is still three steps away at step 60.

The sequence prevents a player from assuming that a future recovery effect will be processed before the game decides whether the nation or game has ended.

### Heroic abilities and immortality are post-victory

Statistics update at step 58, heroic abilities at step 59, and immortal reformation at step 60.

These are transitions into the next turn unless the game has already ended.

### Province Defence can be reduced after reports

At step 61, PD is reduced if population cannot support it. The manual states that at least 10 population is required for each PD point.

Because scouting updates at step 55, an edge case exists: the displayed or reported value may need to be checked against the final post-reduction state. The user interface behaviour should be verified in a controlled test.

### Aftermath closes the turn

Artifact yearning occurs at step 62. Final validation, item checks, and shape changes occur at step 63.

Aftermath is a reminder that not every visible state transition has a named strategic order. Shape-changing units, invalid item states, and other cleanup may be corrected only at the end.

## Timing chains every player should know

### Researcher assassination

| Order | Event |
| ---: | --- |
| 2 | The mage contributes research |
| 20 | The assassination attempt occurs |
| 48 | If wounded and surviving, healing or disease is processed |
| Next turn | The nation keeps the research but may have lost the mage |

**Conclusion:** Assassination disrupts future research, not the research already produced that month.

### Emergency recruitment against invasion

| Order | Event |
| ---: | --- |
| 3 | Recruits are created |
| 24 | Friendly reinforcements may arrive |
| 25 | The hostile army moves |
| 26 | The field battle includes eligible new defenders |

**Conclusion:** Recruitment and friendly reinforcement can both increase a defence beyond what the attacker saw in the preceding scout report.

### Commander assassination strands an army

| Order | Event |
| ---: | --- |
| 20 | The movement commander is assassinated |
| 24-25 | The dead commander cannot complete conventional movement |
| 52 | Troops left alone in hostile territory may be removed |

**Conclusion:** A cheap assassination can have a strategic effect much larger than the commander's personal value.

### Remote attack before a march

| Order | Event |
| ---: | --- |
| 10 | The attacking ritual is cast |
| 11 | Its remote strike hits the army |
| 25 | The surviving conventional army attempts movement |
| 26 | It fights any resulting field battle |

**Conclusion:** Remote attacks can soften, disorganise, or decapitate an army before its conventional operation.

### Teleportation and conventional invasion

| Order | Event |
| ---: | --- |
| 10 | Magical movement ritual resolves |
| 12 | Any resulting magic battle is fought |
| 24-25 | Conventional armies move |
| 26 | Conventional movement battles occur |

**Conclusion:** A teleporting force cannot be treated as arriving at the same moment as a marching army. The magical force may fight alone first.

### Constructing a laboratory

| Order | Event |
| ---: | --- |
| 2 | Research occurs without the unfinished laboratory |
| 5 | Forging occurs without it |
| 10 | Rituals occur without it |
| 35 | The laboratory finishes |
| Next turn | Eligible commanders can use the laboratory |

**Conclusion:** A laboratory order is an investment in next month's magic, not a way to enable this month's rituals.

### Pillage after conquest

| Order | Event |
| ---: | --- |
| 25 | Invaders move |
| 26 | They win the province |
| 37 | A valid Pillage order is processed |
| 38 | Income is collected from the damaged province |

**Conclusion:** Pillaging a newly conquered province can sacrifice immediate and future economic value.

### Starvation after combat

| Order | Event |
| ---: | --- |
| 26-33 | Ordinary, event, special-effect, and sneak battles occur |
| 40 | New starvation effects are applied |
| 48 | Healing or disease is processed |
| Next turn | The army begins in its worsened condition |

**Conclusion:** An army can fight at its pre-starvation state and still emerge strategically crippled afterward.

### Dominion before and after battle

| Order | Event |
| ---: | --- |
| 6-7 | Preaching and heretic preaching adjust dominion |
| 26-33 | Most battles occur |
| 42 | General dominion spread occurs |
| 43 | Dominion effects apply |

**Conclusion:** Active preaching can matter before battle. Passive monthly spread generally affects the state after battle.

### Victory before immortal return

| Order | Event |
| ---: | --- |
| 56 | Elimination is checked |
| 57 | Victory is checked |
| 60 | Due immortals reform |

**Conclusion:** A return scheduled for the end of the month cannot undo a game-ending state already recognised at step 57.

## A new player's turn checklist

### Before finalising orders

- Check the treasury after recruitment, construction, forging, and expected transfers.
- Confirm that every army has a commander with the correct normal, magic, or undead leadership.
- Confirm that the slowest movement restriction has not invalidated an army's route.
- Check whether rivers, roads, mountains, forests, swamps, caves, sailing, or planes alter movement.
- Give bodyguards to commanders exposed to assassination.
- Verify that critical mages have the required paths, gems, laboratory, and target.
- Equip boosters before hosting; forging them this turn is too late for the same caster to use them.
- Check whether a ritual target is the starting province or expected destination of an enemy.
- Inspect every fort for recruitment, siege, storm, and repair intentions.
- Confirm that researchers are actually assigned to Research.
- Review starving, diseased, old, insane, or heavily Horror Marked commanders.
- Check dominion and retreat routes around important battles.
- Confirm that a Throne claimant has the required priest level and correct order.
- Recheck diplomacy messages, gold, gems, and items before sending.
- Save or archive the turn file when a test or major operation needs later reconstruction.

### After hosting

- Read messages before changing orders.
- Separate magic battles, movement battles, event battles, and assassination battles.
- Compare recruitment reports with surviving units.
- Check whether movement failed or whether the commander died before movement.
- Inspect new sites, buildings, heroes, mercenaries, globals, and dominion changes.
- Review income, upkeep, unrest, and supply summaries.
- Inspect wounded survivors for disease and new afflictions.
- Check whether stealthy units remained hidden or fought discovery battles.
- Review scouting reports as end-state snapshots.
- Record any result that contradicts the expected hosting sequence.

## Expert operational checklist

For a complex operation, write the dependency chain before submitting orders.

### Target

- What province, fort, army, commander, site, or global must change?
- Which exact end-state counts as success?

### Earliest interference

- Can a message transfer remove required gems or items?
- Can a remote ritual kill or move the target?
- Can a Horror, assassination, or seduction remove a critical commander?

### Magic-phase dependencies

- Which rituals interact?
- Does random ritual order matter?
- Will magical movement fight alone before conventional movement?
- Are retreats from several magic battles competing for the same provinces?

### Movement dependencies

- Is the destination friendly at step 24 or hostile at step 25?
- Could ownership change between planning and movement?
- Is Break Siege involved?
- Is there a valid retreat province after all battles in the group?

### Post-battle dependencies

- Does a global tick at step 28?
- Can a random event or item effect create another battle?
- Will a stealth force face discovery at step 33?
- Does construction finish too late for the intended action?

### Economic dependencies

- Does Pillage reduce the income expected to pay upkeep?
- Is the army supplied before the starvation tick?
- Does income arrive before the planned upkeep obligation?
- Could population loss reduce PD at step 61?

### End-state dependencies

- Can dominion spread eliminate a nation?
- Is victory checked before an expected immortal return?
- Does a hero, mercenary, or summoned ally arrive too late to matter?

## Troubleshooting: why did the order fail?

### "My army did not move"

Check, in order:

1. Was the commander killed by a Horror, assassination, magic battle, or remote effect before movement?
2. Did the commander become lost in another plane?
3. Was the route valid for every unit in the army?
4. Did terrain, a river, road status, sailing, flying, or survival ability change the cost?
5. Did the destination change from friendly to hostile or otherwise alter the movement category?
6. Was the commander performing a different order?
7. Was the army inside a fort, besieging, breaking siege, patrolling, or sneaking?
8. Did part of the army move while incompatible units remained?
9. Was the apparent failure actually movement followed by defeat and retreat?

### "My ritual did not happen"

Check:

1. Did the caster have the required laboratory?
2. Were the path requirements met after all equipped items and effects?
3. Were sufficient gems or slaves available to that caster?
4. Was the target legal and correctly selected?
5. Did the caster receive the ritual order rather than a battle script or different strategic order?
6. Was the ritual blocked, resisted, intercepted, or converted into a battle?
7. Did another randomly ordered ritual change the target first?
8. Was the expected result an ongoing global effect that waits until step 28?
9. Was the spell from a different ruleset or mod version?

### "My new building did nothing"

Construction finishes at step 35. It cannot enable research at step 2, recruitment at step 3, forging at step 5, or rituals at step 10 during that same hosting cycle.

### "My summoned allies missed the battle"

If they came from a special order such as Summon Allies or Reanimate, they arrived at step 36 after the battle steps. Ritual summons follow different timing and must be analysed under the ritual that created them.

### "The battle used different dominion than expected"

Check:

- preaching at step 6;
- heretic preaching at step 7;
- special religious effects;
- the pre-host candle state;
- whether ordinary dominion spread at step 42 occurred only after the battle;
- whether the battle report or later map screen is being used as the reference state.

### "The province produced less income than expected"

Check:

- ownership after movement and battle;
- pillage at step 37;
- population;
- unrest already present before the income step;
- dominion and scales;
- sites and events;
- partial ownership caused by a fort;
- whether the figure came from a pre-host projection or the final income report.

### "The unit survived battle but disappeared"

Possible causes include:

- a later event or special-effect battle;
- starvation;
- upkeep desertion;
- site or dominion damage;
- disease at step 48;
- lone-unit cleanup at step 52;
- elimination or victory;
- end-of-turn shape or item validation.

## Ruleset and mod implications

### Core sequence versus mod-added content

Ordinary `.dm` mods can add or modify:

- units;
- weapons and armour;
- spells;
- items;
- sites;
- nations;
- blessings;
- population types;
- mercenaries;
- events;
- AI templates and preferences;
- many special attributes.

The current modding manuals do not expose a command for rewriting the engine's entire 63-step hosting sequence.

The practical model is:

- the engine retains its main sequence;
- mods insert new content into the steps appropriate to that content;
- a modded ritual still belongs to ritual processing;
- a modded event still belongs to event processing;
- a modded monthly monster or item effect belongs to the relevant special-effect stage;
- mod load order determines the final data definitions used when those steps run.

This conclusion is **Official limits plus inference**, not proof that no executable-level modification could ever alter hosting.

### Mod load order

The Modding Manual states that complete mods are loaded one at a time. Within a mod, command categories are parsed in an internal order including weapons, armour, units, names, blessings, sites, nations, spells, items, general commands, population types, mercenaries, and events.

When two enabled mods alter the same object, later alterations can overwrite earlier values. The manual warns that overlapping modifications can produce unpredictable behaviour.

For the frozen ruleset, Dominions Enhanced loads before Divinitus. Book IX owns the exact overlap and collision record, while the Grand Hierophant reconstruction is kept with the Arcoscephale dossier in Book VII. The timing lesson here is simply that load order belongs to the ruleset.

### Event chains and compatibility

The Event Modding Manual warns that event-code collisions between mods can scramble event chains and create severe bugs. It recommends negative event codes in a reserved range and careful compatibility checking.

Both active mods add large event libraries. Their size alone does not prove a collision, but it makes code and variable auditing a foundational requirement. The exact registries and current collision findings are recorded once in Book IX.

## Controlled tests required by Book I

The official sequence is explicit, but several practical interactions still need current-game reproduction.

### Test protocol

Every test should record:

- game version;
- operating ruleset;
- enabled mods and load order;
- map and game settings;
- turn number and season;
- relevant units, IDs, paths, items, sites, and province state;
- exact submitted orders;
- pre-host save;
- messages and battle reports;
- before-and-after screenshots or extracted state;
- number of repetitions;
- conclusion and confidence label.

### Priority timing tests

| # | Test | Controlled question |
| ---: | --- | --- |
| 1 | Research completion and same-turn scripting | Can a newly completed research level make a pre-scripted spell available in a later battle that month, and how are invalid scripts handled? |
| 2 | Preaching and battle dominion | Does successful step-6 preaching change dominion-dependent battle statistics before a step-26 battle? |
| 3 | Throne claim-loss regression | Confirm that later claimant death preserves a completed claim, while unfortified conquest or a successful fort storm makes the Throne unclaimed before step 57. |
| 4 | Forged item availability | Can a step-5 forged item influence an already-submitted same-turn ritual or special effect without being equipped beforehand? |
| 5 | Newly discovered site effects | Does a site discovered at step 14 apply its monthly effect at step 44 in the same month? |
| 6 | Assassinated movement commander | What happens to movement and assigned troops when their only commander dies at step 20? |
| 7 | Friendly movement priority | Which forces appear in battle when friendly reinforcement and an enemy invasion enter the same province during an ownership change? |
| 8 | Global casting versus first world tick | Which parts of a global occur at casting step 10 and which wait for world-effect step 28? |
| 9 | Pillage and same-turn income | How much income is lost when a newly captured province is pillaged at step 37 before income at step 38? |
| 10 | Unrest timing | Which of pre-existing unrest, pillage unrest, patrol reduction, and dominion-driven unrest changes influence step-38 income? |
| 11 | Starvation timing | Does a newly undersupplied army fight at its prior state before receiving the post-host starvation effects? |
| 12 | Upkeep desertion priority | Which units desert first during a controlled treasury shortfall? |
| 13 | Site, dominion, and disease ordering | How do site disease, dominion effects, aging, regeneration, and existing disease combine in the end-of-turn health sequence? |
| 14 | Scouting before PD reduction | Do reports or interface values show PD before or after the step-61 population reduction? |
| 15 | Victory before immortal return | Can victory or elimination end the game on the same turn an immortal is due to reform at step 60? |
| 16 | DE and Divinitus event-code audit | Do the two supplied files collide in event codes, variables, rarity classes, or order requirements? |

## Source record

### Primary official sources

- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html), accessed 25 August 2026.
- [Dominions 6 Manual, revision 2](https://www.illwinter.com/dom6/dom6manual.pdf), especially pages 13, 47-57, 73-87.
- [Illwinter update record](https://www.illwinter.com/), recording Dominions 6.36 on 17 August 2026 UTC.
- [Official Dominions 6.36 announcement](https://steamcommunity.com/games/2511500/announcements/detail/693143486970465344).
- [Dominions 6 changes from Dominions 5](https://www.illwinter.com/dom6/changes.html).
- [Dominions 6 Modding Manual, version 6.34](https://www.illwinter.com/dom6/dom6modman.pdf), especially pages 3-5 and 63-65.
- [Dominions 6 Event Modding Manual, version 6.29](https://www.illwinter.com/dom6/dom6eventman.pdf), especially pages 2-11.

### Exact mod sources

- `DomEnhanced2_16.dm`, SHA-256 `72558697f8dae3a1fccf8fb57b3faccde56c7fe6c05dac6403cefe153faf6c1b`.
- `Divinitus_1.15.3_DE.dm`, SHA-256 `cf7f21900a3812b66edddd831df779743eaf33080aef983f9bdea8ec47642809`.

### Verification note

The public base game is version 6.36, while the current official Modding Manual identifies itself as version 6.34 and the Event Modding Manual as version 6.29. This is not automatically a contradiction: auxiliary manuals are updated when their documented interfaces change. It does mean that later patch notes and current-game tests remain necessary whenever a rule could have changed after a manual's stated version.
