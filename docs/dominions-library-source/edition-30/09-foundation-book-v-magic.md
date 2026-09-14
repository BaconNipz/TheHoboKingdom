# Foundation Book V: Magic

## What magic asks of a nation

Magic is the system by which Dominions turns knowledge into force. Research changes what a nation can attempt. Paths determine who can attempt it. Gems, blood slaves, laboratories, turns, and mage actions determine whether the attempt is affordable. Formation, timing, fatigue, targets, resistance, and counters determine whether it works.

> **Foundation rule:** Magic is not a list of powerful spells. It is a conversion chain from mage-turns and magical income into effects delivered at the right place and time.

Book V follows that chain from research and path access through gems, battlefield packages, communions, rituals, globals, forging, and late-game magic. It is meant to answer both the beginner's question—"What can this mage actually do?"—and the harder one: "Can the nation deliver that effect repeatedly, in time, and against resistance?"

## Edition note

Book I defines the common baseline and evidence labels. Book IV owns the arithmetic of battlefield resolution. Book V uses those results to deal with magical planning, while Book IX catalogues exact spell, item, site, and mage changes in the active mods.

## Current-version corrections that matter

The printed manual remains the structural baseline, but current play must include later official changes:

| Version | Current rule or correction | Practical consequence |
| --- | --- | --- |
| 6.25 | Battlefield-wide spells cannot normally be cast indoors; holy spells are excepted | Fort interiors and many assassination fields need separate scripts |
| 6.29 | Several spell, item, ritual, and nation-specific errors were corrected | Old object data must not be treated as current merely because the engine formula is unchanged |
| 6.30 | Communion masters using conservative gem use no longer attempt inappropriate higher-level spells | Old reports of this spell-AI failure are historical |
| 6.32 | Spell AI became less likely to cast invisibility late in battle; several remote and single-target choices were improved | Script fallbacks and unscripted casting should be assessed on the current version |
| 6.34 | Domes can protect against Astral Disruption; ritual messages and several spell-AI choices were corrected | Strategic magic defence and report interpretation changed |
| 6.35 | Innate spellcasters resume their scripts after recovering from unconsciousness | Current innate-caster scripts are more reliable than older replays imply |

Patch notes contain many object-specific balance changes. A current spell dossier needs current game data as well as the manual’s rule text. This foundation preserves the rules needed to make sense of those objects.

## Ways into the book

The shortest route runs through the conversion chain, paths and schools, research, gems, battlefield jobs, rituals, forging, and the first magic audit. Communions, domes, global contests, booster ladders, counter construction, and legendary spells can be added as the national game develops. The controlled tests are kept for questions that genuinely depend on hidden AI choices, rounding, or version-sensitive interactions.

# Part I: Magic as a Conversion System

## The complete chain

A magical effect normally depends on every link below:

```text
mage recruitment
-> laboratory access
-> mage-turns assigned to research
-> required school level
-> required path access
-> gems, slaves, or items
-> a legal order or battle script
-> survival, range, target, and timing
-> penetration, damage, or control
-> strategic exploitation
```

A broken link invalidates the rest. Researching a decisive spell without a caster is stored knowledge without delivery. Forging a booster without the path needed to wear it is dead capital. Sending the correct mage without gems can reduce a battle plan to ordinary AI casting. Winning the resistance check after the line has routed is too late.

## Six magical resources

Magic is paid for with more than gems:

| Resource | What it purchases | Common failure |
| --- | --- | --- |
| Research points | Access to schools and spells | Researching attractive levels with no operational deadline |
| Mage-turns | Research, rituals, forging, site searching, movement, and combat | Counting one mage as if all roles can be performed simultaneously |
| Paths | Eligibility, efficiency, range of effects, and forging access | Confusing national theoretical access with repeatable field access |
| Gems or slaves | Rituals, items, combat boosts, fatigue relief, and some summons | Treating the treasury as income rather than a finite stock |
| Laboratories | Research, rituals, forging, pooling, and logistics | Losing the network that turns sites and mages into national power |
| Time and position | Delivery before the strategic window closes | Finishing research after the war has already been decided |

The strongest magical economy is not always the one with the most gems. It is the one that can turn its available paths, researchers, laboratories, and stocks into the required effects with the fewest broken dependencies.

## Stock, flow, and capacity

The library’s economic model applies directly:

- **Stock:** current gems, slaves, forged items, accumulated research, and prepared casters.
- **Flow:** monthly gem income, blood-hunting output, research points, and repeatable summon production.
- **Capacity:** laboratories, mage recruitment, path distribution, forge access, communion bodies, and ritual range.
- **Position:** where mages, labs, gems, armies, and legal targets are located.

Research is cumulative stock generated by a flow of mage-turns. A booster is stored path access. A global is a large stock expenditure converted into an ongoing flow or worldwide rule. A battle gem converts stock into immediate tempo.

## The three horizons

Every research or forging decision belongs to a horizon:

| Horizon | Typical question | Planning standard |
| --- | --- | --- |
| Immediate | What can prevent defeat this turn or next? | Legal casters, carried gems, exact scripts, and battlefield timing |
| Campaign | What wins the next war or siege cycle? | Research breakpoint, item queue, summon mass, and lab movement |
| Strategic | What changes the nation’s path access or world position? | Boosters, globals, remote movement, legendary spells, and unique artifacts |

The common error is buying strategic possibility while losing the immediate war. The opposite error is repeatedly spending gems on emergency combat without building the research and access that end the emergency.

# Part II: Paths, Schools, and Access

## The nine paths

Dominions has nine ordinary paths of magical power:

| Family | Path | Broad tendencies |
| --- | --- | --- |
| Elemental | Fire | Heat, burning, direct damage, offensive enhancement, destructive globals |
| Elemental | Air | Lightning, storms, flight, precision, mobility, battlefield reach |
| Elemental | Water | Cold, quickness, underwater power, frost, fluid defence |
| Elemental | Earth | Protection, strength, fatigue control, constructs, forging |
| Sorcery | Astral | Resistance contests, communions, teleportation, information, global control |
| Sorcery | Death | Undead, decay, fear, souls, attrition, powerful summons |
| Sorcery | Nature | Life, poison, regeneration, animals, plants, supply, growth |
| Sorcery | Glamour | Illusion, false damage, concealment, bewilderment, perception |
| Neither | Blood | Blood slaves, sacrifice, demons, Sabbaths, corruption, high action cost |

This table describes tendencies, not hard borders. Schools are thematic rather than perfectly rigorous, national spells break general expectations, and multi-path requirements deliberately combine toolsets.

Holy is separate. Divine spells depend on Holy skill rather than ordinary paths and research. Common divine magic is available from the beginning. Some Banishment and Smite replacements are determined by the Pretender’s paths, as detailed in Book III.

## The seven schools

| School | Central study | Frequent output |
| --- | --- | --- |
| Conjuration | Bringing beings or powers into the world | Summons, elemental or otherworldly forces, some searches |
| Alteration | Changing physical properties and conditions | Protection, strength, resistance, weather, transformation |
| Evocation | Projecting magical force | Direct battle damage, area attacks, battlefield destruction |
| Construction | Making items and artificial beings | Equipment, boosters, matrices, constructs, artifacts |
| Enchantment | Imbuing units, objects, land, or the world | Persistent buffs, domes, globals, battlefield enchantments |
| Thaumaturgy | Manipulating minds, souls, information, and space | Resistance-based control, remote vision, movement, sorcery |
| Blood Magic | Unlocking spells that use Blood magic | Demons, Sabbaths, sacrifice, blood rituals, world corruption |

The Blood school is not the Blood path. The school is a research category; the path is a caster statistic. A spell can sit in Blood Magic and have multi-path requirements.

## The three access gates

A mage can cast a spell only when:

1. the nation has researched the spell’s school to the required level;
2. the mage meets every listed path requirement;
3. any required gems or blood slaves are available in the correct place.

Battle spells require carried resources before battle. Rituals draw automatically from the national treasury but require a friendly laboratory. Research level alone never grants a path to a mage.

## Primary and secondary paths

Multi-path spells require every listed path. The first listed path is the **primary path**:

- only excess skill in the primary path improves the ordinary spell-fatigue divisor;
- resistance penetration uses excess skill in the spell path identified by the rule;
- dual-path spells and rituals consume gems of the primary path unless the spell specifies otherwise;
- forging a multi-path item charges each required gem type.

This makes ordering consequential. Two requirements with the same numbers are not necessarily interchangeable if the primary path differs.

## Excess skill

Having more skill than the minimum can:

- reduce the listed fatigue cost;
- contribute to resistance penetration;
- increase the maximum gems usable in a ritual;
- enable stronger overcasting of a global;
- meet a higher item or spell threshold;
- improve path-derived indirect bonuses.

Higher skill gives more than access to extra icons. It increases endurance and sometimes contest strength. That value still needs to be weighed against the booster, communion, empowerment, or rare mage needed to reach it.

## Acquiring and increasing paths

The principal methods are:

| Method | New path from zero? | Duration | Main use |
| --- | ---: | --- | --- |
| Native or random path | Yes | Permanent | National base access |
| Empowerment | Yes | Permanent | Opening a missing path or climbing without another route |
| Path booster item | No | While worn | Efficient repeatable threshold access |
| Battlefield path-boost spell | No | Battle | Combat thresholds and fatigue reduction |
| One combat gem | No | One spell | Temporary +1 and/or fatigue management |
| Communion/Sabbath/Chorus | No | Battle | Shared battlefield escalation |
| Grand Communion | No | One strategic casting | Add same-path strength to a global or dispel |
| Transformation or special effect | Sometimes | Object-specific | Must be verified separately |

Only Empowerment is the general method that grants the first level of an absent path. A booster or Power of the Spheres requires at least level 1 already. A gem can raise a known path by one for one spell but cannot create it or raise it by more than one.

## Empowerment costs

Official costs are:

```text
first level in an absent path = 50 gems of that path
later increase = 15 x target level
```

Examples:

| Change | Cost |
| --- | ---: |
| F0 -> F1 | 50 Fire gems |
| F1 -> F2 | 30 Fire gems |
| F2 -> F3 | 45 Fire gems |
| F3 -> F4 | 60 Fire gems |

Empowerment is expensive because it buys permanent access on one commander. It is justified when the new level unlocks a repeatable ladder: a booster, critical ritual, national summon, global, or item that creates further access. Empowering for a one-off effect should be compared with alchemy, a communion, recruiting a rarer mage, trading for an item, or choosing a different solution.

## Indirect magic

Path knowledge grants side benefits:

| Path | Level 1 and scaling benefits | Level 3 | Level 4 |
| --- | --- | --- | --- |
| Fire | +10 Leadership and +10 Magic Leadership per level; shorter life | +5 Fire Resistance | another +5 Fire Resistance |
| Air | +10 Magic Leadership per level | +5 Shock Resistance | another +5 Shock Resistance |
| Water | +10 Magic Leadership per level | +5 Cold Resistance | another +5 Cold Resistance |
| Earth | +10 Magic Leadership per level | +3 natural Protection | +1 Affliction Resistance |
| Astral | +20 Magic Leadership per level | — | +1 Magic Resistance |
| Death | +50 Undead Leadership per level | rarely dies from old age | +10 Morale |
| Nature | +10 Magic Leadership and +10 supplies per level; longer life | +5 Poison Resistance | another +5 Poison Resistance |
| Glamour | +10 Magic Leadership per level | false-damage regeneration 1 per combat round | True Sight |
| Blood | +10 Undead and +10 Magic Leadership per level | +5 Hit Points | another +5 Hit Points |

Level-one benefits scale with the path level. Threshold benefits are cumulative. These effects can change command capacity, longevity, supplies, resistance, and survivability even when the mage never casts a spell from that path.

