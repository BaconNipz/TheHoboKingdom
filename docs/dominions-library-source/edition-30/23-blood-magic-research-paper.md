# Blood Magic in Dominions 6

## Extraction, Logistics, Ritual Power, and Strategic Conversion

**Research paper, first edition**  
**Rules baseline:** Dominions 6.36  
**Optional mod appendix:** Dominions Enhanced 2.16, loaded before Divinitus 1.15.3 DE  
**Research date:** 3 August 2026

---

## Abstract

Blood magic is often introduced as the ninth magic path, but that description conceals the system that makes it distinctive. Fire, Air, Water, Earth, Astral, Death, Nature, and Glamour normally draw their expendable power from gems produced by sites. Blood draws power from people. It converts mage-turns, population, patrol labour, infrastructure, religious authority, and administrative attention into blood slaves; then it converts those slaves into battlefield spells, demons, remote attacks, path development, dominion pressure, and world enchantments.

This difference changes the correct unit of analysis. A Blood spell cannot be judged only by its path requirement and listed cost. Its real cost includes the province that supplied the victims, the hunter who stopped researching, the patrol that contained the unrest, the laboratory that pooled the slaves, the commander who transported them, and the opportunity displaced by the whole chain. The same system can nevertheless scale far beyond a modest gem income. Once several well-run hunting centres feed a protected ritual network, Blood becomes one of the strongest conversion engines in the game.

The paper develops that argument from exact hunting rules, hosting order, logistics, research, battlefield casting, Sabbaths, ritual portfolios, path access, blessings, sacrifice, late-game globals, counterplay, and operational controls. Engine rules, strategic doctrine, community heuristics, and modded changes are kept separate throughout.

## Scope and evidence

The principal rules source is the official *Dominions 6 Manual*, revision 2. Later official update announcements through 6.36 control where the executable has changed or clarified that printed text. Current in-game data and the community-maintained Dominions 6 reference are used only where the old manual has demonstrably fallen behind, most notably the cost of Enchanted Blood. Strategic recommendations are deductions from those rules, not additional engine rules.

Four labels are used:

| Label | Meaning |
| --- | --- |
| **Official rule** | Stated in the manual or an official Illwinter update. |
| **Derived result** | Arithmetic or timing consequence calculated from official rules. |
| **Doctrine** | A repeatable strategic method supported by the rules but not hard-coded by the engine. |
| **Modded rule** | Applies only to the named mod stack and load order. |

The universal spell index covers the ordinary Blood-school spells and rituals printed in the manual. National, Pretender-specific, event-granted, and mod-added Blood effects form much larger object families. They are discussed as variations rather than being mistaken for universal access.

# 1. Blood Is a Production System

## 1.1 Path, school, and currency

Blood has three related but separate meanings.

- **Blood path** is a statistic on a mage, written B1, B2, and so on.
- **Blood Magic school** is one of the seven research schools.
- **Blood slaves** are the expendable resource used by Blood rituals and by sufficiently fatiguing Blood battle spells.

Researching Blood Magic does not grant the Blood path. Possessing Blood mages does not unlock unresearched spells. Holding slaves does not allow a mage to ignore path requirements, research level, laboratory requirements, range, target restrictions, or underwater restrictions. A legal cast still needs every part of the access chain:

```text
known spell
+ sufficient Blood and crosspaths
+ required research
+ required slaves
+ valid location and target
= legal cast
```

Blood is neither an elemental path nor a sorcery path. This matters for items and effects that increase only one of those path groups. It also matters for strategic expectations: a general sorcery booster does not necessarily raise Blood unless its actual description includes Blood.

## 1.2 Blood slaves are not gems

Blood has no ordinary gem type. Slaves are produced principally by the Blood Hunt order, carried by commanders, pooled at laboratories, transferred to field casters, spent in rituals and battles, or sacrificed by eligible priests. Their physical handling creates a logistics problem that passive gem income does not reproduce.

The production chain is:

```text
hunter recruitment and mage-turns
+ population and low unrest
+ patrol labour and local security
+ laboratory and transport capacity
-> blood slaves
-> spells, summons, items, empowerment, Sabbaths, and sacrifice
```

Calling the slaves “free” ignores most of the chain. Gold is paid for hunters, patrollers, escorts, forts, and laboratories. Research is lost when mages hunt. Income and recruitment suffer when unrest rises. Population can be lost while unrest is suppressed. Slaves carried into danger can be captured or lost with their bearer. The cost is distributed across the state rather than printed in one tooltip.

## 1.3 Indirect benefits of the path

Blood skill has effects even when no spell is cast.

| Blood level | Indirect benefit |
| ---: | --- |
| Every level | +10 Undead Leadership and +10 Magic Leadership per level |
| B3 | +5 Hit Points |
| B4 | A further +5 Hit Points, cumulative with the B3 benefit |

For demons, Blood also governs the body-appropriate maximum-age modification. This is part of the wider age system: Death is relevant to undead, Earth to inanimate bodies, Blood to demons, and Nature to most ordinary living bodies. These indirect benefits help explain why a high-Blood demon or commander can be more durable and command a larger magical host than its spell list alone suggests.

# 2. The Exact Mechanics of Blood Hunting

## 2.1 The three checks

An ordinary Blood Hunt passes three successive checks.

```text
Blood check success = 10% + 30% x Blood level
Population check success = population / 75 percent
Unrest check failure = unrest / 4 percent
```

All three must succeed. Probabilities above 100% are effectively capped by certainty; probabilities below zero contribute no success.

If every check succeeds:

```text
slaves found = d6 + Blood level
unrest gained = d(slaves x 3 + 4)
```

If any check fails:

```text
slaves found = 0
unrest gained = d6 - 1
```

The failure result is important. An unproductive hunter still consumes the order and usually makes the province less suitable for the next attempt.

At 7,500 population the population check reaches its nominal 100%. At B3 the Blood check reaches its nominal 100%. Higher population still supplies a larger long-term economic and demographic buffer, but it no longer improves this particular success check. Blood above B3 continues to increase the slaves found on a successful hunt, while its basic Blood check has already saturated.

## 2.2 Combined probability

For Blood level `B`, population `P`, and unrest `U`, the ordinary chance that all checks succeed can be written:

```text
p = min(1, 0.10 + 0.30B)
    x min(1, P / 7500)
    x max(0, 1 - U / 400)
```

At the default 50% magic-site frequency, the expected slaves from one hunter before retaliation or special abilities are approximately:

```text
expected slaves = p x (B + 3.5)
```

The manual states that every five percentage points of magic-site frequency above or below 50 changes average slaves found by 0.5. The corresponding conditional adjustment is approximately `(site frequency - 50) / 10` slaves.

### Worked expectations at 50% site frequency

| Hunter and province | Success chance | Conditional average | Expected slaves |
| --- | ---: | ---: | ---: |
| B1, 7,500 population, 0 unrest | 40.0% | 4.5 | 1.80 |
| B2, 7,500 population, 0 unrest | 70.0% | 5.5 | 3.85 |
| B3, 7,500 population, 0 unrest | 100.0% | 6.5 | 6.50 |
| B1, 5,000 population, 20 unrest | 25.3% | 4.5 | 1.14 |
| B2, 5,000 population, 20 unrest | 44.3% | 5.5 | 2.44 |
| B3, 5,000 population, 20 unrest | 63.3% | 6.5 | 4.12 |
| B3, 7,500 population, 40 unrest | 90.0% | 6.5 | 5.85 |

