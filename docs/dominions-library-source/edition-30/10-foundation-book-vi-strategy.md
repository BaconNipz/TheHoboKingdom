# Foundation Book VI: Strategy and Campaign Conduct

## From systems to campaign

Dominions is won on the map, but the map is only the visible surface of the contest. Armies occupy provinces; research changes what those armies can survive; laboratories turn gems into reach; scouts turn uncertainty into decisions; forts turn territory into replacement capacity; diplomacy changes how many fronts must be defended; and Thrones determine when strength becomes victory.

> **Foundation rule:** Strategy is the conversion of limited resources into a position that can force, survive, or prevent the next decisive event.

A nation does not win by collecting the largest abstract total of gold, gems, research, or territory. It wins by making those resources matter before rivals can answer, then turning the advantage into enough claimed Ascension Points. Every recommendation in Book VI has a context and a deadline.

Book VI is where the earlier rules meet the map. It assumes the mechanical foundations instead of teaching their formulas again. A spy revealing income is a rule. Recruiting one before the first war is advice whose value depends on access, cost, geography, and the information already available.

## Edition note

The shared ruleset and evidence language remain in Book I. Books II-V own the detailed economy, religious, combat, and magic rules. Book VI brings them together for expansion, intelligence, logistics, diplomacy, defeat, and victory conversion. Book IX supplies exact modded changes whenever a campaign plan depends on DE or Divinitus.

## Current-version corrections and additions that matter

Dominions 6 introduced strategic systems and interface changes that make some older-series advice incomplete:

| Current feature or correction | Strategic consequence |
| --- | --- |
| Optional hidden maps require exploration | Map knowledge is acquired rather than assumed; scouts can reveal routes as well as armies |
| Maps may contain multiple planes | Adjacency, sanctuary, invasion routes, and throne access can cross a plane boundary |
| Formal diplomacy supports binding NAPs with humans and AI | Treaty terms may be enforced by the engine, but the game setting and agreed social doctrine still matter |
| Raid is movement followed by pillaging, without an automatic return | Pillager units now seize and damage the destination rather than performing an abstract round trip |
| Scrying inside dominion can detect glamoured units | Glamour conceals information but does not guarantee operational surprise |
| Thrones become visibly lit after being claimed | Claimed victory progress is easier to read from the map |
| Many globals depend on an origin province that must be held | Strategic enchantment defence includes territorial defence |
| Score graphs incorporate more sources accurately | Threat estimates using graphs are stronger than in early releases, though still incomplete |
| AI builds forts, recruits better national troops, and plans high-level rituals, globals, and dispels | Old descriptions of a purely passive or magically incapable AI are obsolete |
| Magic-phase movers can be included in moving-army setup | Teleporting and ordinary elements can be prepared as one operation |
| Cataclysm is harder to counter | Late games with Cataclysm enabled must treat the victory threshold as a moving clock |
| Large games host faster and allied site information was corrected in 6.34 | Operational coordination is more reliable than in affected older versions |

Object balance still changes through patches. A current nation plan must be rebuilt when its roster, spell access, Pretender options, or mod layer changes, even if the campaign principles remain valid.

## Using the campaign sections

Expansion, scouting, borders, research signals, war planning, sieges, Thrones, and the turn checklist form the main route. Raiding, remote warfare, deterrence, coalition politics, recovery, and after-action review become more useful once those basics are familiar. The single-player chapter explains what AI games teach well and where multiplayer creates a different strategic problem.

# Part I: Strategy as Conversion

## Position, force, and deadline

A strategic position has three parts:

1. **Assets:** provinces, forts, laboratories, temples, armies, mages, gems, research, Pretender, and diplomatic relationships.
2. **Access:** which assets can affect which places and at what time.
3. **Deadline:** the next event that changes the value of the position.

Deadlines include an enemy research breakpoint, a dormant Pretender awakening, a fort cracking, a treaty expiring, a global taking effect, a claim-capable priest reaching a Throne, or the arrival of Cataclysm. The same assets can be sufficient before a deadline and worthless after it.

This yields a practical model:

```text
strategic value
= usable assets
x probability of correct delivery
x value before the deadline
- exposure and opportunity cost
```

This is not an engine formula. It is a way to compare plans. A large army has little current value if it cannot cross the terrain in time. A research lead has little war value if the mages carrying it are trapped in a sieged capital. A cheap raider has high value if it pulls an expensive counter-mage away from the decisive front.

## The six conversions

Most campaigns turn on six conversions:

| Conversion | Example | Failure mode |
| --- | --- | --- |
| Economy into capacity | Gold builds forts and recruits mages | Infrastructure delays necessary defence |
| Capacity into knowledge | Mages spend turns researching | The nation researches effects it cannot field |
| Knowledge into force | Mages, gems, troops, and scripts form an army package | A spell list is mistaken for a deployable force |
| Force into position | Armies take routes, labs, forts, sites, and Thrones | Victories occur in strategically empty provinces |
| Position into constraint | Raids, forts, threats, and treaties narrow enemy choices | Gains are too diffuse to force a response |
| Constraint into victory | The nation cracks, storms, and claims enough Thrones | Dominance is enjoyed but never converted |

Strong play moves deliberately from one conversion to the next. Weak play often becomes trapped between them: rich but unable to recruit, researched but unable to cast, victorious but unable to siege, or dominant but unable to claim.

## Tempo and initiative

**Tempo** is the amount of useful change achieved before an opponent can respond. **Initiative** is the ability to present threats that determine where and how the opponent must spend the next turn.

Tempo is not speed alone. A fast raid that loses a unique commander may surrender more future tempo than it gains. A month spent combining armies may be correct if the merged force can remove a capital and every smaller force would bounce.

Initiative is strongest when threats are:

- **credible:** enough force or hidden capacity exists to execute them;
- **multiple:** the defender cannot cover every target;
- **asymmetric:** the attacker spends less than the defender must reserve;
- **timed:** the threats mature together;
- **convertible:** at least one successful branch leads to a fort, lab, army destruction, or Throne.

The objective is not perpetual aggression. It is the ability to decide which problem becomes urgent.

## The strategic horizons

| Horizon | Typical distance | Central question |
| --- | --- | --- |
| Turn | Current hosting cycle | Which orders can fail, collide, or become illegal? |
| Operation | Several turns | Which target can be isolated, reached, cracked, and exploited? |
| War | Research and reinforcement cycle | Which exchange rate and breakpoint can the enemy not sustain? |
| Game | Victory threshold | Which route produces enough claimed Ascension Points? |

Good decisions align all four. A tactically excellent battle can damage the operation by consuming gems needed for the storm. A successful operation can damage the war if it exposes two unforted borders. A winning war can lose the game if another nation claims the last required Throne.

## The cost of attention

Dominions has an unpriced resource: player attention. Every additional raider, scout network, forge route, blood-hunting transfer, communion, or diplomatic promise creates orders that must be checked. A system that is theoretically optimal but routinely misordered has a lower practical value than a robust system.

Attention costs grow sharply in war because each turn adds:

- battle reports and script diagnosis;
- enemy movement estimates;
- gem and item transfers;
- recruitment replacement;
- route and retreat checks;
- diplomacy;
- throne arithmetic.

Simple habits such as renaming commanders, marking armies, keeping standard scripts, using repeatable gem loads, and following a fixed turn audit are strategic tools. They lower the chance that a mature position dies to an omitted order.

# Part II: Expansion

## What expansion is for

Expansion is the first time a Pretender design and national roster are turned into territory. The result is more than a province count. Good expansion produces:

- gold and resource flow;
- room and population for forts;
- magic sites and independent recruits;
- defensible boundaries;
- routes toward or around Thrones;
- enough surviving troops and commanders to discourage an early war;
- an infrastructure schedule that does not stop recruitment.

A player can finish the first year with many poor, exposed provinces and a hollow army. Another can hold slightly fewer provinces but own two strong fort sites, a narrow border, and intact expansion parties. The second position may be stronger.

## Expansion testing

Expansion should be tested under the actual game assumptions:

| Variable | Why it must match |
| --- | --- |
| Nation and age | Starting army, roster, independent composition, and resources differ |
| Pretender and awakening | An awake expander changes routes, risk, and recruitment |
| Scales and dominion | Gold, resources, supplies, bless, and Pretender safety change |
| Independent strength | Required party size and acceptable targets change |
| Map or map type | Terrain, connectivity, caves, water, and start density change |
| Active mods and load order | Costs, units, blessings, spells, and Pretenders may differ |
| House rules | Expansion diplomacy, mercenaries, and early attack restrictions may differ |

A useful test protocol is:

1. Create the intended ruleset and game settings.
2. Record the Pretender design.
3. Play through turn 12, including realistic recruitment, Province Defence, site searching, and fort construction.
4. Record every fight, loss, province type, treasury level, fort start, and remaining army.
5. Repeat on several starts.
6. Change only one major element at a time.
7. Keep the reliable build, not the one with the luckiest maximum.

The community practice of testing to turn 12 is valuable because one in-game year includes route variation, attrition, winter or summer conditions, and the first infrastructure decision. A benchmark is meaningful only if its accounting includes what the real game will buy. Tests that omit PD, forts, researchers, or required temples create an imaginary expansion economy.

## The first expansion audit

Before the first attack:

- What troop or Pretender package is the expansion engine?
- Which independent types can it defeat cheaply?
- Which types can kill it through lances, high damage, mass missiles, magic, poison, fear, or surround penalties?
- Does it need a bless, prophet, priest, mage, screen, or specific formation?
- How many losses can be replaced without delaying the second party?
- What is the retreat route?
- Which adjacent province improves capital recruitment through resources?
- Which route reveals the most map or claims the most valuable boundary?

The first attack should normally be selected after scouting reports arrive. Independent armies do not change merely because the estimate changes; the report contains uncertainty. The correct response to uncertain numbers is margin, not false precision.

## Expansion party archetypes

| Archetype | Strength | Main risk |
| --- | --- | --- |
| Armoured line | Absorbs low-damage infantry and missiles | High-damage barbarians, lances, fatigue, slow killing |
| Defence or glamour line | Avoids many ordinary attacks | Surround penalties, high attack, area damage, magic weapons |
| Missile mass | Damages before contact and exploits low protection | Shields, armour, weather, ammunition, fast contact |
| Lance or impact force | Powerful first contact | Wasted charge, attrition after impact, missile exposure |
| Giant or elite squad | High individual durability and damage | Low numbers, surrounding, expensive casualties |
| Sacred party | Bless creates an efficient specialist package | Holy-point limits, priest dependency, wrong matchup |
| Awake monster | Independent commander with rapid early tempo | Irreplaceable loss, hostile dominion, fatigue, specialist independents |
| Awake Titan | Expansion plus later slots and strategic magic | Complex scripting, afflictions, insufficient early damage |
| Thug pair or small commander team | Mobile, low troop demand, scalable later | Gem or bless dependency, counter matchups |
| Mage-supported troops | Solves hard types and reduces attrition | Lost research, stray death, gem consumption, script failure |

These are roles, not strict categories. A sacred giant line may belong to three at once. The purpose is to identify why the party wins and which target will break it.

## Target selection

Target value has at least five dimensions:

1. **Win probability.**
2. **Expected permanent loss.**
3. **Economic value.**
4. **Positional value.**
5. **Information value.**

The weakest visible province is not automatically the best target. A resource-rich cap-ring forest can unlock a second party. A low-income mountain may secure a choke point or later fort. A province on the wrong side of the intended boundary may create a diplomatic dispute. A throne province may reveal valuable effects but contain mage support far beyond ordinary independents.

An expansion route should prefer:

- targets the party counters;
- cap-ring terrain that improves recruitment;
- rich farmlands and high population for economy and forts;
- strategic connectors and plane gates;
- provinces that cut off a safe interior;
- independent mages or special recruits;
- routes that can be reinforced rather than isolated.

## Minimum force and acceptable loss

The ideal party is not the smallest one that can win once. It is the smallest one that wins with enough reliability and survivors to keep tempo. A party that takes a province with 55% probability is not efficient merely because it is cheap.

Expansion losses have compounding cost:

- replacement gold and resources;
- commander turns spent collecting troops;
- delayed second and third parties;
- lost veteran experience;
- exposed routes;
- weaker deterrence at first contact.

Overbuilding also compounds. A single enormous party may win every fight but captures only one province per turn. Two parties with safe matchups normally create more map tempo, reveal more land, and deny more provinces.

Use three margins:

- **combat margin:** enough strength to survive report error and random battle outcomes;
- **attrition margin:** enough survivors to take the next scheduled target;
- **strategic margin:** enough reserve or recruitment that one bad fight does not collapse the opening.

## Routing and branch points

An expansion party should rarely be sent to the far edge without a return plan. Every route should mark:

- the next two intended targets;
- a branch if the preferred target is too dangerous;
- a rendezvous province for reinforcements;
- the future border;
- the nearest fort site;
- the path home or toward a threatened neighbour.

Interior provinces can be deliberately left for a later party if the outer route encloses them safely. This increases frontier speed without surrendering the eventual income. The risk is that an unscouted connector, cave, water route, or rival cuts into the pocket.

## First contact

First contact turns expansion into diplomacy. The first border message should settle practical facts before fear fills the gap:

- which provinces each side believes are natural claims;
- whether a disputed province contains a Throne, special site, or critical route;
- whether formal or social NAPs are in use;
- how countdowns are counted;
- whether scouts and stealth units are permitted;
- how accidental bumps will be handled.

The best border is not always equal by province count. A stable border that preserves a rich interior can be worth conceding one weak province. A narrow, fortifiable line is often stronger than a long geometrically “fair” boundary.

## When expansion ends

Independent expansion ends when profitable unclaimed targets disappear or when continuing exposes the nation to an unacceptable first-war position. The transition signs are:

- neighbouring expansion parties can collide;
- taking the next province creates a disputed salient;
- armies must combine to take Thrones or hard independents;
- forts and researchers now return more than another marginal army;
- opponents have reached military breakpoints;
- the nation must choose a first-war target or defensive posture.

The correct transition does not stop all growth. Thrones, underwater access, caves, remote provinces, and independent pockets may remain. It changes the dominant problem from beating known neutral defenders to acting under human opposition.