# Part III: Research as Strategic Planning

## The research formula

An ordinary magical researcher produces:

```text
Research = 5 + (2 x total magic levels) +/- research bonuses or penalties
minimum = 1
```

Magic and Drain scales modify magical research. Dementia halves research ability. The displayed value should be treated as authoritative for the current object after all abilities, scales, afflictions, items, and mod edits.

Some special researchers do not follow the ordinary path requirement:

- philosophers can research without magical paths, gain from Sloth, and ignore Magic and Drain;
- Divine Insights supplies limited research, but no more such researchers in one laboratory contribute than the dominion candles in that province;
- nation- and object-specific abilities can add or alter research.

## Research resolves early

Research is hosting step 2. A researcher contributes for the month even if killed later during hosting. This does not make exposed researchers safe; it means the current month’s points can survive a later raid while the future research flow does not.

## Research is a queue of responses

A weak plan says:

> “Research Evocation because the nation has Fire mages.”

A useful plan says:

> “Reach the precise area-damage spell before the first war, with enough F2 casters and carried gems to cast it after the line has engaged, while retaining an Alteration branch if the opponent fields fire resistance.”

Every breakpoint should record:

| Field | Question |
| --- | --- |
| Deadline | On which turn or war must the spell exist? |
| Caster | How many mages can cast it without rare randoms? |
| Resource | What does one battle, ritual cycle, or item batch cost? |
| Delivery | What range, timing, formation, lab, or ritual range is needed? |
| Counter | What common defence defeats it? |
| Branch | What is researched if scouting disproves the original threat? |
| Afterlife | Does the school level remain useful after the first purpose? |

## Breakpoints, not school completion

Research should be measured by useful breakpoints rather than equal bars. A school level can unlock:

- a defensive self-buff that makes thugs viable;
- an army-wide resistance answer;
- an efficient battlefield damage spell;
- a site-search ritual;
- a national summon;
- a path booster;
- a dome;
- a remote attack;
- a global;
- an artifact tier.

The next level is valuable only through the spells or items the nation can actually use. High school level does not imply high path requirement; low-path utility can appear late and high-path effects can appear earlier.

## Research portfolios

A robust research plan contains four functions:

1. **Immediate survival:** expansion, early war, resistance, protection, or fatigue tools.
2. **Efficient repetition:** spells many recruitable mages can cast.
3. **Access development:** boosters, summons, or rituals that widen the path graph.
4. **Strategic leverage:** movement, remote warfare, globals, artifacts, and legendary effects.

Overconcentration creates brittle excellence. Excessive breadth creates many half-finished answers. The correct portfolio is shaped by national mage distribution and the next opponent, not by a universal school order.

## Research efficiency

Useful measures include:

```text
RP per gold = monthly research / recruitment gold
RP per upkeep = monthly research / monthly upkeep
breakpoint time = remaining RP / current monthly RP
field opportunity cost = RP lost when researchers leave laboratories
```

These ratios answer different questions. Cheap research may have poor commander-point efficiency. A high-RP capital mage may be needed for battlefield duty. A sacred researcher may have low upkeep. A foreign or summoned mage may open a path worth far more than its raw RP.

## Mage-turn accounting

One mage can normally perform only one monthly strategic job:

- research;
- forge;
- cast a ritual;
- empower;
- search manually;
- move;
- preach or perform another order;
- accompany an army.

The full cost of a ritual is:

```text
gem or slave cost
+ one mage-turn
+ foregone alternative output
+ position and exposure
```

A “free” summon paid only in gems still consumes a caster’s month. A cheap item can be expensive if the only qualified mage is the nation’s research engine or unique global caster.

## Legendary research

Level 9 of every school except Construction consists of legendary spells. Reaching level 9 does not automatically grant the entire level:

- one legendary spell is selected and researched at a time;
- the level can be researched repeatedly to learn additional legendary spells;
- the default limited-legendary setting restricts how quickly this catalogue is acquired;
- Construction 9 instead unlocks unique artifacts.

The decision is spell-specific. “Reach Thaumaturgy 9” is incomplete; the plan must name the first legendary spell, the caster and gems that make it real, and the reason its effect is worth delaying every other branch.

## Research audit

At the start of a major plan:

1. list the next two wars and likely counters;
2. identify exact spell breakpoints;
3. count common, uncommon, and unique casters;
4. reserve the gems required for one decisive battle;
5. identify the item or summon ladder that changes access;
6. estimate turns to the breakpoint after fielding losses;
7. name the branch if the opponent changes plan;
8. avoid counting a Pretender or unique mage in two distant places.

# Part IV: Gems, Slaves, and Magical Logistics

## Gem production

Magic sites send gems to the national treasury when their province is connected through friendly territory to a province with a laboratory. Ownership alone is not enough. Raiding, isolation, or laboratory loss can interrupt collection without destroying the site.

The treasury records both current stock and monthly income. These must not be confused:

- **income** supports a sustainable rate;
- **stock** allows bursts, emergency defence, globals, artifacts, and path development;
- **committed stock** is already promised to a forge queue, ritual, or field army even if still visible in the total.

## Blood slaves

Blood has no ordinary gem. Blood slaves are acquired principally through Blood Hunting and are physical units/resources that must be moved and pooled. Their economy includes:

- gold and commander points for hunters;
- unrest and population damage;
- patrol or tax consequences;
- laboratory and transport logistics;
- the opportunity cost of hunter mage-turns;
- battlefield and ritual consumption.

The correct comparison is not “slaves are free.” It is the total provincial and organisational cost per useful blood effect. Book II gives the hunting and unrest foundation; this book treats the magical expenditure.

## Pooling and distribution

The pool command gathers gems carried by commanders in a laboratory province into the national treasury. Direct transfer equips field mages. A reliable monthly process is:

1. pool slaves and unused gems at laboratories;
2. reserve strategic stocks;
3. issue ritual and forge orders;
4. assign exact battle loads;
5. leave an explicit contingency reserve;
6. check that moving armies carry neither too few nor treasury-sized excesses.

Carried gems are exposed to battle loss and may be unavailable to rituals. Treasury gems cannot help a mage in battle unless transferred before combat.

## Combat gem rules

A mage may use gems in combat to:

- raise a known path by one for one spell;
- reduce a spell’s fatigue;
- satisfy a spell’s gem requirement.

Limits:

- a mage cannot spend more gems in one combat turn than the current skill in that path;
- gems cannot grant the first level of an absent path;
- gem use cannot increase the path by more than one;
- the computer controls optional fatigue spending;
- conservative gem use makes the mage spend sparingly and on scripted spells only.

“How many gems does the spell cost?” is only the beginning. The full question is:

```text
required spell gems
+ any path-boost gem
+ optional fatigue gems selected by the AI
<= gems legally spendable this combat turn
```

Because current skill is part of the spending limit, a battlefield boost or communion may change what can be spent. Exact spell-AI decisions remain object- and situation-sensitive.

## What the patch history proves about optional spending

Official corrections place firm limits on any exact table inherited from early reverse-engineering:

| Version | Official correction | Consequence |
| --- | --- | --- |
| 6.12 | Gems are no longer used when the mage is targeted by a remote attack ritual. | Remote-attack replays do not establish ordinary battle spending. |
| 6.15 | Communions sometimes used too many gems to reduce fatigue. | Older communion-spending thresholds are not current law. |
| 6.30 | Communion masters on conservative gem use sometimes failed to try higher-level spells. | Conservative behaviour must be tested on 6.30 or later. |

A pre-release code investigation reported several concrete decision thresholds: conservative casters reacted near 100 projected fatigue and a 30-fatigue addition; ordinary casters used lower 85 and 20 checks, had further 25/40 fatigue-per-divisor tests, and attempted to retain three gems. Those values are valuable test inputs because they predict distinct outcomes. They are not printed here as the current algorithm: the official 6.15 correction establishes that at least part of the old communion-gem behaviour changed after that investigation.

The safe rule for play is narrower. Carry the scripted minimum, allow for optional fatigue control, and reproduce a critical refusal boundary in the current version before building a battle plan around it.

## A battle-gem budget

For each mage, record:

| Field | Meaning |
| --- | --- |
| Scripted minimum | Resources required to execute the intended five orders |
| Likely AI spend | Additional gems that may be used to control fatigue |
| Emergency reserve | Gems retained for later rounds or a second battle |
| Capture exposure | Maximum acceptable value if the army is destroyed |
| Conservative setting | Whether unscripted or optional spending is restricted |

Underloading produces failed scripts. Overloading converts a rout into a treasury loss. The right load depends on the value of the battle, expected duration, retreat route, and likelihood of a second engagement before resupply.

## Gems as fatigue control

Many combat gems are spent not to meet the printed requirement but to keep the caster conscious. This can be decisive because fatigue changes:

- whether later scripted spells are attempted;
- the risk of unconsciousness;
- communion-slave survival;
- vulnerability to critical and armour-defeating hits;
- the number of useful casts before collapse.

The effect should be valued in additional useful actions, not only fatigue removed. A gem that permits the decisive fourth cast may be more valuable than one that merely makes an already won battle cleaner.

## Alchemy

Any magically skilled commander in a friendly laboratory can use the Alchemy order:

```text
2 non-Astral gems -> 1 Astral pearl
2 Astral pearls -> 1 gem of another type
```

Converting one non-Astral type to another through pearls is effectively 4:1. This is a severe exchange rate. It is rational when the receiving gem crosses a binding threshold: a decisive ritual, booster, dome, global, or emergency defence.

The ordinary conversion should not be confused with alchemical spells that convert gems into gold. The Modding Manual’s Alchemy Bonus ability applies to the latter category, not automatically to the treasury’s pearl conversion.

## Gem valuation

The value of a gem depends on access and timing:

```text
strategic gem value
= effect unlocked
x probability of timely delivery
x scarcity of substitutes
- opportunity cost
```

A Nature gem may be common nationally but priceless at the exact army that needs a resistance spell. Astral pearls are flexible but are also consumed by communions, teleportation, dispels, and powerful late rituals. A surplus path can fund a repeatable summon; an apparent shortage may be caused by idle forge queues rather than low income.

## Reserve doctrine

Useful reserve categories are:

- **battle reserve:** one or more decisive engagements;
- **counter reserve:** domes, dispels, emergency movement, or resistance;
- **access reserve:** empowerment or a booster chain;
- **strategic reserve:** a named global, artifact, or legendary ritual;
- **trade reserve:** gems whose diplomatic value exceeds immediate conversion.

An unlabelled treasury is easily spent twice in planning.

# Part V: The Anatomy of Battle Magic

## Spell classes by battlefield job

A battle-magic package normally combines several jobs:

| Job | Desired effect |
| --- | --- |
| Preparation | Path boosts, personal defence, reinvigoration, or communion formation |
| Protection | Resistances, armour, Luck, regeneration, mist, concealment, or anti-magic |
| Control | Immobilisation, confusion, sleep, fear, fatigue, displacement, or terrain conditions |
| Attrition | Repeated efficient damage or summons |
| Breakthrough | Large area, armour-negating, high-penetration, or battlefield-wide effect |
| Sustain | Fatigue relief, healing, replacement bodies, or continuous enchantment |
| Counter | Removal or neutralisation of the enemy’s named mechanism |
| Preservation | Escape, protection of commanders, or reduced gem exposure |

No spell is “good” independently of delivery. A superb damage effect at the wrong range or damage type is a poor answer. A minor resistance buff applied before the relevant area attack can decide the battle.

## The battle-resolution boundary

Book IV is the authoritative home for preparation, interruption, spell accuracy, Magic Resistance contests, casting fatigue, damage families, and the lifetime of battlefield enchantments. Reprinting those formulas here created two places that could drift after a patch.

For magical planning, the essential questions are:

1. Can the caster complete preparation before contact or interruption?
2. Will the spell reach the intended target at an acceptable risk to friendly troops?
3. Which defensive layer does it test: Protection, resistance, Magic Resistance, fatigue, morale, or position?
4. Can the caster afford the fatigue and repeat the effect?
5. Does the plan still work indoors or under a different battlefield condition?
6. Is the caster's survival part of maintaining the effect?

The exact arithmetic and current patch corrections are in Book IV, Part XIV. This chapter uses their result to build the package.

## Scripting and spell AI

A five-order script is a preferred sequence, not complete control. A scripted spell may fail because:

- research or a path was misread;
- the required resource is absent;
- range or target is illegal;
- fatigue is too high;
- the caster was interrupted, stunned, or unconscious;
- the battlefield condition is wrong;
- a target no longer exists;
- the spell AI chooses a fallback after the script.

Robust scripts name their failure branches. If the critical buff is skipped, can the army still survive? If an enemy resistance appears, what does the mage cast after order five? If communion slaves drop below a threshold, which masters become illegal or exhausted?

## Battlefield package worksheet

| Layer | Question |
| --- | --- |
| Threat | What exact damage, control, or defence must be answered? |
| Preparation | Which boosts and communion orders occur first? |
| Screen | What buys the required casting time? |
| Main effect | Which repeated spell performs most work? |
| Breakthrough | Which spell changes the battle state? |
| Sustain | How are fatigue and losses controlled? |
| Counter-counter | What happens against resistance, antimagic, flyers, or assassins? |
| Gem budget | What is the cost per expected battle and per war? |
| Retreat | Which casters and gems survive a failed plan? |

# Part VI: The Nine Paths in Practice

## How to read a path

Each path should be evaluated through six questions:

1. What protection does it create?
2. What defence does it attack?
3. How does it control movement, fatigue, or cohesion?
4. What does it summon or forge?
5. How does it project power on the map?
6. Which other path covers its principal failure?

The summaries below are functional maps, not spell lists. National spells and the active mods can substantially alter them.

## Fire

Fire commonly converts research and gems into immediate destructive tempo:

- direct and area fire damage;
- burning and Heat;
- offensive weapon or strength enhancement;
- Fire Resistance;
- battlefield-wide destructive conditions;
- gem-to-gold alchemy;
- late world effects tied to fire and heat.

Fire’s strengths are efficient damage against dense, insufficiently resistant armies and the ability to turn an ordinary line into a more lethal one. Its weaknesses are resistance, friendly fire, fatigue, limited control, and the possibility that high damage is wasted on dispersed or expendable targets.

Fire packages need:

- a reason targets will remain clustered;
- screening or range;
- a non-fire answer;
- protection from their own area effects;
- a gem budget for high-impact casts.

## Air

Air commonly supplies:

- armour-negating shock damage;
- precision and ranged support;
- storms and anti-flight conditions;
- flight and strategic mobility;
- concealment, mist, or displacement;
- strong remote reach.

Shock damage attacks a different defensive layer from ordinary physical damage. Storms can define the whole battlefield, but may also obstruct friendly flyers, missile plans, or spell requirements. Air mages are often high-value because the path combines battlefield damage with movement and information.

Air planning must distinguish:

- storm-compatible and storm-dependent effects;
- friendly flying requirements;
- shock-resistant targets;
- whether strategic movement resolves into a magic battle or later ordinary battle;
- whether a remote effect is blocked by a dome.

## Water

Water commonly provides:

- Cold Resistance and cold damage;
- quickness and action-tempo changes;
- defence and fluid physical alteration;
- water-elemental and aquatic tools;
- underwater access;
- frost-based battlefield control.

Quickness multiplies both output and fatigue exposure. Cold effects are strongest when resistance and friendly exposure are managed. Water’s ability to operate underwater can be strategically decisive because many ordinary armies and rituals have restrictions there.

Water packages should audit:

- fatigue after additional actions;
- friendly cold resistance;
- underwater legality;
- the difference between temporary battle acceleration and monthly map movement;
- whether the target’s high Protection matters to the chosen cold effect.

## Earth

Earth commonly supplies:

- Protection and natural armour;
- strength and physical enhancement;
- reinvigoration and fatigue control;
- armour damage or earth control;
- constructs and siege power;
- many foundational forging tools.

Earth often wins indirectly by making an army’s existing bodies harder, stronger, and more sustainable. It is also central to path escalation because Construction and Earth forging frequently create the infrastructure for other schools.

Earth packages fail when:

- armour-negating or resistance-based effects bypass the added Protection;
- heavy armour raises casting encumbrance;
- slow preparation loses to early contact;
- transformed or buffed units still lack delivery;
- a forging plan consumes the only field-capable Earth mages.

## Astral

Astral commonly provides:

- communions;
- Magic Resistance contests and penetration;
- antimagic and resistance support;
- teleportation and remote projection;
- information and detection;
- global control, dispels, and late strategic effects.

Astral’s central advantage is leverage: many modest mages can combine, and high Astral can contest units or globals through exact arithmetic. Its central danger is that the same infrastructure can be fragile. Communion slaves can collapse; high-value casters can be exposed; Astral duels or hostile soul effects can punish path-heavy mages.

Astral planning requires:

- MR and penetration estimates;
- slave and master path ratios;
- pearl supply;
- protection of communion infrastructure;
- a clear distinction between battlefield communions and Grand Communion orders.

## Death

Death commonly supplies:

- undead creation and command;
- skeleton-based battlefield attrition;
- fear, decay, disease, and fatigue;
- soul and death effects;
- powerful summons and transformed commanders;
- late rituals involving the dead and Titans.

Death can convert gems into bodies without ordinary upkeep assumptions, but those bodies may be Mindless, vulnerable to Banishment, or dependent on Undead Leadership. Reanimation and battlefield summoning can absorb time while decisive casters work.

Death packages should audit:

- priestly counters;
- Undead Leadership;
- battlefield turn limits;
- friendly morale and disease exposure;
- whether summoned bodies are an objective or only a screen;
- the risk profile of late summons whose minds or forms are uncertain.

## Nature

Nature commonly supplies:

- regeneration, healing, and life enhancement;
- poison resistance and poison offence;
- entanglement and movement control;
- animals, plants, and living summons;
- supplies and longevity;
- growth- and dominion-linked world effects.

Nature often creates persistence rather than immediate lethality. Regeneration is strongest on sufficiently large and protected bodies; it is not a substitute for surviving the initial hit. Poison plans require protection for friendly units and enough battle duration for delayed damage to matter.

Nature packages should distinguish:

- healing from affliction removal;
- regeneration from one-time healing;
- supply generation from battlefield value;
- poison damage from immediate rout pressure;
- living summons from mindless or undead logistics.

## Glamour

Glamour commonly supplies:

- illusions and false damage;
- concealment and misdirection;
- confusion, bewilderment, and perception attacks;
- defence through appearance rather than armour;
- remote or strategic deception;
- True Sight at high indirect path skill.

False damage can disable or rout without ordinary wounds, but it interacts differently with false-damage regeneration and True Sight. Glamour defence can be powerful until the opponent brings the correct perception or wide-area answer.

Glamour packages need:

- an answer to True Sight;
- a plan for Mindless or otherwise inappropriate targets;
- real damage or control when illusion is insufficient;
- awareness that late-battle spell AI and current patches affect invisibility choices;
- protection against area effects that do not care which apparent body is real.

## Blood

Blood commonly supplies:

- demons and blood summons;
- Sabbaths;
- sacrifice and dominion interaction;
- severe single-target or battlefield effects;
- horror and corruption mechanics;
- world enchantments that punish ordinary magic.

Blood converts provincial population, unrest tolerance, patrols, hunters, laboratories, and transport into a magical economy. Its scale can be enormous, but its logistics are unusually visible and disruptive.

Blood packages should audit:

- slaves at the caster rather than only in the treasury;
- hunter, patrol, and laboratory capacity;
- Sabbath fatigue modifiers;
- living-only or underwater restrictions;
- enemy raids on hunting provinces;
- whether blood investment is delaying conventional research and defence.

## Cross-path architecture

Paths become more useful when paired by function:

| Need | First layer | Complementary layer |
| --- | --- | --- |
| Armoured mass | Fire, Air, Death, or resistance-based attack | Earth or Nature screen |
| High MR elites | Physical or elemental pressure | Astral penetration only where efficient |
| Dense low-resistance army | Area elemental damage | Control that holds density |
| Fast rush | Early protection and control | Later breakthrough damage |
| Long attrition | Death or summons | Nature/Earth sustain and fatigue control |
| Remote threat | Air/Astral/Glamour movement or attack | Domes, scouts, and local response |
| Global war | Astral dispel and high ritual strength | Gem income, caster security, diplomacy |

The purpose of a secondary path is not variety. It is to cover the principal failure of the first mechanism.

# Part VII: Communions, Sabbaths, Choruses, and Grand Communions

## What a battlefield communion does

A communion combines mages during battle to:

- raise every master’s already-known paths;
- distribute each master’s spell fatigue among that master and all friendly slaves;
- pass certain personal buffs from masters to slaves;
- concentrate the actions of many mages into stronger casting.

A valid communion requires at least one master effect and one slave effect. Astral uses Communion Master and Communion Slave. Blood uses Sabbath Master and Sabbath Slave. MA Man’s Spellsingers can use Chorus Master and Chorus Slave.

These are separate communion types. One Astral Communion, one Sabbath, and one Chorus may coexist, each with its own masters, slaves, and bonuses. An Astral master does not gain the slaves of a simultaneous Sabbath.

## The level bonus

A master gains `n` levels in every path the master already knows when the communion has at least `2^n` slaves:

| Active slaves | Master bonus |
| ---: | ---: |
| 1 | +0 |
| 2-3 | +1 |
| 4-7 | +2 |
| 8-15 | +3 |
| 16-31 | +4 |
| 32-63 | +5 |
| 64-127 | +6 |

The first slave makes the communion valid but grants no level. Bonus levels do not create an absent path. If slave casualties reduce the total below a threshold, every master’s bonus drops immediately.

The threshold structure makes “spare” slaves strategically useful. Four slaves produce +2, but the loss or unconsciousness of one reduces the group to three and +1. Five or six retain +2 after some attrition.

## Participants in one spell

For a single master’s spell, participants are:

- the master casting that spell;
- all friendly slaves in that communion.

Other masters are not participants in that cast. They gain the path bonus, but they do not share another master’s fatigue as participants.

If there are four slaves and three masters, a spell cast by one master has five participants, not eight. Each master’s separate spell creates its own fatigue event over that master plus the same slave pool.

## Base fatigue distribution

For one master’s spell:

```text
base fatigue per participant
= spell fatigue after path calculations
/ number of participants
```

The slave’s share is then modified by the slave’s skill relative to the casting master in the relevant path:

| Slave path relative to master | Slave fatigue modifier |
| --- | ---: |
| higher than master | x 0.5 |
| equal to master | x 1 |
| lower, but at least half the master | x 2 |
| lower than half the master | x 4 |

Skill gained from the communion and all other sources is included when calculating spell fatigue. Exact rounding at each step is assigned to controlled testing.

## Worked comparison

Suppose one master and four slaves participate, so the divisor is five.

If the resolved spell fatigue before distribution is 100:

```text
base participant share = 100 / 5 = 20
```

The caster receives the master share according to the communion rules. Each slave then receives:

| Relative skill | Fatigue per slave before type-specific modifiers |
| --- | ---: |
| Slave higher | 10 |
| Equal | 20 |
| Lower but at least half | 40 |
| Lower than half | 80 |

Four weak slaves do not automatically make high-path casting safe. The path bonus can raise the master far above the slaves, turning the x4 bracket into the dominant risk.

