# Foundation Book III: Pretenders, Dominion, Scales, and Blessings

## The design problem

Pretender design is the first strategic decision in a game of Dominions 6 and one of the last decisions that can be judged in isolation. A design determines more than the strength of a god. It determines when that strength exists, which sacred units justify their cost, how quickly faith spreads, what kind of provinces the nation creates, which divine spells its priests know, and which magical paths are available when the national roster runs out of answers.

The design screen asks a larger question than “Which Pretender is strongest?”

> **Foundation rule:** A Pretender design is a contract between the nation’s roster, the map, the expected war schedule, and the intended route to victory.

The chapters begin with the unmodded design screen, then follow the consequences through awakening, dominion, scales, blessings, priesthood, death, and team play. Exact arithmetic is included when it helps settle a choice.

## Edition note

Book I owns the common Dominions 6.36 baseline and evidence vocabulary. The revision-2 manual remains the main rules source here, but its printed blessing appendix predates several official balance changes. The structured object snapshot behind the current bless table is still pinned to the Inspector's 6.35 commit; the 6.36 announcement changes a Pretender-loading bug, not any listed bless cost or effect. Current values, historical values, and the one-version data lag are stated separately so they cannot be quietly blended together. Edition 22 reconciled Call God and same-turn Throne ownership. Edition 23 traces the newly republished awakening model back to its pre-Dominions 6 source and keeps it below current-version proof. Book IX is the authoritative source for DE 2.16 and Divinitus 1.15.3 DE changes.

## Finding the useful layer

A new player can move from the one-model design summary through awakening, dominion, scales, blessings, and the final audit. Detailed point curves, dominion checks, sacred throughput, special dominions, disciples, and god-death mechanics support more demanding designs. The test programme is mainly for cases where the interface and documentation do not settle the same question.

# Part I: Pretender Design as a National System

## The design in one model

The unmodded design begins with 450 points before paying for the physical form. Those points are allocated across four linked budgets:

```text
450 design points
  - physical form
  - purchased magic
  - dominion strength and scales
  + deferred-awakening points
  = unspent remainder
```

The arithmetic is simple. The strategic valuation is not.

| Budget | Immediate result | Long-term consequence |
| --- | --- | --- |
| Physical form | Body, slots, statistics, abilities, starting paths, scale limits | Determines personal roles, survivability, mobility, and path-buying efficiency |
| Magic | Personal paths and bless-point pool | Determines research or ritual access, forging, divine spell family, and sacred enhancements |
| Dominion and scales | Candles, provincial tendencies, sacred recruitment capacity | Shapes economy, faith conflict, terrain, events, population, research, and religious survival |
| Awakening | Availability date | Trades immediate agency for design points and changes when Incarnate blessings operate |

These budgets cannot be evaluated independently. An imprisoned god may buy a powerful Incarnate blessing that is unavailable during expansion. An awake monster may defeat independents but leave no useful magic or economy after its expansion role ends. Excellent scales may produce gold that a low-resource or Holy-limited roster cannot convert. High paths may purchase many bless points while satisfying none of the prerequisites needed by the sacred roster.

### The five obligations

A complete design should state how it addresses five obligations:

1. **Expansion:** how provinces are taken reliably and at an acceptable loss rate.
2. **Economy:** which scales and dominion support the planned recruitment and research.
3. **Sacred plan:** whether sacred units are central, supplementary, or mostly irrelevant.
4. **Magic access:** which national weaknesses the Pretender repairs or which strengths it accelerates.
5. **Timing:** when the design becomes stronger than the alternatives whose points were spent elsewhere.

A design need not solve every obligation through the Pretender. It must show where each solution comes from.

## Begin with the nation, not the god

Before opening the Pretender screen, record:

- recruitable sacred troops and commanders;
- capital-only, fort-only, terrain-only, foreign, and summonable sacreds;
- Holy Point and Commander Point bottlenecks;
- ordinary expansion troops and commanders;
- national mage paths, randoms, and missing paths;
- early research packages;
- gold, resource, and Recruitment Point demand;
- temperature preference and scale limits;
- special dominion rules;
- expected map and lobby settings.

The purpose is to identify problems before selecting an attractive solution.

### Roster questions

| Question | Why it changes the design |
| --- | --- |
| Are the principal sacreds massed or elite? | Flat bonuses scale with body count; survival and percentage effects often gain value on expensive bodies |
| Are sacreds capital-only? | A powerful bless may apply to too few units to justify its design cost |
| Are sacred commanders strategically important? | Passive leadership, stealth, recuperation, or magic-related blessings may matter outside battle |
| Can ordinary troops expand reliably? | If yes, an awake expander is optional rather than compulsory |
| Is the nation gold-, resource-, RP-, or Holy-limited? | Scales should support the actual bottleneck |
| Which magic paths are missing? | Pretender paths may open boosters, summons, rituals, or counters unavailable nationally |
| Does the nation need an early battlefield caster? | Awakening time and chassis mobility become central |
| Does the nation possess a special dominion? | Candles and temples may become economic or military infrastructure |

### Lobby questions

Pretender value changes with:

- independent strength;
- map size and terrain;
- number of players;
- team or disciple rules;
- research speed;
- site frequency;
- magic-resource settings;
- throne distribution and points required;
- diplomacy rules;
- starting provinces;
- mods and load order.

A design that is excellent on a crowded, high-independent-strength map may be wasteful in a spacious game with weak independents. An imprisoned research-and-access design may mature comfortably on a slow diplomatic map and arrive too late in a knife-fight.

## Chassis roles

Physical forms should be compared by the jobs they can perform, not by a single tier list.

### Expansion chassis

An expansion chassis personally captures independent provinces during the opening.

Requirements usually include:

- sufficient protection or avoidance;
- a way to prevent chip damage from accumulating;
- enough offence to end battles before fatigue or attrition wins;
- resistance to common independent threats;
- acceptable map movement;
- a script that works without unavailable research or equipment.

An expander is an economic asset only while its conquest produces more value than the alternative use of its design points and commander-turns.

### Bless anchor

A bless anchor buys the paths and bless points required by the sacred plan. Its own combat performance may be secondary.

The anchor must answer:

- which sacreds receive the benefit;
- how many can be recruited;
- when they can be blessed;
- whether the decisive effects are Incarnate;
- which counters remain;
- whether the same paths have a useful later role.

### Scales anchor

A scales anchor spends relatively little on personal power so that the nation can afford strong dominion and favourable scales. It is commonly dormant or imprisoned, but awakening and form are separate choices.

The design succeeds when the nation can convert the improved economy into more useful power than a direct bless or awake form would have supplied.

### Rainbow and access chassis

A rainbow distributes points across several paths to:

- obtain efficient early path levels;
- expand the bless-point pool;
- search for sites;
- forge cross-path items;
- provide ritual access;
- open booster chains;
- diversify divine spells.

The danger is diffuse capability without a timetable. “Can eventually cast many things” is not a plan until the required research, gems, boosters, laboratories, and safe commander-turns are named.

### Ritual platform

A ritual platform buys one or more high paths for a defined strategic package:

- global enchantments;
- remote attacks;
- large summons;
- mobility rituals;
- high-path forging;
- late-game access.

Its value depends on the earliest realistic casting date, not only the final path display.

### Battlefield caster

A battlefield caster supplies spells the national roster cannot cast at the required time. It needs:

- arrival before the relevant war;
- sufficient combat speed or cast time;
- fatigue management;
- gems and research;
- protection from assassination, seeking arrows, remote attacks, and battlefield counters;
- a retreat or immortality plan.

### Thug or supercombatant platform

A thug or supercombatant design intends to fight armies, raid, hold positions, or force specialised counters. Personal statistics alone are insufficient. The design must cover:

- damage types and attack volume;
- fatigue;
- mundane and magical defence;
- elemental and physical resistances;
- magic resistance;
- control effects;
- anti-undead or anti-demon tools where relevant;
- mobility;
- recovery from afflictions;
- escape and death consequences.

### Immobile oracle

Immobile forms often purchase magic efficiently and may have strong dominion or special sites. They trade away conventional movement.

Some can move by teleportation, while others are too large for particular transport effects. Mobility must be checked for the exact form.

### Shape-changer

Dragons and other shape-changers can separate casting and combat forms. The manual notes that a dragon may appear as a humanoid wizard until changing shape or being wounded.

The two forms should be audited separately:

- paths and casting convenience;
- slots;
- movement;
- protection and attacks;
- regeneration or recuperation;
- transformation conditions;
- whether an affliction or shape loss changes the planned role.

### Trinity

A Trinity consists of three entities. According to the manual:

- the members share part of their magical power;
- separated members lose some magic;
- a lone member loses more;
- exact penalties vary by Trinity;
- each member can research, though at reduced ability;
- a dead member can be Called God in half the ordinary time.

Trinities create parallel commander-turns and map presence at the price of coordination and reduced separated power. Every proposed Trinity design needs exact-form testing; the category does not guarantee identical behaviour.

### Immortal and dominion-immortal forms

These forms alter the cost of personal risk.

- **Immortal:** normally reforms regardless of ordinary-plane dominion.
- **Dominion Immortal:** normally reforms after death in friendly dominion.
- **Neither:** requires Call God after death unless another special rule applies.

Soul destruction and death on a remote plane can bypass ordinary reform. Immortality reduces some consequences of death; it does not make every battle strategically free.

## Chassis comparison sheet

| Field | Record |
| --- | --- |
| Form and nation | Exact form, age, nation, and ruleset |
| Base point cost | Points removed before all other purchases |
| Starting paths | Innate path levels in each form |
| New Path Cost | Cost of opening an absent path |
| Starting dominion | Base candle value |
| Scale-limit changes | Direction and amount |
| Awakening restrictions | Ordinary, minimum prison, maximum prison, or other |
| Movement | Map Move, terrain survival, sailing, teleport eligibility |
| Combat shell | HP, protection, defence, MR, resistances, recuperation, regeneration |
| Slots | Hands, head, body, feet, misc, special restrictions |
| Special mechanics | Shape change, Trinity, immortality, freespawn, sites, dominion effects |
| Opening job | Expansion, research, site search, forging, ritual, deterrence |
| Middle-game job | Named repeatable use |
| Failure condition | What makes the investment non-functional |

# Part II: Exact Design-Point Arithmetic

## Physical-form cost

Every form has an inherent point cost. The cost is paid from the initial 450.

```text
points after form = 450 - form cost
```

A Phoenix costing 110, for example, leaves 340 before magic, dominion, scales, and awakening are applied.

Form cost cannot be judged without its embedded value:

- starting magic;
- cheaper or more expensive new paths;
- starting dominion;
- scale-limit adjustments;
- combat statistics;
- slots;
- mobility;
- special abilities;
- national availability.

## Magic-path costs

The official cost for each path level added by the player is:

| Added level number | Marginal cost | Cumulative cost |
| ---: | ---: | ---: |
| 1st | 8 | 8 |
| 2nd | 16 | 24 |
| 3rd | 24 | 48 |
| 4th | 32 | 80 |
| 5th | 40 | 120 |
| 6th | 48 | 168 |
| 7th | 56 | 224 |
| 8th | 64 | 288 |
| 9th | 72 | 360 |
| 10th | 80 | 440 |

These are levels **added by the design**, not the displayed final path.

If a form begins with Nature 2, raising it to Nature 3 is the first purchased level in that path and costs 8. Raising it from Nature 2 to Nature 6 adds four levels and costs:

```text
8 + 16 + 24 + 32 = 80
```

### Opening a new path

If the form begins with no level in a path:

1. the first level costs the form’s **New Path Cost**;
2. the second added level costs 16;
3. the third costs 24;
4. the sequence then continues normally.

The New Path Cost replaces the ordinary 8-point first purchase. It does not replace the entire path curve.

### Official worked example

The Carrion Dragon begins with Death 1 and Nature 1. Raising it to Death 4 and Nature 4 adds three levels in each:

```text
Death: 8 + 16 + 24 = 48
Nature: 8 + 16 + 24 = 48
```

Opening Fire at a New Path Cost of 80 and raising it to Fire 2 adds:

```text
Fire: 80 + 16 = 96
```

Total:

```text
48 + 48 + 96 = 192 design points
```

### Magic-purchase audit

For every path, record:

| Path | Innate | Purchased | Final | Cost | Purpose |
| --- | ---: | ---: | ---: | ---: | --- |
| Fire |  |  |  |  |  |
| Air |  |  |  |  |  |
| Water |  |  |  |  |  |
| Earth |  |  |  |  |  |
| Astral |  |  |  |  |  |
| Death |  |  |  |  |  |
| Nature |  |  |  |  |  |
| Glamour |  |  |  |  |  |
| Blood |  |  |  |  |  |