# Part III: Scouting, Intelligence, and Uncertainty

## Information is a resource

Information changes which orders are rational. It does not directly kill troops, but it prevents armies from attacking the wrong counter, reveals undefended infrastructure, identifies a throne rush, and allows gems to be carried only where necessary.

The value of information depends on:

- **accuracy:** how close the report is to reality;
- **coverage:** how much of the relevant map or force is observed;
- **timeliness:** whether it arrives before orders are due;
- **interpretation:** whether the player understands what the evidence implies;
- **denial:** whether the opponent can be kept from obtaining the same advantage.

Old information decays. A capital report from six turns ago still identifies fort and terrain, but not the current army, research package, gem reserve, or commander movement.

## Official information channels

| Observer or condition | Information provided |
| --- | --- |
| Scout in province | Owner, military estimate, fort construction, province history, current temperature and neighbour temperature |
| Priest in province | Scout information plus dominion strength and owner |
| Spy in province | Scout information plus income, supplies, known sites, unrest, PD, and more accurate military information |
| Friendly dominion | Owner, income, temperature, neighbour dominion |
| Scrying | Owner, highly accurate military information, income, supplies, sites, PD, history, temperature, dominion, forts, and unrest |
| Province ownership | Full provincial information, with map-name exploration distance depending on age |
| Adjacent ownership | Neighbour owner, temperature, and unreliable military information |
| Spy in an enemy capital | Access to enemy score-graph data even when score graphs are disabled |

These channels overlap but are not interchangeable. A scout can see construction; a spy can estimate state capacity; scrying can penetrate heavily patrolled areas without risking a physical scout. Dominion vision is broad but does not reveal every military fact.

## The intelligence cycle

Use a five-step cycle:

1. **Question:** what decision must be made?
2. **Collection:** which scout, spy, scry, battle probe, graph, or diplomatic inquiry can answer it?
3. **Assessment:** which facts are observed, inferred, stale, or possibly deceptive?
4. **Action:** what order changes because of the result?
5. **Review:** after hosting, which assumption was correct and which source failed?

“Scout the enemy” is too broad. Better questions include:

- Can the border fort be cracked in one turn?
- Which province contains the enemy’s research mass?
- Does the army have poison resistance, magic weapons, or battlefield mobility?
- Which commander is likely carrying gems?
- How many Ascension Points can the nation claim within three turns?
- Which route is outside ordinary reinforcement range?

Collection without a decision produces clutter.

## Reading partial evidence

No single clue proves a full plan. Combine indicators:

| Indicator | Possible meaning | Alternative explanation |
| --- | --- | --- |
| Research graph rises sharply | Research infrastructure matured | Site, event, Pretender, or graph uncertainty |
| Gem income appears high | Wide site-search coverage or rich territory | Throne income, globals, events, or hidden alchemy |
| Army disappears from border | Withdrawal or magic-movement staging | Glamour, stealth, transfer, or report failure |
| Construction mages stop researching | Forge cycle or army deployment | Rituals, site searching, illness, lab loss |
| H3 unit moves toward a front | Throne claim preparation | Bless support, preaching, or ordinary movement |
| Large cheap-unit recruitment | Siege preparation or mass screen | Patrol, freespawn organisation, or replacement |
| NAPs requested on several borders | Consolidation for war elsewhere | Genuine insecurity or throne preparation |

An estimate should carry a confidence statement: observed, likely, possible, or unknown. This prevents one attractive story from becoming the only story.

## Scouting density

A useful network has layers:

- **border screen:** current armies, construction, and route changes;
- **operational depth:** forts, labs, reinforcement roads, and reserve armies;
- **strategic nodes:** capitals, Thrones, globals' origin provinces, blood centres, major laboratories;
- **rear warning:** stealth raiders, plane gates, underwater exits, and indirect routes.

One scout on each border province is not a network. Scouts should leapfrog or overlap so the loss of one does not blind an entire front. Spare scouts can travel with armies to loot gear, hold transferred gems, or preserve observation after a province changes hands.

## Patrol and concealment

Official detection compares:

```text
Patrol Strength + 2d25 open-ended
versus
Stealth Strength + 2d25 open-ended
```

Stealth strength is based on the commander and is reduced by troops in the party. Patrol strength combines unit contributions, is reduced by unrest, and gains from PD at 15 or more. Flying, map movement, Precision, Patrol Bonus, commander status, Mindless, and Undisciplined affect individual patrol contribution.

The complete manual arithmetic is:

```text
Stealth Strength
= leader Stealth
- 1 per stealth troop with Stealth below 50
- 0.5 per stealth troop with Stealth 50 or more

individual Patrol Strength
= (Precision + Map Move) / 20 + Patrol Bonus
use Map Move 30 if the unit flies

province Patrol Strength
= sum of individual contributions
- min(Unrest, 100) / 2
+ max(Province Defence - 14, 0)
```

Commander contributions are doubled. The manual halves the contribution of Mindless and Undisciplined units; this official wording controls where community pages describe a different Undisciplined adjustment. The displayed patrol number may be rounded, so exact work should preserve the underlying fractions.

Let `D = Patrol Strength - Stealth Strength`. Enumerating both open-ended 2d25 rolls gives the following chance of detection:

| D below stealth | Chance | D above stealth | Chance |
| ---: | ---: | ---: | ---: |
| -60 | 0.1% | +60 | 99.9% |
| -55 | 0.2% | +55 | 99.8% |
| -50 | 0.4% | +50 | 99.6% |
| -45 | 0.7% | +45 | 99.2% |
| -40 | 1.2% | +40 | 98.7% |
| -35 | 2.0% | +35 | 97.7% |
| -30 | 3.6% | +30 | 96.0% |
| -25 | 6.3% | +25 | 93.0% |
| -20 | 10.6% | +20 | 88.3% |
| -15 | 17.1% | +15 | 81.3% |
| -10 | 25.9% | +10 | 72.1% |
| -5 | 36.7% | +5 | 61.0% |
| 0 | 48.8% | 0 | 48.8% |

Equal strengths do not give 50% because detection requires the patrol total to be greater; a tied opposed total leaves the stealth party hidden. These figures are **official plus derived**: the formula is the manual's, and the table is a direct enumeration rather than a fitted sample.

Consequences:

- detection is probabilistic, not guaranteed;
- repeated exposure raises cumulative risk;
- adding troops makes many stealth parties easier to detect;
- high unrest weakens patrols;
- PD 15+ changes a province from a token garrison into part of an intelligence screen;
- a discovered stealth force fights the outside defenders, while ordinary fort defenders not patrolling remain inside.

Movement and patrol timing also matters. **Move and Patrol** lets an arriving army fight outside a friendly fort, but it does not have time to search for stealth units during that same turn. The order becomes ordinary Patrol on the following turn.

## Information denial and deception

Denial measures include:

- killing or patrolling out scouts;
- avoiding unnecessary army concentration near observed borders;
- moving gems and items at the last practical moment;
- hiding capable commanders among ordinary researchers;
- keeping several plausible research branches;
- protecting capital and throne interiors from spies;
- using domes, stealth, glamour, or magic movement where appropriate;
- displaying false or incomplete threats.

Deception should create a plausible wrong decision. A visible army near an irrelevant Throne matters only if the enemy must reserve a force against it. A false weak border is useful only if the actual counter can arrive. Deception that requires the opponent to act irrationally is hope.

## Battle probes and pings

A probe can reveal:

- troop and commander identities;
- positions, formations, and orders;
- bless effects;
- scripted spells;
- carried gems through observed casting;
- throne independent mages and their spell repertoire;
- fort or field context.

The cost includes the probing commander, information given to the opponent, possible treaty implications, and the chance that the probe changes the target before the real attack. A retreat script does not guarantee survival when routes are hostile, a commander is trapped, or combat reaches it too quickly.

## Score graphs

Graphs are strategic indicators, not inventories. They can show trends in provinces, forts, income, research, army size, dominion, or resources according to game settings. Current versions incorporate more event-derived changes accurately, and a spy in an enemy capital can expose that enemy's graph information even if ordinary graphs are disabled.

Graphs should answer comparative questions:

- Who is compounding fastest?
- Who suffered a sudden army or territory loss?
- Whose research curve implies a breakpoint?
- Which apparent victim remains economically dangerous?
- Which leader can reach a throne threshold?

Graphs cannot show scripts, exact counters, hidden gem stock, diplomatic obligations, or the quality of units behind an army-size number.

Since version 6.35, victory reveals all score graphs and the hidden map to the players who remain until the game ends. Elimination still reveals neither, so a defeated player removed before the final result does not receive the same post-game intelligence. This is a review and learning tool, not information available for the decisions that produced the victory.

# Part IV: Map Structure, Borders, and Infrastructure

## Strategic geography

Every province has at least four geographic meanings:

- **economic:** income, population, resources, supplies, and sites;
- **network:** which provinces and planes it connects;
- **military:** terrain, movement cost, fort and battlefield context;
- **political:** border, Throne, buffer, treaty claim, or coalition route.

A low-income connector may be more valuable than a rich dead end. A cave entrance, water crossing, or plane gate can create an invasion route that ordinary border counting misses.

## Interior lines and exterior pressure

A nation has **interior lines** when its forces can move between threatened fronts faster than enemies can coordinate around the outside. Forts, roads, labs, central terrain, sailing, flight, and magic movement strengthen interior lines. Long tendrils, mountain or swamp barriers, and isolated underwater pockets weaken them.

Interior lines permit one reserve to answer several threats, but simultaneous hosting limits reaction. A reserve must be placed where its legal next-turn destinations are known before the enemy commits. “It can respond eventually” is not the same as “it can intercept next turn.”

Exterior pressure becomes decisive when several enemies attack different nodes at once. Diplomacy is part of geography: a neutral border can shorten the defended perimeter more effectively than any fort.

## Border shapes

| Shape | Advantage | Risk |
| --- | --- | --- |
| Narrow choke | Easy to fortify and scout | One lost node may open the interior |
| Broad line | Many routes for offence | High scouting and reserve demand |
| Salient | Threatens several enemy provinces | Can be cut off from reinforcement |
| Pocket | Safe later expansion and recruitment | Hidden routes or rivals may steal it |
| Corridor | Connects separated holdings | Vulnerable to a single raid or fort |
| Island or underwater enclave | Difficult for some rivals to reach | Limited exits and specialised counters |
| Plane gate network | Strategic mobility and surprise | Gate provinces become decisive nodes |

The strongest border is the one the nation can actually observe, reinforce, and politically maintain.

## Fort placement

Fort decisions should be evaluated across five roles:

1. **Recruitment:** population, resources, terrain recruits, and national restrictions.
2. **Research:** repeatable mage production and safe laboratories.
3. **Control:** sealing routes and forcing enemies into sieges.
4. **Logistics:** resupply, gem pooling, forging, ritual origins, and army assembly.
5. **Victory:** protecting Thrones and claim-capable commanders.

An early fort that produces the key mage may be worth more than a richer province. A border fort with no recruitable value may still impose a siege clock. A fort adjacent to a resource-hungry capital can reduce the capital's resource draw and should be tested before construction.

## Laboratories as strategic nodes

Labs do more than recruit mages:

- collect site income into the national treasury;
- permit research, forging, rituals, and empowerment;
- pool and transfer gems;
- support magic movement and remote operations;
- allow rapid equipment changes;
- become targets for raiders and teleporters.

A forward lab increases force projection but also exposes stored gems and mages. A laboratory network should include redundancy. If one captured lab disconnects the whole front from gem supply and ritual access, the network has a single point of failure.

## Temples and religious infrastructure

Temples:

- generate temple checks;
- support sacred and priest recruitment where national rules allow;
- raise maximum dominion according to the temple rule;
- enable Blood Sacrifice where available;
- protect dominion and help make Pretenders safer;
- turn Throne and border provinces into religious anchors.

Temple value rises near enemy dominion, special dominions, Thrones, and awakening or immortality operations. A temple is also visible intent. Building one in a disputed province can be read as territorial commitment.

## Province Defence as delay and information

PD should be bought for a purpose:

- defeating scout captures or tiny raiders;
- adding patrol strength at 15+;
- forcing larger raids and revealing their composition;
- joining an outside field battle;
- buying time for a counter-raider;
- exploiting unusually strong national PD;
- maintaining a low-cost tripwire.

PD is not a substitute for a mobile defence because the buyer cannot move it, preserve it through retreat, or customise it like a field army. Excessive uniform PD converts liquid gold into local strength that an enemy can bypass or counter once.

## Map annotation

A serious strategic map should mark:

- every known Throne and Ascension Point value;
- claimed and unclaimed status;
- forts under construction and their completion turns;
- laboratories, temples, and major sites;
- routes by movement class;
- water, river, mountain-pass, cave, and plane restrictions;
- likely enemy research and army positions;
- treaty borders and expiry dates;
- rally points, gem depots, and retreat routes;
- provinces whose loss breaks a corridor or global origin.

The map should show commitments as well as ownership.

# Part V: Research as a Strategic Response Tree

## From queue to campaign plan

Book V establishes the mechanics of research. Strategy asks when each breakpoint must enter the field. A research plan should contain:

- a **main line** that creates the nation's preferred army package;
- an **expansion line** if early magic materially changes neutral conquest;
- a **defensive branch** for the most likely early invader;
- a **mobility or raiding branch**;
- a **forging and access branch**;
- a **late-game transition**;
- an explicit rule for when to pivot.

A fixed queue ignores evidence. Constantly changing schools wastes accumulated progress and never reaches a threshold. The solution is a response tree with preselected branch points.

## Breakpoint records

For each important level, record:

| Field | Question |
| --- | --- |
| Effect | What new battle, ritual, item, or summon becomes possible? |
| Caster | Which repeatable or unique commander delivers it? |
| Resources | Which gems, slaves, items, communion bodies, or labs are required? |
| Scale | Can one army use it, or every army? |
| Deadline | On which turn or before which enemy event must it arrive? |
| Counter | What obvious answer reduces its value? |
| Pivot | Which adjacent research provides the next answer? |

The result is useful operational knowledge, not a list of admired spells.