## Master count and slave load

Adding masters increases output but not the number of participants in each cast. If two masters cast 100-fatigue spells into the same four equal-path slaves:

- each event has five participants;
- each slave receives a share from the first cast;
- each slave receives another share from the second cast;
- total slave load approximately doubles.

The correct design ratio depends on:

- master casting frequency;
- spell fatigue after boosted skill;
- slave path relation;
- slave encumbrance and reinvigoration;
- buffs transmitted to slaves;
- expected battle length;
- whether slaves leave at unconsciousness;
- how many threshold casualties can be tolerated.

“Four slaves per master” is not an engine rule.

## Slaves cannot act

While in the communion, slaves perform no independent actions. Their mage-turn in the battle is converted into:

- master path access;
- fatigue capacity;
- receipt of qualifying self-buffs;
- risk.

A slave’s opportunity cost includes the spells that mage could otherwise have cast. High-path slaves may be safer fatigue sinks, but they can be too valuable to immobilise.

## Shared personal buffs

Slaves benefit from self-buffs cast by communion masters when those spells are single-target, range 0 personal effects. This can create powerful shared protection, resistance, regeneration, reinvigoration, or other effects.

The important details are:

- the buff is produced by the particular master’s cast;
- legal qualifying effects must be checked from current spell data;
- timing matters—slaves may already have received fatigue before the protection arrives;
- some buffs can be harmful to particular slave bodies;
- a master’s personal path access and script determine what is transmitted.

Communion buffing is an army-design problem, not an arithmetic trick. Slave chassis, resistances, and encumbrance must suit the intended shared effects.

## Collapse

The communion ends when no masters or no slaves remain.

If all masters die or flee, every slave suffers:

- approximately one combat round of stun;
- `3d50` fatigue damage.

This backlash can disable or kill an already exhausted slave block. Keeping the masters alive is part of keeping the slaves alive. Redundant masters can prevent sudden collapse, but every additional active master can also increase fatigue throughput.

The current patch boundary matters. Version 6.12 made removal from a communion clear the slave spell effect, and 6.29 corrected cases where communion backlash failed to occur. A replay from before those fixes cannot settle present collapse behaviour.

## Automatic participation

Items such as matrices, Slave’s Hearts, and Master’s Athames can make bearers join automatically. The bearer:

- must be a mage, meaning at least one non-Holy magic path;
- need not have Astral or Blood;
- must still be analysed for item slot, cost, timing, and survivability.

Automatic participation can bring foreign paths into a communion without spending the first scripted round joining. It also creates fragile item dependencies and may expose expensive gear to battlefield loss.

## Current communion correction ledger

| Version | Official change | What to retest |
| --- | --- | --- |
| 6.12 | Being thrown out removes the communion-slave effect. | Forced removal, form changes, and automatic slave items. |
| 6.15 | Excessive gem use for fatigue reduction was corrected. | Gem budgets for high-throughput master groups. |
| 6.23 | Spell AI confusion between different communion types was corrected. | Mixed Communion, Sabbath, and Chorus battles. |
| 6.29 | Missing communion backlash was corrected. | Last-master death, flight, and forced removal. |
| 6.30 | Conservative communion masters again try eligible higher-level spells. | Conservative scripts across a slave threshold. |

The manual already settles the ordinary shared-buff rule: a single-target range-0 personal spell cast by a master can affect that master's slaves. An area-one spell centred on the caster is not the same category merely because it covers the caster's square. Automatic items on non-Astral mages, multi-form commanders, and forced participant removal remain current test work.

## The three battlefield types

| Type | Special rule |
| --- | --- |
| Communion | Spells take 25% longer to cast |
| Sabbath | Master suffers half fatigue; slaves suffer 20% extra fatigue |
| Chorus | Spells take 25% longer; a slave leaves on losing consciousness |

The Sabbath improves master endurance by transferring a harsher burden to slaves. Chorus slaves avoid later damage once unconscious, but every departure can reduce the master’s path bonus immediately.

## Designing a safe communion

Proceed in this order:

1. name the highest-path spell each master must cast;
2. calculate master path after the intended slave threshold;
3. estimate spell fatigue at that path;
4. count participants for each cast;
5. place each slave in the relative-path multiplier bracket;
6. add type-specific Sabbath or casting-time effects;
7. estimate simultaneous master throughput;
8. include transmitted buffs and reinvigoration;
9. provide threshold redundancy;
10. protect masters from assassination, flyers, missiles, and early area damage;
11. write a useful plan for masters after the scripted sequence;
12. decide what a controlled collapse looks like.

## Common communion failures

### The threshold cliff

Exactly four slaves produce +2. One casualty produces only +1, invalidating later spells or sharply raising fatigue.

### Weak-slave multiplication

Masters rise several path levels while slaves remain far below half the master. Every cast sends four times the base share to each weak slave.

### Too many masters

The slave pool receives overlapping fatigue from many masters. The communion appears efficient because every master has high paths, then the shared battery collapses at once.

### Harmful self-buffs

A master distributes an effect incompatible with slave physiology, resistance, or role.

### Preparation without contact timing

The army needs several rounds to join, boost, and buff, but the enemy reaches the mages before the package activates.

### No post-script policy

Masters complete five orders and begin casting high-fatigue or inappropriate spells into the same slave pool.

### Master annihilation

All masters are placed together and die to one flanking or area effect, causing backlash.

## Grand Communions are different

Grand Communion is a strategic monthly order used by certain nations. When one eligible mage casts or dispels a global, other eligible mages in the same context can use Grand Communion to add their relevant path skill to the power of the attempt.

It does not:

- create a battlefield communion;
- distribute battlefield fatigue;
- grant every path;
- make participating mages available for research or other orders that month.

For a Dispel, joining Astral skill adds directly to the attempt described by the manual’s example. Grand Communions let a nation convert several mage-turns into ritual contest strength.

## Communion audit

Before a battle:

- identify communion type;
- count slaves at every threshold;
- record each master’s boosted paths;
- calculate every critical spell’s participants and slave brackets;
- check shared self-buffs;
- set gem policy;
- separate or protect masters;
- decide how slaves recover;
- plan for one slave loss, one master loss, and early contact;
- test the exact package in the current ruleset.

# Part VIII: Rituals and Strategic Magic

## Ritual fundamentals

Rituals are map spells that take one entire monthly order. They normally require:

- a friendly laboratory;
- the researched school level;
- a caster with all required paths;
- sufficient gems or slaves in the national treasury;
- a legal target and range.

The treasury supplies ritual gems automatically. A field commander carrying gems elsewhere does not increase the national pool.

## Hosting position

Important magic timing from the official hosting sequence:

| Step | Resolution |
| ---: | --- |
| 2 | Research |
| 4 | Empowerment |
| 5 | Forging |
| 10 | Magic rituals, in random caster order |
| 11 | Remote army attacks |
| 12 | Magic battles, including relevant teleports and movement |
| 14 | Site-search ritual results |
| 28 | Global enchantments take effect on the world |
| 31 | Item and monster special effects |
| 62 | Artifacts may become yearning |

This timing has strategic consequences:

- current research can unlock knowledge before later events, but orders were submitted with the pre-host state;
- forging and empowerment complete before ordinary rituals;
- remote attacks and magic movement can precede ordinary movement battles;
- a global is cast at the ritual step but its world effect begins at step 28;
- a new global does not retroactively change movement battles or storming that already resolved in the same host;
- yearning occurs near the end of the turn.

## Ritual order is random

Rituals at step 10 resolve in random caster order across relevant mages. Plans that require ritual A to precede ritual B in the same month are unsafe unless the engine or objects provide a specific guarantee.

This affects:

- opening and using gateways;
- competing globals;
- sequential remote attacks;
- global-slot contests;
- casting a protection before a hostile action;
- using a summon as a same-turn caster.

## Range and legality

Ritual range is measured in provinces where shown. No listed range normally means a local ritual. Markers include:

- **NUW:** cannot be cast underwater;
- **UW:** can be cast only underwater.

Ritual-range abilities and sites can change reach. Range should be measured from the actual casting laboratory after movement orders, not from the capital or army being supported.

## Local enchantments

Local enchantments affect a province and may persist. Many are linked to their caster:

- caster death ends the effect;
- most also end when the province is conquered;
- limited-duration enchantments can often be extended with extra gems;
- most gain one month per extra gem, while some gain three.

The shortcut `Shift+M` repeats a ritual monthly while the caster remains eligible and resources exist. Repetition is operationally convenient but can drain a treasury silently if the strategic need changes.

## Anonymous and limited rituals

Some rituals are:

- **Anonymous:** caster or origin information is concealed by the effect’s reporting rules;
- **Limited:** only one instance can affect the target province.

Anonymous is not synonymous with undetectable. Scouting, diplomatic inference, target selection, and repeated patterns can still reveal responsibility.

## Ritual categories

| Category | Strategic use | Main counter |
| --- | --- | --- |
| Site search | Convert map ownership into gem income or special access | Raiding, lab isolation, opportunity cost |
| Summon | Convert gems and a mage-turn into units or commanders | Banishment, resistance, upkeep or leadership limits |
| Remote attack | Damage or invade a distant province | Domes, defence, decoys, retaliation |
| Magic movement | Relocate forces outside ordinary movement | Domes, traps, interception, wrong timing |
| Information | Reveal provinces, armies, sites, or magic | Concealment, misinformation, opportunity cost |
| Local enchantment | Protect or transform one province | Dispel, conquest, caster assassination |
| Economy | Produce gems, gold, units, scales, or other flow | Caster loss, global contest, raids |
| Global | Change rules across the world | Dispel, replacement, assassination, dominion pressure |

## Site-search rituals

Remote searches can:

- cover territory faster than manual movement;
- search dangerous provinces without exposing a mage;
- use otherwise idle path access;
- convert gems into future income.

They are investments, not automatic profit. The expected return depends on site frequency, province type, previous searches, ritual cost, and time remaining. A search that pays back in ten turns can be poor during an existential war and excellent during stable expansion.

## Summoning

A summon should be valued by role:

| Summon output | Main value |
| --- | --- |
| Combat bodies | Frontage, attrition, special attack, resistance, or siege |
| Commander | New path, leadership, forging, ritual, or thug chassis |
| Sacred unit | Bless interaction and Holy Point independence where applicable |
| Undead or demon | Different upkeep and leadership system, specific counters |
| Elemental or temporary force | Immediate battlefield conversion |

The cost includes the summoner’s month. A mediocre combat unit can be a great summon if it opens a path, commands a new troop family, or relieves a commander-point bottleneck.

## Remote attacks

Remote attacks resolve before ordinary movement battles. Their purposes include:

- stripping Province Defence;
- killing commanders or laboratories;
- testing a dome;
- exhausting defenders;
- cutting retreat routes;
- creating a magic battle before the main invasion;
- forcing the enemy to distribute defence.

A remote attack should be coordinated with the ordinary campaign. Damage without exploitation may only warn the target. Repeated attacks can also disclose path access and spending.

## Magic movement

Teleportation and related movement create unusual timing. A movement ritual may produce a magic battle at step 12, before ordinary army movement. The arriving force must be self-contained:

- correct leadership;
- gems and slaves;
- a legal survival or retreat plan;
- enough force if the target is stronger than intelligence suggested;
- awareness of domes and redirection.

Strategic mobility is valuable because it compresses distance, but it can also separate mages from laboratories, armies, and friendly retreat provinces.

## Repeat-ritual discipline

For every repeated ritual, record:

- monthly cost;
- assigned caster;
- cancellation condition;
- minimum reserve;
- target rotation;
- lab and range requirement;
- whether a new patch or mod changes the object.

Automation should preserve judgment, not replace it.

# Part IX: Domes and Remote-Magic Defence

## What a dome protects