“Purpose” should be specific: a blessing prerequisite, a named booster chain, a site-search threshold, a combat spell, a ritual, or a divine-spell family. A path bought only because it looks flexible is a candidate for removal.

## Dominion-strength costs

Every form begins with at least Dominion 1 and may be raised to Dominion 10. Each candle added above the form’s base costs progressively more:

| Added candle number | Marginal cost | Cumulative cost |
| ---: | ---: | ---: |
| 1st | 7 | 7 |
| 2nd | 14 | 21 |
| 3rd | 21 | 42 |
| 4th | 28 | 70 |
| 5th | 35 | 105 |
| 6th | 42 | 147 |
| 7th | 49 | 196 |
| 8th | 56 | 252 |
| 9th | 63 | 315 |

For `n` added candles:

```text
cumulative cost = 7n(n + 1) / 2
```

The accelerating curve matters. Raising an already high starting dominion is often much cheaper than buying the same final score on a low-dominion form.

### What initial dominion changes

Initial dominion contributes to:

- the maximum dominion ceiling;
- the chance that temple checks succeed;
- capital-only sacred recruitment through Holy Points;
- Pretender and Prophet statistics in friendly or hostile dominion;
- the speed at which scales tend to establish;
- resistance to hostile faith;
- survival against a dominion kill;
- several special national mechanics.

High dominion means more than “more candles.” It improves several connected parts of the nation while consuming a steep share of the design budget.

## Scale-point costs

Each favourable scale step costs 40 points. Each unfavourable step grants 40.

```text
scale-point change = -40 x favourable steps + 40 x unfavourable steps
```

Temperature is measured relative to national preference during design. Only the first three clicks away from that preference grant points.

The ordinary design window is -2 to +2. National and Pretender scale-limit adjustments can pull that window in one direction. Province scales can reach -5 to +5 during play.

### Scale-limit movement

A `+1 Growth Limit` does more than add one Growth option. It shifts the whole design window:

- Growth maximum rises by one;
- Death maximum in the opposite direction falls by one.

National and Pretender adjustments in the same direction overlap rather than automatically stacking without limit. Exact nation-form combinations should be checked in the design screen.

## Awakening points

| State | Point change | Ordinary arrival |
| --- | ---: | --- |
| Awake | +0 | Present from the beginning |
| Dormant | +150 | Approximately turns 10-13 |
| Imprisoned | +350 | Approximately turns 28-42 |

The official manual intentionally gives ranges rather than a guaranteed turn. It also says that Disciples awaken in about half the time of their Pretender. That wording does not define an exact Disciple range or a rounding rule.

### Planning with an unknown distribution

The range is enough to build a robust opening, but not enough to calculate an expected arrival.

| Design | Safe planning assumption | What must work before arrival |
| --- | --- | --- |
| Awake | The god is available immediately | Its first several orders, expansion targets, and acceptable risks |
| Dormant | The nation may wait until the late end of turns 10-13 | Expansion, research, and sacred use through the whole dormant window |
| Imprisoned | The nation may wait until the late end of turns 28-42 | The first expansion cycle and a substantial part of the first war without the chassis or Incarnate effects |
| Disciple | Roughly half the Pretender delay, with no published exact rounding | The disciple nation must not depend on a single inferred half-turn |

Do not substitute the midpoint for an average. The official range does not say that every turn is equally likely, and an arrival process with repeated rolls can be heavily weighted without changing its visible minimum and maximum. For practical design work:

1. budget the army and research plan to survive the latest official arrival;
2. prepare a useful first order for every plausible arrival turn;
3. treat an early arrival as extra tempo rather than as a requirement;
4. evaluate an Incarnate blessing as two armies: the pre-awakening army and the post-awakening army.

Older reverse-engineering notes propose repeated exploding-die checks rather than a uniform draw. A Dominions 6 community Pretender page, revised on 16 June 2026, now republishes the same model and attributes it to Loggy: `9 + d4!` for Dormant, `27 + d20!` for Imprisoned, and bases of 4 and 13 for the corresponding Disciple rolls. It says a new exploding roll is made each month and the result is compared with the current turn.

The newer page label does not create a new current-version test. The wording and constants can be traced to Loggy's older miscellaneous reverse-engineering notes and to copies published years before Dominions 6. The current page supplies neither raw 6.x outcomes nor an executable trace, and its usual displayed ranges of turns 11-14 and 29-42 are shifted from the revision-2 manual's approximate 10-13 and 28-42 wording. That may be a turn-label convention, an editorial carry-over, or a real version difference; the available sources do not decide which.

The exploding-die model remains a **current community research hypothesis with historical provenance** and is not promoted to a Dominions 6.36 rule. It is more specific than assuming a uniform draw and helps define a decisive reproduction, but it is not safe input for an exact probability calculator. R-014 stays queued until a sufficiently large current sample, a current engine-backed trace, or developer confirmation establishes both the distribution and the displayed-turn convention.

### Total-budget worksheet

```text
450
- form cost
- purchased magic
- added dominion
- favourable scales
+ unfavourable scales
+ awakening grant
= remainder
```

The final screen should be checked against the worksheet. Form-specific restrictions, national scale limits, bonus bless points, and mod changes can make a generic calculator incomplete.

# Part III: Awakening, Time, and the Opening

## Awake

An awake Pretender can contribute from turn one.

Possible opening jobs:

- expand personally;
- research;
- search;
- forge once research permits;
- cast early rituals;
- lead or bless an army;
- deter an early attack;
- establish a special site or dominion effect.

The opportunity cost is the 150 or 350 points not obtained from delay.

An awake design should specify its monthly orders. “Available” is not the same as “productive.”

### Awake-expander ledger

Record:

- provinces taken;
- turns saved relative to an ordinary expansion party;
- gold and commander-turns freed;
- wounds and afflictions;
- additional gear or research required;
- enemy counters revealed;
- time spent returning, healing, or waiting.

The correct comparison is not the expander’s kill count. It is the territory and tempo created after subtracting its design cost and risk.

## Dormant

Dormant grants 150 points and usually arrives near the end of the initial expansion phase.

Common uses:

- moderate Incarnate bless arriving before the first planned war;
- mid-game combat or ritual chassis;
- strong scales with a still-relevant physical god;
- path access not needed during the first ten turns.

Risks:

- an early war begins before arrival;
- the sacred plan requires Incarnate effects for expansion;
- the nation cannot exploit the purchased paths immediately on awakening;
- the arrival location or laboratory network is poorly prepared.

## Imprisoned

Imprisoned grants 350 points and may remain absent until turns 28-42.

Common uses:

- high scales;
- broad or deep magic;
- large bless-point pools;
- late-game path access;
- a powerful Incarnate package deliberately deferred.

The design transfers power from the opening to the economy, blessing, or later magic. That transfer is only favourable if the nation survives and converts the points before the game’s decisive wars.

### The Incarnate trap

An imprisoned god can buy an Incarnate blessing, but the effect remains inactive while the god is imprisoned or dead. The sacred roster may fight for several dozen turns with only the non-Incarnate portion.

The design audit should split the bless into:

| Phase | Available effects |
| --- | --- |
| Before awakening | Innate and ordinary non-Incarnate effects |
| God alive and present | Full bless, including Incarnate effects |
| God dead or absent under the effect’s rule | Incarnate portion disabled |

## Timing comparison

| Question | Awake | Dormant | Imprisoned |
| --- | --- | --- | --- |
| Helps turn-one expansion? | Yes, if capable | No | No |
| Incarnate bless active? | Yes while alive/present | Delayed | Heavily delayed |
| Extra design points | 0 | 150 | 350 |
| Early personal research | Possible | None | None |
| Early personal risk | Highest | Deferred | Deferred longest |
| Best justification | Immediate actions worth more than 150 points | Mid-game arrival matches plan | Nation can carry the opening and exploit the large point grant |

## Arrival preparation

Before a delayed god awakens:

1. preserve a suitable laboratory;
2. reserve the needed gems;
3. complete required research;
4. forge planned equipment;
5. choose a safe operating province;
6. prepare priests and sacred armies if Incarnate effects matter;
7. identify the first three commander-turns after arrival.

An arrival without orders is delayed power followed by idle power.

# Part IV: Dominion

## Dominion in plain language

Dominion is religious control. Province ownership is military and administrative control. The two layers are independent.

A nation can:

- own a province under enemy dominion;
- spread dominion through provinces it does not own;
- conquer a continent without spreading its faith;
- lose by losing every friendly candle even while retaining forts and armies.

Friendly dominion is displayed as positive candles. Enemy dominion is effectively negative from the observing nation’s perspective.

> **Foundation rule:** Armies take provinces. Religious infrastructure makes those provinces part of the god’s world.

## Sources of dominion spread

The manual gives the following sources:

| Source | Checks |
| --- | ---: |
| Pretender | One automatic increase plus two temple checks |
| Home province | One temple check |
| Prophet | One temple check |
| Temple | One temple check |
| Disciple | One temple check |
| Claimed Throne | One to seven checks, depending on Throne |

A check does not guarantee a candle. It attempts to create, increase, propagate, or contest dominion according to the local state.

### Religious hosting order

The official turn sequence separates direct priest orders from ordinary passive spread:

| Step | Religious operation | Consequence |
| ---: | --- | --- |
| 6 | Preaching | Priest orders adjust local dominion. Since version 6.13, commanders performing this order resolve in random order. |
| 7 | Heretic preaching | Heretics, insane commanders, and shattered-soul commanders reduce dominion. |
| 8 | Claim Thrones | Valid Throne claims resolve before movement and battle. |
| 42 | Dominion spread | Pretender, capital, Prophet, temple, Disciple, Throne, and sacrifice-generated spread resolves. |
| 43 | Dominion effects | Population death, insanity, temperature spread, and similar effects use the resulting religious state. |
| 56 | Elimination | A nation without provinces or dominion is removed. |
| 57 | Victory | The game checks whether a victory condition has been fulfilled. |

This closes the ordinary R-015 model at the official-rules tier: the sources, check probabilities, local resolution rules, cross-water reroll, and hosting stage are all stated officially. The manual does not publish the random-number stream or the internal iteration order among simultaneous passive sources, so neither is inferred.

## Maximum dominion

The maximum is:

```text
maximum dominion =
  initial Pretender dominion
  + floor(temples / (5 x players on team))
```

For a solo nation, every five temples raise the maximum by one. For a two-player team, every ten team temples do so.

Example:

```text
initial dominion 3
12 temples
2 players on team

maximum = 3 + floor(12 / 10) = 4
```

The ceiling matters because it affects:

- maximum candle strength reached by ordinary temple spread;
- temple-check success chance;
- resistance in dominion conflict;
- the relay behaviour of strong friendly provinces.

Preaching uses a separate local cap and can exceed what a weak maximum would ordinarily establish.

## Temple-check chance

The official chance that a temple check succeeds is:

```text
50% + 5% x maximum dominion
```

| Maximum dominion | Check chance |
| ---: | ---: |
| 1 | 55% |
| 3 | 65% |
| 5 | 75% |
| 7 | 85% |
| 9 | 95% |
| 10 | 100% |

Temples have two network effects:

1. each adds another check;
2. each threshold of five per team member can raise the maximum, improving every ordinary check.

The value of a temple network is not linear around the threshold.

## Resolving a successful check

### Neutral province

A successful check adds one friendly candle.

### Province with friendly dominion

At `U` friendly candles, the chance to add another candle locally is:

```text
30% - 3% x U
```

If the local increase fails, the check propagates to a random neighbouring province.

High-candle provinces tend to relay pressure outward instead of endlessly concentrating it.

| Friendly candles | Local increase chance |
| ---: | ---: |
| 1 | 27% |
| 3 | 21% |
| 5 | 15% |
| 7 | 9% |
| 9 | 3% |

### Province with enemy dominion

At `E` enemy candles:

```text
chance to reduce enemy dominion =
  50% + 5% x maximum dominion - 5% x E
```

| Maximum dominion | Enemy candles | Reduction chance |
| ---: | ---: | ---: |
| 5 | 1 | 70% |
| 5 | 5 | 50% |
| 7 | 5 | 60% |
| 9 | 8 | 55% |

Dense hostile candles form a religious wall. High maximum dominion pushes against it more effectively.

### Land and sea

When propagation randomly selects a neighbouring province across a land-sea boundary, the manual gives a 50% chance to reroll the destination. Faith crosses the boundary less readily than it spreads within the same environment.

## Dominion as a network

Dominion spread has three behaviours:

1. **creation** in neutral provinces;
2. **consolidation** in weak friendly provinces;
3. **propagation** from strong friendly provinces.

This means a rear temple can influence a frontier through a chain of strong provinces, while a single weak or hostile province can absorb repeated checks.

Useful religious infrastructure is shaped by:

- temple count;
- maximum-dominion thresholds;
- adjacency;
- sea boundaries;
- hostile candle depth;
- local preaching;
- special dominion effects;
- vulnerability of temples to raids.