These are single-hunter expectations, not promises. They omit site-frequency adjustment, special Blood Searcher abilities, national mechanics, retaliation, losses, and the effects of several hunters sharing the same administrative system.

## 2.3 Expected unrest

On a successful hunt that finds `S` slaves, the average of `d(3S + 4)` is `(3S + 5) / 2`. On a failed hunt, the average of `d6 - 1` is 2.5. For a single ordinary hunter at B3 in a perfect 7,500-population, zero-unrest province, the average successful yield is 6.5 slaves and the average unrest addition is 12.25 before later reduction.

This does not create a universal patrolling ratio. Patrol efficiency varies by unit, leadership, abilities, national mechanics, existing unrest, and the population killed while order is restored. It does show why a centre that looks stable before expansion can fail rapidly after one or two additional hunters are assigned.

## 2.4 Site frequency

Magic-site frequency is a game-creation setting, but it also changes Blood output. Every five percentage points away from 50 changes average slaves found by 0.5 in the same direction. A Blood economy should therefore be recalibrated to the actual game settings rather than copied unchanged from a standard game.

The setting affects both sides of the strategic comparison. High site frequency raises ordinary gem access and Blood yield; low site frequency suppresses both, but the exact balance depends on national access, search coverage, and how efficiently population can be converted.

## 2.5 Retaliation and dominion

Commoners may refuse to surrender victims and fight the hunter and whatever bodyguards are present. Strong friendly dominion makes the sacrifice appear religiously legitimate. The manual states that at dominion strength 10 almost no one refuses.

Friendly dominion is therefore a security input, not just a religious overlay. A mature centre benefits from:

- friendly candles;
- bodyguards appropriate to the local retaliation risk;
- patrols that can suppress unrest and reveal hostile stealth;
- a fort or response force protecting the accumulated investment;
- replacement hunters and patrollers.

Hostile dominion can turn a previously safe hunting centre into an unstable one even before the province changes military control.

# 3. Hosting Order and the Blood Calendar

## 3.1 The decisive steps

Blood operations sit at several different points in the 63-step hosting sequence.

| Step | Event | Blood consequence |
| ---: | --- | --- |
| 2 | Research | A mage hunting this month contributes no research; a researcher killed later still contributed. |
| 4 | Empowerment | A completed Blood empowerment applies before later events. |
| 5 | Forging | Blood-funded items complete before rituals and hunting. |
| 6 | Preaching | Ordinary preaching resolves before sacrifice-driven general dominion spread. |
| 10 | Rituals | Blood rituals spend slaves already available when orders were submitted. |
| 18 | Blood Hunting | New slaves and hunt unrest are produced. |
| 19 | Horror visits | Marked or otherwise eligible units may be attacked. |
| 20 | Assassinations | A hunter can be killed after completing the hunt. |
| 24-25 | Movement | Ordinary transport and conquest occur after hunting. |
| 35 | Construction | A new laboratory or temple is too late for this month’s earlier Blood actions. |
| 38 | Income | Hunt-created unrest already exists when income is collected. |
| 39 | Unrest alterations | Patrolling and ordinary unrest reduction occur after income. |
| 42 | Dominion spread | General dominion spread, including the month’s checks, resolves late. |

## 3.2 Consequences of the sequence

Three planning rules follow directly.

First, a ritual resolves at step 10 and a hunt at step 18. Slaves found this month cannot fund a ritual already ordered for this same hosting. Ritual budgets must be covered from pre-existing stock.

Second, hunt unrest exists before step-38 income, while patrol reduction normally waits until step 39. The centre can pay an income penalty for unrest that is removed later in the same hosting. Low baseline unrest is consequently more valuable than a plan that merely restores the province after every spike.

Third, a hunter may complete the hunt and then die to a Horror or assassination before movement. The current slave contribution can survive while the future production stream disappears. Security reports should therefore distinguish this month’s output from next month’s capacity.

## 3.3 A practical monthly calendar

Before submission:

1. forecast ritual, forging, sacrifice, and field requirements;
2. reserve every step-5 and step-10 expense from slaves already in hand;
3. pool hunters standing at laboratories;
4. transfer exact field loads to commanders who may leave;
5. assign hunts only where patrol, population, and security can support them;
6. inspect existing unrest rather than assuming the patrol will erase it in time;
7. preserve a contingency reserve for emergency defence or replacement casts.

After hosting:

1. record slaves per hunter-turn;
2. inspect unrest before assigning more hunters;
3. compare population and income trends;
4. replace losses and bodyguards;
5. pool newly gathered slaves;
6. reconcile the ritual queue against the new reserve;
7. investigate unexpected output before scaling the centre.

# 4. Building a Blood Centre

## 4.1 Site selection

The strongest hunting province is not automatically the largest province on the map. A centre must balance yield, longevity, tax value, recruitment value, defence, connectivity, and replacement cost.

Useful properties include:

- population at or above the 7,500 success threshold;
- enough additional population to survive repeated enforcement losses;
- low unrest and spare patrol capacity;
- friendly dominion;
- a laboratory for pooling and ritual support;
- a fort, nearby army, or rapid response route;
- no irreplaceable recruitment function that unrest will shut down;
- a manageable distance from ritual centres and field armies.

A rich capital can be an efficient early centre and a disastrous long-term sacrifice if hunting interferes with capital-only recruitment, commander production, or research. A secondary high-population province may be strategically better even when its immediate tax base is smaller.

## 4.2 The centre as a coupled machine

A functioning centre contains six linked processes.

1. **Hunters** create slaves and unrest.
2. **Patrols** reduce unrest and detect infiltrators.
3. **Population** supplies victims, taxes, Recruitment Points, supplies, and PD support.
4. **Laboratories** permit pooling, transfers, rituals, and research when mages are not hunting.
5. **Security** protects the hunters, slaves, temple, and laboratory.
6. **Replacement streams** prevent a raid or assassination from stopping production permanently.

Weakness in any one process limits the whole centre. More hunters do not repair insufficient patrols. More patrols do not replace lost population. A fort does not restore research consumed by hunting. A large stockpile does not help a battlefield mage who was never issued slaves.

## 4.3 The scaling trap

The most common expansion error is to add hunters until the displayed slave total rises, then discover several months later that output, income, and recruitment are all falling.

The sequence is predictable:

```text
more hunters
-> more unrest
-> lower hunt success and lower income
-> more patrol labour and population loss
-> weaker recruitment and defence
-> higher vulnerability to raids
-> interrupted production
```

The correct scaling test asks whether the next hunter increases **net useful Blood output**, not merely gross slaves. Net output prices the added hunter, lost research, patrol cost, tax damage, demographic damage, laboratory exposure, and expected security losses.

## 4.4 A community heuristic

Community guides often use roughly 25 patrol strength per B3-equivalent hunter as an initial planning figure under ordinary conditions. This is a doctrine, not an engine ratio. It should be treated as a starting budget followed by observation.

The figure can be wrong because of:

- unusual patrol bonuses;
- low or high site frequency;
- Blood Searcher and national abilities;
- several hunters producing correlated unrest;
- existing province unrest;
- extreme population values;
- friendly or hostile dominion;
- modded events and Pretender powers.

## 4.5 Centre metrics