Domes are local enchantments that interact with hostile ritual effects targeting the province. Their exact chance and consequence are object-specific. Some block, some redirect, and some retaliate.

They do not replace:

- scouts and intelligence;
- conventional defenders;
- protection against assassination;
- laboratory redundancy;
- dispersal of unique casters;
- diplomatic deterrence.

## Major manual examples

| Dome | Listed behaviour in the manual | Friendly-magic consequence |
| --- | --- | --- |
| Dome of Solid Air | 80% protection; destroyed when it fails | Blocks friendly targeted magic as well |
| Frost Dome | 30% protection and a cold trap | Blocks friendly targeted magic as well |
| Forest Dome | 30%; absorbed fire destroys it | Blocks friendly targeted magic as well |
| Dome of Misdirection | 70%; redirects a ritual to a neighbouring province | Can redirect friendly targeted magic |
| Seven Seals | Perfect hostile protection until seven blocks crack it; caster-linked | Friendly Astral magic can pass |
| Dome of Arcane Warding | 50% protection | Check current object text for exact scope |

Strikeback or trap domes may retaliate without blocking. Against global enchantments, strikeback does not hit the global caster. As of 6.34, domes may also protect against Astral Disruption according to the official update.

## Layering domes

When several domes exist, exact ordering and interaction must be tested for the current version and object set. Strategic evaluation should include:

- probability of at least one block;
- whether a failure destroys a dome;
- whether redirection can hit a friendly or valuable neighbour;
- whether friendly rituals are impeded;
- caster dependency;
- recurring gem and mage-turn cost;
- what the hostile caster learns from the result.

Do not multiply listed percentages without confirming resolution order and independence.

## Dome strategy

A dome is best when it protects concentrated value:

- a capital research core;
- an artifact or global caster;
- a gateway;
- a throne;
- a major laboratory and gem stock;
- a predictable army staging province.

Concentration also makes the target predictable. A strong defence can invite repeated cheap probes, assassinations, ordinary invasion, or attacks on the dome caster.

## Remote-defence audit

- Which provinces are worth enemy gems?
- Which hostile paths and ranges are known?
- Is the dome compatible with friendly rituals?
- Can the caster survive old age, raids, and assassinations?
- Is there a second laboratory or alternate staging point?
- What happens after one block, one failure, or redirection?
- Can the enemy simply attack the logistics outside the dome?

# Part X: Global Enchantments and Dispel Wars

## Global slots

Global enchantments are worldwide rituals. Game setup permits 3, 5, 7, or 9 global slots; five is the common default. The slot limit makes globals a shared political resource. Casting one changes not only the world but also what every other nation can maintain.

## Casting cases

When a global is cast:

1. if the same named global already exists, the new casting attempts to replace it through the dispel contest;
2. if an empty slot exists and that name is absent, the new global occupies a slot;
3. if all slots are full and the name is different, the new global contests a randomly selected existing global, including possibly one cast by the same nation.

Global casting order among mages is random. A plan that assumes an open slot at the beginning of hosting may fail after other nations cast first.

## Overcasting

The caster can add gems above the printed minimum. Ritual spending is capped by:

```text
maximum ritual gems = caster path level x 100
```

The dispel strength of a global includes:

```text
+1 per extra gem above minimum
+5 per caster path level above the spell requirement
+DRN
```

The challenger must beat the incumbent’s result. The ordinary lesson is that one extra caster path level is worth five overcast gems in the contest, before considering other abilities or Grand Communion support.

## Dispel

The common Dispel ritual directly challenges a selected global. The same comparison framework applies:

- extra gems add one each;
- excess relevant path adds five each;
- both sides receive a DRN;
- the higher result wins;
- the challenger must overcome the existing enchantment.

Because the roll is open-ended, no finite ordinary advantage is absolute. Large margins produce reliability, not certainty.

## Caster dependency

Most globals end if the caster dies. Immortality does not preserve the enchantment through death while the body reforms. Some globals are also tied to an origin province and end if that province is conquered.

Counterplay includes:

- Dispel;
- same-name replacement;
- slot-pressure casting;
- assassination;
- remote attacks;
- old-age pressure;
- conquest of the origin;
- forcing the caster to take another risk;
- pushing out hostile dominion when the effect is dominion-limited.

A huge overcast protects against magical contest, not against a knife.

## Protection against globals

Domes can protect units against many global effects in the same general way as local rituals. Strikeback domes do not retaliate against global casters. For globals restricted to or strengthened by dominion, removing hostile dominion from a province can function as protection.

The exact protected unit, province, and event scope is global-specific and should be read from current spell text.

## Global categories

| Category | Strategic effect |
| --- | --- |
| Gem engine | Creates monthly magical income |
| Economic engine | Changes gold, resources, supplies, or population |
| Battlefield rule | Adds storms, darkness, scales, or other conditions |
| Summoning or attack engine | Produces units or recurring hostile actions |
| Research or forging engine | Changes item cost, skill, or knowledge economy |
| Punishment global | Taxes rituals, forging, empowerment, or ordinary activity |
| Dominion global | Scales with or operates inside religious territory |
| Information or control global | Changes vision, detection, travel, or global slots |

The printed benefit is only the first-order effect. A world storm, darkness, or ritual tax changes every rival’s research choices and diplomacy.

## Selected strategic examples

The following revision-2 manual values are a reference set; current object data must be checked before a live-game order:

| Global | Requirement and base cost | Principal function |
| --- | --- | --- |
| Eternal Pyre | Enchantment 6, F6, 80 Fire | +20 Fire gems per month; heat and darkness interaction at origin |
| Mother Oak | Alteration 5, N5, 50 Nature | +10 Nature gems per month |
| Well of Misery | Conjuration 8, D6, 80 Death | +21 Death gems per month and world growth interaction |
| Stellar Focus | Enchantment 7, S5, 60 Astral | +10 Astral pearls per month; world Drain and origin Magic effects |
| Gale Gate | Thaumaturgy 8, A5, 60 Air | +20 Air gems per month, stronger Air Elementals, hurricanes |
| Gates of Horn and Ivory | Thaumaturgy 7, G5, 60 Glamour | +15 Glamour gems per month and increased Glamour ritual range |
| Forge of the Ancients | Construction 6, E5, 80 Earth | Item cost reduction and Master Smith bonus |
| Perpetual Storm | Evocation 6, A5, 70 Air | Storms in battles, land-income and movement/range pressure |
| Burden of Time | Thaumaturgy 7, D7, 70 Death | Population, unrest, Death scales, and accelerated aging pressure |
| Eternal Twilight | Alteration 8, G8, 90 Glamour | Worldwide Magic/Twilight and economic pressure outside friendly dominion |

Examples with more extreme late-game effects appear in Part XIII. These values are object data, not engine formulas; patches and active mods can change them.

## Payback

For a pure gem global:

```text
nominal payback time
= total gems spent / monthly gems produced
```

This is incomplete. A proper valuation adds:

- probability of being dispelled or losing the caster;
- value of the global slot;
- diplomacy and coalition response;
- same-path gem scarcity;
- caster and research opportunity cost;
- time remaining in the game;
- benefit from non-income side effects.

An 80-gem global producing 20 per month has a nominal four-month payback before overcast. It can still be poor if it provokes immediate war or exposes the only F6 caster.

## Global diplomacy

Globals change incentives:

- a private gem engine is visible wealth;
- a world penalty creates a coalition even if its caster is hard to identify politically;
- a slot-filling global can block several nations’ plans;
- a defensive overcast can signal a long-term commitment;
- an origin province becomes a public strategic target.

Before casting, assess:

1. who gains;
2. who loses;
3. who can dispel;
4. who can reach the caster or origin;
5. who benefits from helping either side;
6. what explanation or bargain is available.

## Global-war audit

- Confirm the current spell object.
- Name the caster and backup.
- Calculate minimum, overcast, excess-path bonus, and maximum spend.
- Decide whether a Grand Communion applies.
- Verify slot state but assume other casts can precede it.
- Protect the caster and any origin province.
- Reserve a response to replacement or Dispel.
- Model diplomatic reaction.
- Set a minimum number of productive months.
- Do not place every strategic asset in the same protected province.

# Part XI: Forging, Items, and Artifacts

## Forging requirements

Forge Item requires:

- a mage in a friendly laboratory;
- the relevant Construction level;
- all item path requirements;
- the required gems;
- an appropriate item slot on the eventual bearer.

Forging resolves at hosting step 5. `Shift+O` repeats the selected item each month while requirements remain satisfied.

## Construction tiers

| Construction level | Item tier |
| ---: | --- |
| 1 | Magical trinkets |
| 3 | Lesser magical items |
| 5 | Greater magical items |
| 7 | Very powerful magical items |
| 9 | Unique magical artifacts |

Construction also contains spells and constructs. Its strategic value cannot be reduced to equipment alone.

## Base item cost by path requirement

For each required path:

| Required level | Base gems of that path |
| ---: | ---: |
| 1 | 5 |
| 2 | 10 |
| 3 | 15 |
| 4 | 20 |
| 5 | 30 |
| 6 | 40 |
| 7 | 55 |
| 8 | 70 |

Multi-path items charge each path component. Current object data, national discounts, Forge Bonus, Forge of the Ancients, yearning, and mod commands can alter effective cost.

## Item value

An item can provide:

- a path threshold;
- reinvigoration or resistance;
- protection, defence, attacks, or mobility;
- automatic communion membership;
- ritual range or special orders;
- leadership;
- monthly gem generation;
- survival or transformation;
- a chassis-specific thug or supercombatant package.

The correct unit of analysis is the package:

```text
item gems
+ forge mage-turn
+ Construction research
+ bearer opportunity cost
+ risk of loss
```

A cheap item can be strategically expensive on the wrong bearer. A costly booster can be excellent if it unlocks a global or a new repeatable booster ladder.

## Slots and package conflicts

Commanders have limited equipment slots. A booster competes with:

- protection;
- reinvigoration;
- a weapon or shield;
- penetration gear;
- mobility;
- anti-assassination equipment;
- another booster.

Path-access plans must be built on the actual chassis. “Wear three boosters” fails if they occupy the same miscellaneous, head, body, or hand slot.

Mounted units and unusual chassis can have different slot or item restrictions. Strength requirements and two-handed weapons can also invalidate theoretical loadouts.

## National items

Some items are:

- **restricted:** only qualifying nations see and forge them, displayed with a dark blue forge background;
- **discounted:** available at reduced cost for particular nations, displayed in grey.

National items may alter a nation’s access curve earlier than generic tables imply. They belong in every later nation dossier.

## Forge bonuses

Forge Bonus and Master Smith are not identical:

- **Master Smith** raises paths for forging only;
- **Forge Bonus** reduces cost according to the ability or source;
- **Forge of the Ancients** gives a world-effect discount and Master Smith bonus to the caster’s nation;
- national discounts and object-specific commands can also apply.

Exact stacking order and rounding among fixed and percentage effects are assigned to controlled tests. The displayed forge cost is the operational authority.

## Forge of the Ancients

The revision-2 manual lists:

```text
Construction 6
Earth 5
80 Earth gems
-20% item gem cost
Master Smith +1
```

This global changes both price and eligibility. Its strategic value is highest when:

- many item batches are planned;
- the +1 creates new forge thresholds;
- Construction research is already deep;
- the caster and global can be protected;
- the new efficiency will be realised before Dispel or war.

## Artifacts

Construction 9 items are unique artifacts: only one copy of each can exist in the world. The default limited-unique-artifact rule limits each player to one unique artifact forged per turn.

Artifacts create:

- race conditions;
- intelligence from failed availability;
- concentration of power and loss risk;
- global strategic targets;
- an incentive to reach Construction 9 before others.

An artifact is more than an improved item. Its uniqueness changes timing and diplomacy.

