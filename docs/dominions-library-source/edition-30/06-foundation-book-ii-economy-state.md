# Foundation Book II: Economy, Provinces, and the Machinery of State

## Why the economy needs its own book

Dominions 6 presents its economy as a row of numbers: gold, gems, resources, Recruitment Points, supplies, population, unrest, and upkeep. Those numbers do not all work in the same way. Some are national, some belong to one province, some vanish unused, and others can be saved indefinitely. A few are not spendable resources at all; they limit how quickly something else can be turned into useful power.

This is why the richest nation can still fail to raise an army. It is also why a poor province can decide a war by preserving tax trace, feeding a siege, or shortening a reinforcement route. Book II follows those connections from the province screen to the wider war effort. Ordinary play comes first, followed by the formulas, edge cases, and source disputes needed for closer work.

> **Foundation rule:** Economic value is not the number printed beside a province. It is the useful power that can be converted from that province, through the available infrastructure, before an opponent can interrupt the conversion.

## Edition note

Book I defines the common Dominions 6.36 baseline and evidence labels. Book II relies mainly on the revision-2 manual and Modding Manual 6.34. Where those official documents disagree, both readings remain visible. Book IX owns the exact DE and Divinitus definitions; only their economic consequences are repeated here.

The Edition 23 revision returns to R-008 and R-010 through R-013 without opening another economy volume. It separates every known rounding stage, turns the community unrest wording into explicit candidate thresholds, records what the annual upkeep observations do and do not prove, bounds the two printed fort-supply systems, and incorporates the official 6.35 Supply Usage refresh correction. No uncertain engine rule has been promoted merely because one interpretation is convenient.

## A sensible way through

For a first campaign, begin with the economic model, province anatomy, recruitment gates, supply, and infrastructure. The formula sections, PD curves, siege economics, Blood opportunity costs, and diagnostic ratios are there for closer planning. Source conflicts and controlled tests can be left until a disputed number actually matters.

# Part I: The Economic Model

## Dominions as a game of conversion

Territory is not victory by itself. Territory provides inputs which can be converted into military and magical effects:

```text
population and scales
  -> gold, supplies, and recruitment capacity

terrain and forts
  -> resources, infrastructure, and strategic position

gold and local capacity
  -> troops, commanders, buildings, and province defence

labs, mage-turns, and research
  -> spells, items, rituals, summons, and battlefield packages

sites and blood hunting
  -> gems and blood slaves

armies, magic, information, and diplomacy
  -> territory, forts, thrones, and denial

thrones and survival
  -> victory
```

Every arrow takes time. Every conversion can be interrupted. Much of expert play consists of identifying which arrow is currently limiting the nation.

### Stock, flow, capacity, and position

Four categories keep economic discussions clear.

| Category | Meaning | Examples |
| --- | --- | --- |
| **Stock** | A resource saved for future use | Treasury gold, gems, blood slaves, forged items |
| **Flow** | A recurring gain or loss | Monthly income, gem income, upkeep, population growth |
| **Capacity** | A local or national limit on conversion | Resources, Recruitment Points, Commander Points, Holy Points, mage-turns |
| **Position** | Map state that makes conversion possible or safe | Fort network, tax trace, laboratory access, supply reach, defensible borders |

Economic mistakes often begin by treating one category as another. Resources do not accumulate, so they are not a stock. A large treasury does not create recruitment capacity. A fort has a price, but it also changes strategic position and several local limits. A mage is a unit and a recurring choice about how to spend a mage-turn.

### National and local resources

| Resource or limit | Scope | Accumulates? | Portable? | Principal uses |
| --- | --- | --- | --- | --- |
| Gold | National treasury | Yes | Effectively national | Recruitment, buildings, PD, mercenaries, some rituals and events |
| Magic gems | National pool and commanders | Yes | Transferable through labs, commanders, and messages | Rituals, forging, combat magic, empowerment |
| Blood slaves | National pool and commanders | Yes | Transferable, but with distinct handling | Blood rituals, forging, battle magic, sacrifice |
| Resources | Province | No | No | Equipping recruits |
| Recruitment Points | Province | No | No | Ordinary troop throughput |
| Commander Points | Province | No | No | Commander throughput |
| Holy Points | Nation/local sacred queue interaction | Refreshes | No direct transfer | Sacred recruitment |
| Supplies | Province and army situation | No strategic stock, except siege storage and temporary pillage food | Army uses local supply | Sustaining units |
| Population | Province | Changes over time | No | Income, Recruitment Points, supplies, PD support, Blood Hunting |
| Mage-turns | Commander-time | No | Commander can move | Research, site search, forging, rituals, Blood Hunting, combat |

The table explains why “What can the nation afford?” is incomplete. The more useful question is:

> What can be paid for, recruited at the correct location, led, supplied, scripted, and delivered before the relevant deadline?

## The binding constraint

Production is governed by the tightest active limit.

Suppose a fort has:

- 1,000 gold available nationally;
- 120 local resources;
- 80 local Recruitment Points;
- one available Commander Point;
- three Holy Points.

A 10-gold, 5-resource, 10-RP troop is not limited by gold or resources. It is limited to eight by Recruitment Points. A 100-gold commander that costs two Commander Points cannot be recruited there even though the treasury is sufficient. A sacred costing one Holy Point can be limited to three even when every local pool remains.

The bottleneck can change when the recruit mix changes. Adding an expensive armoured unit may convert an RP-limited queue into a resource-limited one. Adding a cheap commander may consume the Commander Point needed for the mage who makes the fort strategically valuable.

### Bottleneck audit

For every major recruitment centre:

1. Identify the desired troop and commander package.
2. Calculate gold, resources, Recruitment Points, Commander Points, and Holy Points separately.
3. Find the first exhausted pool.
4. Ask whether a different mix uses otherwise stranded capacity.
5. Compare the value of expanding capacity against building another centre.

This is more accurate than optimising a single “gold efficiency” statistic.

## Opportunity cost

The true cost of an action includes the best alternative foregone.

Examples:

- A 600-gold laboratory is also troops not recruited this month.
- A searching mage is research not produced.
- A Blood Hunter is research, forging, or ritual work not performed.
- Province Defence is permanent local defence, but the same gold could have become a mobile army.
- A fort under construction ties up a commander and delays military spending before its benefits begin.
- A mage carrying gems into battle makes those gems unavailable for a ritual and risks losing them.

Opportunity cost changes with time. A laboratory that delays the first expansion party may be disastrous; the same laboratory may be essential once the province's recruitable mage or site income becomes relevant.

## Economic tempo

An investment is measured by more than eventual return.

```text
payback time =
  investment cost / recurring net gain
```

This simple ratio is useful but incomplete. Dominions adds:

- construction delay;
- commander-turn cost;
- risk of capture;
- military value during payback;
- capacity unlocked;
- strategic location;
- the possibility that the game ends before repayment.

A fort may never repay its gold through Administration income alone yet still be a strong investment because it recruits mages, concentrates resources, projects supply, protects a laboratory, delays an invasion, and creates a tax-trace anchor.

# Part II: Provinces, Terrain, and Population

## A province is a bundle of systems

A province can contain:

- one or more terrain types;
- population;
- potential and available resources;
- income;
- supplies;
- dominion and scales;
- unrest;
- corpses;
- Province Defence;
- a fort, temple, and laboratory;
- discovered and undiscovered sites;
- recruitable independent or national units;
- commanders and armies;
- partial ownership between the exterior and a besieged fort.

The printed income number is only one part of the province's value.

### Provincial roles

| Role | What makes it valuable |
| --- | --- |
| **Income province** | High population, favourable scales, low unrest, tax trace, Administration |
| **Production province** | High potential resources, strong fort draw, suitable national roster |
| **Mage centre** | Valuable commander roster, lab, Commander Points, safety |
| **Logistics node** | Fort supply reach, roads or movement position, defensible route |
| **Site province** | Gem income, recruit access, discounts, ritual or entry functions |
| **Blood province** | Sufficient population, patrol capacity, acceptable economic sacrifice |
| **Buffer province** | Raid tax, warning time, retreat geometry, denial |
| **Throne province** | Ascension value, special throne effects, strategic obligation |

One province may fill several roles. Its correct investment level depends on the most important role, not on a universal province template.

## Corpses as provincial stock

Unburied corpses are a local provincial stock. They are not gold, population, supplies, or units waiting to be recruited, but several Death effects and reanimation orders can convert them into value. The revision-2 manual names Raven Feast and the raising of undead as ordinary examples.

The stock is deliberately concealed from most observers. Its number is visible when a Death mage or undead priest is present in the province. A nation's ordinary priests can also see it when those priests possess national reanimation. Ermor's Ashen Empire dominion supplies a broader special exception by sensing unburied corpses in covered provinces.

| Question | Current verified answer |
| --- | --- |
| What does the number represent? | Unburied corpses currently available in the province. |
| Who normally sees it? | A Death mage or undead priest in the province. |
| Which ordinary priests can see it? | Priests of a nation whose normal priests can reanimate undead. |
| What consumes it directly? | Reanimating Soulless reduces the available corpse count; corpse-dependent spells and abilities may have their own rules. |
| What does not require this stock? | Ordinary Longdead reanimation has no corpse limit under the manual's basic distinction. |
| Is every battlefield death guaranteed to add one usable corpse? | No general one-for-one rule is stated. Corpse eligibility has changed through patches, so the casualty total is not a safe substitute for the visible stock. |
| Is a universal decay rate documented? | No general monthly decay formula is stated in the current official foundation sources used here. |

The last two limits matter. Version 6.08 specifically changed humanoid apes and dogs so that they leave corpses when killed. That official correction shows that corpse production depends on unit eligibility rather than on a universal "one dead body equals one corpse" rule. Until an exact current production table is available, battle losses should be treated as a clue, not as an exact corpse forecast.

### Corpse-dependent conversions

The manual separates three common reanimation economies:

- **Ghouls** convert living population into undead, reducing the population left behind.
- **Soulless** convert unburied corpses and reduce the local corpse stock.
- **Longdead** can be reanimated without a stated population or corpse ceiling.

Asphodel uses a different branch. Human inhabitants or dead human corpses permit a chance of Manikins and Mandragoras; when those are unavailable, animal-based carrion creatures remain possible. This is a national conversion rule, not a universal reanimation formula.

Operationally, a corpse-dependent plan needs four checks:

1. a legal commander, spell, or ability;
2. visibility or another reliable reason to believe the local stock exists;
3. the correct province at the relevant order or ritual step;
4. a comparison between consuming the stock now and reserving it for a stronger conversion later.