| Measure | What it reveals |
| --- | --- |
| Slaves per hunter-turn | Extraction efficiency across mage types and provinces |
| Unrest before and after hosting | Whether patrol capacity has a safety margin |
| Population trend | Long-term life of the centre |
| Lost research per month | Magical opportunity cost |
| Patrol purchase and upkeep | Gold cost of containment |
| Income delta | Administrative cost paid before patrol resolution |
| Hunter and lab losses | Security cost |
| Slaves converted into effects | Whether stock is becoming power |

The final measure is the most important. A centre that produces 100 slaves and converts none has created potential, not strategic effect.

# 5. Slaves as Logistics

## 5.1 Pool, reserve, field load

Blood slaves carried by commanders can be pooled into the national treasury when those commanders stand in a laboratory province. Slaves required for battle must be placed on the caster before the battle. Treasury stock cannot rescue an under-supplied field mage after combat begins.

A disciplined allocation divides the stock into named pools:

| Pool | Purpose |
| --- | --- |
| Strategic reserve | Globals, emergency rituals, empowerment, and replacement infrastructure |
| Monthly ritual budget | Casts resolving at step 10 |
| Forge budget | Items completing at step 5 |
| Dominion budget | Blood sacrifice at eligible temples |
| Field loads | Battle spells and Sabbath entry |
| Contingency | Recasts, surprise attacks, and losses |

“Available slaves” means stock not already promised to one of these uses. A treasury number that counts the same slaves in three plans is an accounting error.

## 5.2 Battle-spell slave costs

The manual’s general battle-magic rule requires one gem of the primary path for a spell with at least 100 listed fatigue, plus another for each full additional 100. For a Blood-primary spell, the resource is a blood slave.

| Listed fatigue | Primary resource required |
| ---: | ---: |
| Below 100 | None under the ordinary threshold rule |
| 100-199 | 1 slave |
| 200-299 | 2 slaves |
| 300-399 | 3 slaves |
| 400-499 | 4 slaves |

Extra skill reduces the fatigue actually suffered but does not rewrite the spell’s printed resource threshold. Sabbath Master and Sabbath Slave each list 100 fatigue, so each joining Blood mage needs a slave to cast the entry spell.

## 5.3 Transport risk

Moving slaves solves one problem by creating another. A field commander carrying only the exact scripted minimum may become useless after an interruption or changed target. A commander carrying the national treasury exposes months of production to one battle, assassination, seduction, or routing disaster.

The safe load is therefore:

```text
scripted minimum
+ one defined fallback allowance
+ Sabbath entry cost where relevant
- stock with no battlefield purpose
```

The appropriate reserve depends on whether the caster is replaceable, whether a laboratory lies behind the front, and whether the planned battle is decisive enough to justify treasury risk.

# 6. Research and the Blood Portfolio

## 6.1 Research is a response tree

Blood research is strongest when each breakpoint has an assigned job. Researching the school because a nation “uses Blood” can leave the state with unlocked spells but no slaves, no suitable casters, and no military need for the result.

A functional plan names:

- the first battlefield package;
- the first permanent summon;
- the first remote threat;
- the first path booster or access bridge;
- the defensive answer if hunting centres are raided;
- the late-game global worth protecting.

The Blood school mixes cheap tactical spells, permanent demon summoning, horror projection, province attacks, movement, healing, crossbreeding, domes, and world enchantments. Higher research is not simply a stronger version of the same effect.

## 6.2 Early Blood

Early Blood provides basic attacks, healing, reinvigoration, temporary imps, Sabbath entry, and low-cost permanent fiends. Its strategic value is often access rather than raw scale.

Important early decisions include:

- whether a B1 or B2 caster is more valuable researching than hunting;
- whether the field army can supply slaves without starving the first ritual queue;
- whether permanent summons solve a real troop or leadership problem;
- whether a small Sabbath unlocks a crosspath spell package unavailable to individual mages.

Low research can already create a working Blood loop. It should not be confused with a mature Blood economy.

## 6.3 Middle Blood

Middle levels broaden the portfolio into battlefield-wide buffs and debuffs, mind and body attacks, horrors, demon commanders, crossbreeding, province disruption, movement, and more specialised summons. This is often the point at which Blood stops being a supporting path and becomes an operational branch of the state.

The limiting factor shifts from “is any Blood spell useful?” to “which consumer receives the slaves?” A nation simultaneously funding demons, Rain of Toads, Sabbaths, empowerment, and sacrifice can exhaust an apparently large reserve quickly.

## 6.4 High and legendary Blood

High Blood supplies mass strength effects, major horror operations, unique infernal commanders, large demonic armies, harsh province rituals, and four universal Blood globals. These spells can change the international environment rather than merely one battle.

Blood 9 follows the legendary-spell rule: the first level-nine spell is chosen individually, and the remaining legendary spells require further research. Reaching “Blood 9” therefore does not instantly unlock every level-nine option. The choice should be made against the current war, global board, caster access, and slave reserve.

## 6.5 Functional families

| Family | Blood contribution | Principal audit |
| --- | --- | --- |
| Direct damage | Bleeding, boiling, leeching, Hellfire, Harm, life exchange | Armour type, MR, immunities, range, caster survival |
| Sustain | Blood Heal, Reinvigoration, Pain Transfer, Purify Blood, Rejuvenate | Valid body, fatigue, timing, slave cost |
| Army effects | Blood Lust, Blood Rain, Rush of Strength, Bloodletting | Battlefield scope, friendly exposure, caster continuity |
| Control | Banish Demon, Hellbind Heart, Infernal Prison, Claws of Kokytos | MR, target class, escape or banishment consequences |
| Temporary summons | Imps, horrors, Illearth | Arrival, control, danger to both sides, battle duration |
| Permanent summons | Fiends, devils, unique infernal lords, mass forces | Leadership, upkeep, research, crosspaths, uniqueness |
| Remote pressure | Horrors, disease, fumes, toads, dream attacks | Range, anonymity, domes, retaliation, diplomatic cost |
| Mobility | Hell Ride and related national tools | Destination legality, survival, load, interception |
| Development | Bowl of Blood, empowerment, boosters, Infernal Circle | Mage-turns, slave reserve, protection of rare casters |
| Globals | Blood Moon, Blood Vortex, Astral Corruption, Looming Hell | Global slot, caster security, coalition response |

# 7. Battlefield Blood Magic

## 7.1 What Blood does in combat

Blood’s battlefield identity is unusually broad. It can damage living targets through armour-negating or life-draining effects, punish demons, heal or reinvigorate casters, create temporary attackers, amplify strength, alter morale, enslave or banish targets, and send horrors into the battle.

The breadth should not be mistaken for universal reliability. Many Blood spells are marked not usable underwater. Several exempt undead, inanimate, mindless, or other target classes. Horror summoning can introduce an actor whose behaviour is not equivalent to an ordinary controlled troop. Blood packages need a target audit rather than a memorised script.

## 7.2 Script construction

A Blood combat script should answer seven questions.

1. Which spell is essential, and in which round must it resolve?
2. How many slaves does every scripted spell require?
3. Does the caster need a slave for Sabbath entry before the main script begins?
4. Which targets are immune, difficult to reach, or likely to pass MR?
5. What happens if the first spell is interrupted?
6. What will spell AI cast after the five scripted orders?
7. Can the caster and slave load retreat without exposing the strategic reserve?