## Yearning

An artifact can become yearning, allowing it to be forged at half usual cost. Yearning can begin once at least one of these has occurred:

- any nation researches Construction 9;
- Forge of the Ancients is active;
- the Throne of Creation is claimed;
- the Throne of the Artificer is claimed.

Each condition increases the monthly yearning rate by 50 percentage points according to the manual. The check occurs at hosting step 62.

Yearning creates an information problem. Waiting can halve price but lose the artifact race. Forging immediately secures the object but pays full cost.

## Booster reference

The following manual items form the core generic access map. Values are path requirements, not effective gem prices after bonuses.

### Construction 5

| Item | Forge requirement | Boost |
| --- | --- | --- |
| Skull Staff | D2 | +1 Death |
| Thistle Mace | N2 | +1 Nature |
| Flame Helmet | F4 | +1 Fire |
| Winged Helmet | A4 | +1 Air |
| Gossamer Veil | G3 | +1 Glamour |
| Robe of the Sea | W3 | +1 Water |
| Armour of Souls | B5 | +1 Blood |
| Earth Boots | E2 | +1 Earth |
| Coin of Meteoritic Iron | S2E2 | +1 Astral |
| Horn of Storms | A5 | +1 Air |
| Brazen Vessel | B5 | +1 Blood |
| Blood Stone | B3E2 | +1 Earth |
| Armour of Twisting Thorns | B3N2 | +1 Nature and +1 Blood |

### Construction 7

| Item | Forge requirement | Boost |
| --- | --- | --- |
| Staff of Elemental Mastery | F4W4 or A4E4 variant | +1 Fire, Air, Water, and Earth |
| Treelord’s Staff | N5 | +2 Nature |
| Blood Thorn | B3 | +1 Blood |
| Starshine Skullcap | S2 | +1 Astral |
| Skullface | D5 | +1 Death |
| Robe of the Magi | A5B5 | +1 all nine ordinary paths |
| Skull of Fire | F1D1 | +1 Fire |
| Water Bracelet | W1 | +1 Water |
| Ring of Wizardry | S7 | +1 all nine ordinary paths |
| Ring of Sorcery | S6 | +1 Astral, Death, Nature, and Glamour |
| Moonvine Bracelet | N3S1 | +1 Nature |
| Mirage Crystal | G3E2 | +1 Glamour |

The table is a threshold map, not a recommendation to forge every item. It must be combined with slots, national paths, rare randoms, and active-mod data.

## Booster ladders

A ladder begins with actual access and applies legal steps in order:

```text
native path
-> low-tier booster
-> higher forge threshold
-> multi-path booster
-> summon or empowerment
-> global or legendary threshold
```

Example structure:

```text
E2 mage
-> forge Earth Boots
-> operate as E3 while worn
-> cast or forge an E3 threshold
```

This does not create Earth on an E0 mage. It also does not allow one physical item to be worn simultaneously by two casters.

## Forge queue

For each planned item:

| Field | Record |
| --- | --- |
| Purpose | Exact spell, ritual, battle, or chassis unlocked |
| Qualified forger | Common, rare, unique, or Pretender |
| Research | Construction deadline |
| Cost | Displayed current cost after bonuses |
| Slot | Conflict with other equipment |
| Bearer | Where and when the item is needed |
| Reuse | Whether it returns to a laboratory or remains deployed |
| Loss risk | Capture, death, assassination, or artifact uniqueness |

# Part XII: Path Access and Bootstrapping

## National access is a distribution

“The nation has Astral 3” can mean:

- every fort recruits S3;
- a capital-only mage has S3;
- a 10% random reaches S3;
- the Pretender alone has S3;
- a summon can eventually reach S3;
- one empowered commander reaches S3;
- a communion temporarily produces S3.

These are strategically different. Every nation dossier should separate:

- common repeatable paths;
- capital or terrain restrictions;
- random probability;
- foreign recruitment;
- summons;
- Pretender access;
- item-dependent access;
- communion-only combat access;
- empowerment.

## The access graph

Represent each threshold as a node:

```text
recruitable mage
-> booster forger
-> boosted ritual caster
-> summoned new-path commander
-> cross-path item
-> global or legendary caster
```

Every arrow needs:

- research;
- path;
- gems;
- a mage-turn;
- a slot or laboratory;
- correct load order under mods.

If any arrow depends on a rare random, calculate recruitment probability and delay rather than calling the ladder “reliable.”

## Probability of random access

For an independent probability `p` per recruitment, the chance of at least one success after `n` recruits is:

```text
P(at least one) = 1 - (1 - p)^n
```

Examples:

| Random chance | Recruits | Chance of at least one |
| ---: | ---: | ---: |
| 10% | 5 | 41% |
| 10% | 10 | 65% |
| 10% | 20 | 88% |
| 20% | 5 | 67% |
| 20% | 10 | 89% |

This assumes independent rolls and the stated probability. Multi-pick random systems and linked randoms require their actual object definition.

## Access quality

Evaluate a path threshold on:

| Dimension | Question |
| --- | --- |
| Reliability | How often can the caster be obtained? |
| Scale | How many can be fielded? |
| Location | Capital, fort, terrain, summon site, or Pretender? |
| Timing | When do research and gems make it operational? |
| Sustainability | Can the effect be repeated each month or battle? |
| Replaceability | What happens if the caster dies? |
| Competing role | Is the caster also the only forger, researcher, or global anchor? |

## Empowerment as a bridge

Empowerment is most efficient when it creates an access loop. Examples:

- path 0 -> 1 permits a booster to function;
- a new cross-path combination forges a unique enabler;
- a permanent ritual caster summons replaceable mages;
- a global generates more of the gem type used;
- a new path makes an existing rare random unnecessary.

The fifty-gem first level is poor if it ends at level 1 with no useful threshold.

## Pretender as access

A Pretender can:

- forge initial boosters;
- cast a national or global ritual;
- provide a missing cross-path;
- summon new-path commanders;
- establish a communion or item ladder.

This access is delayed by dormancy or imprisonment and endangered by death, Call God delay, and positional commitments. A Pretender path that exists only on the design screen is not operational until the chassis can reach a laboratory and spend the required turns.

## Trading and diplomacy

Items and gems can move path access between nations:

- trade for a booster;
- hire another player to forge;
- exchange surplus gems for a binding shortage;
- coordinate a global or Dispel;
- use allied movement and laboratories where game rules permit.

Trade can be cheaper than empowerment, but it creates dependency and reveals strategic intent. A request for a Starshine Skullcap or Ring of Sorcery tells informed rivals which threshold may be approaching.

## Hidden costs of path escalation

- rare mages stop researching;
- boosters occupy survival slots;
- a ladder concentrates unique items;
- the caster becomes an assassination target;
- alchemy destroys four gems for one off-path gem;
- the required global occupies a contested slot;
- the access arrives too late for the named war.

The correct endpoint is the cheapest **timely and repeatable** access, not the highest theoretical path.

# Part XIII: Legendary and Late-Game Magic

## The level-nine decision

Legendary research is a strategic commitment:

- level 9 has a large research cost;
- one spell is selected at a time;
- required paths are often rare;
- gem costs can consume several months of income;
- the spell can change global diplomacy;
- the caster becomes a critical asset.

The selection should answer:

1. What changes immediately after the spell is learned?
2. Is the caster already operational?
3. Are the gems reserved?
4. What is the counter?
5. Is a second legendary spell worth repeating the level?
6. Would another school’s lower breakpoint win sooner?

## Wish

The revision-2 manual lists Wish as:

```text
Alteration 9
Astral 9
100 Astral pearls
```

Wish can produce extraordinary outcomes and can also harm the caster or nation. The manual suggests that wishing for gems or an artifact is safer than many ambitious requests.

Folklore is not enough to establish the accepted commands, aliases, random results, restricted units, or mod interactions. The library treats a complete Wish catalogue as **test pending**. The controlled suite records exact strings, messages, treasury changes, units, items, afflictions, horror marks, and repeat variation for each ruleset.

## Nexus Gate

The manual lists Nexus Gate as:

```text
Thaumaturgy 9
Astral 5, Earth 3
40 Astral pearls
```

It establishes a permanent gate to the Nexus. The network is shared and creates opportunities for rapid movement as well as exposure to other users and void-related danger. It cannot be evaluated as “forty pearls for movement” alone; it changes map topology.

Questions before opening it:

- who else can use the network;
- which laboratories and armies become connected;
- whether entry provinces can be held;
- what happens if an enemy learns or controls a node;
- which commanders can survive the destination.

## Tartarian Gate

The manual lists Tartarian Gate as:

```text
Conjuration 9
Death 7
7 Death gems
```

It releases a dead Titan or Monstrum from Tartarus. The body can be extraordinarily powerful, but the mind may be destroyed or otherwise impaired. The ritual’s low printed gem cost is balanced by uncertainty, caster requirements, research, leadership, equipment, and remediation.

Tartarians should be classified after arrival:

- fully capable commander;
- impaired commander requiring healing or transformation;
- combat body;
- unusable or dangerous result.

The expected value depends on the nation’s ability to repair minds, equip chassis, command units, and absorb failures.

## Arcane Nexus

The revision-2 manual lists Arcane Nexus as:

```text
Enchantment 9
Astral 8
150 Astral pearls
```

It gathers Astral pearls equal to one quarter of non-Astral, non-Blood gems spent on rituals, forging, and empowerment, along with its ambient collection described by the spell. It does not simply take a percentage of all magic income.

Arcane Nexus changes the world’s incentives:

- rivals may delay forging and rituals;
- gem spending indirectly funds the caster;
- the caster becomes a coalition target;
- Dispel strength and overcast become geopolitical questions;
- Blood activity is comparatively less taxed by the stated collection rule.

## Utterdark

The revision-2 manual lists Utterdark as:

```text
Alteration 9
Death 9
100 Death gems
```

Its world darkness and severe income/resource reduction restructure military and economic play; caves and deep seas receive stated exemptions. Its value is relative. A nation prepared for darkness, nonliving armies, summons, or reduced conventional income may gain while ordinary gold-and-resource nations collapse.

The diplomatic effect is immediate: even nations not at war with the caster have reason to remove it.

## Gift of Nature’s Bounty

The manual’s legendary Nature global improves income inside friendly dominion in proportion to candles and adds Growth. Its effect links:

- dominion strength;
- population economy;
- temple and preaching infrastructure;
- global protection;
- the ability to hold productive territory.

It does more than produce income. It turns religious map control into a fiscal multiplier.

## Astral Corruption

The legendary Blood/Astral global punishes non-Blood rituals, forging, and empowerment with horror-related danger scaling with expenditure. It changes the comparative price of every magical action and can make ordinary path development lethal.

The caster should expect:

- coalition pressure;
- reduced rival forging and ritual tempo;
- greater relative value of Blood magic;
- attacks on the global caster;
- opponents shifting to armies, priests, or already forged assets.

## Cataclysm and slot disruption

Some late rituals affect multiple globals, local enchantments, world magic, horror marks, or even the global-slot environment. Such effects should be treated as regime changes, not isolated spell casts.

Before using one:

- record which friendly enchantments will also be lost;
- estimate who benefits from a cleared global board;
- identify the order in which replacement globals can be cast later;
- protect against the new horror or magic environment;
- recognise that apparent neutrality can still favour one roster.

## Late-game transition

A nation is not in the late game merely because it has researched level 9. A functional late-game magical state includes:

- several protected high-path casters;
- a deep treasury with named reserves;
- repeatable battlefield packages;
- remote response and movement;
- global defence;
- forged and summoned access;
- laboratories and retreat routes;
- intelligence about rival legendary choices.

Research without delivery is a catalogue. Delivery without preservation is a spectacle.

# Part XIV: Countering Magic