## Research signals

Research is partly observable through graphs, deployed spells, forged gear, summoned units, and mage movement. A rapid rush can surprise once; repeated use reveals the level. Rivals can then infer adjacent capabilities.

Information denial methods include:

- delaying public use until the decisive battle;
- researching a cheap supporting branch after the main threshold;
- fielding a lower-level package that conceals the real peak;
- avoiding recognisable booster staging at exposed labs;
- maintaining several mages capable of different path packages.

The cost of secrecy must be real. Refusing to use a completed answer and losing territory to preserve surprise is normally poor conversion.

## Timing attacks as temporary advantage

A timing attack begins when relative power is temporarily highest. Common windows include:

- an awake expander surviving expansion while neighbours' imprisoned designs remain absent;
- a dormant Pretender awakening;
- a mass bless reaching sustainable sacred recruitment;
- a key battlefield enchantment or resistance spell;
- the first reliable communion;
- a Construction level that produces thugs or path boosters;
- a summon mass reaching operational scale;
- a mobility ritual opening unexpected targets;
- a hostile global changing the world's exchange rates;
- an opponent exhausting gems or elite recruitment in another war.

The attack needs preparation before the breakpoint:

- troops and commanders recruited;
- gems moved;
- items forged;
- scouts positioned;
- treaty countdown started;
- routes cleared;
- siege strength assembled.

Research finishing is the last dependency, not the first planning step.

## Portfolio depth

A nation with one exceptional package can force opponents to buy one exceptional counter. Portfolio depth adds a second axis:

- physical protection plus elemental resistance;
- battlefield army plus mobile raiders;
- troops plus MR-negates control;
- field strength plus remote attacks;
- glamour or stealth plus conventional pressure;
- army wipes plus fort-cracking capacity.

The purpose is not variety for its own sake. Each branch should punish the answer to another branch. If all packages fail to the same resistance, mobility, or commander kill, the portfolio is visually diverse but strategically narrow.

## Research under invasion

When invaded, divide research into:

- **survival threshold:** the cheapest completed answer that prevents immediate collapse;
- **stabilisation threshold:** the package that can win or deter field battles;
- **reversal threshold:** mobility, summons, or scale that turns defence into counteroffence.

Do not abandon a nearly complete decisive level for a weaker emergency spell without calculating completion time. Do not continue a grand late-game rush while the laboratories generating it are about to fall. The correct pivot is measured in turns, legal casters, and delivery—not anxiety.

# Part VI: Movement, Logistics, and Force Projection

## The official movement model

Army movement is limited by the slowest unit. Only commanders move independently; troops require leadership. Ground movement is calculated in half-steps: leaving the origin and entering the destination each have a terrain cost.

| Terrain | Ground half-step cost |
| --- | ---: |
| Plains | 3 |
| Forest | 5 |
| Waste | 5 |
| Highlands | 6 |
| Swamp | 7 |
| Sea | 5 |
| Cave | 4 |
| Cave Forest | 6 |
| Crystal Cave | 6 |
| Drip Cave | 7 |

Modifiers include:

- entering or leaving a province with enemy non-stealthy forces: +4;
- enemy stealthy forces: +3;
- snow: +1;
- road: -2, with a minimum cost of 2;
- matching survival ability: -2 for the relevant terrain.

Forest Survival also helps in Cave Forest, Mountain Survival in Crystal Cave, and Swamp Survival in Drip Cave. Flying normally costs 3 per half-step, 5 in caves, and +1 for enemy presence.

Common Map Move parameters provide a scale:

| Example | Map Move |
| --- | ---: |
| Heavy infantry | 8 |
| Light infantry | 14 |
| Light cavalry | 20 |
| Unicorn | 26 |
| Slow flier | 14 |
| Ordinary flier | 20 |
| Fast flier | 26 |

Commanders normally receive +2 to the general parameter. Object values and special abilities still control the actual unit.

## Barriers and army composition

Rivers require Cold +1 on both sides unless the army can fly, float, swim, or otherwise cross amphibiously. Mountain passes require Heat +1 on both sides unless the army flies, floats, or has Mountain Survival.

For special movement, every troop in the relevant army normally needs the required ability. Sailing and granted water breathing have their own exceptions. One slow, non-surviving, or non-amphibious squad can invalidate the intended route for the whole commander.

Version 6.36 establishes three current exceptions or extensions worth recording in route plans:

- a swimming mount is sufficient for its mounted unit to cross a river;
- Perpetual Storm increases movement cost in caves and underwater provinces as well as the previously affected environments;
- Gift of Water Breathing can protect against Lost Land.

Each statement is narrow. A suitable mount does not grant swimming to unrelated troops, and protection from one underwater disaster does not prove general underwater legality.

Every movement order should be checked against **the actual slowest and least capable component**, not the commander icon or the majority of the force.

## Friendly, hostile, and intercepting movement

Friendly movement resolves before hostile movement. In contested situations:

- more than two sides may fight sequential battles in a determined entry order;
- allied defenders fight in sequence, with defender order random;
- hostile armies attempting to swap provinces may meet in either province or miss and exchange positions;
- relative army size and terrain influence interception;
- entering a friendly fortified province normally places the army inside the fort;
- **Move and Patrol** is required to arrive and fight outside.

An arrow remaining on the map does not prove that a movement order is still legal. If conditions change before hosting—such as a river, pass, leadership, or destination issue—the unit may remain in place.

### Published collision algorithm: test hypothesis

A current community movement page publishes a more detailed reverse-engineered procedure for a directly adjacent one-step swap:

1. calculate a chassis value for the moving commanders and squads on each side;
2. compare each side's value with a separate random result from 0 to 349; if both values fall below their rolls, the armies pass and exchange provinces;
3. otherwise, each side rolls an open-ended die with its chassis value as the die size and adds one tenth of that chassis value;
4. the lower result is stopped, so the battle occurs in that side's starting province; a reported tie rule favours the side from the higher-numbered origin province.

The same page says this collision check applies to adjacent single-step swaps, while multi-province movement can pass through. It also opens by warning that the movement article needs more accurate information and publishes no 6.36 save set. Edition 27 therefore records the procedure as a source-traced hypothesis for S4, not as the rule players should assume without qualification.

## Operational reach

Operational reach is the set of provinces that a force can influence within a deadline. It includes:

- ordinary legal movement;
- sailing, flight, stealth, amphibious movement, and plane access;
- magic-phase movement;
- reinforcement and gem routes;
- the ability to survive after arrival;
- the ability to retreat.

A province “in range” of a teleporting thug may still be strategically unsafe if it has no laboratory for escape, no friendly retreat route, or a counter-mage can arrive in the same phase. Reach must include extraction.

## The logistics chain

Every serious army consumes:

- troops and replacements;
- commanders and appropriate leadership;
- food and supplies;
- gems and blood slaves;
- forged items;
- research-capable mage turns;
- scouts and reports;
- retreat routes;
- siege time.

A logistics chain can be represented as:

```text
recruitment fort
-> rally and command
-> route and supply
-> forward lab or gem mule
-> battle package
-> replacement and retreat
```

The chain is only as strong as its most exposed node. A frontier army with no replacement commander can become immobile after one assassination. A communion with no additional slaves may win once and disappear. A giant force without supplies can accumulate fatigue and disease before the decisive battle.

## Gem logistics

Gems are national stock in laboratories but physical carried resources in battle. A campaign needs:

- a load standard for each mage role;
- reserve gems for multiple battles;
- mules or a forward lab for reloads;
- a method to prevent optional gem use from draining the storm budget;
- decoys and bodyguards against assassinations;
- an evacuation plan if the lab is threatened.

Late-game throne operations may require several battles in one hosting cycle: magic-phase attacks, move-phase relief or interception, and a storm. The same script and carried stock may have to survive all of them.

## Supply and attrition

Supply is a campaign constraint, not a seasonal footnote. It affects:

- the size and route of living armies;
- how long a siege force can remain concentrated;
- the safety of capital or cave interiors;
- the usefulness of supply items and Nature magic;
- whether an opponent can force disease without winning a battle.

Book II contains the exact supply and starvation rules. At campaign level, the important point is that besieged storage falls as the siege continues and repeated starvation can lead to disease. A defender may gain time while quietly losing irreplaceable mages.

## Reserves

A reserve is not an army without orders. It is a force positioned to alter several likely enemy branches.

Good reserves:

- sit on a lab or movement hub;
- have compatible movement;
- carry counters rather than generic excess;
- can protect a Throne, fort, or retreat route;
- are hidden or ambiguous when possible;
- remain cheap enough that holding them back does not lose the main front.

The reserve's deterrent value depends on what the opponent believes it can reach. Scouting and information denial can change the value of the same force.

# Part VII: Raiding and Counter-Raiding

## What a raid is

Strategically, a raid is a limited force sent to take or threaten assets without joining the main battle. Its purpose may be:

- provincial income denial;
- capture of sites, labs, and temples;
- interruption of recruitment or gem collection;
- destruction of PD and patrollers;
- cutting retreat or reinforcement routes;
- forcing expensive defenders away from the main front;
- creating unrest or population loss;
- revealing counter capabilities;
- surrounding a fort;
- changing throne access.

The ordinary **Raid** order is a specific mechanic, not a synonym for every small attack. Officially, only a commander with Pillager can issue it, the army must have Map Move 20 or more, and only Pillager units contribute to the pillage at half strength. The force moves to the province, wins any battle, and then pillages. It does not automatically return.

## Pillaging

Pillaging:

- kills population;
- raises unrest;
- reduces supplies;
- yields temporary gold and food.

Fast and large units pillage better, and some unit types such as barbarians or fear-causing forces are particularly effective. The resulting supplies last one month. Pillaging converts long-term provincial value into short-term campaign resources and damage.

This is often rational in enemy land and often self-defeating in territory intended for immediate annexation. A player should distinguish:

- **seizure:** capture intact value;
- **denial:** prevent the enemy using it;
- **destruction:** reduce future value for everyone;
- **foraging:** support a force for one more month.

## Exact-output hypotheses

Older code-analysis notes proposed a base unit pillage strength of `floor((Strength + Combat Speed + 10 x Fear) / 2)`, with a special Combat Speed value for flyers, followed by population, fort, exploding-die, unrest, casualty, food, and gold checks. The same notes gave a separate Raid catch sequence and reduced contribution rules.

Those formulas are precise enough to reproduce but not safe enough to publish as 6.36 law. The notes predate later Raid interface fixes, do not include a current raw outcome set, and Illwinter's current public description deliberately states only that Raid is move plus pillage with no return. Edition 27 keeps the proposed unit-strength expression and its downstream branches as S6 predicates. Until S6 is run, compare raiders by legal order access, mobility, Pillager bodies, expected battle strength, and the official half-strength contribution rather than a promised gold figure.

## Raider classes

| Raider | Strength | Typical answer |
| --- | --- | --- |
| Cheap commander with small troop squad | Low cost, repeatable | Modest PD, local troops, fast commander |
| Stealth army | Hidden approach and broad threat | Patrol network, scrying, chokepoints |
| Light thug | Defeats PD and weak local troops | Counter-thug, mage, specialised PD |
| Heavy thug | Beats larger troop-only responses | Magic weapons, fatigue, control, tailored damage |
| Supercombatant | Threatens armies and critical nodes | Layered specialist response, army magic, denial |
| Flying or sailing force | Crosses ordinary front geometry | Coverage of landing nodes, mobile reserve |
| Magic-phase attacker | Arrives before ordinary movement | Dome, trap, counter-teleporter, protected nodes |
| Assassin or seducer network | Removes command and specialist mages | Bodyguards, decoys, patrols, redundant command |
| Remote army or spell | Projects force without exposing a route | Domes, dispersed assets, retaliation |

Raider value depends on the defender's replacement cost. A ten-gem thug that forces a twenty-gem counter to remain idle can be valuable even before taking a province. The same thug is poor if it walks into a cheap armour-piercing weapon and transfers its equipment to the enemy.

## Raider efficiency

Evaluate a raider by:

```text
value denied
+ response cost imposed
+ positional gain
+ information gained
- expected permanent loss
- attention and opportunity cost
```

The captured province's income is only one term. Cutting a laboratory may strand ritual mages. Taking a corridor can kill retreats. Threatening three provinces can make the enemy divide an army. Conversely, repeatedly trading expensive raiders for low-income provinces can lose the gem war while the map colour appears active.

## Raider design

A raider needs:

- a target class;
- sufficient movement;
- enough offence to end the fight;
- enough defence to survive that target;
- fatigue stability;
- morale or mindlessness appropriate to the task;
- a retreat or escape plan;
- a price ceiling.

Thugs should layer different defences rather than maximise one statistic. Protection alone eventually fails to armour-defeating results, high damage, fatigue, or armour-piercing and armour-negating attacks. Defence alone fails under repeated attacks and surrounding. Regeneration alone fails to burst damage or conditions that prevent recovery.

Minimalism is central. Every additional item must change a relevant matchup or survival probability. Decorative gear increases the reward for the counter-thug.

## Creating a raiding front

A raiding front works when several threats mature together:

1. Scouts identify low-PD, high-value, and weakly connected provinces.
2. Raiders enter from different routes.
3. The main army threatens a fort or decisive battle.
4. Remote or magic-phase attacks threaten the reserve.
5. Captured provinces cut retreat and reinforcement paths.
6. Raiders withdraw, regroup, or join a siege before tailored answers arrive.

One raider is a puzzle. Several raiders plus a main army are a resource-allocation crisis.

## Counter-raiding as a system

Counter-raiding should not chase every loss with the main army. Build layers:

| Layer | Function |
| --- | --- |
| Scouts and scrying | Identify raider type, movement, and equipment |
| PD tripwires | Defeat the smallest raids and reveal larger ones |
| Patrol nodes | Restrict stealth routes and protect critical labs |
| Local recruits | Reclaim undefended provinces cheaply |
| Mobile counters | Catch or threaten expensive raiders |
| Magic-phase response | Intercept forces that ordinary movement cannot catch |
| Fort network | Preserve recruitment and force raiders to stop |
| Strategic reserve | Prevent several raids from becoming a capital or Throne attack |