## Preaching

Preaching acts only in the priest’s province and does not use the ordinary maximum-dominion ceiling.

In neutral or friendly dominion:

```text
success chance = 30% x effective Holy level
```

Against `E` enemy candles:

```text
success chance =
  30% x effective Holy level - 5% x E

minimum = 5%
```

A temple in the province adds 0.5 to effective Holy level for the chance and cap.

The maximum local dominion that preaching can establish is:

```text
preaching cap = 2 x effective Holy level
```

### Preaching examples

| Priest | Temple? | Effective H | Neutral chance | Cap |
| --- | --- | ---: | ---: | ---: |
| H1 | No | 1.0 | 30% | 2 |
| H1 | Yes | 1.5 | 45% | 3 |
| H2 | No | 2.0 | 60% | 4 |
| H2 | Yes | 2.5 | 75% | 5 |
| H3 | Yes | 3.5 | 105% | 7 |

Values above 100% should be treated as automatic for ordinary practical use, but exact engine handling remains a candidate for reproduction.

### Inquisitors

An Inquisitor counts double Holy level when preaching in enemy dominion. In neutral or friendly dominion, ordinary Holy level is used.

An H2 Inquisitor in enemy dominion preaches as effective H4 before a possible temple bonus.

### Heretics

A Heretic reduces dominion locally rather than establishing a rival faith.

```text
chance to reduce = Heretic value x 20%
```

Heretics can erode friendly candles as well as enemy candles. Their position and allegiance require careful handling.

## Blood sacrifice

An eligible priest in a temple may sacrifice blood slaves.

- maximum slaves sacrificed equals Holy level;
- each slave creates one temple check;
- the priest must have the national ability to sacrifice;
- the order consumes a priest-turn and slaves.

Blood sacrifice converts the blood economy directly into religious pressure. Its value rises when:

- the nation already hunts efficiently;
- dominion survival is threatened;
- a throne or special dominion effect depends on local candles;
- the temple network can project the additional checks;
- the sacrificed slaves are worth less than the military or ritual consequences prevented.

### Dying dominion

Early and Late Age Mictlan use a special dying-dominion system.

According to the manual:

- home-province, Prophet, and temple spread do not operate normally;
- Pretender checks are only half as effective;
- blood sacrifice is the essential spread mechanism.

This changes temple construction from passive religious infrastructure into sacrifice stations. A Mictlan design that ignores blood-sacrifice logistics is structurally incomplete.

## Prophets

A Prophet:

- becomes H3, or raises an already H3-or-higher commander by one;
- spreads dominion like a temple;
- gains +2 Attack, Defence, and Precision;
- receives dominion-dependent statistic changes.

Current community references also describe Prophets as automatically blessed, sacred, Morale 30, and upkeep-free, with a replacement delay after death. These details should be checked in 6.36 before being promoted to Official in this library.

### Prophet roles

- battlefield-wide Divine Blessing if H3;
- mobile preaching;
- dominion source;
- Holy access beyond the ordinary roster;
- throne claiming when the other conditions are met;
- combat leadership or thug role on a suitable chassis.

Prophetising a fragile scout can gain cheap mobile H3. Prophetising a robust sacred commander can create a battle piece. The correct choice depends on whether Holy access, survivability, movement, stealth, or equipment matters most.

## Thrones of Ascension

A claimed Throne:

- contributes dominion checks;
- may grant scales, blessings, sites, paths, gems, units, or other effects;
- contributes Ascension Points;
- changes the strategic value of its province.

The revision-2 manual says claimed Thrones spread one to seven checks depending on the Throne. Current community data commonly describes a claimed Throne as generating a number of guaranteed checks equal to its level. That exact success behaviour remains Test Pending.

Claiming normally requires:

- ownership of the province;
- a Pretender or Disciple, a Prophet, or an H3-or-higher priest;
- the Claim Throne order;
- a legal claimant when the order resolves at hosting step 8.

If a fort is present, a besieger cannot claim through its walls. The besieged owner may still claim. A Throne becomes unclaimed when another nation conquers its province and, where present, its fort.

### Same-turn claim, loss, and victory

The official hosting sequence and the current ownership rule answer the central R-018 cases when read together. The claim is processed early, but victory is tested against the state that survives to the end of hosting.

| Hosting point | Relevant change |
| ---: | --- |
| 8 | A legal Claim Throne order establishes the claim. |
| 10-27 | Ritual attacks, assassinations, movement battles, and castle storming can kill the claimant or change control. |
| 53 | An unbesieged fort may reclaim its province under the official partial-ownership rule. |
| 56 | Elimination is checked. |
| 57 | The game checks the victory conditions. |

The resulting state matrix is more useful than the vague instruction to “hold until hosting.”

| Same-turn result after a successful step-8 claim | State at the victory check |
| --- | --- |
| Claimant is killed later, but the nation retains the Throne | The claim remains; a claimant does not need to survive after the claim has resolved. |
| An unfortified Throne province is conquered | The Throne becomes unclaimed and its Ascension Points do not survive to step 57. |
| A fortified Throne is merely placed under siege | The defender still owns the fort and the Throne remains claimed. |
| The fortified Throne is stormed and conquered | The Throne becomes unclaimed before victory is checked. |

This is a mixed **Official plus Community-tested** conclusion. The manual establishes steps 8 and 57 and the rules for full and partial province ownership. The current community Throne reference states that conquest of the province and fort, if present, unclaims the Throne. A published same-turn report independently records the claimant-death and province-loss branches. No official update through 6.36 changes that sequence.

R-018 is complete at that evidence tier. It does not settle every adjacent victory question. In particular, an exact simultaneous tie between different nations at the winning Ascension total still needs a current controlled reproduction before any tie-break rule is published as law.

## Dominion effects on units

### Ordinary troops

All units receive:

- +1 Morale in friendly dominion;
- -1 Morale in enemy dominion.

### Pretender and Prophet

For each friendly candle, the Pretender and Prophet receive:

- +1 Strength;
- +0.5 Magic Resistance;
- +10% Hit Points.

Enemy candles reverse these changes. Hit Points do not fall below 10% through this effect.

Dominion changes whether a god or Prophet can safely take a fight. A combat report from Dominion 8 cannot be transferred unchanged to Dominion -4.

## Scale convergence inside dominion

For each scale in a province, the official chance to move one step toward the god’s selected scales is:

```text
5% x local candles
+ 10% x absolute difference
```

Example:

```text
local dominion = 6
current Order = -1
target Order = +2
difference = 3

chance = 5 x 6 + 10 x 3 = 60%
```

Current community documentation reports that a chance above 100% can move the scale two steps. The manual describes a one-step movement. The additional step requires controlled reproduction.

## Dominion elimination

If a Pretender has no friendly dominion anywhere, the nation is eliminated.

The nation may still possess:

- provinces;
- armies;
- forts;
- a treasury;
- a living Pretender.

None prevents religious extinction.

### Dominion-kill warning indicators

- no safe rear candle core;
- capital under deep enemy dominion;
- low maximum dominion;
- few temples;
- temple thresholds just below the next maximum increase;
- priests absent from threatened provinces;
- land-sea spread barriers;
- enemy blood sacrifice or Inquisitors;
- Pretender deaths that reduce dominion strength;
- simultaneous temple raids.

# Part V: Scales

## Scales in plain language

Scales describe the material and metaphysical tendencies of a god’s dominion.

The six pairs are:

| Positive end | Negative end | Principal systems |
| --- | --- | --- |
| Order | Turmoil | Income, resources, recruitment, unrest recovery, events |
| Productivity | Sloth | Resources and income |
| Heat | Cold | Climate, income, supply, movement, fatigue environment |
| Growth | Death | Population, income, supply, aging, terrain at extremes |
| Fortune | Misfortune | Event quality, frequency, heroes |
| Magic | Drain | Research, MR, spell fatigue, starting research |

“Positive” does not mean universally beneficial. Extreme positive scales carry penalties, and some nations exploit nominally negative scales.

## Ordinary scale effects

The following values are the current unmodded 6.36 publication baseline. The Growth/Death income row uses the newer official Modding Manual default.

| Scale step | Ordinary effect per step |
| --- | --- |
| Order | +3% income, +2% resources, +10% Recruitment Points, stronger unrest reduction, fewer events |
| Turmoil | Reverses Order’s economic and recruitment effects; more events |
| Productivity | +3% income, +15% resources |
| Sloth | -3% income, -15% resources |
| Temperature away from preference | -5% income and -10% supplies per step |
| Growth | +0.2% monthly population, +10% supplies, +2% income |
| Death | Reverses Growth’s ordinary effects |
| Fortune | +10 percentage points to good-event chance, +0.5% monthly hero chance, more events |
| Misfortune | -10 percentage points to good-event chance, -0.5% monthly hero chance, more events |
| Magic | Friendly mages +1 Research Ability, all units -0.5 MR rounded toward zero, -10% spell fatigue, +50 starting research |
| Drain | Reverse research, MR, fatigue, and starting-research effects |

Default starting research is 150. Default monthly hero chance is 3%.

### Resolved and remaining documentation conflicts

| Rule | Revision-2 manual | Other current evidence | Publication treatment |
| --- | ---: | ---: | --- |
| Growth/Death income | 1% per step | Modding Manual 6.34 default `#deathincome 2`; no official change through 6.36 | Use 2%; resolved at official-documentation tier |
| Order/Turmoil resources | 2% per step | No later official change; some unsupported older tables say 3% | Use 2%; resolved at official-documentation tier |
| Order/Turmoil events | Manual commonly states 2% in its scale table | Current community table says 3% | Reproduce |
| Fortune/Misfortune frequency | 5% more events for either direction | Current community table agrees | Provisionally stable |

The two resolved rows may be used in current calculators, while their integer rounding remains subject to R-008. The event-frequency discrepancy still requires better evidence.

## Order and Turmoil

Order improves economic predictability, recruitment throughput, and unrest recovery while reducing events.

It gains value when:

- Recruitment Points bind troop production;
- the roster converts gold efficiently;
- populous provinces can be held;
- blood hunting or pillage creates recurring unrest;
- a stable economy matters more than event volume.

Turmoil grants design points and increases event frequency. It can be part of a coherent design when:

- the nation has Turmoil-dependent recruitment or freespawn;
- events are deliberately valued;
- the roster is not RP-limited;
- special dominion mechanics reward unrest or chaos;
- early direct power outweighs long-term economic loss.

## Productivity and Sloth

Productivity is the clearest answer to resource-heavy recruitment.

It gains value with:

- heavy armour;
- high-resource sacreds;
- fort networks drawing from strong terrain;
- enough gold and RP to use the additional resources.

Sloth is less painful when:

- important troops have low resource cost;
- the nation relies on summons;
- gold, RP, Holy Points, or Commander Points bind first;
- forts cannot access enough potential resources for Productivity to matter.

The correct test is a queue, not an impression:

```text
desired monthly recruit package
vs
gold, resources, RP, CP, and Holy Points
```

## Temperature

Temperature choice is anchored to national preference, but actual provincial temperature also shifts with seasons, events, rituals, and competing dominion.

Official seasonal behaviour:

- summer usually adds one Heat;
- winter usually adds one Cold;
- caves and outer planes are unaffected;
- deep sea remains neutral;
- ordinary sea is limited to Heat or Cold 1;
- sea seasons apply differently from land.

Temperature affects:

- income and supply relative to national preference;
- snow, rain, river, and passability conditions;
- base encumbrance in severe climates;
- fire and cold battlefield interactions;
- extreme-scale population death.

The right design temperature may reflect an economic preference, a battlefield environment, a national mechanic, or a compromise between them.

## Growth and Death

Growth compounds population, improves supply, and modifies income. It also reduces aging pressure.

It gains value when:

- the game is expected to last;
- provinces are populous;
- armies are supply-intensive;
- the roster uses local Recruitment Points;
- the nation does not destroy its own population.

Death grants design points and may support:

- undead or population-indifferent nations;
- a compressed early timing;
- national mechanics tied to death or corpses;
- maps where long-term civilian economy is unlikely to decide the game.

Death is not free merely because the capital roster is undead. Provinces may still supply gold, resources, tax trace, fort locations, and enemy denial.

## Fortune and Misfortune

Fortune changes event quality and hero arrival chance. Both Fortune and Misfortune increase event frequency under the manual’s ordinary rule.

The scale is sensitive to:

- event settings;
- map size and number of provinces held;
- national event lists;
- Turmoil;
- capital dependence;
- the value of heroes;
- tolerance for variance.

Fortune should not be valued only through expected gold. Events also provide or remove gems, population, scales, sites, commanders, troops, unrest, and strategic options.

## Magic and Drain

Magic accelerates research and reduces spell fatigue while lowering MR. Drain does the reverse.