The field load should be derived from the script line by line. A B3 mage with “several slaves” is not a plan.

## 7.3 Blood Bond and Blood Vengeance

Blood Bond redistributes damage; it does not erase it. In the current reference, half the damage taken is dispersed to other bonded units within five squares. Formation density, distance, area damage, regeneration, unequal protection, mounts, and the sequence of hits determine whether the distribution prevents deaths or causes a group collapse.

Blood Vengeance threatens the attacker with the damage inflicted unless Magic Resistance negates the return. It changes targeting economics: a powerful remote attack or elite strike may kill its target and still destroy the source. Patch 6.32 closed a particular exploit by preventing the enemy from looting remote ritual casters killed by Blood Vengeance.

Neither blessing is a generic statement that a sacred cannot be attacked. Blood Bond can be overwhelmed by broad simultaneous damage, and Blood Vengeance is subject to its MR interaction. Both demand matchup-specific analysis.

# 8. Sabbaths

## 8.1 Separate communion type

A Sabbath is Blood’s battlefield communion. It uses Sabbath Master and Sabbath Slave, both at Blood 1 and Blood Magic 1. It is separate from an Astral Communion and from MA Man’s Chorus. One of each type may coexist, but their masters, slaves, bonuses, and fatigue pools do not merge.

A valid Sabbath requires at least one master and one slave. The first slave makes the structure valid but grants no path bonus.

## 8.2 Path bonus thresholds

A master gains `n` levels in every path already known when at least `2^n` active slaves exist.

| Active slaves | Bonus to every known master path |
| ---: | ---: |
| 1 | +0 |
| 2-3 | +1 |
| 4-7 | +2 |
| 8-15 | +3 |
| 16-31 | +4 |
| 32-63 | +5 |
| 64-127 | +6 |

The bonus does not create an absent path. A B1F1 master can become stronger in Blood and Fire; a B1 master does not acquire Fire because Fire spells were researched.

Thresholds update immediately. Four slaves grant +2, but the loss of one drops the bonus to +1. A design with exactly four slaves is therefore powerful and brittle. Five or six provide the same bonus with casualty tolerance.

## 8.3 Participants and fatigue

For one spell cast by a master, the participants are that casting master plus every friendly slave in the Sabbath. Other masters are not participants in that individual cast.

```text
base fatigue share
= spell fatigue after path calculations
/ number of participants
```

Each slave’s share is then modified by its relevant path skill relative to the casting master.

| Slave skill relative to master | Slave fatigue modifier |
| --- | ---: |
| Higher | x0.5 |
| Equal | x1 |
| Lower, but at least half | x2 |
| Lower than half | x4 |

The Sabbath then applies its type-specific rule: the master suffers half fatigue, while slaves suffer 20% extra fatigue.

Suppose one master and four slaves divide a resolved 100-fatigue spell. The initial share is 20. Before the Sabbath’s additional slave modifier, a higher-skilled slave receives 10, an equal slave 20, a lower-but-at-least-half slave 40, and a slave below half 80. The same four slaves receive another fatigue event for every additional master cast.

This is why “four slaves per master” is not an engine rule. Master count, spell frequency, relative path skill, threshold redundancy, shared buffs, body encumbrance, reinvigoration, and expected battle length all matter.

## 8.4 Slaves cannot act

Sabbath slaves take no independent actions while participating. Their battlefield mage-turns become path bonus, shared fatigue capacity, and risk. A high-path slave may absorb fatigue efficiently and still be too valuable to immobilise.

Slaves receive qualifying personal self-buffs cast by masters: single-target, range-zero effects. This can distribute protection, resistance, regeneration, or reinvigoration across the slave block, but it can also apply an unsuitable effect to the wrong body. Timing matters because early master casts can load fatigue before the protection arrives.

## 8.5 Collapse

The Sabbath ends when no masters or no slaves remain. If every master dies or flees, each slave is stunned for about one round and suffers `3d50` fatigue. An already exhausted block can be disabled or killed by the backlash.

Protecting masters is therefore part of protecting slaves. Redundant masters reduce the chance of sudden collapse, but every active master can also increase fatigue throughput. Positioning every master in one area creates a single point of failure against flyers, area attacks, missiles, assassins, and fast contact.

## 8.6 Automatic participation

Crystal Matrix, Slave Matrix, Slave’s Heart, and Master’s Athame are manual examples of items that can cause automatic communion participation. The bearer must be a mage with at least one non-Holy path but need not possess Astral or Blood.

Automatic entry saves the opening cast and can bring foreign paths into the structure. It also consumes item slots, forge resources, and preparation turns, while creating equipment whose loss may invalidate the whole package.

## 8.7 Sabbath design sequence

1. Name the exact spell each master must reach.
2. Calculate the required threshold and provide at least one spare slave where practical.
3. Recalculate the master’s known paths after the bonus.
4. Determine spell fatigue at the boosted level.
5. Count participants for each master cast.
6. Place every slave in the correct relative-skill bracket.
7. Apply the Sabbath master and slave modifiers.
8. Add the simultaneous load from all masters.
9. Check shared personal buffs and body compatibility.
10. Protect masters and separate single points of failure.
11. Plan the unscripted rounds.
12. Define what an orderly retreat or acceptable collapse looks like.

# 9. Summons, Demons, and Horror Operations

## 9.1 Permanent force conversion

Blood summoning converts a renewable but destructive resource stream into permanent military bodies. The universal list progresses from small imps and fiends through specialised elemental demons, commanders, unique infernal beings, and mass late-game forces.

Summons should be valued against more than bodies per slave.

| Question | Why it matters |
| --- | --- |
| Does the result need undead or magic leadership? | A summon that cannot be commanded is not field power. |
| Is the commander unique? | A unique infernal lord is an access bridge and irreplaceable asset. |
| Which crosspath is required? | Blood income alone may not create the caster. |
| Can the ritual be cast underwater? | Most universal Blood rituals are marked NUW. |
| Does the result solve mobility, damage, fear, or magic access? | Raw unit count can conceal the actual purpose. |
| What is the counter package? | Banishment, anti-demon effects, resistances, MR, morale, and specialised weapons vary by summon. |

## 9.2 Horrors are strategic weapons

Blood and Astral together produce several horror operations: battlefield calls, remote Lesser Horror and Horror attacks, dream attacks, Horror Seed, Dome of Corruption, and Astral Corruption. These effects project danger beyond ordinary army movement and can make enemy magical activity itself hazardous.

Horror operations have political consequences. Anonymous rituals may conceal the caster, but repeated attacks still alter threat perception and diplomatic behaviour. Horror marks can outlast the immediate operation and attract future visits. Valuable casters require redundancy and protection even after surviving the first attack.

## 9.3 Crossbreeding

Cross Breeding, Improved Cross Breeding, Infernal Breeding, and the related unique Manual turn slaves into variable created creatures. Their value is distributional rather than represented by one average body. A proper record tracks useful results, leadership demands, production time, and the fraction of outcomes that enter an actual army.

The attraction is flexibility and occasional exceptional value. The cost is variance, mage-turns, infrastructure, and a force whose mixed bodies may be difficult to script or support.

# 10. Blood Sacrifice and Dominion

## 10.1 The order

An eligible national priest standing in a province with a temple may perform Blood Sacrifice.