The defender should calculate which provinces are worth defending. A poor border province may be allowed to change hands while the counter waits at the lab, Throne, or route the raider actually needs.

## Counter-thugs

A counter-thug is usually cheaper and more specialised than the target. It may need only:

- a weapon that bypasses the target's principal defence;
- sufficient attack or precision to connect;
- resistance to the target's damage;
- enough speed or magic movement to catch it;
- a scout or spare commander to loot gear.

Specialisation creates efficiency but reduces general usefulness. Do not send the counter at a different chassis merely because both are called thugs.

## Raid recovery

After losing provinces:

1. Preserve the force that can defeat the raider.
2. Identify its legal next destinations.
3. Protect the high-value nodes among them.
4. Retake empty provinces with cheap commanders.
5. Rebuild a continuous retreat and supply route.
6. Do not overinvest in PD everywhere after one frightening loss.
7. Use the revealed gear and script to construct the cheapest repeatable answer.

The aim is to reduce future response cost. A defender who spends a major mage and ten gems on every raid may technically win each battle and still lose the campaign.

# Part VIII: War Planning, Timing, and Decision

## Reasons to go to war

War is justified when it improves the route to victory more than the alternatives. Common reasons include:

- an opponent can be defeated before its breakpoint;
- a critical Throne, fort, gate, or path recruit is accessible;
- a neighbour is committed elsewhere;
- a hostile position will become unanswerable if left alone;
- a treaty network creates a temporary safe front;
- defensive war is already unavoidable and initiative can be seized;
- the war prevents an imminent victory.

“The neighbour is weak” is incomplete. The relevant questions are what can be taken, how long it takes, who benefits, and what other nations can do during the commitment.

## War aims

Define the minimum successful outcome:

- destroy a specific army;
- seize a border fort or capital;
- capture or neutralise a Throne;
- remove a global origin;
- secure a corridor or plane gate;
- force a treaty or transfer;
- eliminate the nation;
- delay it while another operation succeeds.

Unlimited conquest causes strategic drift. A war that has achieved its aim may be ended or frozen before the winner's armies become trapped in low-value territory.

## The invasion ledger

Before ending a NAP or submitting attack orders, record:

| Requirement | Minimum answer |
| --- | --- |
| Enemy strength | Main army, mobile reserve, Pretender, known thugs, magic phase |
| Friendly package | Troops, mages, scripts, gems, counters, leadership |
| Target sequence | Border battle, fort, lab, Throne, capital |
| Siege | Expected wall strength, reduction per turn, defence and relief |
| Logistics | Route, supplies, reload, reinforcements, replacement commanders |
| Diplomacy | Legal attack date, other borders, coalition reaction |
| Research | Current package and next breakpoint |
| Failure branch | Retreat route, fallback fort, diplomatic exit |
| Victory conversion | Claim unit, AP count, post-capture defence |

If the plan ends at “win the battle,” it is tactical preparation rather than a campaign.

## Back-planning the attack date

The attack date should be derived backwards:

```text
desired decisive battle
<- arrival turn
<- treaty expiry
<- final recruitment and rally
<- item and gem preparation
<- research completion
<- scouting confirmation
```

Because hosting is simultaneous, a force one province away may arrive into a different position than expected. Every route needs a branch for enemy movement, interception, or a changed barrier.

## Concentration and dispersion

Concentration wins difficult battles and cracks forts. Dispersion captures provinces and imposes attention. The campaign should alternate:

1. disperse for expansion or raiding;
2. concentrate for the decisive army or siege;
3. disperse after victory to cut retreats and take infrastructure;
4. reconcentrate before the opponent's new package arrives.

Permanent doomstacks waste map tempo. Permanent dispersion invites defeat in detail.

## Forcing battles

An opponent can often decline an unfavourable field battle. Force commitment by threatening:

- a capital;
- a high-output mage fort;
- a Throne;
- a laboratory with rare commanders;
- a global origin;
- a corridor whose loss traps an army;
- multiple forts whose siege clocks mature together.

The best target is sometimes the one the enemy must defend, not the one with the most immediate income.

## Gem burning

Battle magic consumes carried resources. A weak or sacrificial force may trigger expensive scripts before the decisive battle. This can be achieved through:

- magic-phase attacks before move-phase combat;
- sequential allied or multi-party battles;
- remote attacks;
- probes against an army expected to storm;
- assassinations that cause individual gem use.

Gem burning is not free. The probe may die, reveal information, or fail to trigger the intended spells. Conservative gem-use settings and spell AI affect results. The attacker should compare the expected hostile gems consumed with the permanent cost of the probe.

## Deterrence

Deterrence depends on credible punishment. It can come from:

- a visible army;
- hidden teleporters or thugs;
- a known battlefield wipe;
- a treaty partner;
- a fort that imposes delay;
- the ability to raid an attacker's undefended rear;
- a Pretender whose commitment changes the battle;
- the diplomatic cost of creating a runaway elsewhere.

Purely hidden capacity may not deter because the opponent does not know it exists. Selective disclosure—one demonstration, a truthful warning, or visible staging—can preserve peace more cheaply than actual battle.

## Ending wars

A rational peace assessment asks:

- Has the original aim been achieved?
- Which side's reinforcement and research curve is improving?
- Are forts about to crack?
- Can either party win the game elsewhere?
- Are new enemies entering?
- What border can actually be held?
- Which terms are enforceable?

Continuing from anger is a strategic expenditure. Reputation and justice matter in multiplayer, but they should be pursued through explicit objectives rather than unbounded attrition.

# Part IX: Thugs, Supercombatants, Assassins, and Remote Force

## Campaign roles

Single commanders and remote effects should be classified by what they change:

| Asset | Campaign role |
| --- | --- |
| Light thug | PD raiding, province recovery, bottleneck pressure |
| Heavy thug | Defeat troop-heavy, mage-light forces |
| Supercombatant | Threaten armies, capitals, or decisive nodes |
| Army thug | Hold, kill elites, or add concentrated damage inside a line |
| Counter-thug | Trade cheaply into a known chassis |
| Assassin | Remove commanders, priests, mages, or gem carriers |
| Seducer or corrupter | Remove or acquire commanders through a special duel |
| Remote attacker | Damage, probe, distract, or burn gems without ordinary movement |
| Magic-phase mover | Intercept, surprise, reinforce, or open a storm operation |

The label does not guarantee performance. A heavy thug against troops may die instantly to the first prepared mage. A supercombatant without the correct resistance may be a very expensive target.

## The defensive onion

Durable commanders combine layers:

- avoidance: defence, glamour, awe, ethereal, displacement;
- mitigation: protection, invulnerability, resistances;
- recovery: regeneration, life drain, recuperation;
- control resistance: MR, mindlessness, morale, elemental and status immunity;
- endurance: reinvigoration, low encumbrance, fatigue management;
- offence: enough killing speed to avoid the turn limit and cumulative random failure;
- escape: returning, immortality, retreat, stealth, or magic movement.

Every layer must be checked against the intended target and the likely counter. The DRN makes absolute safety rare.

## Assassin rules

An assassin selects a random enemy commander in the province. Each assigned bodyguard has a base 50% chance of being present, modified by Bodyguard and Patience. The target is unprepared and does not use its ordinary battle script. Province context may add guards or bystanders.

An assassin cannot normally operate into or out of a besieged fort without Scale Walls, flight, teleportation, or equivalent access. Similar access restrictions apply to related orders such as seduction or infiltration. Mounted targets are often dismounted; when the assassin wins, the mount may also be killed.

Strategic consequences:

- commander redundancy reduces assassination leverage;
- bodyguards must be assigned before the attack;
- decoy commanders dilute random targeting;
- vital H3 claimants and communion masters require special protection;
- killing a leader may immobilise troops even if the army survives;
- assassinations inside a throne fort can disrupt both battle and claim timing.

## Remote operations

Remote force can:

- kill or afflict armies;
- summon attackers;
- change weather or scales;
- attack commanders;
- scry;
- damage walls;
- move units or armies;
- establish or protect local enchantments.

Remote operations should be combined with a physical exploitation plan. Damaging an army without contesting its fort or route may merely spend gems. A remote that removes PD immediately before a fast raider arrives converts more cleanly.

Domes reduce probability or redirect certain hostile rituals, but no dome is universal. Current official notes state that domes may protect against Astral Disruption. Exact layering and object interaction must be verified for the current spell set.

## Counter construction

Build answers from the enemy's dependency:

- high protection -> armour-piercing or armour-negating damage, fatigue, control;
- high defence -> area effects, multiple attacks, attack boosts, unavoidable effects;
- regeneration -> burst, decay, disease, or prevention of recovery;
- ethereal or glamour -> magic weapons and appropriate perception;
- elemental damage -> specific resistance;
- life drain -> lifeless targets or denial of contact;
- Phoenix Pyre -> fatigue and soul or battlefield control;
- high MR -> non-MR effects or penetration investment;
- magic movement -> protected nodes, domes, traps, distributed assets;
- stealth -> patrol, scrying, route control;
- item dependency -> counter-thug and looting plan.

The cheapest sufficient answer is normally superior to building a more expensive mirror.

# Part X: Sieges and Fort Operations

## Siege arithmetic

Book II owns the wall-reduction formula and repair modifiers; Book IV owns the storm battle. Strategy begins with the operational consequence: only commanders ordered to **Maintain Siege** and their eligible forces work on the walls. A commander preaching, forging, or performing another order is not also reducing the fort.

## The siege clock

A fort creates delay by requiring:

1. entry into the province;
2. one or more turns of wall reduction;
3. a legal Storm Fortress order after walls reach zero;
4. victory in the storm battle;
5. occupation, repair, and exploitation.

Each added turn permits:

- relief movement;
- remote attacks;
- recruitment elsewhere;
- diplomatic intervention;
- research completion;
- throne counterattacks.

Siege strength is tempo. An army that wins the field but needs six months to crack the fort may lose the strategic race to one that brought specialised siege bodies.

## Information asymmetry

The defender sees wall condition. The besieger receives qualitative messages:

| Message | Approximate wall state |
| --- | --- |
| Lightly damaged | High remaining integrity |
| Moderately damaged | About 51–85% remaining |
| Severely damaged | About 11–50% remaining |
| Critically damaged | About 1–10% remaining |

“Work is going very slowly” indicates less than roughly 15% of wall integrity was removed that turn according to the community reference. Because the besieger lacks exact totals, plans should include a safety margin and scouting of likely repair bodies.

## Inside and outside

At a friendly fort:

- **Defend** places the commander and troops inside;
- **Patrol** keeps them outside and able to fight field battles;
- an arriving ordinary move normally enters the fort;
- **Move and Patrol** arrives outside.