## Counter the chain

Every magical plan has dependencies. It can be attacked at:

```text
research
-> caster
-> path boost
-> gems
-> lab
-> range
-> preparation
-> target
-> effect
-> persistence
```

The cheapest counter is often not the one printed opposite the damage type.

## Counter layers

| Enemy mechanism | Possible counter layers |
| --- | --- |
| Fire area damage | Fire Resistance, dispersion, faster contact, caster interruption, dome if remote |
| MR-based control | Higher MR, path skill, antimagic, fewer valuable targets, physical pressure |
| Communion | Kill or scatter masters, exhaust slaves, force threshold loss, early contact, extended battle |
| Skeleton spam | Priests, fatigue pressure, kill summoners, long-battle clock, commander targeting |
| Heavy buffs | Attack before activation, bypass Protection, remove caster-linked enchantment |
| Remote attack | Dome, decoy province, distributed labs, conventional defence, retaliation |
| Global | Dispel, replacement, assassination, origin conquest, dominion removal, diplomacy |
| Artifact chassis | Disarm through killing bearer, fatigue, MR attack, battlefield control, assassination |
| Gem-heavy script | Cheap probes, sequential battles, retreat denial, treasury pressure |

## Resistance is not a complete counter

Resistance reduces one damage family. It does not necessarily answer:

- physical secondary effects;
- fatigue;
- control;
- armour-negating non-elemental damage;
- summons;
- morale pressure;
- battlefield conditions;
- a complementary second path.

A good counter preserves function after the opponent changes one spell.

## Attack timing

Many magical packages are weakest:

- before research completes;
- while boosters are being forged;
- during the first preparation rounds;
- after gems are spent in a probe;
- when casters move away from laboratories;
- after a communion loses one threshold slave;
- when a global caster becomes publicly identifiable.

Tempo can be a stronger antimagic tool than Magic Resistance.

## Targeting the organisation

Magic concentrates value in commanders. Countermeasures include:

- flyers or rear attacks;
- assassins;
- precision missiles;
- remote strikes;
- fast flanks;
- fear or morale pressure on ordinary mage chassis;
- cutting friendly retreat provinces;
- raiding laboratories and gem connections.

This must be balanced against decoys, bodyguards, traps, and expendable casters.

## Gem denial

Force the enemy to spend resources inefficiently:

- attack twice before resupply;
- threaten multiple fronts;
- use cheap forces that look valuable enough to trigger scripted gems;
- retreat from the expected main battle where legal;
- raid gem-producing sites and laboratories;
- occupy the route that connects sites to labs.

Exact spell-AI gem thresholds are not fully public, so sacrificial-probe doctrine must be tested rather than treated as automatic.

## Counter-counter planning

Every package should answer:

> If the opponent knows the plan, what is the cheapest adjustment that defeats it?

Then add one response:

- alternative damage;
- different formation;
- a faster script;
- a lower-gem mode;
- extra slave redundancy;
- a second route;
- conventional troops that exploit the magical counter.

The aim is not an uncounterable spell. It is a package whose counters create exploitable costs.

# Part XV: Active Mod Ruleset

## Keep the engine and object layers separate

Book IX owns the exact spell, item, site, mage, and command inventories for DE 2.16 followed by Divinitus 1.15.3 DE. Those files can change schools, paths, costs, range, area, effects, boosters, research, forging, ritual mastery, and gem income on thousands of individual objects. An unmodded spell table cannot safely be copied into the combined game.

The object edits do not automatically replace the engine's general research process, communion participant rules, ritual timing, laboratory requirements, global-slot process, or ordinary alchemy. Those rules remain the starting point until an exact command, patch correction, or controlled test changes them.

## Resolving modded magic

For every important spell or item:

1. identify the unmodded object;
2. apply every DE selection or copy in source order;
3. apply Divinitus afterward;
4. resolve linked units, effects, weapons, sites, and shapes;
5. record final school, paths, cost, range, area, effect, and restrictions;
6. verify in game;
7. test AI, communion, and edge behaviour if strategically important.

The published explanation can remain readable, but its source record must retain the full provenance.

# Part XVI: Controlled-Test Programme

## Test standard

Every test records:

- game version;
- ruleset and load order;
- map and province;
- research and global settings;
- exact commander and object IDs where available;
- paths, items, gems, fatigue, and scripts;
- screenshots or turn files;
- number of repetitions;
- observed distribution;
- conclusion and remaining uncertainty.

One replay can demonstrate possibility. It rarely establishes probability or exact rounding.

## Test 1: Research arithmetic

Create researchers with known total paths, bonuses, Magic/Drain, Dementia, philosopher status, and Divine Insights. Verify displayed and contributed RP, minimum 1, halving order, and dominion-candle caps.

## Test 2: Research hosting timing

Have researchers contribute and then die at later hosting steps. Confirm current-month contribution and future loss. Test laboratory loss and site-income connectivity separately.

## Test 3: Combat gem spending

For paths 1-4, script spells requiring zero, one, and several gems. Vary fatigue, conservative use, communion bonus, and carried stock. Record maximum gems spent per combat turn and AI fatigue spending.

Include boundary cases around the historical projected-fatigue checks of `85/20` and `100/30`, the reported `25/40` fatigue-per-divisor checks, and stocks of three versus four spare gems. These are regression predicates, not expected current rules. Run the same scripts outside a communion, inside one, and while targeted by a remote attack ritual so the 6.12, 6.15, and 6.30 corrections are isolated.

## Test 4: Spell-fatigue rounding

Use listed fatigue values not divisible by the excess-skill divisor. Vary base and armour Encumbrance. Record fatigue after each cast and locate every rounding step.

## Test 5: Penetration

Use fixed caster path, excess skill, target MR, and target same-path skill. Run enough trials for baseline, easy, and hard resistance. Confirm tie direction and half-skill rounding.

## Test 6: Communion thresholds

Run 1, 2, 3, 4, 7, 8, and 9 slaves. Remove one slave during battle and record immediate master path changes and spell legality.

## Test 7: Communion fatigue

Vary:

- equal-path slaves;
- higher-path slaves;
- lower but half-path slaves;
- below-half slaves;
- one or several masters;
- odd fatigue totals;
- reinvigoration;
- Communion, Sabbath, and Chorus.

Record master and every slave after each spell.

## Test 8: Communion self-buffs

Cast range-0 single-target buffs before and after joining. Use several masters and incompatible slave types. Record exactly which effects pass, timing, stacking, and harmful interactions.

## Test 9: Communion collapse

Kill or rout all masters at different slave-fatigue levels. Measure stun and `3d50` fatigue distribution. Separately eliminate all slaves and compare.

Include a forced-removal case to reproduce the 6.12 effect cleanup and confirm the 6.29 backlash correction.

## Test 10: Automatic communion items

Test matrices, hearts, and athames on:

- non-Astral mages;
- non-Blood mages;
- priests with and without another path;
- innate casters;
- multi-form commanders.

Verify joining time, type, and slot behaviour.

## Test 11: Ritual order

Construct same-turn rituals whose results reveal order. Repeat across nations and casters. Test dependencies involving summons, gateways, domes, and competing globals.

## Test 12: Dome interaction

For each dome:

- friendly and hostile remote spells;
- anonymous and limited rituals;
- global unit effects;
- Astral Disruption;
- multiple layered domes;
- redirection at map edges;
- caster death and province capture.

## Test 13: Global contest

Vary extra gems, excess path, same-name replacement, full slots, and Grand Communion. Confirm challenger tie behaviour, random incumbent selection, and self-replacement risk.

## Test 14: Forge-cost stacking

Combine national discounts, fixed and percentage Forge Bonus, Master Smith, Forge of the Ancients, yearning, and multi-path items. Record eligibility and displayed cost at each step.

## Test 15: Booster access

Verify that boosters fail at path 0 and activate at path 1. Test multi-path and all-path boosters, forms, item loss, and battlefield boost interactions.

## Test 16: Artifact race and yearning

Trigger each yearning condition alone and in combination. Record monthly checks, half-cost display, simultaneous forging, unique-item failure, and limited-unique-artifact settings.

## Test 17: Legendary research

Under limited and unlimited settings, record:

- first level-9 completion;
- spell-selection interface;
- repeated level-9 cost;
- simultaneous schools;
- Construction 9 differences.

## Test 18: Wish

For every ruleset:

1. prepare an S9 caster and turn backup;
2. enter exact candidate strings;
3. record message, treasury, units, items, afflictions, horror marks, and caster status;
4. test aliases separately;
5. repeat random outcomes;
6. inspect mod restrictions such as `NO_WISH`.

Priority requests include gems, gold, slaves, artifact/artefact, weapon, power, strength, experience, dominion, population, exact unit names, commander or hero, and dangerous wishes.

## Test 19: Indoor magic

Repeat battlefield-wide, ordinary area, personal, holy, and innate spells in open fields, caves, fort interiors, and assassination arenas. Confirm current 6.36 legality and AI fallback.

## Test 20: Combined-mod regression

Build fixed battle and ritual fixtures for:

- school and requirement changes;
- damage, area, range, and fatigue;
- boosters and forge costs;
- communions and `#masterrit`;
- sites and gem income;
- Divinitus overwrites after DE.

Re-run whenever either file changes.

# Part XVII: Operational Checklists

## First magic audit

For a new nation:

1. list every recruitable mage and path distribution;
2. separate common, capital-only, terrain, foreign, sacred, and random access;
3. record research per gold, commander point, and upkeep;
4. identify the first battlefield protection, damage, and control breakpoints;
5. list generic and national boosters;
6. identify summon-based path expansion;
7. map gem income and unsearched paths;
8. name the first war’s battle package;
9. set battle and strategic reserves;
10. identify the Pretender’s unique magical jobs.

## Research-turn checklist

- Did scouting change the next threat?
- What exact breakpoint is being bought?
- Which common mage casts it?
- Are the necessary gems already available?
- Is a critical forger or ritualist still counted as a researcher?
- Does one additional school level produce a usable spell?
- Is the plan overdependent on one rare random?
- What is the branch if war begins early?

## Battle-magic checklist

- legal research and path;
- carried gems or slaves;
- current skill and per-turn spend limit;
- fatigue after excess skill and Encumbrance;
- range and likely target;
- battlefield indoor or underwater status;
- resistance and friendly exposure;
- preparation and interruption risk;
- communion threshold and slave load;
- orders after script completion;
- retreat and gem preservation.

## Ritual checklist

- laboratory;
- treasury stock after other commitments;
- caster path and maximum ritual spend;
- range and UW/NUW legality;
- hosting order;
- dome risk;
- anonymous or limited status;
- repeat-order cancellation condition;
- caster and origin protection;
- exploitation after success.

## Forging checklist

- current Construction;
- current object and mod overwrite;
- actual qualified forger;
- displayed cost;
- national, global, bonus, and yearning modifiers;
- item slot;
- bearer and delivery location;
- forge mage-turn;
- alternative booster or trade;
- loss risk.

## Global checklist

- empty-slot uncertainty;
- minimum and overcast;
- excess-path bonus;
- Grand Communion;
- caster and origin;
- Dispel opposition;
- same-name contest;
- diplomatic coalition;
- payback time;
- world effect begins at step 28.

## Post-battle magic audit

After every important replay:

- Which scripted spell first failed or changed target?
- Did contact occur before the package activated?
- How many gems were consumed and why?
- Which casters were interrupted?
- What was master and slave fatigue after each major cast?
- Did resistance, Protection, dispersion, or summons decide conversion?
- Did the army exploit the effect?
- Which caster, item, or gem stock was permanently lost?
- What single change most improves the next battle?

# Part XVIII: Essays

## Essay I: Research as a Response Tree