Magic gains value when:

- many national mages receive the research bonus;
- early breakpoints matter;
- battlefield casting is fatigue-sensitive;
- the nation can exploit lower enemy MR more than it suffers from its own.

Drain gains value when:

- design points fund a stronger immediate package;
- national researchers are efficient despite the penalty;
- high MR is unusually valuable;
- research speed or early magic matters less;
- the nation has researchers unaffected by the scale.

The spell-fatigue modifier applies locally. An army crossing into different scales may find the same script more or less sustainable.

## Extreme scales

Scales at 4 or 5 carry additional effects.

| Extreme | Additional effect |
| --- | --- |
| Order 4 | -2 Research Ability |
| Order 5 | -4 Research Ability |
| Productivity 4 | +1d5 unrest per month |
| Productivity 5 | +1d15 unrest per month |
| Heat or Cold 4 | -0.4% population per month |
| Heat or Cold 5 | -1% population per month |
| Death 4+ | Forests and farms slowly become plains; plains slowly become wastes |
| Growth 4+ | Plains slowly become forests or farms; sea may become kelp |
| Growth 5 | Farms can slowly become forests |
| Fortune 4 | -5% income and resources |
| Fortune 5 | -15% income and resources |
| Magic 4 | Horror marks and +1d5 unrest per month |
| Magic 5 | Horror marks and +1d15 unrest per month |

Farms from extreme Growth require Order. Extreme scales can spread to neighbouring provinces even beyond the god’s ordinary dominion.

### Extreme-scale audit

An extreme scale should be evaluated as a package:

```text
ordinary scale benefit
+ national or form synergy
+ neighbouring pressure
- extreme penalty
- opportunity cost of reaching the scale limit
```

Calling an extreme scale “positive” hides the final two terms.

## Scale design by bottleneck

| National problem | Scale question |
| --- | --- |
| Cannot afford desired recruits | Are Order, Productivity, Growth, and temperature fixing the correct income constraint? |
| Gold remains unused | Is the fort resource- or RP-limited instead? |
| Resource pool remains unused | Is Sloth tolerable because another gate binds? |
| Research arrives late | Would Magic create a meaningful breakpoint, or merely more unfocused RP? |
| Armies starve | Would Growth or temperature matter more than supply items and fort position? |
| Unrest persists | Does Order improve the state enough to justify its cost? |
| Special dominion kills population | Are Growth points being purchased for an economy the nation itself removes? |

# Part VI: Blessings

## How blessings work

A blessing is a package selected during Pretender design and applied to Sacred units and commanders.

Most effects require a sacred to become blessed in battle. Some effects are innate and operate without battle blessing.

Blessing a sacred unit grants:

- +1 Morale;
- the nation’s selected bless effects;
- blessing effects from claimed Thrones held by the nation or its disciple partners.

The H1 spell **Blessing** affects a limited area. H3 **Divine Blessing** affects the battlefield. Access and script timing matter as much as the written bless.

## Bless points

Each Pretender magic-path level above the first grants one bless point.

```text
bless points from a path = max(path level - 1, 0)
```

Example:

```text
Air 2  -> 1 point
Death 4 -> 3 points
Nature 6 -> 5 points

total = 9 bless points
```

Some nations or forms grant bonus bless points.

The cost of an effect is normally the sum of its magic requirements. Scale requirements add no bless-point cost.

A shared pool does not remove path prerequisites. A Pretender may own enough total points yet be unable to buy an effect because its required path is too low.

## Ordinary, innate, and Incarnate

| Tag | Operation |
| --- | --- |
| Ordinary | Active after the unit is blessed in battle |
| Innate or passive | Active without battle blessing, including strategic-map effects where applicable |
| Incarnate | Active only while the Pretender is awake/present under the rule and alive |
| Innate + Incarnate | No battle blessing needed, but still disabled while the god is absent or dead |
| Stackable | May be selected repeatedly; stated bonuses accumulate |

The revision-2 manual uses an asterisk for passive effects and bold type for Incarnate effects. Current data should be checked because individual tags can change through patches or mods.

### The activation state machine

The tags answer different questions. “Blessed” describes the recipient's battlefield state. “Innate” removes the need for that state. “Incarnate” asks whether the Pretender currently exists as an active, living god on the map. An effect can pass one gate and fail another.

| Effect state | Unit blessed? | Pretender active and alive? | Result |
| --- | ---: | ---: | --- |
| Ordinary, not Incarnate | No | Either | Inactive |
| Ordinary, not Incarnate | Yes | Either | Active |
| Ordinary, Incarnate | No | Yes | Inactive |
| Ordinary, Incarnate | Yes | No | Inactive |
| Ordinary, Incarnate | Yes | Yes | Active |
| Innate, not Incarnate | Either | Either | Active on a valid recipient |
| Innate, Incarnate | Either | No | Inactive |
| Innate, Incarnate | Either | Yes | Active on a valid recipient |

For this purpose, an imprisoned or dormant Pretender has not yet become active, and a dead Pretender is absent until recalled or reformed. Incarnate effects do not require the god to stand in the same province, enter the same battle, or project friendly dominion into the recipient's location. The god's active-and-alive state is the gate.

The 6.36 update corrected a design-loading error in which cancelling a loaded Pretender could leave that design's bless effects loaded. This was a setup-state defect, not a new activation rule, but it matters when old designs are inspected or compared.

## Automatic blessing

Official rules:

- the Pretender is automatically blessed in friendly dominion and cannot ordinarily be blessed outside it;
- a Disciple follows the same personal rule;
- Sacred troops fighting alongside the Pretender are automatically blessed only when the battle occurs in friendly dominion.

Automatic blessing is conditional. A sacred army fighting without sufficient Holy support can lose its package even when the nation paid heavily for it.

The main manual does not extend the troop-wide automatic blessing rule to troops merely fighting beside a Disciple. A current community reference uses broader wording, but that disagreement is not enough to replace the official rule. Unless a reproducible current test or later official text establishes otherwise, plan Disciple-led armies around ordinary priests and Divine Blessing.

### Repeatable effects and effects that overlap

“Stackable” in the bless table means that the same blessing can be bought repeatedly and its stated increment accumulates. In the 6.35 structured snapshot, the repeatable entries are:

| Path | Repeatable blessings |
| --- | --- |
| Fire | Superior Morale, Fire Resistance, Attack Skill, Inspirational Presence |
| Air | Precision, Shock Resistance, Farshot, Awareness, Swiftness |
| Water | Cold Resistance, Defence Skill |
| Earth | Reinvigoration, Strength |
| Astral | Arcane Command, Magic Resistance |
| Death | Undying, Undead Command |
| Nature | Hit Points, Poison Resistance |
| Glamour | Heroism, Quiet Stride |
| Blood | Hit Points, Strength |

This permission does not imply that every different effect or external source stacks. Official patches establish two important exceptions:

- Fear and Dread do not stack with one another.
- Displacement supersedes Blur; since 6.24, invisibility also no longer stacks with Blur or Displacement.

Bless-plus-spell, bless-plus-item, multiple aura, regeneration-source, and form-inheritance questions belong to the cross-source stacking and transformation registers in Books IV and XI. They are not inferred from the stackable marker.

## Current unmodded blessing reference

The following tables represent the 6.35 structured data snapshot checked for this edition, overlaid with official changes through 6.36. No 6.36 announcement changes a listed cost, requirement, tag, or numerical effect. Because the main manual's printed list is older and the Inspector snapshot is one executable version behind, these tables remain **Current Data Reference**, not a claim of direct runtime reproduction.

Abbreviations:

- **I:** Incarnate;
- **N:** innate;
- **S:** stackable;
- **MR:** Magic Resistance negates;
- **AP:** armour-piercing;
- **AN:** armour-negating.

### Revision-2 divergence register

The current table is not a literal reprint of the revision-2 manual. The following differences are already material enough to flag before any roster calculation:

| Subject | Revision-2 manual | Current 6.35 data / 6.36 official overlay | Evidence boundary |
| --- | --- | --- | --- |
| Inspirational Presence | Fire 4 | Fire 3 | Current structured reference |
| Resilience of the Earth | Earth 5 | Earth 6 | Current structured reference |
| Fortitude | Earth 7 | Earth 8 | Current structured reference |
| Reconstruction | Printed older tag state | Incarnate, not passive | Official 6.04 correction plus current reference |
| Fear blessing | Death 8 | Death 9 and Turmoil 1 | Current structured reference; Fear/Dread costs and interaction were revised again in 6.23 |
| Heroism | +50% experience | +35% experience | Official 6.08 change |
| Fear and Dread together | Older guides may stack them | They do not stack with one another | Official 6.08 change |
| Enchanted Blood | Blood 4 | Blood 3 | Current structured reference |
| Passive Pretender effects outside friendly dominion | Older faulty behaviour could remove them | Passive blessings remain active | Official 6.08 correction |
| Cancelled loaded Pretender | Could leave the loaded design's bless effects selected | Cancel now clears the unwanted loaded bless | Official 6.36 correction |

Frost Mist Weapons retains its printed Water 7 and Cold 1 requirement. An earlier edition removed the Cold scale requirement on the strength of an unsupported transcription; the manual and current reference agree, so that change has been reversed.

### Fire

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| F1 | Superior Morale | +1 Morale | S |
| F1 D1 | Wasteland Survival | Wasteland Survival | N |
| F2 | Fire Resistance | +5 Fire Resistance | S |
| F2 | Attack Skill | +1 Attack | S |
| F3 | Inspirational Presence | Inspirational +1 and +50 leadership | N, S |
| F4 | Righteous Wrath | Nearby sacred death triggers temporary +3 Attack, +3 Strength, +6 Morale |  |
| F5 | Death Explosion | On death: 10 AP fire damage, area 4 plus Size | I |
| F5 | Heat Aura | Heat Aura and +10 Fire Resistance | I |
| F6 | Fire Shield | Fire Shield 7 | I |
| F7 | Flaming Weapons | 8 AP fire damage on hit | I |
| F8 S4 | Unbearable Splendour | Sight Vengeance; attacker may be blinded, MR negates | I |

The manual printed Inspirational Presence at F4. Current data places it at F3. The current non-Incarnate, innate treatment should be used for the 6.35 snapshot and 6.36 official overlay.

### Air

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| A1 | Precision | +1 Precision | S |
| A2 | Shock Resistance | +5 Shock Resistance | S |
| A2 | Farshot | +30% mundane weapon range | S |
| A3 | Awareness | Unsurroundable 2 | S |
| A4 | Swiftness | Swiftness 30 and +1 Defence | S |
| A4 | Storm Flight | Storm Immunity for flight |  |
| A5 | Wind Walker | +6 Map Move | N, I |
| A5 E1 | Weightlessness | Floating and halved armour encumbrance | I |
| A6 | Air Shield | Air Shield 80 | I |
| A7 | Thunder Weapons | Capped shock damage and shock fatigue on hit | I |
| A8 | Charged Bodies | Overcharged 20 and +5 Shock Resistance | I |
| A9 | Flight | Flight | I |

Farshot changes weapon range, not spell range. Wind Walker matters on the strategic map but remains Incarnate in the unmodded current table.

### Water

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| W1, Cold 1 | Winter’s Gift | Snow Move | N |
| W1 N1 | Swamp Survival | Swamp Survival | N |
| W2 | Cold Resistance | +5 Cold Resistance | S |
| W2 | Swimming | Swimming | N |
| W2 | Defence Skill | +1 Defence | S |
| W5 | Chill Aura | Chill Aura and +10 Cold Resistance | I |
| W5 | Slowing Weapons | Damaging hit may slow; MR negates | I |
| W6 F2 | Vitriol Weapons | 7 AP acid damage on hit | I |
| W6 | Water Breathing | Water Breathing | N, I |
| W7, Cold 1 | Frost Mist Weapons | Cold clouds created by attacks | I |
| W9, Magic 1 | Quickness | Quickness | I |

Quickness changes action economy and fatigue exposure as well as offence. It should be evaluated with the sacred’s attacks, encumbrance, survivability, and vulnerability to fatigue counters.

### Earth

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| E1 | Mountain Survival | Mountain Survival | N |
| E2 | Reinvigoration | +1 Reinvigoration | S |
| E2 | Strength | +1 Strength | S |
| E4 | Unbreakable | Affliction Resistance 3 |  |
| E4 N3 | Larger | Permanent increase in Size | N |
| E5 | Reconstruction | Regeneration for Inanimates | I |
| E6 | Resilience of the Earth | +10 Fire and Shock Resistance | I |
| E6 | Hard Skin | +5 natural protection | I |
| E8 | Fortitude | Broad physical resistances | I |

Larger changes more than Hit Points. Size can affect square density, repel interactions, trampling relationships, and target profile. It should be tested on the exact sacred roster.