[Book X's special-order reference](#b10-52-reanimate-manikin-contact-allies-and-capture-slaves) owns the order-entry procedure. Exact spells and summoned objects remain in the Book XII data layer. Book II owns the economic reading: corpses are hidden, local, exhaustible in some uses, and valuable only through a legal converter.

## Terrain

The manual characterises terrain by broad tendencies:

| Terrain | Population tendency | Resource tendency | Site tendency |
| --- | --- | --- | --- |
| Plains | Neutral | Neutral | Neutral |
| Mountain Ranges | Neutral | Excellent | Many |
| Forest | Low | High | Many |
| Highlands | Low | High | Neutral |
| Swamp | Very low | Neutral | Many |
| Waste | Extremely low | Neutral | Abundant |
| Farm | Very high | Low | Few |
| River | High | Neutral | Neutral |
| Sea | Low | Neutral | Neutral |
| Deep Sea | Very low | High | Many |
| Kelp Forest | High | Neutral | Neutral |
| Gorge | Low | High | Abundant |
| Cave | Low | Neutral | Neutral |
| Drip Cave | Neutral | Excellent | Neutral |
| Crystal Cave | Very low | High | Abundant |
| Forest Cave | High | Neutral | Many |

Multiple terrain types can coexist and their effects add. Terrain also affects movement, survival skills, combat environments, national recruitment, building costs, site pools, and the boundary between land and underwater systems.

### Strategic reading of terrain

Farms often deserve protection because their population supports income, supply, and recruitment capacity. Highlands, forests, mountains, and special caves often make stronger production or search targets. Wastes and unusual terrain may be economically poor in gold yet rich in site opportunity.

This creates a recurring division:

- population-rich terrain funds the state;
- resource-rich terrain equips the army;
- site-rich terrain may fund magic;
- movement terrain determines whether any of that value can be defended.

## Population

Population supplies four fundamental systems:

1. base income;
2. Recruitment Points;
3. provincial supplies;
4. support for Province Defence.

It is also consumed or damaged by:

- Death scales and extreme temperatures;
- pillaging;
- some forms of patrolling;
- Blood Hunting and related events;
- hostile dominions and special national effects;
- sites, spells, and random events.

Population is slow capital. A temporary gold gain purchased with permanent population loss can weaken income, recruitment, supply, and PD support for the remainder of the game.

### Growth and decline

The current unmodded 6.36 baseline gives ordinary Growth as:

- population growth of 0.2% per month per step;
- 10% additional supplies per step;
- 2% additional income per step.

Death reverses those values.

The revision-2 main-manual scale table prints 1% income per step, but the newer official Modding Manual 6.34 defines the unmodded `#deathincome` default as 2. No version 6.35 announcement alters that default. The newer explicit default governs this edition; the old one-percent value remains useful only for identifying stale guides. Dominions Enhanced 2.16 also sets the income change to 2%, while changing population movement to 0.25% per scale step.

### Compounding

Population growth compounds:

```text
future population =
  current population x (1 + monthly rate)^months
```

The formula illustrates scale, but practical forecasting must account for integer rounding, changing candles and scales, events, patrolling, pillage, and hostile effects.

Growth affects the present month and the province's longer future. Its value rises with:

- early control of populous provinces;
- a long expected game;
- stable dominion;
- protection from raiding and pillage;
- units and forts that can use the resulting recruitment and supply.

Death or destructive economy can still be strategically rational for nations whose population contributes little, whose dominion deliberately kills population, or whose power spike is intended to end the game before the long-term loss dominates.

## Tax trace and the administrative map

**Official rule:** a province produces no income for the turn if it cannot trace an unbroken chain of friendly provinces to a friendly fort. Disciples can trace through allied provinces.

Tax trace creates an economic network:

- forts are collection anchors;
- friendly province chains are conduits;
- raiding can disconnect rather than merely steal;
- a single captured bridge province can suppress the income of a whole pocket;
- recovering the chain before step 38 can restore collection that month.

The system makes map topology economically meaningful. A low-income corridor can protect the income of several rich provinces.

### Tax-cut warfare

A raid should be evaluated by total denied value:

```text
raid value =
  direct province denial
  + disconnected income
  + queue disruption
  + commander attention
  + movement distortion
  + information gained
  - raider losses
  - opportunity cost
```

The direct income printed on the raided province may be the smallest term.

# Part III: Gold, Income, and Upkeep

## Income formula

The official main-manual formula is:

```text
base income = population / 100

modified income =
  (population / 100)
  x dominion-scale modifiers
  x (1 + fort Administration / 200)

final income =
  modified income / (1 + unrest x 0.02)
```

The province display reports the already modified number.

### Administration

Administration increases provincial income by half its rating:

| Administration | Local income bonus |
| ---: | ---: |
| 15 | +7.5% |
| 30 | +15% |
| 45 | +22.5% |
| 60 | +30% |
| 70 | +35% |

The bonus applies to the province containing the fort, not to neighbouring income.

### Scale interaction

The manual gives:

- Order/Turmoil: 3% income per step;
- Productivity/Sloth: 3% income per step;
- each temperature step away from preference: -5%;
- Growth/Death: 2% per step under the current official Modding Manual default.

The main manual also contains an example saying Order 2 increases income by 4%, conflicting with its own repeated 3%-per-step tables. The tables are the stronger internal evidence; the example is treated as a likely textual error.

### Rounding: formula, display, and treasury

The income formula identifies the factors but not every integer conversion. Three different numbers must be kept apart:

1. the unrounded result of a written formula;
2. the whole number displayed for the province;
3. the amount actually credited to the treasury after all current modifiers and collection rules.

The revision-2 manual does not state whether the engine floors after population, after each scale, after Administration, only at the end, or through some combination of those stages. Community documentation describes the population-derived base as rounded down, but it does not provide a versioned boundary test for the whole chain. R-008 remains open.

For ordinary play, the province display is authoritative. For a forecast near a one-gold boundary, record the displayed value before and after changing exactly one input. Do not reverse-engineer a hidden intermediate from the final integer and then present it as an official rule.

The word *rounding* conceals several different questions. They should not be allowed to borrow evidence from one another:

| Subsystem | What is established | What remains open | Safe operational value |
| --- | --- | --- | --- |
| Provincial income | Official factor chain and unrest divisor | Intermediate floors, final conversion, and treasury treatment | Province display and the Income Overview |
| Resources | One worked donor contribution of 13.8 is reduced to 13 | The printed aggregate does not reconcile; fort draw, scale, and unrest stages are not fully ordered | Current province resource pool |
| Recruitment Points | Official population bands, fort bonus, and Order/Turmoil modifier | Band, modifier, and final integer order | Current spendable RP shown by the recruitment screen |
| Commander Points | Ordinary pool and multi-month accumulation | Reduction and rounding under unrest | Current commander queue progress |
| Upkeep | Official monthly divisors and observed annual whole-number entries | Monthly fractional aggregation and desertion boundary | Income Overview, checked after roster or equipment changes |
| Fort supply | Range and highest-fort rule | Competing official multipliers and final integer conversion | Displayed province supply |

A floor observed in a resource example does not prove that income is floored at the same stage. A whole annual upkeep entry does not prove that the treasury discards monthly fractions. Whenever a result can decide a deadline, a calculator should keep three fields: the written decimal, the displayed integer, and the evidence status of the conversion between them.

### Unrest is hyperbolic, not linear

Income is divided by `1 + 0.02U`, where `U` is unrest. This has two important consequences:

1. The first unrest points do substantial damage.
2. Each later unrest point removes a smaller fraction of the already reduced income.

| Unrest | Multiplier | Income lost |
| ---: | ---: | ---: |
| 10 | 0.833 | 16.7% |
| 25 | 0.667 | 33.3% |
| 50 | 0.500 | 50.0% |
| 75 | 0.400 | 60.0% |
| 100 | 0.333 | 66.7% |
| 200 | 0.200 | 80.0% |

Unrest 100 is more severe than the income multiplier suggests because it also stops recruitment.

## Income timing

Income is hosting step 38.

Before income:

- ordinary battles and storming have resolved;
- random events and several late battles have resolved;
- buildings complete at step 35;
- pillage resolves at step 37.

After income:

- ordinary unrest alterations resolve at step 39;
- starvation resolves at step 40;
- upkeep resolves at step 41.

This timing means:

- a province captured through ordinary movement can pay its new owner that month if collection conditions are met;
- pillage can damage the same month's income;
- patrol and Order reductions at step 39 usually improve the next month's income, not the current collection;
- upkeep can use the income collected moments earlier.

## Treasury discipline

The treasury must cover several different horizons:

| Horizon | Typical commitments |
| --- | --- |
| Immediate order phase | Recruitment, buildings, PD, mercenary bids, gold-cost rituals or events |
| Hosting income step | Expected provincial income after conquest, trace, pillage, and unrest |
| Hosting upkeep step | Recurring unit and commander costs |
| Contingency reserve | Emergency recruitment, fort repair decisions, diplomacy, unexpected events |

Planning to exactly zero before uncertain income is a risk decision. The danger is highest when:

- tax traces are exposed;
- capitals or rich forts may be besieged;
- unrest is rising;
- pillage or raiding is expected;
- mercenary contracts or events can change expenditure;
- a large sacred or cavalry force obscures the apparent upkeep calculation.

## Upkeep

The manual states:

```text
ordinary upkeep = gold cost / 15 per month
sacred or slave upkeep = gold cost / 30 per month
```

Most summoned units are exempt. Some exceptions carry additional upkeep.

### Annual display

The detailed unit interface commonly displays annual upkeep:

```text
annual upkeep = monthly upkeep x 12
```

A 30-gold ordinary unit costs 2 gold per month and displays 24 per year.

### Sacred slaves

The manual says Sacred units and Slaves each pay half upkeep. A current-game discussion published on 21 December 2025, under the 6.33 release, identifies their interaction explicitly: the two reductions stack, producing a divisor of 60. The R'lyeh Slave Priest is the clean example because the current structured row carries both the Sacred and Slave tags.

```text
sacred slave upkeep = gold cost / 60 per month
```

The official announcements for 6.34 through 6.36 contain no general upkeep change. The stacking rule is published here as **Community-tested under 6.33; current through 6.36 by patch review**. It is not wording taken from the revision-2 manual.

### Mounted upkeep is component-based

A mounted card can hide more than one upkeep basis. Rider and mount are separate objects, and each component keeps its own base cost and its own Sacred or Slave status. The visible recruitment price is consequently not always enough to reconstruct upkeep.

The 6.33 observation gives a direct check:

| Mounted card | Rider basis | Mount basis | Observed annual split | Total annual upkeep |
| --- | ---: | ---: | ---: | ---: |
| Logrian Cavalry | 10 ordinary | 20 ordinary | 8 + 16 | 24 |

The pinned 6.35 object snapshot supplies further examples of the underlying component structure:

| Mounted card | Rider object | Mount object | Consequence |
| --- | --- | --- | --- |
| Mouflon Cataphract | base-cost adjustment 15, Slave | base-cost adjustment 25, not Slave | the Slave reduction applies to the rider, not automatically to the mount |
| Sacred Serpent Cataphract | base-cost adjustment 15, Sacred | base-cost adjustment 30, Sacred | both components receive their own Sacred reduction |
| Logrian Cavalry | base-cost adjustment 10, ordinary | base-cost adjustment 20, ordinary | the component total reproduces the observed 24 gold per year |

These examples do not establish a universal shortcut from the displayed recruitment price. They establish the opposite: inspect both component cards when cavalry upkeep matters. Patch 6.31 also fixed mounts that could desert separately when the treasury was empty, further confirming that mount state participates in economic resolution even though that bug does not define the upkeep formula.

### Added upkeep and shape changes

The Modding Manual defines `#addupkeep` as increasing the gold basis used for upkeep. It belongs to the object that carries it. Mounted objects need to be checked component by component; one combined modifier should not be applied to the whole recruitment card.

Shapechanged upkeep remains unresolved. The manuals define many shape relations and advise fixed gold costs for shapechanging Pretenders, but they do not say which form supplies the monthly upkeep basis for every temporary, voluntary, seasonal, death, or world shape. A current transformation matrix must compare the Income Overview before and after each shape class. Until then, a transformed commander's visible annual entry is the operational value. R-010 remains in progress.

### Reading the annual line

The December 2025 observation also records ordinary annual values of 6 for a 7-gold unit and 13 for a 16-gold unit. Those are consistent with multiplying monthly upkeep by twelve and displaying a whole number. The sample does not distinguish every possible rounding rule, and the national treasury may retain fractional liabilities that the annual line hides. Annual display rounding must not be reused as proof of monthly treasury rounding.

The same observation gives enough cases to exclude one tempting shortcut:

| Ordinary gold basis | Exact monthly formula | Exact annual equivalent | Observed annual line | What the observation proves |
| ---: | ---: | ---: | ---: | --- |
| 7 | 7/15 | 5.6 | 6 | The annual line is not simply floored at the end |
| 10 | 10/15 | 8.0 | 8 | Exact integers survive unchanged |
| 16 | 16/15 | 12.8 | 13 | The annual line is not simply floored at the end |

These cases are compatible with ordinary nearest-integer rounding and with a ceiling rule; they do not distinguish between them. Nor do they reveal whether twelve fractional monthly charges are accumulated precisely, rounded as a group, or represented through another internal unit. The annual line is a readable estimate of burden, while the treasury change remains the decisive measurement for a zero-margin budget.

### Upkeep as force structure

Upkeep does more than tax army size. It decides which forces can remain permanently mobilised.

- Gold-recruited elite armies preserve battlefield quality but continually consume income.
- Summoned forces shift the burden toward gems and mage-turns.
- Sacred troops can be capital- or Holy-limited but cheaper to maintain.
- Militia-like troops may be cheap to recruit yet expensive relative to their battlefield effect.
- Commanders, scouts, priests, and logistical specialists add recurring cost without always appearing in a front-line count.

The relevant comparison is lifecycle cost:

```text
lifecycle gold cost =
  recruitment cost
  + expected months of upkeep
  + replacement and support cost
```

A unit that survives for thirty months can cost far more through upkeep than through recruitment.

# Part IV: Resources and Recruitment

## Resources are local industrial capacity

Resources represent the materials and labour needed to equip recruits. They:

- belong to a province;
- refresh each month;
- do not stockpile;
- cannot be moved through the treasury;
- are spent only by local recruitment.

Unused resources are lost opportunity, not saved wealth.

### Potential and available resources

An unfortified province uses half its potential resources locally. A fort:

1. raises the host province to its full local potential;
2. draws its Administration percentage from eligible neighbouring provinces' potential resources.

Unrest then reduces availability:

```text
final resources =
  resources / (1 + unrest x 0.01)
```

At unrest 100, half remain, but recruitment is prohibited entirely.

## Fort resource draw

The manual's restrictions are exact:

- land cannot draw from sea, nor sea from land;
- a neighbouring province with a fort does not contribute;
- an enemy province does not contribute;
- eligible shared neighbours can contribute to more than one fort.

The manual's worked example demonstrates that draw uses the neighbour's **potential** resources, not the half-sized pool visible in an unfortified neighbour.

### Production geometry

A production fort should be evaluated by:

```text
fort resource value =
  full local potential
  + Administration% of each eligible adjacent potential
  - expected disruption
```

Expected disruption includes:

- future adjacent forts removing donors;
- hostile raids changing ownership;
- unrest;
- land/sea boundaries;
- a roster unable to use the extra resources;
- supply or gold limits that prevent full production.

### Fort spacing

Dense fort networks increase recruitment sites, Commander Points, laboratories, siege resistance, and tax anchors. They can also remove resource draw between adjacent fortified provinces.

This is not a simple argument for wide spacing. The correct spacing balances:

- mage production;
- troop production;
- resource donors;
- travel time;
- defensibility;
- supply projection;
- capital and Throne protection;
- the expected duration of the game.

## Recruitment Points

Recruitment Points model the province's ability to organise ordinary troop production.

Start at 20, then add population-band contributions:

```text
RP(population) =
  20
  + min(pop, 5,000) / 100
  + min(max(pop - 5,000, 0), 5,000) / 200
  + min(max(pop - 10,000, 0), 10,000) / 300
  + min(max(pop - 20,000, 0), 20,000) / 400
  + max(pop - 40,000, 0) / 500
```

The fort's recruitment bonus is applied afterward. Order or Turmoil changes the result by 10% per step.

### Population examples before fort and scales

| Population | Calculation | Recruitment Points before rounding |
| ---: | --- | ---: |
| 0 | 20 | 20 |
| 1,000 | 20 + 1,000/100 | 30 |
| 5,000 | 20 + 5,000/100 | 70 |
| 6,000 | 20 + 50 + 1,000/200 | 75 |
| 10,000 | 20 + 50 + 5,000/200 | 95 |
| 20,000 | 20 + 50 + 25 + 10,000/300 | 128.33 |
| 40,000 | prior + 20,000/400 | 178.33 |
| 50,000 | prior + 10,000/500 | 198.33 |

The declining contribution per additional inhabitant means population has diminishing marginal effect on RP even while remaining valuable for income and supplies.

### Official-versus-historical conflict

Older community pages preserve a different formula with a lower base and different population bands. Foundation Book II uses the revision-2 main manual formula. Historical formulas must not be used as proof of current Dominions 6 behaviour.

### Rounding

The manual gives formulas and examples but does not fully document every rounding stage:

- population band;
- scale modifier;
- fort bonus;
- final displayed and spendable total.

Until reproduced, calculations should be treated as capacity estimates near fractional boundaries. The interface remains the final operational value.

## Commander Points

Commander Points limit local commander production. The current ordinary pool is:

```text
Commander Point pool = 1 base point + current fort bonus
```

| Recruitment location | Base | Fort bonus | Ordinary total |
| --- | ---: | ---: | ---: |
| No fort | 1 | 0 | 1 |
| Palisades | 1 | +0 | 1 |
| Fortress | 1 | +1 | 2 |
| Castle | 1 | +1 | 2 |
| Citadel | 1 | +2 | 3 |
| Grand Citadel | 1 | +2 | 3 |

The fort bonuses are official revision-2 values. The one-point unfortified base and multi-turn accumulation are stated by the current community commander reference, last updated under 6.35; no 6.36 announcement changes the system. This closes R-009 at **Official plus Community-tested** evidence.

The distinction between the pool and the cost is essential. The Modding Manual defines a simple commander as normally costing one point, permits explicit Recruitment Point costs, and defines `#slowrec` as doubling the Commander Points needed for that commander. A two-point commander in a one-point province is not illegal. The queue invests capacity over multiple months until the cost is met.

```text
months to complete, before disruption = ceiling(commander cost / local CP per month)
```

| Commander cost | 1 CP location | 2 CP location | 3 CP location |
| ---: | ---: | ---: | ---: |
| 1 | 1 month | 1 month | 1 month |
| 2 | 2 months | 1 month | 1 month, with 1 point unused for that order |
| 3 | 3 months | 2 months | 1 month |
| 4 | 4 months | 2 months | 2 months |

The table describes an uninterrupted single order. Queue state, a change of recruit, unrest, ownership, or loss of eligibility can alter the actual completion date.

### What does not multiply Commander Points

- Fort statistics replace the previous stage; their bonuses do not stack across upgrades.
- AI difficulty bonuses apply to income, resources, ordinary Recruitment Points, and magic, but the manual explicitly excludes commander recruitment rate and Holy Points.
- `#slowrec` changes the commander's cost, not the province's pool.
- A recruitable commander supplied by a site changes roster access; the site commands do not by themselves add Commander Points.
- Unrest is a separate local reduction question retained under R-011.

Commander Points are often the real reason to build a fort. A nation may have enough gold to recruit more mages but no place capable of producing them.

### Commander-turn accounting

Gold measures purchase price; Commander Points measure time on the production line. A 400-gold, four-point mage and four 100-gold, one-point commanders may consume the same gold, but they do not create the same schedule. Any comparison should record both:

```text
gold per completed commander
commander-months per completed commander
```

A higher fort is most valuable when it changes a roster's calendar: two-point mages every month instead of every second month, or four-point mages every second month instead of every fourth. That throughput can outweigh the fort's direct Administration income.

## Holy Points

Sacred recruitment consumes Holy Points in addition to ordinary costs. The manual ties the ordinary sacred recruitment limit to maximum dominion. Temples, national rules, Pretender design, sites, and mod commands can alter the system.

Holy Points create several strategic distinctions:

- a sacred may be affordable but unavailable;
- sacred queues can accumulate behind the cap;
- buying ordinary troops can use local resources and RP left stranded by the Holy limit;
- higher maximum dominion can be both religious resilience and production capacity;
- capital-only sacreds concentrate risk at the capital even when other forts have spare resources.

## Queue mechanics and diagnosis

Recruitment orders can fail or wait for different reasons:

| Symptom | Likely gate |
| --- | --- |
| Unit cannot be added | Insufficient treasury, ineligible location, unrest 100+, or limit reached |
| Unit remains queued | Resource, RP, Holy Point, or limited-recruit shortage |
| Commander does not appear | Commander Point shortage, eligibility, gold, or recruitment disruption |
| Resources remain while queue stalls | RP, Holy, commander, or unit-specific cap |
| RP remains while queue stalls | Resources, Holy, or local eligibility |
| Province captured yet recruits fought | Recruitment resolved at step 3 before movement battle |
| Recruits trapped inside fort | Recruitment completed before siege control changed |

The queue should be read as a production plan constrained by several ledgers, not as a single purchase list.

# Part V: Unrest and Coercive Economy

## What unrest does

Officially, unrest:

- reduces income;
- reduces resources;
- prevents recruitment at 100 or greater;
- reduces Blood Hunting success;
- obstructs patrol detection;
- is capped at the lesser of 500 or population divided by 10.

It can rise through:

- random events;
- spies and agitators;
- Blood Hunting;
- sites;
- targeted spells;
- globals;
- pillaging;
- hostile dominion and special effects.

It can fall through:

- patrolling;
- Province Defence;
- Order;
- sites;
- events;
- other national, unit, or magical effects.

## Income and resource damage

```text
income multiplier = 1 / (1 + 0.02 x unrest)
resource multiplier = 1 / (1 + 0.01 x unrest)
```

Income is twice as sensitive in the denominator. At unrest 50, the province retains half its income but about two-thirds of its resources.

## Recruitment shutdown

At unrest 100, no ordinary units or commanders can be recruited. This creates a production-denial objective:

- unrest attacks can neutralise a fort without breaching its walls;
- Blood Hunting can disable its own patrol and recruitment base;
- a province may still show resources while being unable to recruit;
- reducing unrest at step 39 is too late to restore step-3 recruitment that month.

## The unrest cap

```text
maximum unrest = min(500, population / 10)
```

A province with zero population cannot retain unrest. Population loss can reduce the numerical cap while destroying nearly every ordinary economic reason to own the province.

## Patrolling

The main manual gives individual patrol strength as:

```text
individual patrol strength =
  (Precision + Map Move) / 20
```

Flying units use 30 in place of Map Move. Commanders are doubled. Undisciplined and Mindless units are halved.

The total search strength is reduced by half the province's unrest, capped at 100, and gains Province Defence patrol strength beginning at PD 15.

The same patrol force must often satisfy several tasks:

- lower unrest;
- protect Blood Hunters;
- discover scouts, spies, and raiders;
- remain strong enough to survive a discovery battle;
- avoid destroying too much population.

High nominal patrol strength is not the same as a safe patrol. A stealth force that is discovered may still defeat the patrol.

### Community sub-formulas

Current community documentation describes a multi-stage unrest reduction process involving:

1. a baseline affected by friendly candles and PD;
2. an Order/Turmoil-dependent proportional reduction;
3. patrolling.

It also reports that unrest reduces Recruitment Points and Commander Points by one percent per point, with the Commander Point reduction rounded down. The current page states the result but does not publish a 6.36 boundary table, save, or test setup. The precise breakpoints remain queued under R-011.

That wording admits two materially different readings for a small integer pool: round down the **amount lost**, or round down the **capacity remaining**. For a one-point Commander Point pool, the first reading preserves the point until the recruitment shutdown; the second can remove it as soon as unrest rises above zero. The page does not state which intermediate is rounded and does not provide the small-pool observations needed to decide between them.

If the intended community rule is "round down the amount lost," its test predictions are:

| Ordinary pool | First predicted loss | Second predicted loss | Capacity before unrest 100 |
| ---: | ---: | ---: | ---: |
| 1 | Unrest 100 | - | 1 |
| 2 | Unrest 50 | Unrest 100 | 1 from unrest 50-99 |
| 3 | Unrest 34 | Unrest 67 | 1 from unrest 67-99 |

This is a **candidate boundary table**, not a promoted game rule. Its value is diagnostic: a single version-labelled observation at one of those thresholds can support or reject the interpretation far more efficiently than an anecdote from a high-unrest province.

This distinction matters most for the tiny Commander Point pool. A one-point rounding decision can change a mage from a one-month recruit into a multi-month project. Until the breakpoints are reproduced, use three tiers of certainty:

| Claim | Publication state |
| --- | --- |
| Unrest 100 or more prohibits ordinary unit and commander recruitment | Official |
| Unrest reduces ordinary Recruitment Points before shutdown | Current community reference |
| Unrest also reduces Commander Points | Current community reference |
| Exact first-loss threshold for a 1-, 2-, or 3-point pool | Test pending |

The recruitment screen is authoritative for orders. A written forecast near an unrest boundary should preserve a spare month rather than assuming the most favourable rounding.

## Pillaging and raiding

Pillage:

- raises unrest;
- kills population;
- reduces supplies;
- gives gold and temporary food to the pillaging army;
- becomes stronger with larger, faster, and larger-sized forces;
- particularly favours barbarians and units with Fear.

The temporary supplies last one month.

A Raid combines movement with reduced-strength pillage. It requires a commander with Pillager and an army with Map Move 20 or more. Only Pillager units contribute, at half pillage strength, and the force must win any resulting battle before pillaging succeeds.

### Strategic uses

Pillage and raid actions can:

- suppress income before step 38;
- raise a fort province toward recruitment shutdown;
- damage future population and supplies;
- feed an army for the current month;
- force patrols and defensive movement;
- create tax-trace breaks.

They can also destroy value that the attacker expects to conquer. The action is most coherent when denial matters more than future ownership.

# Part VI: Supplies, Armies, and Logistics

## Supply is a location check

Supply is not a national stock. An army consumes the supply available in its current situation.

The decisive logistical questions are:

- Where will the army be when starvation resolves?
- Which fort projects the highest supply there?
- What scales and population will remain after conquest, battle, and pillage?
- Is the army outside a fort, inside a fort, or trapped in a siege?
- Which units consume supply despite appearing small or inexpensive?

## Population-based supply

```text
base population supply =
  first 15,000 / 30
  + population above 15,000 / 60
```

Growth or Death modifies the result first. Temperature deviation modifies it second.

| Population | Base supply before scales |
| ---: | ---: |
| 3,000 | 100 |
| 7,500 | 250 |
| 15,000 | 500 |
| 21,000 | 600 |
| 30,000 | 750 |

The lower marginal supply above 15,000 mirrors the declining RP value of very large populations.

## Fort-based supply

The manual's stated formula is:

```text
fort supply =
  (Administration x 6) / (Distance + 1)
```

The maximum distance is four. Only the largest nearby fort contribution applies.

### Official internal conflict

The same manual also prints a distance multiplier table of 400%, 200%, 133%, 100%, and 80% at distance zero through four. Those percentages correspond to `Administration x 4 / (Distance + 1)`, not the printed multiplier of six. Its worked example gives only 30 supply from an Administration-30 Castle at distance three, agreeing with the table but disagreeing with the formula, which produces 45.

| Distance | Printed `Admin x 6` formula for Admin 30 | Printed percentage table for Admin 30 |
| ---: | ---: | ---: |
| 0 | 180 | 120 |
| 1 | 90 | 60 |
| 2 | 60 | about 40 |
| 3 | 45 | 30 |
| 4 | 36 | 24 |

A second official sentence says an Administration-50 fort contributes 150 to an adjacent province. That agrees with the multiplier-of-six formula at distance one and disagrees with the percentage table. The manual contains two internally coherent calculations, each supported by at least one example.

The current community population reference uses the multiplier-of-six formula and gives a Palisades example at distance two. It is useful corroboration but not a published controlled reproduction across all five distances. R-012 remains open.

These three representations cannot all be correct under the same definition of distance. The safe publication policy is:

- preserve the formula as the stated rule;
- describe the example conflict;
- use the in-game displayed supply for operational orders;
- reproduce every distance from zero through four in 6.36.

For forecasts, the two printed systems can be carried as a documentary interval:

```text
lower printed candidate = Administration x 4 / (Distance + 1)
upper printed candidate = Administration x 6 / (Distance + 1)
```

This interval is not a claim that the executable must lie between the two. It is a compact way to expose how much of a supply plan depends on the unresolved multiplier. The disagreement is a constant one-third of the larger candidate, so an army that fits only under `x6` is not safely supplied by the documents alone. The range, the four-province limit, and the rule that only the single highest nearby fort contribution applies are not part of the conflict.

## Supply usage

The main manual describes usage by physical size:

| Unit | Ordinary supply use |
| --- | ---: |
| Size 0 | 0 |
| Size 1-2 | 0.5 |
| Size 3 | 1 |
| Size 4 | 2 |
| Size 5 | 3 |
| Size 6 | 4 |

Animals use half the ordinary amount. Rider and mount both consume supply. Nature magic indirectly contributes 10 supply per path level.

Special abilities, forms, national rules, and modded effects can change ordinary expectations.

## Starvation selection and effects

When usage exceeds supply, the engine selects troops whose combined usage is approximately the deficit.

First selection:

- the unit becomes Starving;
- morale falls by 4;
- disease chance is 5%.

Selection while already Starving:

- disease chance rises to 50%.

Appropriate survival skill:

- 50% chance to be completely unaffected;
- a separate 50% chance to avoid disease.

When supply becomes sufficient, Starving ends. Disease does not.

### Timing

Starvation resolves at step 40, after all ordinary battles and immediately before upkeep. A newly overextended army normally fights this month's battle without the new Starving condition, then carries the penalty into the next order phase.

This makes starvation a delayed logistical debt. It is easy to ignore after a victory and expensive when the next battle arrives.

### Commander uncertainty

Commanders are commonly described as being fed before troops. That is a priority claim, not the same thing as categorical immunity. The main manual does not grant all commanders a general exemption, and no current controlled sample has exhausted the troop pool and shown the commander-selection boundary. Generic commander immunity remains test pending.

The wording *fed first* is safest read as a ranking within the eligible selection pool. It cannot support *never starves*: once the deficit exceeds the consumption of lower-priority eligible units, the selection process must either reach commanders, leave part of the deficit unmatched, or apply another undocumented exception. No source in the current evidence set demonstrates which branch occurs. Animals being described as fed last is the same kind of priority claim, not proof that every animal starves before any ordinary troop.

### Need Not Eat is the decisive explicit tag

The official Modding Manual gives a firmer rule for individual objects: `#neednoteat` means the monster consumes no supplies and cannot starve. It also explains how to create a creature that still consumes supplies but cannot starve, proving that consumption and starvation eligibility are distinct properties.

The pinned 6.35 object snapshot reinforces that distinction:

- 985 rows carry Need Not Eat;
- 47 rows combine Need Not Eat with Appetite;
- several Undead and Demon rows do not carry the Need Not Eat field explicitly.

Object counts include helpers and non-recruitable forms, so they are not army demographics. Their value is structural: class labels such as Undead, Demon, Inanimate, or commander cannot safely substitute for the actual food and starvation fields.

Official update 6.18 adds the transformation boundary: changing into a non-eating entity removes the Starving condition. The correction does not document the reverse direction, temporary battle shapes, or a universal commander-priority rule. R-013 remains in progress.

Official update 6.35 repaired Supply Usage failing to refresh when magic items were changed. The supply formula did not change, but the correction affects how evidence should be gathered. Screenshots or observations from earlier versions may show a stale usage total after equipment changes. Under the 6.36 baseline, recheck the current Supply Usage after equipping or removing any item that affects size, appetite, supply production, a mount, or a form. The corrected display is the intended operational total, although it still does not prove selection priority.

### Logistics audit for unusual units

For any expensive commander, mount, transformed unit, or summoned army, inspect in this order:

1. current Supply Usage;
2. Need Not Eat or Appetite on every component;
3. rider and mount separately;
4. current Starving and Disease conditions;
5. survival skill in the destination terrain;
6. whether a shape change occurred before starvation resolution;
7. the displayed fort and population supply in the destination.

This avoids the two most common category errors: assuming that a unit which consumes supply must be able to starve, and assuming that a unit which cannot starve contributes no supply burden.

## Siege supply

A besieged fort uses Supply Storage divided by the number of consecutive siege turns:

```text
available interior supply =
  storage / siege turn number
```

Example for 300 storage:

| Siege turn | Interior supply |
| ---: | ---: |
| 1 | 300 |
| 2 | 150 |
| 3 | 100 |
| 4 | 75 |
| 5 | 60 |
| 10 | 30 |

This is different from Administration-based supply projection. Storage sustains defenders inside the fort; Administration helps the surrounding province network.

### Siege logistics as a clock

Even an unbreached wall can become untenable through:

- falling interior supplies;
- cumulative starvation;
- disease;
- upkeep and lost exterior income;
- inability to recruit or move normally;
- the approach of a storm force.

The fort's wall clock and supply clock should be tracked separately.

# Part VII: Infrastructure

## Forts, temples, and laboratories

Each building converts a province in a different dimension.

| Building | Converts the province into |
| --- | --- |
| Fort | A protected recruitment, resource, tax, and logistics node |
| Temple | A dominion-production and preaching node |
| Laboratory | A research, ritual, forging, gem, item, and site-access node |

The standard temple and laboratory each cost 600 gold. Fort stages have separate costs and times. Nations and terrain can alter all of these.

## Construction timing

Buildings complete at hosting step 35.

This is later than:

- research at step 2;
- recruitment at step 3;
- forging at step 5;
- preaching and Throne claims at steps 6-8;
- rituals at step 10;
- site searching at step 14;
- ordinary battles and storming at steps 26-27.

This gives the following results:

- a new lab cannot support research, forging, or ritual casting that month;
- a new temple cannot improve that month's ordinary preaching;
- a new fort cannot expand this month's recruitment or protect against battles already fought;
- infrastructure is operational from the following order phase.

## Construction and demolition

Officially:

- any commander can construct a fort;
- a sacred commander is required for a temple;
- a mage is required for a laboratory;
- any commander can demolish a fort or laboratory;
- demolition takes one month;
- temples cannot be demolished by order;
- enemy temples are destroyed automatically upon conquest;
- a fort cannot be demolished while under siege.

The construction order itself consumes the commander's month. The economic cost includes both gold and commander-time.

## Standard fort progression

| Fort | Stage cost | Stage time | Admin | Commander Points | Recruitment bonus | Storage | Wall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Palisades | 1,000 | 5 | 15 | +0 | +50% | 150 | 200 |
| Fortress | 600 | 3 | 30 | +1 | +75% | 750 | 500 |
| Castle | 600 | 3 | 45 | +1 | +100% | 2,500 | 1,000 |
| Citadel | 600 | 3 | 60 | +2 | +125% | 7,500 | 1,500 |
| Grand Citadel | 1,000 | 5 | 70 | +2 | +150% | 10,000 | 2,000 |

Statistics replace the previous stage rather than adding to it.

The standard maximum is:

- Early Age: Fortress;
- Middle Age: Castle;
- Late Age: Citadel.

Primitive and advanced national access can differ. Masons can construct one level above the ordinary national limit. A Grand Citadel requires Citadel access and a Mason.

## Fort valuation

A fort can create:

1. full local resource use;
2. adjacent resource draw;
3. local income through Administration;
4. Recruitment Point bonus;
5. Commander Point bonus;
6. regional supply;
7. siege storage;
8. wall integrity and protected interior;
9. national recruitment access;
10. a tax-trace anchor;
11. a secure laboratory or temple location;
12. a movement and reinforcement node.

No single payback formula captures all twelve.

### Fort question set

Before construction:

- Which units and commanders become recruitable?
- Which local pool will bind after the fort is complete?
- How many adjacent potential resources are eligible?
- Does another planned fort remove a major donor?
- What tax region will this fort anchor?
- What routes and provinces fall within supply range?
- How many turns until the first new mage or army leaves?
- Can the province be held during construction?
- Is the builder's command-turn scarce?
- What military force is delayed by the gold payment?

## Laboratories

Official functions:

- permit Research;
- permit ritual casting;
- permit access to the national pool of gems, slaves, and items;
- serve as gem collection points;
- enable site functions that require a lab.

Laboratories are strategic concentration points. Losing one can strand mages away from the national pool even when the nation still owns gems elsewhere.

### Laboratory risk

A lab attracts:

- researchers;
- gems and slaves;
- forged items;
- ritual casters;
- valuable site recruits.

The 600-gold structure can protect assets worth far more than its price. Defence should be based on the value concentrated there, not only the cost of replacing the laboratory.

## Temples

Official functions:

- ordinary dominion spread for most nations;
- preaching bonus;
- Blood Sacrifice access where the nation allows it;
- religious and national mechanics tied to temple count or location.

Only one temple can exist in a province. Capture destroys an enemy temple automatically.

Temples belong fully to the dominion volume, but their economic effect begins here:

- they cost gold and sacred commander-time;
- maximum dominion and Holy Points can affect sacred throughput;
- temple loss can weaken recruitment, candles, preaching, and special national systems;
- temples in exposed provinces can be destroyed without a separate demolition delay.

# Part VIII: Siege and Fort Control

## Province exterior and fort interior

A besieged province can have divided control:

- the besieger controls the exterior;
- the defender retains the fort interior;
- armies, laboratories, temples, and recruitment must be interpreted by location and ownership rules rather than a single flag.

This partial ownership affects:

- income and recruitment;
- movement and retreat;
- assassination and stealth;
- supply;
- siege contribution;
- the eventual reclaim-province step.

## Reducing walls

Official formulas:

```text
reduction strength = Strength squared
repair strength = Strength squared / 2
```

Flying doubles both contributions.

Repair penalties:

- Mindless: one-eighth of calculated value;
- Animal: half;
- Undisciplined: half.

Only forces whose commanders remain on Maintain Siege contribute.

### Squaring rewards strength

Strength-squared means one stronger unit can contribute more than several weaker units with the same total linear Strength.

| Strength | Reduction contribution | Base repair contribution |
| ---: | ---: | ---: |
| 5 | 25 | 12.5 |
| 10 | 100 | 50 |
| 15 | 225 | 112.5 |
| 20 | 400 | 200 |
| 30 | 900 | 450 |

Flying doubles the result. Special siege abilities and modded values can further alter practical contribution.

### Wall resolution

Each turn:

- total reduction is compared with total repair;
- the difference damages or repairs wall integrity;
- repair cannot exceed original wall integrity;
- an unbesieged damaged fort fully restores.

The defender receives exact wall information. The attacker normally receives a descriptive estimate, creating an information problem around the storm date.

## Storm timing

A fort can be stormed only after wall integrity reaches zero and the next order phase presents the Storm Castle order.

Storming resolves at step 27, after movement battles at step 26. This has several immediate consequences:

1. a relieving army may arrive;
2. the besiegers fight it first;
3. surviving storm commanders and assigned troops attack the fort;
4. a storm commander killed before the gate battle contributes no troops to the storm.

Maintain Siege and Storm Castle are commander orders. A commander performing another action does not supply siege strength merely because it remains in the province.

## Fort defenders

Forts supply Castle Guards and Wall Defenders:

- their number depends on fort level;
- they replenish for each fight like PD;
- they add repair strength;
- Wall Defenders have unlimited ammunition, extra range, and wall protection;
- they are fort defence, not the same system as Province Defence.

The shared word “defence” is a recurring source of confusion:

| Term | Meaning |
| --- | --- |
| Province Defence | Gold-purchased local force attached to province control |
| Wall integrity or fort Defence | Damage required before storming |
| Castle Guards and Wall Defenders | Fort-generated troops in a storm battle |
| Unit Defence skill | Tactical chance to avoid melee attacks |

# Part IX: Province Defence

## Cost curve

The first point is free. Every later point costs its new level.

```text
total cost to PD n =
  2 + 3 + ... + n
  = n(n + 1)/2 - 1
```

| PD | Total cost | Additional cost from prior listed row |
| ---: | ---: | ---: |
| 1 | 0 | - |
| 5 | 14 | 14 |
| 6 | 20 | 6 |
| 10 | 54 | 34 |
| 15 | 119 | 65 |
| 20 | 209 | 90 |
| 25 | 324 | 115 |
| 30 | 464 | 140 |
| 40 | 819 | 355 |
| 50 | 1,274 | 455 |
| 100 | 5,049 | 3,775 |

The convex curve means “another ten PD” is not a consistent investment. Going from 1 to 10 costs 54; going from 40 to 50 costs 455.

## What PD provides

Officially:

- level 1 provides a commander and troops;
- further levels add troops;
- level 20 adds new commander and troop types;
- additional benefits occur at 10, 15, and 20;
- every full 10 points reduces unrest by 1 per turn;
- stealth detection begins at 15;
- patrol strength is `PD - 14` from that point;
- maximum PD is 100;
- no upkeep is charged;
- the force fully returns after battle if the province is retained.

The actual roster is national. One nation's PD may deter a raider that walks through another nation's equal investment.

## Population support and permanence

Each PD point requires 10 population. Unsupported PD is reduced at hosting step 61.

PD cannot be voluntarily lowered. It is reduced by:

- insufficient population;
- capture, which wipes it;
- disciple-game relinquishment, which removes 25%;
- special exceptions for some populationless nations.

Because the spending is irreversible while control is retained, excessive PD can trap gold in the wrong place after a border moves.

## Roles of PD

### Raid tax

Low or moderate PD forces an attacker to bring a credible commander and force rather than a single opportunist.

### Alarm and information

A battle report reveals attacker composition, script, and direction. Even a losing PD force can improve the next decision.

### Unrest control

Every ten points creates recurring unrest reduction, though buying PD solely for this purpose must be compared with a mobile patrol.

### Stealth detection

From 15 onward PD contributes patrol strength. Detection is not capture; the revealed stealth force may still win.

### Battle support

PD can combine with a local army, fort defenders, terrain, and battle magic. Its expendability can buy time for mages whose spells decide the fight.

## Why PD is not an army

PD:

- cannot move;
- cannot choose a different strategic target;
- cannot retreat into a future offensive;
- may have poor leadership, morale, equipment, or formation;
- scales in gold cost faster than it scales in quality;
- disappears on capture.

High PD can still be correct at a throne, capital approach, blood centre, or mage concentration. The decision must price the attack it is intended to defeat.

### Community thresholds

Some guides recommend values such as 6 or 11 to prevent particular event outcomes or deter generic raiders. Such numbers are rules of thumb, not universal mechanics. Event pools, nation, mods, map settings, and attacker design can change the result.

# Part X: Sites, Gems, and Magical Capital

## Site frequency and terrain

The main manual states that sites are more common in terrain such as:

- forests;
- wastes;
- deep seas;
- mountains and unusual cave terrain.

They are less common in plains and farmlands.

This is a probability, not a guarantee. Search planning should combine:

- terrain;
- path availability;
- prior searches;
- national site frequency;
- opportunity cost of the mage-turn;
- value of remote search spells;
- safety of the searching mage.

## Search difficulty

Hidden sites have difficulty 1 through 4. A mage manually searching a path finds sites in that path up to the mage's level. Path 4 is the highest ordinary requirement.

Examples:

- N1 finds difficulty-1 Nature sites.
- N3 finds difficulty 1-3 Nature sites.
- N4 finds every Nature site detectable by ordinary path search.
- An N3 mage says nothing about Fire, Death, or Glamour sites.

Remote path-search rituals reveal all sites of their path. Acashic Knowledge reveals all paths.

## Site benefits and harms

Sites may provide:

- monthly gems;
- gold;
- resources or supplies;
- units and commanders;
- laboratories, temples, forts, or discounts;
- rituals or enter-site orders;
- path bonuses;
- scale or dominion effects;
- unrest, disease, population loss, or other harms.

A harmful undiscovered site can still operate. Discovery explains a problem; it does not necessarily create it.

### Ownership and national recruitment

A captured site that recruits another nation's national unit does not normally grant that recruit to the conqueror. The conqueror can still collect the site's gem income where applicable.

Some sites require a laboratory before recruitment or another function becomes available.

## Gem income and mage-turn economy

Gems accumulate nationally and can be converted into:

- rituals;
- summons;
- forged items;
- empowerment;
- battle magic;
- global enchantments;
- trades and diplomacy.

The site-search decision has an expected-value structure:

```text
expected search value =
  probability of discovery
  x expected monthly and strategic value
  x expected remaining turns
  - mage-turn cost
  - travel and risk
```

The formula is not intended to assign fake precision. It identifies the relevant terms. A single rare site can dominate the average, and information about a searched path has future value even when nothing is found.

### Search records

Every serious game benefits from recording:

- province;
- terrain;
- path searched;
- manual or remote method;
- path level;
- discovered sites;
- remaining unsearched paths;
- laboratory requirement;
- hostile or passive effects.

Without a record, mages repeat searches or leave valuable paths untouched.

# Part XI: Blood Economy

## Blood slaves are produced, not passively collected

Blood magic substitutes an active extraction system for ordinary gem-site income. Blood Hunting consumes a commander order and damages the province through unrest and possible population loss or attacks.

The economic chain is:

```text
blood mage-turns
  + suitable population
  + patrol strength
  + dominion security
  -> blood slaves
  -> forging, rituals, summons, battle magic, and sacrifice
```

## Official hunting checks

The main manual gives:

```text
Blood check success =
  10% + 30% x Blood level

population check success =
  population / 75 percent

unrest failure chance =
  unrest / 4 percent
```

All three must succeed.

If they do:

```text
slaves = d6 + Blood level
unrest gained = d(slaves x 3 + 4)
```

If any fails:

```text
slaves = 0
unrest gained = d6 - 1
```

At 7,500 population, the population check reaches a nominal 100%. At Blood 3, the Blood check reaches a nominal 100%. Existing unrest can still cause failure.

Site frequency changes average yield by 0.5 slaves for every five percentage points away from 50%.

## Dominion and retaliation

Commoners may attack Blood Hunters. Strong friendly dominion makes the sacrifice appear religiously legitimate; the manual states that dominion 10 leaves almost no resistance.

The risk extends beyond lost slaves:

- the hunter can be injured or killed;
- bodyguards consume gold, supply, and patrol capacity;
- a hidden enemy can exploit the concentration;
- hostile dominion can make a previously safe centre unstable.

## The blood-province cycle

A functioning centre balances:

1. hunters create slaves and unrest;
2. patrols remove unrest and detect hostile infiltrators;
3. population and income absorb the damage;
4. labs provide pool access and ritual logistics;
5. forts or armies protect the investment;
6. replacement hunters and patrollers sustain throughput.

If patrol strength is insufficient, unrest reduces success, income, resources, and eventually recruitment. Adding more hunters can then reduce total output.

### Rule of thumb versus rule

Community guides often estimate that roughly 25 patrol strength supports each Blood-3-equivalent hunter under ordinary conditions. This is a planning heuristic, not an official fixed ratio. Patrol efficiency, population loss, unrest, dominion, site frequency, hunter abilities, and national mechanics change the result.

## Measuring the blood economy

Useful records:

| Measure | Purpose |
| --- | --- |
| Slaves per hunter-turn | Compares extraction efficiency |
| Unrest before and after hosting | Reveals patrol shortfall |
| Population trend | Detects hidden long-term collapse |
| Lost research per month | Prices mage-turn diversion |
| Patrol gold and upkeep | Prices support force |
| Hunter and lab losses | Prices security failures |
| Slaves converted to effects | Distinguishes stockpiling from power |

The goal is not the largest slave count. It is the most decisive magical output produced without collapsing the rest of the state.

# Part XII: Economic Timing Through Hosting

## The state-economy chain

The most important monthly sequence is:

| Step | Event | Economic reading |
| ---: | --- | --- |
| 3 | Recruitment | Existing infrastructure and local capacity create units first. |
| 18 | Blood Hunting | Slaves and hunting unrest are generated early. |
| 24-27 | Movement, battles, storming | Control and siege state change. |
| 29-33 | Events and later battles | Income provinces can still be altered. |
| 35 | Construction | New buildings become part of the end-state, too late for earlier production. |
| 37 | Pillage | Immediate population, unrest, and supply damage occurs. |
| 38 | Income | Collection uses the post-conquest, post-pillage state and tax trace. |
| 39 | Unrest changes | Patrolling, Order, and related adjustments primarily prepare next month. |
| 40 | Starvation | Armies acquire logistical penalties after battle. |
| 41 | Upkeep | Recurring military costs are charged after income. |
| 42-44 | Dominion and site effects | Longer-term provincial state changes arrive. |
| 53-54 | Reclaim and conscription | Late ownership correction and automatic PD prepare the next turn. |
| 61 | Unsupported PD reduction | Population-depleted provinces lose excess PD at the end. |

## Worked timing cases

### Emergency recruitment under attack

- Units are queued during the order phase.
- Recruitment resolves at step 3.
- An enemy army arrives and fights at step 26.
- The new units defend.
- They had no opportunity to receive a new strategic order.

### New laboratory under invasion

- A mage is ordered to build a lab.
- Research, forging, rituals, and battles all occur before step 35.
- The lab completes only if the builder and province still satisfy the construction result.
- Its practical magical use begins next order phase.

### Pillage before collection

- A province changes hands at step 26.
- The winner pillages at step 37 if the relevant order succeeds.
- Pillage damage occurs before income at step 38.
- The new owner may collect less than the pre-battle province panel suggested.

### Patrol after income

- A Blood Hunt at step 18 raises unrest.
- Income is collected at step 38.
- Patrol and ordinary unrest alterations occur at step 39.
- The province may pay reduced income this month even if the patrol restores order moments later.

### Siege relief before storm

- The wall was already at zero when orders were written.
- A relief army moves and battles at step 26.
- Surviving storm commanders attack at step 27.
- Defeating or killing them in the relief battle prevents or weakens the storm.

# Part XIII: Strategic Frameworks

## Expansion income versus expansion burden

A conquered province can provide:

- income;
- resources;
- Recruitment Points;
- supplies;
- independents;
- sites;
- tax trace;
- movement position.

It also creates:

- a border to defend;
- unrest to manage;
- commander travel;
- potential tax isolation;
- a target for raids;
- a possible need for PD, patrol, lab, temple, or fort.

The correct expansion measure is not provinces per turn alone. It is useful, connected, defensible economic mass acquired per loss and per commander-turn.

## Infrastructure tempo

Infrastructure has a delay chain:

```text
decide and pay
  -> construction months
  -> completion at step 35
  -> next order phase
  -> first enabled recruitment or magical order
  -> travel to the war
```

A fort whose first mage reaches the front in twelve months belongs to a different strategic horizon than emergency troops recruited now.

### Fort-now test

Build when most of the following are true:

- the commander or troop roster is valuable;
- capacity will be used continuously;
- the location anchors tax or supply;
- the province can be defended through construction;
- the expected game horizon allows military conversion;
- no nearer timing attack requires the gold;
- resource geometry is favourable;
- the nation needs another mage or commander stream.

Delay when:

- the war is decided before completion;
- the site cannot be held;
- the desired roster remains gold-limited elsewhere;
- adjacent forts remove most resource gain;
- the builder or gold has a more urgent conversion.

## Mage-turn accounting

A mage can usually do one major strategic job per month:

- research;
- search;
- forge;
- cast a ritual;
- Blood Hunt;
- build a lab;
- move;
- participate in battle;
- perform a special order.

The cost of a ritual is not limited to gems. It also includes:

```text
ritual cost =
  gems
  + caster-turn
  + laboratory and position requirements
  + risk
  + research or other work displaced
```

This accounting becomes decisive for small mage corps and Blood nations.

## Static and mobile gold

Gold can become:

- **static power:** PD, forts, temples, labs;
- **mobile power:** troops, commanders, mercenaries;
- **productive power:** mages, researchers, infrastructure;
- **religious power:** temples, priests, sacred throughput;
- **insurance:** treasury reserve.

An efficient state carries a deliberate mix. Too much static power loses the field. Too much mobile power can lack replacement, research, and safe logistics. Too much productive power can die before repayment.

## Denial and recovery

Economic warfare targets conversion rather than ownership alone.

High-value actions include:

- cutting a tax trace;
- besieging a mage fort;
- raising unrest to 100;
- killing the patrols of a blood centre;
- taking a lab with stored items or positioned casters;
- forcing an army into poor supply;
- damaging population that supports PD and RP;
- building an adjacent fort that changes resource geometry;
- repeatedly raiding the same reconstruction corridor.

Recovery priorities:

1. restore tax trace and province control;
2. prevent recruitment shutdown;
3. preserve or rebuild irreplaceable mage production;
4. feed armies and halt disease;
5. reconnect labs and gem access;
6. replace mobile defence before rebuilding luxury infrastructure.

# Part XIV: New-Player Operational Guide

## First-turn provincial reading

For each owned province:

1. Read population, income, resources, supplies, unrest, terrain, and PD.
2. Identify whether income has a valid fort trace.
3. Check the recruit roster before buying infrastructure.
4. Note site searches already completed.
5. Compare the province's best role with its exposed position.

## Recruitment checklist

- Is the unit recruitable here?
- Is gold available now?
- Are resources sufficient?
- Are Recruitment Points sufficient?
- Is a commander using the local Commander Point?
- Is the unit sacred or limited?
- Will unrest reach or remain at 100?
- Is the army's future supply sufficient?
- Is there leadership for the recruited troop type?
- Does the queue create a usable army package?

## Army logistics checklist

- Current Supply Usage.
- Destination population and scales.
- Highest nearby fort contribution.
- Expected pillage or ownership change.
- Survival skills.
- Mounted and large-unit consumption.
- Existing Starving or disease conditions.
- Siege interior versus exterior.
- Retreat province supply.

## Building checklist

- Correct constructor type.
- Gold after recruitment and reserve.
- Completion date.
- Step-35 timing.
- Province security.
- Roster or magical function unlocked.
- Tax, supply, and resource geometry.
- Commander-turn cost.

## End-of-host checklist

- Income and upkeep totals.
- Queued recruits.
- New unrest.
- Tax-trace breaks.
- Starving and diseased units.
- Fort wall and siege duration.
- New sites and lab requirements.
- Population losses.
- PD reductions.
- Empty or overloaded recruitment centres.

# Part XV: Expert Diagnostics

## Warning indicators

| Indicator | Likely problem |
| --- | --- |
| Large treasury, weak army | Local capacity, commander throughput, logistics, or delayed conversion |
| Resources unused every month | RP, gold, Holy limit, or unsuitable roster |
| RP unused every month | Resources, sacred cap, or recruit-mix problem |
| Mages available but research stagnant | Movement, searching, forging, hunting, combat, or lab denial |
| Income drops without province loss | Tax trace, unrest, scales, dominion, event, or Administration change |
| Blood output falls as hunters increase | Unrest and patrol saturation |
| Armies win then decay | Supply debt and disease |
| Fort never produces enough | Wrong roster, resource geometry, gold shortage, Commander Points, exposure |
| High PD still loses | National roster, magic, morale, raider design, or convex overinvestment |
| Siege stalls unexpectedly | Commanders left Maintain Siege, defender repair, strength composition, relief activity |

## Ratios worth recording

No ratio is universal, but consistent tracking reveals a nation's own failure modes.

- upkeep as a percentage of gross income;
- unspent resources and RP at major forts;
- commander slots used per turn;
- research per mage-turn;
- gems converted per month;
- slave yield per hunter-turn;
- unrest change per blood centre;
- turns from fort payment to first useful output;
- gold lost to disconnected tax regions;
- mobile army value versus static PD spending;
- siege reduction per supplied unit.

## Decision ledger

For major investments, record:

| Field | Example question |
| --- | --- |
| Goal | What military or magical capability is being created? |
| Cost | Gold, gems, mage-turns, commander-turns, upkeep |
| Bottleneck | Which local or national pool limits output? |
| Completion | When does the first useful effect occur? |
| Risk | What raid, siege, assassination, or diplomacy can interrupt it? |
| Alternative | What is the best use of the same resources? |
| Exit | Can the investment be repurposed if the front changes? |

This turns economic planning into falsifiable reasoning rather than habit.

# Part XVI: Modded Economy

## Read the global layer once

Book IX, Section 7 is the authoritative table for DE's six global commands. It records the exact source values, their vanilla defaults, and the result under the frozen load order. The Turn and Economy Quick Reference repeats only the final values because they are needed during play.

The economic consequence is straightforward. DE changes the income weight of Order/Turmoil, Productivity/Sloth, and Growth/Death; changes monthly population movement under Growth and Death; and strengthens the event-frequency effect of Fortune and Misfortune. Divinitus does not later redefine those globals.

## Local changes still decide the real economy

The global layer is only the starting point. The two mods also alter unit costs and upkeep, recruitment limits, sites, event income, supplies, forts, temples, research output, gem flow, and national mechanics. Those changes belong to the final object or nation, not to a universal economy formula.

Accordingly, a modded economic claim needs a ruleset label and an object boundary. "Growth is worth more under DE" is a global statement. "This fort produces more useful mages" requires the final national roster, costs, site access, and any Divinitus event layer. Book IX and the machine-readable catalogue provide that source record; nation dossiers provide the strategic application.

# Part XVII: Contradictions and Controlled Tests

## Known documentary conflicts

### Growth and Death income

- Main manual revision 2: 1% income per step.
- Modding Manual 6.34: default `#deathincome 2`.
- Official announcements through 6.36: no later change to the general default.

**Publication state:** resolved for unmodded 6.36 at 2% per step. The newer explicit official default supersedes the older table entry. DE 2.16 independently pins the same income value.

### Order and Turmoil resources

- Main manual revision 2: 2% resources per step.
- Official announcements through 6.36: no general change to this scale effect.
- Unsourced or historical three-percent tables do not override the official value.

**Publication state:** resolved for the unmodded 6.36 publication baseline at 2% per step. Integer rounding remains part of the separate R-008 question.

### Fort supply distance

- Main-manual formula: `(Administration x 6)/(Distance + 1)`.
- Printed multiplier table: 400%, 200%, 133%, 100%, 80%, equivalent to a multiplier of four.
- Worked example: Administration 30, described as three provinces away, adds 30 and agrees with the table.
- Adjacent example: Administration 50 adds 150 and agrees with the multiplier-of-six formula.

**Publication state:** internally inconsistent. The current community reference follows the multiplier-of-six formula, but a versioned reproduction at distances zero through four is still required.

### Recruitment Points

- Revision-2 main manual: base 20 and five listed bands.
- Older community reference: different base and bands.

**Publication state:** revision-2 formula wins; verify rounding only.

### PD 15 patrol strength wording

The manual says detection starts at 15 and that each point “above 15” adds one patrol strength, then gives PD 25 as patrol strength 11. The example corresponds to `PD - 14`, counting level 15 as one.

**Publication state:** use the numerical example and formula `PD - 14`; note wording discrepancy.

## Controlled-test programme

### Test E1: scale-income matrix

Create identical provinces under every Order/Turmoil, Productivity/Sloth, temperature, and Growth/Death value. Record:

- population;
- fort Administration;
- unrest;
- displayed income;
- treasury change;
- rounding.

Run unmodded and the frozen combined mod set.

### Test E2: resource matrix

Use a fixed terrain and resource value. Vary:

- Order/Turmoil;
- Productivity/Sloth;
- unrest;
- fort stage;
- adjacent fort;
- shared resource donor;
- enemy ownership;
- land/sea boundary.

Record potential, displayed, spendable, and queue behaviour.

### Test E3: Recruitment Point boundaries

Test population immediately below, at, and above:

- 5,000;
- 10,000;
- 20,000;
- 40,000.

Apply every fort bonus and Order/Turmoil step. Determine each rounding stage.

### Test E4: Commander and Holy Points

The ordinary base and fort ladder are now closed. The remaining test should isolate exceptional interaction. Record unfortified and each standard fort stage, then vary:

- one-, two-, three-, and four-point commanders;
- `#slowrec` and an explicit `#rpcost` test object;
- site recruitment without changing the fort;
- unrest immediately around every visible Commander Point loss;
- sacred queues;
- temple and maximum-dominion changes.

The baseline prediction is one point plus the current fort bonus. AI difficulty must not alter Commander Points or Holy Points.

### Test E5: upkeep

Use units with:

- ordinary gold recruitment;
- Sacred;
- Slave;
- Sacred and Slave;
- rider and mount;
- summons;
- `#addupkeep`.

Compare the detailed annual display, monthly treasury charge, and base object costs. The 6.33 published observation already predicts divisor 60 for Sacred Slaves and separate rider/mount bases. Concentrate the new test on:

- monthly fractional aggregation;
- a Slave rider with an ordinary mount;
- a Sacred rider with an ordinary mount;
- a pair where both components are Sacred;
- voluntary, battle-only, seasonal, and death transformations;
- whether `#addupkeep` follows the active or persistent form.

### Test E6: supply distance

Place an Administration-known fort at each distance zero through four from a fixed province. Remove population supply where possible. Record displayed and consumed supply. Repeat with two forts in range.

### Test E7: starvation

Test:

- troops and commanders;
- survival skills;
- animals;
- mounts;
- Need Not Eat with zero usage;
- Need Not Eat combined with Appetite or negative supply production;
- transformation into a non-eating form and back;
- existing Starving;
- siege interior;
- restoration of supply.

Record selection priority, Supply Usage, Starving, morale, disease, and recovery. Separate “fed first” from “cannot be selected.”

### Test E8: unrest resolution

Vary:

- candles;
- Order/Turmoil;
- PD;
- patrol strength;
- population;
- Blood Hunters.

Record income, resources, RP, Commander Points, recruitment eligibility, and end-turn unrest.

For Commander Points, test every unrest integer around the first and second visible loss from ordinary pools of one, two, and three. The purpose is to distinguish rounding of the reduction from rounding of the remaining capacity.

### Test E9: construction timing

Complete a lab, temple, and fort during threatened turns. Verify:

- research;
- ritual and forging access;
- preaching;
- recruitment;
- fort protection;
- tax trace and Administration income;
- demolition edge cases.

### Test E10: siege contribution

Vary Strength, Flying, Mindless, Animal, Undisciplined, siege abilities, and commander orders. Record exact wall changes from both sides.

## Test record format

| Field | Required entry |
| --- | --- |
| Test ID | Stable identifier such as E6-03 |
| Game version | Exact patch |
| Ruleset | Unmodded or exact mod list and order |
| Map and province | Reproducible setup |
| Starting state | Population, scales, unrest, buildings, units |
| Orders | Every relevant order |
| Prediction | Formula and expected result |
| Observation | Interface, message, treasury, battle, or wall result |
| Repetitions | Count and variation |
| Conclusion | Supported, contradicted, or unresolved |
| Artifacts | Save, turn file, screenshot, source diff |

# Part XVIII: Essays

## Essay I: The Economics of Forts and Mages

A fort is often evaluated as if it were a bank: pay gold now, receive additional income later, and ask how many turns are needed to break even. That calculation is useful only as a lower bound. A Dominions fort is simultaneously an industrial concentrator, recruitment licence, tax office, supply depot, laboratory shelter, siege obstacle, and movement node.

Its most valuable output is frequently a commander slot. A nation whose power depends on mages does not become stronger merely because the treasury grows. Gold must pass through a fort's Commander Points and national roster before it becomes research or battlefield magic. If the existing forts already consume every commander slot, the marginal value of another fort can exceed its Administration income by an order of magnitude.

The opposite error is to treat every possible mage fort as mandatory. A fort begun during an immediate war may not produce its first useful mage until after the decisive campaign. Construction takes months, resolves late in hosting, and then begins a sequence of recruitment and travel. The gold and builder are absent from the present front throughout that delay.

The correct question is not whether forts are economically efficient in the abstract. It is whether this fort converts current resources into the capability needed at the time and place it will matter. A safe high-resource province with valuable mages, strong tax geometry, and central supply position may justify investment without a short cash payback. An exposed province with redundant recruits and poor donors may not justify even a superficially attractive income bonus.

Fort networks also shape one another. Adjacent fortified provinces stop donating resources to each other, while a shared unfortified donor can feed both. Dense forts provide more mage streams and protection but may reduce the resource concentration required for elite troops. The best geometry is national: mage-heavy nations often favour more production centres than resource-hungry troop nations can fully equip.

A fort is a promise about future conversion. Its value depends on whether the nation can keep that promise.

## Essay II: Population Is Strategic Capital

Population looks passive. It sits in a province and produces a little gold each month, but it also supports income, Recruitment Points, supplies, and PD. Damaging it can strike the treasury, troop throughput, army logistics, and static defence at the same time.

This makes population loss qualitatively different from an ordinary expense. Gold spent can be earned again from an intact economy. Population destroyed by pillage, patrolling, Death, Blood Hunting, or hostile effects reduces the machinery that would have produced future gold and capacity.

The value is nevertheless not uniform. The first population bands contribute more Recruitment Points and supplies per inhabitant than later bands. A small province can lose its ability to support meaningful PD quickly, while a huge farm province may retain considerable capacity after the same absolute loss. Terrain, dominion stability, game length, and national mechanics all change the horizon.

Blood magic demonstrates the tension most clearly. A Blood nation converts population and mage-turns into slaves, then converts slaves into effects that may dwarf the foregone income. Refusing all population damage would misunderstand the nation's power. Ignoring the damage would eventually shut down recruitment and tax collection. Mastery lies in choosing which provinces become extraction zones, supporting them with patrols, and spending the slaves quickly enough that the sacrifice becomes strategic advantage.

Population is capital with a location and a lifespan. It is most valuable when connected, protected, and given enough time to grow. It is expendable only when the return arrives before the loss matters.

## Essay III: The Hidden Price of Static Defence

Province Defence is attractive because it has no upkeep, restores after successful battles, and requires no commander management. Those strengths conceal a convex cost curve and absolute immobility.

The first points are cheap. They tax careless raids, generate reports, and can combine with a real army. Later points become dramatically more expensive while remaining tied to one province. The gold that raises PD from 40 to 50 could fund several commanders, a laboratory, or a significant mobile force. Once purchased, PD cannot voluntarily be recovered or moved.

This does not make high PD irrational. A capital approach, Throne, blood centre, or mage fort can have enough concentrated value that static defence is exactly correct. National PD rosters also vary wildly. Battlefield magic can make disposable bodies valuable, and the need to force an attacker into a full army can protect an entire region.

The mistake is to value PD by the number alone. Its return is the attack it prevents, delays, reveals, or defeats. If no plausible enemy force is affected, the investment is decorative. If the attacker must reveal a major army, consume gems, or delay a campaign, even losing PD may have succeeded.

Static defence buys local certainty. Mobile armies buy choices. A healthy state knows which one the province requires.

## Essay IV: Logistics After Victory

The most dangerous logistical moment often comes after a successful battle. The army has moved into hostile terrain, the province may be pillaged or depopulated, the fort may still belong to the enemy, and the new supply state is easy to overlook because the battle report is positive.

Starvation resolves after battle. That timing allows an army to win first and acquire its -4 morale penalty afterward. The next turn begins with a force that looks victorious but may already carry Starving, disease risk, damaged units, and an uncertain retreat path. If the next battle follows immediately, the logistical debt becomes tactical collapse.

Fort supply projection and siege storage are separate. A nearby high-Administration fort can sustain provinces outside its walls, but a besieged garrison consumes a declining fraction of interior storage. A large relieving army may also worsen local supply even while saving the fort.

Operational planning needs to extend one turn beyond contact. Before an attack, calculate the destination's supply under the state expected after conquest, not the state currently shown. Include temperature, Growth or Death, population damage, mounts, animals, large units, and the possibility that the enemy fort remains.

Winning the battle secures a position. Supplying the survivors converts it into a campaign.

## Essay V: Unrest as Administrative Warfare

Unrest is often treated as a local nuisance to be patrolled away. Its actual effect is to attack the conversion machinery of a province.

The income formula loses one-third of output by unrest 25 and half by unrest 50. Resources decline more slowly, but at unrest 100 recruitment stops completely. Blood Hunting becomes less reliable, patrolling becomes harder, and community evidence suggests local recruitment capacities may also fall continuously.

Because unrest alteration normally occurs after income, restoration has a one-month lag. A province can be pacified at step 39 only after paying reduced income at step 38. Reaching recruitment shutdown is worse: step-39 recovery cannot retroactively restore recruitment that already failed at step 3.

This makes unrest a weapon against fortified production. Walls do not prevent spies, sites, spells, hunting mistakes, or some globals from degrading the province. A high-value fort at 100 unrest can retain its physical infrastructure while losing the reason it was built.

Administratively resilient nations do more than patrol after the damage. They keep baseline unrest low, maintain spare patrol capacity, protect Blood centres, identify hostile infiltrators, and avoid placing every economic function in the same vulnerable province.

## Essay VI: Conversion, Not Accumulation

A full treasury and gem stockpile create options, but they do not fight. A large research total creates spell access, but access does not script a mage or supply the gems. A broad empire creates potential income, but disconnected provinces may collect nothing. Dominions rewards stockpiling only when a later conversion justifies the delay.

Every stored resource should have a plausible route:

- gold to commander and troop production;
- gems to a research breakpoint, item, ritual, or battlefield package;
- blood slaves to a defined Blood power;
- population and safe time to infrastructure;
- information to a movement, diplomacy, or scripting decision.

Premature conversion is also dangerous. Troops create upkeep, gems carried into battle can be lost, and a fort begun too early can remove the army needed to defend it. The central skill is timing: retain flexibility until the strategic question is clear, then convert fast enough to decide it.

The pinnacle of economic play is not owning the largest numbers. It is reaching the decisive battlefield, ritual, or Throne state with the right power one turn before the opponent.

## Essay VII: The Month Hidden Inside a Single Point

Dominions displays most of its economy as integers, which makes one point look trivial. At a production boundary, one point can be an entire month.

Commander Points are the clearest case. A two-point mage in a two-point fort appears every month. Reduce the usable pool to one and the same mage appears every second month. Nothing on the mage card has changed: not price, paths, Research Points, or battlefield value. Yet a twelve-month plan has fallen from twelve mages to six. The missing point is not one unit of capacity; it is half the production stream.

Recruitment Points can behave similarly when a queue sits just above the local total. One missing point may delay a complete army package, strand unused resources, and postpone expansion or a relief force. A single point of supply can decide whether another unit enters the starvation selection pool. A single point of income can determine whether the treasury pays every component of a mounted army without desertion risk.

This is why exact rounding matters, but also why false precision is dangerous. A spreadsheet can calculate decimals the engine never exposes and place the apparent total on the favourable side of a boundary. If the internal rounding stage is unknown, more decimal places do not create more knowledge.

The practical response is to plan in layers. Use the official formula for direction, the current interface for the operative integer, and a reserve when one point controls a deadline. Record the boundary if it repeats often enough to matter. A reliable player does not need every hidden rounding rule memorised; a reliable player knows when an unverified rounding rule is carrying the entire plan.

# Part XIX: Sources and Open Questions

## Primary official sources

- [Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf), revision 2
- [Dominions 6 Modding Manual](https://www.illwinter.com/dom6/dom6modman.pdf), version 6.34
- [Dominions 6 official changes](https://www.illwinter.com/dom6/changes.html)
- [Illwinter home and current release record](https://www.illwinter.com/)

Principal manual sections:

- Province attributes and economy, pages 21-29.
- Strategic orders, especially Blood Hunting, sieges, construction, demolition, pillage, and raids, pages 50-54.
- Turn resolution, pages 55-57.
- Sieges and storming, pages 71-72.
- Dominion scales and extreme scales in the Dominion chapter.

## Community sources used as leads

- [Current Commander Point reference](https://illwiki.com/dom5/dom6/commander)
- [Illwiki unrest reference](https://illwiki.com/dom5/dom6/unrest)
- [Illwiki starvation reference](https://illwiki.com/dom5/dom6/starving)
- [Illwiki supplies reference](https://illwiki.com/dom5/dom6/supplies)
- [Current population and fort-supply reference](https://illwiki.com/dom5/dom6/population)
- [Illwiki Province Defence reference](https://illwiki.com/dom5/game-mechanics/province-defence)
- [Illwiki fort reference](https://illwiki.com/dom5/fort)
- [Illwiki Blood Hunting reference](https://illwiki.com/dom5/blood-hunting)
- [Illwiki generic Blood guide](https://illwiki.com/dom5/dom6/generic-blood-magic-guide)
- [December 2025 in-game upkeep observations](https://steamcommunity.com/app/2511500/discussions/0/691996377956257521/)

Community pages are not treated as final authority. Several retain historical Dominions 5 material or conflict with current official text. They are used to locate edge cases and testable claims. The upkeep discussion has firmer limits than a general guide because it records the observation date, annual values shown in game, a mounted component example, and the manual rule being checked. Its claims remain Community-tested evidence, below an official rule or an archived controlled save.

## Mod sources

The economic discussion uses the supplied DE 2.16 and Divinitus 1.15.3 DE files. Their hashes, order, and exact global commands are recorded in Book IX.

## Open questions

- fort-supply distance arithmetic;
- exact rounding in income, resources, RP, and fort draw;
- shapechanged upkeep and monthly fractional aggregation;
- full unrest effects on RP and Commander Points;
- generic commander feeding priority and starvation eligibility;
- national and object-specific effects from DE and Divinitus.

For the unmodded 6.36 publication baseline, Growth/Death income and Order/Turmoil resources use 2% per step. The ordinary Commander Point pool is one plus the current fort bonus. At the stated Community-tested tier, Sacred and Slave reductions stack and mounted upkeep uses separate component bases. No 6.36 announcement changes those rules. Until the remaining questions are reproduced under the current game, close calculations should state their exact uncertainties instead of hiding them inside a rounded recommendation.