Research is often imagined as a ladder: climb one school, take the strongest spell at each level, then begin another. That image is convenient and strategically misleading. A ladder has only one direction. A real research plan is a response tree whose branches depend on enemy armies, geography, Pretender timing, gems, and the distribution of national mages.

The root is the nation’s repeatable access. If most forts can recruit E2 mages, an Earth spell cast by E2 is not one option among many; it is a scalable transformation of the roster. If S3 appears only on a rare random, the same research level may provide a spectacular but unreliable trick. Research points do not distinguish between them. Strategy must.

The branches are deadlines. A spell that finishes two turns after an invasion is not an answer to that invasion. A defensive level reached one turn early may preserve laboratories and researchers, increasing every later branch. This is why research value cannot be reduced to spell efficiency. Timing changes the quantity of future research that exists.

Scouting prunes the tree. Fire Resistance becomes urgent against mass fire damage and largely idle against an enemy who changes to poison or fatigue. A wide portfolio protects against uncertainty, but each unfinished branch delays every completed answer. The best plan is neither a straight rush nor equal investment. It maintains one main branch and one affordable pivot.

Access development creates new branches. A Construction level can forge a booster; the booster permits a summon; the summon carries a new path; that path unlocks a ritual. The original research may produce far more than its first item. A high-level spell with no caster is the opposite: knowledge with no route into the world.

An expert research screen should be read as a decision map. Every allocated point says which future is being prepared for and which is being delayed. The useful question is not “Which school is best?” It is “Which branch leaves the nation with a timely answer and the strongest next choice?”

## Essay II: Gems as Stored Time

A gem is condensed magical power, but strategically it is also stored time. It represents a site found, territory held, a connection maintained to a laboratory, and several turns during which the resource was not spent elsewhere.

This explains why equal gem costs are not equal. Five gems from a path producing twenty each month are a small slice of current flow. Five gems in an absent or scarce path may represent alchemy at four to one, diplomatic trade, or the entire stock accumulated since expansion. The spell interface displays cost; it does not display replacement time.

Combat converts stored time into immediate tempo. A path-boosting gem can bring a spell forward by one threshold. Fatigue spending can buy an additional useful cast before unconsciousness. A battlefield enchantment can make one battle occur under conditions that would otherwise require an entirely different army. The gem is efficient when the time purchased now is worth more than the time stored for later.

Forging converts gems into persistent access. A booster may be moved between mages, reused across wars, and become the first rung of a larger ladder. A summon converts them into a body or commander. A global converts a large stock into continuing flow or a new worldwide rule. These forms have different exposure: items can be captured, summons can die, and globals depend on casters and contested slots.

The gem treasury is also a calendar. A reserve for Dispel protects future turns. A forge queue promises gems to a coming threshold. Battle loads prepay the chance to survive an invasion. If every gem remains in one unlabelled total, future plans are silently sold to the first attractive order.

The mature question is not whether to spend or save. It is which future action the stock is preserving, and whether the current crisis is more valuable than that future. Hoarding without a named endpoint is wasted time. Spending without an opportunity-cost ledger is borrowed defeat.

## Essay III: From Mage to Army

A nation does not possess battlefield magic merely because its mage can cast a spell. The effect becomes military power only when it is delivered through an army structure.

The first requirement is time. Buffs, communion formation, and battlefield enchantments occupy preparation rounds. The line must hold without routing or pushing the fight outside spell range. Formation is part of the magical plan. A cheap screen may be the piece that makes an expensive spell work.

The second requirement is scale. One powerful caster can influence a battle, but repeatable mages define doctrine. If every fort supplies the required path, losses can be replaced and several armies can carry the package. If the Pretender or one rare random is essential, the effect is a strategic reserve, not standard army equipment.

The third requirement is conversion. Protection must answer the actual damage family. Evocations need legal targets and acceptable friendly exposure. Resistance spells must activate before the hostile effect. Summoned bodies must appear where their frontage and morale matter. A spell cast successfully but converted into irrelevant damage has consumed time and perhaps gems without becoming force.

The fourth requirement is exploitation. Immobilising an enemy matters if missiles, flankers, or heavy infantry can use the delay. Darkness matters if the friendly roster functions better inside it. A storm matters if it disables more hostile systems than friendly ones. Magic is strongest when it changes the exchange in favour of bodies already prepared to exploit it.

The final requirement is preservation. Mages, boosters, slaves, and gems are campaign assets. A victorious army that loses its magical core may not fight again. The full magical package includes retreat routes, commander protection, spare laboratories, and a resupply plan.

Turning a mage into part of an army is an organisational job. The spell is only one component. Screen, formation, script, gem load, counter, and post-battle survival complete the weapon.

## Essay IV: Communions Without Myths

Communions attract rules of thumb because their exact arithmetic feels cumbersome. “Use four slaves,” “one master per four,” or “communions share buffs” are memorable. None is a sufficient design rule.

Four slaves do create +2 paths, but they also stand on a cliff. One loss reduces every master to +1. Whether they survive depends on the spell’s fatigue, the master’s boosted path, each slave’s relative path, the number of masters casting, the communion type, and shared buffs. The visible slave count is only the beginning of the calculation.

The participant definition corrects another common assumption. Other masters do not help divide one master’s spell. One casting master and all slaves participate. Adding masters increases the number of fatigue events sent into the same pool, so an impressive casting roster can make the communion less stable.

The path comparison is equally important. Communion bonuses lift the master. If weak slaves remain below half that boosted skill, their fatigue share is multiplied by four. A spell that looks cheap after the master’s excess-skill reduction can still crush every slave when repeated by several masters.

Shared self-buffs are the creative centre of communion design. A master can transmit qualifying personal protection, resistance, regeneration, or other effects to the slave block. This can turn fragile researchers into a durable magical battery. It can also distribute an incompatible effect and kill them faster. The chassis matters as much as the paths.

The communion is best understood as a power grid. Slaves provide capacity, masters draw and transform it, thresholds govern voltage, and every spell creates load. Redundancy, compatible components, controlled demand, and protected control nodes make a grid reliable. A copied ratio does not.

## Essay V: Rituals and Geopolitics

Battle spells act inside one encounter. Rituals act on a map shared with other players and intentions. A remote attack, dome, teleport, or global is both a mechanical action and a political signal.

Range compresses geography. A nation with remote search and attack can turn distant laboratories into forward influence. Magic movement can ignore ordinary fronts. Domes create protected capitals and staging provinces. None abolishes position: every effect still begins from a caster, laboratory, origin, range, or gateway that can be scouted and attacked.

Hosting order makes this influence simultaneous. Rituals resolve in random caster order. Remote attacks and magic battles precede ordinary movement. Globals take world effect after several military phases. The strategic map visible when orders are submitted is not the map on which every effect resolves.

An anonymous ritual conceals information but does not remove inference. Nations observe who has the path, range, motive, and gem economy. A repeated attack can unite several targets against the suspected caster. A global publicly changes every nation’s incentives even if its direct benefit is private.

Protection also redistributes violence. A dome over the capital encourages enemies to raid gem sites, assassinate the dome caster, probe the percentage, redirect magic, or invade conventionally. Successful defence changes the cheapest hostile route; it does not end hostility.

Ritual planning must include the diplomatic aftermath. The effect, its likely attribution, the victims’ alternatives, and the means of exploiting it all belong in the order. Strategic magic is geopolitics carried out through the hosting sequence.

## Essay VI: Globals as Political Economy

A global enchantment is often evaluated by payback: cost divided by monthly income. This is necessary for gem engines and radically incomplete.

The global occupies a scarce public slot. It announces a caster with high path access and a treasury capable of overcasting. It may reveal an origin province. It changes which rivals gain from cooperation, Dispel, assassination, or slot pressure. Its true cost includes the coalition it creates.

World penalties demonstrate the point most clearly. Darkness, storms, aging, ritual corruption, or income collapse do not harm every roster equally. The caster has presumably prepared summons, resistances, dominion, or alternative income. Other nations assess not the absolute harm but the caster’s relative gain. A spell that reduces everyone by half can be overwhelmingly aggressive if one nation loses only a quarter.

Gem globals also alter politics. Private income increases future Dispel and forging capacity. A rival may reasonably spend more than the global’s nominal value to stop it compounding. The caster's payback calculation must include the chance that the global survives, not only its monthly output.

Overcasting buys resistance to one form of attack. It does not prevent assassination, old age, origin conquest, or a random full-slot replacement attempt. Every additional gem increases magical security while concentrating more value behind the same mortal dependency.

The strongest global plan is a state programme: caster security, reserve gems, dome and mundane defence, diplomatic preparation, origin protection, and a schedule for exploiting the new world. The enchantment is the public institution; the protected network behind it is the state that keeps it alive.

## Essay VII: The Level-Nine Decision

Level-nine research is seductive because it promises the largest effects in the game. The cost is not only the research points shown on the bar. It is every lower branch delayed while the nation climbs, every mage-turn required to create the caster, and every gem reserved instead of winning earlier battles.

Legendary selection makes the trade sharper. Most schools do not grant a complete catalogue at level 9; one spell is selected at a time. The first choice needs a named caster, treasury, target, counter, and operational date.

Some legendary spells transform the map. Nexus Gate changes connectivity. Others transform magical economy: Arcane Nexus taxes world expenditure, and Astral Corruption punishes ordinary magical action. Utterdark or similar world effects change the value of entire rosters. Wish can cross conventional boundaries but carries uncertainty that must be tested rather than romanticised.

The best legendary spell is relative to preparation. Tartarian Gate is stronger for a nation that can repair, equip, and lead its results. A dominion-scaled economic global is stronger for a nation already winning religious territory. A punishment global is stronger when the caster’s own economy is exempt or prepared.

Counterpressure begins before the cast. Rivals can observe research direction, boosters, rare path mages, pearl hoarding, and Construction races. A path to level 9 may invite attack precisely because its future is frightening. Reaching the threshold requires surviving the signal.

The level-nine decision should be worked backwards from the world it creates. Describe the position one turn after success, four turns after success, and after the obvious coalition response. If those positions are not favourable, the legendary spell is not yet a plan. It is only a possibility.

# Sources and Open Questions

## Principal sources

- Illwinter, *Dominions 6 Manual*, revision 2, especially Magic, paths and schools, battle magic, rituals, global enchantments, communions, gems, research, legendary spells, items, Divine Magic, alchemy, and the spell and item appendices.
- Illwinter, *Dominions 6 Modding Manual*, version 6.34.
- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html).
- [Illwinter Dominions 6 changes](https://www.illwinter.com/dom6/changes.html).
- [Official Dominions 6.30 announcement](https://steamcommunity.com/games/2511500/announcements/detail/516348030198220655).
- Supplied `DomEnhanced2_16.dm`.
- Supplied `Divinitus_1.15.3_DE.dm`.
- Loggy's reverse-engineering notes, used only to define historical combat-gem threshold tests; the notes predate official 6.15 and 6.30 corrections.
- Naaira's communion guide, used for current player doctrine and examples, while the manual and patch ledger own the rules.

Community references are used to discover disputed questions and test candidates, not to override current official rules without reproducible evidence.

## Open questions

Current-game tests or resolved object data are still needed for:

- exact current optional combat-gem AI thresholds and all target-selection weights after 6.15 and 6.30;
- every rounding step in spell fatigue, penetration, communions, forging, and ritual contests;
- complete ordering and independence of layered domes;
- every current object value altered after the revision-2 manual;
- exact Wish vocabulary, aliases, random distributions, and restrictions;
- all effective DE and Divinitus spell, item, site, mage, and summon records;
- automatic-item, forced-removal, multi-form, mod-specific communion, Grand Communion, and forge interactions;
- simultaneous artifact and global edge cases.

Book IX now owns the exact mod command scope; this list is limited to behaviours that still need engine evidence.