### Astral

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| S1 | Arcane Command | Grants or improves magic leadership | N, S |
| S2 | Magic Resistance | +1 MR | S |
| S3 D1 | Spirit Sight | Spirit Sight |  |
| S3 F1 | Solar Weapons | 4 AP holy fire damage on hit |  |
| S4 | Far Caster | +1 spell-range multiplier level |  |
| S4 | Arcane Finesse | +1 spell penetration |  |
| S5 | Magic Weapons | Mundane weapons become magical | I |
| S6 | Twist Fate | Negates the first damaging hit under its rule | I |
| S7, Misfortune 1 | Fateweaving | Attackers may suffer misfortune; MR negates | I |
| S8, Magic 2 | Etherealness | Ethereal | I |

Astral blessings can support sacred mages and commanders rather than only melee troops. Far Caster and Arcane Finesse should be valued by the actual sacred spell roster.

### Death

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| D1 | Undying | -2 minimum Hit Points before death | S |
| D1 | Undead Command | Grants or improves undead leadership | N, S |
| D2, Death 2 | Half Dead | Need not eat and strong disease resistance | N |
| D3 | Mending Bones | Recuperation for undead | N |
| D4 | Withering Weapons | Damaging hit may cause Decay; MR negates |  |
| D5 | Stygian Flesh | Invulnerability 10 | I |
| D6 | Reforming Flesh | 10% regeneration for undead | I |
| D7 | Reanimators | Many attacks deal unlife damage; additional undead leadership | I |
| D8 | Death Weapons | Armour-negating death damage and disease checks | I |
| D9, Turmoil 1 | Fear | Fear 5 | I |

Undying does not prevent routing, fatigue collapse, soul destruction, or every form of battlefield removal. Its value depends on whether the sacred can still act while surviving below ordinary zero Hit Points and whether recovery is possible afterward.

### Nature

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| N1 | Hit Points | +1 Hit Point | S |
| N1 | Low Light Vision | Darkvision 50 |  |
| N2 | Poison Resistance | +5 Poison Resistance | S |
| N2 | Forest Survival | Forest Survival | N |
| N3, Magic 1 | Unaging | Slower aging and younger sacred recruitment | N |
| N4 D1 | Poison Weapons | Poison damage on damaging hit |  |
| N5 | Recuperation | Living units recover afflictions | N, I |
| N5 | Berserker | Berserker +2 | I |
| N6 | Barkskin | Barkskin protection package | I |
| N7 | Regeneration | 10% regeneration for compatible units | I |

Regeneration is percentage-based, so it scales with Hit Points. Its full value also depends on incoming burst damage, poison, decay, fatigue, disease, and whether the unit survives long enough to receive repeated healing.

### Glamour

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| G1 | Undreaming | Unsleeping 4 |  |
| G1 | Heroism | +35% experience gain | S |
| G2 | Quiet Stride | +20 Stealth if already stealthy | N, S |
| G3 | True Sight | True Sight |  |
| G3 | Blur | Attackers suffer -2 Attack under the sight rules |  |
| G6 | Obfuscate | Grants Stealth 40 or adds 40 to existing Stealth | N, I |
| G6 F2 | Awe | Awe 3 | I |
| G7 | Displacement | Attackers suffer -5 Attack; replaces Blur | I |
| G7 | Dread | Dread 5 under the sight rules | I |
| G8 | Luck | Luck | I |

Official update 6.08 reduced Heroism from +50% to +35% experience. Older guides and the printed revision-2 manual may retain the former value.

### Blood

| Requirement | Name | Effect | Tags |
| --- | --- | --- | --- |
| B1 | Hit Points | +1 Hit Point | S |
| B2 | Strength | +1 Strength | S |
| B3 | Strong Blood | +5 Poison Resistance and strong disease resistance | N |
| B3 | Enchanted Blood | Slow regeneration, +1 MR, and bleeding immunity |  |
| B4 | Blood Surge | A kill triggers temporary +3 Attack, +3 Strength, +1 Defence, +1 Reinvigoration |  |
| B5 | Blood Bond | Distributes part of damage among nearby bonded units | I |
| B6 | Unholy Weapons | 15 AP damage against sacred or blessed targets | I |
| B7 | Blood Vengeance | Attacker may suffer the inflicted damage; MR resists | I |
| B8 D4 | Vampiric Weapons | 3 AN life-drain damage on damaging hit | I |

Blood Bond changes damage distribution rather than removing damage. Formation, unit spacing, regeneration, area damage, and unequal protection can change whether distribution helps or accelerates collapse.

## Weapon blessings: what causes the rider to fire

The phrase “weapon blessing” covers several different mechanisms. Treating them as interchangeable produces bad counter advice, especially when armour, shields, zero-damage hits, spells, natural weapons, and ranged attacks enter the same battle.

| Trigger family | Blessings | Present rule |
| --- | --- | --- |
| Weapon property | Magic Weapons | Changes an otherwise mundane parent weapon into a magical weapon; it does not add a second damage packet. Since 6.25 the property also works correctly for repel attacks. |
| On hit | Flaming Weapons, Thunder Weapons, Slowing Weapons, Vitriol Weapons, Solar Weapons, Death Weapons, Unholy Weapons | The rider is tied to a successful weapon hit under its own damage, resistance, target, and MR rules. A parent hit need not always inflict ordinary HP damage unless the individual blessing says otherwise. |
| On damaging hit | Withering Weapons, Poison Weapons, Vampiric Weapons | The parent attack must first cause damage. A shield, protection, immunity, or other prevention that leaves no qualifying damage can therefore suppress this class. |
| Attack-generated field | Frost Mist Weapons | Attacks create cold mist rather than attaching an ordinary direct-damage rider. Official fixes make ranged misses create the cloud and make the cloud appear even when the target is killed. |
| Probabilistic attack conversion | Reanimators | The current reference assigns a 50% chance for hits, including spell hits, to deal Unlife Damage; the bless also grants undead leadership. This is a special rule, not a model for other weapon blessings. |

### Patch-established boundaries

- The 6.12 update stopped some breath weapons from incorrectly receiving weapon blessings and stopped Flaming Weapons from affecting melee ice weapons.
- The 6.19 update repaired weapon-blessing interaction with mirror images.
- The 6.23 update made friendly units immune to Unholy Weapons and allowed Vampiric Weapons to drain a little life when the target dies from the attack.
- The 6.29 update stopped Phoenix Pyre from triggering weapon blessings.
- The 6.34 update made shields protect correctly against weapon blessings that are not armour-negating.

The shield correction proves that shield protection participates in resolving applicable riders. It does not, by itself, prove that every blocked attack is treated as a hit or a miss for every blessing. When that distinction decides a build, the battle log and a reproducible current test are still the correct evidence.

### Counter-analysis by trigger

| Question | Why it matters |
| --- | --- |
| Did the parent attack hit? | All ordinary weapon riders begin with a qualifying attack connection. |
| Did the parent attack cause damage? | Withering, Poison, and Vampiric Weapons require this additional gate. |
| Is the rider AP or AN? | Armour and shield protection interact differently with the added packet. |
| Does MR negate the rider? | Slowing and Withering can fail after the physical attack succeeds. |
| Is the target in the required class? | Unholy Weapons is specialised against sacred or blessed targets and excludes friendlies. |
| Is the attack an excluded breath, ice, or triggered effect? | The patch history contains explicit exclusions; visual resemblance to a normal weapon is insufficient. |
| Does the effect create an area rather than damage the struck target? | Frost Mist can matter after a miss or a killing blow because its cloud is the product. |

## Blessing from items

The Modding Manual distinguishes two item mechanisms:

| Command | Model | Consequence |
| --- | --- | --- |
| `#bless` | Shroud of the Battle Saint | Applies the Bless spell to the bearer automatically. The item is itself the source of the blessed state. |
| `#autobless` | Flask of Holy Water | Automatically blesses the bearer only if the bearer is Sacred. |
| `#bestowtomount` | Mount propagation modifier | Causes a supported effect defined after the command to be bestowed on the mount as well. It must be read with the specific item effect, not as a universal rider-to-mount rule. |

The current 6.35 item snapshot identifies the Shroud of the Battle Saint, Immaculate Shield, Armor of Virtue, and Sun Sword as item-granted blessing sources. The Flask of Holy Water uses the sacred-only route. These items can make a unit blessed without a priest, but they do not erase the ordinary Incarnate gate: an Incarnate effect still switches off while the Pretender is absent or dead.

Official update 6.34 established one unusually important lifetime rule: a magic-item blessing persists when Life after Death changes the bearer. That is firm for this case and should not be generalised to every shape-change mechanism.

## Riders, mounts, and separate sacred status

A mounted unit is not one undifferentiated sacred object. The rider form and mount have their own records and can have different Sacred flags. Current examples show both matched and unmatched pairs: the Knight of the Chalice and its Destrier are Sacred, the Wind Rider and Armored Pegasus are Sacred, while the Triton Knight and its mount are not. The 6.02 correction that gave Triton Knights their proper mount state is further evidence that mount data are resolved separately.

This produces four practical rules:

1. Do not infer the mount's Sacred status from the rider's title or icon.
2. Do not infer that an item effect reaches the mount unless the effect supports the mount-bestow mechanism or a current rule says so.
3. Do not infer that a dismounted or transformed body retains the original body's sacred and blessed state; inspect the resulting form and the source that created the state.
4. Keep movement abilities separate from blessing. For example, 6.36 makes a swimming mount sufficient for river crossing, but that does not make the rider or mount Sacred.

Exact transfer when a mount dies, a rider dismounts, or one component changes form remains part of the mount and transformation research in Book XI. The blessing chapter records the independent-object rule without inventing an unverified transfer sequence.

## Shape change and effect lifetime

Three questions should be asked separately whenever a blessed unit changes body:

1. Is the resulting body still Sacred?
2. Does the unit still possess the blessed state from the original source?
3. If the state remains, which Innate or Incarnate effects are currently eligible?

Only the item-blessing Life after Death case has a direct official ruling in the present evidence set. Ordinary shape change, secondshape, mount loss, transformation, death-shape, and new-body interactions remain governed by their specific form rules and the transformation register. A single successful case is not evidence for a universal inheritance rule.

## Display, tooltip, and engine state

The blessing interface has accumulated several corrections: 6.04 repaired Incarnate information for known blessings, 6.08 repaired Throne-granted Awe display, 6.13 made Obfuscate appear in bless information, 6.23 corrected Half Dead display, and 6.35 printed Enchanted Blood's Magic Resistance bonus. These changes make the current interface more useful, but they also demonstrate why an icon or tooltip is not conclusive evidence of activation in every edge case.

For a disputed interaction, record all three layers:

- the design-screen or unit-panel description;
- the battle log and observed state;
- the official rule or patch record that explains the result.

### R-016 research decision

R-016 is complete for the present unmodded scope: current tags and requirements, battlefield and Incarnate gates, automatic blessing boundaries, repeatable effects, documented overlap exceptions, weapon-trigger families, item-granted blessing, and the independent status of riders and mounts. Cross-source stacking remains R-049; transformation and effect lifetime remain R-040 and R-052. This division closes the blessing question without pretending that adjacent engine-state questions have also been solved.

## Bless design by function

### Expansion reliability

An expansion bless should solve a measured failure.

Common failures:

- attacks do not connect;
- hits fail to penetrate protection;
- sacreds are surrounded;
- chip damage accumulates;
- morale fails after casualties;
- fatigue produces critical hits;
- elemental independents bypass defence;
- too many sacreds die for the expansion to be economical.

The best blessing is not the one with the largest description. It is the cheapest package that changes the relevant battle result with an acceptable margin.

### Offence

Offensive blessings fall into several families:

| Family | Examples | Best against | Weakness |
| --- | --- | --- | --- |
| Accuracy | Attack Skill, Righteous Wrath | High defence | Does not solve low damage |
| Damage | Strength, Blood Surge | Protection and high HP | Requires hits and often kills |
| On-hit riders | Flaming, Solar, poison, death, vampiric weapons | Targets vulnerable to the added type | May require damaging hit or face resistance |
| Tempo | Quickness | Targets overwhelmed by action volume | Doubles fatigue exposure and incoming opportunity |
| Attrition | Withering, slowing, fear, dread | Long fights or morale-sensitive armies | MR, immunity, sight, or fast killing can counter |

### Defence

Defensive blessings should be separated by threat:

- mundane weapon avoidance;
- natural or armour protection;
- physical resistance;
- elemental resistance;
- Magic Resistance;
- affliction recovery;
- regeneration;
- first-hit insurance;
- luck or ethereal avoidance;
- formation and unsurrroundability;
- morale.

Stacking one layer creates a specialist. Layering different defences creates breadth but may buy too little of each to change a breakpoint.

### Mobility and logistics

Strategic mobility effects can be worth more than battlefield statistics when they allow:

- faster reinforcement;
- unexpected routes;
- forest, swamp, mountain, snow, or wasteland movement;
- underwater operations;
- stealth armies;
- regrouping with the main force.

The effect must apply to every necessary member of the force. A commander with mobility but troops without it, or sacred troops without a matching commander, may not produce the expected movement.

### Sacred commanders and mages

Bless value is not confined to line troops.

Sacred commanders may exploit:

- leadership blessings;
- undead or magic command;
- map movement;
- stealth;
- recuperation;
- Unaging;
- Far Caster;
- Arcane Finesse;
- reinvigoration;
- resistances;
- defensive effects for thugging.

When sacred mages are numerous, a small caster-oriented bless can affect hundreds of mage-turns and battles.

### Mass sacreds versus elite sacreds

Mass sacreds often value:

- cheap stackable statistics;
- morale;
- resistances against common area damage;
- on-hit effects multiplied by many attacks;
- effects triggered by sacred deaths.

Elite sacreds often value:

- percentage regeneration;
- layered resistance;
- protection of an expensive body;
- affliction recovery;
- mobility;
- effects that preserve veteran experience;
- tools against specific counters.

This is a tendency, not a law. Attack count, HP, slots, recruit limit, cost, and battlefield role are more important than the labels “mass” and “elite.”

## Bless throughput

The value of a blessing depends on how many useful recipients can be fielded.

```text
monthly sacred throughput =
  minimum of:
    gold capacity
    resource capacity
    Recruitment Points
    Holy Points
    recruitment limit
    fort availability
    commander and leadership capacity
```

A 200-point blessing affecting six capital-only sacreds per month is a different investment from the same blessing affecting sacreds at every fort.

### Practical bless value

```text
practical bless value =
  effect per relevant sacred
  x relevant sacreds fielded
  x battles in which blessing is active
  x probability the effect changes the result
```

The expression is conceptual, not an engine formula. It forces the design to include throughput, activation, and relevance.

## Bless access and scripting

Audit:

- number and Holy level of priests;
- whether H3 Divine Blessing is available;
- priest movement relative to sacred armies;
- priest survivability;
- the round on which blessing lands;
- whether sacreds engage before being blessed;
- battlefield size and formation;
- whether a Prophet is required;
- whether automatic blessing conditions apply;
- what happens when the priest is assassinated or delayed.

An unblessed sacred is missing more than a bonus. It may be an expensive unit designed around statistics it does not currently possess.

## Counter-audit

For every major blessing, name:

1. the damage type or control effect it does not resist;
2. the relevant immunity or resistance;
3. the MR check, if any;
4. the sight rule, if any;
5. whether the effect requires a damaging hit;
6. whether it is Incarnate;
7. whether it depends on formation or nearby sacreds;
8. whether fatigue defeats it;
9. whether routing defeats it;
10. how the opponent can avoid fighting the blessed army at all.

No blessing removes the need for scouting.

# Part VII: Divine Magic and Priest Identity

## Divine magic

Divine spells:

- require Holy skill rather than ordinary paths;
- require no research;
- are available from the beginning;
- include spells such as Blessing, Banishment, Smite, and Divine Blessing.

The Pretender’s magic can replace the nation’s ordinary Banishment and Smite with path-themed versions.

If the Pretender has no path at level 4 or higher, priests retain ordinary Banishment and Smite.

If one or more paths reach the threshold:

- the highest path determines the replacement family;
- ties use the manual’s priority order;
- Banishment and Smite each receive the corresponding replacement;
- Blood has no Banishment replacement.

### Divine spell families

| Path | Banishment replacement | Smite replacement | Character |
| --- | --- | --- | --- |
| Fire | Ashes to Ashes | Heavenly Fire | Burning and armour-negating fire |
| Air | Wind of Memories | Heavenly Strike | Range, area, and shock |
| Water | Purifying Water | Watery Death | Area, drowning, and anti-unarmoured secondary damage |
| Earth | Pull from the Grave | Word of Stone | Grip and petrification |
| Astral | Stellar Decree | Word of Power | Range, stun, and paralysis |
| Death | Decree of the Underworld | Syllable of Death | Bewilderment, exhaustion, or death |
| Nature | Final Rest | Word of Thorns | Kill attempt, entanglement, and bleeding |
| Glamour | Return of the Past | Word of Bewilderment | Anti-minded undead and confusion |
| Blood | No replacement | Claim Life | Anti-living damage and Chest Wound |

Pretender paths alter the national priest toolkit even when those paths are never used for a ritual.

### Design implication

A high path may simultaneously buy:

- personal casting;
- bless points;
- a bless prerequisite;
- a new priestly Banishment;
- a new priestly Smite;
- site-search or forging access.

That bundle is strategically meaningful. It should still be compared with the cost curve required to reach level 4 or higher.

# Part VIII: Death of a God

## Ordinary Pretender death

Each ordinary Pretender death causes either:

- loss of one magic-path level; or
- loss of one dominion-strength point.

The chance to lose magic is:

```text
50% + 10% x Nature level at death
```

If no path level is lost, or no magic is available to lose, dominion falls by one. Dominion cannot fall below 1 through this rule.

Nature makes magic loss more likely. The path selected for loss is weighted, with Nature more exposed and Death less exposed. The manual also notes small chances to gain Death and still smaller chances to gain Astral or Blood. Exact weights belong in the controlled-test register unless directly extracted from current data.

## Why death compounds

A death can remove:

- the Pretender’s commander-turns;
- Incarnate blessing effects;
- personal expansion or battle presence;
- ritual access;
- item access while the body is absent;
- a magic path or dominion strength on return;
- candles through the reduced maximum and check chance;
- confidence in a throne or war timetable.

The casualty affects the whole nation, not only the dead commander.

## Call God

Priests may use the Call God order after an ordinary Pretender death.

The revision-2 manual gives the player-facing model: every assigned Holy level generates one point per month, the Pretender returns to the home province after “around 50,” and recalling the main Pretender in a Disciple game requires 50% more. It deliberately says that the total is not exactly 50 so that the arrival is uncertain. Its example assigns three H1 priests and one H2 and predicts about ten months.

The Modding Manual adds two official modifiers:

- **Elegist:** the unit's Elegist value is added to its priest level while calling a god or Disciple;
- **Recall God:** an applicable nation or claimed-Throne `#recallgod` value is added to the priest level of everyone performing Call God.

The main manual also gives the special Trinity rule: a dead member of a Trinity can be called back in half the normal time. The official text defines the time result, not the internal threshold calculation.

### Reconciled current model

Published controlled research resolves the manual's apparent uncertainty by moving the randomness from the target into each priest's monthly contribution. The tested base threshold is 50 points. An ordinary priest contributes its effective recall rating, plus or minus one, each month. The small published sample found the three outcomes equally or nearly equally weighted; that weighting remains a community-tested estimate rather than an official probability table.

For ordinary positive ratings:

```text
effective recall rating =
  Holy level
  + Elegist value
  + applicable Recall God modifier

monthly contribution per priest =
  effective recall rating - 1, effective recall rating,
  or effective recall rating + 1
```

An ordinary H1 contributes 0-2 points in a month, H2 contributes 1-3, and H3 contributes 2-4. Elegist changes the rating before that variation: an H1 Elegist (2) calls at the same ordinary rate as an H3. Elegist alone does not grant the order; the unit must still be a priest.

| Caller | Monthly range | Approximate average | Approximate solo time from an empty pool |
| --- | ---: | ---: | ---: |
| One H1 | 0-2 | 1 | 50 months |
| Five H1 | 0-10 | 5 | 10 months |
| One H2 | 1-3 | 2 | 25 months |
| One H3 | 2-4 | 3 | 17 months |
| Three H3 | 6-12 | 9 | 6 months |
| One H1 Elegist (2) | 2-4 | 3 | 17 months |

These are capacity estimates, not deadlines. With roughly symmetric `-1/0/+1` variation, a useful planning approximation is:

```text
expected months for an ordinary Pretender =
  ceiling(50 / sum of effective recall ratings)

expected months for the main Pretender in a Disciple game =
  ceiling(75 / sum of effective recall ratings)
```

The 75-point figure follows from the tested 50-point base and the manual's official 50% increase. The formula predicts the centre of the workload, not the exact return month. A small priest corps has proportionally wider timing risk; many callers average the monthly variation more effectively.

### Who can contribute in a Disciple game

Current community documentation reports that:

- a Disciple nation's priests may help recall the main Pretender;
- the Pretender nation's priests may help recall any dead Disciple on the team;
- a Disciple nation's priests may recall their own Disciple, but not another nation's Disciple.

Those cross-team routing rules are **Current Community Reference**, not wording supplied by the revision-2 manual. A legacy community mechanics page reports 25 points for one dead Trinity member, consistent with the official half-time rule, but the library retains the official result rather than presenting that implementation detail as directly reproduced under 6.36.

### Order, interruption, and return

Call God resolves at hosting step 16. A caller removed by an earlier ritual or magic battle cannot be assumed to contribute. Once step 16 has passed, a later assassination or ordinary battle cannot retroactively remove that month's points. This timing conclusion follows directly from the official hosting order.

The manual places the returning Pretender in the nation's home province. Current community documentation refines this to the capital province: inside the fort when the nation still owns it, even under siege, and outside the walls if the capital has been lost. A hostile return can cause an immediate fight. These placement details remain **Current Community Reference** until a 6.36 return-state reproduction or later official wording is preserved.

Version 6.28 repaired Call God when the order was issued without its keyboard shortcut. That was an order-interface defect, not a change to the contribution model. No later official update through 6.36 changes Call God.

### R-017 decision

R-017 is complete at a mixed evidence tier:

- **Official:** the order, ordinary Holy contribution model, Disciple-game 50% increase, home-province return, Elegist and Recall God modifiers, Trinity half-time rule, and hosting step;
- **Community-tested:** fixed 50-point ordinary threshold and per-priest effective-rating `-1/0/+1` variation;
- **Current Community Reference:** detailed Disciple routing and capital/fort placement.

Future direct runtime testing would upgrade the last two layers, but the present evidence is sufficient for planning as long as the labels remain attached.

### Recall opportunity cost

Every calling priest is not:

- blessing an army;
- preaching;
- blood sacrificing;
- claiming a Throne;
- researching if also a mage;
- moving with a force;
- performing another special order.

A recall plan should identify the priests before the god takes a high-risk battle.

## Immortality

### Dominion Immortal

A dominion-immortal Pretender normally reforms if killed in friendly dominion. Death outside friendly dominion requires Call God.

### Immortal

An Immortal normally reforms regardless of friendly dominion on the ordinary plane.

### Limits

- Soul Slay or equivalent soul destruction can prevent ordinary reform and require Call God.
- Death on a remote plane can prevent immortality.
- Reform time is often about three months but varies by form.
- Reform removes most afflictions.
- Immortality alone does not improve ordinary affliction recovery while alive.

Dominion-immortal combat planning should always include the candle state at the battle location and the possibility that dominion changes before combat resolves.

## Safe and unsafe risk

| Situation | Principal risk |
| --- | --- |
| Immortal god in ordinary plane | Temporary absence, items, operational gap, soul attacks |
| Dominion Immortal in strong friendly candles | Same, plus candle reversal before battle |
| Dominion Immortal on frontier | Failure to reform if dominion becomes hostile |
| Any god on remote plane | Immortality may not operate |
| Any god facing soul destruction | Call God and permanent-loss consequences |
| Non-immortal god in battle | Full recall delay, path or dominion loss, disabled Incarnate bless |

# Part IX: Special Dominions

## Why special dominions deserve their own audit

Some nations transform candles into effects far beyond ordinary scales and morale. Special dominions may:

- kill population;
- create units;
- spread disease or insanity;
- change terrain;
- alter unrest;
- hide information;
- empower constructs;
- enable movement;
- modify religious conflict.

The design question becomes:

```text
value of another candle =
  ordinary dominion value
  + special national effect
  + scale convergence
  + survival value
```

## Major categories

| Nation or family | Special dominion effect | Strategic consequence |
| --- | --- | --- |
| Arcoscephale, all ages | Accurate scrying throughout dominion, including Glamour detection | Candles become an intelligence network |
| EA and LA Mictlan | Dying dominion and blood-sacrifice dependence | Blood economy and temples are core religious logistics |
| Yomi | Oni arise from temples according to turmoil, terrain, and temperature | Scales, temples, and terrain form a freespawn system |
| MA Ermor | Population death and undead arising | Civilian economy is converted into an undead dominion |
| MA Asphodel | Population death and Manikin generation | Growth, forests, corpses, and dominion interact unusually |
| MA C'tis | Miasma, disease, rain, wetness, and terrain effects | Friendly and hostile forces experience different economic and disease pressure |
| MA Agartha | Golem Cult improves constructs' Hit Points | Candles can strengthen friendly, allied, and enemy constructs |
| LA R'lyeh | Dreamlands spread insanity and related effects | Dominion is psychological warfare as well as faith |
| EA Therodos | Population death and fort-related ghost generation | Forts and dominion convert population into spectral power |
| Phaeacia | Dark-ship sailing linked to friendly dominion | Candles become movement infrastructure |
| EA Mekone | Improved effective maximum in dominion conflict | Religious contests behave better than the printed initial score suggests |
| MA and LA Phlegra | Dominion-linked unrest | More candles can carry an internal economic cost |
| Ubar, Na'Ba, Ind, Feminie | Province information can be hidden | Dominion creates strategic uncertainty |