- The maximum slaves sacrificed equals the priest’s Holy level.
- Each slave creates one temple check.
- The priest must belong to a nation or unit permitted to perform the order.
- The action consumes the priest’s monthly order and the slaves.

Possessing a temple, a priest, and slaves does not by itself grant eligibility. Blood Sacrifice is a national or unit ability.

Version 6.36 corrected an operational trap: changing the items carried by a blood sacrificer no longer removes the Blood Sacrifice order. The correction preserves the order; it does not alter eligibility, the Holy-level cap, or slave consumption.

## 10.2 Strategic value

Blood Sacrifice converts the same slave stock used by magic into religious pressure. Its value rises when:

- dominion survival is threatened;
- a throne claim or special dominion effect depends on local candles;
- the nation already has efficient hunting infrastructure;
- the temple network can project checks from useful locations;
- the military and magical value preserved exceeds the sacrificed alternative.

The correct comparison is not “slave versus candle.” It is the expected strategic consequence of the temple checks versus the ritual, summon, item, or battle spell displaced.

## 10.3 Mictlan’s dying dominion

Early and Late Age Mictlan use the special dying-dominion system. Home-province, prophet, and temple spread do not operate normally; Pretender checks are half as effective; Blood Sacrifice becomes the essential spread mechanism.

For these nations, temples are sacrifice stations rather than ordinary passive dominion engines. Hunting, priest recruitment, slave transport, temple placement, and military security form one religious logistics system. Treating sacrifice as an optional late-game use of surplus slaves misunderstands the national structure.

## 10.4 Nations listed by the revision-2 manual

The manual lists the following vanilla nations as historically able to perform Blood Sacrifice. Current unit cards and mod data remain authoritative where later content changes eligibility.

| Era | Nations |
| --- | --- |
| Early | Mictlan, Xibalba, Marverni, Sauromatia, Abysia, Pangaea, Vanheim, Hinnom, Berytos |
| Middle | Abysia, Vanheim, Pyrène, Vanarus, Nidavangr |
| Late | Marignon, Mictlan, Xibalba, Abysia, Midgård, Gath |

# 11. Blood Blessings

## 11.1 Current vanilla reference

The current 6.35 reference differs from the older printed manual on Enchanted Blood: the revision-2 table prints B4, while the current game reference places it at B3. Patch 6.35 also makes its +1 Magic Resistance display explicitly in the unit details.

| Requirement | Blessing | Effect | Incarnate |
| --- | --- | --- | --- |
| B1 | Strong Vitae | +1 Hit Point; stackable | No |
| B2 | Strength of the Blood | +1 Strength; stackable | No |
| B3 | Strong Blood | +5 Poison Resistance and Disease Resistance 80; innate | No |
| B3 | Enchanted Blood | Regeneration 0.5, +1 Magic Resistance, and bleeding immunity | No |
| B4 | Blood Surge | A kill against a non-inanimate target triggers temporary +3 Attack, +3 Strength, +1 Defence, and +1 Reinvigoration | No |
| B5 | Blood Bond | Half of damage is dispersed to bonded units within five squares | Yes |
| B6 | Unholy Weapons | 15 armour-piercing damage on hit against sacred or blessed targets | Yes |
| B7 | Blood Vengeance | The attacker also takes inflicted damage unless MR negates | Yes |
| B8 D4 | Vampiric Weapons | 3 armour-negating life-drain damage after a damaging hit | Yes |

## 11.2 Design principles

Blood blessings fall into four functional groups.

- **Reliable statistics:** Hit Points, Strength, Strong Blood, and Enchanted Blood improve ordinary performance without requiring the Pretender to remain awake and alive.
- **Conditional tempo:** Blood Surge rewards units likely to secure kills and continue fighting.
- **Damage architecture:** Blood Bond changes where damage lands; its value depends on formation and recovery.
- **Incarnate punishment:** Unholy Weapons, Blood Vengeance, and Vampiric Weapons create matchup-specific offensive or retaliatory power.

A blessing should be bought for the sacred roster that will use it. Enchanted Blood is disproportionately useful on bodies that survive long enough for repeated half-point regeneration and benefit materially from +1 MR. Blood Surge is weak on sacreds that rarely land the killing blow or die immediately after it. Vampiric Weapons rewards repeated damaging hits against drain-compatible targets, not merely a high nominal attack count.

The same blessing can change value across expansion, the first war, mass battlefield magic, and late-game counters. Pretender points should be priced against all four periods.

# 12. Path Access, Empowerment, and Items

## 12.1 Empowerment

Empowerment is the universal way to acquire a path a mage does not possess. The first Blood level costs 50 slaves. Later increases cost `15 x target level`: B1 to B2 costs 30, B2 to B3 costs 45, and B3 to B4 costs 60.

Empowerment is expensive but can unlock an entire booster ladder, a unique summon, or a national crosspath. It should be evaluated as an access investment rather than a mere statistic increase.

## 12.2 Non-unique path tools

| Research | Item | Requirement | Blood relevance |
| ---: | --- | --- | --- |
| Construction 5 | Armor of Souls | B5 | +1 Blood; also defensive benefits |
| Construction 5 | Armor of Twisting Thorns | B3 N2 | +1 Blood and +1 Nature |
| Construction 5 | Brazen Vessel | B5 | +1 Blood |
| Construction 5 | Sanguine Dowsing Rod | B1 | Blood Searcher 1; hunting tool rather than a path boost |
| Construction 5 | Blood Stone | B3 E2 | +1 Earth and temporary Earth gems; a Blood-funded Earth bridge |
| Construction 7 | Blood Thorn | B3 | +1 Blood |
| Construction 7 | Robe of the Magi | A5 B5 | +1 to all nine magic paths |
| Construction 7 | Ring of Wizardry | S7 | +1 to all nine magic paths |
| Construction 7 | Blood Pendant | B2 | +25% Blood spell range and +2 Strength |

Slots matter. Armor of Souls and Armor of Twisting Thorns compete for the body slot. Blood Thorn occupies a hand. Brazen Vessel and other miscellaneous tools compete for limited misc slots. A theoretical ladder that requires the same slot twice does not exist on one commander.

## 12.3 Unique artifacts

Several Construction 9 artifacts raise Blood, including the Oath Rod of Kurgi, Tome of the Lower Planes, Black Book of Secrets, and the Trapped Dreams of Hruvur. Their exact crosspath benefits differ, and only one of each artifact can exist.

Artifact access is therefore a race, not a stable national assumption. A build that requires a unique artifact needs an alternative branch if another nation forges it first or if the bearer is lost.

## 12.4 Access ladder discipline

An access ladder should be written as a graph:

```text
native caster
-> empowerment or summon
-> first booster
-> second compatible booster
-> target ritual
```

Every arrow must include research, slave cost, crosspaths, item slot, commander availability, and vulnerability. “Can reach B7” is incomplete if the only route consumes a unique mage, three strategic slots, a unique artifact, and the same slaves reserved for the ritual.

## 12.5 Nations without native Blood

Research cannot create a missing path. A nation with no recruitable Blood mage must import the first link through a Blood-capable Pretender, a national or independent summon, a foreign recruit, a conversion effect, or empowerment funded by slaves acquired from trade, events, capture, or another exceptional source.