Version 6.35 adds one narrow escape route: a commander with teleport movement can move out of a besieged fort. This does not release an ordinary army, legalise every teleport ritual, or change the movement phase for other units. The order-entry exception is recorded in [Book X's siege orders](#b10-siege-orders), while [Book I](#b1-phase-iii-movement-and-conquest) retains the hosting sequence.

This distinction determines whether a unit joins a relief battle, remains protected, contributes to wall repair, or can be attacked by the besieger.

## Relief, break siege, and storm

A relief battle occurs before a scheduled storm. If relief succeeds, the storm does not occur. If relief fails, the besieger may still have to storm with losses, fatigue, expended gems, or altered scripts.

The defender can also **Break Siege**. A retreating defender may return inside the fort or move to an adjacent friendly province; where both are available, the manual gives a 50/50 selection. Fort context and later battles can change the ultimate retreat result.

When storming:

- the gate creates a narrow and dangerous battle context;
- intrinsic fort guards aid the defender;
- if a storming commander dies before the gate battle, its squads do not participate;
- besieged commanders that retreat from the storm die;
- relief and storm may force one attacker script through several battles;
- battlefield-wide magic may be restricted indoors under the current indoor rule.

## Starvation and trapped value

Besieged recruitment stops. Provincial income is divided between besieger and defender according to the siege rules, while site gems continue to the besieged side if a laboratory can connect them to the treasury. Declining fort supply can starve and eventually disease the garrison.

The defender should classify trapped units:

- irreplaceable mages that justify early relief;
- cheap repair bodies that justify delay;
- troops suitable for a break-siege battle;
- claim-capable priests on a Throne;
- stealth or special-access units able to leave;
- Pretender or immortal assets with separate risk.

Saving the fort while permanently diseasing the research core may be a strategic loss.

## One-turn cracks

A one-turn crack denies the defender most of the siege clock. It is especially important in throne operations. Calculate:

- fort wall strength;
- expected defending repair;
- flying and siege bonuses;
- Mindless, Animal, and Undisciplined penalties;
- remote wall damage;
- loss of siege contribution if commanders fight or perform other orders;
- possible Iron Walls or equivalent increases.

The one-turn crack force must also fight. Siege bodies that contribute enormous reduction but collapse in relief can become a liability unless protected.

## Multi-fort operations

Besieging several forts at once can exceed the defender's relief capacity. The attacker should stagger clocks so:

- at least one fort becomes stormable each turn;
- the main army can move between decisive storms;
- raiders cut reinforcement routes;
- enough force remains on each fort to prevent repair;
- gem reserves survive repeated battles.

The defender should repair, reinforce, and sally selectively. Preserving a key mage fort or Throne can justify abandoning a peripheral castle.

# Part XI: Diplomacy, Treaties, and Reputation

## Diplomacy changes force ratios

A treaty can remove an entire front from the immediate defence problem. A trade can create a path booster that research cannot. Intelligence from an ally can prevent a surprise. A coalition can turn a leading nation's local superiority into global inferiority.

Diplomacy is an exchange of:

- time;
- information;
- territorial certainty;
- resources and items;
- military access;
- threats and commitments;
- reputation.

The resource is not the message. It is the changed set of legal and expected actions.

## Formal and social NAPs

Dominions 6 can use formal in-game diplomacy. Depending on settings, a formal NAP may be binding: the game blocks offensive actions that violate it. Games can also use nonbinding settings or social treaties negotiated outside the engine.

These systems should not be silently mixed:

| Doctrine | Authority | Main benefit | Main risk |
| --- | --- | --- | --- |
| Strict formal NAP | Game engine | Clear mechanical enforcement | Edge cases may permit conduct players consider hostile |
| Written social NAP | Agreed text and host rules | Can cover remotes, stealth, globals, access, and victory | Requires shared interpretation and reputation |
| Hybrid | Formal pact plus written additions | Enforcement plus broader expectations | Conflicts between engine legality and social meaning |
| No NAP | No non-aggression commitment | Maximum freedom and fewer countdown disputes | Higher uncertainty and defence cost |

Before a game begins, players should know which doctrine governs conflicts.

## Binding diplomacy

Illwinter describes formal diplomacy as optional, with binding NAPs available for humans and AI and a setting that makes them nonbinding. The command-line help exposes the corresponding `--weakdiplo` and `--nodiplo` settings. This establishes three engine baselines: binding, nonbinding, and absent. It does not turn an organised game's social customs into engine rules.

The official correction history supplies the safest current exception ledger:

| Version | Official NAP or allied-territory rule |
| --- | --- |
| 6.01 | NAPs do not govern arena battles; global-enchantment attacks no longer respect NAPs. |
| 6.03 | A besieged force may break free from its fort during a NAP. |
| 6.04 | A defect involving movement bumps during a NAP was corrected. |
| 6.12 | Players can bump forces covered by a NAP; a besieger counts as bordering the besieged player for diplomacy. |
| 6.13 | An army may move into NAP-protected forces that are besieging its own fort. |
| 6.19 | An expiring NAP continues counting down after a nation dies; modders gained `#napbreakrit` for spells. |
| 6.29 | The Wait order became legal in allied territory. |
| 6.30 | Expiring NAPs were corrected in disciple games. |

This ledger proves that a binding pact is not a blanket ban on every hostile-looking interaction. It also shows why an old anecdote can be wrong after a patch. The complete action matrix—ordinary movement, magic movement, anonymous and attributed rituals, stealth incidents, province transfers, sieges, and every disciple case under all three settings—still requires S12.

## Minimum treaty terms

A useful NAP states:

- the parties;
- whether it is formal, social, or both;
- the notice period;
- exactly how turns are counted;
- the first legal turn for hostile orders and for hostile contact;
- treatment of scouts and stealth armies;
- remotes, assassinations, seduction, heretics, disease spreaders, and unrest effects;
- dominion and temple pressure;
- province trades and accidental bumps;
- harmful globals;
- third-party access;
- whether imminent victory suspends the pact;
- how mistakes are repaired.

Without these terms, both parties may act in good faith under incompatible definitions.

## Countdown arithmetic

Community conventions differ. One explicit convention treats an N-turn NAP ended on turn T as permitting contact on turn T+N. Under that convention, ending NAP3 on turn 10 permits attack orders on turn 12 that make contact during hosting into turn 13. Other groups count differently.

Never rely on the label alone. State the first legal **order-submission turn** and the first legal **contact turn** in plain numbers.

## Treaty edge cases

Potential disputes include:

- a scout being discovered;
- a stealth army positioned before expiry;
- an accidental movement bump;
- a remote attack with uncertain attribution;
- a harmful global;
- selling a corridor to a third party;
- cutting off agreed spoils;
- dominion pressure;
- independent or event armies taking border provinces;
- a throne rush while formal NAPs remain binding.

Engine legality does not settle social legitimacy unless the group agreed that it would. A written doctrine protects both strategic freedom and the community from avoidable arguments.

## Trade

Trades can exchange:

- gems and blood slaves;
- forged items;
- provinces;
- mercenary noncompetition;
- intelligence;
- ritual or global contributions;
- military access;
- coordinated timing.

Good trade messages specify item, gem type, quantity, delivery turn, sender, recipient, and contingency if forging or delivery becomes impossible. Trades are generally treated as binding in community practice because simultaneous turns expose one party to opportunistic default.

Assess the strategic effect, not only nominal gem equality. A five-gem booster that opens a new path can be worth far more than five surplus gems. A trade that enables an enemy's throne rush may be profitable and fatal.

## Reputation

Reputation changes future transaction costs. Reliable players receive information, trades, and treaties with less suspicion. Deceptive or rules-lawyering play may win one exchange while forcing expensive hostility in later games.

Reputation is not a demand for passivity. A treaty can be ended, a rival can be threatened, and a surprise attack after legal expiry is ordinary strategy. The core distinction is between hard bargaining within clear terms and exploiting ambiguity that the other party reasonably believed was settled.

## Threat communication

A useful threat states:

- the behaviour that must change;
- the consequence;
- the deadline;
- an achievable off-ramp.

Vague outrage does not deter. Impossible demands turn the threat into a declaration of war. Excessive detail can reveal exact capacity. The objective is credible constraint with minimal disclosure.

## Coalition politics

Coalitions form around relative threat. Indicators that create coalitions include:

- rapid province, fort, research, or gem growth;
- oppressive globals;
- visible throne progress;
- elimination of neighbours;
- treaty networks that appear permanent;
- unique late-game access;
- refusal to communicate.

A leader can reduce coalition pressure by:

- leaving other players with meaningful autonomy;
- sharing limited intelligence or trade;
- avoiding unnecessary worldwide harm;
- framing war aims as bounded;
- preventing a rival from appearing harmless while compounding;
- keeping the true throne conversion window short.

Coalition management is not concealment of all strength. If the position is obviously dominant, implausible denials destroy credibility.

# Part XII: Thrones, Cataclysm, and Endgame Conversion

## Victory by Ascension Points

By default, Thrones of Ascension provide the victory structure. A Throne's level equals its Ascension Point value:

| Throne level | Ascension Points | General defence |
| --- | ---: | --- |
| 1 | 1 | Stronger than ordinary independents but often early-accessible |
| 2 | 2 | Substantial army and magic support |
| 3 | 3 | Extremely strong defence, often including Pretender-class commanders |

The host sets the total points present and the number required. Conquer-all is an alternative, but throne settings define most campaign deadlines.

## Finding and identifying Thrones

The presence of a Throne becomes visible when the province is observed through ordinary means such as scouting, dominion, or neighbouring ownership. Exact identity requires stronger information, such as a spy or direct control, according to the current community reference. When a Pretender awakens, unrevealed Thrones are sensed; an awake Pretender receives this information on turn 2.

Throne identity matters because effects vary widely: gems, gold, scales, bless changes, recruitment, research access, unrest, dominion spread, or world events. Treat community tables as object references to verify against current game data before committing a design.

## Claiming

A Throne can be claimed by:

- the Pretender;
- the Prophet;
- a priest with Holy 3 or more.

The nation must own the province. If a fort exists, a besieger cannot claim through the walls, while the besieged owner can still claim. Claiming is a turn action and resolves during hosting at the throne-claim step. Conquest makes the Throne unclaimed until a legal claimant acts.

Book III owns the exact same-turn state matrix. For campaign planning, remember the operational result: killing a claimant after the step-8 claim does not undo it; conquering an unfortified Throne or successfully storming its fort removes the claim before the step-57 victory check; a siege that has not taken the fort does not. Once the claim resolves, counterplay must attack the ownership state and not only the claimant.

A claimed Throne:

- supplies Ascension Points;
- spreads dominion through its throne checks;
- activates its claimed effects;
- visibly lights on the map.

The campaign must include the claimant. A victorious army without an H3, Pretender, or Disciple is at least one turn farther from victory.

## Throne arithmetic

Every turn, record for each living nation:

- claimed points;
- unclaimed controlled points;
- points under siege;
- points reachable within one ordinary move;
- points reachable in the magic phase;
- claim-capable units in range;
- forts that can be cracked in one turn;
- points required to win.

Also record the **maximum plausible claim**, not only current points. A nation on five of eight required points that controls an unclaimed three-point Throne can win with one claim order.

## The throne-rush sequence

A common fortified one-Throne rush follows this timing:

| Turn | Attacker | Defender and bystanders |
| --- | --- | --- |
| T+0 orders | Move enough army and siege power onto the Throne | Detect approach, reinforce, remote, or prepare relief |
| T+1 orders | Walls are cracked; order storm; move H3 or Pretender into position | Break siege, relieve, attack other attacker Thrones, burn gems |
| T+2 orders | After successful storm, claim | Last chance is normally to remove another claimed Throne or prevent the claim |
| T+3 hosting | Claim resolves and victory occurs if threshold is met | Counter must already have changed the AP total or ownership |

Exact battle sequence, magic movement, wall state, and claim position can alter this schedule. The important lesson is that bystanders do not have “several turns” merely because the fort has not yet fallen. A one-turn crack compresses the coalition's response into one hosting cycle.

## Requirements for a credible rush

The attacker needs:

- enough siege power to crack on schedule;
- enough combat power for relief, sequential battles, and the storm;
- scripts that function across those battle contexts;
- gems for repeated combat;
- resilience against remotes and assassins;
- claimant access;
- defence of existing claimed Thrones;
- secrecy or deception;
- a response to Iron Walls and emergency reinforcement.

A throne rush is an operation, not a large army walking toward a victory icon.

## Defending against a rush

Defence can attack any dependency:

- reinforce or increase wall strength;
- kill the siege bodies;
- force extra battles to consume gems;
- assassinate commanders or the claimant;
- use magic-phase attacks before relief and storm;
- break siege;
- capture or unclaim one of the attacker's existing Thrones;
- cut the claimant's route;
- form a coalition and share exact timing;
- exploit binding-NAP limitations through pre-agreed victory clauses.

Counterattacking another claimed Throne may be more reliable than saving the target. Victory arithmetic, not pride of ownership, decides.

## Information warfare

Surprise is especially valuable because every visible turn permits specialised counter-scripts and coalition formation. Methods include:

- stealthy elements staged near or on the target;
- flying, sailing, underwater, or plane routes;
- magic-phase mage delivery;
- high Map Move and movement items;
- false army displays and secondary throne threats;
- ordinary wars used as cover;
- keeping the H3 claimant separate until required.

The attacker must balance concealment against siege. Stealth forces on the fort do not contribute while sneaking. The operation needs a turn when hidden potential becomes actual wall reduction.

## Defence of owned Thrones

Throne defence should be layered:

- fort and wall strength;
- enough repair to defeat casual siege;
- patrols and anti-assassin measures;
- a claimant or priest plan;
- a mobile relief force;
- remote and magic-phase support;
- gem reserves;
- alternate victory arithmetic if one Throne falls.

Not every Throne requires the same force. Concentrate on the points whose loss changes the victory threshold, the routes opponents can reach, and the forts vulnerable to one-turn cracking.

## Cataclysm

If enabled, Cataclysm begins after the configured turn. Horrors attack and destroy Thrones. Each destroyed Throne reduces the Ascension Points required to win, so the threshold moves as the world collapses. Current official changes make Cataclysm harder to counter.

The manual states that if no one owns a Throne when the last is destroyed, the horrors win. Current community reference describes all Thrones destroyed as a draw; this wording conflict must be reproduced under current 6.36 before being stated more narrowly. Operationally, neither result is a player victory.

Cataclysm strategy:

- track turns to arrival;
- fort and defend key Thrones;
- prepare to kill or dislodge horrors;
- recalculate required points after every destruction;
- avoid plans that mature after the relevant Thrones cease to exist;
- treat every surviving point as increasingly decisive.

Cataclysm is more than late-game flavour. It shrinks the objective map.

# Part XIII: Recovery, Elastic Defence, and Defeat Management

## A lost battle is not automatically a lost war

After a major defeat, the strategic position contains several different losses:

- **force loss:** troops, mages, Pretender, items, and gems;
- **capacity loss:** forts, laboratories, sacred recruitment, and researchers;
- **position loss:** routes, sites, Thrones, dominion, and borders;
- **information loss:** scouts, known enemy scripts, and hidden alternatives;
- **diplomatic loss:** confidence, allies, and deterrence;
- **tempo loss:** the opponent chooses the next urgent event.

Recovery begins by separating them. A nation may have lost its main army but retained every mage fort and a superior research curve. Another may win the field but lose its only laboratory and retreat corridor. Battle animation does not rank these consequences.

## The first post-defeat turn

Perform this audit before issuing revenge orders:

1. Count surviving mages, commanders, items, and gem stocks.
2. Identify where every routed force went.
3. Check leadership and whether troops are stranded.
4. Mark the enemy's legal next destinations.
5. Protect the capital, key mage forts, labs, Thrones, and corridors.
6. Determine whether the enemy can crack each fort in one turn.
7. Read the replay for spent hostile gems, fatigue, casualties, and revealed scripts.
8. Ask neighbours for information, trade, pressure, or coalition action.
9. Select the cheapest research or recruitment stabiliser.
10. Preserve a retreat path for the next battle.

The instinct to recreate the destroyed army exactly is often wrong. The opponent has already demonstrated an answer to it.

## Elastic defence

Elastic defence exchanges low-value territory for time while preserving the force needed for a counterstroke. It uses:

- forts as delay;
- scouts to track the attacker;
- PD and cheap units as tripwires;
- raiders against the attacker's rear;
- mobile reserves;
- selective relief;
- research completed behind the line;
- diplomacy that makes further advance expensive.

The defence is not passive. It forces the attacker to choose between:

- concentrating and losing provinces to raids;
- dispersing and risking defeat;
- storming and spending gems;
- waiting and allowing research or coalition response.

## What to hold

Rank provinces:

| Priority | Examples |
| --- | --- |
| Existential | Capital, last candle sources, victory-critical Throne |
| Capacity | Major mage fort, rare recruit site, blood centre, global origin |
| Network | Corridor, plane gate, only lab chain, retreat hub |
| Economic | Rich province, strong gem site |
| Disposable | Poor border land that does not open the interior |

The list changes with the position. A one-income cave can be existential if it is the only route to a plane or underwater enclave.

## Preserving cadres

Troops are often easier to replace than:

- high-path mages;
- experienced communion leaders;
- H3 priests;
- item carriers;
- rare randoms;
- prophet;
- Pretender;
- specialised commanders.

A small surviving cadre can rebuild a battlefield package if given forts and time. Protect command redundancy, retreat routes, and extraction items. Do not place every rare path in the same army unless the battle is truly decisive.

## Counteroffence

The attacker is most exposed when:

- concentrated on a fort;
- low on gems after several battles;
- beyond reinforcement range;
- dependent on one lab;
- holding provinces with token PD;
- using a revealed script;
- committed under expiring treaties elsewhere.

Counteroffence does not require retaking every lost province. It may destroy the siege army, cut its retreat, take its staging lab, threaten its capital, or force a peace by opening a second front.

## Negotiating from weakness

A weakened nation still possesses:

- information;
- remaining army or raiders;
- forts that consume time;
- gems and items;
- a vote in coalition politics;
- the ability to make another nation the beneficiary of its collapse.

Useful offers are concrete: a stable border, a province transfer, gem payment, joint war, intelligence, or permission to disengage. Empty threats weaken reputation; credible kingmaking threats can change the attacker's calculation but may also unite the table against the speaker.

## Elimination, handover, and meaningful play

When recovery is impossible, distinguish:

- a nation still capable of affecting victory;
- a position that can be handed to a substitute;
- an agreed concession under host rules;
- a player leaving without setting AI or notifying the host.

Long multiplayer games depend on continuity. A defeated player should follow the game's substitution, AI, and concession rules rather than silently stale. The host's master password can set a dropped player to AI, but it also grants access to positions and should be controlled accordingly.

# Part XIV: Single-Player Strategy and the AI

## What the AI receives

Difficulty modifies AI bonuses to gold, resources, recruitment points, and magic income:

| Difficulty | Bonus or penalty |
| --- | ---: |
| Easy | -30% |
| Normal | 0% |
| Difficult | +30% |
| Mighty | +60% |
| Master | +100% |
| Impossible | +150% |

These modifiers do not increase commander recruitment rate or Holy Points. The AI also has omniscient knowledge of province ownership, which removes one information problem human players face.

## Current AI capabilities

Dominions 6 AI is improved over earlier descriptions. It:

- builds forts;
- recruits better national troops;
- plans high-level rituals;
- uses global enchantments;
- attempts Dispels;
- participates in formal diplomacy.

Current patches also corrected behaviours such as trying rituals without a laboratory, researching when unable, and preaching with non-priests. The AI still operates through programmed evaluation rather than human political judgment and long-form deception.

Version 6.35 also improved the AI's protection of important mages. This should be read as a narrower targeting and preservation improvement, not as evidence that the AI now values mage-turns, research concentration, retreat routes, or political risk with human reliability.

## Learning games

A useful first learning environment uses:

- a small or medium map;
- one plane unless plane travel is the lesson;
- Normal AI before large economic bonuses;
- ordinary independent strength;
- visible score graphs;
- Thrones as the victory condition;
- a nation with understandable troops and broad enough magic;
- no mods for the first rules-learning game.

Then add difficulty or complexity one variable at a time. High AI bonuses teach crisis management but can hide whether the player's economy and expansion are fundamentally sound.

## Productive self-imposed constraints

To learn transferable strategy:

- do not rely on repeated reloads except for controlled testing;
- avoid exploiting a predictable movement loop indefinitely;
- track Throne arithmetic even when the AI does not punish mistakes;
- practise scouts, reserves, forts, and gem budgets as if facing humans;
- watch important battles and diagnose mechanisms;
- use formal diplomacy if it is part of the intended multiplayer environment;
- compare turn-12 expansion across repeated starts.

The objective of practice is not only to beat the AI. It is to create habits that survive a human opponent.

## What AI games teach well

- interface and turn execution;
- national recruitment and expansion;
- battle scripting;
- economy and infrastructure;
- research pacing;
- siege and movement rules;
- army composition against varied rosters;
- surviving numerical pressure;
- late-game spell and global operation.

## What requires multiplayer experience

- credible deception;
- negotiated borders;
- reputation;
- coalition timing;
- adaptive counter-research;
- human throne-rush detection;
- trades built around path scarcity;
- restraint and threat communication;
- opponents deliberately burning gems or hiding scripts.

Single-player mastery is a foundation, not a complete substitute for diplomacy and adversarial uncertainty.

# Part XV: Turn Discipline and Multiplayer Operations

## The strategic turn order

The complete engine hosting sequence appears in Book I. A player-facing strategic turn should be reviewed in this order:

1. **Victory:** Can anyone win during the coming hosting?
2. **Messages:** Battles, events, rituals, construction, diplomacy, and throne changes.
3. **Map change:** Ownership, forts, labs, dominion, routes, and enemy movement.
4. **Threats:** Every hostile force's legal destinations and phase.
5. **Battles:** Replay decisive and surprising results.
6. **Research:** Completion, caster access, and pivot.
7. **Economy:** Treasury, upkeep, recruitment queues, forts, and PD.
8. **Magic:** Rituals, forging, site search, gem movement, globals, and domes.
9. **Armies:** Leadership, squads, scripts, supplies, movement, and retreats.
10. **Diplomacy:** Treaties, countdowns, trades, warnings, and coalition information.
11. **Verification:** Illegal arrows, idle commanders, empty labs, unclaimed Thrones, and unsubmitted turn.

Victory comes first because every other optimisation is irrelevant if the game ends.

## Commander roles and naming

Names should expose function:

- `RCH F2A1` for a researcher's relevant paths;
- `FORGE E3` for a forge specialist;
- `ARMY N` for a field group;
- `CLAIM H3` for a throne claimant;
- `RAID A` for a raider;
- `MULE 20F` for carried gems;
- `SCOUT EAST` for coverage;
- `NAP3 T24` in notes for a treaty deadline.

The exact scheme matters less than consistency. A late-game turn should not require reopening every commander to remember why it exists.

## Army package records

For each major army, record:

- commander roster and redundancy;
- troop roles and formations;
- five-order scripts;
- expected unscripted behaviour;
- gem load and optional spending policy;
- communion or Sabbath structure;
- target matchups;
- known counters;
- movement class;
- supply;
- retreat provinces;
- siege contribution;
- next reinforcement.

This converts battle preparation into a repeatable system and makes after-action review possible.

## Diplomacy records

Keep:

- exact treaty text;
- agreement turn;
- expiry notice turn;
- first legal order and contact turns;
- trades owed and delivered;
- disputed province settlement;
- promises to third parties;
- public and private victory commitments according to house rules.

Memory becomes unreliable over games lasting months. Written terms protect strategy and relationships.

## Submitting safely

Before ending the turn:

- use the warning system but do not assume it catches every strategic error;
- confirm commanders who must remain hidden are Sneaking, not moving normally;
- confirm an army entering its own fort uses Move and Patrol if it must fight outside;
- confirm all special-movement troops qualify;
- confirm rivers and passes are open;
- confirm claimant and siege orders;
- confirm commanders expected to reduce walls are maintaining siege;
- confirm gems and slaves are on the correct bodies;
- confirm no forge, ritual, or research order unintentionally replaced a military task;
- save and submit according to server practice.

## Stales, extensions, and substitutes

House rules should define:

- when extensions are granted;
- how requests are made;
- what counts as repeated staling;
- when a substitute may be found;
- when the host may set AI;
- how concessions are handled;
- whether private information can be shared with a substitute.

Reliable scheduling is part of multiplayer skill. A brilliant plan that repeatedly stales damages the game more than an imperfect plan submitted on time.

# Part XVI: The Active Modded Ruleset

## What carries across

Book IX defines the exact combined ruleset and its load order. The durable strategic ideas still include simultaneous planning, movement timing, information, concentration, siege clocks, treaty clarity, Throne arithmetic, conversion, logistics, and attention. Their numbers and available tools may change, so their application must be recalculated.

Recruitment, sacred throughput, paths, Pretenders, blessings, spells, items, summons, sites, siege bodies, national mechanics, and AI priorities may all differ. An unmodded expansion party, research queue, thug kit, or counter is evidence for a method, not a ready-made combined-mod plan.

## The strategic rule

> **Mod compatibility is part of force estimation.** If load order changes an object that a plan depends on, the plan is a different plan even when its name remains the same.

## Combined strategy test

Every nation package will later require four snapshots:

1. unmodded;
2. DE only;
3. Divinitus only where applicable;
4. DE then Divinitus.

Diff the roster, Pretenders, paths, blessings, spells, items, sites, summons, and strategic special abilities. Then repeat expansion, research, battle, raid, and throne tests.

# Part XVII: Controlled Strategy Tests

## Test record format

Every controlled test should record:

- game version;
- exact map and settings;
- nation and age;
- Pretender design;
- active mods, hashes, and load order;
- turn;
- province and terrain;
- units, commanders, items, gems, orders, and scripts;
- expected result;
- actual messages and replays;
- repetition count;
- conclusion and confidence.

Strategy tests differ from formula tests because the objective is often robustness. Record distributions and failure types rather than only the best result.

## S1: Expansion reliability

Run the intended opening to turn 12 on at least ten starts.

Record:

- provinces and forts;
- treasury and income;
- army survivors;
- commander and mage production;
- PD spending;
- target types;
- defeats and causes;
- ability to fight a first war.

Compare median and worst credible outcomes, not only maximum provinces.

## S2: Expansion matchup matrix

Create representative independent provinces for:

- militia and ordinary infantry;
- archers;
- barbarians and high-damage infantry;
- light and heavy cavalry;
- tribes;
- giants or elephants;
- undead;
- Amazons and mage-supported defenders;
- Throne defenders.

Test party size, formation, script, bless, attrition, and retreat.

## S3: Map movement boundaries

Test armies at exact Map Move limits across:

- every surface terrain;
- snow;
- roads;
- friendly and enemy presence;
- survival abilities;
- rivers and mountain passes;
- caves;
- flying;
- mixed armies.

Record when the arrow remains but movement fails.

## S4: Hostile swaps and interception

On several terrains and army-size ratios, order hostile armies to swap provinces.

Record:

- battle province;
- whether they miss;
- sequential-battle order;
- retreat results;
- effect of stealth and allied forces.

Run direct one-step swaps separately from multi-province movement. For the direct set, preserve army chassis values and compare miss rate and battle location with the published 0-349 and open-ended chassis-die hypothesis.

## S5: Patrol detection

At controlled Stealth and Patrol strengths, repeat detection trials with:

- zero and high unrest;
- PD below and above 15;
- commanders and ordinary units;
- flying, Mindless, and Undisciplined patrollers;
- stealth troops with ordinary and +50 or greater stealth.

Compare observed rates with the official opposed open-ended rolls.

The main 6.36 table is already closed by direct enumeration. This suite now checks exceptional contributors, displayed rounding, invisible units, global bonuses, and any difference between the manual's halving rule and community descriptions of Undisciplined patrol strength.

## S6: Raid and pillage

Verify:

- the Map Move 20 requirement;
- Pillager commander legality;
- which units contribute;
- half-strength contribution;
- sequence after battle;
- population, unrest, supplies, gold, and food;
- one-month supply duration;
- interaction with forts and retreat.

Add boundary cases around the historical `floor((Strength + Combat Speed + 10 x Fear) / 2)` unit-strength hypothesis, the proposed flyer substitution, population-to-strength failure boundary, and enemy-fort failure. Record raw outcomes rather than accepting the old downstream gold and casualty formulas.

## S7: Intelligence channels

For the same province, compare:

- neighbour report;
- scout;
- priest;
- spy;
- dominion;
- scrying;
- ownership.

Record every displayed field, error range, glamour detection, and update timing.

## S8: Siege arithmetic

Test Strength values around square and rounding boundaries with:

- flying;
- Mindless;
- Animal;
- Undisciplined;
- combinations;
- siege and castle-defence bonuses;
- intrinsic fort guards.

Verify reduction, repair, qualitative messages, and the effect of non-siege orders.

## S9: Relief and storm order

Create a cracked fort with:

- outside relief;
- Break Siege;
- magic-phase reinforcements;
- a scheduled storm;
- multiple allied attackers;
- commander deaths before the gate.

Record battle sequence, scripts, gem consumption, participant squads, and retreat.

## S10: Fort starvation

Record supplies and disease risk for at least ten siege turns with:

- ordinary living units;
- survival abilities;
- supply items and spells;
- commanders and mounts;
- large and small forts.

Verify the printed declining supply sequence and two-turn disease condition.

## S11: Assassination and bodyguards

Repeat assassination against:

- zero to five bodyguards;
- different Bodyguard and Patience values;
- mounted targets;
- fort interior and exterior;
- besieged forts;
- special-access assassins;
- multiple decoy commanders.

Record target distribution, bodyguard presence, surprise context, mount survival, and retreat.

## S12: Formal NAP edge cases

Under binding and nonbinding settings, test:

- direct movement attack;
- magic-phase attack;
- remote damage;
- assassination and seduction;
- stealth positioning;
- accidental bumps;
- independent recapture;
- harmful globals;
- throne-rush response.

Distinguish engine blocking, warnings, legal execution, and social doctrine.

Repeat the matrix with diplomacy binding, nonbinding through `--weakdiplo`, and absent through `--nodiplo`. Preserve the exact version and separate engine legality from any social rule used by the game.

## S13: Throne claim timing

Treat the established claim-loss matrix as a regression target and test claims by:

- Pretender;
- Disciple;
- H3;
- H2 boosted or transformed by relevant effects;
- besieged owner;
- besieger;
- claimant arriving by ordinary and magic movement;
- simultaneous capture and claim attempts.

Record hosting messages, claimant survival, full or partial ownership, fort state, AP immediately before victory, and dominion spread. A current test should reproduce claimant death, unfortified conquest, siege without storming, and successful storming separately. Exact simultaneous winning-AP ties remain an unresolved adjacent branch.

## S14: One-turn throne operation

Build a T+0 to T+3 scenario with:

- one-turn wall crack;
- relief;
- remotes;
- assassins;
- claimant movement;
- counterattack on an owned Throne.

Repeat with different event and movement branches to validate the operational timeline.

## S15: Cataclysm

In 6.36, record:

- first Cataclysm turn;
- horror target selection;
- fort interaction;
- throne destruction;
- required AP after each destruction;
- final result when all Thrones disappear;
- effect of current countermeasures.

This test resolves the manual/community wording conflict.

## S16: AI difficulty economy

Use identical nations and provinces at each difficulty.

Measure:

- gold;
- resources;
- recruitment points;
- magic income;
- commander recruitment;
- Holy Points;
- fort timing;
- ritual, global, and Dispel behaviour.

Confirm which modifiers apply and which do not.

## S17: Raider response exchange

For each standard thug or stealth package:

1. price the raider in gold, gems, and mage-turns;
2. price each defender;
3. run repeated battles;
4. include capture and looting;
5. measure provinces taken before interception;
6. compare attention and map impact.

The output is a campaign exchange table, not only a duel result.

## S18: Recovery scenario

Begin from a saved position after a main-army loss. Compare:

- immediate reconstruction;
- fort-based elastic defence;
- raiding counteroffence;
- emergency research pivot;
- negotiated peace.

Measure survival of capacity, territory after six turns, research, gem stock, and opponent advance.

## S19: Information-deception scenario

Present opponents with:

- visible false mass;
- hidden magic movers;
- multiple target routes;
- manipulated gem loads;
- staged claimants.

Record which observations actually change rational defence. Reject deception that works only because the defender ignores available evidence.

## S20: Combined-mod campaign regression

For the frozen DE + Divinitus load order, repeat:

- turn-12 expansion;
- key movement;
- first-war package;
- representative raider and counter;
- siege arithmetic;
- throne operation;
- AI practice game.

Any difference must be linked to a mod command or recorded as test-only evidence.

# Part XVIII: Operational Checklists

## New-game settings

- Patch and manual revision recorded.
- Map, planes, and start density understood.
- Independent strength recorded.
- Research and magic-site settings recorded.
- Throne levels, total points, required points, and Cataclysm recorded.
- Score-graph settings recorded.
- Diplomacy mode and NAP doctrine recorded.
- Story events and special rules recorded.
- Mods, hashes, and load order recorded.
- Extension, substitution, and concession rules recorded.

## Turn-12 expansion audit

- Provinces, forts, and claimed routes.
- Income, treasury, upkeep, and resources.
- Surviving expansion parties.
- Capital recruitment unlocked.
- Researchers and site search.
- First fort start or reason for delay.
- Known neighbours and border settlements.
- Thrones located and inspected.
- First-war deterrence.
- Opening variance across tests.

## Pre-war audit

- War aim and stopping condition.
- Legal treaty date.
- Enemy main army and reserve.
- Known research, paths, Pretender, and counters.
- Friendly package, scripts, gems, and replacements.
- Siege strength and fort sequence.
- Scout coverage and deception plan.
- Other borders and coalition reaction.
- Failure route and peace terms.
- Throne conversion.

## Army departure

- Every troop has legal leadership.
- Slowest movement and survival checked.
- Rivers, passes, caves, water, and planes checked.
- Supply checked.
- Scripts and formations checked.
- Gems and slaves checked.
- Bodyguards checked.
- Spare commander and retreat route checked.
- Siege contribution checked.
- Claimant included if required.

## Raider

- Target class and likely PD.
- Legal route and movement.
- Counter locations.
- Minimal equipment.
- Fatigue stability.
- Retreat or escape.
- Replacement cost.
- Captured province exploitation.
- Loot carrier.
- Recall condition.

## Counter-raider

- Exact raider observed or inferred.
- Cheapest relevant counter.
- Interception destinations.
- High-value nodes covered.
- Empty provinces reclaimed cheaply.
- Gear-looting plan.
- Main army not distracted unnecessarily.
- PD raised only where it changes the matchup.

## Siege attacker

- Wall strength and one-turn crack estimate.
- Repair estimate.
- Maintain Siege orders.
- Relief routes.
- Sequential battle and gem budget.
- Storm script suitable for gate and indoor context.
- Commander survival and redundancy.
- Supplies.
- Claimant and post-storm defence.

## Siege defender

- Wall condition.
- Repair bodies.
- Interior supply and disease.
- Break Siege package.
- Outside relief and phase timing.
- Remote and assassination options.
- Irreplaceable cadre extraction.
- Alternate fort or Throne defence.
- Counterattack on attacker's strategic assets.

## Diplomacy

- Exact parties and terms.
- Formal, social, or hybrid.
- Notice and first legal turns.
- Scout, stealth, remote, dominion, global, and access terms.
- Trade quantities and delivery.
- Victory emergency clause.
- Mistake procedure.
- Written record.

## Throne watch

- Current and plausible AP for every nation.
- Controlled but unclaimed Thrones.
- Claim-capable units and movement.
- One-turn-crack forts.
- Magic-phase access.
- Existing claimed-Throne defence.
- Cataclysm threshold.
- Coalition contacts.
- Counterattack targets.

## Recovery

- Surviving cadres, gems, and items.
- Enemy next destinations.
- Existential, capacity, network, economic, and disposable provinces.
- Cheap stabilisation research.
- Fort and retreat line.
- Raider counteroffence.
- Diplomatic options.
- New army package rather than blind replacement.

## Final submission

- No immediate opponent victory.
- All messages read.
- All decisive replays watched.
- Treasury and queues checked.
- Research allocated.
- Forts, labs, temples, and PD intentional.
- Rituals and forging intentional.
- Gems, items, and troops transferred.
- Movement remains legal.
- Siege, patrol, sneak, defend, and claim orders correct.
- Treaty and trade obligations fulfilled.
- Turn saved and submitted.

# Part XIX: Essays

## Essay I: The Expansion Problem

Expansion is often measured by a turn-12 province count because the number is visible, easy to compare, and strongly connected to early income. It is useful and incomplete. The real expansion problem is to acquire enough valuable and defensible territory while preserving the capacity to survive first contact.

The opening begins before the map appears. Pretender design decides whether an awake monster supplies a second army, a bless turns sacreds into a specialist expansion force, or scales finance ordinary troops and early infrastructure. These choices do not buy abstract power. They buy particular expansion matchups at particular times. An awake monster that clears militia but dies to the first heavy cavalry province has not solved expansion; it has created a route constraint with catastrophic failure.

The first skill is classification. Independents are not a ladder from small to large. They are a collection of damage, armour, morale, missile, lance, formation, and magic problems. Heavy national infantry may walk through ordinary weapons and bleed out against barbarians. High-defence sacreds may dominate low-attack infantry and collapse when surrounded. Archers may erase unarmoured tribes but waste months against shielded heavy troops. A party becomes reliable when its player knows what it is designed to fight.

The second skill is routing. Each province changes future options. A cap-ring forest can release resources into capital recruitment. Rich farmland can finance a fort. A choke point can define a border. A route around an interior pocket can reserve easy provinces for a third party. Province value is not just the income shown this turn; it is the chain of recruitment, movement, and diplomacy that ownership makes possible.

The third skill is force sizing. Too little force creates losses whose true cost includes replacement, delayed parties, commander transport, and deterrence. Too much force concentrates strength that can conquer only one province per month. The efficient party is not the mathematical minimum that can win under average rolls. It carries enough margin to survive uncertain reports, unlucky combat, and the next target.

The fourth skill is transition. Independent expansion offers largely static opponents. Human contact introduces adaptation, deception, and simultaneous movement. A nation that continues driving small parties outward after borders are settled may present each one for defeat. A nation that combines too early may surrender unclaimed land. The transition occurs when the next neutral gain is worth less than the fort, research, reserve, or diplomatic stability it delays.

Expansion testing works because it turns these judgments into experience before the game begins. The test must include realistic PD, recruitment, site search, and infrastructure or it rewards a position that cannot exist in the real campaign. Repetition matters more than one ideal map. The goal is a procedure that produces a resilient median and an acceptable bad start.

The final measure is the first-war position. Territory is valuable when it has become income, resources, forts, mages, sites, routes, and political claims. Expansion is complete only when the nation can defend or exploit what it has taken.

## Essay II: Information as a Resource

Information has no treasury icon, yet it changes the value of every other resource. Ten gems carried into the correct battle are a weapon; ten gems carried by a mage who is intercepted by the wrong counter are loot. A fort one turn from cracking is a crisis if observed and a surprise defeat if not. A Throne held by an opponent is ordinary territory until its claim changes the victory arithmetic.

Dominions distributes information unevenly. Ownership gives one view, adjacency another, scouts another, spies another, dominion another, and scrying another. Score graphs show trends without scripts or stocks. Battle replays reveal exact deployed tools but only after contact. Diplomacy supplies claims whose reliability must be judged. The strategic task is not to obtain perfect knowledge. It is to combine imperfect channels before the decision deadline.

This begins with questions. “What does the enemy have?” has no practical stopping point. “Can the border fort be cracked next turn?” directs collection toward army size, siege bodies, wall modifiers, and nearby movement. “Can the army survive Foul Vapors?” directs attention toward Nature paths, research evidence, poison resistance, and gem carriers. Intelligence has value when it changes an order.

Uncertainty must remain visible. A missing army may have withdrawn, hidden through glamour, moved through another route, or prepared a magic-phase attack. A research spike may indicate a new threshold, an event, or simply accumulated infrastructure. Experts are not those who always guess correctly. They assign confidence, retain alternative explanations, and choose orders that remain tolerable under several branches.

Denial is the other half. Patrolling out scouts reduces enemy coverage. Concealing item transfers delays counter construction. Holding a magic mover on a central lab creates several possible targets. Hiding everything also sacrifices deterrence: an enemy cannot fear a capability it does not believe exists. Selective revelation can preserve a border while the decisive package stays concealed.

Deception is useful only when it changes rational allocation. A false army near an irrelevant province is theatre. A displayed force near one Throne while a stealth and magic-movement package can reach another may force the defender to split. The false story must fit observed paths, movement, and incentives. Good opponents do not need certainty to respond; they need a threat whose expected cost is high enough.

Information also imposes attention costs. A hundred unlabelled scouts and reports can make a position harder to understand rather than easier. Networks need roles: border screen, operational depth, strategic nodes, and rear warning. Reports need dates. Old observations must be marked stale. The player must know which provinces going dark matter.

The final advantage is learning speed. Each battle answers questions about scripts, gem use, target selection, and counters. A player who reviews those answers converts losses into future efficiency. A player who watches only whether the green bar won receives almost no information from the same event.

Information is not omniscience. It is the reduction of expensive surprise.

## Essay III: Raiding and Counter-Raiding

Raiding is often described as taking low-defence provinces with small forces. Its deeper purpose is to create an unfavourable allocation problem. A raider costs less than the force that must remain available to stop it, threatens more provinces than the defender can cover, and moves while the main army creates a separate emergency.

The provincial income is only the simplest return. A raider can cut a reinforcement route, stop a lab from pooling gems, interrupt recruitment, isolate a fort, remove a temple, expose retreat into hostile land, or force a combat mage away from the field army. These gains are positional and temporal. A poor province can be the most valuable raid if it breaks a corridor on the decisive turn.

Raider design begins with a target class. A small troop squad may defeat token PD. A light thug may defeat stronger PD and ordinary local recruits. A heavy thug may punish troop-only responses. A stealth army may bypass the line. A teleporter may strike a lab before normal movement. Each class has a ceiling. Calling every geared commander a thug hides the question that matters: what can it beat at its price?

Minimalism creates the favourable exchange. A protection item that changes the PD matchup can be efficient. A fifth defensive item that does not change the likely counter turns the unit into loot. Equipment keeps its value only while the carrier survives; when captured, the swing includes the attacker's loss and the defender's gain. Expected target value, escape probability, and available counters should set the item budget.

Counter-raiding fails when the defender treats every lost province as equally urgent. Chasing a fast raider with the main army abandons the decisive front. Raising heavy PD everywhere can cost more than the raids. Sending an expensive mage after incomplete information can donate another asset.

A layered defence is cheaper. Scouts predict routes. PD tripwires defeat the smallest attacks and reveal larger ones. Forts preserve recruitment. Local commanders retake empty land. Mobile specialists cover labs, Thrones, and junctions. Magic-phase counters threaten raiders that ordinary armies cannot catch. The strategic reserve does not chase; it occupies a node from which several valuable provinces are protected.

The defender should also attack the raid's support. A stealth force may need a commander route, a laboratory for magic escape, or a predictable safe province. A thug may depend on one irreplaceable item factory. A remote attacker may expose a high-path caster and gem stock. Counter-raiding becomes counteroffence when it removes the infrastructure that makes repeated raids possible.

Raiding succeeds when it is connected to the campaign. Provinces taken at random are noise. Provinces taken while a fort is being cracked can prevent relief. A raider that forces the only counter-mage away may let the main army win. A raid that captures a Throne can change the victory threshold without destroying an army.

The mature contest is not province against province. It is response cost against threat cost, repeated until one side can no longer cover the map.

## Essay IV: Siege as a Strategic Clock

A fort does not make a province invulnerable. It buys time, preserves an interior, and changes the sequence required to convert field victory into ownership. That sequence is the siege clock.

The attacker first has to reach the province and defeat whatever remains outside. Wall reduction then compares Strength-squared contribution against repair. Only armies maintaining the siege contribute. Once walls reach zero, the attacker must issue a storm order and win the gate battle. Relief can occur first. The same mages may fight several times, spend gems, lose commanders, and enter the storm with a script designed for a different battlefield.

Each turn of delay creates room to act. The defender can finish research, move relief, cast remotes, recruit elsewhere, negotiate assistance, or counterattack another Throne. The attacker pays upkeep, supply, attention, and exposure. A fort's value is not only its wall number. It is also the number of hostile deadlines that pass while the walls remain.

Siege strength converts troop composition into tempo. High-Strength and flying units can reduce enormous walls quickly. Mindless, Animal, and Undisciplined penalties can make a visually vast army unexpectedly slow. An army optimised only for field battle may spend months outside a cheap fort. A smaller army with specialised siege bodies may convert victories before the political situation changes.

The defender also converts bodies into time. Cheap units can repair. Intrinsic guards strengthen the storm. Mages inside remain able to research or prepare while the fort holds, but declining supplies create an attrition clock in the opposite direction. A capital packed with irreplaceable living mages cannot wait indefinitely if starvation and disease begin.

Relief creates the siege's most dangerous turn. If the defender breaks the besieger outside, the storm is cancelled. If relief fails, it may still consume attack gems and kill siege commanders before the gate. The attacker must decide whether one script can survive several combats and whether gem loads cover the full chain. The defender must decide whether the relief force is buying victory, delay, or merely a cheap gem burn.

Throne forts expose the clock's endgame importance. A one-turn crack can reduce coalition reaction to a single cycle. A force that requires two turns may allow every surviving nation to move, forge, assassinate, and attack the rusher's existing points. Wall strength is then not local defence; it is world reaction time.

Siege strategy should be planned backwards from the storm and forward from the relief. How many turns can the larger game afford? Which assets are trapped? What counterstroke becomes possible during delay? A fort has fulfilled its role when the time it creates is converted, even if the walls eventually fall.

## Essay V: Timing Attacks and Power Spikes

Power is relative and temporary. A nation may have a stronger endgame and still die before reaching it. Another may dominate the first year with an awake expander and lose once opponents acquire armour-negating magic. Strategy identifies the interval when a package produces more usable force than rivals can answer and converts that interval before it closes.

A power spike can come from awakening, research, recruitment scale, a forged booster, a summon, a global, a treaty expiry, or an opponent's losses. The visible event is rarely sufficient by itself. Completing a battlefield enchantment does nothing if troops have not assembled, gems remain in the capital, and mages need three turns to walk to the front.

Preparation must begin before research completes. Recruit the line that the spell will protect. Forge the boosters that create legal casters. Place scouts on the target. Begin the NAP countdown. Move siege bodies and claimants. Accumulate enough gems for the operation and the response. The spike begins when the whole package can act, not when one school reaches a number.

Relative timing also includes counters. A mass protection spell may dominate mundane armies for several turns and become ordinary once armour-piercing evocations or battlefield control appear. A sacred rush may exploit neighbours who spent design points on scales and imprisonment, then face awake gods and deeper research later. The attack's deadline is the earliest likely answer, not the player's preferred calendar.

Good timing attacks produce a conversion that persists after the window. They take forts, destroy irreplaceable cadres, seize Thrones, or force treaties. Merely winning peripheral battles allows the defender to survive until the counter arrives. The objective should be the asset whose loss prevents recovery.

There is also a defensive spike. A nation under attack may be two turns from a cheap resistance spell, a communion threshold, or an awakened Pretender. Elastic defence can surrender land to preserve those turns. The invader's strongest play is often to force the decisive battle before the threshold; the defender's strongest is to make every route consume time.

Not every spike should be used for war. Visible capacity can deter and create favourable treaties. A global or research lead can improve economy more safely than conquest. The comparison is between what the window can gain through attack and what it can compound through peace.

The essential habit is to date power. “This army is strong” is not a plan. “This package can crack the border fort on turn 25, before the likely counter on turn 28, and hold the captured lab” is strategic reasoning.

## Essay VI: The Diplomacy of Threat

Diplomacy in Dominions is not separate from military power. It determines how much power must be held idle, where armies can move, which gems become accessible through trade, and how quickly a leader faces a coalition. The central diplomatic object is the credible threat.

A threat has capacity, communication, and an off-ramp. Capacity means the stated consequence can actually occur. Communication means the target understands the condition and deadline. The off-ramp gives the target a cheaper action than defiance. Without capacity, the threat is noise. Without clarity, it produces fear without control. Without an achievable exit, it becomes war.

NAPs formalise some of this uncertainty. Dominions 6 can mechanically enforce them, but engine enforcement cannot answer every social question. Remotes, stealth staging, dominion pressure, harmful globals, third-party access, and victory emergencies create conduct that may be legal in code and unacceptable under a group's expectations. Clear doctrine prevents disagreement from becoming the most destructive event in a months-long game.

Treaties purchase time. That time should have a named use: research, a war on another front, fort construction, recovery, or a throne operation. A NAP with no purpose can allow a stronger neighbour to compound more efficiently than the beneficiary. Long commitments also reduce the table's ability to respond to victory. Their duration must be compared with plausible throne windows.

Reputation is stored diplomatic capacity. A player known to deliver trades and follow written countdowns can create agreements with fewer guarantees. A player known for exploiting ambiguity forces neighbours to hold armies and refuse valuable exchanges. Betrayal may occasionally be strategically decisive, but its full price includes future games and coalition response, not only the current province.

Leaders face a different problem. Strength attracts balancing. Oppressive globals, rapid eliminations, hidden throne progress, or permanent treaty blocs can make every other nation safer by cooperating. A leader should convert strength quickly enough that the coalition cannot form, or behave in ways that keep rivals divided without making promises that destroy credibility.

Weaker nations possess leverage because their collapse redistributes territory, Thrones, and fronts. They can offer information, gems, access, or coordinated resistance. They can also choose which rival benefits from conquest. This is not unlimited power, but it means diplomacy does not end when the army graph falls.

The diplomacy of threat is ultimately the management of expected futures. Every treaty, warning, trade, and coalition message changes what other players believe will happen if they choose one branch. The most efficient military victory is the one a credible threat secures without spending the army.

## Essay VII: Recovery and Elastic Defence

Defeat creates a dangerous illusion of total collapse. The missing army is immediately visible; surviving research, forts, gems, diplomatic value, and enemy exposure are less vivid. Recovery begins by measuring what remains.

The first objective is capacity. Territory can be retaken if forts still recruit the mages that define the nation. Troops can be rebuilt if command survives. Gems can become a new counter if laboratories remain. A panicked counterattack that loses the surviving cadre turns a reversible battle loss into structural defeat.

Elastic defence uses space to buy the time needed for a different exchange. Poor provinces are allowed to fall. PD reveals movement. Forts interrupt advance. Scouts identify whether the attacker concentrates or disperses. Raiders enter the rear. A research pivot matures behind the line. The defender chooses a shorter perimeter while the attacker acquires a longer supply and reinforcement problem.

This approach works because field victory creates commitments. The attacker must siege or bypass forts, protect captured labs, cover retreats, and decide how much force to leave behind. If it concentrates, raiders can recover provinces. If it disperses, a surviving reserve can defeat pieces. If it storms repeatedly, gems and commanders are exposed. The defender's purpose is to make every further gain cost more time than the attacker budgeted.

Recovery also changes diplomacy. Neighbours may fear the attacker more after a major victory. Exact reports of the winning army, its spent gems, and revealed scripts are valuable coalition information. A weakened nation can offer access or intelligence that a bystander could not obtain alone. The diplomatic position may improve while the military graph worsens.

The counterstroke should target dependency rather than colour. Destroy the army's lab, cut its retreat, assassinate the leader carrying most troops, relieve the key mage fort, or take a Throne elsewhere. Retaking every low-value province can wait. The goal is to remove the opponent's initiative.

Some positions cannot recover. The same discipline still matters. A final defence can delay a throne leader, transfer useful information under the rules, or create time for a substitute. Silent staling damages the competitive structure and removes strategic choices from everyone.

Elastic defence is not an excuse for indecision. It is a controlled exchange of land for the one resource a defeated nation most needs: a future turn in which the answer exists.

## Essay VIII: The Throne Race

Thrones transform Dominions from a war of unlimited conquest into a contest of conversion. A nation does not need to defeat every army or own most provinces. It needs to own and claim the configured number of Ascension Points at the relevant hosting step.

This makes arithmetic a strategic skill. Current claimed points are only the visible baseline. Controlled but unclaimed Thrones, H3 movement, one-turn-crack forts, magic-phase reach, and Cataclysm can change the threshold within several turns. A nation that appears three points short may already control a three-point Throne. A nation at the threshold can be stopped by unclaiming one existing point before the new claim resolves.

Throne defence differs from ordinary border defence. A Throne province has discontinuous value because losing the wrong one can end the game. Its fort walls measure coalition reaction time. A one-turn crack may leave only one cycle for remote attacks, relief, claimant assassination, or a counterattack on another Throne.

The attacker must prepare for more than the storm. Bystanders who ignored a conventional war may unite when victory becomes visible. Magic-phase probes can consume gems before the relief and gate battle. Assassins can remove the claimant or commanders whose squads are needed to storm. Existing Thrones become counterattack targets. The winning operation needs redundancy, secrecy, siege, combat, claimant access, and defence at once.

The defender should resist local fixation. Saving the targeted Throne may be impossible. Cracking one of the attacker's owned Throne forts can change the arithmetic faster. Killing the claimant can buy a turn. Cutting a route can strand H3 access after the army wins. Coalition members should assign tasks by reach rather than all sending armies toward the same province too late.

Diplomacy changes near victory. Many communities treat an imminent throne win as superseding ordinary NAP expectations; formal binding systems may still constrain actions unless a victory clause was agreed. Games should resolve this before play, because a rule intended to create peace can otherwise make a legal response impossible.

Cataclysm adds a moving target. As Thrones disappear, required points decline and surviving points gain value. A long plan can become irrelevant between order and resolution. Endgame arithmetic must be recalculated every turn.

The throne race rewards preparation disguised as ordinary strength. The best rush becomes obvious only when the response window is already closing.

## Essay IX: Why the AI Behaves as It Does

The Dominions AI plays the same fundamental economy, recruitment, movement, battle, magic, and victory systems, but it does not possess human political reasoning. It receives programmed priorities, complete province-ownership knowledge, and difficulty bonuses rather than intuition or social memory.

This distinction explains both pressure and predictability. At high difficulty, large bonuses to gold, resources, recruitment points, and magic income can create armies and magical output that a human position could not match from the same land. The AI can build forts, recruit national troops, cast high-level rituals and globals, and Dispel. It is not passive. Its threat comes from production and broad action.

What it lacks is the full human model of intention. A human may conceal a research spike, accept a poor local exchange to win a Throne elsewhere, or maintain a treaty because reputation across future games matters. Human coalitions can distribute tasks and share exact enemy scripts. The AI's decisions are bounded by the behaviours its evaluation can express.

Patch corrections matter. An old report that the AI repeatedly attempts rituals without a lab or assigns non-priests to preach no longer describes current 6.36 behaviour where those errors have been corrected. AI strategy must be evaluated by version rather than inherited folklore.

Difficulty also changes what a practice game teaches. Impossible pressure trains emergency defence and efficient battle magic, but its economic ratios are not a fair benchmark for human expansion. Normal difficulty better exposes whether the player's first fort, recruitment, and research produce a sound state. Both have value when their purpose is explicit.

Players can defeat predictable behaviour through loops that teach little. Better practice keeps scouts, legal Throne arithmetic, layered defence, gem budgets, and realistic no-reload consequences. The aim is to rehearse a full national campaign, not only discover one weakness in target selection.

The AI is best understood as an active strategic environment with asymmetric advantages and bounded judgment. It is capable enough to punish weak fundamentals and broad enough to expose players to many spells and rosters. It is not a substitute for the social, deceptive, and adaptive layer of multiplayer.

# Sources and Open Questions

## Principal sources

- Illwinter, *Dominions 6 Manual*, revision 2, especially game settings, scouting, movement, patrol, stealth, raid, pillage, assassination, siege, diplomacy, Thrones, Cataclysm, AI, and hosting sequence.
- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html).
- [Illwinter Dominions 6 changes and new features](https://www.illwinter.com/dom6/changes.html).
- [Illwinter home page and current release record](https://www.illwinter.com/).
- [Official Dominions 6.36 announcement](https://steamcommunity.com/games/2511500/announcements/detail/693143486970465344).
- [Official Dominions 6.35 release note](https://store.steampowered.com/news/app/2511500/view/679624547358474861).
- [Official Dominions 6.30 announcement](https://steamcommunity.com/games/2511500/announcements/detail/516348030198220655).
- Supplied `DomEnhanced2_16.dm`.
- Supplied `Divinitus_1.15.3_DE.dm`.

## Community doctrine and test references

- [Naaira's Expansion Guide](https://illwiki.com/dom5/naaira-expansion-guide), used for the repeat-to-turn-12 expansion-testing method.
- [Cybertron2's Guide to Expansion, Part 1](https://illwiki.com/dom5/dom6/guides_and_player_improvement/cybertron2-s_guide_to_expansion/part1_types_of_units), used for current Dominions 6 expansion-role and mage-support discussion.
- [Cybertron2's Guide to Expansion, Part 3](https://illwiki.com/dom5/dom6/guides_and_player_improvement/cybertron2-s_guide_to_expansion/part_3_assorted_concepts), used for frontage and expansion analysis.
- [Building Thugs and Supercombatants](https://illwiki.com/dom5/dom6/guides_and_player_improvement/strategy_articles/thugs), used for contemporary role, efficiency, defensive-layer, and counter-thug doctrine.
- [NAPS: a rundown and two formal doctrines](https://illwiki.com/dom5/dom6/naps), used to document community ambiguity and explicit treaty conventions.
- [Siege](https://illwiki.com/dom5/siege), used for community-documented messages and operational edge cases that remain assigned to tests.
- [Owl's Mini-Guide to Throne Rushes](https://illwiki.com/dom5/owl-mini-guide-thronerush), used for the T+0 to T+3 operational model and coalition-response doctrine.
- [Dominions 6 Thrones](https://illwiki.com/dom5/dom6/thrones), used as a current community object reference and to identify Cataclysm and identity questions requiring current-game verification.

Community sources supply doctrine, hypotheses, and test candidates. They do not override the current manual or official update notes. Where a community page is inherited from Dominions 5, only system-level reasoning consistent with Dominions 6 is retained, and exact claims remain marked for reproduction.

## Open questions

Current-game tests or resolved data are still needed for:

- exact movement-interception probability and battle location in hostile swaps;
- full rounding and combination rules for movement and siege modifiers;
- current patrol-detection distributions under every unit modifier;
- all Raid and pillage output functions;
- exact bodyguard, Patience, surprise, and mounted-assassination distributions;
- every binding-NAP edge case under all diplomacy settings;
- complete current Throne identity and object-effect data;
- final Cataclysm outcome wording and current horror interaction;
- AI decision weights, target priorities, and diplomacy evaluation;
- current effective strategy objects under the DE 2.16 then Divinitus 1.15.3 DE layer;
- nation-specific expansion, research, war, raid, and throne packages.

These remain explicit research tasks. Nation dossiers can still use the campaign method as long as their local assumptions are stated.