This table identifies system categories, not complete nation guides. Exact inheritance by Disciples and exact scale formulas belong in the later nation dossiers.

## Special-dominion design questions

1. Does the effect scale with local candles, maximum dominion, temples, or merely presence?
2. Does it affect allies, Disciples, enemies, or everyone?
3. Does it operate underwater, in caves, or on remote planes?
4. Does it change population, terrain, unrest, or recruitment permanently?
5. Can an enemy exploit the effect?
6. Does high dominion improve the effect enough to justify its point curve?
7. What happens if the special dominion overruns a valuable captured economy?

# Part X: Teams and Disciples

## Shared and separate systems

In a disciple game:

- the team has one Pretender and one or more Disciples;
- disciples awaken in about half the Pretender’s delayed time;
- team size increases the number of temples required to raise maximum dominion;
- Call God requires 50% more progress;
- claimed-Throne blessings can be shared within the team;
- ordinary team play has no Prophets because Disciples fill the religious role.

The team needs one religious network, not a collection of independent personal builds.

## Disciple design audit

Record:

- which Pretender blessings the Disciple and sacreds receive;
- which Incarnate effects depend on the Pretender’s state;
- which special dominion effects transfer to the Disciple;
- temple responsibility by geography;
- preaching and blood-sacrifice responsibility;
- Call God priest reserve;
- Throne-claiming access;
- land-sea religious boundaries;
- whether the Disciple’s personal paths and body create an independent battlefield role.

Some special dominions transfer fully, some partially, and some not at all. This must be checked nation by nation.

# Part XI: The Frozen Modded Ruleset

## Exact definitions belong to Book IX

The former edition repeated DE's global scale table, the complete blessing delta, broad command counts, and Divinitus chassis counts here. Book IX now provides the corrected source inventory and is the only authoritative home for those figures.

Book III keeps the design consequences:

- DE changes the economic weight of several scales;
- many blessings become cheaper, cross-path, or independent of an awake Incarnate chassis;
- DE broadly rewrites Pretender availability, starting dominion, path cost, and national god lists;
- Divinitus then adds a second chassis layer whose sites, events, items, summons, scale limits, and delayed powers may matter more than the visible card;
- the final design must be calculated after both files load.

This division matters. Book IX answers, "What did the files define?" Book III answers, "How should a player reason about the resulting design?"

## Modded-design audit

For every combined design:

1. name the exact nation and form ID;
2. confirm final form availability after load order;
3. record final starting paths and New Path Cost;
4. record final starting dominion;
5. record final scale limits;
6. record prison restrictions;
7. calculate blessing costs from Book IX's current table;
8. identify non-Incarnate and cross-path conversions;
9. check national bless-point bonuses;
10. test displayed totals in the actual design screen.

# Part XII: Complete Design Method

## Step 1: Define the national plan

Write one sentence:

> The nation intends to reach **this first military state**, using **these units and spells**, by **this turn range**, while preserving **this economy or late-game route**.

If the sentence cannot be written, Pretender selection is premature.

## Step 2: Identify mandatory constraints

Examples:

- sacreds require Fire Resistance to survive the nation’s own battlefield plan;
- ordinary expansion fails without a personal expander;
- the roster has no feasible path into a required ritual;
- capital sacred throughput requires Dominion 8;
- the special dominion needs rapid temple expansion;
- the first war is expected before a dormant god can arrive.

Mandatory constraints eliminate designs before subjective preference begins.

## Step 3: Build the cheapest functional design

Purchase only the elements needed to make the plan work:

- minimum reliable expansion package;
- minimum bless breakpoint;
- minimum dominion for sacred throughput and faith;
- minimum magic access;
- acceptable scales;
- correct awakening.

This creates a baseline against which luxuries can be priced.

## Step 4: Spend the remainder on leverage

Possible leverage:

- one more dominion candle;
- a scale threshold;
- a second resistance;
- a new path;
- a better chassis;
- earlier awakening;
- an Incarnate blessing;
- broader divine magic;
- more robust expansion.

Each addition should have a named use.

## Step 5: Test the opening

Run repeated expansion tests against:

- heavy infantry;
- cavalry;
- archers;
- barbarians;
- undead;
- poison;
- high defence;
- high protection;
- unusual terrain;
- the strongest common independent province under the lobby settings.

Record losses and failure conditions, not only wins.

## Step 6: Test the first war

Construct a representative enemy answer:

- armour;
- evocations;
- poison;
- fatigue;
- magic weapons;
- MR-negates control;
- flyers or flankers;
- sacred counters;
- anti-thug tools.

The purpose is not to prove invincibility. It is to identify what scouting must detect and which research branch answers it.

## Step 7: Test the economy

Simulate at least twelve turns of:

- capital recruitment;
- expansion parties;
- first fort and laboratory;
- mage recruitment;
- upkeep;
- Holy Point use;
- resource and RP bottlenecks;
- temple schedule.

Strong paper scales can still fail to fund the intended sequence.

## Step 8: State the failure modes

A publishable design should name:

- its worst independent matchup;
- its first-war counter;
- its economic bottleneck;
- its Incarnate dependency;
- its god-death consequence;
- its map weakness;
- the latest safe arrival;
- the research branch it cannot afford early.

# Part XIII: New-Player and Expert Audits

## New-player design audit

Before confirming:

- Does the total equal the design screen?
- Can the nation expand without assuming perfect battles?
- Who blesses the sacreds?
- Are the important effects Incarnate?
- When does the god arrive?
- Do the scales support the troops actually being recruited?
- Is temperature set relative to national preference?
- Is dominion high enough for the intended sacred output?
- What does the god do after expansion?
- Which path solves a national magic gap?
- What happens if the god dies?
- Is any number copied from an unmodded guide into a modded game?

## Expert design audit

### Budget

- marginal point cost of every path;
- marginal point cost of every candle;
- scale-limit opportunity cost;
- point value of awakening delay;
- unused point remainder.

### Timing

- expansion turn targets;
- first fort and lab;
- research breakpoints;
- awakening range;
- first Incarnate-bless battle;
- first ritual or forge use;
- first expected enemy timing.

### Religion

- starting maximum dominion;
- temple thresholds;
- checks per month;
- front-line preaching;
- blood-sacrifice capacity;
- land-sea barriers;
- special-dominion effects;
- dominion-kill recovery.

### Bless

- recipients per month;
- activation method;
- effect by combat role;
- effect while god absent;
- counters;
- scale and side requirements;
- commander and mage beneficiaries.

### God risk

- safe dominion for combat;
- immortality limits;
- soul-destruction exposure;
- remote-plane exposure;
- recall priest-months;
- item loss;
- path or dominion loss;
- turns without Incarnate effects.

### Mod integrity

- exact patch;
- exact `.dm` files;
- hashes;
- load order;
- final design-screen values;
- whether a later mod overwrites the form or nation.

# Part XIV: Controlled-Test Programme

## Test P1: Awakening distribution

For awake, dormant, and imprisoned forms:

1. use identical nation, map, seed policy, and game settings;
2. use at least 200 independent seeds per delayed state rather than repeatedly re-hosting one save;
3. record the first turn on which the god is present and the corresponding announcement state;
4. repeat for Disciples and Trinity forms;
5. publish every raw result, the game version, seed method, minimum, maximum, median, mean, frequency table, and confidence intervals;
6. compare the current sample against the older `9 + exploding d4` and `27 + exploding d20` hypotheses without assuming that either survived into Dominions 6.

Purpose: determine the current distribution rather than merely rediscovering the official range.

## Test P2: Dominion spread

Create controlled maps with:

- fixed adjacency;
- no competing sources;
- exact temple counts;
- maximum dominion 1 through 10;
- neutral, friendly, and hostile target candles;
- land and sea boundaries.

Record at least several hundred check opportunities per condition.

Purpose: reproduce trigger chance, propagation, contest chance, and land-sea rerolls.

## Test P3: Preaching

Test H1-H5:

- with and without temple;
- neutral, friendly, and enemy dominion;
- ordinary and Inquisitor;
- at and above the predicted cap.

Purpose: verify fractional Holy handling, minimum chance, and cap rounding.

## Test P4: Scale convergence

For candle strengths 1-10 and differences 1-10:

1. lock out events and rituals where possible;
2. record monthly scale changes;
3. include cases above 100% predicted chance;
4. test whether two-step movement occurs;
5. repeat under extreme neighbouring scales.

## Test P5: Scale regression and rounding

Use controlled identical provinces to confirm version stability and settle:

- the published 2% Growth/Death income baseline;
- the published 2% Order/Turmoil resource baseline;
- Order/Turmoil event-frequency effect;
- rounding order;
- hostile-dominion application;
- Magic and Drain rounding.

## Test P6: Bless tags and values

For every blessing:

- inspect the design-screen prerequisite and cost;
- inspect unit abilities before blessing;
- bless in battle;
- remove or kill the Pretender;
- test innate and Incarnate states;
- test stacking;
- record damage, MR, resistance, sight, and “damaging hit” conditions.

Repeat unmodded, DE only, and DE plus Divinitus.

## Test P7: Automatic blessing

Cross:

- Pretender present or absent;
- Disciple present or absent;
- friendly, neutral, and enemy dominion;
- sacred troop and sacred commander;
- god alive, dead, and imprisoned.

Purpose: define exactly which units begin blessed under each condition.

## Test P8: Pretender death

For controlled path arrays:

- ordinary death;
- dominion-immortal death in friendly and enemy dominion;
- immortal death;
- Soul Slay;
- remote-plane death;
- repeated deaths.

Record:

- path lost or gained;
- dominion lost;
- reform time;
- afflictions;
- Incarnate blessing state;
- Call God requirement.

## Test P9: Call God

Regression-test the published model with:

- H1-H5 priests;
- mixed groups;
- Trinity member;
- ordinary Pretender, main Pretender in a Disciple game, and dead Disciple;
- nations with `#recallgod`;
- Elegists and combined Elegist/Recall God cases;
- pre-step-16 and post-step-16 priest deaths;
- friendly, besieged, and hostile capital states.

Purpose: upgrade the community-tested threshold, contribution distribution, routing, and placement rules to a direct current-version reproduction and detect later regressions.

## Test P10: Throne checks

Claim level-one, level-two, and level-three Thrones in controlled maps.

Record:

- checks per month;
- whether each check is guaranteed;
- target selection;
- interaction with maximum dominion;
- claimant death after step 8;
- unfortified conquest after step 8;
- siege without storming;
- successful storming and recapture;
- Ascension Point state immediately before the step-57 victory check;
- disciple sharing.

The claim-loss matrix is already resolved at the stated mixed evidence tier. These cases are retained as regression tests. The separate unresolved branch is the result of simultaneous winning totals, especially an exact tie in Ascension Points.

## Test P11: Special dominions

Each special dominion receives a nation-specific harness measuring:

- candle dependence;
- ally and Disciple treatment;
- underwater and remote-plane operation;
- unit generation;
- population and unrest change;
- terrain transformation;
- information hiding;
- enemy exploitation.

## Test P12: Combined-mod design regression

For every published combined design:

1. save the design file;
2. record displayed cost, paths, scales, dominion, and blessing;
3. update one mod at a time;
4. reload and compare;
5. flag any changed prerequisite, cost, availability, or form statistic.

# Part XV: Strategic Essays

## Essay I: Pretender Design as National Engineering

A Pretender is often described through an archetype: expander, rainbow, titan, scales chassis, bless chassis. These labels are useful only if they lead back to the nation. Engineering begins with a requirement, not a component catalogue.

The nation possesses a machine already. Its troops convert gold, resources, Recruitment Points, and Holy Points into armies. Its mages convert gold and commander-turns into research, gems into spells, and research into timing windows. Its dominion converts temples and priests into candles, then candles into scales, morale, survival, and national effects. The Pretender changes the machine’s inputs and supplies missing parts.

A good design has internal causality.

Productivity is bought because the planned queue exhausts resources. Dominion is bought because sacred throughput, religious conflict, or a special dominion uses it. A path is bought because it opens a blessing, booster, ritual, or divine spell that matters on a timetable. Awake status is bought because the god’s early commander-turns are worth more than the points surrendered.