The first B0-to-B1 empowerment costs 50 slaves, creating a bootstrapping problem: ordinary Blood Hunting requires an eligible hunter, but the intended hunter does not yet possess Blood. The first stock must therefore come from outside the normal national hunt. Arcoscephale is a useful vanilla example. Its ordinary roster does not supply a native Blood programme, so Blood is an imported strategic project rather than an assumed extension of research.

# 13. The Four Universal Blood Globals

## 13.1 Blood Moon — Blood 7, B7 S5, 90 slaves

Blood Moon grants +1 Blood for rituals and Blood searching and imposes Misfortune +2 worldwide. It has no effect in caves, underwater, or where there is no night, such as under two suns.

The global is both production and access. It raises hunting capability, improves ritual path levels, and may open casts that previously required another booster. Its geographic exceptions matter on multi-plane and underwater maps. The worldwide Misfortune penalty makes the benefit politically visible even to nations with little interest in Blood.

## 13.2 Blood Vortex — Blood 8, B7, 166 slaves

Blood Vortex creates a central site that draws suitable mortals from across the world toward sacrifice. Order reduces the effect and Turmoil increases it. The surrounding world is gradually emptied as victims are drawn to the vortex.

The global is a production engine with demographic and geopolitical consequences. Its value depends on how quickly the increased slave flow becomes decisive power and how long the central province can be held. A centre-bound global creates a strategic target rather than an abstract permanent bonus.

## 13.3 Astral Corruption — Blood 9, B6 S6, 166 slaves

Astral Corruption taints non-Blood ritual casting, item forging, and empowerment with a chance of attracting Horrors. The more gems spent, the greater the danger.

It changes the relative price of magic across the world. Blood rituals remain outside the punished category, while rival path development, forging, and high-cost rituals become hazardous. Opponents can respond by using existing armies and items, delaying magic, sacrificing expendable casters, attacking the global caster, or forming a coalition.

The spell is therefore a political economy weapon. It is strongest when the caster already possesses Blood infrastructure and opponents still depend on expensive non-Blood conversion. It is weakest when the coalition can remove the caster or when rival power is already embodied in armies and forged assets.

## 13.4 The Looming Hell — Blood 9, B8, 150 slaves

The Looming Hell sends devils into the dreams of enemy forces inside the caster’s dominion, attempting to turn soldiers against their commander. Stronger dominion makes the threats harder to resist; a feared commander makes refusal easier.

The global converts dominion reach into internal military pressure. Its target environment is not simply “the world” but enemy forces standing under the caster’s candles. Dominion warfare, army morale, commander fear, and global defence consequently become one system.

## 13.5 Global-war checklist

Before casting any Blood global:

1. verify the legendary spell has actually been selected where level nine applies;
2. reserve the full slave cost before issuing the ritual;
3. secure the caster and any centre province;
4. identify the likely coalition and its fastest attack route;
5. prepare a defence that does not consume the same irreplaceable caster;
6. calculate who benefits if the global is dispelled after only one or two months;
7. keep enough conventional force to survive while the world reacts.

# 14. Countering Blood

## 14.1 Attack the chain, not only the spell

Blood is powerful because many inputs combine. That also gives opponents several points of attack.

```text
population -> hunters -> patrols -> laboratories -> transport -> casters -> effects
```

Breaking any link can strand the others.

| Target | Effect of pressure |
| --- | --- |
| High-population provinces | Reduces future extraction and the tax base supporting patrols |
| Hunters | Removes production and often scarce mage paths |
| Patrol forces | Allows unrest and infiltrators to accumulate |
| Laboratories | Interrupts pooling, rituals, transfers, and replacement research |
| Temples | Removes sacrifice stations and local religious infrastructure |
| Slave couriers | Captures or destroys mobile reserves |
| Sabbath masters | Risks backlash and removes boosted casting |
| Sabbath slaves | Drops path thresholds and fatigue capacity |
| High-path ritualists | Breaks access ladders and globals |

## 14.2 Tempo

Blood infrastructure takes recruitment, laboratories, patrols, and diverted mage-turns. A nation investing heavily in that transition may be temporarily weaker in conventional research and field force. Early pressure can force hunters back into research or battle, turning the opponent’s planned scaling into dead infrastructure.

The objective need not be conquest. Repeated raids that require garrisons, bodyguards, and patrol redeployment can raise the administrative cost per slave enough to delay the decisive threshold.

## 14.3 Administrative warfare

Unrest attacks are especially effective against Blood centres because unrest damages both the ordinary economy and hunt success. Spies, hostile rituals, pillaging, dominion pressure, and stealth threats can force the Blood nation to over-patrol or abandon the centre.

An opponent should distinguish between destroying population that might later be conquered and denying population that will otherwise be converted into demons. Scorched-earth pressure is strategically rational only when the denial exceeds the value of the captured province.

## 14.4 Battlefield answers

Blood has no single battlefield counter. The answer depends on the package.

- Against demons, use the relevant banishment, anti-demon weapons, resistances, and leadership disruption.
- Against Sabbaths, threaten masters and slaves separately; a small casualty can cross a threshold cliff.
- Against Blood Bond, use broad or simultaneous damage and prevent the group from converting redistribution into regeneration.
- Against Blood Vengeance, improve MR where relevant and avoid spending irreplaceable attackers on low-value targets.
- Against horror calls, protect high-value mages, manage Horror Marks, and avoid scripts that assume every new battlefield actor is controlled.
- Underwater, exploit the large number of universal Blood spells and rituals marked not usable underwater.

## 14.5 Information

The Blood economy is comparatively visible. High-population provinces with labs, repeated patrol concentrations, stationary low-cost mages, and rising slave-income graphs reveal likely centres. Scouting turns those clues into target priorities.

The best defensive response is not secrecy alone. It is redundancy: several centres, spare laboratories, distributed reserves, replacement hunters, and at least one conventional army capable of fighting when a ritual plan is disrupted.

# 15. Doctrine: From Extraction to Victory

## 15.1 The conversion principle

The purpose of Blood is not to accumulate the largest slave number. It is to convert a renewable but damaging flow into an advantage that arrives before the damage matters.

That conversion can take several forms:

- a demon army that wins the next war;
- a booster ladder that unlocks a decisive ritual;
- Blood Sacrifice that prevents dominion death;
- remote attacks that remove enemy research;
- a Sabbath that changes a critical battle;
- a global that makes rival magic uneconomic.

Every slave reserve should have a planned route. Stockpiling is justified when timing, secrecy, or a large threshold gives the future conversion more value than immediate spending.

## 15.2 Three stages of a Blood economy

### Establishment

The establishment stage proves that one or two centres can hunt without collapsing. Research remains important, rituals are selective, and the state records real output rather than relying on theoretical averages.

### Expansion

The expansion stage adds hunters, patrol capacity, laboratories, transport, and specialised consumers. It distributes centres so that one raid cannot stop the economy and begins using Blood to replace some conventional troop expenditure.

### Strategic dominance

The dominance stage protects high-path casters, sustains large permanent summons, threatens several remote operations, and can contest or impose globals. The limiting resource is often no longer slaves alone but attention: scripts, movement, target selection, defence, and coordination across many centres.

## 15.3 The attention ceiling

Blood scales administratively before it scales tactically. Each additional centre creates orders for hunters, patrols, pooling, movement, rituals, and security. A technically profitable centre can still be strategically harmful if it consumes the attention needed to plan wars.

Standardised records, repeat orders, named reserves, and stable centre roles raise the attention ceiling. They do not eliminate the need for inspection, especially after raids, dominion changes, or a sudden rise in unrest.