Bad designs often contain individually powerful elements with no causal chain. Strong scales produce more gold, but the capital is Holy-limited. A deep blessing improves sacreds, but they are capital-only and too expensive to mass. A rainbow reaches many paths, but the nation cannot research or fund the promised rituals before the game is decided. An awake titan expands, but ordinary troops could have done the same while the 150-point difference funded the whole economy.

Engineering does not demand one correct answer. It demands that alternatives be compared against the same requirements.

One design may solve expansion with an awake monster and accept average scales. Another may solve it with an inexpensive blessing on national sacreds. A third may use ordinary troops, imprison the god, and turn the saved points into production and research. The correct comparison measures territory, losses, fort timing, research, vulnerability, and future path access—not aesthetic preference.

The final test is replaceability. Remove one purchase and ask what fails. If nothing important fails, the purchase is luxury. Replace the chassis and ask which jobs disappear. If none do, the form is overpriced. Move the first war ten turns earlier and ask whether the design remains coherent. If it collapses, its timing assumptions belong in the guide.

Pretender design becomes clearer when treated as national engineering because every point must enter a machine that can use it.

## Essay II: Dominion Is Territory by Other Means

Military maps invite a simple reading: coloured provinces are power. Dominion adds a second map beneath the first. It is a map of belief, morale, climate, legitimacy, and metaphysical survival.

The two maps spread differently. An army moves along a route and fights for a province. Dominion begins with sources, attempts checks, consolidates weak provinces, relays through strong ones, and grinds against enemy candles. A nation can win the military battle and inherit hostile scales. It can hold a fortress while its god weakens outside. It can raid a temple and reduce pressure across an entire religious front.

Dominion is a network because the value of a source depends on the state around it. A temple behind strong candles may relay checks to the frontier. The same temple behind a hostile wall may spend months reducing a single province. Five temples can be worth more than four plus one because the fifth raises maximum dominion, improving every check. In a team, that threshold moves with the number of players and changes who should build where.

Preaching is different. It is local, labour-intensive, and independent of the ordinary maximum. This makes priests tactical religious units. They can prepare a throne, hold a capital, weaken an immortal god’s safe ground, or reclaim a province faster than distant temples can reach it. Inquisitors are specialists in this conflict. Blood sacrifice turns a stored magical resource into additional checks and can overwhelm an ordinary temple economy when properly supplied.

Special dominions make the second map still more concrete. Candles can kill population, raise undead, create Manikins, scry enemies, hide ownership, spread disease, generate unrest, empower constructs, or enable sailing. In these nations, religious infrastructure is part of the military and economic production system.

Dominion death reveals the final importance of faith. A nation without friendly candles dies even if its armies remain undefeated. Religious survival is not flavour attached to conquest. It is a separate victory and defeat condition with its own network and logistics.

Territory supplies the state. Dominion determines whose reality governs it.

## Essay III: A Bless Is a Roster Contract

A blessing has no independent battlefield value. It has recipients, activation conditions, counters, and a price paid before the map exists.

The recipient is the beginning. A point of Attack applied to hundreds of inexpensive sacred attacks is not the same purchase as a point of Attack on a handful of already accurate giants. Regeneration on high-Hit-Point elites is not the same as regeneration on units killed by a single decisive hit. Leadership on sacred commanders can matter in every army while an offensive weapon blessing matters only when sacred troops reach melee and connect.

Throughput is the second condition. Capital-only sacreds, Holy Points, gold, resources, and Commander Points all restrict how much of the blessing enters the world. A huge design investment can end up enhancing a small fraction of the army. Conversely, a modest passive effect on recruit-everywhere sacred mages or commanders can alter a large part of the national economy.

Activation is the third condition. Ordinary sacreds need priests, scripts, time, and battlefield geometry. Incarnate effects need the god awake and alive. An imprisoned Incarnate design may exist on the Pretender screen while remaining absent from the first thirty turns. A god’s death can remove the centre of a sacred strategy without killing a single sacred.

Counterplay is the fourth condition. A weapon rider can face resistance. A control effect can face MR. Glamour defences can face special sight. Protection can face armour-negating damage. Regeneration can face burst damage, decay, poison, fatigue, or battlefield removal. A massed sacred army can be avoided, raided around, or starved of priests.

A blessing is a contract. The nation pays design points and accepts the opportunity cost. In return, the roster must field enough suitable sacreds, bless them in the battles that matter, and create matchups where the effects can change the result.

When those promises are explicit, bless design becomes testable. When they are not, “strong bless” is only an adjective.

## Essay IV: Awake Power and Deferred Power

Awakening is a trade across time. Awake status purchases commander-turns now by refusing future design points. Dormancy and imprisonment purchase permanent design advantages by surrendering early agency.

The apparent comparison—zero, 150, or 350 points—is incomplete. Time changes what each point can become.

An awake expander may take provinces before a dormant god exists. Those provinces generate income, resources, sites, recruitment locations, and strategic position. The expander may also free gold and commanders that ordinary expansion parties would have consumed. Early power can compound.

Deferred power compounds too. Stronger scales affect every held province. A better blessing affects every sacred recruited. Additional paths can unlock rituals and forging for the rest of the game. If the nation can expand and deter attack without the god, the point grant may exceed the value of early commander-turns.

The uncertainty of arrival matters. A dormant plan must survive the late end of the arrival range, not only the average. An imprisoned Incarnate blessing must be evaluated as two different armies: the army before awakening and the army after. A strategy that functions only if the god appears on the first legal turn has converted uncertainty into an unpriced risk.

The useful question is not “Is awake or imprisoned stronger?” It is:

> At what turn does each design overtake the other, and what must remain true for that crossover to occur?

If the game’s first decisive war happens before the crossover, deferred power may never be collected. If the awake god cannot produce territory, research, or deterrence worth its opportunity cost, immediate availability is being wasted.

Time is not another statistic on the design. It is the dimension in which every statistic is realised.

## Essay V: The Religious Logistics of War

Armies require supply, commanders, reinforcement routes, and retreat provinces. Sacred armies require a parallel chain: temples, priests, candles, and an active god where Incarnate effects matter.

The chain begins in recruitment. Holy Points determine how many sacreds leave the queue. Dominion and temple thresholds shape that capacity. Priests must then accompany the army or meet it before battle. Their map movement must match the force. Their scripting must bless the right squads before contact. Their survival must be protected against assassination, arrows, flyers, and battlefield spells.

Dominion determines the environment in which the force operates. Friendly candles provide morale and may automatically bless sacreds alongside the Pretender. They strengthen the god and Prophet. They carry selected scales and special national effects. Enemy candles reverse some of those advantages and may turn a dominion-immortal advance into a permanent death risk.

Temples are logistical nodes. A forward temple does more than increase a global religious score: it adds checks, supports preaching, permits blood sacrifice where eligible, contributes to maximum-dominion thresholds, and may accelerate sacred recruitment or special effects. Like a laboratory or fort, it has a position and a vulnerability.

Religious logistics can be attacked. Priests can be assassinated. Temples can be raided. Candle chains can be contested. A throne can be unclaimed by capture. A god can be killed to disable Incarnate effects. An army designed around automatic or battlefield blessing can be forced into a fight before its religious support arrives.

An expert sacred army is more than a roster with a blessing. It is a supported formation whose religious supply line has been planned as carefully as its food and reinforcements.

## Essay VI: The Death of a God

Dominions makes gods powerful by making their death national.

An ordinary commander’s death removes a body, equipment, leadership, and perhaps magic. A Pretender’s death can additionally remove an Incarnate blessing, path access, dominion strength, ritual timing, expansion capacity, and the nation’s central strategic threat. Priests must abandon other work to call the god back. The returned god may be weaker.

This creates a risk budget. A combat Pretender should not be asked merely whether it wins a battle. The correct question is whether the probability and consequence of failure are acceptable relative to the battle’s strategic value.

Immortality changes the budget but does not erase it. A dominion-immortal god needs friendly candles at death. An Immortal can still face soul destruction or remote-plane failure. Reform takes time. Equipment and operational tempo remain exposed. A supposedly safe attack can become unsafe when enemy preaching or temple checks reverse the province before combat.

Call God turns priest-months into recovery. The cost can be enormous. The same priests might bless armies, preach a threatened capital, sacrifice blood, or claim a throne. A nation with few priests may own a theoretically recoverable god and lack the practical capacity to recover it before the war ends.

Pretender risk is justified when it creates disproportionate value: a decisive throne, the destruction of an irreplaceable army, the relief of a capital, or a timing window no ordinary force can exploit. It is poorly justified when the god fights a battle that mundane troops could win or raids a province worth less than the risk imposed on the entire national plan.

A god is not preserved by refusing every battle. A god is preserved by spending divine risk only where divine power is necessary.

# Part XVI: Reference Checklists

## One-page Pretender worksheet

| Section | Decision |
| --- | --- |
| Nation and ruleset |  |
| Lobby assumptions |  |
| First military state |  |
| Expansion method |  |
| Chassis and role |  |
| Awakening |  |
| Initial and maximum dominion plan |  |
| Scale package |  |
| Paths and exact purposes |  |
| Bless package |  |
| Sacred recipients per month |  |
| Blessing access |  |
| First research breakpoints |  |
| First three god orders |  |
| Temple schedule |  |
| God-death and recall plan |  |
| Principal counters |  |
| Test results |  |

## Monthly dominion audit

- Current maximum dominion.
- Temples until next threshold.
- Friendly-candle core.
- Enemy candle fronts.
- Capitals or Thrones at religious risk.
- Preachers and Inquisitors assigned.
- Blood-sacrifice sites and slave budget.
- Special-dominion damage or benefit.
- Incarnate blessing active or inactive.
- Dominion-immortal safe operating area.

## Bless battle audit

- Sacred units began blessed?
- Which round did Blessing or Divine Blessing resolve?
- Which effects were innate?
- Which effects were Incarnate?
- Was the Pretender alive and present as required?
- Did damage riders require a damaging hit?
- Which effects faced MR?
- Which resistances or sight abilities countered the package?
- Did fatigue, morale, or formation fail first?
- Were the casualties economically replaceable?

## Publication checklist

- State base patch and manual revision.
- State mods and load order.
- Separate manual, current-data, and modded values.
- Name every current-value conflict.
- State awakening assumptions as ranges.
- State sacred throughput.
- State Incarnate dependence.
- State priest and blessing access.
- State god-death consequences.
- Link tests when an edge case decides the recommendation.

# Sources and Open Questions

## Principal sources

- Dominions 6 Manual, revision 2, especially Pretender design, Dominion, Divine Magic, Bless Effects, scale effects, Thrones, and Call God.
- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html).
- [Illwinter Dominions 6 changes](https://www.illwinter.com/dom6/changes.html).
- [Illwinter current release record](https://www.illwinter.com/).
- [Official 6.08 Steam announcement](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637648186096).
- [Official Dominions 6.36 announcement](https://steamcommunity.com/games/2511500/announcements/detail/693143486970465344).
- [Current Dominions 6 blessing reference](https://illwiki.com/dom5/dom6/bless).
- [Current Dominions 6 scales reference](https://illwiki.com/dom5/dom6/scales).
- [Current Dominions 6 Pretender reference](https://illwiki.com/dom5/dom6/pretender-god).
- [Current Dominions 6 Pretender-design reference](https://illwiki.com/dom5/dom6/pretenders), including the 16 June 2026 republication of the awakening model.
- [Loggy's miscellaneous reverse-engineering notes](https://illwiki.com/dom5/user/loggy/misc), used to trace the awakening formula's pre-Dominions 6 provenance.
- [Current Dominions 6 Elegist reference](https://illwiki.com/dom5/dom6/elegist).
- [Published Call God research notes](https://illwiki.com/dom5/user/loggy/callgod).
- [Current Dominions 6 Throne reference](https://illwiki.com/dom5/dom6/thrones).
- [Published same-turn Throne claim report](https://www.reddit.com/r/Dominions5/comments/pu0l7c/noob_questions_on_claiming_thrones/).
- [Legacy Pretender and awakening mechanics page](https://illwiki.com/dom5/pretenders), retained only as a historical test hypothesis where it identifies an older game baseline.
- Dominions 6 Modding Manual 6.34.
- Dominions 6 Inspector, 6.35 data commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.
- Supplied `DomEnhanced2_16.dm`.
- Supplied `Divinitus_1.15.3_DE.dm`.

## Open questions

Cross-source stacking, shape inheritance, mount-transfer lifetime, Order/Turmoil event frequency, economic rounding, awakening distributions, simultaneous-victory ties, and special-dominion inheritance remain assigned to their research registers or controlled tests. Same-turn Throne ownership and the practical Call God model are resolved at their stated mixed evidence tiers. Modded blessing costs and chassis definitions should be taken from Book IX rather than from older copies of this chapter.