# 16. Operational Reference

## 16.1 Blood Hunt card

```text
Required: eligible Blood hunter in the province

Blood check: 10% + 30% x B
Population check: population / 75 percent
Unrest failure: unrest / 4 percent

Success: d6 + B slaves; d(slaves x 3 + 4) unrest
Failure: no slaves; d6 - 1 unrest

Key thresholds: B3; 7,500 population
Site setting: +/-0.5 average slaves per +/-5 percentage points from 50
Timing: hosting step 18
```

## 16.2 Centre audit

- Population remains adequate for the intended life of the centre.
- Existing unrest is low enough for the next hunt.
- Patrol capacity includes a margin rather than only the average requirement.
- Friendly dominion suppresses retaliation.
- Hunters have appropriate bodyguards.
- A laboratory is available for pooling and replacement research.
- Security can answer a raid without abandoning every other front.
- Slave output is assigned to actual consumers.

## 16.3 Field-caster audit

- Every scripted spell is researched and legal for the caster.
- Crosspaths are present after, not before, any Sabbath bonus.
- Slave cost is calculated from every line of the script.
- Entry slaves for Sabbath Master or Slave are included.
- The target is not immune or outside the spell’s legal environment.
- The carrier is not holding an unnecessary strategic reserve.
- A post-script policy and retreat branch exist.

## 16.4 Sabbath audit

- At least one master and slave can enter.
- Every entry caster carries a slave.
- The active-slave threshold has redundancy.
- Every master’s boosted paths are written down.
- Each spell’s fatigue has been divided by the correct participants.
- Relative skill multipliers and the 20% slave surcharge are included.
- Masters are protected from one shared area threat.
- Slave bodies can tolerate the transmitted buffs.
- Backlash risk is accepted and planned.

## 16.5 Ritual audit

- The ritual has been selected if it is legendary.
- Path and crosspath requirements are met without double-booked items.
- Slaves already exist before hosting; the current hunt is not counted.
- Laboratory, range, target, plane, and underwater restrictions are legal.
- Dome interaction and anonymity are understood.
- The caster has a follow-up order if the target becomes invalid.
- The diplomatic response is included for horrors and globals.

# 17. Frozen Mod Appendix: DE 2.16 and Divinitus 1.15.3 DE

## 17.1 Ruleset boundary

The following material applies only when **Dominions Enhanced 2.16 loads first and Divinitus 1.15.3 DE loads second**. The files contain thousands of selected and new objects, including extensive nation-, unit-, event-, and Pretender-specific Blood mechanics. Those mechanics do not become universal rules merely because the mods are active.

## 17.2 Dominions Enhanced blessing edits

DE makes two direct Blood-related changes in its general blessing rewrite.

| Blessing | Vanilla 6.36 | DE 2.16 |
| --- | --- | --- |
| Berserker | N5 | N4 B1; non-Incarnate under the rewritten cost structure |
| Vampiric Weapons | B8 D4 | B6 D3; total requirement reduced from 12 to 9 |

These changes alter Pretender design opportunity cost. They do not change the hunting formula, ordinary Blood currency, or universal Sabbath arithmetic.

DE also adds nations, mages, heroes, and summons with Blood access. Those are roster facts and belong in the relevant nation dossier rather than in a universal Blood rule.

## 17.3 Divinitus power components

Divinitus adds many Pretender-specific Blood systems: priests gaining Blood, temple or sacrifice events, Blood Hunt riders, slave income, special summons, path teaching, and dominion-scaled effects. They are power components attached to particular gods and events.

One shared object worth identifying is the **Bowl of Blood**. It is an unforgeable Construction-11 divine item copied from the Brazen Vessel, grants +1 Blood, and casts the spell named Bowl of Blood. In the frozen file it is the starting item of the Devi of Darkness. It should not be listed as an ordinary forgeable vanilla booster.

The mod file also includes examples where Blood Sacrifice or Blood Hunt triggers an additional summon or resource event. Such effects sit on top of the ordinary order: the vanilla formula still describes the hunt unless the specific event or ability modifies its result.

## 17.4 Modded verification rule

For any combined-set Blood claim, resolve evidence in this order:

1. vanilla engine rule;
2. DE selected or new object;
3. Divinitus selected or new object loaded afterward;
4. event gates and hidden helper objects;
5. current in-game display and controlled reproduction.

Source comments are valuable design documentation, but executable commands and load-order resolution determine the object that enters play.

For technical reading, Blood is path number `8` and uses path mask `32768`. Thus `#magicskill 8 1` grants B1, `#magicboost 8 1` grants a +1 Blood boost, and `#gemprod 8 1` produces one blood slave. The distinction between path and school remains important: the site command `#bloodcost` discounts rituals in the Blood Magic research school, rather than serving as a generic test for every spell that happens to require the Blood path.

# Appendix A. Universal Blood Battle-Spells Index

The table reproduces the universal Blood-spell rows in the revision-2 manual. “Fat.” is listed fatigue; the ordinary 100-fatigue threshold determines primary-resource expenditure. Special tags are abbreviated only where they materially clarify targeting.

| Level | Spell | Path | Fat. | Principal role or table property |
| ---: | --- | --- | ---: | --- |
| 0 | Bleed | B1 | 100 | Armour-negating, MR-negates; excludes undead and inanimate targets |
| 1 | Blood Burst | B1 | 200 | Area-1 armour-negating damage; excludes undead and inanimate targets |
| 1 | Blood Heal | B1 | 100 | Large healing effect; excludes undead and inanimate targets |
| 1 | Sabbath Master | B1 | 100 | Joins as Sabbath master |
| 1 | Sabbath Slave | B1 | 100 | Joins as Sabbath slave |
| 1 | Reinvigoration | B1 | 100 | Major self-fatigue reduction |
| 1 | Summon Imps | B1 | 100 | Five temporary imps |
| 1 | Blood Boil | B1 F1 | 50 | Armour-negating, MR-negates; excludes undead and inanimate targets |
| 2 | Banish Demon | B1 | 100 | MR-negates demon banishment |
| 2 | Agony | B2 | 100 | Area fatigue/control; MR-negates; excludes undead and inanimate targets |
| 2 | Hell Power | B3 | 300 | Personal power effect with severe Blood character |
| 3 | Leeching Touch | B1 | 20 | Range-1 armour-negating life drain; excludes inanimate targets |
| 3 | Pain Transfer | B2 | 20 | Personal damage-transfer effect |
| 4 | Hellfire | B1 F2 | 100 | Area armour-piercing fire attack |
| 4 | Blood Lust | B2 | 100 | Battlefield-wide strength/ferocity support; excludes undead |
| 4 | Call Lesser Horror | B2 S2 | 200 | Calls a temporary Lesser Horror |
| 5 | Hellbind Heart | B2 | 100 | MR-negates mind control; excludes mindless targets |
| 5 | Summon Illearth | B2 E2 | 200 | Calls a temporary Illearth |
| 5 | Bloodletting | B4 | 400 | Battlefield-wide armour-negating bleeding pressure; MR-negates; excludes undead and inanimate targets |
| 6 | Soul Transaction | B1 G1 | 100 | MR-easy soul effect; excludes mindless targets |
| 6 | Harm | B2 | 100 | Area armour-negating harm; MR-negates; excludes inanimate targets |
| 6 | Blood Rain | B3 | 300 | Battlefield enchantment affecting morale and Blood conditions |
| 6 | Call Horror | B3 S3 | 300 | Calls a temporary Horror |
| 7 | Leech | B1 | 100 | Ranged area armour-negating life drain; excludes inanimate targets |
| 7 | Purify Blood | B4 N1 | 300 | Battlefield-wide Blood purification/support |
| 8 | Damage Reversal | B1 | 100 | Personal retaliatory damage effect |
| 8 | Rush of Strength | B3 | 100 | Battlefield-wide strength support |
| 8 | Life for a Life | B3 | 199 | Long-range armour-negating life exchange; excludes inanimate targets |
| 8 | Infernal Prison | B3 F1 | 200 | Armour-negating removal to Inferno |
| 8 | Claws of Kokytos | B3 W1 | 200 | Armour-negating removal to Kokytos |

# Appendix B. Universal Blood Summoning Rituals

All costs are blood slaves. The table lists universal manual entries; national Blood summons are additional.

| Level | Ritual | Path | Cost |
| ---: | --- | --- | ---: |
| 1 | Bind Shadow Imp | B1 | 4 |
| 1 | Bind Fiery Imps | B1 F1 | 5 |
| 2 | Bind Bone Fiends | B1 D1 | 5 |
| 2 | Bind Spine Devil | B2 | 2 |
| 2 | Bind Fiend | B2 | 3 |
| 3 | Bind Devil | B2 F2 | 5 |
| 3 | Bind Frost Fiend | B2 W2 | 7 |
| 4 | Bind Serpent Fiends | B1 | 4 |
| 4 | Bind Storm Demon | B2 A2 | 10 |
| 5 | Awaken Dark Vines | B1 N3 | 12 |
| 5 | Bind Demon Knight | B2 E2 | 15 |
| 5 | Send Lesser Horror | B3 S3 | 14 |
| 5 | Horde from Hell | B4 | 44 |
| 5 | Bind Succubus | B4 G1 | 66 |
| 5 | Bind Incubus | B4 G1 | 66 |
| 6 | Blood Rite | B2 D2 | 11 |
| 6 | Bind Ice Devil | B3 W3 | 88 |
| 6 | Ritual of Five Gates | B5 | 33 |
| 7 | Father Illearth | B3 E4 | 105 |
| 7 | Bind Arch Devil | B4 F2 | 99 |
| 7 | Plague of Locusts | B5 | 88 |
| 8 | Curse of Blood | B3 D4 | 96 |
| 8 | Bind Heliophagus | B5 | 111 |
| 9 | Send Horror | B4 S4 | 30 |
| 9 | Infernal Forces | B5 F2 | 50 |
| 9 | Infernal Tempest | B5 A2 | 50 |
| 9 | Forces of Ice | B5 W2 | 50 |
| 9 | Infernal Crusade | B5 E2 | 50 |
| 9 | Forces of Darkness | B6 | 50 |
| 9 | Bind Demon Lord | B8 | 150 |

# Appendix C. Universal Blood Utility and Attack Rituals

All costs are blood slaves. Global enchantments are separated in the next table.

| Level | Ritual | Path | Cost |
| ---: | --- | --- | ---: |
| 2 | Bowl of Blood | B1 | 5 |
| 3 | Cross Breeding | B1 N1 | 15 |
| 3 | Blood Feast | B2 | 5 |
| 3 | Infernal Circle | B5 | 5 |
| 4 | Blood Fecundity | B2 N2 | 10 |
| 4 | Hell Ride | B3 | 10 |
| 5 | Wrath of Pazuzu | B1 A3 | 15 |
| 5 | Rain of Toads | B3 N1 | 20 |
| 6 | Rejuvenate | B1 | 10 |
| 6 | Infernal Disease | B5 | 5 |
| 7 | Send Dream Horror | B3 S4 | 15 |
| 7 | Dome of Corruption | B4 S4 | 20 |
| 8 | Improved Cross Breeding | B2 N2 | 20 |
| 8 | Horror Seed | B3 S4 | 25 |
| 8 | Three Red Seconds | B5 | 120 |
| 9 | Infernal Fumes | B4 E3 | 40 |

| Level | Global enchantment | Path | Cost |
| ---: | --- | --- | ---: |
| 7 | Blood Moon | B7 S5 | 90 |
| 8 | Blood Vortex | B7 | 166 |
| 9 | Astral Corruption | B6 S6 | 166 |
| 9 | The Looming Hell | B8 | 150 |

# Appendix D. Source and Patch Ledger

## Official sources

1. Illwinter Game Design, *Dominions 6 Manual*, revision 2, especially orders and hosting sequence (pp. 51-57), magic and communions (pp. 73-80), dominion and Blood Sacrifice (pp. 82-85), magic items and path boosters (pp. 99-116), Blood spells and rituals (pp. 130-131, 141-216, and 217 onward).
2. Illwinter Game Design, [official *Dominions 6* documentation page and downloadable manual](https://www.illwinter.com/dom6/docs.html).
3. Illwinter Game Design, [official update announcements for versions 6.27-6.36](https://steamcommunity.com/app/2511500/announcements/).
4. Illwinter Game Design, [*Dominions 6 Modding Manual*](https://jaffa.illwinter.com/dom6/dom6modman.pdf).

## Current community reference

5. Illwiki, [“Dominions 6 Bless,” current Blood-effects table](https://illwiki.com/dom5/dom6/bless). This is used to identify the post-manual B3 requirement for Enchanted Blood and is kept distinct from official rules evidence.

## Frozen mod sources

6. *Dominions Enhanced 2.16*, source file `DomEnhanced2_16.dm`, read in load order before Divinitus.
7. *Divinitus 1.15.3 DE*, source file `Divinitus_1.15.3_DE.dm`, read as the later override layer.

## Relevant official patch notes

| Version | Blood-related clarification or fix |
| --- | --- |
| 6.27 | Added the `#enchantedblood` monster/item mod command; disease resistance began protecting against disease spells including Plague. |
| 6.29 | Temporary blood slaves no longer cause bleeding after gem longevity has occurred; communion backlash was fixed. |
| 6.31 | Fixed Looming Hell interaction with mounted units; regeneration became accurate to its percentage value. |
| 6.32 | Remote ritual casters killed by Blood Vengeance can no longer be looted by the enemy. |
| 6.35 | The MR bonus from Enchanted Blood is now printed in stat details. |
| 6.36 | Changing a blood sacrificer's items no longer removes the Blood Sacrifice order. |

# Conclusion

Blood magic rewards states that can govern a destructive industry. Its power does not begin with the first slave and does not end with the last ritual. It begins when population, mages, patrols, dominion, laboratories, transport, research, and security are made to serve one conversion plan.

The central discipline is to measure the whole chain. A profitable hunt that ruins a crucial recruitment centre can be a strategic loss. A costly empowerment that unlocks a decisive global can be a strategic bargain. A vast reserve that never reaches a battlefield or ritual is inert. A small, carefully allocated reserve can change a war.

Blood therefore belongs among the deepest systems in *Dominions 6*. It is economy, logistics, religion, battlefield engineering, remote warfare, and diplomacy at once. Mastery lies less in memorising a list of infernal spells than in knowing when the state can afford to turn its people into power, and how quickly that power must be spent before the machinery of extraction consumes the state that built it.
