# Foundation Book VII: Nations

## The Nation Dossier Method, Middle Age Arcoscephale, Marignon, Pyrène, Ulm, Man, Abysia, Pythium, Eriu, Agartha, Uruk, Ashdod, T'ien Ch'i, and Machaka

## What a nation dossier should do

A nation guide should do more than name strong units and recommend a research queue. It should explain how a nation turns its starting roster into a functioning state, how that state changes when research arrives, how its plans fail, and how to rebuild those plans when the ruleset changes.

This volume of the nation library does two jobs:

- establish a reproducible method for every later nation dossier;
- apply that method to **Middle Age Arcoscephale, the Old Kingdom**, **Middle Age Marignon, Fiery Justice**, **Middle Age Pyrène, Time of the Akelarre**, **Middle Age Ulm, Forges of Ulm**, **Middle Age Man, Tower of Avalon**, **Middle Age Abysia, Blood and Fire**, **Middle Age Pythium, Emerald Empire**, **Middle Age Eriu, Last of the Tuatha**, **Middle Age Agartha, Golem Cult**, **Middle Age Uruk, City States**, **Middle Age Ashdod, Reign of the Anakim**, **Middle Age T'ien Ch'i, Imperial Bureaucracy**, and **Middle Age Machaka, Reign of Sorcerors**.

It offers a safe first route through the roster and opening, but it also follows the harder questions of mage probability, force packages, path access, counters, logistics, and opportunity cost. There is no single build detached from map, opponents, settings, and patch. The dossier instead presents several coherent strategic families and the conditions that favour each one.

## Edition note

Book I defines the common 6.36 live baseline and evidence terms. The dossiers' structured object comparisons remain pinned to their stated 6.35 snapshot. Unmodded rules, DE 2.16, Divinitus 1.15.3 DE, and the combined load order stay visibly separate. Book IX owns the general mod catalogue; Book VII applies it to individual nations.

## How to use this dossier

The one-page brief, roster, expansion plan, mage roles, research branches, army packages, and turn checklists form the practical core. Probability portfolios, communion failure analysis, access ladders, matchups, reserves, and controlled tests provide the expert layer. Each nation chapter begins again from its own ruleset and evidence label; advice from one dossier should not be carried into another merely because both are Middle Age nations.

# Part I: The Nation Dossier Method

## What a complete nation guide must answer

A useful dossier answers twelve questions.

| Question | Required evidence |
| --- | --- |
| What is the nation trying to convert? | National summary, roster, magic, economy |
| What wins neutral expansion? | Unit statistics, formations, repeated tests |
| What prevents an early defeat? | Neighbour analysis, reachable research, reserve plan |
| What does each fort recruit? | Commander costs, recruitment points, role demand |
| What does each mage random actually enable? | Exact random scheme and probability |
| Which research creates deployable packages? | Spells, paths, gems, mage-turns, delivery |
| Which paths are native, bootstrapped, or Pretender-dependent? | Access ladder with every step named |
| How does the nation fight different defence classes? | Armour, numbers, elites, giants, ethereal, undead, magic resistance |
| How does it raid, defend, siege, and claim? | Movement, leadership, magic, siege strength, priests |
| What information does it possess or lack? | Scouts, spies, scrying, remote spells, battle evidence |
| Which Pretender family solves the actual constraint? | Legal design, scales, timing, bless and ritual jobs |
| What changes under each mod? | Source diff, load order, combined test |

If one answer is missing, the guide should say so. Concealing uncertainty creates a brittle strategy.

## The four layers of a nation

Every nation should be analysed in four layers.

| Layer | Contents | Common mistake |
| --- | --- | --- |
| Rules | Roster, paths, costs, sites, spells, dominion, buildings | Repeating obsolete data |
| Capacity | What can be recruited, researched, forged, and delivered | Treating theoretical access as immediate access |
| Doctrine | How the capacities can be combined | Presenting one context-dependent plan as law |
| Evidence | Tests, replays, probability, and source records | Treating an anecdotal win as proof |

The rules layer is descriptive. Capacity is conditional: an E2S1 mage does not automatically equal an E2S2 ritual caster; the necessary item, gems, laboratory, and forge turn must exist. Doctrine is comparative: one package is chosen because it fits an enemy, a deadline, and an economy. Evidence determines confidence.

## The national conversion chain

The central dossier model is:

```text
scales and starting assets
-> expansion and borders
-> forts and recruitment
-> mage distribution
-> research and gems
-> battlefield or ritual packages
-> positional gains
-> siege, Throne claim, and victory
```

A nation can fail at any arrow. Strong troops may expand but consume so many resources that the second fort cannot recruit. Broad magic may remain a collection of low paths if no communion or booster plan exists. A devastating battlefield spell may arrive without the troops, gems, or movement needed to exploit it. A winning army may lack siege or claim capacity.

Each nation chapter records both **assets** and **conversions**.

## The national identity statement

A national identity statement should be one paragraph, not a slogan. It should name:

- the reliable early force;
- the recruitment bottleneck;
- the magic engine;
- the information advantage;
- the main strategic transition;
- the principal vulnerabilities.

An identity statement is a starting hypothesis. It must be revised when a patch or mod changes one of those elements.

## Roster analysis by job

Units should first be grouped by job, then compared by statistics.

| Job | Questions |
| --- | --- |
| Screen | How cheaply can it absorb missiles, charges, and first contact? |
| Line | What ordinary damage can it resist, and how long before fatigue defeats it? |
| Damage | What armour, size, defence, or resistance class can it kill? |
| Flank | Can it reach exposed mages or force the enemy to deploy wider? |
| Trampler | What sizes can it trample, and how are morale and magic resistance protected? |
| Sacred | Is the unit scarce, cap-only, resource-heavy, or massable? |
| Siege body | What wall damage, supply use, and opportunity cost does it impose? |
| Raider | Which Province Defence and local recruits can it beat reliably? |
| Bodyguard | What assassination, arrow, or flying threat does it prevent? |

“Elite” is not a job. “High protection” is not a complete evaluation. A high-protection unit with low combat speed, high encumbrance, and ordinary damage may be an excellent anvil and a poor pursuit force.

## Commander analysis by constrained turn

Commanders compete for recruitment capacity. Their gold cost is only one part of the decision.

For every commander, record:

- commander recruitment-point cost;
- fort and terrain restrictions;
- leadership types and limits;
- research;
- priest level;
- magic and randoms;
- strategic abilities;
- likely monthly orders;
- what is delayed when this commander is recruited.

A capital-only four-point mage has a different strategic cost from a one-point scout even if sufficient gold exists for both. Nation plans should budget **fort-turns**, **capital-turns**, and **commander points** as explicitly as gold.

## Magic access as a probability portfolio

Random paths are not a list of possible maxima. They are a distribution.

For every random mage, the dossier should record:

- fixed paths;
- each random roll and its probability;
- maximum natural paths;
- probability of each important threshold;
- mutually impossible combinations;
- expected recruits needed for a role;
- the effect of bad variance;
- what a Pretender or independent mage can replace.

If a required result occurs with probability \(p\), the probability of seeing at least one result after \(n\) independent recruits is:

\[
P(\text{at least one}) = 1-(1-p)^n
\]

The expected count \(1/p\) is not a guarantee. A one-in-eight specialist has about a 65.6% chance to appear within eight recruits, not certainty. It takes twenty-three recruits to exceed a 95% chance:

\[
1-(7/8)^{23} \approx 95.4\%
\]

This distinction matters when the first war arrives before the desired random.

## Native, bootstrapped, and imported access

Every path claim belongs in one of four classes.

| Class | Meaning |
| --- | --- |
| Native | A normal national recruit can perform the job without external help |
| Boosted native | A national recruit can perform it with named items or self-buffs |
| Bootstrapped | An earlier summon, transformation, empowerment, or national event creates access |
| Imported | A Pretender, hero, independent, mercenary, Throne, site, or ally provides access |

The access ledger must name every bridge. “Arcoscephale can cast a Death ritual” is incomplete if it actually means “a rare Nature hero forges or casts into a summon chain that eventually produces Death.”

## Research as response trees

A fixed research queue assumes the enemy and map will cooperate. A response tree has:

- a **trunk** of broadly useful early research;
- **branches** for observed threats;
- **conversion nodes** where research becomes a fieldable package;
- **rejoin points** so emergency research does not permanently destroy the long plan.

Every node should specify:

- school and level;
- spell or item obtained;
- eligible caster;
- required communion, booster, or self-buff;
- gem load;
- troop or target interaction;
- operational delivery;
- counters;
- what the research delays.

## Army packages, not spell lists

An army package is:

```text
troops + commanders + mages + scripts + gems + formation
+ movement route + retreat route + replacement plan
```

A spell becomes strategy only when the nation can put the correct caster, protection, gems, and targets in the same battle.

Each package should have:

- **purpose:** what defence or target it defeats;
- **minimum core:** the smallest robust version;
- **scaling rule:** what to add as the enemy grows;
- **failure branch:** what happens if the script is interrupted;
- **counter warning:** the most economical answer available to the enemy;
- **replacement cost:** how quickly the nation can field another.

## Matchup classification

Nation-versus-nation memorisation becomes obsolete quickly. Defence classes are more durable.

| Enemy class | Questions |
| --- | --- |
| Massed light troops | Can the nation kill squares faster than it is surrounded? |
| Heavy armour | Is damage high enough, or is armour destruction available? |
| High defence and glamour | Are attack buffs, area effects, or sight effects available? |
| Giants and elite sacreds | Can control, fatigue, armour-negating damage, or mass be delivered? |
| Undead and demons | Are priests, magic weapons, banishment, morale, and resistance adequate? |
| Flyers and cavalry | Is the rear protected and the line deep enough? |
| Tramplers | Can size, body-blocking, control, and morale attacks stop them? |
| Battle-mage mass | Can the nation disperse, interrupt, resist, or strike first? |
| Thugs and supercombatants | Can the chassis be controlled, exhausted, penetrated, or ignored? |
| Remote and stealth warfare | Are domes, patrols, redundant labs, and reserves in place? |

Specific opponents can then be placed into one or more classes.

## Pretender families

A dossier should present families, not copied designs:

- **awake expansion:** buys early territory and deterrence;
- **dormant intervention:** appears for the first war or path bridge;
- **imprisoned scales:** maximises the recruitable state;
- **bless support:** improves a sacred unit that can be recruited in relevant numbers;
- **ritual bridge:** supplies paths the national roster cannot reach;
- **hybrid:** deliberately performs two of these jobs at a real cost to each.

Every proposed build must pass five audits:

1. legality in the exact version and mod order;
2. expansion or survival job;
3. scales and recruitment compatibility;
4. mid-game job on awakening;
5. unique late-game access that cannot be bought more cheaply elsewhere.

## Verification standard

Nation claims are verified in this order:

1. official manual or current official data;
2. current structured object data;
3. supplied mod source;
4. controlled game test;
5. detailed community evidence;
6. strategic inference.

The source hierarchy does not make community strategy unimportant. It prevents strategic experience from being confused with engine definition.

## Minimum controlled-test suite

Every nation eventually receives:

- three or more turn-12 expansion runs for each serious Pretender family;
- controlled battles against the main independent types;
- random-mage sampling large enough to detect transcription errors;
- communion fatigue and script tests;
- a research timing test with realistic infrastructure;
- siege and storm tests;
- representative matchups against armour, elites, undead, flyers, tramplers, and magic;
- modded repetitions under each supported load order;
- a save, turn number, settings record, result table, and replay note.

Until those tests are recorded, precise party sizes and timing claims remain hypotheses.

# Part II: Middle Age Arcoscephale, the Old Kingdom

## The one-page national brief

Middle Age Arcoscephale is a human combined-arms nation whose ordinary military is old-fashioned but broad: inexpensive formation infantry, armoured spear lines, chariots, elephants, and a small capital sacred. Its strategic engine is a network of recruit-anywhere Mystics backed by capital Astrologers, priestess-healers, and automatic scrying inside friendly dominion.

The nation converts gold into versatile S1 elemental mages, those mages into communions or independent specialist casters, and research into an adaptable battlefield. It is strongest when intelligence identifies the defence to defeat before the army is scripted. It is weakest when expensive human mages are caught unprotected, when tramplers are exposed to morale or magic-resistance attacks, when heavy infantry is exhausted, or when random-path variance prevents a required specialist from arriving on time.

### National profile

| Feature | Unmodded Dominions 6.35 |
| --- | --- |
| Race | Humans |
| Military | Heavy spear infantry, chariots, elephants |
| Recruitable magic | Astral, Fire, Water, Earth; some Nature |
| Priests | H1 and H2 priestess-healers |
| Dominion | Accurate automatic military reports inside dominion |
| Scale limit | Order limit +1 |
| Forts | Standard |
| Laboratories | 300 gold |
| Capital income | 1 Nature gem and 4 Astral pearls per month |
| Central constraint | Gold- and mage-turn-intensive magical state |
| Central advantage | Information plus highly adaptable recruit-anywhere magic |

## Lore and strategic meaning

The Old Kingdom is intentionally archaic. Its armies retain cumbersome armour, long spears, chariots, and war elephants while ancient Astrologers return to guide the realm. This is not only flavour. The roster juxtaposes slow, reliable formation troops with volatile tramplers, while the mage corps juxtaposes broad low-level access with capital astral depth.

Three strategic themes follow.

First, **knowledge precedes commitment**. Automatic scrying inside dominion and Astrologers who read the heavens support a nation that should know what is approaching before choosing a script.

Second, **the old army needs magical renewal**. The troops can expand and hold ground, but armour, fatigue, morale, large targets, and elite opposition eventually require tailored magic.

Third, **restoration is cumulative**. Arcoscephale becomes stronger as forts produce Mystics, research broadens, boosters accumulate, and communions scale. Losing a mage core or capital does more than remove units; it breaks the conversion chain.

## National special features

### Automatic dominion scrying

**Official:** provinces inside Arcoscephale's dominion receive accurate automatic military reports. Current structured data also identifies this scrying as capable of revealing glamoured units, and disciple partners receive the information.

This is a strategic advantage, not omniscience.

It helps with:

- army size and composition near the interior;
- early warning against ordinary movement;
- more informed deployment of elephants, communions, and counters;
- identifying when a border force has split;
- tracking glamoured forces that ordinary reports may conceal.

It does not replace:

- scouts beyond dominion;
- spies for income, unrest, Province Defence, and deeper provincial information;
- battle replays for scripts, gems, and exact spell use;
- patrols against stealth;
- caution against magic movement, assassinations, remote attacks, and simultaneous orders.

The correct doctrine is a layered network:

1. scouts beyond the border;
2. dominion scrying across owned approaches;
3. reserve mages at central laboratories;
4. battle reports converted into response scripts.

### Order limit +1

The nation can take one more step toward Order than an ordinary nation. This is not an instruction to maximise Order in every design. It is an option to support:

- expensive Mystics and Astrologers;
- fort and laboratory construction;
- elephant and chariot recruitment;
- larger mundane armies;
- reduced dependence on risky event income.

The scale must be evaluated against the Pretender family and opportunity cost. A high-Order scales design and an awake expander solve different problems.

### Healing

Hiereiai have Healing 1. Archousai have Healing 3.

**Official rule:** a healer automatically attempts to cure a number of afflictions up to the value of the ability in the same province each turn. Healing is a provincial capacity. It does not guarantee that the exact desired affliction on the exact desired unit disappears immediately.

Healing improves the expected service life of:

- expensive commanders;
- Astrologers;
- battle-wounded Mystics;
- a combat Pretender that can be healed;
- surviving elephants and sacreds;
- thugs and summoned commanders without healing restrictions.

Healing does not make reckless attacks efficient. Dead units cannot be healed, some beings have special restrictions, and cursed-item afflictions require removal of the item first.

## Recruitable commander roster

The following table is the official revision-2 unmodded roster. `Rec` is commander recruitment-point cost.

| Commander | Gold | Res | Rec | Principal attributes and role |
| --- | ---: | ---: | ---: | --- |
| Scout | 35 | 5 | 1 | Stealth 50, Forest and Mountain Survival; forward intelligence |
| Mounted Commander | 70 | 9 | 1 | Leadership 75, Map Move 16; fast transport for compatible forces |
| Hypaspist Commander | 95 | 25 | 1 | Leadership 100, Protection 15, Defence 14; armoured line commander |
| Hoplite Commander | 105 | 31 | 1 | Leadership 100, Protection 18; slow heavy commander |
| Strategos | 150 | 30 | 2 | Leadership 150, Morale 15; large formations and army command |
| Hiereia | 155 | 1 | 2 | N1H1, Sacred, Healing 1; recruitable outside forts |
| Mystic | 190 | 1 | 2 | S1 plus elemental/astral randoms, Research +1; main national mage |
| Archousa | 235 | 1 | 2 | N1H2, Sacred, Healing 3, Leadership 50 |
| Astrologer | 270 | 1 | 4 | Capital only, S3 plus randoms, Fortune Teller 10; astral specialist |

### Recruitment doctrine

No commander is “free” merely because the treasury can pay for it.

- A **Scout** competes with a leader or mage for the local commander queue.
- A **Strategos** is valuable when leadership quality and army size justify the extra recruitment cost.
- A **Hiereia** can be recruited outside forts, preserving fort mage production while extending temples, healing, supplies, and H1 support.
- A **Mystic** is normally the default fort investment because it produces research and future battlefield flexibility.
- An **Archousa** is a healing and H2 capacity purchase, not a generic researcher.
- An **Astrologer** consumes scarce capital recruitment capacity and should have a defined astral job.

The recurring question is:

> Which missing capacity causes the next failure: intelligence, transport, leadership, religion, healing, research, or high Astral?

## Recruitable troop roster

The official revision-2 values below describe the unmodded units. Mounts and coriders are separate combat entities where applicable.

| Unit | Gold | Res | Rec | Protection | Morale | Combat / map move | Primary role |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Slinger | 7 | 2 | 3 | 5 | 7 | 12 / 14 | Cheap ranged harassment and screening |
| Cardaces | 10 | 8 | 9 | 9 | 10 | 11 / 16 | Cheap formation infantry |
| Peltast | 10 | 5 | 9 | 5 | 10 | 11 / 16 | Mobile spear and javelin screen |
| Hoplite | 13 | 31 | 16 | 18 | 11 | 7 / 14 | Resource-heavy armoured anvil |
| Hypaspist | 16 | 25 | 23 | 15 | 13 | 10 / 16 | Higher-defence, higher-morale heavy infantry |
| Charioteer | 40 | 7 | 9 | 9 | 10 | Rider 12 / 16 | Chariot trampling and mobile missile pressure |
| Elephant Rider | 100 | 3 | 9 | 5 | 8 | Rider 12 / 16 | War-elephant trampling with two archers |
| Heart Companion | 20 | 31 | 23 | 18 | 13 | 8 / 14 | Capital-only sacred heavy spear infantry |

### Mounts

| Mount | HP | Prot | MR | Morale | Combat / map move | Role and risk |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| Riding Horse | 18 | 3 | 5 | 7 | 26 / 22 | Gives the Mounted Commander strategic and tactical speed |
| Chariot | 20 | 3 | 5 | 9 | 20 / 20 | Trampling platform; vulnerable if stopped or controlled |
| War Elephant | 64 | 11 | 6 | 9 | 18 / 22 | Large trampler; powerful against smaller bodies, vulnerable to MR and morale pressure |

## Troop roles and comparisons

### Slingers

Slingers are cheap bodies and ranged nuisance fire. Their morale, protection, attack, and defence are poor. They are useful when:

- an inexpensive screen protects a more valuable line;
- mass missiles can punish unshielded or low-protection enemies;
- recruitment resources are scarce;
- siege bodies are urgently required.

They should not be treated as a reliable melee line. A routed slinger mass can contribute to wider morale problems.

### Cardaces

Cardaces are the economical formation body. Protection 9 and Defence 13 are respectable for ten gold and eight resources, but their damage remains that of ordinary human spear infantry.

Use them to:

- add square density and bodies;
- hold ordinary light troops;
- screen elephants or mages;
- fill lines when resources cannot support Hoplites;
- absorb attacks whose damage would waste expensive armour anyway.

Do not ask Cardaces to solve high protection, giants, or elite sacreds without magic.

### Peltasts

Peltasts exchange armour for javelins and low resource cost. They support early contact by throwing before melee and are less resource-constrained than the heavy line.

They are preferable when:

- the target is lightly protected;
- mobility and replacement matter;
- a sacrificial screen is needed;
- a province has gold but poor resources.

They are vulnerable to sustained missiles and decisive melee contact.

### Hoplites

Hoplites bring Protection 18 and long spears at only thirteen gold, but cost thirty-one resources and carry Encumbrance 8, Combat Speed 7, and Map Move 14.

Their favourable fight is a direct clash against ordinary, low- or moderate-damage infantry that must spend time cutting through armour. Their unfavourable fight includes:

- armour-negating or armour-piercing attacks;
- high-strength giants;
- armour destruction;
- prolonged fatigue environments;
- enemies that refuse the front and reach the mages;
- operational races where Map Move 14 is too slow.

Hoplites are an anvil. They need a hammer or a magical answer.

### Hypaspists

Hypaspists cost more gold and recruitment points than Hoplites but save six resources, gain Defence 13, Morale 13, Combat Speed 10, and Map Move 16 while retaining Protection 15.

They are generally better when:

- enemy damage already threatens to penetrate Protection 18;
- defence, morale, and mobility matter more than three protection;
- the army must keep pace with faster elements;
- gold is available but capital or local resources are constrained.

Hoplites are better at absorbing repeated ordinary hits. Hypaspists are a more flexible high-quality line. The choice should be made against an enemy damage profile and the province's resource economy, not by declaring one universally superior.

### Chariots

The chariot package supplies mobility, a trampling mount, and a corider archer. It threatens flanks and lighter units but is less decisive than the elephant against dense small bodies.

Chariots benefit from:

- a screen that prevents premature pinning;
- flank deployment;
- targets lacking large body-blockers;
- magic that improves survival or disrupts the enemy line.

They suffer when:

- surrounded after the charge;
- confronted by large units;
- controlled by magic;
- committed into weapons and buffs designed to punish mounts.

### War elephants

The elephant is Arcoscephale's most dramatic early force and its easiest trap.

Its 64 HP, Protection 11, Size, Combat Speed 18, Map Move 22, and trample can collapse ordinary human formations. The rider and two elephant archers add bodies and attacks, but the elephant's MR 6 and Morale 9 create explicit counter surfaces.

Use elephants as a package:

- a disciplined line or screen absorbs lances and delays contact;
- elephants begin behind or beside the screen rather than alone in front;
- leadership and standards support morale where available;
- the target has been scouted for size, anti-large damage, fear, paralysis, and MR-negates effects;
- a retreat route exists;
- the number committed is large enough to decide contact but not so large that one panic destroys the treasury.

Avoid treating elephants as an answer to:

- giants and other large bodies that cannot be trampled efficiently;
- high-defence elite troops that stop and surround them;
- concentrated fear or morale attacks;
- cheap MR-negates control or killing;
- poison, fatigue, and effects that exploit a large valuable target;
- narrow deployment where they cannot reach useful targets.

### Heart Companions

Heart Companions are capital-only, sacred, heavily armoured spear infantry. They are individually better than Hoplites, but remain Map Move 14 and consume scarce capital resources.

Their scarcity changes bless economics. A bless that exists only to improve a slow, capital-only sacred must be compared with:

- more scales for the entire economy;
- an awake expander;
- missing Death, Air, Glamour, or Blood access;
- a combat or ritual Pretender.

A light incidental bless can add value. A major bless needs a campaign plan that proves the capital can recruit enough Companions without delaying other essential forces.

## Formation doctrine

Arcoscephale's infantry benefits from formation-fighter density, but density has two faces.

It improves:

- concentration of melee attacks;
- the number of armoured bodies holding a frontage;
- the ability to protect mages behind a compact line;
- efficient buff coverage.

It increases exposure to:

- area damage;
- fatigue clouds;
- battlefield-wide debuffs;
- trampling if the enemy is large enough;
- mass routing when a dense formation loses many units quickly.

The default army should not be one dense block. It needs separate functional elements:

- a central anvil;
- one or two flank or trample groups;
- a rear guard against flyers and attack-rear orders;
- mages separated enough to reduce common-area losses;
- spare commanders so one casualty does not strand the army.

# Part III: The Mage State

## Why the Mystic defines the nation

The Mystic is the repeatable national engine:

- recruitable in any fort;
- guaranteed Astral 1;
- one guaranteed random from Fire, Water, Earth, or Astral;
- an independent 50% Fire random;
- an independent 50% Water random;
- an independent 50% Earth random;
- Research +1;
- able to enter Astral communions;
- capable of independent low-level magic even when no communion is appropriate.

The important word is **independent**. The three 50% rolls are separate from the guaranteed four-path random and from each other.

### Mystic random structure

Let:

- \(R\) be one guaranteed uniform roll among F, W, E, and S;
- \(F_b\), \(W_b\), and \(E_b\) be independent 50% bonus rolls.

The final paths are:

```text
S1
+ one level from R
+ F1 if Fb succeeds
+ W1 if Wb succeeds
+ E1 if Eb succeeds
```

There are thirty-two equally likely combinations before any other game effects: four values of \(R\) multiplied by eight combinations of the three binary bonus rolls.

### Mystic threshold probabilities

| Result | Probability | Interpretation |
| --- | ---: | --- |
| F0 / W0 / E0 | 37.5% each | No level in that element |
| F1 / W1 / E1 exactly | 50% each | Useful low-level elemental caster |
| F2 / W2 / E2 | 12.5% each | One-in-eight natural specialist |
| S1 exactly | 75% | Ordinary communion-capable Mystic |
| S2 | 25% | Stronger Astral caster or master |
| Any named element at 1+ | 62.5% | Five in eight |
| Any named pair of elements at 1+ | 37.5% | Example: F1+ and E1+ |
| F, W, and E all at 1+ | 21.875% | Seven in thirty-two |
| Two elemental paths at level 2 | 0% | Mutually impossible from this random scheme |
| E2 and S2 | 0% | Both require the single guaranteed roll |

The last two rows are strategically important. A Mystic can be broad, but the same guaranteed roll cannot create two doubled paths. Plans requiring E2S2 or F2E2 need boosters, empowerment, a Pretender, a hero, or another access source.

### Probability of obtaining a specialist

For a one-in-eight F2, W2, or E2 Mystic:

| Recruits | Chance of at least one |
| ---: | ---: |
| 1 | 12.5% |
| 4 | 41.4% |
| 8 | 65.6% |
| 12 | 79.9% |
| 16 | 88.2% |
| 23 | 95.4% |

**Derived:** the table assumes independent recruitment rolls and uses \(1-(7/8)^n\).

This produces a recruitment rule:

> A one-in-eight random is a portfolio capability, not a deadline-safe capability.

If a war plan requires E2 by a fixed turn, build redundancy, recruit from multiple forts, or provide another route.

## Mystic role classification

Rename or otherwise record Mystics when recruited. A practical classification is:

| Tag | Minimum path | Principal jobs |
| --- | --- | --- |
| `S2` | S2 | Astral master, penetration and Astral scaling |
| `F2` | F2 | Fire specialist, Fire self-buff route, high-damage evocation |
| `W2` | W2 | Water specialist, cold damage, Water buffs, elemental summons |
| `E2` | E2 | Earth specialist, protection, armour destruction, forging and Dragon Teeth |
| `FWE` | F1W1E1 | Broad point buffs, site search, cross-path utility |
| `FE` | F1E1+ | Fire/Earth cross-path and forging candidate |
| `WE` | W1E1+ | Water/Earth cross-path and protection/control candidate |
| `FW` | F1W1+ | Elemental resistance and mixed evocation candidate |
| `S1 utility` | No doubled path | Communion slave, research, low-level Astral and random-specific support |

This is not a permanent caste system. A war can change priorities. The point is to prevent an E2 specialist from spending twenty turns as an anonymous researcher and then being unavailable when armour destruction is required.

## The Astrologer

The capital-only Astrologer has:

- fixed S3;
- one guaranteed random among F, W, E, and S;
- a further 10% random among F, W, E, and S;
- Fortune Teller 10;
- commander recruitment cost 4;
- Research 13 in the current structured data;
- high magical leadership.

### Astrologer probability

Assuming the 10% roll independently chooses one of the four listed paths:

| Astral result | Probability |
| --- | ---: |
| S3 | 73.125% |
| S4 | 26.25% |
| S5 | 0.625% |
| S4 or higher | 26.875% |

For any one element:

| Elemental result | Probability |
| --- | ---: |
| No level | 73.125% |
| Level 1 | 26.25% |
| Level 2 | 0.625% |

**Derived:** these values include the rare 10% random instead of rounding the unit to “one in four S4.”

### Astrologer roles

Astrologers are recruited for jobs that justify capital scarcity:

- reliable S3 master casting;
- S4 or rare S5 ritual and remote-magic thresholds;
- high-Astral penetration;
- a capital communion anchor;
- Fortune Teller concentration;
- eventual high-end Astral rituals and battlefield magic;
- an elemental random that opens a specific Astral cross-path.

An Astrologer should not automatically replace a Mystic as a generic researcher. The capital turn, gold, and recruitment points are the real comparison.

## Priestess-healers

### Hiereia

The Hiereia is N1H1, Healing 1, sacred, and recruitable outside forts.

Her roles include:

- building temples without consuming a fort mage turn;
- blessing sacreds;
- Sermon of Courage and other low-priest support;
- low Nature support;
- provincial healing;
- supply assistance;
- accompanying expansion or siege forces where one affliction recovered matters.

Outside-fort recruitment is a state-building advantage. Provinces without forts can produce religious infrastructure and healing while the forts continue producing Mystics.

### Archousa

The unmodded Archousa is N1H2 with Healing 3 and Leadership 50.

Her roles include:

- stronger healing concentration;
- H2 battle and ritual duties;
- leading a modest army while providing priest support;
- protecting the long-term value of expensive units and commanders.

She is not a substitute for broad Nature magic. Unmodded Arcoscephale's normal recruitable Nature ceiling is N1.

## Recruitment portfolios

### The research-first portfolio

Use when:

- borders are stable;
- the mundane army can deter a rush;
- no urgent H2 or healing deficit exists;
- an early research breakpoint creates the next advantage.

Default:

- most new forts recruit Mystics;
- capital alternates Astrologers and whatever national need is genuinely scarce;
- Hiereiai come from non-fort provinces;
- scouts are scheduled rather than forgotten.

Risk:

- too little mundane leadership;
- mages accumulated in one vulnerable laboratory;
- no reserve army;
- specialist variance arriving late.

### The healing-and-expander portfolio

Use with an awake or dormant combat Pretender and expensive surviving troops.

Add:

- one or more Archousai at recovery hubs;
- Hiereiai following army groups;
- a safe path from battlefront to healing province;
- explicit checks for beings or afflictions that cannot be healed normally.

Risk:

- buying more healing than the casualty pattern warrants;
- delaying the research or Astral depth that prevents the next wounds.

### The communion portfolio

Use when the first war requires path elevation.

Recruit:

- enough Mystics to separate slaves, masters, independent casters, and research;
- S2 or desired elemental masters;
- reserve slaves;
- ordinary leaders and screens that keep mages alive.

Risk:

- every master is counted but slaves are treated as expendable;
- slaves are also required for independent spells;
- shared self-buffs or fatigue kill the slave line;
- one battlefield clear destroys years of research investment.

### The dispersed-reserve portfolio

Use against remote attacks, flyers, raiders, assassins, or fast fronts.

Maintain:

- small mage cells in several laboratories;
- spare pearls and elemental gems at operational hubs;
- scouts on approach routes;
- a mobile ordinary reserve;
- a protected capital core.

Risk:

- insufficient concentration for the decisive battle;
- gems and items stranded in isolated labs;
- scattered mages defeated in detail.

# Part IV: Unmodded Magic Access

## Native access summary

| Path | Repeatable native ceiling | Main source | Important limitation |
| --- | --- | --- | --- |
| Fire | F2 | One-in-eight Mystic | No native high Fire without communion or boosters |
| Air | None | Hero only at A1 | Normal roster cannot use Air |
| Water | W2 | One-in-eight Mystic | High Water requires communion or access chain |
| Earth | E2 | One-in-eight Mystic | E2 and S2 do not occur on the same Mystic |
| Astral | S4 common peak; rare S5 | Astrologer | Capital-only high Astral |
| Death | None | Summons, hero/Pretender routes | Several national rituals are inaccessible initially |
| Nature | N1 | Hiereia and Archousa | N3 hero is chance-dependent |
| Glamour | None | Summon or imported route | No normal national access |
| Blood | None | Deep summon or imported route | No normal Blood economy |
| Holy | H2 | Archousa | H3 normally requires prophet/Pretender or imported access |

“Ceiling” here means a recruitable unit before boosters, empowerment, heroes, or communions. It does not mean that every spell at that level is strategically available; school, gems, range, and battlefield conditions still apply.

## Native battlefield strengths

### Astral

Astral is the stable spine:

- every Mystic can join a communion;
- S2 Mystics and S3+ Astrologers can serve as stronger masters;
- low-level Astral offers ethereal, luck, fatigue, mind, and resistance tools;
- high Astral creates remote and battlefield threats;
- capital pearl income supports early Astral use.

Astral also creates vulnerabilities:

- enemy Astral mages can threaten Magic Duel dynamics;
- communion clusters attract area attacks;
- pearls have competing uses in combat, forging, remote magic, and legendary rituals;
- an Astral plan without penetration can fail against high MR.

### Fire

Fire supplies direct damage and morale pressure. F2 Mystics are natural specialists; F1 Mystics can reach higher levels through a communion or self-buff where available.

Fire is strongest against:

- dense ordinary troops;
- cold-aligned or fire-vulnerable targets;
- formations whose protection is less relevant to the chosen spell.

It is weaker against:

- fire resistance;
- dispersed targets;
- friendly formations too close to inaccurate area fire;
- battles where fatigue and gem use outrun protection.

### Water

Water supplies cold damage, control, quickness and resistance effects, and elemental summons. W2 specialists are one in eight; W1 is common enough to support mixed packages.

Water is especially valuable when:

- the enemy lacks Cold Resistance;
- control and slowing matter more than raw kills;
- a Water/Earth Mystic can combine defensive and fatigue tools;
- summoned elementals can exploit enemy size or formation.

### Earth

Earth renews Arcoscephale's old infantry:

- protection;
- strength;
- armour destruction;
- battlefield control;
- reinvigoration and path elevation;
- constructs and national summons;
- forging.

E2 specialists are among the most important randoms because they can use national Sow Dragon Teeth without ritual access problems and can anchor Earth communions. Earth still does not solve every high-protection fight: the chosen package must specify whether it raises friendly durability, lowers enemy armour, deals high damage, or controls movement.

### Nature

N1 is support, not broad Nature dominance. It provides selected protection, entanglement, poison-related, healing, supply, and small-summon options as research permits.

Without a hero, Pretender, independent, empowerment, or summon chain, the nation does not naturally reach the powerful N3-N5 ritual tier. A guide that assumes easy high Nature is using another age, a mod, or an unrecorded access source.

## Communions

### Why Arcoscephale uses them

Mystics combine guaranteed S1 with heterogeneous elements. A communion:

- raises each master's known paths according to the number of slaves;
- distributes spell fatigue across participants;
- lets low elemental randoms reach battlefield thresholds;
- makes a roster of modest mages behave like a high-path school.

The official level thresholds are:

| Slaves | Master bonus |
| ---: | ---: |
| 2 | +1 |
| 4 | +2 |
| 8 | +3 |
| 16 | +4 |
| 32 | +5 |

The bonus applies only to paths the master already knows.

### The smallest useful communion

Two slaves are enough to raise paths by one. This can turn:

- F2 into F3;
- W2 into W3;
- E2 into E3;
- S2 into S3;
- an Astrologer S3 into S4.

The small communion is efficient for a limited script, but brittle:

- one slave loss can remove the bonus;
- fatigue per slave is higher;
- an overambitious master script can collapse it;
- the master may choose an unintended expensive spell after scripted orders.

### Four- and eight-slave communions

Four slaves provide +2 and are the first general-purpose threshold for turning common F1/W1/E1 Mystics into level 3 casters.

Eight slaves provide +3 and support high-end battlefield effects, but create a large concentration of expensive mages. The cost includes:

- eight researchers leaving laboratories;
- pearls or scripting needed to establish the communion;
- bodyguards and formation space;
- fatigue management;
- risk of battlefield-wide or rear attacks;
- the loss of those mages if the army is trapped.

### Master selection

Choose masters by spell package:

- F2 master for Fire;
- W2 master for Water;
- E2 master for Earth;
- S2 Mystic or S3+ Astrologer for Astral;
- cross-path Mystic when the spell or shared buff genuinely requires it.

Avoid adding masters merely because they can join. Every additional master:

- increases total fatigue placed into the slave pool;
- expands spell-selection variance after scripts;
- raises the value of the target presented to the enemy.

### Slave selection

The cheapest-looking S1 Mystic may still carry a valuable cross-path. Slave selection should preserve:

- rare E2, W2, and F2 specialists;
- S2 masters;
- cross-paths needed for forging or point buffs;
- battlefield-independent casters.

If every Mystic costs the same, “slave” is a temporary assignment, not a low-value unit type.

### Fatigue failure

Official communion fatigue depends on:

- the spell's fatigue cost;
- the number of participants;
- the slave's relevant effective path compared with the master's;
- bonuses and effects included in effective skill;
- the continued number of living slaves.

The dangerous cascade is:

```text
slave becomes exhausted
-> slave stops contributing or dies
-> remaining slaves receive more fatigue
-> master bonus can fall below a threshold
-> later spells become more expensive or illegal
-> communion collapses
```

The package must be tested with the actual master scripts, gems, self-buffs, enemy pressure, and expected battle length.

### When not to use a communion

Communions are not mandatory.

Independent casting is often better when:

- many Mystics can each cast a useful low-level spell;
- the spell does not need path elevation;
- the enemy can punish a mage cluster;
- the battle is small;
- slaves would cost more mage-turns than the target is worth;
- one pearl per independent caster produces more total useful actions;
- the desired mix of spells is easier to control without shared fatigue.

Community discussion of MA Arcoscephale correctly highlights this tradeoff: a Mystic assigned as a slave is not a cheap acolyte; it is a 190-gold researcher and possible specialist that no longer casts independently.

## National spells and rituals

The official unmodded national list contains one battlefield summon and seven rituals.

| Spell or ritual | School | Requirement | Cost | Result | Native access |
| --- | --- | --- | ---: | --- | --- |
| Sow Dragon Teeth | Enchantment 6 | E2 | 1 Earth gem | 10 Spartae in battle | Yes: E2 Mystic |
| Forge Brass Bull | Construction 6 | F3E3 | 25 Fire gems | 1 Khalkotauros | Not on an unboosted recruit |
| Summon Hound of Twilight | Conjuration 5 | E2D1 | 3 Earth gems | 1 Hound of Twilight | No native Death |
| Craft Keledone | Construction 6 | E2S2 | 5 Earth gems | 1 Keledone | No natural E2S2 Mystic |
| Bind Keres | Conjuration 6 | D2 | 12 Death gems | 3 Keres | No native Death |
| Procession of the Underworld | Conjuration 5 | D3 | 13 Death gems | 15 Lampads | No native Death |
| Awaken Hamadryad | Enchantment 5 | N4 | 25 Nature gems | 1 N3 Hamadryad | Hero or imported path route |
| Monster Boar | Conjuration 5 | N3 | 10 Nature gems | Remote unrest monster, range 5 | Hero or imported path route |

### National access is not castability

Five of the eight entries are not immediately castable by the normal recruitable roster. This is deliberate strategic terrain.

- **Sow Dragon Teeth** is the clean native national tool.
- **Craft Keledone** requires bridging the missing point on an E2S1 or another caster.
- **Forge Brass Bull** requires substantial dual-path elevation.
- the Death rituals require imported or bootstrapped Death;
- high Nature depends on a hero, Pretender, independent, empowerment, or another chain.

The dossier separates “the nation owns this ritual” from “the present game can cast it.”

## Path-access ladder

### Fire

1. Recruit Mystics until F1 and F2 roles are available.
2. Use communion bonuses or a Fire self-buff to reach battlefield thresholds.
3. Forge only after confirming the current item path and Construction level.
4. Use Pretender Fire when a ritual requires a dual path the Mystic distribution cannot produce.

### Water

1. Recruit W1 and W2 Mystics.
2. Use Water self-buffs and communions for battlefield scaling.
3. Use booster chains when ritual thresholds require them.
4. Treat very high Water as a deliberate project rather than normal roster access.

### Earth

1. Preserve E2 Mystics.
2. Use Earth self-buffs in battle.
3. Forge Earth boosters when current research and item paths allow.
4. Use E2 to cast Sow Dragon Teeth.
5. Bridge E2S1 to E2S2 for Craft Keledone through a named Astral booster or another caster.

### Astral

1. Every Mystic provides S1.
2. S2 Mystics become stronger masters and forgers.
3. Astrologers provide S3, commonly S4, and rarely S5.
4. Astral boosters extend high rituals and penetration.
5. Communions reach extreme battlefield levels but do not cast ordinary rituals.

### Nature

1. Hiereiai and Archousai provide N1.
2. The national hero Axieros provides N3 if he appears.
3. A single Nature booster can bring N3 to N4 for Awaken Hamadryad, subject to current item legality.
4. Pretender or independent access can make the route reliable.

### Death

1. There is no recruitable national Death.
2. A Pretender is the reliable pregame bridge.
3. Suitable independent mages, sites, heroes, empowerment, or summons can create a later bridge.
4. Once D2 or D3 exists, the national Keres and Lampad rituals can produce units with further magic potential if made commanders by an appropriate current spell.

### Air, Glamour, and Blood

These are absent from the ordinary national roster.

- Air appears on Orokestes at A1, if the hero arrives.
- Glamour and Blood require imported or summon-chain access.
- A Pretender taking one of these paths should have a clear job beyond merely making the national summary look broad.

# Part V: Expansion and the First Year

## Expansion objectives

Arcoscephalian expansion is successful when it produces:

- enough provinces to finance multiple forts and laboratories;
- resource provinces that let those forts recruit the intended line;
- surviving elephants, infantry, and commanders;
- a border that automatic scrying can help cover;
- an early fort schedule that begins multiplying Mystics;
- a credible force against opportunistic neighbours.

Province count alone is insufficient. Eight disconnected or exposed provinces with no second fort can be weaker than six provinces with a defensible boundary and a fort already building.

## Starting force

Unmodded Arcoscephale begins with:

- a Hypaspist Commander;
- a Scout;
- twenty Peltasts;
- twenty Hoplites.

The starting army already contains a screen and an armoured line. It can take suitable human infantry provinces, but the correct first target depends on the actual report. Heavy cavalry, barbarians, crossbows, large numbers, and other high-damage independents can convert the expensive Hoplite line into an early setback.

### Starting formation hypothesis

**Strategic doctrine, test pending:**

- Hoplites form the central or forward anvil.
- Peltasts begin slightly behind or on a flank so javelins do not disrupt the first contact.
- The commander remains protected and away from the most likely projectile path.
- Orders and distance are adjusted to make the two lines contact in a useful sequence.

This is a starting point for testing, not a universal script. Battlefield terrain, enemy placement, and projectile range alter the timing.

## Expansion engines

### Heavy-infantry expansion

**Core:** Hoplites or Hypaspists with a proper commander and a cheaper supporting line.

Strengths:

- little dependence on Pretender awakening;
- good against ordinary low-damage infantry;
- survivors retain value in the first war;
- predictable morale and formation.

Weaknesses:

- high resource demand;
- slow map movement for Hoplites;
- attrition from high-damage attacks;
- limited killing speed against dense or armoured enemies;
- replacement can delay infrastructure.

### Elephant expansion

**Core:** a small number of elephants behind or beside an infantry screen.

Strengths:

- high shock and trample output against smaller human troops;
- fast strategic movement from the mount;
- low resource cost on the rider listing;
- strong deterrent against opponents without prepared counters.

Weaknesses:

- 100 gold per recruit;
- low mount MR and ordinary morale;
- catastrophic losses against control, fear, giants, and anti-large force;
- routs can trample friendly troops;
- a single bad expansion can delay a fort.

The correct number is empirical. It varies with independent strength, screen size, bless, leadership, target composition, and map. The library will not print a “safe” elephant count until repeated tests establish a range under the frozen settings.

### Chariot expansion

**Core:** chariots on a flank with a centre that holds the enemy.

Strengths:

- cheaper than elephants;
- multiple package elements through rider, corider, and mount;
- mobile ranged and trample pressure;
- useful against light troops.

Weaknesses:

- smaller and easier to stop than elephants;
- less decisive against dense or large targets;
- vulnerable if pinned.

### Awake-expander expansion

An awake combat Pretender can:

- take difficult provinces;
- establish a second route;
- reduce mundane losses;
- deter a first-year attack;
- bring missing magic.

The cost is paid in:

- scales;
- dominion or bless;
- design paths;
- risk to the Pretender;
- healing and support turns;
- the possibility that the chosen chassis cannot safely fight the actual independent.

Arcoscephalian healing makes a recoverable combat Pretender more attractive, but does not make it immortal or immune to lethal counters.

## Target classification

Before each neutral attack, classify the province.

| Independent feature | Arcoscephalian concern |
| --- | --- |
| Large low-damage infantry | Heavy line usually favourable; check total numbers and fatigue |
| Barbarians or high-strength weapons | Protection can be penetrated; use margin and missiles |
| Heavy cavalry | Lance impact can kill expensive infantry or riders |
| Crossbows | Heavy armour helps, but concentrated armour-piercing fire still matters |
| Archers and slingers | Shields and armour help; exposed Peltasts and Slingers suffer |
| Elephants or other tramplers | Body size, morale, and formation require a specific plan |
| Heavy infantry | Killing speed may be too low without elephants or magic |
| Sacred or unusual independents | Inspect weapons, paths, morale, and special abilities |
| Many commanders or mages | Assassination, morale, or magic can change the expected fight |

## Expansion losses and stop rules

An expansion party should stop when:

- its next target is outside the package's favourable class;
- losses would delay a fort or second party;
- the retreat province is unsafe;
- enemy borders make the party easy to trap;
- an elephant or commander has accumulated a material affliction;
- consolidation produces more value than one more exposed province.

The real cost of a dead Hoplite is not thirteen gold. It includes thirty-one resources, recruitment capacity, transport, and the effect of a thinner line on the next battle.

## First-year infrastructure

A robust first year normally needs:

- continued expansion;
- a second expansion party or awake Pretender route;
- a second fort site chosen for population, resources, geometry, and safety;
- a laboratory where the first new Mystic production matters;
- temples where dominion, priest recruitment, or sacred production justify them;
- enough scouts to find neighbours before armies do;
- a treasury reserve against bad events, defence, and fort completion.

The 300-gold laboratory surcharge changes timing. A fort that cannot receive a laboratory on schedule is not yet a Mystic factory.

## Turn-12 test record

Every serious design should be tested through turn 12 with:

- exact scales and awakening;
- exact independent strength;
- map type or seed;
- active mod list and order;
- recruitment by turn;
- Province Defence purchases;
- fort, lab, and temple starts;
- site searching;
- expansion route;
- every battle and loss;
- treasury and gem stock;
- surviving army;
- research level;
- contact and border geometry.

### Minimum comparison metrics

| Metric | Why it matters |
| --- | --- |
| Provinces owned | Gross territorial result |
| Income | Ability to sustain Mystics and infrastructure |
| Forts completed / building | Future mage throughput |
| Labs completed / planned | Actual conversion of forts into magic |
| Mage count and randoms | Research and access |
| Expansion-party survivors | Deterrence and replacement burden |
| Pretender state | Wounds, afflictions, location, fatigue and risk |
| Border length | Defence demand |
| Neighbour contact | First-war pressure |
| Research reached | Whether the proposed timing is real |

## Expansion test hypotheses

The first Arcoscephale test suite should compare:

1. scales plus starting heavy infantry;
2. scales plus early elephants;
3. mixed infantry, chariots, and elephants;
4. awake combat Pretender;
5. dormant intervention Pretender with stronger scales.

For each, test at least:

- ordinary infantry;
- barbarians;
- heavy cavalry;
- crossbows;
- heavy infantry;
- enemy tramplers.

Precise party sizes remain **test pending** until those runs are saved.

# Part VI: Research Response Trees

## The research trunk

Arcoscephale wants many schools. The solution is not to research every school evenly. It is to reach small conversion nodes that make the present army better, then branch.

A broadly useful trunk is:

1. **Thaumaturgy 1** for Communion Master and Communion Slave.
2. **Alteration 3** for Earth Meld, Body Ethereal, Mossbody where the cross-path exists, and a cluster of defensive or control tools.
3. **Conjuration 3** for Phoenix Power, Summon Earthpower, Power of the Spheres, and early elemental options.
4. A branch chosen from the observed enemy.

This is doctrine, not a mandatory order. An immediate rush can require Evocation, Thaumaturgy 2, Construction, or another emergency branch first.

## Exact early and middle conversion nodes

The manual confirms the following relevant spells:

| Node | Requirement | Effect and Arcoscephalian use |
| --- | --- | --- |
| Communion Master / Slave, Thaumaturgy 1 | S1 | Creates the national path-elevation system |
| Mind Burn, Thaumaturgy 2 | S2 | 12+ armour-negating damage, MR negates; early single-target Astral threat |
| Body Ethereal, Alteration 3 | S1 | Point protection against nonmagical attacks |
| Earth Meld, Alteration 3 | E2 | Area movement control |
| Phoenix Power, Conjuration 3 | F2 | Raises Fire on the caster |
| Summon Earthpower, Conjuration 3 | E2 | Raises Earth and supplies reinvigoration |
| Power of the Spheres, Conjuration 3 | S1 | Raises the caster's known magic paths |
| Strength of Giants, Enchantment 1 | E2 | Point Strength support |
| Destruction, Alteration 4 | E3 | Armour-negating armour damage over area |
| Paralyze, Thaumaturgy 4 | S2 | MR-negates control against non-mindless targets |
| Light of the Northern Star, Conjuration 4 | S3 | Battlefield enchantment raising Astral |
| Falling Fires, Evocation 5 | F3 | Area armour-piercing Fire damage |
| Falling Frost, Evocation 5 | W3 | Area armour-piercing Cold damage |
| Gifts from Heaven, Evocation 5 | E3S1 | Very high damage with low precision; dangerous near friendly troops |
| Stellar Cascades, Evocation 5 | S2 | Area armour-piercing fatigue damage |
| Soul Slay, Thaumaturgy 5 | S3 | MR-negates death against a single non-mindless target |
| Mind Hunt, Evocation 6 | S4 | Remote commander attack; detection and feeblemind risk matter |
| Sow Dragon Teeth, Enchantment 6 | E2 + 1 gem | Ten national Spartae in battle |
| Marble Warriors, Alteration 7 | E3 | Large-area protection for non-spirit targets |
| Will of the Fates, Alteration 7 | S5 | Battlefield-wide Luck |
| Legions of Steel, Construction 6 | E4 | Battlefield-wide armour improvement |
| Army of Lead, Alteration 9 | E5S1 | Battlefield-wide major protection |
| Army of Gold, Alteration 9 | E5F1 | Battlefield-wide major protection |
| Master Enslave, Thaumaturgy 9 | S8 | Battlefield-wide MR-negates enslavement against eligible minds |

The table gives capabilities, not recommended scripts. Friendly-fire risk, magic resistance, fatigue, gem cost, battlefield range, and enemy resistance still determine value.

## Branch A: anti-armour

### Problem

Enemy protection makes mundane spears and tramplers trade poorly.

### Early answer

- **Destruction** at Alteration 4 from an E3 caster.
- An E2 Mystic reaches E3 through Summon Earthpower or a two-slave communion.
- Ordinary infantry and tramplers exploit the reduced armour.

### Middle answer

- combine armour destruction with Falling Fires, Gifts from Heaven, elementals, or strengthened troops;
- use Stellar Cascades if fatigue rather than immediate kills is the better axis;
- avoid concentrating expensive magic into a battle the enemy can decline.

### Failure branch

If Destruction misses the relevant squares, or if raw HP and size matter more than Magic Resistance, add control, high damage, or more attacks. Repeating armour reduction will not solve that problem.

## Branch B: anti-elite and anti-giant

### Problem

Few high-stat or giant troops defeat ordinary lines and cannot be trampled efficiently.

### Tools

- Earth Meld to hold targets;
- Body Ethereal on critical blockers;
- Mind Burn, Paralyze, and Soul Slay where MR permits;
- Gifts from Heaven for extreme physical damage at accepted accuracy risk;
- elementals to create size and disruption;
- Destruction if armour is the main defence;
- fatigue through Stellar Cascades or prolonged combat;
- a properly chosen Pretender or thug.

### Doctrine

Do not ask one spell to do every job. A complete anti-elite package needs:

1. a line that survives initial contact;
2. control or distraction;
3. damage that attacks the correct defence;
4. mage protection;
5. a plan if the elite force attacks the rear or refuses the centre.

## Branch C: anti-mass

### Problem

Large numbers surround the line and exhaust killing capacity.

### Tools

- elephants and chariots against eligible sizes;
- Falling Fires or Falling Frost against low resistance;
- area control;
- summoned elementals;
- dense formation infantry to hold frontage;
- Fire or Cold resistance on friendly forces when using hazardous battlefield conditions.

### Failure branch

If the enemy mass is mindless, do not rely on mind effects. If it is undead, add priests and check the exact banishment environment. If it contains sacrificial chaff protecting dangerous mages, rear pressure or remote commander attacks may matter more than killing every body.

## Branch D: anti-undead and anti-demon

### Assets

- H1 and H2 priestesses;
- a prophet or Pretender;
- Astral, Fire, and national summoned options;
- morale support;
- precise information from dominion scrying.

### Requirements

- enough priests to matter at battlefield scale;
- bodyguards against undead flyers or assassins;
- protection against fear and fatigue;
- Spirit Sight or another answer when darkness, invisibility, or special sight is relevant;
- an answer to the enemy mages rather than only the undead screen.

The ordinary infantry may hold skeletons but can be exhausted by endless replacement. The strategic target is often the summoning engine.

## Branch E: anti-rush

The emergency branch is selected after reading the neighbour.

| Rush feature | Candidate response |
| --- | --- |
| High protection | Alteration 4 for Destruction |
| Few elite sacreds | Thaumaturgy 2/4, control, elementals, body-blocking |
| Giants | Control, high damage, fatigue, avoid elephant dependence |
| Flyers | Rear guards, dispersed mages, bodyguards, wider deployment |
| Fire or Cold aura | Resistance, spacing, ranged damage, suitable element |
| Glamour and high defence | Spirit Sight where available, area effects, attack improvement |
| Regeneration | Concentrated damage, decay or disease where accessible, control |
| Undead mass | Priests, morale, engine-killing |

Construction can be an anti-rush branch if a combat Pretender or thug is the fastest viable answer. It is not automatically useful merely because items are permanent.

## Branch F: remote Astral control

### Mind Hunt

Mind Hunt is Evocation 6, S4, two Astral pearls, range six.

Arcoscephale can obtain S4 on capital Astrologers without boosters, though not every Astrologer is S4. Healing reduces the long-term cost of some recoverable afflictions, but does not remove detection risk or make indiscriminate hunting sound.

Targets should be chosen from:

- commanders outside Astral protection;
- siege leaders;
- critical priests;
- isolated thugs;
- laboratory mages exposed by scrying and scouts.

The package includes:

- target intelligence;
- several S4 casters if the objective justifies them;
- a safe laboratory;
- pearls;
- healing capacity;
- a plan for enemy Astral detection or domes.

### Soul Slay and Master Enslave

Soul Slay is a battlefield precision tool against eligible high-value units. Master Enslave is an endgame operation, not a research aspiration in isolation.

A Master Enslave operation needs:

- S8 effective skill;
- a robust communion;
- penetration;
- protection from interruption;
- enough fatigue support;
- a plan for mindless and high-MR enemies;
- commanders able to control any captured units;
- an exploitation plan if the enemy army is stolen.

## Branch G: battlefield renewal

Arcoscephale's mundane army scales when research makes old soldiers survive modern magic.

Key transformations include:

- point ethereal and protection effects on the contact line;
- Destruction making ordinary spears relevant against armour;
- Marble Warriors improving a broad formation;
- Will of the Fates reducing casualties across the army;
- Legions of Steel improving worn armour;
- Army of Lead or Gold creating a late-game protected mass.

The more expensive the buff package, the more important it is to ask whether the troops are the right recipients. A battlefield-wide spell does not make a routed, immobile, poisoned, or bypassed army successful by itself.

## Research rejoin points

Emergency branches should rejoin a larger plan.

Examples:

- Thaumaturgy 2 anti-elite -> Thaumaturgy 5 for Soul Slay -> Evocation 6 for Mind Hunt;
- Alteration 4 anti-armour -> Alteration 7 for Marble Warriors and Will of the Fates -> Alteration 9;
- Evocation 5 damage -> Evocation 6 remote Astral -> later battlefield offence;
- Conjuration 3 self-buffs -> Conjuration 4 Northern Star -> national and elemental summons;
- Construction branch for a Pretender -> boosters -> ritual access.

The rejoin point should be recorded before emergency research begins, preventing a permanent drift across half-finished schools.

# Part VII: Army Packages

## Package 1: The old line

**Purpose:** defeat ordinary human troops and hold ground cheaply.

**Core:**

- Hoplite or Hypaspist centre;
- Cardaces or Peltasts as screen or flank;
- one reliable commander;
- optional Hiereia;
- scouts on the operational route.

**Scaling:**

- add a Strategos for a larger army;
- add elephants or chariots for killing power;
- add a small Mystic cell once research provides a specific effect.

**Failure modes:**

- high-damage weapons penetrate the line;
- fatigue breaks Hoplites;
- flyers reach the rear;
- the army cannot kill high protection;
- slow movement cedes operational initiative.

## Package 2: The elephant hammer

**Purpose:** break large formations of smaller ordinary troops.

**Core:**

- infantry screen;
- elephant group on a flank or behind the line;
- commander with adequate leadership and morale support;
- rear guard;
- scouting of size, morale attacks, and MR-negates magic.

**Scaling:**

- add enough elephants to create simultaneous contact;
- add point buffs to the screen;
- add area damage or control so elephants are not stopped by elites;
- add Hiereia/Archousa support and a post-battle healing route.

**Failure modes:**

- panic or control;
- giants;
- rear attack on commanders;
- a narrow battlefield;
- friendly trampling during rout;
- overinvestment in a countered chassis.

## Package 3: Independent Mystic battery

**Purpose:** obtain many useful casts without communion concentration.

**Core:**

- several Mystics selected for the same low-level effect;
- one pearl or relevant elemental gems where needed;
- heavy infantry screen;
- separation and bodyguards;
- strict scripts whose unscripted continuation is acceptable.

Examples:

- repeated Body Ethereal;
- Mind Burn from S2 casters;
- Power of the Spheres followed by elemental effects;
- small elemental summons;
- repeated point buffs.

**Strength:** every mage acts.

**Failure:** individual path and gem use may be less powerful than a communion; spell-selection variance can scatter effects.

## Package 4: Four-slave elemental communion

**Purpose:** turn common elemental randoms into level-three battlefield casters.

**Core:**

- four Communion Slaves;
- one or two chosen masters;
- screen and rear guard;
- gem load calculated from the exact script;
- no unnecessary masters.

Candidate master outcomes:

- F1 -> F3;
- W1 -> W3;
- E1 -> E3;
- S1 -> S3.

Self-buffs can raise paths further, but also change fatigue relationships and must be tested.

**Failure:** slave fatigue, lost threshold, massed mage casualties, or masters improvising expensive spells.

## Package 5: Astral elimination cell

**Purpose:** remove a few high-value eligible targets.

**Core:**

- Astrologers or appropriate masters;
- Soul Slay or another current Astral killing spell;
- penetration where available;
- a line long enough to permit repeated casts;
- target selection based on MR and mind status.

**Failure:** high MR, mindlessness, enemy Magic Duel threat, insufficient range, or line collapse.

## Package 6: Armour-break combined arms

**Purpose:** let ordinary troops and tramplers defeat armour.

**Core:**

- E3 effective caster for Destruction;
- resilient screen;
- Hypaspists, elephants, chariots, or summoned bodies ready to exploit;
- secondary magic if armour destruction lands unevenly.

**Failure:** the enemy disperses, kills the Earth caster, relies on innate protection, or counters the exploitation force.

## Package 7: Fort storm and Throne claim

**Purpose:** convert field advantage into victory position.

**Core:**

- sufficient siege bodies;
- a storming line;
- an anti-commander or anti-mage plan;
- H2 or H3 claim capacity as required by the Throne;
- supply and laboratory support;
- a relief interception force;
- replacement commanders.

Arcoscephale's strength in field magic does not automatically crack walls or claim Thrones. The claim-capable priest and army must arrive together after the fort falls.

## Package 8: Distributed counter-raiding

**Purpose:** prevent fast or stealth forces from turning a slow main army into territorial collapse.

**Core:**

- dominion scrying on approaches;
- scouts outside dominion;
- small Mystic cells in protected labs;
- cheap commanders and local troops;
- mobile elephants, chariots, or a Pretender where suitable;
- fort and laboratory redundancy.

**Failure:** every cell is too weak, pearls are absent, or the main army cannot exploit the enemy's dispersion.

# Part VIII: Pretender Families

## Family A: Awake expansion and missing path

### Job

- take difficult neutral provinces;
- preserve national troops;
- deter an early rush;
- bring one or two missing paths, commonly Death, Air, Glamour, or another ritual bridge.

### Good fit

- crowded maps;
- dangerous neighbours;
- weak starting terrain;
- a design whose chassis can reliably expand under the actual settings.

### Costs

- weaker scales;
- Pretender risk;
- fewer design points for broad ritual access;
- possible overlap with elephants.

### Audit

The chassis must be tested against heavy cavalry, barbarians, poison, magic weapons, and MR attacks. Healing is a recovery advantage, not a licence to attack unknown targets.

## Family B: Dormant intervention platform

### Job

- stronger scales than an awake expander;
- arrive near the first serious war;
- carry missing paths;
- serve as thug, battlefield caster, forger, or ritual bridge.

### Good fit

- national troops can expand;
- the likely danger begins after contact;
- the nation wants a high-impact mid-game path package.

### Costs

- no help during the first expansion turns;
- the planned battlefield role can be invalidated by the actual neighbour;
- a dormant chassis that cannot move or fight as expected may become an expensive researcher.

## Family C: Imprisoned scales and research

### Job

- maximise gold, resources, growth, and research scales;
- multiply forts and Mystics;
- emerge as a late ritual platform.

### Good fit

- spacious map;
- reliable troop expansion;
- diplomatic room;
- a plan that uses the additional economic throughput before awakening.

### Costs

- no Pretender during expansion or first war;
- greater vulnerability to rush;
- high-path ritual promises may arrive after the decisive period.

The design succeeds only if the recruitable state survives long enough to compound.

## Family D: Sacred-support hybrid

### Job

- provide an incidental or moderate bless to Heart Companions;
- remain useful as an expander, battlefield caster, or ritual bridge.

### Good fit

- the capital can recruit Companions without sacrificing the rest of the plan;
- the bless also improves sacred commanders, summons, or the Pretender;
- the sacred unit fills a clear tactical role.

### Costs

- capital-only recruitment;
- heavy resources;
- slow map movement;
- bless points that could solve wider national constraints.

## Family E: Ritual bridge

### Job

Provide paths missing from the national roster.

Priority candidates:

- Death for the national Underworld summons and wider Death economy;
- Air for mobility, lightning, forging, and storm tools;
- Glamour for sight, illusion, and control options;
- Blood only if the design includes a credible way to create and sustain a Blood economy;
- high Nature for national N3/N4 rituals and global access.

### Audit

For every promised ritual, write the complete route:

```text
Pretender base path
+ named booster
+ empowerment if any
+ research level
+ gem cost
+ laboratory and province requirement
= legal caster
```

If one step is missing, the ritual is not part of the build.

## Historical builds and current legality

Earlier project discussions proposed:

- an imprisoned Astral-Earth Titan;
- a dormant Great Enchantress with Astral, Earth, Nature, and Death;
- a later Grand Hierophant with Fire, Air, Astral, and Blood under the combined mod set.

These are retained as historical design families, not copied as current legal builds. Chassis paths, design costs, scale limits, blesses, and mod abilities must be rebuilt in the current Pretender screen before publication as finished designs.

## Scale priorities

### Order

Supports:

- expensive mage recruitment;
- fort and laboratory construction;
- elephants and ordinary armies.

The national +1 limit makes high Order available, but the final value depends on the design-point curve and map economy.

### Production

Supports:

- Hoplites;
- Hypaspists;
- Heart Companions;
- fort provinces with strong local resources.

Elephants themselves are not resource-intensive on the rider listing, so an elephant-heavy opening can use gold faster than resources.

### Growth

Supports:

- long-run income;
- population resilience;
- supplies;
- Blood resistance if Blood Hunting occurs nearby;
- campaigns expected to last.

### Magic

Supports:

- Research Points;
- spell performance through the scale's ordinary effects;
- the national plan of reaching several response nodes.

It also affects enemy magic in the same province and may interact with events. It is not an uncontested bonus.

### Luck

Interacts with events and the concentration of Astrologer Fortune Tellers. It should be evaluated as part of the whole event policy, not only because the nation uses Astrologers.

### Temperature

Choose after checking:

- national preference;
- design points;
- income and supplies;
- expected battlefield effects;
- mod changes.

### Sloth

Sloth purchases design points by taxing a roster that contains resource-heavy infantry and sacreds. It is more plausible in an elephant- or magic-heavy design than in one promising massed Hoplites and Heart Companions.

# Part IX: Campaign Doctrine

## Early game

### Objectives

- expand without crippling attrition;
- identify neighbours before contact becomes war;
- begin the second fort and its 300-gold laboratory;
- recruit the first Mystic portfolio;
- retain enough mundane force to deter a rush;
- choose research from observed threats.

### Questions each turn

- Which independent class is the next target?
- Is a valuable elephant or commander entering an uncertain battle?
- Does the treasury still meet the fort and laboratory schedule?
- Which Mystic random appeared, and has it been recorded?
- Which neighbour can reach the capital fastest?
- Does the research branch produce a complete package before that attack?

### Common early failure

Arcoscephale can spend on everything:

- 190-gold Mystics;
- 270-gold Astrologers;
- 100-gold elephants;
- forts;
- 300-gold labs;
- ordinary armies.

The nation risks buying one of each and completing none of its conversions. A plan should state the current priority:

```text
expansion force
or infrastructure
or mage throughput
or emergency defence
```

The other categories receive maintenance, not equal spending.

## First war

### War aim

The first war should have a positional aim:

- remove a dangerous rush neighbour;
- seize a fort cluster;
- secure a Throne corridor;
- take a high-income or high-gem region;
- shorten the border;
- destroy an exposed mage core.

“Use the research lead” is not a war aim.

### Preparation

Record:

- enemy troop defence classes;
- known magic paths and school evidence;
- likely battlefield enchantments;
- routes and retreat provinces;
- fort wall strength and relief distance;
- required gems by battle;
- replacement Mystic production;
- the branch if the first army is countered.

### First-war strengths

- heavy infantry can anchor;
- elephants punish unprepared human formations;
- Mystics can tailor several low- and middle-level packages;
- automatic scrying improves defence inside dominion;
- healing preserves expensive survivors;
- Astrologers threaten high Astral.

### First-war weaknesses

- most mages are expensive human bodies;
- a large communion risks a national research disaster;
- no normal Death, Air, Glamour, or Blood limits adaptation;
- tramplers have clear morale and MR counters;
- heavy infantry can be bypassed or fatigued;
- the 300-gold lab cost slows replacement infrastructure.

## Middle game

The middle game begins when the nation has several forts, multiple Mystic cohorts, and enough research that the opponent must respect several branches.

### Objectives

- turn random-mage breadth into repeatable packages;
- establish booster and gem logistics;
- create at least one remote or mobile threat;
- defend the capital Astrologer pipeline;
- convert won battles into forts and labs;
- begin a Throne claim plan.

### Portfolio doctrine

Do not send the entire mage corps with one army. Divide it into:

- research reserve;
- main field package;
- counter-raiding cells;
- ritual and forging specialists;
- capital Astral core;
- healing and recovery hubs.

The exact proportions change during war. The distinction prevents the same mage from being promised simultaneously to research, forge, cast a ritual, and fight.

## Late game

### National late-game strengths

- accumulated Astral;
- communions capable of high battlefield paths;
- broad elemental response;
- strong research if the fort network survived;
- information across friendly dominion;
- healing of valuable commanders;
- access to high-end Astral rituals and battlefield magic.

### National late-game limits

- low innate non-Astral path ceilings;
- absent Death, Air, Glamour, and Blood unless bridged;
- mortal human mage core;
- expensive fort and lab replacement;
- capital dependence for Astrologers;
- greater enemy ability to clear dense armies and communions.

### Late-game transition

The old army should become one of several shells around the magic:

- protected mass;
- siege and Throne body;
- screen for remote or high-Astral operations;
- distributed defence;
- disposable frontage for summons.

If every late-game battle still depends on unmodified Hoplites and elephants reaching melee, research has not been converted.

## Endgame and Thrones

An endgame plan states:

- current Ascension Points;
- claimable Thrones and required priest levels;
- forts and walls on each target;
- enemy relief routes;
- magic-phase threats;
- claim timing;
- the army that survives after the storm;
- the diplomatic response to visible victory progress.

Arcoscephale's H2 Archousa can claim Thrones that require H2. Higher requirements need a prophet, Pretender, hero, or imported priest.

Automatic scrying helps defend claimed territory inside dominion, but the victory turn may depend on simultaneous attacks beyond that information umbrella.

## Raiding

### Native raiders

Unmodded Arcoscephale is not defined by stealth thugs or flying sacreds. Native options are modest:

- small conventional troop groups;
- chariot or elephant detachments against known weak defence;
- a combat Pretender;
- a geared commander when Construction and target class justify it;
- remote Astral attacks against commanders rather than province capture.

### Raiding doctrine

The nation should raid to:

- cut reinforcement routes;
- take laboratories;
- force counters away from the decisive siege;
- break a dominion or temple corridor;
- isolate a fort;
- punish an enemy who concentrated against the main line.

Slow heavy infantry should not chase fast raiders province by province. Scrying, forts, Mystic cells, mobile tramplers, and prediction form the counter-raiding system.

## Sieges

The roster supplies many human siege bodies but no automatic siege miracle.

Before besieging:

- calculate whether the army can breach on the required deadline;
- protect the lab and gem route;
- keep enough field power to defeat relief;
- preserve a storming package distinct from wall damage;
- move a claim-capable priest toward any Throne;
- scout every adjacent retreat.

Mystics researching inside a siege army are not free value if a relief battle destroys them.

## Diplomacy

Arcoscephale presents two political images.

The visible image is a conventional human kingdom with slow infantry and elephants. The hidden image is a rapidly compounding Astral state capable of communions, remote attacks, and high research.

This creates predictable diplomacy:

- neighbours may seek an early war before the mage network matures;
- others may value Arcoscephale as a stable border or anti-elite partner;
- Mind Hunt and Master Enslave potential can make later coalitions wary;
- scrying makes covert movement inside dominion less reliable;
- broad but shallow paths create useful gem and item trades.

Good diplomacy communicates enough strength to deter without advertising every random and research branch.

## Matchup framework

### Against heavy armour

Prefer:

- Destruction;
- high-damage or armour-negating magic;
- fatigue;
- elementals;
- a protected line that buys casting time.

Avoid:

- relying on ordinary spear damage alone;
- sending elephants into elite armour without disruption.

### Against giants

Prefer:

- Earth Meld and other control;
- Gifts from Heaven or other high-damage effects;
- fatigue and MR pressure;
- enough line depth to prevent immediate mage contact.

Avoid:

- treating trample as the primary answer;
- spending heavily on protection that giant damage easily penetrates without another plan.

### Against high-MR elites

Prefer:

- physical control and damage;
- armour destruction;
- fatigue that does not depend on one MR check;
- penetration only when the arithmetic is credible.

Avoid:

- a pure Soul Slay plan without enough attempts and penetration.

### Against undead mass

Prefer:

- priest support;
- engine killing;
- morale protection;
- fire, area damage, and fatigue tools appropriate to the exact undead;
- sustained lines that do not exhaust before the summoners.

Avoid:

- counting skeleton kills without measuring mage fatigue and replacement.

### Against flyers and attack-rear forces

Prefer:

- rear guards;
- mage bodyguards;
- wider or staggered deployment;
- separated mage cells;
- predictive interception through scrying.

Avoid:

- a single unguarded communion block.

### Against glamour and stealth

Prefer:

- dominion scrying;
- Spirit Sight or other current sight tools;
- area effects;
- patrol networks;
- redundant defence.

Avoid:

- assuming a missing army is absent.

### Against enemy Astral

Prefer:

- explicit Magic Duel policy;
- non-Astral damage where possible;
- protecting high-S Astrologers;
- decoy and target-priority planning;
- assessing enemy penetration and remote threat.

Avoid:

- exposing irreplaceable high-S casters to cheap duellists without need.

## Heroes

The unmodded national hero pool includes:

| Hero | Strategic contribution |
| --- | --- |
| Anthromachus | Inspirational military leadership |
| Orokestes, Hierophant | F1A1W1E1S2H2; unique Air and broad cross-path access |
| Pathos, Son of Titans | Durable inspirational hero with Awe and Invulnerability |
| Axieros, Kabeiride | W1N3H2, Healing 3, Sailing, recuperation and support abilities |

Heroes are opportunities, not foundations. A plan that requires Axieros for N3 or Orokestes for Air has no deadline guarantee unless the hero is already present.

When a hero appears:

1. record the exact paths and abilities in the current version;
2. identify unique items, rituals, or movement unlocked;
3. protect the hero according to replacement impossibility;
4. avoid forcing the hero into a role a repeatable recruit can perform.

## Gem economy

The capital produces four Astral pearls and one Nature gem per month.

Astral pearls compete among:

- communions and Power of the Spheres;
- battlefield Astral;
- forging;
- remote magic;
- boosters;
- globals;
- high-end rituals;
- reserve against an unexpected war.

Nature gems compete among:

- support summons;
- boosters;
- national Monster Boar or Hamadryad routes after access exists;
- later globals;
- trades that buy missing Death, Air, or other resources.

An Astral-rich nation can still run out of pearls if every Mystic receives one for every battle. Gem budgets should be assigned by operation, not distributed by habit.

## Laboratory and item security

Because labs cost 300 gold and pool gems:

- do not leave the only forward laboratory exposed;
- keep irreplaceable boosters off commanders taking uncertain routes;
- maintain a rear laboratory for recovery;
- transfer operation gems shortly before commitment;
- record item ownership;
- include retreats and laboratory capture in the invasion ledger.

## New-player turn checklist

### Recruitment

- Is every fort recruiting the commander it needs?
- Was a rare Mystic random identified?
- Is the capital buying an Astrologer for a defined job?
- Can a Hiereia be recruited outside a fort instead?
- Does troop recruitment match local gold and resources?

### Research

- What enemy problem does the current school solve?
- Which mage can cast the spell?
- Does the caster need a communion, self-buff, gem, or item?
- Will the army and caster reach the same battle?

### Armies

- Are elephants screened?
- Is the rear protected?
- Is the commander safe?
- Are retreat provinces friendly?
- Are slow Hoplites delaying an urgent operation?

### Economy

- Is the next fort still affordable?
- Has the 300-gold lab been budgeted?
- Are pearls reserved for the next operation?
- Is a mage promised to both research and fight?

### Information

- What is seen by scouts?
- What is seen only by dominion scrying?
- Which report is stale?
- Could the missing force use stealth or magic movement?

## Expert turn audit

- Recalculate specialist probabilities against current recruitment.
- Separate native, boosted, bootstrapped, and imported path claims.
- Compare independent casting with communion opportunity cost.
- Check every master/slave path and fatigue relationship.
- Audit post-script spell-selection risk.
- Check Magic Duel exposure.
- Recalculate siege and relief clocks.
- Mark every S4+ Astrologer and rare dual-path asset.
- Protect capital recruitment and laboratory continuity.
- Update Throne claim capacity and simultaneous victory threats.

# Part X: Dominions Enhanced 2.16

## Scope of the overhaul

Dominions Enhanced 2.16 genuinely overhauls MA Arcoscephale. The changes go well beyond one adjusted cost.

**Source-confirmed changes include:**

- a rebuilt ordinary troop roster;
- new phalangite and cavalry units;
- a new mounted commander;
- revised Hoplites, Hypaspists, Heart Companions, Archousai, Mystics, and Astrologers;
- paired Heart Companion recruitment at national sites;
- capital Hetairoi;
- a different hero pool and multihero;
- a large national spell and summon suite;
- national items;
- new late-game Titans, nymphs, heroes, and constellation magic.

The strategic identity changes from “broad low-elemental Astral nation with several inaccessible nationals” to “Astral combined arms with a geography-dependent summon ladder capable of opening most missing paths.”

## Recruitment rewrite

The nation block clears ordinary recruitment and then rebuilds access.

### Fort commanders

All listed terrain forts receive:

- Scout;
- Lokhagos;
- Hipparchus;
- Strategos;
- Mystic;
- Archousa;
- Hiereia.

The Hiereia is also added outside forts in plains, forests, mountains, swamps, wastes, farms, and caves.

Capital Astrologer access remains tied to the Tower of a Thousand Stars rather than the rebuilt ordinary fort list.

### Ordinary troops

The rebuilt list contains:

- Slinger;
- Peltast;
- Cardaces;
- Hoplite;
- Phalangite;
- Hypaspist;
- Prodromoi;
- Chariot;
- Elephant.

Hetairoi are defined but commented out of the ordinary list. They are instead placed at the Tower of a Thousand Stars. Paired Heart Companions are placed at that site and at the Gymnasium.

### Starting army

The mod sets:

- Lokhagos as starting commander;
- Scout as starting scout;
- twenty Peltasts;
- twenty Hoplites.

## Revised and new units

### Hoplite

**Source-confirmed delta:**

- Defence 11;
- effective gold setting 11 in the mod source;
- new sprites.

Compared with the unmodded 13-gold Defence-9 Hoplite, this is a substantial efficiency and survival improvement.

### Hypaspist

**Source-confirmed delta:**

- Attack 12;
- Defence 13;
- Combat Speed 14;
- effective gold setting 12.

The source contains two consecutive Defence assignments, 11 then 13; the later value controls. The unit becomes a faster and cheaper elite line rather than merely the flexible alternative to a Hoplite.

### Phalangite, unit 9316

The new MA Phalangite:

- uses half plate, Hoplite helmet, and buckler;
- wields a Sarissa;
- has HP 11, Strength 11, Attack 12, Defence 12;
- costs 16 recruitment points;
- uses the source's effective 13-gold setting.

The long Sarissa and lighter armour define a more offensive formation unit than the old Hoplite.

### Prodromoi, unit 9317

The Prodromoi are light cavalry:

- Xyston, broad sword, and javelin;
- ring-mail hauberk, half helmet, and buckler;
- Skilled Rider 3;
- leather-barding horse;
- HP 11, Attack 11, Defence 11, Morale 12;
- 13 recruitment points;
- effective 10-gold setting.

They add cheap mobile flank and skirmish pressure that vanilla MA Arcoscephale lacks.

### Hetairoi, unit 9318

The Hetairoi are capital-site heavy cavalry:

- half plate, half helmet, and buckler;
- Xyston, broad sword, and javelin;
- Skilled Rider 5;
- light scale-barding horse;
- HP 13, Strength 12, Attack 12, Defence 12, Morale 12.

Their cost and recruitment values are inherited from the copied Agema Companion because the proposed explicit overrides are commented out. The exact final in-game card remains a combined-object verification item.

### Hipparchus, unit 9319

The Hipparchus is the matching cavalry commander:

- same main equipment family as the Hetairoi;
- Skilled Rider 6;
- light scale-barding horse;
- HP 13, Attack 12, Defence 12, Morale 12;
- inherited leadership and costs from the Agema Commander.

The final inherited values should be captured from the live modded unit card before publication of a numeric quick-reference.

### Heart Companions in pairs

Unit 9322 represents paired recruitment:

- source cost 50 gold;
- recruitment-point cost 46;
- resource cost 28;
- Plate Hauberk, Hoplite Helmet, Buckler, Sarissa;
- Morale 14, Strength 12, Attack 12;
- description explicitly states that two are recruited at once.

Seasonal shapes and nation events convert the paired representation into two ordinary Heart Companions. The ordinary Heart Companion is also rewritten with the same equipment family and improved Morale, Strength, and Attack.

This changes sacred economics:

- the recruitment purchase is indivisible;
- the effective body cost is nominally half the pair cost;
- capital and Gymnasium access matters;
- bless value must be recalculated against two-at-a-time production;
- the transformation/event timing should be reproduced before assuming both bodies are immediately available in every interface.

### Archousa

The Archousa becomes:

- N2 rather than N1;
- 265 gold rather than 235.

This single path increase is strategically central. It turns high Nature from a hero-dependent hope into a booster and summon-ladder project.

### Mystic

The Mystic gains Poor Magic Leadership.

The magic random structure is not cleared or rewritten in the inspected source, so the unmodded path distribution remains unless another loaded layer changes it. Poor Magic Leadership matters when summoned magic beings are moved with Mystic armies.

### Astrologer

The Astrologer gains permission to use restricted-item group 10, enabling the national Zodiac item. The base path structure is not rewritten in the inspected source.

## Site recruitment

### Tower of a Thousand Stars

Dominions Enhanced clears and rewrites the site:

- 4 Astral pearls per month;
- 1 Nature gem per month;
- Astrologer as home commander;
- paired Heart Companions;
- Hetairoi.

### Gymnasium

The Gymnasium is rewritten to provide paired Heart Companions.

This creates two sacred-production cases:

- capital production from the Tower;
- any obtained Gymnasium site.

The frequency and map availability of Gymnasia are not a guaranteed national resource and should not be assumed at Pretender design.

## Hero rewrite

The MA national hero line becomes:

- Aleksandros, the Conqueror;
- Orokestes;
- Pathos;
- Axieros;
- Muse as multihero.

### Aleksandros

Aleksandros replaces Anthromachus in the era's primary hero slot. The source defines:

- mounted movement;
- Awe and Fear;
- Inspirational 2;
- high leadership;
- sacred status;
- enchanted equipment;
- events that rally local population types when he is present.

The rally events can generate troops and commanders from horse tribes, Raptorians, several Amazon types, elephant populations, Atavi, and other local groups. These are opportunity effects dependent on both the hero and province population type.

### Muses

Muses are repeatable multiheroes with:

- Glamour 3;
- two random picks from a Fire/Air/Astral/Nature mask in the source;
- Awe, stealth, seduction, Inspirational 2, and Inspiring Research 1;
- sacred and magic-being status.

They can open valuable paths, but hero arrival remains non-deterministic. A deadline-safe plan cannot require a Muse.

### Adventurers and Divine Heroes

The nation receives future-site pools for:

- adventurer heroes;
- Divine Heroes;
- ordinary national heroes;
- a broad summon catalogue.

These pools support national spells. They are not ordinary recruits.

## National spell suite

The source-confirmed DE suite is grouped below by strategic function. Fields inherited through `#copyspell` should be checked on the final in-game spell card; explicit overridden values are reliable source claims.

### Immediate and battlefield magic

| Spell | Research | Explicit requirement | Cost | Effect |
| --- | ---: | --- | ---: | --- |
| Zodiac Cascades | 0 | S1 | 0 | Modified Stellar Cascades, AoE 3, Precision +5; unavailable in caves |
| Light of the Aries Constellation | 4 | S4F1 | Inherits Northern Star cost | Fire +1 and Astral +1 to eligible casters; Fire Resistance 5 to battlefield |
| Light of the Cetus Constellation | 5 | S4W1 | Inherits Northern Star cost | Astral +1; battlefield speed -25%, +3 encumbrance, d4 fatigue per square moved |
| Light of the Taurus Constellation | 6 | S4E1 | Inherits Northern Star cost | Earth +1, Astral +1, Reinvigoration 4 |
| Dissolve into Atoms | 7 | Inherits Soul Slay path | 20 fatigue | AoE 1, MR negates, soul slay; ethereal targets are harder to affect |
| Light of the Libra Constellation | 7 | S6 | Inherits Northern Star cost | Spirit Sight to battlefield and Astral +1 |
| Summon Daimones | 7 | S4 | 3 pearls | Twelve sacred ethereal Daimones; secondary effect gives Luck to 25% of friendly soldiers |

The four constellation lights are mutually incompatible with each other and with an Arcoscephalian Light of the Northern Star. They are a strategic choice, not cumulative path stacking.

### Astral economy and events

| Spell | Research | Requirement | Cost | Effect |
| --- | ---: | --- | ---: | --- |
| Power of the Zodiac | 5 | Inherited from Stellar Focus | 25 pearls | Produces five Astral pearls per month; attempts to override Stellar Focus; not in caves |
| Call to Adventure | Thaumaturgy 4 | S4 | 15 pearls | Summons a band drawn from the national adventurer montage |
| Baleful Conjunction | Inherits Baleful Star | Inherited | 4 pearls | Mountain cast; +30 unrest, Misfortune +3, 10% of units cursed through event |
| Beneficent Conjunction | Inherits Baleful Star | Inherited | 4 pearls | Mountain cast; -30 unrest, Luck +3, 10% tax boost through event |
| Cursed Omen | 6 | Inherited | 5 pearls | Mountain cast; event intended to curse half the target army |

Event-based ritual outcomes and temporary scale duration should be reproduced under the combined mods.

### Nature and elemental summon ladder

| Summon | Research | Requirement | Cost | Geography | Summoned magic |
| --- | ---: | --- | ---: | --- | --- |
| Contact Karyatid | 4 | N3 | 20 Nature | Forest | N3 in forest, N2 outside |
| Contact Oceanid | 5 | W3 | 25 Water | Not restricted in shown block | W3 plus three random picks from A/E/D/N/G |
| Contact Oreiad | 6 | N4 | 30 Nature | Mountain or border mountain | N3A2E1 |
| Contact Eleionomae | 6 | W3 | 35 Water | Swamp | W3D2A1 |
| Contact Nephelae | 7 | W3A1 | 30 Water | Not caves | A3W3 |
| Daughter of the Evening | 8 | S4 | 38 pearls | Ordinary land conditions | S3A2, immortal |
| Summon Boread | 8 | A3W2 | 45 Air | Ordinary valid province | Winged giant commander |

This is the heart of the overhaul. Geography becomes magic access.

### Unique and late summons

| Summon | Research | Requirement | Cost | Notes |
| --- | ---: | --- | ---: | --- |
| The Guardian of Hades | Conjuration 6 | D4 | 20 Death | Unique Kerberos |
| Summon Divine Hero | Conjuration 7 | S5 | 40 pearls | One Divine Hero from national pool |
| Titan of War & Wisdom | Conjuration 8 | S4E2 | 40 pearls | Unique Athena |
| Titan of the Seas | Conjuration 8 | W4E2 | 40 Water | Underwater only; unique Poseidon |
| Titan of the Underworld | Conjuration 8 | D5 | 40 Death | Unique Hades |
| The Scourge of the Deeps | Conjuration 9 | W5N3 | 60 Water | Underwater only; unique Cetus |

### Other national summons

- **Headless Men:** N2, seven Nature gems, ten-plus Blemmyes; the school and research level are inherited from Summon Ogres.
- **Sow Dragon Teeth** and the unmodded Arcoscephalian national rituals remain relevant unless specifically overwritten elsewhere.
- The future-site lists also identify Spartae, Blemmyes, Lampads, Hound of Twilight, Keres, Keledone, Khalkotauros, Daimones, nymph commanders, Kerberos, and the three Titans as national summon products.

## National items

### Bag of Dragons Teeth

**Source-confirmed:**

- Construction 5;
- Earth level 2 through the copied Earth item;
- reduced item cost;
- summons three Spartae at battle start;
- grants one point of magic leadership;
- restricted to a group of appropriate nations including MA Arcoscephale.

It converts an E2 forge turn and Earth gems into a repeatable battlefield screen or reinforcement. The exact inherited base cost should be read from the final item card.

### Horoskopos

**Source-confirmed:**

- S2;
- cursed and not normally forgeable/found in the ordinary way;
- Luck;
- Morale +2;
- Inspirational 1;
- effects apply to the mount where relevant.

Its acquisition route is not established by the inspected item block. It should not be included in a routine forge plan until reproduced.

### Zodiac

**Source-confirmed:**

- Construction 5;
- S2;
- Astrologer-restricted item group;
- 50 points of bad-event prevention;
- Twist Fate;
- effects extend to mount.

The mod explicitly authorises Astrologers to use its restricted group. This turns selected Astrologers into provincial event-control assets without changing their magic.

## DE access ladders

### Reliable Nature-to-Air ladder

1. Recruit an N2 Archousa.
2. Obtain a named Nature booster to N3.
3. Cast Contact Karyatid in a forest.
4. Use the N3 Karyatid in forest, with a booster to N4 if required.
5. Cast Contact Oreiad on a mountain.
6. Receive an N3A2E1 Oreiad.
7. Use Air boosters, empowerment, or another summon to reach higher Air.

Every step requires the relevant research, gems, item, and geography. The ladder is powerful because it is reproducible; it is not instantaneous.

### Water-to-Death ladder

1. Preserve a W2 Mystic.
2. Add a named Water booster to reach W3 for ritual casting.
3. Cast Contact Eleionomae in a swamp.
4. Receive W3D2A1.
5. Use Death boosters, empowerment, or further summons to reach D4.
6. Cast The Guardian of Hades or other Death nationals.

Contact Oceanid is an alternate W3 route with random Death, Glamour, Nature, Air, or Earth outcomes. Because the Oceanid randoms are variable, it is a portfolio rather than deadline guarantee.

### Astral-to-Air ladder

1. Recruit an S4 Astrologer or boost S3.
2. At Conjuration 8, cast Daughter of the Evening.
3. Receive an immortal S3A2 commander.
4. Use Air boosters or combine with Water access.
5. Reach A3W2 for Summon Boread or other Air operations.

### Constellation ladder

Astrologer randoms can naturally provide:

- S4F1 for Aries;
- S4W1 for Cetus;
- S4E1 for Taurus.

Because the fixed and rare randoms interact, exact probabilities should be computed from the current Astrologer distribution and verified after the mod is loaded. S6 for Libra requires boosters or another high-Astral route.

## DE research priorities

The mod creates two new trunks.

### Constellation trunk

- immediate Zodiac Cascades provides an early fatigue tool;
- Conjuration 4 gives the ordinary Northern Star and the research neighbourhood for Aries if the copied school remains;
- levels 5-7 progressively add Cetus, Taurus, and Libra;
- the chosen constellation must fit the army and enemy because only one light can operate.

### Nymph trunk

- level 4 Karyatid begins the Nature ladder;
- level 5 Oceanid begins the Water-random ladder;
- level 6 Oreiad and Eleionomae open Air and Death;
- level 7 Nephelae and Divine Heroes expand force;
- level 8 Daughter of Evening and Titans establish late magic.

The best branch depends on gems and terrain. Researching Contact Oreiad without an N4 caster and a mountain produces no immediate capacity.

## DE army identity

The new roster supports a more mobile combined-arms formation:

- cheaper improved Hoplites;
- fast Hypaspists;
- offensive Phalangites;
- cheap Prodromoi;
- capital Hetairoi;
- paired sacreds;
- elephants and chariots;
- constellation-enhanced Mystics.

The nation can now create:

- a mobile Map Move 16 cavalry and infantry wing;
- a slower sacred or Hoplite core;
- Astral fatigue operations;
- nature-spirit and elemental commander support;
- late unique-summon armies.

Mixed movement must still be audited. One slow unit can reduce the route of an otherwise mobile force.

# Part XI: Divinitus 1.15.3 DE and the Grand Hierophant

## Layer boundary

Divinitus does not rewrite MA Arcoscephale's ordinary national roster in the inspected source. It rewrites Pretenders and adds event-driven powers.

The relevant national interaction is:

```text
Dominions Enhanced national overhaul
+ Divinitus Pretender choice
= combined MA Arcoscephale
```

The strongest documented interaction is the Grand Hierophant, monster 3053.

## Combined object inheritance

Dominions Enhanced first rewrites the Grand Hierophant with:

- S2;
- path cost 20;
- base Pretender cost 30;
- HP 10, MR 18, and human item slots;
- 50 points of bad-event prevention;
- Disease Resistance 100.

Divinitus loads afterward and sets:

- base Pretender cost 150;
- all known non-priest magic paths +1 through `#magicboost 53 1`;
- bad-event prevention 75;
- Disease Resistance 100;
- the anointing, teaching, and site-search description and events.

Because Divinitus does not clear magic or reset the path cost in this block, the earlier DE S2 and path-cost values remain in the combined object unless another later command changes them. This is a load-order conclusion and should be confirmed in the Pretender screen.

## Paths known +1

The Grand Hierophant adds one effective level to known non-priest paths.

Strategic consequences:

- purchased path thresholds may be one level easier;
- battlefield and ritual access must be calculated from effective, not merely purchased, paths;
- bless path requirements and design costs must still use the Pretender interface's actual rules;
- path loss, transformation, and boosters require live verification.

The phrase does not mean the Pretender knows every path. It boosts paths that are known.

## Mystic anointing

The source event:

- requires the Grand Hierophant as god;
- targets a Mystic or Erytheian Mystic;
- requires a temple;
- adds Holy;
- transforms the target into monster 382, the Mystic Prophet;
- is hidden from the event log.

The mod description states that one Mystic at a temple is anointed each month, becoming H1 and sacred.

### Strategic uses

Anointed Mystics can potentially provide:

- sacred researchers;
- H1 communion participants;
- temple builders and preachers;
- bless access in battle;
- priest support without Archousa recruitment;
- targets for the teaching event.

### Operational requirement

Maintain:

- at least one eligible Mystic in a temple province;
- enough temple coverage to place trainees without disrupting the front;
- a record of which Mystic random is being transformed;
- a protected training hub.

### Test pending

The exact preservation of:

- random magic paths;
- experience;
- items;
- age;
- orders;
- recruitment identity;
- prophet interactions

must be reproduced through the transformation.

## Teaching deeper mysteries

The source event for Mystic Prophets:

- requires the Grand Hierophant in the same province;
- requires positive dominion;
- uses `#req_domchance 5`;
- checks the target's Astral threshold through `#req_targnopath3 4`;
- adds +1 Fire, Water, Earth, and Astral simultaneously.

The description expresses this as candles times 5% chance and a maximum of three.

### Probability

If `#req_domchance 5` behaves as described, the monthly success chance at \(c\) friendly candles is:

\[
p = 0.05c
\]

| Candles | Monthly chance |
| ---: | ---: |
| 1 | 5% |
| 3 | 15% |
| 5 | 25% |
| 7 | 35% |
| 10 | 50% |

The probability of at least one success after \(n\) eligible months is:

\[
1-(1-0.05c)^n
\]

At five candles, six eligible months give:

\[
1-0.75^6 \approx 82.2\%
\]

### Path consequence

One success turns a typical Mystic Prophet into a much broader caster. Repeated success can create:

- multi-element communion masters;
- ritual cross-paths otherwise impossible in vanilla;
- high independent casters;
- forgers who compress several national roles.

### Source discrepancy

The prose says paths rise to a maximum of three. The event block visibly gates on an Astral-path condition and then boosts all four paths. A Mystic beginning at F2S1 could, under a literal reading of the commands, receive two successful boosts before Astral reaches three, potentially producing F4.

This is not asserted as engine behaviour. It is a high-priority controlled test because:

- command semantics may cap the other paths;
- transformation may alter the starting paths;
- the event requirement may behave differently from the literal reading;
- another hidden engine rule may enforce the prose maximum.

Until tested, the public doctrine uses the stated cap of three and records elemental over-cap as **test pending**.

## Site-search treasure

The source event:

- requires the Grand Hierophant;
- requires the Site Searching order on land;
- requires positive dominion;
- uses candles times 5% chance;
- grants 150 gold;
- grants 1d6 of each elemental gem.

“Elemental” means Fire, Air, Water, and Earth in the mod description.

### Conditional value

On success, expected gem gain is:

\[
4 \times E(1d6) = 4 \times 3.5 = 14
\]

At \(c\) candles, ignoring caps or event interactions, expected monthly value is:

\[
E(\text{gold}) = 150(0.05c)=7.5c
\]

\[
E(\text{total elemental gems}) = 14(0.05c)=0.7c
\]

| Candles | Expected gold / search month | Expected total elemental gems / search month |
| ---: | ---: | ---: |
| 1 | 7.5 | 0.7 |
| 3 | 22.5 | 2.1 |
| 5 | 37.5 | 3.5 |
| 7 | 52.5 | 4.9 |
| 10 | 75 | 7 |

These are expected values, not guaranteed yields.

### Opportunity cost

The Grand Hierophant's search month could instead be:

- researching;
- forging;
- casting a ritual;
- moving;
- joining a battle;
- teaching at a different hub;
- preaching or performing another Pretender task.

Site searching is attractive when:

- friendly dominion is high;
- unsearched provinces remain;
- elemental gems unlock immediate DE summon or battle packages;
- the Pretender is not needed on the front.

It is unattractive when the expected treasure does not beat the deadline value of another order.

## Training-hub doctrine

A Grand Hierophant training province should contain:

- temple;
- laboratory;
- strong friendly dominion;
- eligible Mystic Prophet;
- guards and fortification;
- no unnecessary exposed gem stock;
- access to the front through a safe route.

The hub converts time into exceptional mages. It also concentrates the Pretender and valuable Mystics into an obvious remote and conventional target.

Security includes:

- dome consideration;
- patrols;
- scouts on adjacent provinces;
- reserve troops;
- an evacuation route;
- alternate laboratories;
- avoiding the capital if that creates one catastrophic target.

## Grand Hierophant strategic families

### Research-and-training family

Prioritises:

- high Magic scale;
- early Mystic production;
- temple network;
- protected training hub;
- ritual paths that trained Mystics can complement.

Risk:

- too much stationary investment;
- delayed first-war force;
- Pretender time consumed by teaching and searching.

### Elemental-treasure family

Prioritises:

- high dominion candles;
- systematic site searching;
- DE elemental summon ladder;
- rapid conversion of found gems.

Risk:

- expected-value variance;
- Pretender absent from critical operations;
- gathering gems without research or casters to spend them.

### Battlefield-hierophant family

Prioritises:

- combat paths and survivability;
- trained Mystics as battlefield masters;
- healing support;
- an awakening timed for war.

Risk:

- sacrificing the mod's unique economic and training effects;
- exposing the central Pretender and training engine.

### Ritual-platform family

Prioritises:

- paths missing after accounting for DE summon ladders;
- legendary ritual thresholds;
- booster and forge plan;
- imprisoned or dormant timing if the recruitable state can survive.

Risk:

- paying for paths the DE nymph ladder would have supplied more cheaply;
- planning rituals before the gem economy exists.

# Part XII: Combined-Mod Strategy

## What the combined ruleset changes

The combined nation has three compounding engines:

1. cheaper and broader combined-arms recruitment;
2. DE's national constellation and nymph summon ladder;
3. Divinitus Grand Hierophant training and treasure.

This creates exceptional upside but also severe attention demands.

The player must track:

- Mystic randoms;
- anointed status;
- training history;
- geography for summons;
- national spell research;
- constellation compatibility;
- multiple gem colours;
- hero and unique availability;
- ordinary fronts and Thrones.

## Combined opening priorities

A coherent opening selects one primary engine.

### Military opening

- use improved Hoplites, Hypaspists, Phalangites, cavalry, and elephants;
- build forts;
- keep Grand Hierophant support secondary until borders stabilise.

### Mystic training opening

- prioritise temple and Mystic production;
- accept a slower mundane expansion only if tests prove it;
- protect the training centre;
- research spells that make the first enhanced Mystics immediately useful.

### Summon-ladder opening

- secure forest, mountain, and swamp provinces;
- reach the relevant Conjuration levels;
- preserve N2 and W2 specialists;
- use Grand Hierophant treasure to finance elemental bottlenecks.

Attempting all three at maximum speed is likely to produce too few troops, too few forts, and half-completed research.

## Combined magic compression

A trained Mystic can receive simultaneous F/W/E/S growth. DE then offers:

- constellation spells requiring S plus an element;
- elemental and Nature summons;
- national items;
- high Astral hero and Titan rituals.

This compresses jobs that would otherwise require several masters.

Potential trained roles include:

- S4F1 Aries caster;
- S4W1 Cetus caster;
- S4E1 Taurus caster;
- E2S2 Keledone ritual caster;
- F3E3 Brass Bull caster;
- W3 ritual caster for Oceanid or Eleionomae;
- broad independent Power of the Spheres caster.

Each role must be checked against:

- actual post-training paths;
- ritual versus battle restrictions;
- boosters;
- research;
- gem stock;
- whether using the mage consumes an irreplaceable training product.

## Combined path priorities

The Pretender should avoid buying paths that the nation can obtain reliably and cheaply through DE unless timing justifies them.

### More valuable Pretender paths

- paths required before summon ladders mature;
- paths that unlock national rituals with no cheap bridge;
- paths supporting an awake expansion role;
- paths needed for a specific global or legendary ritual;
- paths that improve blesses used by a meaningful sacred roster.

### Less valuable redundant purchases

- high Nature bought solely to reach N3 when N2 Archousai plus a booster can begin the ladder;
- high Air bought solely for eventual access when Oreiads and Daughters can supply it in time;
- broad elements bought without a ritual, battlefield, bless, or forging job.

Redundancy can still be worth paying for when it removes a deadline or geography dependency.

## Combined counter surfaces

The combined nation can be attacked through:

- temple and training-hub destruction;
- capital pressure against Astrologers and unique site troops;
- raids on forests, mountains, and swamps required for summons;
- gem denial;
- assassination of trained Mystics;
- communion clears;
- anti-Astral Magic Duel tactics;
- resistance to the chosen constellation;
- simultaneous fronts that overload attention.

The correct defence is not a larger single army. It is redundancy across:

- temples;
- labs;
- trained casters;
- access routes;
- gem stores;
- battlefield packages.

# Part XIII: Controlled Tests

## Test standard

Every test record should include:

- Dominions version;
- mod names, versions, and load order;
- game settings;
- nation and Pretender;
- turn and province;
- relevant units, paths, items, gems, and scripts;
- expected result;
- observed result;
- replay or save identifier;
- whether the result was repeated;
- conclusion and confidence.

Change one major variable at a time.

## Test 1: Mystic random distribution

**Question:** Does the current unmodded and modded Mystic use the documented guaranteed FWES roll plus independent 50% F/W/E rolls?

**Method:**

1. Recruit at least 128 Mystics under unmodded 6.35.
2. Record exact F/W/E/S paths.
3. Compare F2, W2, E2, and S2 frequencies with 12.5%, 12.5%, 12.5%, and 25%.
4. Confirm no E2S2 or double-elemental-2 result appears.
5. Repeat with DE 2.16.
6. Repeat with both mods.

**Purpose:** detect current-data or mod inheritance errors, not prove random fairness from a small sample.

## Test 2: Astrologer rare random

**Question:** Does the 10% extra random operate independently and can it produce S5 or an elemental level 2?

**Method:**

1. Recruit a large Astrologer sample in a debug or long test.
2. Record S3/S4/S5 and elemental results.
3. Compare with the derived 73.125%, 26.25%, and 0.625% Astral distribution.
4. Repeat under DE.

## Test 3: Starting-army expansion

**Question:** Which independent classes can the starting twenty Peltasts and twenty Hoplites defeat with acceptable losses?

**Method:**

1. Use fixed settings and no combat Pretender.
2. Test ordinary infantry, barbarians, heavy cavalry, crossbows, and heavy infantry.
3. Vary only formation and orders.
4. Record body losses, commander safety, battle duration, and next-turn readiness.

## Test 4: Elephant package sizing

**Question:** How many elephants and screening bodies produce reliable expansion under the chosen independent strength?

**Method:**

1. Test several small counts rather than one large army.
2. Use identical target classes.
3. Record routs, friendly trample, elephant wounds, and economic replacement.
4. Compare screen types.
5. Repeat under DE because ordinary troop performance changes.

## Test 5: Chariot versus elephant

**Question:** Against which targets does the cheaper chariot produce a better gold and attrition result than the elephant?

**Method:**

- compare equal gold values;
- test light infantry, archers, heavy infantry, and large units;
- record total package survival, not only mounts.

## Test 6: Hoplite versus Hypaspist

**Question:** When do three extra Protection points outperform Defence, Morale, movement, and lower resources?

**Method:**

- equal gold;
- equal resources;
- equal frontage;
- low-damage swarm;
- high-damage infantry;
- giants;
- armour-destruction support;
- long fatigue battle.

Repeat under vanilla and DE, where both units change materially.

## Test 7: Formation density

**Question:** How do formation fighters perform under area damage and frontage pressure?

**Method:**

- dense versus ordinary formation;
- equal troop count;
- melee-only opponent;
- area evocation opponent;
- fatigue-cloud opponent;
- trample opponent.

Record contact timing, attacks delivered, casualties by square, and rout timing.

## Test 8: Independent casting versus communion

**Question:** At what battle size does a communion outperform the same number of independent Mystics?

**Method:**

1. Select a single enemy army and research level.
2. Test eight independent Mystics.
3. Test four slaves and four masters.
4. Test six slaves and two masters.
5. Equalise gems.
6. Record useful casts, fatigue, slave wounds, enemy kills, and mage survival.

## Test 9: Communion collapse

**Question:** Which master scripts overload two-, four-, and eight-slave communions?

**Method:**

- record each master path before and after communion;
- use exact five-spell scripts;
- test battle lengths beyond the script;
- remove one slave through controlled damage;
- observe threshold loss and fatigue cascade.

## Test 10: Shared self-buffs

**Question:** Which Mystic master self-buffs are shared with slaves and how do they change fatigue relationships?

**Method:**

- Power of the Spheres;
- Phoenix Power;
- Summon Earthpower;
- personal resistance and protection spells;
- compare slave effective paths and fatigue before and after.

## Test 11: Magic Duel policy

**Question:** How does enemy low-S duel pressure affect S2 Mystics and S3-S5 Astrologers?

**Method:**

- one opposing duellist per target class;
- repeated trials;
- record deaths and surviving caster value;
- compare independent deployment and communion.

## Test 12: Mind Hunt and healing

**Question:** How valuable is national healing after failed or detected Mind Hunts?

**Method:**

- S4 Astrologer against provinces with and without enemy Astral;
- record feeblemind, death, and other outcomes;
- move survivors to Hiereia and Archousa provinces;
- record recovery time and failures.

## Test 13: Scrying and glamour

**Question:** What exact information does automatic dominion scrying reveal in 6.35?

**Method:**

- ordinary army;
- glamoured units;
- stealth units;
- hidden commander;
- fort construction;
- adjacent and same-province dominion states;
- disciple partner view.

Compare with scout, spy, and ritual scrying reports.

## Test 14: Hiereia outside-fort recruitment

**Question:** Which province types and structures allow Hiereia recruitment under vanilla and DE?

**Method:**

- every land terrain;
- with and without fort;
- with and without lab;
- with and without temple;
- record recruitment interface and requirements.

## Test 15: Healing allocation

**Question:** How are Healing 1 and Healing 3 attempts allocated among multiple afflicted units?

**Method:**

- identical afflicted units;
- mixed affliction severity;
- ordinary, sacred, mounted, magic-being, undead, and inanimate cases;
- repeat over enough months to distinguish impossibility from variance.

## Test 16: DE paired Heart Companions

**Question:** When and how does one 9322 recruitment become two unit-747 Heart Companions?

**Method:**

- recruit at Tower and Gymnasium;
- observe recruitment queue, arrival, seasonal shape, event timing, upkeep, experience, and squad assignment;
- verify whether both bodies receive bless and equipment changes;
- test losses before and after transformation.

## Test 17: DE inherited unit cards

**Question:** What are the final costs and inherited attributes of Hetairoi, Hipparchus, and other copied objects?

**Method:**

- capture full live unit cards;
- compare with copied vanilla source object;
- record every explicit override;
- verify rider and mount separately.

## Test 18: DE constellation exclusivity

**Question:** How do Aries, Cetus, Taurus, Libra, and Light of the Northern Star replace or block each other?

**Method:**

- cast each alone;
- cast two in both orders;
- use opposing Arcoscephalian casters;
- inspect path boosts, battlefield effects, duration, and message log.

## Test 19: DE summon geography

**Question:** Which terrain flags satisfy forest, swamp, mountain, border mountain, cave, and underwater restrictions?

**Method:**

- test every nymph ritual in each plausible terrain combination;
- test forted and unforted provinces;
- test alternate planes;
- record ritual availability before spending gems.

## Test 20: Oceanid randoms

**Question:** Does `#custommagic 29952 300` produce three independent picks from Air, Earth, Death, Nature, and Glamour as expected?

**Method:**

- summon a statistically useful sample;
- record duplicates and maxima;
- compare access probabilities;
- identify deadline-safe and portfolio-only outcomes.

## Test 21: Grand Hierophant inheritance

**Question:** Under DE then Divinitus, what are the final S path, path cost, base cost, item slots, bad-event prevention, and magic boost?

**Method:**

- inspect the Pretender selection screen;
- buy one level in several paths;
- create the Pretender;
- compare design display and in-game unit card;
- reverse the load order in a separate test to demonstrate why the supported order matters.

## Test 22: Mystic anointing

**Question:** Is an eligible Mystic anointed every month, and what survives transformation?

**Method:**

- one target at a temple;
- several targets at one temple;
- targets at several temples;
- no target;
- target carrying items;
- target with experience and a rare random;
- record selection, timing, and preserved attributes.

## Test 23: Grand Hierophant teaching cap

**Question:** Can an elemental path exceed three when an S1 Mystic begins with F2, W2, or E2?

**Method:**

1. Anoint a known F2S1 Mystic.
2. Place it with the Grand Hierophant in high dominion.
3. Repeat until two training successes or the event stops.
4. Record F and S after each success.
5. Repeat with S2 and ordinary elemental starting paths.

This directly resolves the prose-versus-event ambiguity.

## Test 24: Site-search treasure

**Question:** Does the event chance equal candles times 5%, and does `1d6vis 51` grant one separate d6 of F/A/W/E?

**Method:**

- repeat searches at several candle values;
- record ordinary discovered sites separately;
- record event gold and each gem colour;
- compare success frequencies and conditional dice distribution;
- test provinces already fully searched.

## Test 25: Combined trained caster roles

**Question:** Which trained Mystic thresholds can be reached before a realistic first or second war?

**Method:**

- run full turn-20 and turn-30 economies;
- include temples, forts, labs, research, troop recruitment, and Pretender orders;
- record number and quality of trained Mystics;
- field one complete constellation or ritual package;
- compare against a military-first opening.

# Part XIV: Essays

## Essay I: The Nation Dossier as a Reproducible Argument

A nation guide is an argument about conversion. It begins with rules, claims that certain capacities follow, and recommends decisions intended to turn those capacities into victory. Like any argument, it can fail because a premise is false, a step is missing, or the conclusion exceeds the evidence.

The most common false premise is stale data. A guide remembers a gold cost, random path, spell level, or bless from another patch or another age. The prose may remain persuasive because the strategic vocabulary still sounds familiar. Yet the actual nation now recruits a different unit, pays a different opportunity cost, or cannot reach the claimed path. Version labels are not editorial decoration. They define the object being discussed.

The most common missing step is access. A national ritual is listed, so the writer says the nation can cast it. A mage reaches one of its paths, so the other path is assumed to appear through “boosters.” A communion reaches a battlefield threshold, so the same elevated mage is imagined casting a ritual next month. These statements collapse distinct systems. Rituals do not ordinarily borrow battlefield communion levels. Boosters require research, paths, gems, item slots, and forge turns. A hero may never arrive. A summon may require terrain the nation does not own.

The most common excessive conclusion is the universal build. A design succeeds on one map against one field and becomes “best.” But an awake expander, imprisoned scales build, and ritual platform purchase time in different currencies. One survives a rush, one compounds behind space, and one accesses effects after research. None can be evaluated without the expected deadline.

A reproducible dossier exposes every bridge. It says which unit casts the spell, which random produces the unit, how likely the random is, which item supplies the missing level, when the item can be forged, where the army assembles, which gem carrier accompanies it, and what happens if the opponent presents another defence.

This precision does not eliminate judgment. It improves judgment by showing where it enters. “The manual gives the Hoplite Protection 18” is a rule claim. “Hoplites are preferable to Hypaspists here” is doctrine based on enemy damage, resources, movement, and morale. Another player can disagree with the choice while accepting the data. That is productive disagreement.

Tests complete the argument. Expansion claims are played to turn 12 with real infrastructure. Communion scripts are allowed to continue after the fifth spell. Random distributions are sampled. Modded objects are read after load order. A battle replay is not used merely to announce victory; it is used to see contact timing, target selection, fatigue, and the first point of failure.

The finished dossier is neither a recipe nor a plain encyclopaedia entry. It connects verified facts to conditional plans, with a method for correcting each one when the situation changes.

## Essay II: Arcoscephale and the Conversion of Knowledge

Arcoscephale's most distinctive resource is not Astral pearls or heavy infantry. It is the ability to turn information into tailored force.

Automatic scrying inside dominion gives the kingdom unusually good reports where it is politically strongest. Mystics then provide a probabilistic library of Fire, Water, Earth, and Astral tools. Astrologers deepen Astral. The combination invites a particular form of play: observe the approaching force, classify its defences, and assemble the appropriate package.

This promise is easy to exaggerate. Seeing an army does not defeat it. A report can reveal heavy infantry, but the E2 Mystic needed for Destruction may be in another laboratory. The research may be one level short. The Earth gems may be carried by a commander marching elsewhere. The only road may be blocked. Knowledge has strategic value only when the state can deliver the response before the deadline.

This is why fort distribution matters. Each fort supplies Research Points, another draw from the Mystic distribution, and another place from which a response cell can move. A larger mage portfolio reduces variance. A distributed laboratory network reduces distance. A gem reserve cuts preparation time. Scouts beyond dominion extend the warning horizon.

The same system explains the danger of losing a field army. An Arcoscephalian army often carries years of stored options: rare randoms, Astral pearls, boosters, and communion slaves that were also researchers. When destroyed, the loss is not measured only in battlefield gold. The nation loses response branches. An opponent who kills the E2 and S4 specialists may invalidate spells that remain fully researched.

Knowledge also has diplomatic value. Accurate reports discourage weak raids and reveal concentration. They allow credible warnings to allies and more reliable estimates of whether a neighbour is honouring a border. Yet information can make a player overconfident. Scrying inside dominion creates a sharp boundary: the interior feels visible, the exterior does not. Stealth, magic movement, and remote attacks exploit that comfort.

A mature Arcoscephalian state treats information as a chain:

```text
report
-> classification
-> response choice
-> caster and gem assignment
-> movement
-> battle evidence
-> revised classification
```

The final step matters. A report predicts. A battle replay teaches. The nation that learns faster eventually needs fewer mages and gems to solve the same problem.

## Essay III: Mystics, Probability, and Doctrine

The Mystic appears broad because any recruit can display several paths. The strategic reality is more exact. Every Mystic begins with S1, gains one guaranteed roll among Fire, Water, Earth, and Astral, then receives separate fifty-percent chances in each element. This creates abundance and constraint at the same time.

The abundance is obvious. Five of eight Mystics know any named element. More than one in five know all three. Every one can participate in an Astral communion. Several forts quickly produce a catalogue of point buffs, self-buffs, evocations, control spells, and forging cross-paths.

The constraint lies in doubled paths. F2, W2, and E2 each appear only one time in eight. E2S2 cannot occur naturally because the same guaranteed roll would have to be both Earth and Astral. Two elements cannot both reach level two on the same recruit. A strategy that remembers only the broad catalogue will eventually promise an impossible mage.

Probability changes recruitment doctrine. A one-in-eight result has an expected waiting time of eight recruits, but expectation is not a delivery date. After eight recruits there remains more than a one-third chance that no such specialist has appeared. A state that needs E2 for the first war must recruit from several forts, maintain an alternate branch, or use another access route.

Probability also changes the meaning of an individual mage. An F2 Mystic is more than a stronger F1. It is one of the nation's limited natural bridges to Phoenix Power, high Fire evocation, and particular forging paths. Assigning it as a communion slave may be correct, but the decision should be deliberate. The same body can serve as a researcher, master, ritual candidate, or battlefield caster, and those roles compete.

This competition explains why communions should be designed from spell packages rather than habit. Four slaves can raise a common F1 master to F3, but those four slaves could also have cast four independent Astral or elemental spells. The communion wins when path elevation and fatigue distribution produce effects that the independent group cannot match. It loses when the battle is small, the target can be solved by low magic, or enemy area attacks make concentration fatal.

The expert skill is not memorising every possible Mystic. It is managing a portfolio:

- label rare results;
- protect deadline-critical specialists;
- keep alternate branches;
- calculate at-least-one probabilities;
- compare independent and communal output;
- preserve enough researchers that victory today does not erase research tomorrow.

Under Divinitus, the Grand Hierophant can change the distribution after recruitment by teaching several paths at once. Portfolio thinking still matters because training introduces another scarce resource: time in high dominion with the Pretender present. The question is not only which Mystic arrived, but which one deserves the next training opportunity.

## Essay IV: Healing, Intelligence, and the Preservation of Force

Arcoscephale possesses two advantages that are easy to undervalue because neither directly kills an enemy: healing and automatic scrying. Together they improve force preservation.

Healing converts survivors into future capacity. A wounded elephant, Astrologer, combat Pretender, or thug may carry an affliction whose cost exceeds the hit points already restored. A damaged eye reduces precision. A crippled leg ruins movement. Feeblemind can remove a mage from useful service. Concentrated healers create a place where those losses can sometimes be reversed.

The useful economic comparison is not the healer's monthly wage against one cured affliction. It is the value of the unit's remaining lifetime. Restoring a rare S4 Astrologer may recover remote-magic and ritual access that would take many capital turns to replace. Restoring an ordinary Peltast is worth less. Healing allocation still has a strategic side even when the engine selects targets automatically, because players decide which units gather in the province and how long they remain.

Scrying reduces the wounds that need healing. Seeing the enemy approach allows the nation to avoid presenting elephants to fear, Mystics to flyers, or Hoplites to armour destruction. It permits the correct reserve to move before contact. It also allows damaged units to withdraw through safer routes.

Neither system eliminates risk. Healing cannot restore the dead and may not cure the desired affliction immediately. Scrying does not reveal every stealth or magic-phase threat and only functions where dominion supplies the view. Overreliance produces predictable failures: the combat Pretender attacks because “the priestesses will heal it,” or the capital is left open because “scrying sees everything.”

Preservation requires a full cycle:

```text
observe threat
-> choose favourable engagement
-> protect valuable bodies
-> win with survivors
-> withdraw damaged assets
-> heal and reassign
```

The final word is reassign. A recovered unit should return to the role its current body and strategic value justify. A once-wounded elephant may rejoin expansion. A recovered Mind Hunter may return to a rear laboratory. A Pretender healed after a narrow victory may be more valuable forging or deterring than repeating the same gamble.

## Essay V: From Classical Army to Astral State

The visual identity of Middle Age Arcoscephale is classical warfare: spear lines, bronze, chariots, and elephants. The strategic identity is a transition away from dependence on those bodies.

In the first year, ordinary troops seize the economy. Hoplites absorb common weapons. Hypaspists move and defend. Peltasts and Cardaces provide affordable frontage. Elephants transform favourable size matchups into rapid routs. The army is not obsolete; it is the instrument that buys time and provinces.

Research changes what the army means. Earth magic can harden it or destroy the enemy's armour. Astral can make key squares ethereal, paralyse elites, or attack minds. Fire and Water can kill dense formations. Communions turn modest randoms into specialists. At this stage the troops are still combatants, but their greater function is to create time and targets for magic.

Later, the relation reverses. The mage state is the scarce offensive core. Troops screen it, hold forts, absorb attacks, provide siege bodies, and claim territory after remote or battlefield magic has broken resistance. A player who continues measuring strength only by the number of elephants will misread the nation.

This transition creates a tension. The old army is expensive in resources and attention; the Astral state is expensive in gold, laboratories, pearls, and mage-turns. Investing too early in magic produces a small realm that can research but not survive. Investing too long in troops produces a large realm that cannot answer modern counters.

The transition point is not a turn number. It arrives when:

- the next troop purchase adds less capability than the next Mystic;
- a research node defeats a class the army cannot;
- borders stabilise enough for forts to compound;
- enemy magic begins invalidating unbuffed troops;
- a siege or Throne operation requires more than field bodies.

Dominions Enhanced makes the transition richer rather than removing it. Cheaper and more mobile troops extend mundane relevance, while constellations, nymph summons, and Titans create a larger magical destination. Divinitus adds trained Mystics who can embody several elements at once. The classical army does not disappear. It becomes the territorial shell of an increasingly supernatural state.

## Essay VI: Geography as a Magic Path

Under Dominions Enhanced, forest, mountain, swamp, and water access become part of Arcoscephale's mage roster.

An N2 Archousa is not yet an Oreiad caster. She needs a Nature booster and a forest to contact a Karyatid. The Karyatid is strongest in forest and can help reach N4. N4 plus a mountain produces an Oreiad, which opens Air and Earth. A W3 caster in a swamp produces an Eleionomae with Death and Air. An S4 Astrologer eventually calls an immortal Daughter of Evening with Air.

The map contains latent paths. A nearby forest may be worth more than its income because it begins the Nature ladder. A swamp can become the nation's first reliable Death bridge. A mountain supports Oreiad contact and conjunction rituals. An underwater foothold enables Titans and the Scourge of the Deeps.

This changes expansion and diplomacy. Terrain is no longer valued only by income, resources, and fort geometry. A treaty that cedes the only safe swamp may also cede Death access. A raid that interrupts the mountain laboratory can delay the entire constellation or nymph programme. A fort built on the correct terrain protects a magical production node.

Geographic access has a cost: it is visible and contestable. A Pretender path travels with the Pretender. A terrain ladder depends on holding the province, building or preserving a laboratory, moving the caster, and surviving the ritual month. Opponents can read the same map and attack the bridge.

The expert response is to record terrain in the access ledger:

```text
N2 Archousa
+ Nature booster
+ forest laboratory
+ Conjuration 4
+ 20 Nature gems
= Karyatid
```

This notation makes two things clear. First, the access is real. Second, every component can be delayed or denied.

# Part XV: Reference Checklists

## Vanilla quick doctrine

- Expand with tested infantry, elephant, chariot, or Pretender packages.
- Budget the 300-gold laboratory with every fort.
- Recruit Mystics widely; record every random.
- Treat E2, W2, F2, and S4+ as portfolio assets.
- Use communions only when path elevation beats independent casting.
- Preserve the capital Astrologer pipeline.
- Use scrying as one layer of intelligence.
- Use Hiereiai outside forts and Archousai for concentrated healing.
- Bridge missing paths deliberately.
- Convert field victories into forts, laboratories, and Thrones.

## DE quick doctrine

- Recalculate the entire roster; do not use vanilla cost assumptions.
- Use cheaper improved infantry and new cavalry for mobility.
- Treat paired Heart Companions as a separate sacred economy.
- Exploit N2 Archousai.
- Secure forest, mountain, swamp, and water nodes.
- Choose one constellation per battle.
- Plan the nymph ladder from caster, booster, gem, research, and terrain.
- Protect unique summons and heroes.
- Capture live cards for inherited mod objects.

## Divinitus quick doctrine

- Confirm the final Grand Hierophant in the Pretender screen.
- Build temples where anointing can occur safely.
- Record which Mystic is transformed.
- Train in strong dominion.
- Compare teaching, site searching, research, forging, and war orders.
- Do not assume the stated path cap until tested.
- Convert elemental treasure into immediate packages.
- Protect the training hub without concentrating every irreplaceable asset there.

## Source register

### Official

- *Dominions 6 Manual*, revision 2:
  - Scouting and Scrying;
  - Healing and afflictions;
  - Communions;
  - spell and ritual tables;
  - MA Arcoscephale national summary and roster;
  - national spells and rituals.

### Supplied mod sources

- `DomEnhanced2_16.dm`
  - MA Arcoscephale unit definitions 9316-9323;
  - vanilla monster rewrites;
  - national sites;
  - nation 50 recruitment block;
  - national spells, items, heroes, and events.
- `Divinitus_1.15.3_DE.dm`
  - Grand Hierophant rewrite;
  - Mystic anointing;
  - teaching events;
  - site-search treasure event.

### Current structured and community cross-checks

- Dominions 6 Mod Inspector, maintained by larzm42;
- Illwiki Dominions 6 MA Arcoscephale page;
- current and historical community discussion used only for doctrine and hypothesis.

Community claims are not used to override official or source-confirmed object definitions without a recorded current test.

## Open research ledger

The highest-priority unresolved questions are:

1. current live Mystic and Astrologer random display under 6.36;
2. exact scrying interaction with glamour and stealth;
3. reliable expansion party ranges;
4. independent casting versus communion break-even;
5. DE inherited unit and spell-card values;
6. paired Heart Companion timing;
7. constellation replacement behaviour;
8. nymph custom-magic distributions;
9. Grand Hierophant combined inheritance;
10. Mystic Prophet transformation preservation;
11. teaching cap semantics;
12. treasure-event probability and gem colours.

These questions are deliberately visible. The dossier is already usable, but it should become more precise as controlled evidence replaces provisional labels.

# Part XVI: Middle Age Marignon, Fiery Justice

## Marignon one-page command brief

Marignon begins as an armoured human kingdom backed by crossbows, sacred cavalry, cheap Fire apprentices, Astral-capable Witch Hunters, powerful priests, and a capital pipeline of Grand Masters. Its first transition is from ordinary steel into coordinated Fire and Astral battle magic. Its later transition is into angelic summons and stronger strategic magic.

The nation is strongest when it uses each layer for the job it actually performs:

- crossbows punish armour and force shields;
- cheap heavy infantry hold space and add siege bodies;
- Knights of the Chalice provide concentrated sacred force rather than affordable frontage;
- Witch Hunters turn ordinary forts into Fire-Astral war colleges;
- Grand Masters supply high paths, random Air or Earth access, and the best communion masters;
- Inquisitors and freely recruitable Friars turn dominion control into a campaign tool;
- Architects improve the fort network and shorten sieges;
- national angel rituals convert Conjuration research and Astral pearls into mobile sacred power.

The main limits are just as important. Marignon has no dependable native Water, Death, Nature, Blood, or Glamour. Its best mage is capital-only, expensive, and consumes four recruitment points. Much of the army wears enough armour to care about fatigue, armour destruction, and battlefield-wide elemental damage. A plan that only adds more heavy infantry eventually meets a counter it cannot out-armour.

## Marignon evidence and ruleset

The roster and national rules below use the revision-2 official manual. Grand Master randoms are resolved through the pinned 6.35 Inspector export: `F3 S2 H2`, one guaranteed level from Fire, Air, Earth, or Astral, plus an independent 10% second level from the same set. Advice is labelled strategy. Exact expansion counts remain test dependent because map strength, independent composition, scales, bless, formations, and commander quality change the result.

## Marignon conversion chain

```text
crossbows, armour, and sacred cavalry
-> safe expansion and defensible borders
-> forts, laboratories, and Architects
-> Witch Hunters at ordinary forts
-> Fire-Astral battlefield packages
-> Grand Master communions and boosters
-> angels, remote reach, and Throne operations
```

The chain can break in three common places. Excess cavalry delays forts. Too many Initiates produce research without enough Astral organisers. Too many Grand Masters consume capital time and gold before the wider fort network can support them.

## National rules that shape the plan

| Rule | Practical consequence |
| --- | --- |
| Order limit +1 | Marignon can lean further into Order when the economy and recruitment plan justify it. |
| Bless points +3 | A useful sacred package does not require the Pretender to pay for every point alone. |
| Inquisition | Inquisitors remove enemy dominion and can spread friendly dominion up to one candle in owned provinces. |
| Friars outside forts | Priest coverage, preaching, and army leadership do not consume a fort commander slot everywhere. |
| Architects | The capital can produce commanders that build better forts and provide +15 siege strength. |
| Standard forts | The nation still needs a deliberate fort-and-laboratory budget; the Architect improves the result but does not pay for it. |

Inquisition is not merely defensive flavour. It supports border conversion, weakens hostile dominion effects, and helps sacred forces operate under their own bless. It is still slower than winning the province and building infrastructure. Priests should support the campaign rather than replace it.

## Marignon roster by job

| Unit | Best job | Important limit |
| --- | --- | --- |
| Crossbowman | Armour pressure, supporting fire, cheap ranged mass | Ordinary precision and friendly-fire risk; needs a screen |
| Pikeneer | Anti-large line and repel pressure | Low Defence and ordinary damage when the length advantage is irrelevant |
| Halberdier | Armour-piercing line damage and siege mass | Slow, heavily armoured, vulnerable to fatigue and missiles without shields |
| Swordsman | General heavy infantry and high-damage strikes | No shield and the same fatigue problem as the other heavy line troops |
| Man at Arms | Better-defended line and bodyguard-quality infantry | Higher gold, resources, and recruitment-point demand |
| Flagellant | Cheap sacred mass, patrol or siege body, disposable pressure | No armour, poor Defence, and losses can become expensive when the bless is overbuilt around them |
| Royal Guard | Durable non-sacred cavalry and mobile reserve | Very expensive in resources and recruitment points |
| Knight of the Chalice | Sacred shock cavalry and decisive flank | Seventy gold, heavy resource and recruitment demand, and a mount that remains a separate target |

The ordinary expansion army should normally combine a protected line with crossbows. Pikes are selected when large targets justify them. Great weapons are selected when armour is the problem. Sacred cavalry is used where the charge and survivability change the battle enough to justify its price. Mixing every unit into every party hides which piece is doing useful work.

## Marignon commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Initiate | F1 | Cheap research, light Fire support, site searching | Two recruitment points for a narrow mage; do not let cheap gold cost hide the fort-turn cost |
| Inquisitor | F1 H2, Inquisitor | Dominion work, blessing, banishment, leadership | Better at religious operations than research efficiency |
| Witch Hunter | F2 S1 H1, Patrol +10 | Core researcher, communion member, Holy Pyre caster, patrol support | Costs 260 gold and two recruitment points; field losses damage both research and war capacity |
| High Inquisitor | F1 H3, Inquisitor | Strong preaching, large blessings, claims, banishment | Capital-only and four recruitment points |
| Grand Master | F3 S2 H2 plus FAES randoms | High research, communion master, boosters, angels, high Fire and Astral | Capital-only, 520 gold, four recruitment points |
| Architect | Mason, Siege +15 | Better forts, siege acceleration | Capital commander turn competes directly with Grand Masters and High Inquisitors |
| Friar | H1, recruitable outside forts | Cheap priest coverage and ordinary leadership | Not a replacement for a battle mage |
| Assassin, Scout, Troubadour | Stealth operations | Information, commander pressure, deception | Outcomes are matchup dependent and can create diplomatic consequences |

### Reading the Grand Master random

The guaranteed random gives a nominal 25% result in Fire, Air, Earth, or Astral. The independent 10% second roll slightly raises the chance of seeing at least one chosen path to 26.875%. A double result in the same chosen path occurs only 0.625% of the time.

This produces several distinct assets:

- F4 reaches stronger Fire thresholds without a battlefield boost;
- S3 casts the first national angel ritual directly and improves Astral work;
- A1 opens Air searching and low-level utility, but it does not make Marignon a broad Air nation;
- E1 opens Earth searching and can begin an Earth booster or Summon Earthpower route;
- rare doubled results are bonuses, not requirements on which an opening should depend.

Every Grand Master should be labelled by random immediately. An unrecorded E1 or A1 roll can sit in a laboratory for years while the nation mistakenly plans around a path it believes it lacks.

## Marignon opening priorities

The opening has four simultaneous jobs:

1. expand with a tested infantry, crossbow, sacred, or Pretender package;
2. preserve enough gold and resources for the next fort;
3. begin recruiting Witch Hunters wherever laboratories exist;
4. use the capital on the scarce asset actually needed: Grand Master, Architect, High Inquisitor, or sacred cavalry.

The default capital choice is not automatically a Grand Master every month. An early Architect can create better long-term fort geometry. A High Inquisitor may be necessary for a Throne or dominion emergency. The correct capital queue follows the national bottleneck.

### Expansion packages to test

| Package | Intended target | Failure signal |
| --- | --- | --- |
| Armoured line plus crossbows | Ordinary infantry and armoured independents | Fast flankers reach the crossbows or missile fire causes unacceptable friendly loss |
| Pikes plus supporting fire | Large animals and cavalry | Small high-Defence troops ignore the length advantage and win the melee |
| Knight-led shock force | Weak lines and exposed ranged troops | Dense anti-large weapons, fatigue, or magic-resistant damage remove the expensive front |
| Awake Pretender plus minimal escort | Rapid tempo and difficult early provinces | The god is taking afflictions, being trapped, or delaying the economic design it was meant to enable |

No fixed troop count is presented as universal. The useful range comes from replaying the actual local independent types under the chosen scales and bless.

## Marignon research response tree

### Trunk: make Witch Hunters operational

```text
Thaumaturgy 1
-> Conjuration 3
-> Evocation 4
```

- Thaumaturgy 1 opens Communion Master and Communion Slave.
- Conjuration 3 supplies Power of the Spheres for Astral casters and Phoenix Power for Fire casters.
- Evocation 4 opens the national Holy Pyre: an F2 armour-piercing area spell with a large base area, available to every Witch Hunter.

This is a real first-war package because an ordinary fort can recruit the caster. It still needs range, formation, gem, fatigue, and friendly-fire checks before battle.

### Branch A: heavier Fire and Astral fighting

Continue into Evocation 5 when Falling Fires, Stellar Cascades, or another current spell solves the observed enemy. Fire resistance can make a pure Fire branch poor. High-MR targets can reduce some Astral control packages. The army should carry at least two damage mechanisms rather than asking one school to defeat every defence.

### Branch B: protect the mundane army

Alteration 3 gives S1 Witch Hunters Body Ethereal and other defensive tools. Construction 2 and 4 open practical equipment and Earth support when the right Grand Master exists. This branch is strongest when ordinary troops are still winning contact but need help surviving the enemy's damage.

### Branch C: national angel ladder

| Research | National ritual | Native route |
| --- | --- | --- |
| Conjuration 5 | Contact Angel of the Host, S3, 7 pearls | S3 Grand Master or an S2 caster with a named boost |
| Conjuration 6 | Angelic Choir, S3, 15 pearls | Same S3 route; produces three H2 flying sacred mages |
| Conjuration 6 | Contact Harbinger, S4, 25 pearls | Higher Astral access; supplies an A3 H2 flying commander |
| Conjuration 7 | Heavenly Wrath, S3 F1, 35 pearls | S3 Grand Master already meets Fire |
| Conjuration 7 | Angelic Host, S5, 50 pearls | Communion, boosters, or imported access |
| Conjuration 9 | Heavenly Choir, S7 F2, 144 pearls | Endgame project, not an ordinary extension of the opening |

Contact Angel of the Host is the first clean conversion point. It turns a reachable S3 Grand Master and seven pearls into a flying sacred combat body. Contact Harbinger is an access project as much as a summon: its A3 H2 path line can widen Air magic and support mobile operations.

## Marignon battlefield packages

### Holy Pyre battery

- protected infantry establishes contact;
- crossbows punish armour before and during contact;
- Witch Hunters cast Holy Pyre from safe range;
- an Astral package protects or controls the most important squares;
- a reserve handles fire-resistant or highly mobile targets.

The spell is national, but the formation is not automatic. Large area can punish friendly troops if the battle line collapses into the target zone.

### Small communion

Use a small communion only when the path gain creates a named spell package. Count every master cast and every slave's relative path. Witch Hunters are expensive enough that disposable-slave doctrine can lose the research war even after winning one battle. Book V owns the fatigue and collapse arithmetic.

### Angel-supported mobile force

Flying angels solve movement and target-access problems that ordinary heavy infantry cannot. They still need intelligence, retreat routes, and enough conventional mass to hold what they take. A seven-pearl Angel of the Host should not be traded for trivial Province Defence merely because it flies.

## Marignon Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Scales and path bridge | Economy, missing Nature/Death/Water/Blood/Glamour, high Astral or Air | A dormant or imprisoned bridge does not help an early war |
| Moderate sacred bless | Knights and Flagellants without sacrificing the whole economy | The two sacred types have different bodies and failure modes |
| Awake expander | Early tempo and difficult neutral provinces | Marignon already has expansion tools; the god must repay its opportunity cost |
| Angel and endgame enabler | S5-S7, stronger Air, globals, and ritual economy | Researching the ritual is not the same as owning pearls and a safe caster |

A durable, resistance-aware bless generally serves sacred cavalry more reliably than a narrow damage gimmick. Flagellants may value different effects because their main problem is surviving contact. The final design should test both bodies separately, including the sacred mounts.

## Marignon matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Heavy armour | Crossbows, great weapons, Holy Pyre, armour reduction | Buying only more sword infantry |
| Fire resistance | Astral control, mundane armour pressure, angels, imported paths | Assuming F3-F4 automatically converts into damage |
| Mass undead | Priests, H3 support, morale-safe formations, Fire where applicable | Sending expensive priests forward without screens |
| Flyers and assassins | Patrollers, bodyguards, dispersed command, protected mages | One exposed communion master holding the entire plan |
| Armour destruction or fatigue | Wider spacing, ranged pressure, quicker battles, alternate troops | Treating protection as permanent |
| High Magic Resistance | Physical and Fire pressure, buffs, summons | Overcommitting to resistible single-target control |

## Monthly Marignon audit

- Which capital asset is the current bottleneck?
- Is the next fort followed immediately by a laboratory and Witch Hunter queue?
- Are Grand Master randoms recorded?
- Can the first-war spell be cast by a repeatable mage?
- Does the army have a non-Fire answer?
- Are priests changing dominion where the army will actually fight?
- Are Knights of the Chalice earning more than their fort and resource cost?
- Is Conjuration research attached to an affordable pearl budget?
- Which missing path is being solved by the Pretender, a summon, or an import?

## Marignon verification ledger

Open work remains narrow:

1. expansion ranges for each common independent class;
2. current live confirmation of the 6.35 Grand Master random display;
3. Holy Pyre targeting and friendly-fire formations across battlefield sizes;
4. small-communion fatigue budgets using Witch Hunters and Grand Masters;
5. angel package survival, upkeep, and return on pearl cost;
6. Architect timing versus repeated Grand Master recruitment;
7. DE and Divinitus changes kept in separate ruleset appendices.

# Part XVII: Middle Age Pyrène, Time of the Akelarre

## Pyrène one-page command brief

Pyrène combines unusually resilient human troops with mobile Air-Blood witches, blood-sacrificing priests, forest-recruitable Akerbeltz, cave recruits, and a capital sacred cavalry arm. The nation is not merely "Blood with knights." Its real advantage is distributed recruitment. Forests, caves, mountains, and ordinary forts can each add a different part of the state.

The opening should convert that geography into capacity:

- forts recruit the ordinary army, Sorginak, and Bishops;
- non-fort forests can recruit Akerbeltz;
- non-fort provinces can recruit path-random Pyrènian Monks;
- non-fort caves and the capital can recruit Bekryde scouts, leaders, and troops;
- the capital produces Emerald Knights and Emerald Counts;
- Blood and Nature then turn population, slaves, and terrain access into a growing magical economy.

The nation has clear weaknesses. Most human troops and leaders have Magic Resistance 9. The best sacred cavalry is capital-only and extremely resource intensive. Crossbows have Precision 8. Akerbeltz are expensive four-point commanders. Native Astral, Death, Water, and Glamour are absent. Air begins at A2, which is useful but does not by itself cast every famous Air spell or the national A3 ritual.

## Pyrène evidence and ruleset

The official revision-2 manual supplies the roster, national summary, and Send Aatxe. The pinned 6.35 Inspector export resolves randoms:

- Pyrènian Bishop: `B1 H2` plus one guaranteed Fire, Earth, or Blood level;
- Pyrènian Monk: `H1` plus one guaranteed Fire, Earth, Nature, or Blood level;
- Sorgina: fixed `F1 A2 B2`;
- Akerbeltz: `E1 N2 B3`, one guaranteed Earth, Nature, or Blood level, plus an independent 10% second roll from the same set.

These are unmodded records. Dominions Enhanced and Divinitus must be treated as separate rosters.

## Pyrène conversion chain

```text
resistant infantry, crossbows, and cavalry
-> forests and caves secured during expansion
-> distributed commanders and blood hunters
-> Akerbeltz crossbreeding and Nature-Earth support
-> Sorgina Air-Blood battlefield groups
-> slave economy, blood rituals, and remote pressure
-> mobile sacred and supernatural armies
```

Pyrène can own many commanders while still lacking the right package. Distributed recruitment only becomes an advantage when every location has a declared job and the roads, laboratories, and blood-slave routes connect them.

## National body and terrain rules

The ordinary Pyrènian and Bekryde roster has partial resistance to Fire and Cold, darkvision, and broad Mountain Survival. Those traits matter most when the nation deliberately chooses terrain and opponents that make them relevant. Five points of resistance softens common elemental damage; it is not immunity to concentrated battlefield magic.

| Geographic asset | What it can produce | Strategic use |
| --- | --- | --- |
| Forest without a fort | Akerbeltz | Expensive high Blood-Nature-Earth mage production outside the normal fort queue |
| Cave without a fort | Bekryde troops, scout, and leader | Cheap local bodies, information, and mountain-capable reinforcement |
| Any suitable non-fort province | Pyrènian Monk | Distributed H1 and one random path from F/E/N/B |
| Capital | Emerald sacred cavalry and Akerbeltz | Sacred shock force and the most reliable elite mage point |
| Ordinary fort | Main human army, Sorgina, Bishop | Repeatable military and magic core |

The extra Turmoil design limit is permission, not a command. Blood hunting, expensive commanders, forts, and knights still depend on population and gold. A high-Turmoil design needs a clear compensating engine rather than assuming national flavour makes lost income harmless.

## Pyrène roster by job

| Unit | Best job | Important limit |
| --- | --- | --- |
| Bekryde and Bekryde Warrior | Cheap cave and mountain-capable line or siege mass | Low MR and light armour; local availability controls scale |
| Pyrènian Crossbowman | Armour pressure behind a screen | Precision 8 and ordinary protection |
| Pyrènian Spearman | Shielded line and general frontage | Ordinary damage and MR 9 |
| Pyrènian Footman | Higher-Defence shielded line | Armour and Encumbrance can become a fatigue problem |
| Pyrènian Swordsman | High-damage heavy infantry | No shield and modest Defence |
| Pyrènian Man at Arms | Better-quality line | Higher gold, resources, and recruitment points |
| Pyrènian Knight | Mobile shock and reserve | Expensive and still MR 9 on the rider |
| Emerald Knight | Capital sacred cavalry | Seventy gold, forty resources, thirty-one recruitment points, and capital competition |

The sacred mouflon is a separate component with strong armour, Mountain Survival, and Cold Resistance. Its low Magic Resistance remains relevant against effects that can target the mount. Book IV's mounted rules should be applied to both rider and animal.

## Pyrène commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Pyrènian Bishop | B1 H2 + F/E/B random | Blood sacrifice, hunting, priest support, low-path magic | Two recruitment points; record random immediately |
| Sorgina | F1 A2 B2, flying, Storm Immune | Blood hunting, Air and Fire battle magic, mobile reinforcement | Costs 260 gold; mass recruitment can consume the whole research and fort budget |
| Akerbeltz | E1 N2 B3 + E/N/B random, Blood Searcher 1, Cross Breeder +4 | Blood economy, Cross Breeding, Nature-Earth support, searching | 450 gold, four recruitment points; forests need protection and logistics |
| Pyrènian Monk | H1 + F/E/N/B random, non-fort recruitment | Distributed research, searching, rituals, preaching | Slow recruitment and modest research efficiency; use the roll rather than collecting them without purpose |
| Emerald Count | Sacred H1 cavalry leader | Sacred command and mobile priest support | Capital-only, two recruitment points |
| Castellan, Marquess, Bekryde Champion | Mundane leadership | Main army, cavalry, and cave command | Pick leadership for the actual force instead of paying for unused armour or mobility |

### Random-path consequences

A guaranteed one-in-three Bishop random creates F1B1H2, E1B1H2, or B2H2. This gives every ordinary fort a predictable portfolio after several recruits, but it does not guarantee the required result on the first month.

The Monk's one-in-four random is valuable because recruitment is geographically distributed. F1, E1, N1, and B1 results cover searching and minor rituals without using a fort. The trade is speed: a province producing a Monk is not producing another special commander that month, and the mage still needs a laboratory for most magic work.

The Akerbeltz guaranteed random produces E2, N3, or B4 before the 10% roll is considered. Each result changes its best job:

- E2 can use Summon Earthpower to reach higher battlefield Earth thresholds;
- N3 opens stronger Nature support and searching;
- B4 accelerates high Blood rituals;
- the rare second roll may deepen or mix these roles, but no opening should require it.

## Blood economy without self-destruction

Pyrène has unusually broad access to hunters: Sorginak are B2, Bishops are at least B1, and Akerbeltz are B3 with Blood Searcher 1. That does not mean every mage should hunt.

A working blood province needs:

- enough population to survive the intended hunting period;
- hunters whose slave return exceeds their lost research or battle work;
- unrest control and patrollers;
- a laboratory or a reliable slave-transfer route;
- protection against raids and assassins;
- a declared use for the slaves.

Akerbeltz are excellent hunters but expensive researchers, ritualists, searchers, and crossbreeders. Using every one as a hunter can waste the very path breadth that makes them special. Bishops and Sorginak often provide the scalable hunting layer while selected Akerbeltz handle the difficult Blood, Nature, or Earth jobs.

Blood sacrifice should be budgeted separately. Slaves spent on dominion are not available for rituals or battle. The sacrifice is worthwhile when it changes a real dominion contest, sacred operation, or victory condition.

## Pyrène opening priorities

1. Test the local independent types against shielded infantry, crossbows, knights, or the Pretender.
2. Identify every reachable forest and cave before deciding the first fort route.
3. Recruit enough Sorginak and Bishops to start research and a controlled blood economy.
4. Use forests for Akerbeltz only when the province can be defended and connected.
5. Keep capital resources from being consumed by Emerald Knights when infrastructure is the actual bottleneck.

### Expansion packages to test

| Package | Intended target | Failure signal |
| --- | --- | --- |
| Shielded foot plus crossbows | Ordinary infantry and armour | Precision and friendly fire erase the value of the ranged line |
| Heavy foot | Low-damage opponents | Fatigue, armour-piercing weapons, or magic overwhelms protection |
| Pyrènian Knights | Weak lines and exposed ranged troops | Anti-large weapons or MR attacks trade too efficiently |
| Emerald Knights | Important high-value provinces | Capital production and resources fall behind the economic timetable |
| Awake Pretender | Difficult early targets and fast terrain capture | The design duplicates jobs the national roster already performs |

## Pyrène research response tree

### Trunk: establish Blood and practical equipment

```text
Blood 1
-> Blood 3
-> Construction 2 or 4
```

Early Blood research should lead to a named slave use. Blood 3 is especially important for Cross Breeding, because Akerbeltz carry Adept Cross Breeder +4. Construction opens tools for hunters, commanders, and battlefield specialists. The exact order changes when war demands an immediate Air, Earth, or Nature spell.

### Branch A: Sorgina battlefield magic

Evocation 2 and later Air research gives the fixed A2 Sorgina a repeatable damage role. A2 is not A3. Storm, the national Send Aatxe ritual, and several famous Air breakpoints require a real route to A3 or higher. A Pretender, hero, empowerment, booster chain, or later summon must own that bridge. Storm Power can raise a mage during an existing storm; it does not solve who created the first storm.

### Branch B: Akerbeltz Earth and Nature

Conjuration 3 lets E2 Akerbeltz use Summon Earthpower and makes several elemental routes practical. Alteration and Enchantment then provide protection, armour reduction, regeneration, poison, or control according to the actual random and target. Do not research N3 or E3 packages until the matching random has been recorded or a reliable bridge exists.

### Branch C: blood battlefield and ritual pressure

Blood research should be advanced in steps attached to a current army or strategic ritual, not rushed as one uninterrupted school. The nation can support Sabbath structures through Blood, but Book V's communion correction ledger applies: master throughput, slave paths, gem use, and collapse must be budgeted. A large slave stock is not permission to use an untested communion.

### Branch D: Send Aatxe

The national ritual is Conjuration 6, A3, costs six Air gems, has range four, is anonymous, and cannot be cast underwater. Native Sorginak stop at A2. The research target therefore becomes real only after the A3 caster route is written down. If that route exists, the ritual gives Pyrène a cheap remote pressure tool; if it does not, Conjuration 6 alone delivers nothing.

## Pyrène battlefield packages

### Resistant human line

Pyrènian infantry can absorb modest Fire and Cold better than ordinary humans. Add shields, spacing, and the right troop type before adding magic. The resistance is a margin that makes some trades favourable, not a reason to stand inside full battlefield elemental damage.

### Sorgina strike group

Flying, Storm-Immune F1 A2 B2 mages can reposition rapidly and join selected battles. Their scripts should use reachable A2, F1, or Blood effects and preserve a retreat route. Flying mobility does not protect a 10-HP human body from arrows, assassins, or a collapsed screen.

### Akerbeltz crossbreeding economy

Cross Breeding converts Blood slaves and an Akerbeltz turn into variable bodies. The +4 national specialist bonus makes Pyrène unusually suited to the system, but the output remains a portfolio rather than a guaranteed army type. Record batches, costs, useful results, leadership burden, and attrition before assigning a fixed strategic value.

### Sacred mouflon force

Emerald Knights offer protection, mobility, Mountain Survival, and a sacred mount. They are scarce enough that the bless should improve survival and role reliability. The package still needs magic resistance, fatigue control, and answers to anti-large weapons. A sacred cavalry army that cannot replace losses is a finite resource.

## Pyrène Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Air bridge | A3+ for Storm, Send Aatxe, stronger Air, and battlefield transitions | The caster still needs research, gems, safety, and timing |
| Astral or Death import | Missing strategic paths, resistance magic, summons, and communions | Imported access may remain tied to one irreplaceable god |
| Scales and blood economy | Gold, forts, laboratories, population, and recovery from hunting | Turmoil or Death choices can undermine the population base |
| Moderate cavalry bless | Emerald Knights and mounts | Sacred production is capital and resource limited |
| Awake expander | Rapid forests, caves, and chokepoints | National infantry and knights may already handle ordinary expansion |

The most valuable design often solves a missing system rather than adding more Fire, Nature, or Blood to paths already available. Air, Astral, Death, Water, or a specific global route can change the whole national tree.

## Pyrène matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| High-MR attacks against troops | Buffs, screening, summons, imported Astral, shorter exposure | Assuming armour protects MR 9 infantry |
| Fire or Cold warfare | National resistance plus additional buffs and spacing | Treating resistance 5 as immunity |
| Heavy armour | Crossbows, great swords, Earth armour reduction, Blood or summoned alternatives | Relying on low-Precision crossbows without enough volume and protection |
| Fast raiders | Flying Sorgina reserve, cave and forest scouts, local commanders | Leaving blood provinces and forest mages undefended |
| Battlefield-wide Air | Storm immunity on Sorginak, shock resistance plans, dispersed command | Extending a mage's immunity to the whole army |
| Population pressure | Rotate hunting, control unrest, move the blood centre | Continuing to hunt a province after its long-term value collapses |

## Monthly Pyrène audit

- Which forests and caves are producing something that no ordinary fort can?
- Are blood hunters separated from battle mages and researchers?
- What are the current slave income, stock, and committed uses?
- Are Bishop, Monk, and Akerbeltz randoms recorded?
- Does the active research target have a real caster?
- Who reaches A3 for Storm or Send Aatxe?
- Is the sacred cavalry queue delaying forts or mages?
- Are MR 9 troops being sent into a counter they cannot armour through?
- Can every distributed recruitment province be reinforced or evacuated?

## Pyrène verification ledger

The next useful tests are:

1. expansion ranges for shielded foot, crossbows, Pyrènian Knights, and Emerald Knights;
2. current live confirmation of Bishop, Monk, and Akerbeltz random displays;
3. Blood Searcher 1 returns across population and unrest bands;
4. Cross Breeder +4 outcome records across a versioned sample;
5. Air transition packages before and after a real A3 bridge;
6. sacred rider and mouflon survival under MR and anti-large attacks;
7. distributed-recruitment payback from forests and caves;
8. DE and Divinitus variants kept separate from this unmodded dossier.

# Part XVIII: Middle Age Ulm, Forges of Ulm

## Ulm one-page command brief

Middle Age Ulm converts resources into heavily armoured human armies, then uses recruit-anywhere Master Smiths to turn a narrow Earth and Fire base into battlefield support and forged equipment. Its forts receive 25% more resources, its smiths add local resources, and its capital produces five Earth gems each month. The result is a nation whose military and magical economies reinforce one another when forts, laboratories, troop production, and smith recruitment stay in balance.

The reliable core is compact:

- half plate offers more bodies when resources are tight;
- black plate offers exceptional mundane protection at a steep resource cost;
- pikes, shields, great weapons, flails, crossbows, and cavalry let the roster answer different physical targets;
- Sappers and Master Masons turn recruitment into siege pressure and stronger fort construction;
- Master Smiths provide fixed F1 E2, research unaffected by Drain, Forge Bonus 2, and a 20% FAES random;
- capital Priest Smiths combine F1 E2 H1 with Forge Bonus 1;
- Black Priests provide E1 H2, Inquisition, and a smaller FAES random;
- national spells add cold-iron missiles, army-wide magic-resistance support, and a late Iron Angel ritual;
- national items give Construction a strategic branch with defined jobs.

Ulm's weaknesses are equally structural. Most soldiers and mundane commanders have MR 9. The roster is slow, resource hungry, and vulnerable to attacks that bypass armour. Native magic has no dependable Water, Death, Nature, Glamour, or Blood, while Air and Astral appear only on rare randoms. Heavy recruitment can also consume the gold and resources needed to build the fort network that makes the nation scale.

## Ulm evidence and ruleset

The scope is unmodded MA Ulm on the Book I 6.36 live baseline. The roster, costs, and national summary are taken from the revision-2 official manual. Random-path masks, capital sites, national spells, national items, and object identifiers are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The two sources have different jobs. The current manual controls the player-facing roster and national rules. The pinned export resolves fields that the manual compresses or omits. Opening priorities, research branches, battlefield packages, Pretender families, and matchup choices are strategy. No live-game result is inferred from a database field when targeting, timing, stacking, or displayed cost requires engine observation.

## Ulm conversion chain

```text
enhanced fort resources and weapon-specific infantry
-> reliable expansion and protected borders
-> additional forts and laboratories
-> repeatable Master Smith recruitment
-> Earth buffs, national priest magic, and discounted forging
-> specialised armies, siege columns, and imported path access
-> fortified territorial gains and late ritual options
```

The chain commonly breaks in three places. Full black plate and cavalry can absorb the resources meant for expansion volume. Troop recruitment can absorb the gold meant for forts and laboratories. Smiths can be treated as generic researchers, leaving rare Air, Earth, Fire, or Astral results unlabelled and the matching spell branches unused.

## Ulm national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Forts produce 25% more resources | Fort placement has military value beyond recruitment access; high-resource provinces become especially useful production centres. |
| Productivity limit +1 | The Pretender design may buy more Production than an ordinary nation, but the extra scale is useful only if gold and recruitment points can consume the resources. |
| Drain limit +1 | Ulm may take deeper Drain, and smith researchers are unhindered by it. Non-immune researchers and other magic consequences still need to be counted. |
| Master Smith and Priest Smith Resource Bonus +10 | A recruited smith improves the province's troop capacity while serving as researcher, forger, or caster. |
| Master Mason | The capital can produce a Mason with Siege +30 and Castle Defence +20 in the structured record; its construction job competes with other capital recruitment. |
| Capital Earth income | The Forges of Ulm site supplies five Earth gems each month, supporting Earth rituals, battlefield gems, and forging. |
| Weak priesthood with Inquisitors | Black Acolytes supply H1, while capital Black Priests supply H2 and Inquisition. Religious operations remain concentrated in the capital queue. |
| Superior armour and national forging | Mundane protection is a real advantage, but armour does not answer magic resistance attacks, fatigue, armour destruction, or armour-negating damage. |

The resource bonuses reward a distributed production network. They do not remove the gold cost of that network. A province that can recruit another block of black plate but cannot fund a laboratory, commander, or next fort may be producing the wrong asset for the current turn.

## Ulm roster by job

| Unit group | Best job | Important limit |
| --- | --- | --- |
| War Dog | Cheap armoured screening, flanking pressure, and pursuit | Low HP and MR; animal leadership and losses must be managed |
| Infantry of Ulm in half plate | Resource-efficient line mass with shield, flail, hammer, maul, morningstar, or battleaxe variants | Protection is lower than black plate, and the correct weapon still depends on the target |
| Black Plate Infantry | High-protection line, bodyguard-quality mass, and attritional holding | Much higher resource cost, ordinary MR, low battlefield speed, and fatigue exposure |
| Pikeneer and Black Plate Pikeneer | Long-weapon line against large units, cavalry, and repel-sensitive attackers | No shield and limited value when weapon length or armour does not solve the matchup |
| Crossbowman | Arbalest pressure against armoured targets from behind a screen | Slow rate of fire, ordinary precision, and friendly-fire risk |
| Sapper | Siege strength, crossbow support, and campaign utility | Twenty gold and high recruitment-point demand make it a specialist, not default infantry |
| Guardian | Capital-only elite infantry with a Black Halberd | Capital restriction, high resources, and high recruitment-point demand limit mass |
| Black Knight | Armoured shock cavalry, flank threat, and mobile reserve | Sixty gold, heavy resource demand, MR 9, and separate rider-and-mount failure modes |

Ulm should select armour and weapon by job. Half plate increases numbers when the resource ceiling matters. Full black plate increases protection when conventional weapons are the threat. Shields matter under missile pressure. Great weapons and the Black Halberd matter when damage and armour penetration are more important than defence. Flails matter against shields. Pikes matter against large targets and for repel interactions. None is the universal Ulmish infantry.

### The armour budget

The useful recruitment question is whether black plate's extra resources prevent another soldier, crossbowman, fort, or specialist from being produced on the required turn. A mixed formation can place the most protected troops where contact is expected and use cheaper armour where frontage matters more than individual survival.

The same rule governs Black Knights. Their charge, protection, and mobility can solve a battle that infantry cannot reach in time. Buying them as ordinary line troops turns a resource advantage into a narrow and expensive queue.

## Ulm commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Commander of Ulm variants | Mundane leadership with different armour and weapons | Low-cost army command matched to the troop package | MR 9 and no magic utility; full black plate increases resource cost |
| Black Lord | Heavy cavalry commander, Leadership 100 | Mobile command, armoured reserve, and battle leadership | Expensive and still MR 9 |
| Spy | Stealth 60, Spy | Information, unrest reporting, and enemy-strength checks | Intelligence quality depends on position and time; it does not replace scouting or scrying |
| Black Acolyte | H1 | Blessing, preaching, light religious support | Narrow role and no Earth path for the national priest spells |
| Master Smith | F1 E2, 20% FAES random, Forge Bonus 2, Resource Bonus +10 | Core research, Earth support, forging, site searching, and rare-path branches | Two recruitment points; rare paths are each only 5% |
| Master Mason | Mason, Siege +30 | Better fort construction, siege and fort defence | Capital-only commander turn |
| Lord Guardian | Halt Heretic +3, Leadership 100 | Capital defence, leadership, and hostile-dominion pressure | Capital-only and not a mage |
| Black Priest | E1 H2, Inquisitor, 10% FAES random | National priest spells, preaching, Inquisition, and rare-path utility | Capital-only, two recruitment points, and no forge bonus in the pinned record |
| Priest Smith | F1 E2 H1, Forge Bonus 1, Resource Bonus +10 | Fixed-path national priest magic, research, Earth support, and forging | Capital-only, 245 gold, and two recruitment points |

The normal fort queue should be read as a capacity decision. Master Smiths are the repeatable magical engine. Mundane commanders move the troops that engine supports. The capital must choose among religious access, Mason infrastructure, elite commanders, and ordinary fort recruits; it should not be assigned one permanent queue without reference to the current bottleneck.

## Reading the smith randoms

### Master Smith distribution

The pinned record gives every Master Smith fixed F1 E2 and a 20% chance of one additional level chosen equally from Fire, Air, Earth, or Astral.

| Final paths | Probability per recruitment |
| --- | ---: |
| F1 E2 | 80% |
| F2 E2 | 5% |
| F1 A1 E2 | 5% |
| F1 E3 | 5% |
| F1 E2 S1 | 5% |

The chance of recruiting at least one named rare path after `n` independent Master Smiths is `1 - 0.95^n`. That is about 51.2% after 14 recruits, 64.2% after 20, and 90.1% after 45. Twenty recruits are an average waiting time for a named 5% result, not a guarantee. A plan that requires A1, S1, F2, or E3 on a fixed early turn needs a backup.

### Black Priest distribution

The capital-only Black Priest has fixed E1 H2 and a 10% chance of one FAES level. The four named rare results are 2.5% each.

| Final paths | Probability per recruitment |
| --- | ---: |
| E1 H2 | 90% |
| F1 E1 H2 | 2.5% |
| A1 E1 H2 | 2.5% |
| E2 H2 | 2.5% |
| E1 S1 H2 | 2.5% |

The Priest Smith is not a random-path substitute. It has fixed F1 E2 H1, so it supplies dependable access to Iron Darts and Iron Blizzard but never becomes the rare Air or Astral result by repeated recruitment.

Every smith and Black Priest should be labelled when recruited. The label should record paths, home fort, current job, and whether the unit is reserved for a threshold spell, searching route, or forge chain. Rare paths lose strategic value when they disappear into an undifferentiated research stack.

## National spells and the caster who owns them

| Spell | School and requirement | Native caster | Planning use and boundary |
| --- | --- | --- | --- |
| Iron Darts | Evocation 3, E1 H1 | Black Priest or Priest Smith | Low-fatigue national cold-iron missiles. The source describes special value against magical beings; formation, target selection, and actual damage still belong to battle context. |
| Tempering the Will | Thaumaturgy 5, E3 | Master Smith or Priest Smith after Summon Earthpower; E3 Master Smith directly | National battlefield magic-resistance support. It addresses a central roster weakness but does not make MR 9 troops immune to hostile magic. |
| Iron Blizzard | Evocation 6, E1 H1 | Black Priest or Priest Smith | A larger national cold-iron missile package with much higher fatigue. Caster count, range, fatigue recovery, and friendly-fire exposure determine whether it is worth fielding. |
| Contact Iron Angel | Conjuration 8, E5 S2, 25 Earth gems | No unassisted recruit | Late summon with high MR and Halt Heretic. Research alone does not create the E5 S2 caster; the exact booster, empowerment, summon, or Pretender route must be owned first. |

This table distinguishes research access from caster access. Ulm can research Contact Iron Angel while still lacking any legal caster. Conversely, every normal fort can recruit the E2 smith who reaches E3 in battle through Summon Earthpower, so Tempering the Will has a much more dependable delivery route.

## National item portfolio

The pinned item register separates Ulm's items into **discounted** designs and a **restricted** design. The distinction matters. A national rebate changes cost for Ulm; a restriction changes who may forge the item. Book V owns the general forging rules and the unresolved stacking ledger.

### Early discounted blacksteel

Construction 1 opens the Blacksteel Sword, Blacksteel Tower Shield, Blacksteel Kite Shield, Blacksteel Helmet, Blacksteel Plate, and Blacksteel Full Plate. Most require E1; the full plate requires E2. These items let an ordinary Master Smith equip thugs, commanders, and specialists from the nation's native Earth income.

The item card should decide whether a piece solves the actual failure. More protection is useful against conventional weapons. It does not repair low MR, fatigue, elemental vulnerability, or command problems. A tower shield, kite shield, weapon, helmet, and full plate also compete for slots with non-national answers.

### Later national equipment

| Item | Construction and paths | Evidence-backed role |
| --- | --- | --- |
| Black Halberd | Construction 3, E1 | Restricted to MA and LA Ulm in the pinned record; a national two-handed weapon option |
| Blacksteel Barding | Construction 3, E2 | Discounted national mount armour |
| The Copper Arm | Construction 7, E3 F1 | Discounted cursed item that grants extra arms; use requires a complete chassis and slot plan |
| Krupp's Bracers | Construction 9, E2 | Discounted artifact-tier reinvigoration item |

Master Smith Forge Bonus 2, Priest Smith Forge Bonus 1, national rebates, global forge modifiers, and integer rounding can interact. The final gem price remains unresolved. The live forge screen is the operational authority until the current stacking order is supported by a versioned observation record.

## Ulm opening priorities

The opening has five linked jobs:

1. identify whether resources, gold, commander turns, or recruitment points are the immediate ceiling;
2. recruit the armour-and-weapon mix that answers the local independent provinces;
3. reserve the gold needed for the next fort and laboratory;
4. start a repeatable Master Smith pipeline without leaving armies leaderless;
5. preserve enough capital flexibility for a Mason, Priest Smith, Black Priest, Lord Guardian, or Guardian block when its specialised job becomes real.

A safe default is a protected infantry line with arbalest support, adjusted for the target. Pike weight rises against large units and cavalry. Great weapons rise against protection. Shields rise against missiles. Half plate rises when resource-limited frontage matters. Black plate rises when ordinary weapon damage is the main threat and the production centre can sustain it.

### Expansion packages to evaluate from reports

| Package | Intended target | Failure signal |
| --- | --- | --- |
| Half-plate line plus crossbows | Ordinary infantry and armoured independents | The line collapses before the slow ranged damage pays back |
| Shielded black-plate line | Missile-heavy or conventional melee provinces | Resources produce too few bodies, or fatigue defeats the protection advantage |
| Pikes with protected flanks | Cavalry, large animals, and long-weapon matchups | Small high-Defence troops close safely and win the sustained melee |
| Great-weapon infantry | High-protection targets | Low Defence, missiles, or first-strike losses remove the damage dealers |
| Black Knight reserve | Weak flanks, exposed ranged troops, and time-sensitive reinforcement | Anti-large weapons, armour-negating damage, or attrition consume an irreplaceably expensive package |

These are decision templates, not published expansion counts. Exact party sizes remain open because the map, scales, formations, commander, independent type, and combat rolls change the answer. No new runtime test preparation is required to use the dossier's economic and matchup logic.

## Ulm research response tree

### Trunk: make fixed E2 recruitment useful

```text
Enchantment 1
-> Construction 2
-> Conjuration 3
```

- Enchantment 1 gives Strength of Giants to fixed E2 smiths.
- Construction 2 gives Temper Armors and completes the first ordinary equipment tier.
- Conjuration 3 gives Summon Earthpower, raising an E2 smith to E3 during battle.

This is a capacity trunk, not a mandatory order. An immediate armoured enemy may justify Alteration. Magical beings may justify early Iron Darts. A fort network that needs equipment may value Construction first. Every research choice should name the current caster, army, and expected deployment turn.

### Branch A: Earth control and armour reduction

Alteration 3 gives Earth Meld to E2. Alteration 4 gives Destruction to an E3 caster, which an ordinary Master Smith can reach after Summon Earthpower. Alteration 5 adds Maws of the Earth for E3 and a gem. Later Marble Warriors and Iron Warriors strengthen protection packages, but their caster thresholds, fatigue, and exposure must be scheduled with the army.

This branch is strongest when conventional Ulmish damage is losing to protection or when the line needs Earth control to keep enemies in the kill zone. It is weaker when the enemy ignores armour, attacks MR, or forces the smiths to move too far from the troops they support.

### Branch B: national priest missiles and MR support

Evocation 3 opens Iron Darts for Black Priests and Priest Smiths. Thaumaturgy 5 opens Tempering the Will for E3. Evocation 6 opens Iron Blizzard. The first branch is capital-caster limited even when the research is cheap; the second can be delivered by repeatable E2 smiths after Summon Earthpower.

Do not read the national spell list as one automatic queue. Iron Darts and Iron Blizzard are most attractive when their cold-iron profile and ranged delivery solve the observed target. Tempering the Will is most attractive when hostile MR checks threaten expensive low-MR soldiers.

### Branch C: broad Earth force multiplication

Enchantment 5 gives Weapons of Sharpness to E3. Construction 6 gives Legions of Steel to E4 and a gem. An E3-random Master Smith reaches E4 through Summon Earthpower; ordinary E2 smiths need another real step. High Earth rituals such as Riches from Beneath, Forge of the Ancients, and Earth Blood Deep Well are planning endpoints, not native guarantees. Their E5 or E6 caster and large gem cost must be built before the research can pay back.

### Branch D: rare Fire, Air, and Astral results

- An F2 Master Smith can cast Phoenix Power and reach F3 for stronger Fire battle magic such as Falling Fires or Summon Fire Elemental.
- An A1 Master Smith can combine Air with the fixed Earth base. After Summon Earthpower it reaches E3 A1, including the path threshold for Rain of Stones; that spell's danger to Ulm's own human army makes delivery and protection part of the package.
- An S1 Master Smith opens basic Astral searching and utility, but S1 is not a communion engine or the S2 half of Contact Iron Angel by itself.
- An E3 Master Smith reaches E4 through Summon Earthpower and owns thresholds that ordinary smiths do not.

These are portfolio branches. Researching one before recruiting the matching 5% result converts certainty into hope. Record the rare mage first, then select the branch.

## Ulm battlefield packages

### Armoured line with Earth support

A mundane commander moves the infantry while one or more Master Smiths supply reachable buffs. The screen's armour and weapon are selected from the enemy report. Smiths stand far enough back to survive but close enough for the spell's real area and range. Adding more spells is not automatically safer: fatigue, script length, and a broken line can turn valuable researchers into casualties.

### Priest Smith cold-iron cell

A Priest Smith combines the paths for Iron Darts or Iron Blizzard with forging and E2 support. Black Priests can cast the same national missiles and bring H2 Inquisition. The cell requires a protected firing lane and an enemy for whom the missile profile matters. Against dispersed, resistant, or rapidly closing targets, the capital mage turn may be more valuable elsewhere.

### Rare-path specialist cell

An F2, A1, E3, or S1 Master Smith is paired with the troop package and research that use that exact result. The unit receives a permanent label and a retreat plan. Rare access should not be risked merely because the spell list permits a dramatic script.

### Siege column

Sappers provide Siege +5, while Master Masons provide Siege +30 and improve fort construction. Ordinary infantry supply bodies. This lets Ulm convert a production advantage into campaign tempo instead of leaving a victorious heavy army stalled at a wall. The column still needs scouts, supply, leadership, and protection against relief armies.

## Ulm Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Production and economy | Converts the fort resource bonus into larger armoured queues and supports more infrastructure | Extra resources do not pay gold, recruitment points, or commander turns |
| Missing-path bridge | Imports Water, Death, Nature, Glamour, Blood, dependable Air, or dependable Astral | One god is not a distributed national path; site searching, boosters, and replacement access still matter |
| High Earth-Astral ritual bridge | Builds toward Contact Iron Angel or other late rituals | E5 S2, research, gems, and opportunity cost must all be explicit |
| Resistance or mobility design | Covers shock, cold, poison, MR, map-move, or another identified roster weakness | A bless affects sacred recipients, while most Ulmish troops are mundane |
| Awake expander | Adds early tempo where armoured troops cannot secure the required map | Afflictions, path design, and lost scales can cost more than the provinces gained |

Ulm often benefits more from a missing system than from another level in paths it already recruits. The design should name the first site-search target, booster, ritual, battlefield job, and replacement plan for every imported path. A theoretical late spell is not a reason to weaken the entire opening unless its access chain is credible.

## Ulm matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Heavy conventional armour | Great weapons, Black Halberds, Destruction, Maws of the Earth, and crossbow concentration | Paying for maximum protection while using damage that cannot penetrate the target |
| High-Defence or shielded troops | Flails, longer weapons, attack support, control, and more frontage | Assuming protection fixes missed attacks |
| MR attacks and mind magic | Tempering the Will, imported Astral, resistance equipment, summons, spacing, and shorter exposure | Treating black plate as protection against MR checks |
| Armour-negating or armour-piercing magic | Dispersal, resistance, ranged pressure, summons, and attacks on the caster | Concentrating expensive slow troops inside the effect |
| Fatigue and armour destruction | Mixed armour weights, shorter fights, reinvigoration, reserves, and counter-caster pressure | Increasing armour without addressing the mechanism defeating it |
| Flyers and fast raiders | Guarded smiths, protected rear formations, local commanders, forts, and spies | Leaving the research and forging stack as an exposed single point of failure |
| Magical beings | Iron Darts or Iron Blizzard when the national profile fits, plus ordinary Earth and weapon answers | Assuming the national label guarantees favourable targeting or damage in every battle |
| Large units and cavalry | Pikes, layered formations, Earth control, and concentrated missile fire | Exposing unshielded pikes to the wrong ranged matchup |
| Strategic mobility | Fort geometry, forward laboratories, mounted command, prepared reserves, and imported mobility | Expecting slow heavy infantry to answer every raid after it appears |

## Monthly Ulm audit

- Which production centre is limited by resources, and which is limited by gold or recruitment points?
- Is half plate or black plate the correct marginal purchase for the current enemy?
- Are crossbows protected and assigned a target worth their slow rate of fire?
- Does every field army have a commander whose movement and leadership fit it?
- Are Master Smith randoms labelled at recruitment?
- Does the active research target have a named caster and deployment turn?
- Are Earth gems divided among battlefield use, forging, and rituals before spending begins?
- Is the capital queue solving a real religious, Mason, elite, or command bottleneck?
- Does the next fort improve recruitment geometry, resource conversion, or strategic defence?
- Is low MR being answered before the army meets mind or soul attacks?
- Are rare-path smiths protected from assassination, raiding, and routine frontline risk?
- Is a late ritual route supported by actual paths, research, and gems?

## Ulm unresolved evidence boundary

The dossier deliberately leaves the following claims open:

1. exact expansion-party ranges for each armour and weapon mix;
2. live 6.36 display confirmation of the pinned Master Smith and Black Priest random masks;
3. final displayed item costs when national rebate, Forge Bonus, global modifiers, and rounding combine;
4. Iron Darts and Iron Blizzard targeting, friendly-fire, and damage outcomes in specific formations;
5. Tempering the Will's exact battlefield application against current MR attack types;
6. the economic break-even point for Sappers, Master Masons, and stronger forts on different maps;
7. reliable routes and payback for Contact Iron Angel and the larger Earth globals;
8. rider-and-mount survival outcomes for Black Knights under different attack types;
9. modded Ulm variants, which remain separate from this unmodded chapter.

These are preserved as unresolved claims, not converted into new test assets or guessed conclusions. R-047, R-058, and the broader runtime-testing queue remain parked until hands-on testing is explicitly resumed.

# Part XIX: Middle Age Man, Tower of Avalon

## Man one-page command brief

Middle Age Man turns several modest recruitment pools into a flexible human army. Ordinary forts supply longbows, infantry, cavalry, scouts, spies, priests, and three levels of Avalon mage. Forests add Foresters and Royal Foresters, while non-fort provinces can raise Logrian troops, Monks, and Logrian Wise Men. The capital adds the sacred Wardens and Knights of Avalon, their commanders, and the Crone of Avalon.

The reliable core is easy to state:

- Longbowmen provide accurate, long-ranged mundane fire behind a line chosen for the target;
- Knights of Man give every fort a heavily armoured mobile recruit;
- Wardens and Knights of Avalon are powerful sacred capital troops, but their price and limited queue keep them scarce;
- Monks spread cheap H1 research beyond the main mage forts;
- Bards, Daughters, Mothers, and Crones are Spellsingers with fixed Glamour access;
- Mothers provide the repeatable random portfolio, while capital Crones start at N3 G2 H1;
- Logrian Wise Men recruit outside forts and add low Earth plus Fire, Air, Earth, or Nature branches;
- the Forest and Tower of Avalon supply three Nature and two Glamour gems each month.

Man can recruit many different answers, but it cannot pay for all of them at once. Mothers cost 305 gold, capital Crones cost 465 gold and four commander recruitment points, Knights of Man cost 45 gold and 32 resources, and Knights of Avalon cost 90 gold and 32 resources. A plan that spends on every elite option can delay the forts and laboratories that make the roster useful.

## Man evidence and ruleset

The scope is unmodded MA Man on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, recruitment locations, national summary, communion description, spells, and rituals. Random masks, object identifiers, capital sites, hero records, and nation restrictions are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The official 6.13 patch changed the Forest of Avalon from a +2 Magic increase to its intended +1. That correction is applied here. The patch ledger through 6.36 names no later MA Man roster or national-spell change, but the older structured snapshot is still labelled 6.35. A live display remains the final authority where the manual compresses a random scheme or the database carries a hidden casting restriction.

## Man conversion chain

```text
longbows, infantry, and ordinary knights
-> secure provinces and useful forests
-> forts, laboratories, and distributed recruitment
-> Monks, Spellsingers, Mothers, and Logrian Wise Men
-> Chorus, Nature-Glamour support, and national summons
-> specialised field armies and imported missing paths
-> protected territory, sieges, and Throne operations
```

The chain tends to break at three points. Gold-heavy mages and cavalry can delay the next fort. The capital commander queue can be consumed by Crones before the army has enough leaders. Random Mothers and Wise Men can disappear into research without being labelled for the spell or forge branch their paths opened.

## Man national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Standard forts | Man needs an ordinary fort-and-laboratory budget; terrain recruitment supplements the network but does not replace it. |
| Temples cost 300 gold | Religious infrastructure is cheaper than the ordinary 400-gold temple, but it still competes with mages, troops, and forts. |
| Weak priests and inspired researchers | Monks are H1 Mundane Researchers and can be recruited outside forts as well as in forts. They widen research and preaching without adding a magic path. |
| Forest recruitment | Foresters and Royal Foresters can be recruited in every forest. Forest ownership can therefore add stealth, patrol, and ranged recruitment away from a fort. |
| Non-fort recruitment | Logrian Slingers, Warriors, Cavalry, Monks, and Logrian Wise Men can be recruited outside forts according to the manual and structured membership tables. |
| Forest of Avalon | The capital site supplies three Nature gems, Wardens, Knights of Avalon, and their commanders; patch 6.13 sets its Magic increase to +1. |
| Tower of Avalon | The second capital site supplies two Glamour gems and the Crone of Avalon. |
| Communal Chants | Man's Spellsingers can cast Chorus Master and Chorus Slave. Book V owns the general communion rules and safety discussion. |

Terrain recruitment is part of Man's economy. A forest can contribute scouts and Foresters before it has a fort, while an otherwise ordinary non-fort province can contribute a Monk or a random Wise Man. Those commanders still cost gold and recruitment time. The map offers more queues, not free capacity.

## Man roster by job

| Unit or group | Best job | Important limit |
| --- | --- | --- |
| Logrian Slinger | Cheap ranged body from forts or outside them | Low protection and modest accuracy; the sling is not a substitute for the longbow line. |
| Longbowman | Long-ranged supporting fire | Needs a screen and a target for which mundane arrows matter; friendly troops still occupy the line of fire. |
| Spearman and Longspear | Inexpensive line and long-weapon control | Ordinary protection and damage; each version should be chosen for the opposing weapon and size mix. |
| Logrian Warrior | Javelin-and-axe reinforcement from forts or outside them | More expensive and resource-heavy than the basic line, with no shield against concentrated missiles. |
| Tower Guard | Better-defended sword line | Fourteen recruitment points and eighteen resources slow mass recruitment. |
| Forester | Forest-surviving stealth archer, patrol support, and dispersed reinforcement | Light armour and a mixed weapon set; useful terrain access does not make it a heavy line unit. |
| Landless Knight | Armoured foot line with a broad sword | Better protection costs resources, while the unit still moves and fights as infantry. |
| Logrian Cavalry | Mobile reinforcement from forts or outside them | Rider 1 and a lightly protected War Horse make it the cheaper cavalry tier, not a Knight of Man. |
| Knight of Man | Heavy shock cavalry from any fort | Forty-five gold, 32 resources, 25 recruitment points, and separate rider and Destrier risks. |
| Warden of Avalon | Capital-only sacred great-sword infantry with True Sight | Twenty-six gold, 28 resources, and 33 recruitment points keep the unit specialised. |
| Knight of Avalon | Capital-only sacred unicorn cavalry | Ninety gold and 35 recruitment points; both the rider and Armored Unicorn must survive the attacks aimed at them. |

The default army should not mix every row. Longbows need a line that holds for the expected approach. Cavalry needs space and a target worth charging. Wardens and Knights of Avalon need a bless and battle that justify spending the capital troop queue on them.

## Man commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Royal Forester | Stealth 55, Patrol +5, forest recruitment | Scouting, patrolling, stealth leadership, and moving Foresters | Leadership 10; it is a specialist, not a general army commander. |
| Castellan | Leadership 100 | Ordinary field command | No priest or magic role. |
| Monk | H1, Mundane Researcher, outside-fort recruitment | Research, preaching, blessing, and light sacred support | Low morale and no non-Holy magic path. |
| Bard | G1, Spy, Spellsinger | Intelligence, Chorus participation, Glamour support | Two recruitment points for a narrow battle mage and spy. |
| Daughter of Avalon | N1 G1, Spellsinger | Core research, Chorus participation, Nature and Glamour support | Two recruitment points and no random path. |
| Mother of Avalon | N1 G1 H1 plus two random rolls, Spellsinger | Main random mage, Chorus, rituals, battlefield support, searching | 305 gold and two recruitment points; the useful result must be labelled. |
| Lord Warden | Sacred, True Sight, Leadership 100 | Capital command and elite infantry leadership | Capital-only commander turn and 170 gold. |
| Knight Commander of Avalon | Sacred mounted Leadership 100 | Mobile capital command and sacred cavalry leadership | Capital-only, 210 gold, with a separate Armored Unicorn mount. |
| Crone of Avalon | N3 G2 H1 plus randoms, Spellsinger | High Nature and Glamour, national rituals, Chorus master, searching | Capital-only, 465 gold, and four recruitment points. |
| Logrian Wise Man | E1 plus FAEN random, Research -4, non-fort recruitment | Elemental branch access, Earth support, searching, and forging | 125 gold and two recruitment points for reduced research efficiency. |

The capital queue should answer a current need. A Crone gives paths and ritual certainty. A Lord Warden or Knight Commander moves an elite force. Recruiting the expensive mage every turn without funding armies, forts, and field leaders can leave Man rich in theory and slow on the map.

## Reading Avalon's random paths

### Mother of Avalon distribution

The manual prints the Mother as N1 G1 H1 with two random levels. The pinned record resolves two guaranteed and independent rolls:

1. one level from Nature or Glamour;
2. one level from Water, Earth, or Nature.

The six combinations are equally likely.

| Final paths | Probability per Mother |
| --- | ---: |
| W1 N2 G1 H1 | 16.67% |
| E1 N2 G1 H1 | 16.67% |
| N3 G1 H1 | 16.67% |
| W1 N1 G2 H1 | 16.67% |
| E1 N1 G2 H1 | 16.67% |
| N2 G2 H1 | 16.67% |

A Mother has a 50% chance to reach G2, a 33.33% chance to gain Water, a 33.33% chance to gain Earth, a 66.67% chance to reach at least N2, and a 16.67% chance to reach N3. Four independent Mothers give about a 93.75% chance of at least one G2 result, 80.25% for at least one Water result, 80.25% for at least one Earth result, and 51.77% for at least one N3 result.

These chances describe recruitment, not timing guarantees. A G2 Mother owns Geas, Summon Cu Sidhe, and the Glamour threshold of Herd of Unicorns. Water and Earth Mothers open different general spell and forge branches. An N3 Mother reaches thresholds that the ordinary Daughter cannot.

### Crone of Avalon distribution

Every Crone begins at N3 G2 H1. The pinned 6.35 record then gives:

- one guaranteed level chosen equally from Air, Water, Earth, Nature, or Glamour;
- an independent 10% chance of a second level from the same five-path set.

The guaranteed result is 20% for each named path. Including the second roll, the chance of receiving at least one chosen path is 21.6%. Ten percent of Crones receive two random levels; two percent receive both levels in the same path, and eight percent receive two different paths.

The current manual compresses the Crone to `?1` and does not expose that 10% second slot on the nation page. This dossier keeps the extra roll labelled as pinned structured evidence until a live 6.36 recruitment card or another current official source resolves the display.

### Logrian Wise Man distribution

The Logrian Wise Man has fixed E1 and one guaranteed level chosen equally from Fire, Air, Earth, or Nature.

| Final paths | Probability per Wise Man |
| --- | ---: |
| F1 E1 | 25% |
| A1 E1 | 25% |
| E2 | 25% |
| E1 N1 | 25% |

For any named result, `1 - 0.75^n` gives the chance of seeing at least one after `n` independent recruits. That is about 57.8% after three, 76.3% after five, and 94.4% after ten. The expected wait is four recruits, but the non-fort provinces, gold, commander points, and laboratories needed to use the result still have to exist.

## National spells and caster access

| Spell | School and requirement | Native caster | Planning use and boundary |
| --- | --- | --- | --- |
| Chorus Master | Thaumaturgy 1, G1, Spellsinger | Bard, Daughter, Mother, or Crone | Starts the master side of Man's national Chorus. The official manual limits it to Spellsingers. |
| Chorus Slave | Thaumaturgy 1, G1, Spellsinger | Bard, Daughter, Mother, or Crone | Starts the slave side. Caster count, path mix, fatigue, timing, and retreat safety must be planned together. |
| Summon Black Dogs | Conjuration 2, D2, 5 Death gems | No recruit or listed national hero has D2 | Summons 20 Black Dogs. Owning the ritual does not create its caster. |
| Summon Cu Sidhe | Conjuration 3, G2, 5 Glamour gems | Crone or G2 Mother | Summons 10 sacred Cu Sidhe. Research, gems, commander capacity, and the army that will lead them all matter. |
| Geas | Thaumaturgy 3, G2 | Crone or G2 Mother | National combat control. Target selection, resistance checks, and battle value remain context dependent. |
| Summon Barghests | Conjuration 4, D2, 7 Death gems | No recruit or listed national hero has D2 | Summons 14 sacred Barghests. A Pretender, summon, empowerment, or independent path must supply the missing Death caster. |
| Herd of Unicorns | Conjuration 4, G2 N1, 10 Glamour gems | Crone or G2 Mother | Summons 10 sacred Unicorns. The pinned record also restricts the source province to forest terrain; check the current spell card before committing the gems. |

The Death rituals are the clearest access warning. Man owns them nationally, but its repeatable roster and six listed national heroes contain no Death path. Researching those spells before building a real D2 route creates no casting capacity.

## Man national item boundary

The revision-2 manual does not list a separate Man item portfolio, and the pinned BaseI register has no nation-57 restriction or rebate record. Man can still forge ordinary items when a mage meets their paths. Those designs remain general objects, not national equipment.

This matters for planning. A Water or Earth Mother and an elemental Wise Man may open useful forging thresholds, but their random path does not create a discount. Item cost, booster order, and replacement access should be checked before a rare mage is assigned to repeated forging.

## Man opening priorities

The opening has six linked jobs:

1. identify which nearby provinces need longbows, shields, long weapons, cavalry, or a different answer;
2. preserve enough gold for the first infrastructure target while recruiting a line that can protect the archers;
3. use forests and safe non-fort provinces as extra recruitment points where the map supports them;
4. begin Monk, Daughter, Mother, or Bard recruitment without leaving the armies short of leadership;
5. decide whether the capital commander queue needs a Crone, Lord Warden, or Knight Commander;
6. label every Mother, Crone, and Wise Man as soon as its paths are known.

### Recruitment packages to evaluate from reports

| Package | Intended target | Failure signal |
| --- | --- | --- |
| Spear line with Longbowmen | Ordinary infantry and lightly protected targets | The line breaks before the arrows matter, or shields and armour make the volleys inefficient. |
| Tower Guard or Landless Knight screen | Stronger conventional melee and missile pressure | Resources buy too few bodies, or armour-negating attacks remove the investment. |
| Knight of Man reserve | Exposed flanks, ranged troops, and time-sensitive reinforcement | Anti-large weapons, control, or mount losses turn the charge into an expensive trade. |
| Logrian mixed reinforcement | Provinces where outside-fort recruitment adds useful bodies quickly | The local queue consumes gold without producing a coherent formation. |
| Warden or Knight of Avalon core | Battles where the bless and sacred traits answer a known threat | Capital scarcity and losses cost more than an ordinary troop solution. |

These are report templates, not fixed expansion counts. Independent strength, formations, scales, bless, terrain, and combat rolls change the required party. No battle result is invented here.

## Man research response tree

### Branch A: fixed Glamour support

Thaumaturgy 1 gives every Spellsinger access to Chorus Master and Chorus Slave. Alteration 2 gives G1 Blur and Mirror Image. Thaumaturgy 3 gives G1 Luck and the national G2 Geas. This branch is available before a rare elemental random appears, but each spell still needs a protected caster and a battle where its effect matters.

Chorus is a force multiplier, not a substitute for planning. Masters and slaves should be counted before the script is chosen. Book V records the official rule that an unconscious Chorus Slave leaves the Chorus; the field plan must account for the resulting path and fatigue change.

### Branch B: national summons

Conjuration 3 opens Summon Cu Sidhe to every Crone and half of Mothers. Conjuration 4 adds Herd of Unicorns to the same casters because they also meet N1. The capital already receives three Nature and two Glamour gems each month, but that income must also support battlefield gems, searching, and any other rituals.

Summon Black Dogs and Summon Barghests sit on the same research branch but need D2. They should remain a future option until the nation actually owns a Death caster.

### Branch C: Nature protection and pressure

Crone access makes N3 dependable from the capital. Enchantment 3 gives Regeneration to N3, Conjuration 5 gives Howl to N3 with three Nature gems, and Alteration 6 gives Wooden Warriors to N3 with one Nature gem. Mothers add repeatable lower Nature and a one-in-six N3 result.

The choice depends on the army and opponent. Protection does not answer every elemental or armour-negating attack. Regeneration does not prevent a unit from dying to a single large hit. Howl and other battlefield pressure still depend on placement, duration, and the enemy's rear security.

### Branch D: Logrian Earth and elemental access

Every Wise Man can cast the E1 Earth Grip at Alteration 1. The 25% E2 result reaches Strength of Giants at Enchantment 1, Earth Meld at Alteration 3, and Summon Earthpower at Conjuration 3. Fire, Air, and Nature results widen searching and low-path utility, but one random level does not make Man a deep elemental nation.

Research should follow the recruited result. A plan that assumes an E2 Wise Man on a fixed turn has only a 25% success chance per recruit. If the branch matters, recruit across several eligible provinces and keep a fallback that uses fixed Nature and Glamour.

## Man battlefield packages

### Longbow line

A Castellan or other suitable commander holds the infantry line while Longbowmen fire from protected positions. The line type is selected from the report: spears for cheap frontage, longer weapons for the right approach, or heavier troops when ordinary protection is the limiting factor. More archers do not repair a screen that collapses too early.

### Cavalry reserve

Knights of Man or the cheaper Logrian Cavalry wait for a flank, rear, or reinforcement job. Their riders and mounts are separate creatures under Dominions 6. Formation, charge lanes, anti-large weapons, and the survival of both parts remain battle questions.

### Avalon sacred force

Wardens bring capital-only sacred infantry with True Sight. Knights of Avalon add sacred Armored Unicorns and mobility. The bless should solve an identified weakness or improve a job the units already perform. Capital scarcity means they should not be treated as a mass replacement for ordinary infantry and cavalry.

### Spellsinger cell

Bards and Daughters provide cheap G1 Chorus bodies, while Mothers and Crones bring the paths that benefit from the Chorus. The cell needs a clear master-slave count, script, gem allocation, guard plan, and retreat route. Losing the cell can remove both battle magic and a large block of research.

### Distributed recruitment column

Forests add Royal Foresters and Foresters. Non-fort provinces add Logrian troops, Monks, and Wise Men. This can replace losses and widen research without waiting for every fort, but the resulting pieces still need commanders, laboratories where required, supply, and a route to the front.

## Man Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and infrastructure | Pays for 305-gold Mothers, 465-gold Crones, cavalry, forts, laboratories, and temples | More income does not remove capital turns, commander points, or resource limits. |
| Sacred support | Improves Wardens, Knights of Avalon, and national sacred summons | Most ordinary Man troops remain mundane, while the best sacred recruits are capital-only. |
| Death bridge | Supplies the missing D2 for Black Dogs and Barghests and may open broader Death work | One Pretender is not distributed access; searching, gems, timing, and replacement still matter. |
| Elemental bridge | Makes a required Fire, Air, Water, or Earth threshold dependable instead of waiting on randoms | The bridge should name its first search, forge, ritual, and battlefield job. |
| Early tempo | Covers an opening that the available troop mix cannot handle safely | Lost scales, afflictions, and chassis risk may cost more than the early provinces gained. |

Man already has strong Nature and Glamour. A Pretender earns its cost by repairing a real bottleneck, supporting the scarce sacreds, or improving the economy that recruits the roster. Adding more of an existing path without a funded job can leave the original problem untouched.

## Man matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Shielded or heavily armoured line | Cavalry pressure, Earth support from Wise Men, control, sacreds, or imported damage | Assuming another block of mundane arrows will solve protection by itself. |
| Fast flankers and flyers | Protected rear positions, reserves, guards, wider formations, and local commanders | Leaving Longbowmen and Spellsingers as one exposed rear cluster. |
| Large units and cavalry | Long weapons, layered lines, control, and concentrated fire | Sending expensive cavalry into the enemy's preferred anti-large fight. |
| High Defence, Glamour, or ethereal targets | Area effects, buffs, True Sight assets, magic weapons, and researched control | Treating high arrow volume as guaranteed contact. |
| Armour-negating or elemental magic | Spacing, resistance, pressure on casters, summons, and shorter exposure | Buying heavier human armour against damage that ignores it. |
| Mind and MR attacks | Better-MR Avalon troops, buffs, spacing, imported Astral, and target-specific counters | Assuming a sacred tag protects ordinary soldiers from MR checks. |
| Raiding and dispersed pressure | Forest recruitment, non-fort queues, scouts, Bards, cavalry, and prepared local leaders | Keeping every useful commander and mage in the capital. |
| Attrition and mage loss | Monks for distributed research, protected rare randoms, reserves, and retreat planning | Risking the only Water, Earth, Fire, or Air result in routine frontline work. |

## Monthly Man audit

- Is the next gold piece buying troops, a field leader, a mage, or the infrastructure that multiplies later recruitment?
- Does every Longbowman group have a line that can hold for the expected approach?
- Are forests contributing Royal Foresters or Foresters where that queue is useful?
- Are safe non-fort provinces producing the right Logrian unit, Monk, or Wise Man?
- Is the capital commander queue solving a path or leadership shortage?
- Are Mother, Crone, and Wise Man randoms labelled by final paths and assigned jobs?
- Does the current research target have a legal caster already recruited?
- Are Nature and Glamour gems divided between battle use, summons, and reserves before spending begins?
- Is a Chorus sized and scripted around its actual masters and slaves?
- Do the Death rituals have a real D2 route, or are they only names in the spell list?
- Are capital sacred losses justified by the battle and supported by the bless?
- Can the research stack survive a raid, assassination attempt, or forced retreat?

## Man unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for each line, longbow, cavalry, and sacred package;
2. live 6.36 display confirmation of the two Mother rolls, the Wise Man mask, and especially the Crone's pinned 10% second random;
3. current spell-card confirmation of Herd of Unicorns' forest-source restriction;
4. Chorus fatigue, casting-time, path-boost, unconscious-slave, and script outcomes in specific battles;
5. Geas target choice, resistance, and practical value against different formations;
6. rider-and-mount survival outcomes for Logrian Cavalry, Knights of Man, and Knights of Avalon;
7. the economic payback of distributed Wise Man and Monk recruitment on different maps;
8. hero arrival timing and the value of late elemental or Astral access;
9. modded Man variants, which remain separate from this unmodded chapter.

These questions stay visible without becoming guessed conclusions or new test assets. R-047, R-058, and the rest of the hands-on runtime queue remain parked.

# Part XX: Middle Age Abysia, Blood and Fire

## Abysia one-page command brief

Middle Age Abysia converts heat, heavy infantry, strong priests, and a capital Blood-mage queue into a compact but demanding war machine. Ordinary forts supply Humanbred screens, four weapon profiles of Abysian Infantry, Salamanders, assassins, animal handlers, Warlords, and two grades of Fire priest. The capital adds Lava Warriors and three Blood-capable commanders, including fixed S2 B3 Warlocks.

The reliable core is straightforward:

- Humanbred cost fewer resources and move faster than the armoured Abysian line, so they can supply bodies where protection is not the only requirement;
- Abysian Infantry provide fire-resistant heavy troops with battleaxe, flail, shielded axe, and shielded morningstar profiles;
- Salamanders add large heat effects and fire attacks, but they are animals, undisciplined, and expensive in gold per body;
- Anathemant Salamanders provide repeatable F2 H2, while Anathemant Dragons provide fixed F3 E1 H3;
- Warlock Apprentices, Demonbred, and Warlocks put Blood access in the capital commander queue;
- the two capital sites generate five Fire gems each month and gate every capital-only recruit;
- national magic spans Fire battle support, Blood crossbreeding, two summons, and a hostile-province ritual;
- repeatable recruits have no fixed Air, Water, Death, Nature, or Glamour access.

Abysia's roster is narrow enough to understand and expensive enough to punish an unfocused plan. Heavy infantry consume resources, Warlocks consume gold, Demonbred consume the entire four-point capital commander allowance shown on their card, and Salamanders consume gold that could have funded another mage or fort. The first question each month is not which strong object exists. It is which bottleneck the next purchase removes.

## Abysia evidence and ruleset

The scope is unmodded MA Abysia on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing national rules, recruitment locations, displayed paths, costs, national spells, rituals, and artifact description. Object identifiers, site fields, nation restrictions, hero records, and expanded random slots are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The official 6.01 announcement says only that Abysia's wall defenders were tweaked. It does not print a new defender count, composition, or formula, so none is invented here. The later 6.27 reference to EA Abysia's AI is not applied to the Middle Age nation. A current unit card, spell card, or battle remains authoritative where the manual and the older structured snapshot expose different levels of detail.

## Abysia conversion chain

```text
heat preference and fire-resistant bodies
-> Humanbred screens, armoured infantry, and early commanders
-> forts, laboratories, temples, and protected recruitment queues
-> Fire priests plus capital Astral-Blood mages
-> Fire research, blood hunting, and national rituals
-> target-specific infantry, heat, assassination, and mage packages
-> protected Blood economy, sieges, and Throne operations
```

The chain commonly breaks at three points. Too much armour can delay infrastructure because resources do not pay gold costs. Too many capital mages can leave Lava Warriors and field leadership underproduced. A Blood plan can also consume commanders and population without first building safe hunting provinces, patrollers, laboratories, and a reason to spend the slaves.

## Abysian national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Heat preference +3 | The roster is designed around very hot territory; scales and foreign provinces must be evaluated from Abysia's preference, not a generic human baseline. |
| Heat limit +2 and Death limit +1 | Pretender-scale choices have nation-specific limits. This does not make every extreme setting economically correct. |
| Radiated heat and Fire Resistance | Most Abysian bodies carry Heat 3 and Fire Resistance 25. Humanbred instead have Fire Resistance 15 and no printed Heat ability. |
| Modified Growth and Death effects | Growth and Death have half the standard effect on income and population growth and no effect on supplies. Population still dies slowly in Abysian provinces with Death scales. |
| Fort protection from heat deaths | Forts reduce heat-scale deaths by two steps. This is a population rule, not a claim that forts erase every economic consequence of temperature. |
| Cave-fort bonus | The manual grants extra gold and resources in cave forts, but prints no amount. Cave provinces are attractive, while the missing multiplier stays unquantified. |
| Powerful priests and blood sacrifice | H2 and H3 priests support sacreds, preaching, and sacrifice. Blood sacrifice still spends slaves and priest turns. |
| Bless points +1 | Abysia receives one extra bless point, but most of its ordinary infantry is mundane. The main recruitable sacred troop is the capital-only Lava Warrior. |
| No national missile troops | Ranged pressure must come from magic, summons, independents, or imported options. A heavy line does not itself answer a protected enemy caster. |

The Growth and Death exception is easy to overread. It changes several scale effects, yet it does not make population disposable: Death still kills people, Blood hunting raises unrest, and lost population can still reduce later income. The roster's fire resistance also does not make it immune to cold, armour-negating damage, fatigue, morale failure, or magic-resistance attacks.

## Abysia capital sites and recruitment queues

| Site | Verified fields | Recruitment consequence |
| --- | --- | --- |
| The Smouldercone, site 1 | Four Fire gems per month; Heat scale capped at 4 | Enables Warlock Apprentice, Warlock, and Demonbred |
| Temple of the All-Consuming Flame, site 121 | One Fire gem per month | Enables Lava Warrior |

Together the sites produce five Fire gems each month. That income supports Fire operations, not the Blood slaves or Astral pearls implied by the capital mages. Those economies require their own provinces, searches, trades, conversions, or imported access.

The Smouldercone creates the main capital-queue decision. A Warlock Apprentice costs 190 gold and two recruitment points; a Warlock costs 400 gold and two; a Demonbred costs 375 gold and four. The Temple creates a separate capital troop option, but the same capital must still supply ordinary troops, infrastructure, and commanders. A queue should be planned by the capability required next, not by buying the most expensive unit automatically.

## Abysia roster by job

| Unit or group | Best job | Important limit |
| --- | --- | --- |
| Humanbred with spear | Lower-resource screen and longer-weapon body | Morale 9, Protection 9, Fire Resistance 15, and no heat aura make it materially different from an Abysian Infantryman. |
| Humanbred with axe | Lower-resource damage body behind or beside a holding line | The axe version gives up the spear's length and still has the Humanbred defensive profile. |
| Battleaxe Abysian Infantry | Heavy two-handed damage | No shield; slow combat speed and encumbrance make contact and fatigue part of the purchase. |
| Flail Abysian Infantry | Heavy alternative weapon profile | No shield and lower printed Defence than the battleaxe version; use only when the target justifies the weapon. |
| Shielded axe Abysian Infantry | Protected general line | More resources and encumbrance than the two-handed profiles; its one-handed damage must still defeat the target. |
| Shielded morningstar Abysian Infantry | Protected line with a different damage profile | The highest resource cost among ordinary infantry variants and no universal answer to armour. |
| Salamander | Fire attack and Heat 6 pressure | Animal, undisciplined, Morale 9, and 50 gold; needs suitable leadership and a battle where heat or fire matters. |
| Lava Warrior | Capital-only sacred assault infantry | Thirty gold, 28 resources, Berserker +3, two weapons, and low printed Defence; losses consume a limited capital queue. |

The four Abysian Infantry versions are choices, not a progression ladder. Shielded troops improve the defensive profile against many mundane missiles and attacks, while two-handed troops preserve a different weapon and resource trade. Exact performance depends on the enemy weapon, protection, size, formation, fatigue, and terrain; the dossier does not assign a universal winner.

## Abysia commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Slayer | Stealth 60, Assassin, Patience +1 | Scouting, assassination pressure, and intelligence | Ninety-five gold for no army leadership or magic path; assassination outcomes remain target dependent. |
| Beast Trainer | Beastmaster 3, Animal Awe +4, Magic Leadership 10 | Handling Salamanders and other suitable animals | Inspirational -1 and Leadership 25 mean it is not Abysia's general field commander. |
| Warlord | Leadership 100, Taskmaster +2, two axes | Main mundane army command | One hundred ten gold and 34 resources compete with another armoured body and infrastructure. |
| Anathemant Salamander | F2 H2, sacred | Repeatable Fire research, priest work, blood sacrifice, blessing, and battle support | Two recruitment points and 260 gold; it does not reach the F3 E1 national spell by itself. |
| Anathemant Dragon | F3 E1 H3, sacred | High priest, national spell access, forging, and Fire-Earth support | Four recruitment points and 415 gold; the pinned random slot is not printed on the manual card. |
| Warlock Apprentice | S1 B2, Adept Cross Breeder +2 | Blood research, hunting support, communions, and Infernal Breeding | Capital-only and two recruitment points; it has no Fire path despite being Abysian. |
| Demonbred | F2 B2 H2, flying, Blood Searcher 1, sacred | Mobile priest, Blood search, Fire-Blood support, and command | Capital-only, four recruitment points, and 375 gold; flying mobility does not prove a safe raid. |
| Warlock | S2 B3 plus pinned randoms, Adept Cross Breeder +6 | Main Astral-Blood mage, crossbreeding, hunting, rituals, and research | Capital-only and 400 gold; every useful random result must be labelled and protected. |

The ordinary-fort commander pool and capital pool solve different problems. Warlords move conventional armies. Anathemants provide religion and Fire. The three Smouldercone recruits build Blood and Astral capacity. Treating all eight as interchangeable commanders hides the queue that actually limits each plan.

## Reading the Abysian random paths

The pinned path mask `35968` decodes to Fire, Earth, Astral, or Blood. Its four component bits are 128, 1024, 2048, and 32768. The mask appears in both the Warlock and Anathemant Dragon records, but the roll structure differs.

### Warlock distribution

Every Warlock begins at S2 B3. The manual then prints one random level. The pinned 6.35 record resolves that display as:

1. one guaranteed level chosen equally from Fire, Earth, Astral, or Blood;
2. an independent 10% chance of a second level from the same four paths.

For any one named path, the first roll hits 25% of Warlocks. If it misses, the second roll can still add that path with probability `75% x 10% x 25%`. The chance of reaching at least one level in a named random path is 26.875%.

| Portfolio result | Probability per Warlock |
| --- | ---: |
| No second random level | 90% |
| Second level matches the first path | 2.5% |
| Second level is a different path | 7.5% |
| Any one named path appears at least once | 26.875% |
| A chosen named path appears twice | 0.625% |
| At least Fire or Earth appears | 52.5% |

Three independent Warlocks give about a 60.90% chance of at least one result in a chosen named path. Five give about 79.09%, and ten give about 95.63%. These figures measure a recruitment portfolio. They do not guarantee when the result arrives, that it survives, or that the economy can afford uninterrupted recruitment.

The threshold consequences are asymmetric. A Fire double produces F2 on the Warlock; an Earth double produces E2; an Astral double raises the fixed S2 to S4; and a Blood double raises fixed B3 to B5. A single Astral or Blood result instead produces S3 or B4. These path cards open different spell and forge branches, so the final paths should be recorded immediately.

### Anathemant Dragon pinned random

The Anathemant Dragon is fixed F3 E1 H3 in the manual. The pinned structured record adds an independent 10% one-level roll from Fire, Earth, Astral, or Blood. That gives 90% no extra level and 2.5% each for F4, E2, S1, or B1.

This slot is less secure than the Warlock's printed random because the manual page shows no random marker at all. The dossier uses it only as a 6.35 planning possibility. In particular, native F4 ritual access must remain conditional until a current recruitment card confirms the bonus.

## Abysia native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Fire | F2 Anathemant Salamander and Demonbred; F3 Anathemant Dragon; Warlock random | Strong and distributed, although the capital Fire-Blood mage and high priest are expensive. |
| Earth | Fixed E1 Anathemant Dragon; Warlock random; pinned Dragon random may reach E2 | No ordinary repeatable E2 guarantee. |
| Astral | S1 Apprentice, fixed S2 Warlock, Warlock random | Capital-only; the main Warlock can reach S3 or rarely S4 under the pinned scheme. |
| Blood | B2 Apprentice and Demonbred, fixed B3 Warlock, Warlock random | Capital-only; hunting, unrest control, slaves, laboratories, and caster turns all need a budget. |
| Air, Water, Death, Nature, Glamour | No repeatable recruit | Must come from independents, summons, empowerment, transformation, items after another bridge, or the Pretender. |

None of the three pinned national heroes supplies Air, Water, Death, Nature, or Glamour. Owning a Death ritual does not create a native Death caster. A plan that needs one of these paths must name the source, timing, cost, search route, and replacement plan.

## Abysia national spells and caster access

| ID | Spell or ritual | Research and paths | Cost or fatigue | Verified native access |
| ---: | --- | --- | --- | --- |
| 317 | Summon Spectral Infantry | Conjuration 2, D1 F1 | 5 Death gems | No recruit or pinned hero has Death; national ownership is not native castability. |
| 318 | Contact Scorpion Man | Conjuration 8, E1 F1 | 12 Earth gems | Fixed Anathemant Dragon qualifies. |
| 319 | Inner Furnace | Enchantment 5, F3 | 100 fatigue, battlefield-wide | Fixed Anathemant Dragon qualifies; an F2 battle caster may require a separate Fire-boost route. |
| 320 | Infernal Breeding | Blood 3, B2 | 25 blood slaves | Apprentice, Demonbred, and Warlock qualify. |
| 690 | Liquid Flames of Rhuax | Evocation 5, F3 E1 | 20 fatigue, range 30+, area 1 | Fixed Anathemant Dragon qualifies. |
| 850 | Hellscape | Alteration 6, F4 | 10 Fire gems, range 5 | Pinned F-random Dragon reaches F4 only 2.5%; otherwise another explicit bridge is required. |

Inner Furnace is described as strengthening the heat radiated by every Abysian on the battlefield. Its exact radius increase, affected-unit boundary, stacking, and fatigue consequences are not derived from the database effect field. Liquid Flames of Rhuax is an armour-piercing Fire attack and is marked unavailable underwater in the manual.

Infernal Breeding crossbreeds Abysians, humans, and giants with demons, Salamanders, and other beasts. The manual warns that many Hell Spawn suffer afflictions and early aging. Neither the manual nor a spell row supplies a complete current output distribution, so the dossier does not promise a particular creature count or quality beyond the ritual record.

Hellscape is an anonymous hostile-province ritual. Its printed effects are Heat +3, Death +1, population -10%, and unrest +20. The fixed Dragon does not meet F4 without another step; a battlefield Fire boost cannot be carried into a strategic ritual. Researching Alteration 6 for Hellscape should follow confirmed caster access, not precede it on hope.

## Abysia national item boundary

O'al Kan's Sceptre, item 97, is a unique Construction 9 artifact requiring F3. The pinned item record grants a national rebate to both EA Abysia 16 and MA Abysia 63. The manual lists Fire Spell Range +50%, Cold Resistance +10, Leadership +100, the spell Flare, and a small-area fatigue effect on strike.

A fixed Anathemant Dragon meets the printed F3 forging path. That does not settle the displayed gem cost after the national rebate, other forge modifiers, artifact availability, and rounding are combined. The live forge screen controls that value. The artifact's late research and uniqueness also mean it is a possible capstone, not an opening solution to leadership or range.

## Abysia opening priorities

The opening should secure four systems before adding exotic branches:

1. enough field leadership to move the troop profile being purchased;
2. a line whose protection, weapon, movement, and gold cost fit the nearby independents;
3. laboratories, temples, and forts that can recruit the next mage or priest without stranding the army;
4. a capital queue split deliberately among Blood-Astral access, mobile Demonbred, and other national needs.

An exact expansion count is not supplied. Humanbred, shielded infantry, two-handed infantry, Salamanders, and Lava Warriors face different risks against cavalry, missiles, high Defence, armour, cold, poison, and morale pressure. Map generation, scales, bless, commander, formation, and combat rolls change the minimum safe force.

The first additional fort should be judged by gold, resources, caves, neighbours, travel geometry, and commander access together. A cave bonus can improve a fort's value, but the manual gives no number. A rich surface chokepoint may still be more useful than a cave that cannot protect borders or connect armies.

## Abysia recruitment packages to evaluate from reports

### Humanbred screen

Use Humanbred where lower resource cost, higher map movement, or additional bodies matter more than Abysian protection. Spears can extend the weapon line; axes change the damage profile. Their Morale 9 and lower fire resistance require appropriate leadership and positioning; they are distinct from the Abysian line.

### Armoured Abysian line

Choose shielded axe or morningstar versions when the defensive profile answers the observed threat. Choose battleaxe or flail versions when their weapon and lower resource cost justify losing the shield. Keep the line narrow enough for support to reach it and broad enough that slow troops do not leave an exposed flank.

### Salamander group

Salamanders offer Fire Flare, a bite, Heat 6, and Heat Power 1. A Beast Trainer provides the relevant animal leadership tools, while a mage or Warlord may supply the rest of the force. The group should be selected against a target that is vulnerable to its damage and fatigue pressure; fire resistance, dispersal, cold, morale, or fast contact can change the value sharply.

### Lava Warrior reserve

Lava Warriors concentrate capital resources, sacred status, two attacks, Berserker +3, and Heat Power 1. They are an elite answer only when the bless, commander, and target justify scarce recruitment. Low printed Defence and berserking make extraction and casualty control part of the decision.

## Abysia research response tree

Research begins with a battlefield or strategic problem and a recruited caster. Abysia owns several national spells at attractive path thresholds, but it cannot deploy every branch from the same mage pool or gem economy.

### Branch A: Fire battlefield breakpoints

Conjuration 3's Phoenix Power lets an F2 battle caster reach a higher Fire threshold. Enchantment 5 then offers Inner Furnace at F3, while Evocation 5 offers Liquid Flames of Rhuax to F3 E1. The fixed Dragon reaches both national spells directly; Salamander priests and Demonbred can use an available battle boost for F3 effects but do not gain the Dragon's Earth path.

This branch is strongest when heat pressure or armour-piercing Fire solves the reported enemy. It is weaker against fire resistance, rapid mage disruption, underwater operations, or a battle where Abysia's own fatigue and formation fail before the Fire package matters.

### Branch B: Blood economy and Infernal Breeding

Blood 3 makes Infernal Breeding available to all three capital Blood-mage types. The research is only one part of the cost. The plan also needs hunting provinces, patrollers, laboratories, slave transport, unrest control, and mage turns. Apprentices are cheaper crossbreeders; Warlocks carry stronger Blood and the larger Adept Cross Breeder value; Demonbred add flight, priesthood, and Blood Searcher 1.

No expected return is assigned to the ritual or a hunting province. Population, unrest, scales, hunter skill, patrol strength, random outcomes, and current engine rules determine the result. Record actual slaves, unrest, population loss, and outputs before calling the branch efficient.

### Branch C: Astral-Blood Warlocks

Fixed S2 B3 makes every Warlock a useful Astral-Blood platform before randoms. Astral and Blood randoms raise the ceiling, while Fire and Earth randoms add cross-path options. This branch should be chosen after recruiting and labelling the actual portfolio; a research target that needs S3, B4, F1, or E1 is conditional until the relevant Warlock exists.

The capital-only nature of the whole Astral pool creates a strategic risk. One raid, siege, or assassination campaign can threaten research, blood hunting, and high-path casting together. Distributed forts, ordinary priests, protected movement, and reserve mages reduce that concentration.

### Branch D: summons and remote pressure

Conjuration 2 lists Summon Spectral Infantry, but its D1 F1 requirement exposes a missing native path. Conjuration 8's Contact Scorpion Man is reachable by the fixed Dragon and costs 12 Earth gems. Alteration 6's Hellscape requires F4 and ten Fire gems, with only conditional native access in the pinned Dragon random.

These rituals should be scheduled from the caster backward. Confirm the path, laboratory, research, gems, province, and opportunity cost first. A national name in the spell list is not a reason to divert research when the legal caster or gem income does not exist.

## Abysia battlefield packages

### Humanbred screen with Abysian damage

Humanbred occupy space and absorb selected contact while more expensive Abysian Infantry supply the weapon needed against the target. The two groups should not be treated as statistically identical. Leadership, morale, movement, fire resistance, and heat exposure differ, so formation and retreat routes matter.

### Shielded line with priest support

Shielded Abysian Infantry form the main protected block while an Anathemant blesses sacred auxiliaries, supports morale and religion, or delivers reachable Fire magic. A Warlord can preserve the priest's script and commander turn for magic. The package still needs an answer to enemies that ignore armour or attack the rear.

### Salamander heat cell

A limited Salamander group applies Heat 6 and fire attacks beside fire-resistant national troops. Beast Trainer support keeps the animal role explicit. Inner Furnace may intensify the wider Abysian heat package, but its live area and fatigue interactions remain open; do not assume that adding more heat is harmless or universally effective.

### Anathemant Fire battery

F2 Salamander priests provide the repeatable base, while a Dragon supplies F3 E1 and H3. The battery is selected for a specific spell breakpoint and protected by troops and placement. Concentrating expensive priests can solve one battle while exposing research, sacrifice, and preaching elsewhere.

### Capital Blood operations cell

Apprentices perform lower-cost Blood and Astral work, Warlocks provide high paths and crossbreeding, and Demonbred provide mobile Fire-Blood priesthood. The cell needs scouts, patrol, laboratories, slave logistics, and a protected route between hunting provinces and casting centres. It should not sit as one undefended capital stack merely because every member was recruited there.

## Abysia Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and production | Supports gold-heavy mages, resource-heavy infantry, and additional infrastructure | Extra resources do not pay Warlock gold, while extra income does not replace capital recruitment points. |
| Missing-path bridge | Imports Air, Water, Death, Nature, Glamour, or dependable higher Earth | One god does not create distributed national access, search coverage, boosters, or replacement casters. |
| Sacred combat design | Improves Lava Warriors and sacred commanders | The bulk Humanbred and Abysian Infantry receive no bless. |
| Resistance and mobility design | Answers cold, shock, poison, magic resistance, map movement, or another observed gap | A broad defensive bless can crowd out the path or scale needed for the wider state. |
| Awake expander | Supplies early independent-taking power where the roster cannot meet the map safely | Afflictions, counter chassis, lost scales, and delayed path infrastructure can erase the tempo gained. |
| Ritual and forging bridge | Reaches Death-Fire, F4, higher Earth, or late artifact thresholds reliably | Research, gems, laboratory turns, and the Pretender's availability remain real costs. |

Abysia already possesses deep Fire, Blood, and Astral. A Pretender often creates more value by supplying a missing system, resistance, mobility, or reliable ritual bridge than by adding an unsupported theoretical endpoint. Each imported path should have a first search target, first forge or ritual job, and a plan if the Pretender is unavailable.

## Abysia matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Conventional missiles | Shielded infantry, terrain, spacing, pressure, and magic | Marching unshielded two-handed troops through fire because their armour looks high. |
| Heavy armour | Battleaxes, morningstars, Fire magic, buffs, summons, and target-specific control | Buying more low-damage bodies without checking whether they can penetrate. |
| High Defence, ethereal, or Glamour targets | Area effects, attack support, magic weapons, Astral tools, and imported counters | Treating a second expensive infantry block as guaranteed contact. |
| Fire-resistant armies | Mundane weapon selection, Earth support, Astral-Blood options, summons, or imported damage | Building the entire battle around heat and Fire because they are national strengths. |
| Cold and fatigue pressure | Resistance, shorter fights, formation depth, spell disruption, and reserves | Assuming native heat prevents cold damage or exhaustion automatically. |
| Armour-negating and MR attacks | Spacing, resistance, summons, counter-caster pressure, and target-specific buffs | Treating Protection 17 as a defence against every damage channel. |
| Fast flankers and flyers | Protected mages, guards, reserves, wider lines, and local commanders | Leaving the capital mage portfolio in one exposed rear cluster. |
| Raids and dispersed pressure | Warlords, Slayers, forts, scouts, patrols, and prepared local forces | Expecting slow infantry to recover every province after contact. |
| Underwater objectives | Independent or summoned amphibious access, a Pretender bridge, and a separate logistics plan | Assuming Fire resistance or wasteland survival supplies underwater capability. |
| Pressure on the Blood economy | Distributed hunting, patrols, protected laboratories, reserve casters, and alternative research | Concentrating slaves, hunters, researchers, and high-path mages in one vulnerable province. |

## Monthly Abysia audit

- Is the current troop queue limited by gold, resources, recruitment points, leadership, or travel time?
- Does each infantry version have a target-specific reason to be in the queue?
- Are Humanbred being used for their actual cost and movement profile, without treating them as disposable Abysians?
- Does every Salamander group have suitable leadership and a target vulnerable to heat or Fire?
- Is the capital commander queue buying the exact Astral, Blood, mobility, or priest capability required next?
- Are Warlock and Dragon randoms labelled by their displayed final paths?
- Does the research target have a legal, protected caster already recruited?
- Are Fire gems, Earth gems, and blood slaves budgeted separately?
- Are hunting unrest, patrol strength, population, and slave transport recorded instead of assumed?
- Is a cave fort valuable for its position as well as its unquantified national bonus?
- Are sacred recruitment and the bless large enough to justify one another?
- Can the research and Blood infrastructure survive a raid, siege, or assassination campaign?

## Abysia unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for Humanbred, each infantry weapon profile, Salamanders, and Lava Warriors;
2. live 6.36 confirmation of the Warlock's pinned 10% second random and any Dragon random, which the manual does not display;
3. the numerical cave-fort gold and resource bonus;
4. the exact post-6.01 wall-defender count and composition;
5. Inner Furnace's current affected-unit boundary, heat-area increase, stacking, and formation-level fatigue results;
6. Infernal Breeding's current output distribution, afflictions, ages, and economic return;
7. displayed O'al Kan's Sceptre cost after national rebate, other forge modifiers, artifact availability, and rounding;
8. assassination, blood-hunting, Blood Searcher, and patrol outcomes in a particular game state;
9. underwater access, battlefield scripts, and Pretender designs in a specific map and opponent field;
10. modded Abysia variants, which remain separate from this unmodded chapter.

These questions remain evidence gaps; no rule or new test asset fills them. R-047, R-058, and the wider hands-on runtime queue stay parked until testing is explicitly resumed.

# Part XXI: Middle Age Pythium, Emerald Empire

## Pythium one-page command brief

Middle Age Pythium turns a broad legion roster, powerful Astral priest-mages, a separate troop-queue communion recruit, and unusually high capital gem income into a flexible imperial army. Ordinary forts recruit nine commanders and twelve troop types. The capital adds the Arch Theurg, Hydra Tamer, Battle Vestal, Hydra Hatchling, and Hydra through two national sites.

The reliable core is easy to state:

- the legion roster ranges from cheap Slingers and Velites to Hastati, Principes, Triarii, and Emerald Guards;
- Serpent Cataphracts add a heavily protected rider and a separately tracked Armored Serpent mount;
- Theurg Acolytes provide S1 H1, Theurgs provide A1 W1 S2 H2, and capital-only Arch Theurgs begin at A2 W1 S3 H3 before randoms;
- Theurg Communicants are troop recruits with a printed limit of one per month and a pinned automatic Communion Slave field;
- the Cathedral of the Spheres supplies two Air gems, one Water gem, and five Astral pearls each month;
- the national ritual list contains six angelic summons plus Contact Lar and Awaken Hamadryad;
- repeatable recruits have no fixed Earth, Death, Nature, Glamour, or Blood access;
- the official manual gives Pythium an Order scale limit of +1 and a Fortified City at the start.

Pythium has options, but each option draws on a different queue. Arch Theurgs consume capital commander time and 565 gold. Hydras consume capital troop time, 200 gold, and a one-per-month slot. Theurg Communicants use the troop queue even though their purpose is magical. A strong plan names which queue is solving which problem before the capital becomes a collection of expensive pieces without a field army.

## Pythium evidence and ruleset

The scope is unmodded MA Pythium on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing nation rules, printed roster, costs, recruitment locations, paths, national rituals, and mount statistics. Object identifiers, site fields, hidden random slots, national restrictions, item-rebate fields, hero records, and special unit flags are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The official update ledger through 6.36 contains one Pythium name match: a 6.07 correction for Epoteia that explicitly belongs to Late Age Pythium. It is not applied to the Middle Age nation. No ledger record through 6.36 names MA Pythium, one of its listed recruits, either capital site, or one of its national rituals as receiving a direct change. That is a patch-ledger result, not proof that no undocumented engine change exists; a current game card remains authoritative when it exposes newer detail.

## Pythium conversion chain

```text
fortified capital, legion choices, and eight capital gems
-> target-specific infantry, leaders, and early expansion
-> forts, laboratories, temples, and protected recruitment
-> Acolytes, Theurgs, Arch Theurgs, and Communicants
-> battlefield communions, Grand Communion, and national rituals
-> legion support, Astral control, Air damage, and summoned specialists
-> protected mage economy, siege operations, and Throne claims
```

The chain most often breaks when one resource is mistaken for another. Eight capital gems do not pay the gold cost of a Theurg. Cheap legionnaires do not protect a communion by themselves. A large communion can reach high paths and still fail through fatigue, slave losses, a dead master, or a threatened rear. Pythium works best when its army, mage turns, pearls, and replacement plan are budgeted together.

## Pythian national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Order limit +1 | Pythium can take a higher Order scale than a normal nation. The extra legal point is an option, not a command to use it in every design. |
| Fortified City start | The capital begins with stronger infrastructure than an ordinary starting fort. It still has only one commander queue and one troop queue each turn. |
| Standard forts | Expansion of the recruitment network follows the normal fort system; capital-only mages, sacreds, and hydras remain tied to their sites. |
| Powerful priests | Repeatable H2 Theurgs and the capital H3 Arch Theurg support religion and battlefield priest work; the pinned hero Bartholomeus reaches H4. |
| High capital gem income | The Cathedral produces A2, W1, and S5 each month, eight gems in total. Nature rituals and Nature-forged national items still need a separate Nature economy. |
| Grand Communion | The official manual uses Pythium's Arch Theurg, Theurgs, and Acolytes as its worked example for strengthening a public ritual such as Dispel. Joining mages give up their own activity for that ritual. |
| Separate communion recruit | Theurg Communicants are recruited as troops, printed at one per month, and carry a pinned automatic Communion Slave field. They ease pressure on the commander queue but compete with the army queue. |
| Serpent mounts | Serpent Cataphracts and Serpent Lords ride Armored Serpents with their own hit points, protection, and poisonous bite. Rider and mount outcomes remain separate. |
| Capital hydras | Hydras and Hatchlings offer regeneration, poison resistance, and multiple head weapons in the printed roster. The pinned record also marks poison clouds and other fields whose live operation remains open. |

The strongest national features do not all point in the same direction. Legionnaires reward broad fort recruitment, while Arch Theurgs and hydras remain capital bound. Grand Communion concentrates ritual power in one province, while campaign survival usually rewards distributing ordinary Theurgs and replacement armies. The plan must decide when concentration is worth the risk.

## Pythium capital sites and recruitment queues

| Site | Verified fields | Recruitment consequence |
| --- | --- | --- |
| Cathedral of the Spheres, site 3 | Two Air gems, one Water gem, and five Astral pearls per month | Enables Arch Theurg and Battle Vestal |
| Swamps of Pythia, site 4 | No gem income in the pinned site row | Enables Hydra Tamer, Hydra, and Hydra Hatchling |

The Cathedral produces eight gems each month. This supports Air, Water, and especially Astral work, but not the Nature gems required by Contact Lar, Awaken Hamadryad, Gloves of the Gladiator, or Hydra Skin Armor. Search coverage, trade, site capture, or another explicit source must fund that branch.

The capital has two distinct decisions. Its commander queue chooses between the four-point, 565-gold Arch Theurg and the one-point Hydra Tamer, along with any ordinary commander. Its troop queue chooses among legionnaires, Battle Vestals, Communicants, Hydra Hatchlings, and the 200-gold Hydra. Monthly limits on the Hydra and Communicant do not create extra queues; they only limit those individual recruits.

## Complete Pythium roster by job

| Unit or group | Best job | Important limit |
| --- | --- | --- |
| Slinger | Cheapest printed missile body | Morale 7, low protection, and low melee skills make it a support body, not a line anchor. |
| Retiarius and Gladiator | Low-resource shock troops with net-trident or flail profiles | The pinned records mark both as Single Battle. Their current departure timing remains a live-card question. |
| Velite | Mobile skirmishing infantry with spear and javelin | Protection 7 and Morale 10 demand suitable targets and leadership. |
| Alae Legionnaire | Ten-gold armoured spear-and-javelin body | The cheap gold price is balanced by 20 resources and ordinary Morale 10. |
| Hastatus | Short-sword legionnaire with javelin | Eleven gold and 21 resources; its value depends on whether the weapon profile reaches the target. |
| Principe | Higher-skill, higher-morale legion line | Fourteen gold and 20 recruitment points reduce the number produced from a busy fort. |
| Triarius | Heavily protected long-spear line | Twenty-nine resources, 25 recruitment points, Encumbrance 10, and Combat Speed 6 make fatigue and contact central concerns. |
| Emerald Guard | Elite human bodyguard and line troop | Twenty gold, 30 resources, and 31 recruitment points make losses expensive; its broad sword still needs to beat the target's protection. |
| Standard | Legionnaire carrying the pinned Standard +1 field | Twenty gold for a support effect that should be placed where morale support is actually needed. |
| Serpent Cataphract | Mobile heavy rider with a poisonous serpent mount | Forty-five gold and 27 resources; rider and mount can be hit separately, and poison is not universal damage. |
| Battle Vestal | Capital-only sacred skirmisher | Low protection and nine hit points place a premium on bless design, positioning, and casualty control. |
| Hydra Hatchling and Hydra | Capital-only regenerating poison pieces | Fire Resistance -10, low combat speed, poison exposure, animal leadership, and friendly formation all need attention. |
| Theurg Communicant | Troop-queue communion support | Fifty gold, 31 recruitment points, one per month, and unable to act independently while serving as a communion slave. |

The legion roster is a set of cost and weapon trades, not a single ladder from bad to good. Alae Legionnaires put armoured bodies on the field cheaply in gold. Principes and Emerald Guards buy stronger individual profiles at a higher gold and recruitment-point cost. Triarii add protection and reach but also heavy encumbrance. Reports about the enemy should decide which mix is produced.

## Pythium commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Scout | Stealth 50, forest and mountain survival | Exploration and army reporting | Thirty-five gold and no leadership role beyond scouting. |
| Assassin | Stealth 65, Assassin, Patience +1 | Targeted pressure and intelligence | Outcomes depend on the target, guards, arena, equipment, and rolls. |
| Centurion | Leadership 100 | Ordinary legion command | Ninety-five gold and 21 resources; no priest or magic path. |
| Serpent Lord | Leadership 75, Skilled Rider 2 | Command for serpent-mounted forces and mobile detachments | The mount is a separate creature and does not share every rider protection. |
| Emerald Lord | Leadership 100 | Durable command and bodyguard work | One hundred twenty-five gold and 30 resources compete with an Emerald Guard group or infrastructure. |
| Legatus Legionis | Leadership 150 | Main large-army command | Two recruitment points and 150 gold; high capacity has value only when an army needs it. |
| Battle Deacon | H1, sacred, Leadership 50 | Cheap priest and small military command | No non-Holy magic path and only one priest level. |
| Theurg Acolyte | S1 H1, sacred | Lower-cost research, communion participation, preaching, and Astral support | Two recruitment points for a fragile mage with low battlefield skills. |
| Theurg | A1 W1 S2 H2, sacred, Fortune Teller 5 | Main repeatable mage-priest, battle communion master, research, and priest work | Three hundred gold; using one in a Grand Communion also consumes its strategic turn. |
| Hydra Tamer | Swamp Survival and Poison Resistance 15; pinned Beastmaster 2 | Hydra leadership and poison-aware support | Capital-only, Leadership 10, and no magic path; it is a specialist, not a general commander. |
| Arch Theurg | A2 W1 S3 H3 plus pinned randoms, Fortune Teller 10 | High Astral ritual work, Grand Communion lead, Air-Water support, and high priest duties | Capital-only, 565 gold, and four recruitment points; the second pinned random is not printed in the manual. |

The ordinary-fort mage line is the strategic backbone. Acolytes put S1 and H1 in every developed recruitment centre. Theurgs provide the fixed A1 W1 S2 H2 package that supports several schools without waiting for a random. Arch Theurgs raise the ceiling, but a plan that uses them for every magical job will overload the capital and leave valuable ordinary forts underused.

## Reading the Arch Theurg random paths

The official manual prints the Arch Theurg as A2 W1 S3 H3 with one random level. The pinned 6.35 record resolves mask `2944` into Fire, Air, Water, or Astral and records two rolls:

1. one guaranteed level chosen equally from Fire, Air, Water, or Astral;
2. an independent 10% chance of a second level from the same four paths.

The mask components are 128, 256, 512, and 2048. The second slot is not visible in the manual's `?1` summary, so it remains pinned planning evidence without current 6.36 display confirmation.

### Arch Theurg distribution

| Portfolio result | Probability per Arch Theurg |
| --- | ---: |
| No second random level | 90% |
| Second level matches the first path | 2.5% |
| Second level is a different path | 7.5% |
| Any one named path appears at least once | 26.875% |
| A chosen named path appears twice | 0.625% |
| At least Air or Water appears | 52.5% |

For Fire, the result is at least F1 on 26.875% of Arch Theurgs and F2 on 0.625%. Air results raise fixed A2 to at least A3, Water results raise W1 to at least W2, and Astral results raise S3 to at least S4. A matching second roll can rarely reach A4, W3, or S5.

Three independent Arch Theurgs give about a 60.90% chance of at least one result in a chosen named path. Five give about 79.09%, and ten about 95.63%. Those figures describe a recruitment portfolio, not a schedule. The capital cost, four-point queue, survival, and arrival order still decide whether a threshold exists when it is needed.

## Pythium native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Astral | S1 Acolyte, S2 Theurg, S3 Arch Theurg, Arch random | Deep and widely recruitable; high ritual thresholds still require rare randoms, boosters, empowerment, summons, or a Pretender. |
| Air | A1 Theurg, A2 Arch Theurg, Arch random | Repeatable A1 and capital A2; A3 is conditional without a battle communion or another bridge. |
| Water | W1 Theurg and Arch Theurg, Arch random | Repeatable W1; W2 and W3 depend on capital randoms or an imported step. |
| Fire | Arch Theurg random only | No fixed recruit has Fire. Even F1 access is a random portfolio result. |
| Holy | H1 Deacon and Acolyte, H2 Theurg, H3 Arch Theurg | Strong repeatable priest line; the hero Bartholomeus reaches H4. |
| Earth, Death, Nature, Glamour, Blood | No repeatable recruit | Must come from independents, a Pretender, empowerment, summons, transformations, or another proved bridge. |

The three pinned heroes do not fill a missing non-Holy path. Bartholomeus supplies A2 W2 S3 H4, while Marius Lorca and Hierogallus have no magic paths in the snapshot. Pythium owns two Nature rituals and two Nature-forged discounted items, but national ownership does not create a Nature caster or Nature gems.

## Grand Communion and ordinary communions

The manual distinguishes battlefield communions from Grand Communions. An ordinary Astral communion needs Communion Master and Communion Slave in effect. Masters gain one level with two slaves, two levels with four, three with eight, and so on. Spell fatigue is divided among participants and then modified by the slaves' path levels. If every master dies or flees, the slaves receive the printed backlash.

Theurgs and Acolytes can cast the Thaumaturgy 1 communion spells because they have Astral magic. The pinned Communicant field places that troop into the slave role automatically. This saves a setup action but also means a Communicant is not an independent battle caster. Exact survival still depends on master spells, slave paths, fatigue, resistances, buffs, battlefield timing, and enemy access to the rear.

Grand Communion is a strategic ritual order. The official example has an Arch Theurg cast Dispel while Theurgs and Acolytes in the province add their Astral levels. Each helper gives up its own activity for the turn. Grand Communion can make a key public ritual stronger, but it also concentrates mages and opportunity cost in one place. It should not be counted as a battlefield communion or as free ritual strength.

## Pythium national rituals and caster access

| ID | Ritual | Research and paths | Cost and result | Verified native access |
| ---: | --- | --- | --- | --- |
| 477 | Contact Angel of the Host | Conjuration 5, S3 | 7 Astral pearls; one Angel of the Host | Fixed Arch Theurg qualifies. |
| 479 | Angelic Choir | Conjuration 6, S3 | 15 Astral pearls; three Angels of the Heavenly Choir | Fixed Arch Theurg qualifies. |
| 481 | Heavenly Wrath | Conjuration 7, S3 F1 | 35 Astral pearls; one Angel of Fury | Requires an Arch Theurg with Fire or another S3 F1 caster; pinned native chance is 26.875% per Arch. |
| 478 | Contact Harbinger | Conjuration 6, S4 | 25 Astral pearls; one A3 H2 Harbinger | Requires an Astral-random Arch or another S4 bridge; pinned chance is 26.875% per Arch. |
| 480 | Angelic Host | Conjuration 7, S5 | 50 Astral pearls; six Angels of the Host | A double-Astral Arch reaches S5 only under the pinned 0.625% result; otherwise another bridge is required. |
| 482 | Heavenly Choir | Conjuration 9, S7 F2 | 144 Astral pearls; Seraph and choir host | No recruit or hero meets both thresholds. This is a late external-access project. |
| 275 | Contact Lar | Conjuration 5, N1 | 16 Nature gems; one W1 E1 N2 Lar | No recruit or pinned hero has Nature. An imported N1 caster and Nature economy are required. |
| 274 | Awaken Hamadryad | Enchantment 5, N4 | 25 Nature gems; one N3 Hamadryad | No native N4 caster. The printed summon also has map movement 0 and Research -4. |

The angelic branch aligns with the capital's five Astral pearls per month and fixed S3 Arch Theurg. The first two rituals are directly castable once research and pearls exist. Higher thresholds depend on the actual random portfolio, boosters, empowerment, a summon, or a Pretender. Grand Communion is not silently applied to ordinary unit-summoning rituals.

Contact Lar is the main national bridge into a missing path family. The ritual needs imported N1, but the summoned Lar carries W1 E1 N2. That can create Earth access and reach the printed N2 requirement of both national-discount items once the relevant Construction research and gems exist. Awaken Hamadryad remains harder because it needs N4 before producing an N3 unit.

## Pythium national item boundary

Two pinned item records carry a Pythium national-rebate field:

| ID | Item | Construction and paths | Printed properties | Access boundary |
| ---: | --- | --- | --- | --- |
| 41 | Gloves of the Gladiator | Construction 3, N2 | Magic Resistance +1, Strength +3, four attacks | No native Nature mage; a Lar or another N2 bridge can forge it. |
| 269 | Hydra Skin Armor | Construction 7, N2 | Hit Points +8, Regeneration 10%, Poison Resistance +15 | Same N2 boundary, with much later research. |

The structured rows establish a national rebate marker, not the final gem price shown after every discount, forge bonus, and rounding step. The live forge screen controls that number. Neither item should be counted as an early national asset until Pythium has a legal N2 forger, Nature gems, the research level, and a safe forge turn.

## Pythium national heroes

| ID | Fixed name | Unit name | Verified role or paths |
| ---: | --- | --- | --- |
| 584 | Bartholomeus | Patriarch | A2 W2 S3 H4; high priest and fixed caster for the S3 angel rituals |
| 505 | Marius Lorca | Hero | Mundane Leadership 100 commander with strong personal combat statistics; no magic path recorded |
| 506 | Hierogallus | Hero | Mounted Leadership 100 commander on Armored Serpent; Skilled Rider 3; no magic path recorded |

Hero arrival is not a recruitment plan. Bartholomeus expands fixed Water and Holy depth but does not add Fire, Earth, Death, Nature, Glamour, or Blood. Marius and Hierogallus add command options, while Hierogallus retains the same rider-and-mount separation that applies to recruited serpent cavalry.

## Pythium opening priorities

The opening should secure four things before chasing the expensive ritual list:

1. a troop mix chosen for the nearby independent weapons, protection, numbers, and terrain;
2. enough leadership to move that mix without tying a Theurg to mundane command;
3. laboratories and forts that can recruit Acolytes and Theurgs away from the capital;
4. a deliberate capital split among Arch Theurgs, hydra support, Battle Vestals, Communicants, and ordinary troops.

No exact expansion count is supplied. Alae Legionnaires, Hastati, Principes, Triarii, Serpent Cataphracts, Vestals, and hydras all face different risks. Map generation, scales, bless, commander, formation, enemy composition, and combat rolls change the minimum safe force.

The first additional fort has special value because the best repeatable Theurg is not capital-only. A new lab and fort can expand the A1 W1 S2 H2 mage line while the capital handles Arch Theurgs and site recruits. That benefit must still be compared with gold, travel time, resources, border safety, and the troops needed now.

## Pythium recruitment packages to evaluate from reports

### Legion core

Alae Legionnaires and Hastati provide affordable armoured bodies, Principes buy a stronger individual profile, and Triarii add protection and a long spear at a heavy resource and fatigue cost. Emerald Guards are the expensive elite option. The correct mix depends on the target's weapon length, damage, protection, missiles, and numbers; no legionary type is the answer to every province.

### Serpent wing

Serpent Cataphracts pair a protected rider with an Armored Serpent carrying 28 hit points, Protection 19, and a poisonous bite in the manual. They offer mobility and a different contact profile from the infantry line. The mount can be hit or killed separately, poison can be resisted, and a 45-gold rider must deliver enough value to justify the cost.

### Hydra group

Hydra Hatchlings and Hydras are capital-only pieces with regeneration, poison resistance, blunt and piercing resistance, and Fire Resistance -10 in the printed roster. The pinned rows add Animal, Undisciplined, poison-cloud, Beastmaster, and head-related fields. Use Hydra Tamers, separation, and poison-aware support while keeping exact cloud spread, friendly exposure, head loss, and regeneration behaviour open.

### Gladiator reserve

Retiarii and Gladiators cost little in resources and have useful contact profiles, but the pinned rows mark them Single Battle. They can be considered for a specific urgent fight, not silently counted as a permanent standing army. Current departure timing and the economic value of that exchange remain unresolved without live evidence.

## Pythium research response tree

Research begins with a battlefield or strategic problem and the caster already recruited. Pythium's paths offer several clean breakpoints, but a large list of reachable spells is not the same as one coherent army package.

### Branch A: Astral control and communions

Thaumaturgy 1 unlocks Communion Master and Communion Slave at S1. Thaumaturgy 2 adds Mind Burn at S2, Thaumaturgy 4 adds Paralyze at S2, and Thaumaturgy 5 adds Soul Slay at S3. Acolytes, Theurgs, and Arch Theurgs cover those fixed thresholds in different numbers, while communions can raise masters further.

This branch is selected when magic-resistance attacks, single-target control, or higher communion paths answer the enemy. It is weaker when the rear cannot be protected, slaves are too few or too fragile, fatigue is unmanaged, or the target's magic resistance makes the expected return poor.

### Branch B: Air, Water, and Astral battle support

Evocation 2 gives Lightning Bolt at A2, directly available to every Arch Theurg. Evocation 4 gives Thunder Strike at A3, requiring an Air-random Arch, communion support, or another bridge. Evocation 5 gives Stellar Cascades at S2. Alteration 3's Body Ethereal is available at S1, while Alteration 4's Quickness needs W2 and so requires a Water-random Arch, communion, or imported access.

The branch should be built around a named spell and formation. Air damage loses value against Shock Resistance, Astral effects can meet Magic Resistance or mindless targets, and short-range buffs require safe delivery. Research alone does not protect the caster or solve gem use.

### Branch C: national summons

Conjuration 5 is the first direct national threshold: fixed S3 Arch Theurgs can Contact Angel of the Host, while an imported N1 caster can Contact Lar. Conjuration 6 adds Angelic Choir and the conditional S4 Harbinger. Conjuration 7 adds Heavenly Wrath and Angelic Host. Heavenly Choir at Conjuration 9 is a separate legendary-scale commitment with an S7 F2 access problem.

Schedule each ritual from the caster and treasury backward. Pythium's Astral income supports the angel branch, but high capital mage costs, laboratory turns, and pearl stock still matter. The Nature branch needs a new gem economy as well as a legal caster.

### Branch D: Dispel and Grand Communion

Enchantment 5 gives Dispel at S3 and costs 30 Astral pearls before extra investment. A fixed Arch Theurg can cast it. The official Pythium example shows Theurgs and Acolytes joining through Grand Communion to add their Astral levels to the attempt.

This branch is a strategic answer to a specific global enchantment, not a routine use of every mage. The extra pearls, participating mage turns, concentration of valuable casters, and timing all need to be weighed against the global's actual harm.

## Pythium battlefield packages

### Legion line with Theurg support

A target-specific legion line supplies numbers and protection while Theurgs provide reachable Air, Water, Astral, and priest magic. Mundane commanders keep leadership separate from spell scripts. The package still needs a plan for armour that short swords cannot penetrate, flankers that reach the mages, and spells that hit friendly formations.

### Communion battery

Acolytes or Communicants provide slaves while Theurgs or Arch Theurgs act as masters chosen for specific path thresholds. Guards, spacing, fatigue planning, and a retreat route are part of the package. Adding more masters can multiply slave fatigue, and a master collapse can trigger backlash; size alone does not make the communion safe.

### Hydra containment group

Hydras occupy a separate pressure role with regeneration, fear on the full Hydra, head attacks, and poison. A Hydra Tamer supplies the pinned Beastmaster role. Ordinary legionnaires do not have printed Poison Resistance, so formation and separation matter. Fire damage, poison resistance, low combat speed, animal leadership, and hostile control can all reduce the group's value.

### Serpent flank and reserve

Serpent Cataphracts move and contact differently from the legions, while a Serpent Lord can lead a mounted detachment. Use them where their speed, rider profile, and mount attack solve a real positioning problem. Do not treat 19 mount protection as immunity or assume a dismounted rider retains the same battle plan.

## Pythium Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and production | Funds 300-gold Theurgs, 565-gold Arch Theurgs, forts, and resource-heavy elites | Extra income does not create capital commander turns, and extra resources do not pay mage gold. |
| Missing Nature and Earth bridge | Casts Contact Lar, starts Nature income, and can open the two national-discount items | One Pretender does not create distributed sites, spare gems, or replacement forgers. |
| Other missing-path bridge | Adds Death, Glamour, Blood, dependable Fire, or another map-specific need | A theoretical late spell is not useful without research, gems, availability, and delivery. |
| Sacred combat design | Improves Battle Vestals and sacred mage-priests | Most legionnaires, Serpent Cataphracts, and hydras receive no bless. |
| Resistance and communion safety | Helps sacred participants survive shock, poison, magic-resistance attacks, or fatigue pressure | A bless cannot fix poor slave ratios, exposed masters, bad scripts, or mundane troop losses. |
| Awake expander | Supplies early independent-taking power and preserves legion recruitment | Afflictions, counters, delayed scales, and an unavailable god can erase the early gain. |
| Astral ritual specialist | Strengthens globals, Dispel plans, and high Astral access | Pythium already has deep Astral; the design must justify what extra Astral solves. |

Pythium often gains more from a missing bridge or economy plan than from repeating fixed S3 access. A Pretender path should have a first search target, first ritual or item, gem source, and backup plan. The Order +1 limit is useful only if the complete scale and awakening design benefits from it.

## Pythium matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed ordinary infantry | Legion depth, javelins, standards, buffs, and area magic | Paying elite prices everywhere when cheaper bodies hold the required ground. |
| Heavy armour | Higher-damage weapons, Astral control, Air magic, summons, buffs, and target-specific counters | Assuming more short swords will solve protection they cannot penetrate. |
| High Defence, ethereal, or Glamour targets | Area effects, attack support, magic weapons, Astral tools, and imported counters | Relying on one expensive melee wing to make clean contact. |
| High Magic Resistance or mindless units | Physical pressure, Air damage, buffs, summons, and non-MR effects | Building the whole battle around Mind Burn, Paralyze, or Soul Slay. |
| Shock-resistant armies | Astral, Water, mundane weapons, summons, and other imported damage | Treating Air research as universal because Arch Theurgs have A2. |
| Poison-resistant, undead, or inanimate armies | Legion damage, priest magic, Astral-Air packages, and non-poison summons | Buying hydras for poison value the target largely ignores. |
| Fast flankers, flyers, and assassins | Guards, reserves, dispersed mages, protected routes, and mundane commanders | Placing every communion master and slave in one open rear cluster. |
| Giants, tramplers, and dense shock forces | Long weapons, depth, control, buffs, poison where legal, and reserve lines | Assuming formation density alone will hold a much larger contact profile. |
| Raids and dispersed pressure | Centurions, Serpent Lords, forts, scouts, local troops, and replacement Theurgs | Keeping all magical capacity and mobile forces in the capital. |
| Underwater objectives | Amphibious independents or summons, items, and a separate logistics plan | Treating W1 mages or a swimming hydra as proof of army-scale underwater access. |

## Monthly Pythium audit

- Is each fort limited by gold, resources, recruitment points, commander time, or travel distance?
- Does the legion mix answer the weapons, armour, numbers, and terrain actually reported nearby?
- Is a mundane commander available so a Theurg can keep its research or battle role?
- What is the capital commander queue buying this month, and why is it more urgent than the alternative?
- Are Communicants, Hydras, and other capital troops competing for a planned share of the troop queue?
- Has every Arch Theurg been labelled by its final displayed paths?
- Does each communion have named masters, slaves, path thresholds, guards, fatigue limits, and a retreat plan?
- Are Grand Communion helpers giving up turns for a ritual worth that cost?
- Does the current research target have a legal caster and a force that can use it?
- Are Air, Water, Astral, and Nature treasuries being treated as separate economies?
- Are hydras kept with appropriate leadership and away from unsupported poison-vulnerable troops?
- Can forts outside the capital replace Theurgs if the main army or capital is threatened?

## Pythium unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for each legion mix, Serpent Cataphracts, Battle Vestals, and hydras;
2. live 6.36 confirmation of the Arch Theurg's pinned 10% second random, which the manual does not display;
3. the current unit-card display and automatic battle behaviour of the Communicant's pinned Communion Slave field;
4. exact Hydra and Hydra Hatchling poison-cloud spread, friendly exposure, head-loss thresholds, regeneration, and recovery sequence;
5. current Single Battle departure timing for Retiarii and Gladiators;
6. displayed Gloves of the Gladiator and Hydra Skin Armor costs after the national rebate, other modifiers, and rounding;
7. battlefield communion scripts, fatigue distribution in a particular spell sequence, slave survival, and backlash outcomes;
8. current Grand Communion participant display, ritual timing, and opportunity cost in a particular game state;
9. Serpent Cataphract and Serpent Lord rider-and-mount outcomes under specific attacks;
10. assassination, underwater access, Pretender designs, and matchup performance on a particular map.

These are evidence gaps, not invitations to guess. No runtime test or new test asset was prepared during this unit. R-047, R-058, and the wider hands-on testing queue remain parked until testing is explicitly resumed.

# Part XXII: Middle Age Eriu, Last of the Tuatha

## Eriu one-page command brief

Middle Age Eriu joins ordinary Milesian infantry to terrain-dependent Fir Bolg recruitment and a capital-only Sidhe core. Eight commanders and five troops are available from ordinary forts. Highland and mountain forts add two Fir Bolg commanders and five Fir Bolg troops, while the capital adds those Fir Bolg choices plus the Tuatha commander and sacred Daoine Sidhe.

The reliable structure is:

- ordinary forts produce the full Milesian line, Bards, Sidhe Champions, Bean Sidhe, and Sidhe Lords;
- highland and mountain forts add Fir Bolg Druids, Fir Bolg Champions, and five Fir Bolg troop profiles;
- the capital's Mound of Ancient Kings provides two Nature and three Glamour gems each month, Tuatha, and Daoine Sidhe;
- Milesian Mages guarantee A1 E1 and one random level from Fire, Air, Earth, or Nature;
- Bean Sidhe guarantee W1 N1 G1 and one random level from Air, Water, Earth, Nature, or Glamour;
- Fir Bolg Druids guarantee A1 and one random level from Water, Earth, Nature, or Glamour;
- Tuatha guarantee N2 G3 H2, one random level, and a pinned independent 10% second level from the Bean Sidhe set;
- Geas and Summon Cu Sidhe are the two active national spell records; two additional nation-restricted placeholder rows are disabled and are not counted as usable magic.

Eriu's main planning problem is geography. A fort can be an ordinary Milesian centre, a highland or mountain Fir Bolg centre, or the capital with its unique Sidhe access. Strategy should therefore be built from the actual province network instead of assuming every fort can reproduce every army.

## Eriu evidence and ruleset

This chapter covers unmodded MA Eriu on the Book I 6.36 live baseline. The revision-2 official manual controls player-facing roster values, recruitment locations, printed paths, national magic, item descriptions, and mount profiles. Identifiers, recruitment sets, capital-site fields, random masks, hero records, national restrictions, and item-rebate fields are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The official 6.01 update says Eriu's recruit in mountain and highland forts did not work and records that correction. It also contains a presentation correction for the Bean Sidhe. These statements establish the direction of the fixes, but they do not replace the current manual's explicit recruitment lists or prove a current runtime outcome.

## Eriu conversion chain

```text
Milesian capital, five monthly gems, and terrain-dependent recruits
-> target-specific expansion forces and reported highland or mountain sites
-> ordinary mage forts plus selected Fir Bolg recruitment centres
-> random-path portfolios, sacred Sidhe, and stealth-capable detachments
-> Glamour, Nature, Air, Water, Earth, and conditional Fire packages
-> dispersed pressure, summons, fortified borders, and Throne claims
```

The chain breaks when a terrain recruit is budgeted before the correct province and fort exist, when capital Tuatha are treated as a cheap answer, or when a random path is counted before a qualifying mage has actually been recruited. Eriu needs a roster ledger that distinguishes guaranteed access, random access, and location access.

## Eriu national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Luck limit +1 | A Pretender may take one more Luck scale than the normal limit. It is an option whose value depends on the complete design. |
| Standard forts | Ordinary infrastructure follows the normal fort system; terrain and capital recruitment remain separate restrictions. |
| Temples cost 300 | Temple expansion has a lower printed gold price than the usual 400, improving priest and sacred infrastructure when a temple is actually needed. |
| Highland and mountain recruitment | Fir Bolg commanders and troops require the named terrain and a fort, except that the same roster is also available in the capital. |
| Capital glamour mound | The Mound of Ancient Kings produces N2 G3 each month and enables Tuatha and Daoine Sidhe. |
| Spell Singer roster | Bards, Sidhe Champions, Bean Sidhe, Sidhe Lords, and Tuatha have the printed Spell Singer ability. Exact chorus outcomes are left to current rules and battle states. |
| Glamour sacreds | Daoine Sidhe and the elite Sidhe commanders combine sacred status with Glamour. The ability does not make them immune to detection or all forms of damage. |
| Mixed mounts | Sidhe Lords and Tuatha ride Fay Horses; Fir Bolg Charioteers use Chariots. Rider and mount have separate printed profiles. |

## Eriu capital sites and recruitment geography

| Site or location | Verified fields | Recruitment consequence |
| --- | --- | --- |
| Mound of Ancient Kings, site 135 | Two Nature and three Glamour gems per month | Enables Tuatha and Daoine Sidhe in the capital |
| Fir Bolg Highlands, site 225 | No gem income recorded | Enables the Fir Bolg roster in the capital |
| Highland or mountain fort | Nation recruitment attributes 690 and 691 | Enables five Fir Bolg troops, Fir Bolg Champion, and Fir Bolg Druid |
| Other fort | Ordinary fort tables | Enables eight ordinary commanders and five Milesian troops |

The five capital gems do not pay troop gold or prove a caster for every Nature or Glamour threshold. Likewise, finding a mountain does not create Fir Bolg recruitment until the fort is complete. Recruitment geography should be recorded before construction begins.

## Complete Eriu commander membership

| ID | Commander | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 1789 | Milesian Scout | 35 | 4 | 1 | Forts |
| 1783 | Milesian Champion | 55 | 22 | 1 | Forts |
| 1784 | Milesian Monk | 45 | 1 | 1 | Forts |
| 2425 | Bard | 105 | 5 | 2 | Forts |
| 3887 | Milesian Mage | 160 | 1 | 2 | Forts |
| 850 | Sidhe Champion | 225 | 19 | 2 | Forts |
| 1774 | Bean Sidhe | 285 | 1 | 2 | Forts |
| 848 | Sidhe Lord | 375 | 16 | 2 | Forts |
| 1788 | Fir Bolg Champion | 70 | 12 | 1 | Capital, highland forts, and mountain forts |
| 2469 | Fir Bolg Druid | 95 | 2 | 2 | Capital, highland forts, and mountain forts |
| 856 | Tuatha | 630 | 22 | 4 | Capital only |

The eight ordinary records, two terrain commanders, and one capital commander reconcile to eleven distinct commanders. The manual, the fort table, the terrain attributes, and both capital sites agree on those membership classes.

## Complete Eriu troop membership

| ID | Troop | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 1779 | Milesian Slinger | 7 | 2 | 4 | Forts |
| 1780 | Milesian Spearman | 10 | 9 | 11 | Forts |
| 1781 | Milesian Longspear | 10 | 13 | 11 | Forts |
| 1782 | Milesian Swordsman | 10 | 18 | 11 | Forts |
| 3631 | Milesian Man at Arms | 14 | 24 | 20 | Forts |
| 1785 | Fir Bolg Slinger | 12 | 2 | 14 | Capital, highland forts, and mountain forts |
| 1786 | Fir Bolg Clan Warrior, axe | 15 | 10 | 18 | Capital, highland forts, and mountain forts |
| 1787 | Fir Bolg Clan Warrior, spear and javelin | 15 | 10 | 18 | Capital, highland forts, and mountain forts |
| 3630 | Fir Bolg Cattle Raider | 19 | 9 | 25 | Capital, highland forts, and mountain forts |
| 3634 | Fir Bolg Charioteer | 35 | 12 | 23 | Capital, highland forts, and mountain forts |
| 849 | Daoine Sidhe | 35 | 12 | 23 | Capital only |

The five ordinary records, five terrain records, and one capital record reconcile to eleven distinct troops. The two Clan Warriors share a name but have different object identifiers, weapons, and Defence values; they are preserved as separate profiles.

## Complete Eriu roster by job

| Unit or group | Best source-backed role | Important limit |
| --- | --- | --- |
| Milesian Slingers | Cheapest missile and siege bodies | Morale 7 and weak melee values require leadership and protection. |
| Milesian Spearmen and Longspears | Affordable line and longer-weapon frontage | Ordinary human statistics and moderate protection demand a target-specific formation. |
| Milesian Swordsmen and Men at Arms | Shielded, more protected line | Resources and recruitment points rise while damage remains that of human weapons. |
| Fir Bolg Slingers | Stronger stealth-capable slingers | Need capital or the correct fortified terrain. |
| Fir Bolg Clan Warriors | Axe damage or spear-and-javelin flexibility | Fifteen gold and restricted recruitment; choose the actual weapon need. |
| Fir Bolg Cattle Raiders | Higher-hit-point berserk shock infantry | Berserk and low protection can increase losses after contact. |
| Fir Bolg Charioteers | Mobile mounted pressure | Chariot and rider outcomes are separate and Trample is not a universal answer. |
| Daoine Sidhe | Capital sacred with Glamour and Spell Singer | Thirty-five gold, capital queue pressure, and limited protection make casualty control important. |

## Eriu commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Milesian Scout | Forest and mountain survival, Stealth 50 | Intelligence and route checking | Does not lead the field army. |
| Milesian Champion | Leadership 75 | Ordinary troop command | Twenty-two resources compete with troop production. |
| Milesian Monk | H1, sacred | Preaching and inexpensive priest work | Leadership 10 and no non-Holy path. |
| Bard | G1, Spy, Spell Singer, Stealth 50 | Intelligence, research, and low Glamour work | Two recruitment points for a single-path mage. |
| Milesian Mage | A1 E1 plus F/A/E/N random | Main affordable path-diversity recruit | A particular random cannot be scheduled as guaranteed. |
| Sidhe Champion | N1 G1 H1, Glamour, sacred | Combat command, priest work, and magic support | Expensive for a one-level non-Holy path pair. |
| Bean Sidhe | W1 N1 G1 plus A/W/E/N/G random | Broad support, research, and random-path portfolio | No Fire random and no guaranteed level two outside fixed totals. |
| Sidhe Lord | N1 G2 H2, mounted, Glamour | High leadership, priest work, and fixed G2 | High gold cost and separate Fay Horse profile. |
| Fir Bolg Champion | Leadership 75, Berserker 3 | Terrain-force command | Not available from an ordinary non-terrain fort. |
| Fir Bolg Druid | A1 plus W/E/N/G random | Cheap terrain mage and path portfolio | Requires capital or a highland or mountain fort. |
| Tuatha | N2 G3 H2 plus A/W/E/N/G randoms | Highest native Glamour, ritual work, command, and priest duties | Capital only, 630 gold, and four recruitment points. |

## Reading the Milesian Mage random paths

The manual prints A1 E1 and one random level. The pinned mask `9600` decodes as Fire, Air, Earth, or Nature, with one guaranteed equally likely result.

| Final non-Holy result | Probability |
| --- | ---: |
| A1 E1 F1 | 25% |
| A2 E1 | 25% |
| A1 E2 | 25% |
| A1 E1 N1 | 25% |

This is Eriu's repeatable native Fire source. A selected result appears at least once with probability `1 - 0.75^n`: 57.81% after three Milesian Mages, 76.27% after five, and 94.37% after ten. Those figures describe a portfolio, not an arrival date.

## Reading the Bean Sidhe random paths

Bean Sidhe are fixed W1 N1 G1 and receive one guaranteed equally likely level from Air, Water, Earth, Nature, or Glamour. Mask `26368` therefore yields A1, W2, E1, N2, or G2 at 20% each.

A chosen result appears at least once with probability `1 - 0.8^n`: 48.80% after three Bean Sidhe, 67.23% after five, and 89.26% after ten. This provides broad access, but each recruit costs 285 gold and two recruitment points.

## Reading the Fir Bolg Druid random paths

Fir Bolg Druids are fixed A1 and receive one guaranteed equally likely level from Water, Earth, Nature, or Glamour. Mask `26112` therefore yields A1 W1, A1 E1, A1 N1, or A1 G1 at 25% each.

The Druid is cheaper than the ordinary Milesian Mage but is geographically restricted. Its value depends on whether a suitable fort is useful for the wider campaign, not merely whether the random mask is attractive.

## Reading the Tuatha random paths

The manual prints N2 G3 H2 and one random level. The pinned record applies the same Air, Water, Earth, Nature, or Glamour mask as the Bean Sidhe, then adds an independent 10% second roll from that mask.

| Portfolio result | Probability per Tuatha |
| --- | ---: |
| No second random level | 90% |
| Second level repeats the first path | 2% |
| Second level differs from the first | 8% |
| A chosen named path appears at least once | 21.6% |
| A chosen named path appears twice | 0.4% |

The extra slot is not exposed by the manual's single `?1` marker, so it remains pinned 6.35 planning evidence rather than a current live-display claim. The very high gold and recruitment-point cost also makes large-sample portfolio assumptions impractical.

## Eriu native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Glamour | G1 Bard, G1 Sidhe Champion, G1 Bean Sidhe, G2 Sidhe Lord, G3 Tuatha, randoms | Deep fixed access, with capital G3 and conditional higher results. |
| Nature | N1 Sidhe Champion, Bean Sidhe, and Sidhe Lord; N2 Tuatha; randoms | Fixed N1 outside the capital and fixed capital N2. |
| Air | A1 Milesian Mage and Fir Bolg Druid; randoms | Fixed A1 is repeatable; higher Air requires a random or another bridge. |
| Water | W1 Bean Sidhe; Bean and Druid randoms | Fixed W1 is repeatable; W2 is a Bean random or another bridge. |
| Earth | E1 Milesian Mage; Mage, Bean, and Druid randoms | Fixed E1 is repeatable; E2 is a Milesian Mage random or another bridge. |
| Fire | Milesian Mage random only | No fixed recruit has Fire. |
| Holy | H1 Monk and Sidhe Champion, H2 Sidhe Lord and Tuatha | H2 exists outside the capital on the Sidhe Lord. |
| Astral, Death, Blood | No repeatable recruit | Require independents, summons, empowerment, Pretender access, or another proved bridge. |

## Eriu national spell and ritual reconciliation

| ID | Name | School | Requirement | Cost | Verified access |
| ---: | --- | --- | --- | --- | --- |
| 1294 | Geas | Thaumaturgy 3 | G2 | 20 fatigue | Sidhe Lord and Tuatha qualify; Bean Sidhe qualify on a Glamour random |
| 439 | Summon Cu Sidhe | Conjuration 3 | G2 | 5 Glamour gems | Sidhe Lord and Tuatha qualify; summons ten Cu Sidhe |

Two other nation-58 restriction rows, IDs 445 and 446, are named `xxx`, use school `-1`, and are disabled in the pinned spell table. They are retained in the evidence audit as placeholders and are not presented as playable national rituals.

## Eriu national item reconciliation

| ID | Item | Construction | Paths | Verified national field |
| ---: | --- | ---: | --- | --- |
| 345 | Gossamer Cloth | 3 | G2 N1 | National rebate includes nations 11 and 58 |
| 93 | Singing Sword | 7 | G2 | National rebate includes nations 11 and 58 |

The manual describes Gossamer Cloth as veiling an army of up to 25 units and the Singing Sword as casting Entrancement. Sidhe Lords and Tuatha meet both printed path requirements. The final displayed cost after the national rebate, other modifiers, and rounding remains unresolved without a current forge screen.

## Eriu national hero records

| ID | Fixed name or class | Unit name | Verified magic or status |
| ---: | --- | --- | --- |
| 1777 | Ferdiad | Fir Bolg Hero | Mundane Leadership 100, Berserker 5 |
| 1778 | Cu Chulainn | Hero | Mounted mundane Leadership 100, Berserker 8 |
| 1794 | Tuan | Last Partholonian | A2 W1 D4 G2 H1; pinned `latehero = 10` |
| 1844 | Scathach | Trainer of Heroes | A2 D2 G2 H1, Glamour, sacred |
| 1806 | Fianna | Generic hero record | Sacred Leadership 150; no magic path recorded |

The first four are unique-hero attributes; Fianna is a generic or repeatable hero attribute. No arrival turn, frequency, or guaranteed strategic role is derived from either the hero slot or the uninterpreted `latehero` value.

## Eriu patch reconciliation

Update 6.01, published 19 January 2024, states that Eriu's recruit in mountain and highland forts did not work. The current official manual explicitly lists the Fir Bolg units and commanders available in the capital and in fortified highland or mountain provinces, while the pinned data records the same terrain sets. The chapter therefore treats the current recruitment locations as intended rules and does not invent the earlier failure mode.

The same update includes a Bean Sidhe presentation correction. It supports only that a display asset changed; it does not establish a rules or balance change. No later direct Eriu roster change was found in the official ledger through 6.36.

## Eriu opening priorities

The opening should secure ordinary troop production, leadership, scouting, and an affordable mage stream before assuming a terrain fort or repeated Tuatha. Milesian units can form the initial army while Scouts identify routes and suitable fort provinces. Exact expansion counts remain open because map generation, scales, bless, formation, opposing roster, and combat rolls change them.

A first fort has two different strategic meanings. An ordinary province expands Milesian Mages, Bean Sidhe, Sidhe Lords, and the human army. A highland or mountain adds cheap Fir Bolg Druids and the terrain troop package. The correct choice depends on distance, resources, defence, construction time, and the path portfolio already available.

## Eriu recruitment packages to evaluate from reports

### Milesian line

Spearmen and Longspears provide inexpensive frontage, while Swordsmen and Men at Arms buy more protection at higher resource and recruitment-point costs. Slingers add cheap ranged bodies. Choose the mix from the reported target rather than treating the more expensive profile as automatically superior.

### Fir Bolg terrain force

Fir Bolg offer higher hit points and magic resistance than the ordinary Milesian line, plus stealth on most profiles. Axe and spear Clan Warriors answer different targets; Cattle Raiders add berserk pressure; Charioteers add a separate mount profile. Their restricted recruitment makes replacement geography part of the plan.

### Sidhe sacred group

Daoine Sidhe and sacred commanders combine Glamour with higher defence and magic resistance. They remain limited by capital access, gold, recruitment points, and ordinary battlefield counters. A bless should solve a named problem instead of assuming Glamour replaces protection, numbers, or retreat planning.

## Eriu research response tree

### Branch A: Glamour control and national magic

Thaumaturgy 3 provides Geas at G2, while Conjuration 3 provides Summon Cu Sidhe at G2 for five Glamour gems. Sidhe Lords give fixed non-capital G2 and Tuatha give capital G3. This branch is attractive when its control effect or stealth-capable sacred summons answer the current opponent, not simply because it is national.

### Branch B: Air and Earth support

Milesian Mages always bring A1 E1 and can random higher Air or Earth. Fir Bolg Druids always bring A1. Research should be chosen around a spell that the existing mage can cast and deliver. A theoretical A2 or E2 package should stay conditional until the matching random exists.

### Branch C: Nature, Water, and sacred support

Nature is fixed across the Sidhe line and reaches N2 on Tuatha, while Bean Sidhe provide fixed W1 and conditional W2. This supports buffs, protection, recovery, and summons at different research thresholds. Gem income remains separate: the capital supplies Nature but no Water gems.

### Branch D: forging and path bridges

Construction 3 exposes the nationally discounted Gossamer Cloth and other low-level utility items; Construction 7 exposes the Singing Sword. Forging should begin from a current requirement, available caster, and gem budget. It should not consume the Glamour treasury needed for an imminent Cu Sidhe summon without an explicit trade-off.

## Eriu battlefield packages

### Human line with mage support

Milesian infantry supply replaceable frontage while Milesian Mages, Bards, and Bean Sidhe provide the selected spell package. A mundane Champion keeps troop leadership separate from mage turns. The package still needs answers to armour, high defence, missiles, fatigue, and rear attacks.

### Fir Bolg stealth detachment

A terrain fort can combine stealth-capable Fir Bolg troops with a Champion or Druid. This can create a distinct movement and information package, but exact stealth discovery, interception, and battle outcomes remain dependent on current rules and game state.

### Sidhe sacred pressure

Daoine Sidhe, Sidhe Champions, Sidhe Lords, and Tuatha can combine sacred status, Glamour, and Spell Singer access. Their gold and capital constraints make concentration expensive. The force should have a clear target, retreat line, and replacement plan.

## Eriu Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and production | Funds forts, 285-gold Bean Sidhe, 375-gold Sidhe Lords, and 630-gold Tuatha | Income does not create commander turns or suitable terrain. |
| Missing Astral, Death, or Blood bridge | Opens searches, rituals, or counters absent from repeatable recruits | A path without research, gems, and delivery is not a working bridge. |
| Sacred combat design | Improves Daoine Sidhe and sacred commanders | Most Milesian and Fir Bolg troops receive no bless. |
| Resistance design | Protects sacreds against a reported damage or control class | One resistance does not solve mundane attrition, fatigue, or positioning. |
| Awake expander | Supplies early independent-taking power while preserving troop recruitment | Afflictions, counters, and delayed economy can erase the advantage. |
| Luck-oriented design | Uses Eriu's Luck +1 legal limit | The extra point must justify its opportunity cost within the full scale design. |

## Eriu matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light troops | Longer weapons, missiles, formation depth, buffs, and area magic | Spending capital sacreds on work ordinary lines can perform. |
| Heavy armour | Axes, buffs, magic, summons, and target-specific counters | Assuming more low-damage human attacks will penetrate. |
| High Defence or Glamour | Area effects, attack support, magic weapons, and control | Treating Eriu's own high Defence as proof it counters the same mechanic. |
| High Magic Resistance | Physical pressure, buffs, and non-MR effects | Building the battle solely around Geas or other resistance checks. |
| Fire pressure | Appropriate resistance, spacing, and nonflammable or expendable layers | Concentrating expensive sacreds without a tested answer. |
| Fast flankers or flyers | Guards, reserves, dispersed mages, and protected routes | Leaving costly Spell Singers in an open rear cluster. |
| Raids and dispersed pressure | Scouts, Bards, local forts, terrain recruits, and replacement commanders | Keeping every important mage and sacred in the capital. |
| Underwater objectives | Amphibious independents, summons, items, and a separate logistics plan | Treating W1 Bean Sidhe as army-scale underwater access. |

## Monthly Eriu audit

- Which forts are ordinary, highland, mountain, or capital recruitment centres?
- Is each queue limited by gold, resources, recruitment points, terrain, or travel distance?
- Does the current troop mix answer the reported weapons, protection, numbers, and terrain?
- Has every random mage been labelled by final displayed paths before receiving a job?
- Is Fire being treated as conditional rather than guaranteed?
- Are capital commander turns being spent on Tuatha only when G3, N2, H2, or high leadership is required?
- Are Nature and Glamour income budgeted separately from Air, Water, Earth, and Fire needs?
- Does each research target have a legal caster, treasury, force, and delivery route?
- Are sacred and stealth forces assigned a retreat and replacement plan?
- Is a new fort being placed for its actual ordinary or terrain roster?

## Eriu unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for Milesian, Fir Bolg, and Daoine Sidhe forces;
2. live 6.36 confirmation of the Tuatha's pinned 10% second random, which the manual does not display;
3. current terrain-recruit interface and any edge case left by the old 6.01 bug;
4. displayed Singing Sword and Gossamer Cloth costs after national rebates, other modifiers, and rounding;
5. exact Geas targeting and resistance outcomes in a particular battle;
6. Spell Singer timing, chorus composition, fatigue, interruption, and survival outcomes;
7. Glamour, stealth, and detection interactions already parked under R-058;
8. rider, Fay Horse, Chariot, and dismount outcomes under specific attacks;
9. hero arrival timing, generic Fianna frequency, and the meaning of Tuan's pinned late-hero value;
10. specific Pretender designs, scripts, and matchup performance on a generated map.

These are evidence gaps, not invitations to guess. No runtime test or new test asset was prepared during this unit. R-047, R-058, and the wider hands-on testing queue remain parked until testing is explicitly resumed.

# Part XXIII: Middle Age Agartha, Golem Cult

## Agartha one-page command brief

Middle Age Agartha combines protected human infantry with Pale One cave recruits, capital sacred giants, underwater recruitment, and an Earth-led priest-mage corps. Seven commanders and seven troops appear in the ordinary fort tables. The capital adds two commanders and three sacred troops through three national sites, while underwater forts add a Wet One Captain and an armoured Wet One profile.

The reliable structure is:

- ordinary forts recruit the human infantry line, Pale and Wet Ones, Troglodyte Slaves, and all repeatable non-capital mages;
- every cave province can recruit Pale One Captains, Pale One Soldiers, and the lightly armoured Wet One even without a fort;
- cave forts receive extra gold and resources, although the official nation page gives no arithmetic for the increase;
- Golem Crafters guarantee F1 W1 E2 H1 and qualify for the early Fire, Water, and Earth national rituals;
- capital Oracles guarantee E3 D1 H3, one full W/E/D random, and a pinned independent 10% second W/E/D random;
- the capital produces F1 E3 D1 each month and supplies Ancient Ones, Ancient Stone Hurlers, Shard Guards, Ancient Lords, and Oracles;
- twelve national rituals form summon ladders for magma, elementals, olms, living statues, mercury, shadow beings, and undead Pale Ones;
- the manual states that constructs gain Hit Points inside Agartha's dominion, but exact candle scaling and affected ownership classes remain unresolved.

Agartha's central planning problem is conversion. Slow, well-protected troops and deep Earth access become strategically valuable only when the nation also budgets commander turns, research, mixed gem types, cave infrastructure, and movement to the target.

## Agartha evidence and ruleset

This chapter covers unmodded MA Agartha on the Book I 6.36 live baseline. The revision-2 official manual controls player-facing roster values, explicit recruitment locations, printed paths, national rules, capital-site output, and national ritual tables. Identifiers, membership sets, site fields, random masks, hero records, and nation restrictions are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

Official update 6.04, published 2 February 2024, includes a short Lich-shape correction for Agarthan Oracles. The note establishes that an Oracle transformation record was corrected, but it does not supply the resulting form, trigger, or present-game sequence. Those details are not reconstructed from the headline.

## Agartha conversion chain

```text
protected infantry, cave access, and five monthly gems
-> target-specific expansion groups and surveyed cave routes
-> ordinary mage forts plus protected capital recruitment
-> Earth-led research and separate Fire, Water, Earth, and Death budgets
-> elementals, olms, statues, shadows, undead, and battlefield support
-> durable fronts, cave logistics, sieges, and Throne claims
```

The chain breaks when the capital queue is treated as unlimited, when slow troops are sent on a deadline they cannot meet, when a national ritual is counted without its gem type, or when an Oracle random is assumed before the commander exists.

## Agartha national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Humans and Pale Ones | The roster contains different size, movement, amphibious, leadership, and equipment profiles; one formation does not fit all of them. |
| Darkvision | Agarthan profiles carry substantial Darkvision, which is relevant underground and in darkness but does not remove other combat penalties or targeting limits. |
| Cave recruitment | Pale One Captains, Pale One Soldiers, and the light Wet One profile are available in all caves as well as forts. |
| Cave-fort economy | The nation page promises extra gold and resources in cave forts; the exact increase is not printed there and remains an arithmetic boundary. |
| Poor amphibians and amphibians | Several Pale One and construct profiles can enter water with different limitations; army-scale underwater readiness still depends on the complete force. |
| Golem Cult | Constructs receive increased Hit Points inside friendly dominion according to the nation page. Exact scaling and ownership coverage remain unresolved. |
| Bless points +1 | The Pretender design receives one additional bless point. It does not by itself choose a useful bless. |
| Standard forts | Ordinary fort construction follows the standard system, with the separate cave-fort economy rule layered on top. |

## Agartha capital sites and recruitment geography

| Site or location | Verified fields | Recruitment consequence |
| --- | --- | --- |
| Roots of the Earth, site 110 | One Fire and three Earth gems per month | Supplies most of the capital's gem income |
| Halls of the Oracles, site 111 | No gem income recorded | Enables Ancient Lord, Oracle of the Ancients, Ancient One, and Ancient Stone Hurler |
| The Chamber of the Broken Seal, site 166 | One Death gem per month | Enables Shard Guard |
| Any cave | Nation cave-recruit attributes | Enables Pale One Captain, Pale One Soldier, and the light Wet One profile |
| Underwater fort | Underwater recruitment attributes | Enables Wet One Captain and the armoured Wet One profile |

The capital therefore produces five gems each month: F1 E3 D1. It produces no Water gems even though Golem Crafters have W1 and Olm Conclave and Living Mercury require Water gems. A legal caster and a funded ritual are separate claims.

## Complete Agartha commander membership

| ID | Commander | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 1448 | Agarthan Scout | 35 | 4 | 1 | Forts |
| 2483 | Troglodyte Trainer | 60 | 15 | 1 | Forts |
| 1471 | Pale One Captain | 65 | 18 | 1 | Forts and all caves |
| 1445 | Cave Captain | 95 | 22 | 1 | Forts |
| 1475 | Attendant of the Oracles | 65 | 1 | 1 | Forts |
| 1473 | Earth Reader | 115 | 1 | 2 | Forts |
| 1474 | Golem Crafter | 295 | 2 | 2 | Forts |
| 2506 | Ancient Lord | 175 | 23 | 1 | Capital only |
| 1459 | Oracle of the Ancients | 540 | 1 | 4 | Capital only |
| 1638 | Wet One Captain | 50 | 6 | 1 | Underwater forts |

The seven ordinary records, two capital records, and one underwater record reconcile to ten distinct commanders. The Pale One Captain is both an ordinary fort commander and a cave recruit, so it is counted once.

## Complete Agartha troop membership

| ID | Troop | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 1472 | Pale One Soldier | 9 | 14 | 18 | Forts and all caves |
| 1489 | Wet One, light | 9 | 1 | 18 | Forts and all caves |
| 1354 | Agarthan Heavy Infantry | 10 | 27 | 9 | Forts |
| 1355 | Agarthan Infantry | 10 | 22 | 9 | Forts |
| 1447 | Agarthan Light Infantry | 10 | 10 | 9 | Forts |
| 2507 | Defender of the Halls | 13 | 23 | 26 | Forts |
| 2482 | Troglodyte Slave | 50 | 1 | 40 | Forts |
| 2188 | Ancient One | 40 | 27 | 32 | Capital only |
| 2189 | Ancient Stone Hurler | 40 | 13 | 32 | Capital only |
| 2508 | Shard Guard | 45 | 34 | 30 | Capital only |
| 1636 | Wet One, armoured | 9 | 5 | 18 | Underwater forts |

The seven ordinary records, three capital records, and one underwater record reconcile to eleven distinct troops. The two Wet One rows retain separate identifiers, equipment, protection, combat values, and recruitment channels.

## Complete Agartha roster by job

| Unit or group | Best source-backed role | Important limit |
| --- | --- | --- |
| Agarthan infantry | Protected human frontage at three resource levels | Slow map and combat movement make route and formation planning important. |
| Pale One Soldier | Large amphibious cave recruit with siege strength | Low Attack and Defence require support and target selection. |
| Wet Ones | Cheap amphibious bodies from cave or underwater channels | The light and armoured profiles are not interchangeable. |
| Defender of the Halls | Larger, shielded poor-amphibian line | High recruitment-point and resource costs limit massing. |
| Troglodyte Slave | Large trampling shock unit | High gold, recruitment-point cost, low Magic Resistance, and friendly positioning risks constrain use. |
| Ancient One | Capital sacred heavy infantry | Capital access, 40 gold, 27 resources, and 32 recruitment points make losses costly. |
| Ancient Stone Hurler | Capital sacred boulder thrower and siege body | Low Defence and limited capital production require protection. |
| Shard Guard | Capital sacred glaive unit with poison resistance | Highest resource cost in the roster and slow movement restrict replacement and delivery. |

## Agartha commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Agarthan Scout | Stealth 50, forest and mountain survival | Intelligence and route checking | Does not lead the field army. |
| Troglodyte Trainer | Taskmaster +2, Leadership 20 | Directing slave formations | Limited leadership and no magic path. |
| Pale One Captain | Leadership 75, amphibious, siege strength +5 | Cave and amphibious force command | Slow movement and 18 resources. |
| Cave Captain | Leadership 100 | Human army command | Twenty-two resources compete with infantry. |
| Attendant of the Oracles | H1 | Inexpensive priest work | Leadership 10 and no non-Holy path. |
| Earth Reader | E1 H1, Fortune Teller 5 | Research, low Earth, preaching, event support | Two recruitment points for a shallow mage. |
| Golem Crafter | F1 W1 E2 H1 | Main repeatable mage, early national rituals, forging | 295 gold and two recruitment points. |
| Ancient Lord | Sacred Leadership 100 | Capital sacred command and siege leadership | Capital commander turn with no magic path. |
| Oracle of the Ancients | E3 D1 H3 plus W/E/D randoms | Deep Earth, Death, high priest work, national rituals | 540 gold, four recruitment points, and capital only. |
| Wet One Captain | Amphibious Leadership 75 | Underwater recruitment command | Underwater fort only and no magic path. |

## Reading the Oracle random paths

The manual prints E3 D1 H3 and `?1`. The pinned record uses mask `5760`, which decodes as Water, Earth, or Death. It gives one guaranteed equally likely level and an independent 10% second roll from the same three paths.

| Primary result | Probability | Final paths before the second roll |
| --- | ---: | --- |
| Water | 33.33% | W1 E3 D1 H3 |
| Earth | 33.33% | E4 D1 H3 |
| Death | 33.33% | E3 D2 H3 |

The second slot produces no extra level 90% of the time, repeats the primary path 3.33% of the time overall, and adds a different path 6.67% of the time overall. A chosen named path appears in at least one slot with probability 35.56%; two levels in that chosen path occur with probability 1.11%.

The manual exposes only one random marker, so the second slot remains pinned 6.35 planning evidence rather than a current live-display claim.

## Agartha native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Earth | E1 Earth Reader, E2 Golem Crafter, E3 Oracle, Oracle randoms | Deep fixed access; E5 without equipment is a rare double-Earth Oracle result. |
| Fire | F1 Golem Crafter | Fixed F1 qualifies for Rhuax Pact; higher Fire requires a bridge. |
| Water | W1 Golem Crafter, Oracle random | Fixed W1 exists but the capital supplies no Water gems. |
| Death | D1 Oracle, Oracle random | D2 requires a qualifying Oracle random or another bridge. |
| Holy | H1 Attendant, Earth Reader, and Golem Crafter; H3 Oracle | The capital has repeatable H3 but at high cost and queue pressure. |
| Air, Astral, Nature, Glamour, Blood | No repeatable recruit | Require independents, summons, empowerment, Pretender access, or another proved bridge. |

Olm Conclave can add an Olm Sage with W2 E1, but a summoned commander is not starting access. It requires Conjuration 4, W1 E1, twenty Water gems, and a ritual turn.

## Agartha national ritual reconciliation

| ID | Ritual | School | Requirement | Cost | Printed result |
| ---: | --- | --- | --- | --- | --- |
| 608 | Rhuax Pact | Conjuration 3 | F1 E1 | 2 Fire gems | 3 Magma Children |
| 609 | Barathrus Pact | Conjuration 3 | E2 | 3 Earth gems | 2 Earth Elementals |
| 603 | Olm Conclave | Conjuration 4 | W1 E1 | 20 Water gems | 1 Olm Sage and 15 Great Olms |
| 616 | Living Mercury | Enchantment 5 | W1 E1 | 6 Water gems | 1 Living Mercury |
| 611 | Attentive Statues | Enchantment 1 | E2 | 3 Earth gems | 2 Attentive Statues |
| 612 | Enliven Sentinel | Enchantment 3 | E2 | 2 Earth gems | 1 Sentinel |
| 613 | Enliven Granite Guard | Enchantment 5 | E3 | 10 Earth gems | 1 Granite Guardian |
| 614 | Enliven Marble Oracle | Enchantment 6 | E3 D1 | 35 Earth gems | 1 H2 Marble Oracle |
| 604 | Hall of Statues | Enchantment 8 | E5 | 30 Earth gems | 20 or more Sentinels |
| 601 | Summon Penumbrals | Conjuration 3 | D1 E1 | 6 Death gems | 6 Penumbrals |
| 622 | Awaken Shard Wights | Conjuration 3 | D1 E1 | 10 Death gems | 5 or more Shard Wights |
| 602 | Summon Umbrals | Conjuration 5 | D2 E1 | 8 Death gems | 6 Umbrals |

The current manual controls the counts shown here. `20+` and `5+` are deliberately retained as variable results; no extra-path scaling formula is invented. The pinned nation restrictions confirm all twelve rows for nation 59.

## Agartha ritual access from repeatable mages

Golem Crafters directly qualify for Rhuax Pact, Barathrus Pact, Olm Conclave, Living Mercury, Attentive Statues, and Enliven Sentinel. Every Oracle directly qualifies for Enliven Granite Guard, Enliven Marble Oracle, Summon Penumbrals, and Awaken Shard Wights.

Summon Umbrals requires D2, so it needs an Oracle with at least one Death random or another proved Death bridge. Hall of Statues requires E5. Without equipment, only the 1.11% Oracle result with Earth in both random slots reaches E5. With an Earth booster, any Oracle with Earth in at least one random slot reaches the printed threshold; that portfolio probability is 35.56%, subject to the booster, research, gems, and forge turn actually existing.

## Agartha capital and ritual gem economy

The capital's F1 E3 D1 income aligns well with Rhuax Pact, the statue line, Penumbrals, and Shard Wights. It does not fund Water rituals by itself. Earth gems also compete among battlefield use, boosters, construction, Barathrus Pact, statues, and late Hall of Statues. Death gems compete among both shadow and undead summon lines.

A ritual plan should record four separate facts:

1. the caster's current displayed paths;
2. the research level and school;
3. the available gem type and amount;
4. the army, commander, and route that will use the result.

## Agartha national hero records

| ID | Fixed name | Unit name | Verified magic or status |
| ---: | --- | --- | --- |
| 1846 | Kin-Breaker | Onyx Oracle | W1 E3 H3; inanimate stone magic being; pinned late-hero field 20 |
| 1847 | Golog | Decrepit | E3 D4 H1; pinned transformation fields and late-hero field 10 |
| 1848 | Klaus | Mason of the Underworld | F1 W1 E2 D3 H1; Mason, forge bonus 1, Stealth 80, Spy |

The three unique-hero attributes identify a powerful but non-repeatable path expansion. The late-hero and transformation fields are recorded as structured metadata only; no arrival turn, probability, death sequence, or Lich outcome is inferred.

## Agartha patch reconciliation

Update 6.04 records a Lich-shape correction for Agarthan Oracles. The note is relevant to Oracle transformations but contains no numerical detail and does not identify a current roster or path change. It is therefore preserved as patch metadata and an unresolved transformation boundary.

No later direct nation, roster, or national-ritual name match was found in the official ledger through 6.36. This is a ledger result, not proof that no undocumented engine behaviour changed.

## Agartha opening priorities

The opening should secure leadership, scouting, protected frontage, and an affordable research stream before assuming repeated 540-gold Oracles. Human infantry offer resource-scaled protection choices; Pale Ones and Wet Ones widen cave access; Troglodyte Slaves supply a costly trampling option. Exact expansion counts remain open because map generation, scales, bless, formation, opposing roster, and combat rolls change them.

A cave fort can combine ordinary national recruitment with the printed cave economy benefit, but its value still depends on province income, resources, position, construction time, and exposure. The manual does not provide the exact extra-income formula on the nation page, so the chapter does not assign one.

## Agartha recruitment packages to evaluate from reports

### Protected human line

Light, standard, and heavy Agarthan infantry trade resources and encumbrance for protection. Select the profile that survives the reported weapons without delaying the rest of the queue. Cave Captains keep troop command separate from mage turns.

### Pale One cave group

Pale One Soldiers and Captains add larger bodies, amphibious movement, and siege strength from any cave. Their lower Attack, Defence, Precision, and movement need formation and support. Cave availability does not eliminate the need to pay gold, resources, recruitment points, and travel time.

### Capital sacred group

Ancient Ones, Ancient Stone Hurlers, and Shard Guards give the capital three distinct sacred profiles. Their high recruitment-point and resource costs make mixed production and casualty control important. The extra bless point should solve a named weakness rather than merely encourage sacred concentration.

### Troglodyte shock group

Troglodyte Slaves provide size, strength, and Trample. A Trainer supplies Taskmaster support. The package still needs a formation that protects friendly troops and a target whose size and resistance make the cost worthwhile.

## Agartha research response tree

### Branch A: early Conjuration

Conjuration 3 opens Rhuax Pact, Barathrus Pact, Summon Penumbrals, and Awaken Shard Wights. Golem Crafters cover the Fire and Earth pair; Oracles cover the Death pair. The correct first summon depends on available gems and the enemy rather than national status alone.

### Branch B: Enchantment constructs

Enchantment 1 and 3 open the cheapest statue rituals, while levels 5, 6, and 8 add Living Mercury, Granite Guardians, Marble Oracles, and Hall of Statues. The branch converts Earth and Water gems into durable units, but movement, magic leadership, poison fumes, and repair or healing rules differ by summon.

### Branch C: Earth battlefield support

Earth Readers, Golem Crafters, and Oracles provide a fixed E1-E3 ladder before randoms or boosters. Research should be chosen around the protection, control, fatigue, or damage problem actually reported. Deep paths do not make a slow army arrive sooner.

### Branch D: construction and boosters

Construction can turn repeatable E2 into Earth equipment and widen the Oracle's ritual ceiling. Every booster consumes gems and a mage turn and should be tied to a named threshold, especially Hall of Statues or another high-Earth objective.

## Agartha battlefield packages

### Protected line with Crafter support

Human infantry provide the line while Golem Crafters supply selected Fire, Water, and Earth magic. A Cave Captain handles command. The package needs a deliberate answer to fatigue, armour-piercing damage, flanks, and rear attacks.

### Mixed Pale One and statue force

Pale Ones add amphibious bodies and siege strength; summoned statues add inanimate protection and patrol ability. Leadership, magic leadership, movement, and repair assumptions must be checked for every component rather than inferred from the word construct.

### Oracle-led capital force

An Oracle can combine H3, E3, D1, random paths, and sacred leadership support around the capital roster. The commander is expensive and slow to recruit, so battle exposure, scripting, and replacement cost should be explicit.

## Agartha Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and production | Funds 295-gold Crafters, 540-gold Oracles, forts, and resource-heavy sacreds | Income does not create capital commander turns or movement. |
| Missing Air, Astral, Nature, Glamour, or Blood bridge | Opens searches, rituals, or counters absent from repeatable recruits | A path without gems, research, and delivery is not a working bridge. |
| Water-income bridge | Funds Olm Conclave and Living Mercury from native casters | Water paths alone do not create Water gems. |
| Sacred combat design | Uses the extra bless point on Ancient Ones, Stone Hurlers, Shard Guards, and sacred summons | Most human troops, Wet Ones, and Troglodyte Slaves receive no bless. |
| Construct-oriented design | Supports a statue and summoned-construct plan | Exact Golem Cult scaling and ownership remain unresolved, and enemies may bring construct counters. |
| Awake expander | Supplies early independent-taking power while preserving troop recruitment | Afflictions, counters, and delayed scales can erase the early gain. |

## Agartha matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light infantry | Protected lines, trampling where legal, Magma Children, and area magic | Paying capital-sacred prices for work ordinary troops can perform. |
| Heavy armour | High-strength Pale Ones, Earth support, elementals, fatigue, and target-specific magic | Assuming ordinary short swords will solve high protection. |
| Armour-piercing or armour-negating damage | Spacing, resistance, summons, disruption, and a different line profile | Treating high mundane protection as universal defence. |
| High Defence, ethereal, or Glamour targets | Area effects, magic weapons, attack support, Spirit Sight summons, and control | Assuming Darkvision or large size answers unrelated mechanics. |
| High Magic Resistance or mindless units | Physical pressure, elementals, buffs, and non-MR effects | Building the battle around one resistance check. |
| Fast flankers and flyers | Guards, reserves, dispersed mages, and protected routes | Leaving expensive Crafters and Oracles in an open rear cluster. |
| Raids and dispersed pressure | Scouts, forts, local cave recruits, and replacement commanders | Keeping every useful commander and mage in the capital. |
| Underwater objectives | Wet One recruitment, amphibious troops, appropriate commanders, and a separate logistics plan | Treating a few amphibious profiles as a complete underwater army. |

## Monthly Agartha audit

- Is each fort limited by gold, resources, recruitment points, commander time, terrain, or travel distance?
- Has every cave and underwater recruitment channel been labelled separately?
- Does the troop mix answer the reported weapons, protection, numbers, size, and terrain?
- Is a mundane commander available so a Crafter or Oracle can keep its research or battle role?
- Has every Oracle been labelled by its final displayed paths before receiving a ritual job?
- Are Fire, Water, Earth, and Death treasuries being treated as separate economies?
- Does each national ritual have a legal caster, research level, gem budget, commander, and delivery route?
- Are capital sacreds competing for a planned share of resources and recruitment points?
- Is the cave-fort decision based on the province and route rather than an unverified income formula?
- Are summoned constructs assigned adequate magic leadership and movement support?

## Agartha unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for human infantry, Pale Ones, Troglodyte Slaves, and capital sacreds;
2. live 6.36 confirmation and display of the Oracle's pinned 10% second random;
3. exact cave-fort gold and resource arithmetic across province and scale states;
4. exact Golem Cult Hit Point scaling, candle relationship, and affected ownership classes;
5. current underwater movement, combat, supply, and retreat outcomes for mixed amphibious forces;
6. the variable scaling behind Hall of Statues and Awaken Shard Wights beyond their printed minimums;
7. repair, healing, poison-fume, leadership, and battlefield behaviour of particular summoned constructs;
8. Oracle transformation and Lich-shape outcomes referenced by the 6.04 correction;
9. hero arrival timing and the meaning of the pinned late-hero values;
10. specific Pretender designs, scripts, and matchup performance on a generated map.

These are evidence gaps, not invitations to guess. No runtime test or new test asset was prepared during this unit. R-047, R-058, and the wider hands-on testing queue remain parked until testing is explicitly resumed.

# Part XXIV: Middle Age Uruk, City States

## Uruk one-page command brief

Middle Age Uruk fields large Enkidu infantry, strong priests, a broad but uneven mage corps, capital sacreds and Mushussu chariots, province recruits, and a complete underwater recruitment branch. Ten commanders and six troops appear in the ordinary fort tables. The capital adds two commanders and two troops, non-fort provinces add an Enkidu Shaman and Enkidu Warrior, and underwater forts add four commanders and two troops.

The reliable structure is:

- ordinary forts recruit the armoured Enkidu line and ten commanders ranging from scouts and leaders to priests and mages;
- every non-fort province can recruit an E1 N2 Enkidu Shaman and an Enkidu Warrior, allowing useful recruitment outside the fort network;
- the capital adds Entu and Mashmashu, sacred Maidens of the Moon, and a maximum of one Mushussu Charioteer each month;
- underwater forts add Kulullu troops, commanders, priests, and mages instead of merely extending the land roster;
- the capital produces W1 E1 S2 N1 each month through three national sites;
- fixed recruitable paths cover Water, Earth, Astral, Nature, and Holy, while Air is random and Fire is absent from the recruitable mage roster;
- six national rituals offer Buffaloes, Kusarikkus, Ugallu, Anzus, a Scorpion Man, and an Umu-apkallu, but only the first two have immediate fixed-path access;
- five national item records include a Nature crown and four late Earth-Astral pieces, although national ownership does not solve the required path thresholds.

Uruk's main planning problem is coordination. It has many recruitment channels and useful specialists, but its best paths, gems, sacreds, chariot, underwater branch, and ritual thresholds do not automatically meet in one place or on one timetable.

## Uruk evidence and ruleset

This chapter covers unmodded MA Uruk on the Book I 6.36 live baseline. The revision-2 official manual controls player-facing roster values, explicit recruitment locations, printed paths, national rules, capital-site output, national ritual tables, and item descriptions. Identifiers, membership sets, site fields, random masks, hero records, nation restrictions, and national item fields are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

No Uruk, Enkidu, Mushussu, or named Uruk national-ritual match appears in the official patch ledger through 6.36. That means no named patch correction is applied to the pinned object cross-check. It does not prove that every engine detail is unchanged.

## Uruk conversion chain

```text
large Enkidu bodies, province recruitment, and four monthly gems
-> target-specific infantry groups and distributed Shamans
-> ordinary mage forts plus protected capital recruitment
-> separate Water, Earth, Astral, and Nature budgets
-> battlefield support, sacred reserves, underwater access, and national summons
-> sustained fronts, remote recruitment, sieges, and Throne claims
```

The chain breaks when capital recruitment is treated as unlimited, when a random path is assumed before the mage is recruited, when a ritual is counted without its caster and gem type, or when the underwater roster is mistaken for a ready mixed-domain army.

## Uruk national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Large Enkidu population | Most land troops have more Hit Points and Strength than ordinary humans, but also occupy larger squares and have their own resource, encumbrance, and formation limits. |
| Heat preference +1 | Pretender scales begin from the printed national preference; this is not a recommendation for a complete scale design. |
| Order limit +1 and Heat limit +1 | The nation can select these scales one step beyond the ordinary limit. The benefit still depends on the full design and map. |
| Strong priests | Repeatable H2 priests exist on land and underwater, while capital Entu reach H3. This supports preaching, claiming, blessing, and Call God work without making every priest interchangeable. |
| Recall bonus | The nation page says Uruk is good at recalling a dead God. The precise live calculation and best use remain outside this source-only dossier. |
| Fortified Cities | Uruk uses its printed fortified-city building family rather than the standard-fort label. Construction time and local value still depend on province and campaign. |
| Temples cost 900 gold | Religious expansion has a higher printed building cost than the ordinary baseline and must be budgeted against forts, laboratories, troops, and mages. |
| Distributed recruitment | Enkidu Shamans and Warriors are available in non-fort provinces, while underwater forts unlock a separate Kulullu roster. |

## Uruk capital sites and recruitment geography

| Site or location | Verified fields | Recruitment consequence |
| --- | --- | --- |
| Great Temple of the Moon, site 186 | Two Astral pearls per month | Supports the capital religious centre and the Astral treasury |
| The Swamps of Ur, site 187 | One Nature gem per month | Adds Nature income to the capital budget |
| The House of Water, site 188 | One Water and one Earth gem per month | Completes the W1 E1 S2 N1 monthly income |
| Any non-fort province | Nation recruitment records | Enables Enkidu Shaman and Enkidu Warrior without constructing a fort |
| Underwater fort | Underwater recruitment records | Enables four Kulullu commanders and two Kulullu troops |

The capital produces four gems each month: W1 E1 S2 N1. It produces no Air or Fire gems. A random Air caster or an imported Fire caster therefore remains separate from the treasury needed to use that path.

## Complete Uruk commander membership

| ID | Commander | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 2934 | Enkidu Scout | 40 | 7 | 1 | Forts |
| 2942 | Enkidu Commander | 60 | 26 | 1 | Forts |
| 2946 | Naditu | 100 | 1 | 2 | Forts |
| 2944 | Nin | 105 | 1 | 2 | Forts |
| 2945 | Gala | 105 | 1 | 2 | Forts |
| 2949 | Gudu | 110 | 2 | 2 | Forts |
| 2951 | Ashipu | 185 | 1 | 2 | Forts |
| 2950 | Ishib | 220 | 2 | 2 | Forts |
| 2947 | Ereshdingir | 265 | 1 | 2 | Forts |
| 2943 | Ensi | 300 | 21 | 2 | Forts |
| 2948 | Entu | 400 | 1 | 4 | Capital only |
| 2952 | Mashmashu | 395 | 1 | 4 | Capital only |
| 2954 | Enkidu Shaman | 175 | 2 | 2 | Non-fort provinces |
| 3093 | Kulullu Commander | 60 | 11 | 1 | Underwater forts |
| 3094 | Kulullu King | 200 | 11 | 2 | Underwater forts |
| 3091 | Kulullu Sage | 265 | 1 | 2 | Underwater forts |
| 3092 | Kuliltu Queen | 270 | 1 | 2 | Underwater forts |

The ten ordinary, two capital, one non-fort, and four underwater records reconcile to seventeen distinct commanders. The non-fort and underwater entries are additional recruitment channels, not ordinary-fort duplicates.

## Complete Uruk troop membership

| ID | Troop | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 2935 | Enkidu Archer | 16 | 16 | 9 | Forts |
| 2936 | Enkidu Spearman | 16 | 16 | 9 | Forts |
| 2938 | Enkidu Heavy Archer | 16 | 24 | 9 | Forts |
| 2939 | Enkidu Soldier | 16 | 24 | 9 | Forts |
| 2941 | Enkidu Royal Guard | 20 | 26 | 15 | Forts |
| 2940 | Enkidu Iron Warrior | 22 | 24 | 17 | Forts |
| 2963 | Mushussu Charioteer | 170 | 21 | 16 | Capital only; maximum one per month |
| 2953 | Maiden of the Moon | 27 | 31 | 16 | Capital only |
| 2937 | Enkidu Warrior | 16 | 16 | 9 | Non-fort provinces |
| 3089 | Kulullu | 16 | 2 | 9 | Underwater forts |
| 3090 | Kulullu Soldier | 16 | 11 | 9 | Underwater forts |

The six ordinary, two capital, one non-fort, and two underwater records reconcile to eleven distinct troops. Mushussu Charioteer is the rider record; the Mushussu has a separate mount profile and is not counted as another recruitable troop.

## Complete Uruk roster by job

| Unit or group | Best source-backed role | Important limit |
| --- | --- | --- |
| Enkidu archers | High-Strength longbow fire at light or heavy armour levels | Precision 10 and formation, range, armour, and target protection still decide results. |
| Enkidu spear line | Large shielded frontage in medium or heavy armour | The heavier profile spends more resources and gains encumbrance. |
| Royal Guard | Better Attack, Defence, Morale, Hit Points, and leadership compatibility than the basic line | Twenty gold, 26 resources, and 15 recruitment points limit massing. |
| Iron Warrior | Armoured axe infantry with Berserker +1 | Higher recruitment cost and loss of shield change its defence profile. |
| Maiden of the Moon | Capital sacred spear infantry with Protection 17 | Thirty-one resources and capital-only recruitment make casualties expensive. |
| Mushussu Charioteer | Capital mobile shock piece with a large trampling, poisonous, fear-causing mount | 170 gold, one-per-month limit, and separate rider-and-mount behaviour prevent mass replacement. |
| Enkidu Warrior | Province-recruited axe infantry | Non-fort access is valuable, but local resources and travel still govern delivery. |
| Kulullu line | Amphibious underwater troops with low resource costs | Underwater recruitment does not establish mixed-army movement, supply, retreat, or battle outcomes. |

## Uruk commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Enkidu Scout | Stealth 40, forest and mountain survival | Intelligence and route checking | Does not lead the field army. |
| Enkidu Commander | Leadership 50 | Ordinary land command | Twenty-six resources compete with heavy troops. |
| Naditu | S1 H1, sacred | Inexpensive research, Astral utility, priest work | Low morale and 10 magic leadership. |
| Nin | H1 plus W/E/S/N random, sacred | Flexible low mage-priest | The useful path is not known before recruitment. |
| Gala | N1 H1, Spell Singer, sacred | Nature and chorus support | Spell Singer timing and outcomes remain unresolved. |
| Gudu | H1 plus A/E random, sacred | Low Air or Earth support | A single random level does not satisfy high ritual thresholds. |
| Ashipu | S1 N1 H1, Disease Healing 1 | Research, disease support, Astral-Nature work | Disease Healing output is not treated as a guaranteed timetable. |
| Ishib | W1 H2 plus A/W/E/N random | Strong priest and flexible elemental or Nature support | Final path must be recorded before assigning a job. |
| Ereshdingir | W1 S2 H2, Fortune Teller 5 | Fixed Astral-Water work and event support | Does not add Earth, Nature, Air, or Fire. |
| Ensi | W1 N1 H2 plus W/E/S/N random, Leadership 100 | Army-priest-mage and flexible random | 300 gold and 21 resources compete with both mages and troops. |
| Entu | W1 S2 H3 plus W/E/S/N randoms | Capital high priest, deep Astral-Water base, sacred command | Four recruitment points and capital-only queue pressure. |
| Mashmashu | S3 N1 plus A/W/E/S and pinned secondary randoms | Deep fixed Astral, national ritual preparation, high magic leadership | 395 gold, four recruitment points, and uncertain second live display. |
| Enkidu Shaman | E1 N2, Research -4 | Province recruitment, Earth-Nature access, first two national rituals | Research penalty makes its non-research jobs important. |
| Kulullu Commander | Amphibious Leadership 50 | Underwater mundane command | Underwater fort only and no magic path. |
| Kulullu King | W1 H2, amphibious Leadership 100 | Underwater priest and army command | Does not provide Earth or Astral. |
| Kulullu Sage | W2 plus A/W/S/N random, Research +4 | Underwater research and path support | Random result and underwater infrastructure govern availability. |
| Kuliltu Queen | W1 N1 H2 plus A/W/S/N random | Underwater priest-mage and command | Final path remains a recruitment result. |

## Reading the common Uruk random masks

The pinned records contain several one-level random pools. A 100% one-level result is divided equally among the paths in its mask.

| Mage | Fixed paths | Guaranteed random pool | Each primary outcome |
| --- | --- | --- | ---: |
| Nin | H1 | W, E, S, or N | 25% |
| Gudu | H1 | A or E | 50% |
| Ishib | W1 H2 | A, W, E, or N | 25% |
| Ensi | W1 N1 H2 | W, E, S, or N | 25% |
| Kulullu Sage | W2 | A, W, S, or N | 25% |
| Kuliltu Queen | W1 N1 H2 | A, W, S, or N | 25% |

The table describes recruitment probabilities, not a schedule. Gold, recruitment points, location, survival, and the order of results still determine when a path exists.

## Reading the Entu random paths

The pinned Entu record has W1 S2 H3, one guaranteed W/E/S/N level, and an independent 10% second roll from the same four paths. The manual displays one `?1` marker and does not expose that second field.

| Portfolio result | Probability per Entu |
| --- | ---: |
| No second random level | 90% |
| Second level matches the first path | 2.5% |
| Second level differs from the first path | 7.5% |
| A chosen named path appears at least once | 26.875% |
| A chosen named path appears twice | 0.625% |

A Water primary raises the fixed W1 to W2, while an Astral primary raises S2 to S3. Two matching results can rarely produce W3 or S4. Earth and Nature begin from zero and can rarely reach level two through two matching rolls.

## Reading the Mashmashu random paths

The Mashmashu has fixed S3 N1. Its guaranteed one-level pool is A/W/E/S. The pinned record also contains an independent 10% A/W/E/N level that the manual's single `?1` marker does not show.

| Result family | Probability |
| --- | ---: |
| Primary Air, Water, Earth, or Astral | 25% each |
| No secondary level | 90% |
| Any one of Air, Water, or Earth appears in at least one slot | 26.875% for that named path |
| Matching Air, Water, or Earth in both slots | 0.625% for that named path |
| Secondary Nature level | 2.5%, raising fixed N1 to N2 |
| Primary Astral level | 25%, raising fixed S3 to S4 |

The secondary pool does not contain Astral, and the primary pool does not contain Nature. No Mashmashu result reaches the national S5 or A3 ritual threshold without another proved bridge.

## Uruk native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Water | W1 on Ishib, Ereshdingir, Ensi, Entu, Kulullu King, and Kuliltu Queen; W2 Kulullu Sage; several randoms | Broad fixed access, but W2 E2 together is not printed on a recruit. |
| Earth | E1 Enkidu Shaman; several randoms | Fixed E1 casts Summon Kusarikkus; higher Earth depends on randoms, boosters, empowerment, summons, or a Pretender. |
| Astral | S1 Naditu and Ashipu, S2 Ereshdingir and Entu, S3 Mashmashu; several randoms | Deep fixed access reaches S3; Call Apkallu still requires S5. |
| Nature | N1 Gala, Ashipu, Ensi, Mashmashu, and Kuliltu Queen; N2 Enkidu Shaman; several randoms | Fixed N2 casts Herd of Buffaloes and forges the restricted Nature crown. |
| Air | Random Gudu, Ishib, Mashmashu, Kulullu Sage, or Kuliltu Queen | No fixed recruit has Air, and no recruit reaches A3 unaided. |
| Holy | H1, H2, and capital H3 recruits | Strong land and underwater priest depth, with cost and recruitment-channel differences. |
| Fire, Death, Glamour, Blood | No recruitable mage | Require independents, a Pretender, empowerment, summons, transformations, or another proved bridge. |

The two heroes add deeper Water, Earth, Nature, and Holy access, but heroes are not repeatable recruitment and are not assumed to arrive on schedule.

## Uruk national ritual reconciliation

| ID | Ritual | School | Requirement | Cost | Printed result |
| ---: | --- | --- | --- | --- | --- |
| 958 | Herd of Buffaloes | Conjuration 3 | N2 | 8 Nature gems | 5 or more Buffaloes |
| 360 | Summon Kusarikkus | Conjuration 4 | E1 | 4 Earth gems | 2 Kusarikkus |
| 361 | Summon Ugallu | Conjuration 5 | A3 | 24 Air gems | 1 A3 Ugallu |
| 362 | Call Anzus | Conjuration 7 | W2 E2 | 4 Water gems | 2 Anzus |
| 318 | Contact Scorpion Man | Conjuration 8 | E1 F1 | 12 Earth gems | 1 Scorpion Man |
| 363 | Call Apkallu | Conjuration 8 | S5 | 60 Astral pearls | 1 A3 W3 E2 S4 N2 H2 Umu-apkallu |

The six structured rows restrict to nation 66 and match the official Ur ritual table inherited by Uruk. `5+` Buffaloes remains a printed minimum; no extra-path scaling formula is inferred.

## Uruk ritual access from repeatable mages

Every Enkidu Shaman directly qualifies for Herd of Buffaloes and Summon Kusarikkus. Other Earth or Nature randoms may also qualify, but the fixed Shaman makes both early thresholds independent of capital luck.

Summon Ugallu needs A3, while the recruitable portfolio reaches at most A2 on the rare matching secondary results of Mashmashu, Kulullu Sage, or Kuliltu Queen and otherwise A1. Call Anzus needs W2 E2 on one caster; no recruit has that fixed pair, and the pinned random combinations do not produce both at level two unaided. Contact Scorpion Man needs Fire, which no recruitable mage possesses. Call Apkallu needs S5; fixed S3 Mashmashu can reach S4 from its primary Astral result but no pinned recruitable outcome reaches S5 unaided.

These are path-threshold statements. Boosters, empowerment, summons, a Pretender, or another legal bridge can change them, but the chapter does not assume such a bridge exists before it is named and funded.

## Uruk capital and ritual gem economy

The capital's W1 E1 S2 N1 income directly funds the two accessible early rituals: Herd of Buffaloes and Summon Kusarikkus. The same gems also compete with forging, battlefield use, site searching, and later path development. Astral is the largest capital income but the S5 national ritual remains beyond an unaided recruit.

Uruk receives no capital Air or Fire gems. Summon Ugallu therefore needs both a higher Air caster and an Air treasury. Contact Scorpion Man needs a Fire caster even though its printed cost is paid in Earth gems. Caster access and payment type must be recorded separately.

## Uruk national item boundary

| ID | Item | Construction and paths | Printed properties | Access boundary |
| ---: | --- | --- | --- | --- |
| 227 | Headdress of the Bull | Construction 5, N1 | Strength +2; Retinue 1; nation restricted | Many land mages qualify at N1; the live retinue arrival and replacement details remain unresolved. |
| 104 | Dawn Fang | Construction 9, E2 S1 | Magic Resistance +1, Affliction Resistance 1, Awe +1, double damage against undead and demons | National rebate field is pinned; no recruit has fixed E2 S1. |
| 184 | Shield of the Dawn | Construction 9, E2 S1 | Magic Resistance +1, Affliction Resistance 1, Fire Resistance +5, Awe +1 | Same E2 S1 and late-research boundary. |
| 216 | Helmet of the Dawn | Construction 9, E2 S1 | Magic Resistance +2, Affliction Resistance 1, Awe +1 | Same E2 S1 and late-research boundary. |
| 275 | Armor of the Dawn | Construction 9, E2 S1 | Hit Points +10, Magic Resistance +1, Affliction Resistance 2, Fire Resistance +15, Awe +1 | Same E2 S1 and late-research boundary. |

The four Dawn pieces carry Uruk national-rebate fields in the pinned item records. That establishes a nation-specific discount marker, not the final live price after every modifier and rounding step. The forge screen controls the displayed cost. The Headdress is restricted to a defined nation list that includes Uruk rather than carrying the same rebate field.

## Uruk national hero records

| ID | Fixed name | Unit name | Verified magic or status |
| ---: | --- | --- | --- |
| 2433 | Utnapishtim | Favored of Enki | N3 H2; sacred; inspirational penalty; pinned late-hero field 5 |
| 2965 | U'an | Apkallu | W4 E3 N2 H3; Research +10; high leadership; pinned late-hero field 10 |

The two national hero attributes identify powerful but non-repeatable access. No arrival probability, arrival turn, guaranteed ritual bridge, or interpretation of the late-hero raw values is inferred.

## Uruk patch reconciliation

No direct Uruk, Enkidu, Mushussu, Mashmashu, Ereshdingir, Kusarikku, Ugallu, Anzu, Apkallu, or Buffalo name match was found in the official ledger through 6.36. No patch change is therefore attached to the dossier's roster or national assets.

This negative ledger result is narrow. It confirms only that the collected official announcement text contains no named match; it is not proof against undocumented changes or behaviour that can only be observed in the current engine.

## Uruk opening priorities

The opening should secure a commander, enough protected frontage for the nearby independent weapons, and a research plan that uses recruitable mages without choking the troop queue. Enkidu infantry cost sixteen gold each but differ sharply in resources, shield use, weapon, Morale, and recruitment points. Exact expansion counts remain open because map generation, scales, formation, bless, opposition, and combat rolls change them.

Non-fort Enkidu Shamans and Warriors let productive provinces contribute before a fort is built. The Shaman's E1 N2 gives immediate ritual and research-path value, but Research -4 means its best job may be site searching, forging, ritual work, or battlefield support rather than remaining in a laboratory.

## Uruk recruitment packages to evaluate from reports

### Shielded Enkidu line

Spearmen and Soldiers provide shielded bodies at two armour levels. Select the heavier Soldier only when its extra protection is worth eight more resources and higher encumbrance. A mundane Enkidu Commander keeps the mage queue separate from troop leadership.

### Enkidu missile group

Archers and Heavy Archers use longbows with Strength 15. The heavier profile trades eight resources and mobility for protection. Missile range and damage still depend on current rules, while target armour, shields, weather, precision, and friendly positioning decide battlefield value.

### Capital sacred reserve

Maidens of the Moon provide protected sacred infantry, while one Mushussu Charioteer can be added per month. These are distinct pieces: the Maiden is a costly spear infantry profile, while the Charioteer depends on a separate trampling and poison-capable mount. Bless, formation, friendly size, and rider-and-mount outcomes remain case-specific.

### Distributed province group

Enkidu Warriors can be recruited outside forts and paired with local Enkidu Shamans. This turns otherwise undeveloped provinces into replacement and support points. It does not remove local resource limits, travel time, vulnerability, or the need for leadership.

### Kulullu underwater group

Kulullu and Kulullu Soldiers provide two resource levels, while the Commander, King, Sage, and Queen supply command, priesthood, research, and magic. This is a real underwater recruitment branch, but moving land assets into it or emerging onto land remains a separate logistics problem.

## Uruk research response tree

### Branch A: early Conjuration

Conjuration 3 opens Herd of Buffaloes for every Enkidu Shaman. Conjuration 4 adds Summon Kusarikkus from the same fixed E1 N2 chassis. The branch converts separate Nature and Earth treasuries into large tramplers or sacred magical guardians, but the printed Buffalo count is variable and battlefield performance remains untested here.

### Branch B: Astral control and support

Naditu and Ashipu provide S1, Ereshdingir and Entu provide S2, and Mashmashu provides S3 before randoms. Research should be selected around a named control, protection, or resistance problem. Deep Astral access does not by itself supply bodyguards, safe spell range, fatigue management, or a legal S5 ritual caster.

### Branch C: Nature and Earth support

Gala and several mixed mages provide N1, while the province Shaman guarantees E1 N2. This branch can combine buffs, protection, recovery support, site searching, the Headdress, and the first two national summons. Its value depends on which spells answer the actual enemy and whether the caster can reach the army.

### Branch D: path bridges and late national assets

Later goals include A3 for Ugallu, W2 E2 for Anzus, E1 F1 for the Scorpion Man, S5 for the Umu-apkallu, and E2 S1 for the Dawn items. None is an automatic recruitable threshold. Each project should name the booster, empowerment, hero, summon, Pretender, or other bridge; the research, gems, and mage turns; and the force that will use the result.

## Uruk battlefield packages

### Shielded line with mixed priest support

Enkidu Spearmen or Soldiers hold the line while an Ishib, Ereshdingir, Ensi, or another selected mage-priest supplies the script. A mundane commander handles leadership. The package still needs an answer to armour, fatigue, flanks, and spells that can strike its large formations.

### Province force with Shaman support

Warriors recruited outside forts can assemble near a threatened route while Shamans add fixed Earth and Nature access. The package is useful for distributed defence and replacement, but low infrastructure and travel can leave it fragmented.

### Capital sacred and chariot force

Maidens provide the stable sacred line and the monthly Mushussu adds a mobile shock piece. Entu can supply H3 and selected magic. The package is expensive in capital resources and commander time, and the mount's Trample, Fear, poison, attacks, and survival must not be collapsed into the rider's profile.

### Underwater Kulullu force

Kulullu Soldiers provide the armoured line while a King commands and a Sage or Queen supplies magic. The force should be planned within the underwater roster first. Mixed-domain movement, retreat, supply, and combat outcomes remain open rather than being inferred from Amphibious tags alone.

## Uruk Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and infrastructure | Funds 900-gold temples, fortified cities, capital mages, and resource-heavy troops | Income does not create capital turns or remove local resource limits. |
| Fire bridge | Opens Contact Scorpion Man and Fire searching or forging absent from recruits | A path without Fire gems, research, and delivery remains incomplete. |
| Air bridge | Reaches the A3 Ugallu threshold without relying on a future random ladder | Air income and the 24-gem ritual cost still need a plan. |
| Earth-Astral bridge | Supports the E2 S1 Dawn set and can help the W2 E2 or S5 projects | Construction 9 and national rebates do not make the items early. |
| Sacred design | Supports Maidens, sacred mages, Kusarikkus, Ugallu, and other sacred summons | Most Enkidu troops and the Mushussu rider are not improved merely by being in the same army. |
| Awake expander | Supplies early independent-taking power while other queues develop | Afflictions, counters, and delayed scales can erase the gain. |

## Uruk matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light infantry | Large shielded lines, high-Strength arrows, Buffaloes, Kusarikkus, and target-specific area magic | Paying capital prices for work ordinary Enkidu can perform. |
| Heavy armour | High Strength, axes, Earth or Astral support, fatigue, summons, and armour-answering magic | Assuming spears or longbows solve every protection level. |
| Armour-piercing or armour-negating damage | Spacing, resistance, disruption, summons, and a different line profile | Treating mundane Protection as universal defence. |
| High Defence, ethereal, or Glamour targets | Area effects, magic weapons, attack support, Spirit Sight summons, and control | Assuming size or Strength answers unrelated defensive mechanics. |
| High Magic Resistance or mindless units | Physical pressure, buffs, summons, and non-MR effects | Building the battle around one Astral resistance check. |
| Fast flankers and flyers | Guards, reserves, dispersed mages, and protected routes | Leaving expensive Entu or Mashmashu in an open rear cluster. |
| Raids and dispersed pressure | Scouts, province Warriors and Shamans, local forts, and replacement commanders | Keeping every useful commander and mage in the capital. |
| Underwater objectives | Kulullu recruitment, underwater commanders, and a separate logistics plan | Treating an underwater roster as proof that a land army crosses domains cleanly. |

## Monthly Uruk audit

- Is each queue limited by gold, resources, recruitment points, location, or travel time?
- Are non-fort Shaman and Warrior provinces being used without leaving them undefended?
- Does the current troop mix answer the reported weapons, protection, numbers, size, and terrain?
- Is a mundane commander available so a mage can keep its research, ritual, or battle job?
- Has every random mage been labelled by final displayed paths before receiving a task?
- Are Water, Earth, Astral, Nature, Air, and Fire treasuries being treated separately?
- Does each national ritual have a legal caster, research level, gem budget, commander, and delivery route?
- Are the capital's four recruitment points being divided deliberately among Entu and Mashmashu?
- Is the monthly Mushussu limit being treated as a slow reserve rather than a mass-recruitment line?
- Does any underwater operation have its own commanders, supply, movement, retreat, and replacement plan?

## Uruk unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for Enkidu infantry, missile groups, Maidens, and Mushussu Charioteers;
2. live 6.36 confirmation of the Entu and Mashmashu secondary random fields, which the manual does not display;
3. exact Call God recall advantage and its interaction with current priest commitment;
4. Spell Singer timing, chorus composition, fatigue, interruption, and survival outcomes for Gala;
5. rider, Mushussu, Trample, Fear, poison, dismount, and separate-target outcomes under specific attacks;
6. underwater movement, supply, retreat, and battle outcomes for mixed Uruk and Kulullu forces;
7. the variable scaling behind Herd of Buffaloes beyond its printed minimum;
8. live discounted costs of the Dawn set and the Headdress retinue's arrival and replacement behaviour;
9. hero arrival timing and the meaning of the pinned late-hero values;
10. specific Pretender designs, scripts, and matchup performance on a generated map.

These are evidence gaps, not invitations to guess. No runtime test or new test asset was prepared during this unit. R-047, R-058, and the wider hands-on testing queue remain parked until testing is explicitly resumed.

# Part XXV: Middle Age Ashdod, Reign of the Anakim

## Ashdod one-page command brief

Middle Age Ashdod combines human slaves and nine recruitable giant troop profiles with a compact mage corps built around Fire, Earth, Astral, Death, and Holy magic. Five commanders and seven troops are available from ordinary forts. The capital adds three expensive mage-commanders, two sacred Anakites, and two sites producing five gems each month.

The reliable structure is:

- cheap human Slingers and Slaves can fill low-cost roles while Edomites and the larger Rephaite troops supply the national giant line;
- Amorites, Gileadites, Gileadite Archers, and Bashanites trade gold, resources, armour, shields, weapons, and recruitment points rather than forming one interchangeable elite class;
- Sheshai and Ahiman Anakites are capital-only sacreds with distinct armour and combat profiles;
- ordinary forts can recruit Kohanim, Emites, and Rephaite Sages, while the capital queue must divide four-point turns among Adons, Zamzummites, and Talmai Elders;
- the capital produces F1 E2 S1 D1, with no native Air, Water, Nature, Glamour, or Blood income;
- recruitable randoms can reach deep Fire, Earth, Astral, and Death, but several important cross-path combinations are rare;
- national Conjuration includes angels, ancestor spirits, and Mazzikim, while Strange Fire supplies one national battlefield spell;
- Ashdod has no national item or rebate record in the pinned item table.

Ashdod's planning problem is concentration. Its strongest bodies and deepest mages are expensive, resource-heavy, capital-bound, or random-dependent. A plan that buys only premium giants can lose infrastructure and mage tempo, while a plan that treats random paths as guaranteed can reach research with no legal caster.

## Ashdod evidence and ruleset

This chapter covers unmodded MA Ashdod on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, explicit capital restrictions, printed paths, national summary, site income, national spell tables, and ritual requirements. Identifiers, recruitment membership, random masks, site fields, hero records, and nation restrictions are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

No Ashdod, Anakite, Rephaite, Zamzummite, Ditanu, Malik, or named Ashdod national-spell match appears in the collected official patch ledger through 6.36. No named patch correction is therefore applied. A negative ledger search does not establish undocumented engine behaviour.

## Ashdod conversion chain

```text
cheap human bodies, giant infantry, and five capital gems
-> a target-specific line backed by ordinary-fort researchers
-> protected capital recruitment and recorded random paths
-> separate Fire, Earth, Astral, and Death treasuries
-> battlefield support, sacred reserves, angels, or ancestor summons
-> surviving armies, sieges, Throne claims, and replacement cycles
```

The chain breaks when human slaves are mistaken for durable giants, when every giant profile is priced as if resources were unlimited, when a Talmai path is budgeted before recruitment, or when a national ritual is counted without both its caster and gem type.

## Ashdod national rules that shape the plan

| Rule or asset | Operational consequence |
| --- | --- |
| Rephaite giants | Most national troops have high Hit Points and Strength, but their gold, resources, recruitment points, appetite, size, and formation needs remain real costs. |
| Human slaves | Seven-gold Slingers and Spearmen provide a separate low-cost body class; low Morale and ordinary human durability limit what that price buys. |
| Prefers Heat +2 | The nation summary identifies the preferred climate; this is not a complete scales recommendation. |
| Heat limit +1 and Death limit +1 | Pretender design can select those scales one step beyond the ordinary limit. The strategic value depends on the whole design and map. |
| Giant Forts | Ashdod uses the printed giant-fort family rather than a standard-fort label. Local construction value and timing still depend on province and campaign. |
| Weak priesthood with one medium priest | Kohanim and Zamzummites are H1; capital Adons reach H2. Priest access exists, but high-priest work competes for the capital queue. |
| Sacred Anakites and capital mage-commanders | The strongest sacred troops and all three deep mage chassis are capital-only, making capital turns a strategic resource. |

## Ashdod capital sites and recruitment geography

| Site | Verified fields | Recruitment or income consequence |
| --- | --- | --- |
| The Twin Cities, site 144 | D1; home recruitment for Sheshai Anakite, Ahiman Anakite, Zamzummite, Adon, and Talmai Elder | Holds the full capital-only troop and commander set |
| Mount Seir, site 145 | F1 E2 S1 | Completes the capital's Fire, Earth, Astral, and Death income |

The capital produces five gems per month: F1 E2 S1 D1. It produces no Air, Water, Nature, Glamour, or Blood gems. Caster access and gem income must therefore be recorded separately, especially for Summon Mazzikim and Call Arel, which require Nature.

## Complete Ashdod commander membership

| ID | Commander | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 2010 | Edomite Scout | 45 | 17 | 1 | Forts |
| 2009 | Rephaite Commander | 140 | 35 | 1 | Forts |
| 2029 | Kohen | 120 | 3 | 1 | Forts |
| 2038 | Emite | 175 | 3 | 2 | Forts |
| 2060 | Rephaite Sage | 215 | 3 | 2 | Forts |
| 2027 | Adon | 425 | 85 | 4 | Capital only |
| 2011 | Zamzummite | 440 | 3 | 4 | Capital only |
| 2028 | Talmai Elder | 520 | 3 | 4 | Capital only |

The five ordinary and three capital records reconcile to eight distinct commanders. The capital entries are additional home-site recruits, not ordinary-fort duplicates.

## Complete Ashdod troop membership

| ID | Troop | Gold | Resources | Rec points | Verified recruitment |
| ---: | --- | ---: | ---: | ---: | --- |
| 2003 | Human Slinger | 7 | 2 | 3 | Forts |
| 2004 | Human Slave | 7 | 3 | 3 | Forts |
| 2005 | Edomite | 20 | 15 | 15 | Forts |
| 2006 | Amorite | 40 | 27 | 17 | Forts |
| 2007 | Gileadite | 40 | 29 | 17 | Forts |
| 2061 | Gileadite Archer | 40 | 47 | 17 | Forts |
| 2008 | Bashanite | 50 | 33 | 21 | Forts |
| 2025 | Sheshai Anakite | 130 | 50 | 47 | Capital only |
| 2026 | Ahiman Anakite | 130 | 89 | 47 | Capital only |

The seven ordinary and two capital records reconcile to nine distinct troops. The two Anakites share price and recruitment-point cost but do not share the same armour, protection, Morale, Strength, Attack, Defence, or Fire Resistance.

## Complete Ashdod roster by job

| Unit or group | Best source-backed role | Important limit |
| --- | --- | --- |
| Human Slinger | Cheapest national missile body | Low Morale, light protection, and sling performance depend on range and target. |
| Human Slave | Cheapest spear frontage | Low Morale and ordinary human durability make it a screen rather than a giant substitute. |
| Edomite | Lower-cost javelin and spear giant | Less durable and less skilled than the larger Rephaim. |
| Amorite | Mobile poison-tipped spear giant | Moderate armour and lack of shield change its survival profile. |
| Gileadite | Shielded spear giant | Resources and encumbrance exceed the Edomite line. |
| Gileadite Archer | Armoured great-bow giant | Forty-seven resources and low Defence make protection and positioning important. |
| Bashanite | Strong broad-sword line giant | Fifty gold and 21 recruitment points constrain mass replacement. |
| Sheshai Anakite | Capital sacred attacker with Berserker +2 and Fire Resistance +10 | Capital-only, 130 gold, and 50 resources. |
| Ahiman Anakite | Heavier capital sacred with higher Protection, Morale, Strength, Attack, and Defence | Eighty-nine resources and the same capital-only queue. |

## Ashdod commander and mage portfolio

| Commander | Paths or ability | Main jobs | Recruitment warning |
| --- | --- | --- | --- |
| Edomite Scout | Stealth 50; forest, mountain, and waste survival | Intelligence and route checking | Seventeen resources compete with troops. |
| Rephaite Commander | Leadership 100 | Giant army command | Thirty-five resources and 140 gold are paid for a non-mage leader. |
| Kohen | H1; pinned independent 10% Death level | Low priest and occasional Death access | The manual prints H1 only; the 10% field remains pinned, not live-confirmed. |
| Emite | D1 plus guaranteed F/E/S/D level; Fortune Teller 10 | Death research, event support, and low random magic | Final path must be recorded before assignment. |
| Rephaite Sage | One guaranteed level two in F/E/S; Research +4 | Efficient research and a focused level-two path | No fixed path exists before the random resolves. |
| Adon | H2 plus one guaranteed level two in F/E/S; Leadership 150; sacred; Research -4 | Capital army-priest and deep elemental or Astral support | 425 gold, 85 resources, four recruitment points, and a research penalty. |
| Zamzummite | E1 D2 H1 plus E/D and F/E/S/D randoms; Spirit Sight | Deep Death, ancestor rituals, undead leadership, and mixed magic | Capital-only, 440 gold, and four recruitment points. |
| Talmai Elder | One guaranteed level three in F/E/S plus pinned 10% F/E/S/D level; Research +8; Forge Bonus 1 | Deep research, forging, and rare cross-path access | Capital-only, 520 gold, four recruitment points, and the second slot is not printed by the manual. |

## Reading the ordinary Ashdod randoms

| Mage | Fixed paths | Pinned random scheme | Result |
| --- | --- | --- | --- |
| Kohen | H1 | Independent 10% D1 | D1 on 10%; no Death level on 90% |
| Emite | D1 | One guaranteed F/E/S/D level | 25% each; a Death result reaches D2 |
| Rephaite Sage | None | One guaranteed level two in F/E/S | F2, E2, or S2 at one third each |
| Adon | H2 | One guaranteed level two in F/E/S | F2, E2, or S2 at one third each |

These are recruitment probabilities, not delivery dates. Gold, recruitment points, fort location, survival, and the order of results decide when the path can be used.

## Reading the Zamzummite random paths

The Zamzummite has fixed E1 D2 H1. Its first guaranteed random is E or D, and its second guaranteed random is F, E, S, or D.

| Portfolio result | Probability per Zamzummite |
| --- | ---: |
| Fire 1 | 25% |
| Astral 1 | 25% |
| At least one extra Earth level | 62.5% |
| Both randoms Earth, reaching E3 | 12.5% |
| At least one extra Death level, reaching at least D3 | 62.5% |
| Both randoms Death, reaching D4 | 12.5% |

Fixed E1 D2 means every Zamzummite already has both Earth and Death. The table describes how the two randoms deepen or broaden that base; it does not establish a recruitment timetable.

## Reading the Talmai Elder random paths

The Talmai Elder has one guaranteed level-three result in Fire, Earth, or Astral. The pinned record also contains an independent 10% one-level result from Fire, Earth, Astral, or Death, while the manual prints only `?3`.

| Portfolio result | Probability per Talmai Elder |
| --- | ---: |
| Primary F3, E3, or S3 | One third each |
| No secondary level | 90% |
| Named F, E, S, or D secondary | 2.5% each |
| A chosen F, E, or S path appears at least once | 35% |
| Matching primary and secondary, reaching level four | About 0.833% for that named path |
| Death 1 | 2.5% |

A Talmai can satisfy S2 F1 for Strange Fire when the primary and secondary rolls split between Astral and Fire. That combined result occurs in two orientations, about 1.667% in total. Call Hashmal specifically needs S3 F1, which occurs only when the primary is Astral and the secondary is Fire, about 0.833%.

## Ashdod native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Fire | Emite F1 random; Rephaite Sage or Adon F2 random; Talmai F3 primary with rare F4 | No fixed Fire recruit, and Fire-Astral cross-paths depend on rare Talmai results. |
| Earth | Fixed E1 Zamzummite; random E2 Sages and Adons; E3 Talmai; Zamzummite can reach E3 | Broad access, but the deepest results remain random or capital-bound. |
| Astral | Random S1 Emite or Zamzummite; random S2 Sage or Adon; S3 Talmai with rare S4 | No recruitable result reaches S5 unaided. |
| Death | Fixed D1 Emite and D2 Zamzummite; randoms can reach D2, D3, or D4 | Zamzummite supports the national ancestor rituals, subject to its random result. |
| Holy | H1 Kohen and Zamzummite; H2 Adon | Medium priesthood is capital-only. |
| Air, Water, Nature, Glamour, Blood | No recruitable mage | Require independents, a Pretender, empowerment, summons, heroes, or another proved bridge. |

The three national heroes add deep Fire, Earth, Water, Astral, and Holy paths, but heroes are not repeatable recruitment and are not assumed to arrive on schedule.

## Ashdod national spell and ritual reconciliation

| ID | Spell or ritual | School | Requirement | Cost | Printed result |
| ---: | --- | --- | --- | --- | --- |
| 345 | Strange Fire | Evocation 4 | S2 F1 | 20 fatigue | Area 3, armour-piercing, 8+ damage |
| 358 | Summon Mazzikim | Conjuration 3 | N1 | 3 Nature gems | 10 Mazzikim |
| 352 | Call Malakh | Conjuration 4 | S2 | 9 Astral pearls | 1 Malakh |
| 353 | Call Hashmal | Conjuration 6 | S3 F1 | 21 Astral pearls | 1 Hashmal |
| 347 | Dirge for the Dead | Conjuration 6 | D3 H1 | 25 Death gems | 1 Ditanu |
| 354 | Call Arel | Conjuration 7 | S4 N1 | 39 Astral pearls | 1 Arel |
| 355 | Call Ophan | Conjuration 8 | S5 F2 | 49 Astral pearls | 1 Ophan |
| 348 | Banquet for the Dead | Conjuration 8 | D4 H1 | 55 Death gems | 1 Malik and 4 Ditanu |
| 356 | Call Merkavah | Conjuration 9 | S7 F3 | 222 Astral pearls | 1 Chayot |

The nine structured rows restrict to nation 64, alone or with the other named nations shown in the official tables. Printed summon counts and requirements are retained without inferring retinue behaviour, shape mechanics, or battlefield performance.

## Ashdod ritual access from repeatable mages

Call Malakh is directly available to an S2 Rephaite Sage or Adon and to an S3 Talmai, each a one-third result on its chassis. Strange Fire needs S2 F1 on one caster; only the rare split Talmai secondary produces the necessary recruitable combination. Call Hashmal needs the narrower S3 F1 Talmai result.

A Zamzummite reaches D3 H1 whenever at least one random adds Death, a 62.5% result, qualifying for Dirge for the Dead. It reaches D4 H1 only when both randoms add Death, a 12.5% result, qualifying for Banquet for the Dead.

Summon Mazzikim and Call Arel need Nature, which no recruitable mage has. No recruit reaches the S5 F2 threshold for Call Ophan or S7 F3 for Call Merkavah. Boosters, empowerment, summons, heroes, or a Pretender can change access, but each bridge must be named and funded before the ritual is counted.

## Ashdod capital and ritual gem economy

The capital's F1 E2 S1 D1 income naturally supports Earth work and slowly accumulates the Astral and Death currencies used by most national summons. It does not produce Nature gems for Mazzikim or Arel. A Nature caster and a Nature treasury are separate missing parts.

The highest angelic rituals cost 49 or 222 Astral pearls, while the ancestor rituals cost 25 or 55 Death gems. Research, caster rarity, gem accumulation, forging, and battlefield use compete for different bottlenecks. A legal path does not prove that the ritual is timely or affordable.

## Ashdod national item boundary

No item in the pinned `BaseI.csv` carries Ashdod's nation ID 64 in the national-restriction or national-rebate fields. The dossier therefore records no Ashdod national item, national discount, or national forging exception.

This is a structured-snapshot result, not a claim that ordinary magic items are unavailable. General forging follows Book V and the current game interface; final displayed costs and any undocumented exception remain outside this source-only statement.

## Ashdod national hero records

| ID | Fixed name | Unit name | Verified magic or status |
| ---: | --- | --- | --- |
| 2047 | Sheshai | First Son of Anak | F4 H2; sacred; pinned late-hero field 20 |
| 2048 | Ahiman | Second Son of Anak | E4 H2; sacred; pinned late-hero field 20 |
| 2049 | Talmai | Third Son of Anak | F1 W4 E1 S4 H2; sacred; pinned late-hero field 20 |

The hero records provide powerful but non-repeatable access, including the nation's only listed Water path. No arrival probability, arrival turn, guaranteed ritual bridge, or meaning of the raw late-hero value is inferred.

## Ashdod patch reconciliation

No direct Ashdod, Anakite, Rephaite, Zamzummite, Talmai Elder, Malakh, Hashmal, Arel, Ophan, Merkavah, Ditanu, Malik, or Mazzikim name match was found in the official ledger through 6.36. No patch change is attached to the roster or national spell tables.

This is a narrow search result. It does not prove that every current engine interaction matches the pinned snapshot, and it does not turn undocumented behaviour into a fact.

## Ashdod opening priorities

The opening should separate three budgets: enough bodies to take and hold territory, enough infrastructure to recruit research mages outside the capital, and enough protection for the home queue to produce its rare deep casters. Human troops cost seven gold, but their Morale and durability differ sharply from the giant line. Exact expansion counts remain open because opposition, scales, formation, bless, terrain, and combat rolls change them.

The ordinary mage choices solve different problems. Emites guarantee D1 and a broad level-one random; Sages provide Research +4 and one focused level-two path. Rephaite Commanders keep leadership off the mage queue, but their gold and resources must be justified against the troops they lead.

## Ashdod recruitment packages to evaluate from reports

### Human screen and giant damage line

Human Slaves or Slingers can provide cheap bodies while Amorites, Gileadites, or Bashanites supply giant damage. The package should be chosen against the reported weapons and protection. Low-Morale humans can fail before the premium line does, and large units still need enough frontage.

### Shielded Gileadite line

Gileadites bring shields, spears, Morale 13, and Protection 14. They cost forty gold, 29 resources, and 17 recruitment points. The package is useful when missile and contact protection matter, but it should not be purchased by habit when the enemy calls for poison spears, swords, missiles, or cheaper bodies.

### Giant missile group

Gileadite Archers carry great bows behind Protection 17. Their forty-seven-resource cost can sharply reduce output in a weak fort. Target armour, shields, weather, range, and positioning remain battle questions, so recruitment should respond to reports rather than a universal ratio.

### Capital Anakite reserve

Sheshai and Ahiman Anakites are sacred capital troops with different offensive and defensive profiles. Sheshai is cheaper in resources and has Berserker +2 and Fire Resistance +10; Ahiman spends 89 resources for heavier protection and better core combat statistics. Bless value and survival remain matchup-dependent.

## Ashdod research response tree

### Branch A: ordinary Earth, Fire, and Astral support

Rephaite Sages and Adons produce F2, E2, or S2 in equal thirds. Early research should answer a named protection, damage, fatigue, or resistance problem rather than chase a path label. The result must be recorded before a spell package is assigned.

### Branch B: national Conjuration

Conjuration 4 opens Call Malakh for S2 results. Conjuration 6 adds Hashmal for a rare Talmai and Dirge for a qualifying Zamzummite. Later levels offer Arel, Ophan, Banquet for the Dead, and Merkavah, but each has a distinct path and treasury gate. National availability does not make every ritual natively castable.

### Branch C: Strange Fire

Evocation 4 unlocks Strange Fire, an S2 F1 armour-piercing area spell. The repeatable recruitable combination is rare because it depends on a split Talmai primary and secondary result. Researching the spell before such a caster exists creates no battlefield package.

### Branch D: Death and ancestor economy

Every Zamzummite begins at D2 H1 and has a 62.5% chance to reach at least D3, while 12.5% reach D4. This branch can plan around Dirge and Banquet, but capital turns, 25- or 55-gem costs, undead leadership, summoned composition, and delivery must all be budgeted.

## Ashdod battlefield packages

### Giant line with mundane command

A Rephaite Commander leads the selected giant line while a Sage, Emite, or Zamzummite handles magic. Separating leadership preserves mage actions, but the commander itself costs 140 gold and 35 resources. The force still needs answers to fatigue, armour, flanks, and magic that bypasses mundane protection.

### Mixed human and Rephaite force

Cheap humans expand frontage or absorb low-value contact while the giants supply damage. Morale and speed differences can split the formation or routing sequence. The package should be judged from battle reports rather than assumed to behave as one uniform line.

### Capital sacred force

Anakites form an expensive sacred reserve with an H2 Adon available from the same capital. This compresses troops, priesthood, and deep random magic into one queue. The force must justify both the capital turns and the resources that could have produced many ordinary giants.

### Ancestor-supported force

Dirge or Banquet adds Ditanu and Malik records to a national army. Their printed paths, ethereal and undead status, Fear, leadership, and weapon profiles are source facts. Their retinue organisation, replacement, spell use, and battlefield outcomes remain unresolved until observed.

## Ashdod Pretender families

| Family | What it solves | What it must not conceal |
| --- | --- | --- |
| Economy and infrastructure | Funds giant forts, laboratories, premium troops, and capital mages | Income does not add capital recruitment points or local resources. |
| Nature bridge | Opens Mazzikim and helps reach Arel while adding a missing gem path | A path without Nature income, research, and mage-turns remains incomplete. |
| Astral-Fire bridge | Makes Strange Fire and angel thresholds deliberate rather than rare Talmai outcomes | High Astral ritual costs still need a treasury and delivery plan. |
| Death support | Accelerates ancestor rituals and Death searching | Zamzummites already offer deep random Death; duplication should solve a timing problem. |
| Sacred design | Supports Anakites, Adons, Zamzummites, and sacred summons | Most ordinary troops and human slaves are not blessed. |
| Awake expander | Supplies early independent-taking power while expensive queues develop | Afflictions, counters, and delayed scales can erase the gain. |

## Ashdod matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light infantry | Giant Strength, protected lines, missiles, and area magic | Paying capital prices for work ordinary giants can perform. |
| Heavy armour | High Strength, poison weapons, Earth or Fire support, fatigue, and armour-answering magic | Assuming every spear or great bow solves every protection level. |
| Armour-piercing or armour-negating attacks | Spacing, resistance, disruption, summons, and cheaper screens | Treating large Hit Point totals as universal defence. |
| High Defence, ethereal, or Glamour targets | Area effects, magic weapons, attack support, Spirit Sight, and control | Assuming size and Strength answer unrelated defensive mechanics. |
| High Magic Resistance or mindless units | Physical pressure, buffs, summons, and non-MR effects | Building the fight around one Astral resistance check. |
| Fast flankers and flyers | Guards, reserves, dispersed mages, and protected routes | Leaving 440- or 520-gold capital mages exposed in one rear cluster. |
| Raids and dispersed pressure | Scouts, local forts, cheap replacement bodies, and reserve commanders | Concentrating every useful unit and mage in the capital. |

## Monthly Ashdod audit

- Is each fort limited by gold, resources, recruitment points, or commander turns?
- Does the troop mix answer the reported weapons, armour, numbers, and terrain?
- Are human units performing a defined cheap role rather than being mistaken for giants?
- Is a mundane commander available where using a mage as leader would lose research or ritual tempo?
- Has every random mage been labelled by final paths before receiving a task?
- Are Fire, Earth, Astral, Death, and missing Nature treasuries tracked separately?
- Does each national ritual have a legal caster, research level, gem budget, commander, and delivery route?
- Are capital turns being divided deliberately among Adons, Zamzummites, Talmai Elders, and sacred troops?
- Is the plan paying for premium Anakites only when their distinct profile matters?
- Are hero paths excluded from any schedule that must be repeatable?

## Ashdod unresolved evidence boundary

The following claims remain open:

1. exact expansion-party ranges for human screens, each Rephaite line, giant missiles, and Anakites;
2. live 6.36 confirmation of the Kohen and Talmai secondary random fields that the manual does not display;
3. Strange Fire targeting, friendly-fire risk, scaling, and battlefield results;
4. Ditanu, Malik, Malakh, Hashmal, Arel, Ophan, and Chayot scripting, retinue, shape, and combat behaviour;
5. final effective research and forge value of particular random mages under real scales and sites;
6. giant appetite, supply, movement, formation, siege, retreat, and replacement outcomes on a generated map;
7. hero arrival timing and the meaning of pinned late-hero values;
8. specific Pretender designs, scripts, blesses, and matchup performance.

These are evidence gaps, not invitations to guess. No runtime test or new test asset was prepared during this unit. R-047, R-058, and the wider hands-on testing queue remain parked until testing is explicitly resumed.

# Part XXVI: Middle Age T'ien Ch'i, Imperial Bureaucracy

## T'ien Ch'i one-page command brief

Middle Age T'ien Ch'i converts a large human roster, fortified cities, conscription, broad low-path magic, and four capital gems into flexible conventional armies and specialised ritual access. The official manual describes cavalry, heavy infantry, archers, crossbows, average priests, Order limited to +1, Misfortune limited to +1, and the ability of Eunuchs to conscript troops for province defence while collecting taxes. The nation is broad rather than automatically deep: most non-capital mages begin at one path and depend on randoms, combinations, gems, or capital recruitment for higher thresholds.

The opening should therefore preserve choices. Footmen and archers are cheap in gold, Ministry troops provide an intermediate line, Imperial troops consume more resources and recruitment points, and cavalry shifts more cost into gold. A Fortified City does not guarantee that every line can be produced efficiently; local resources, recruitment points, commander turns, and the need for laboratories still decide what a province can support.

The capital is unusually congested. Red Guards, Prince Generals, Imperial Alchemists, and Celestial Masters all compete for its recruitment capacity. The two capital sites also supply five gems per month in four paths, but income is not the same as access: a ritual still needs the correct caster, research, laboratory, gems, and a useful destination.

Treat random mages as recorded portfolios. The Inspector snapshot exposes the random masks, while the official manual confirms the visible base paths and costs. Recruit first, record the result, and only then assign a research, search, forge, ritual, priest, or battlefield role. Exact live display timing and any behaviour not printed by the sources remain unresolved.

## T'ien Ch'i evidence and ruleset boundary

This chapter covers unmodded Middle Age T'ien Ch'i under the Dominions 6.36 baseline. The official manual supplies the nation summary, roster, costs, recruitment locations, visible magic, site income, national spells, and item descriptions. The Dominions 6 Data Inspector snapshot at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, pinned to the 6.35 data update, supplies object identifiers, random masks, hidden restriction fields, and cross-checks.

The two sources have different jobs. A structured row can establish that a random draw exists and which paths it contains, but it does not prove how the current client reveals that draw or how the resulting mage behaves in a real battle. The 6.36 patch ledger is checked for named changes after the pinned snapshot. No runtime test, replay, save, or new test asset is used here.

## T'ien Ch'i conversion chain

```text
cheap human roster and fortified cities
-> borders, taxes, and recruitment centres
-> recorded random-mage portfolio
-> research plus four-path capital gem income
-> national summons, alchemy, forging, and battlefield support
-> local armies, reserves, siege, and claims
```

The fragile arrows are infrastructure and depth. A wide roster can spend resources without creating the needed battlefield answer. A wide path portfolio can also look stronger on paper than it is if the required two-path or level-two result is rare. Plans should be attached to actual recruits and treasury balances, not to the union of every possible random.

## T'ien Ch'i national rules that shape planning

| Rule | Source-backed fact | Planning consequence |
| --- | --- | --- |
| Fortified Cities | The manual lists Fortified Cities as the national building type. | Fort cost and build time still compete with laboratories, temples, troops, and commanders. |
| Conscription | Eunuchs conscript troops for province defence while collecting taxes. | Tax collection has a national side benefit, but the manual does not print exact composition or scaling. |
| Scales limits | Order is limited to +1 and Misfortune to +1. | Pretender design must respect both bounds instead of importing a generic human-nation scale plan. |
| Broad magic | The nation summary lists Water, Astral, Fire, Air, Earth, Nature, and Glamour. | The list describes the national portfolio, not guaranteed depth on each recruit. |
| Capital sacred | Red Guards are sacred and capital-only. | Bless investment serves a narrow recruitable troop queue unless it has other jobs. |

The exact province-defence units and conscription rate are not stated in the manual table. Those details remain open rather than being inferred from an opaque attribute code.

## T'ien Ch'i capital sites and recruitment geography

The Heavenly Gate produces one Air gem and two Astral pearls per month and enables Celestial Master recruitment. The Celestial City produces one Water and one Earth gem per month and enables Red Guards, Prince Generals, and Imperial Alchemists. Together they provide five capital gems per month: A1, W1, E1, and S2.

Master of the Way is the geographical exception among ordinary commanders: the manual marks it recruitable outside forts as well as in forts. That improves access to W1H1 and its five-path random without adding another fort, but gold, local recruitment rules, and safe movement still matter. All other capital-only records remain confined to the capital unless a source explicitly says otherwise.

## T'ien Ch'i complete commander membership

The official roster contains eleven ordinary commander records and three capital-only records.

| Recruitment | Commander records |
| --- | --- |
| Ordinary | Scout; Imperial Consort; Eunuch; General; Ceremonial Master; Minister of Rituals; Apothecary; Imperial Geomancer; Minister of Magic; Alchemist of the Five Elements; Master of the Way |
| Capital only | Prince General; Imperial Alchemist; Celestial Master |

This is a membership table, not a recommendation. Scout and Eunuch jobs differ from combat command; priests differ in holy level; and several mage names hide materially different fixed and random paths.

## T'ien Ch'i complete troop membership

The official roster contains fifteen ordinary troop records and one capital-only record.

| Recruitment | Troop records |
| --- | --- |
| Ordinary | Footman with pike; Footman with glaive; Footman with spear and shield; Archer; Ministry Guardsman with glaive; Ministry Footman with spear and shield; Ministry Guardsman with man catcher; Imperial Footman; Imperial Archer; Imperial Crossbowman; Imperial City Guard; Imperial Guard; Horseman; Heavy Horseman; Imperial Horseman |
| Capital only | Red Guard |

Weapon, shield, armour, morale, resource, and recruitment-point differences prevent these records from collapsing into one generic infantry or cavalry line. The right purchase depends on the reported enemy and the local production constraint.

## T'ien Ch'i roster by job

| Job | Main records | Boundary |
| --- | --- | --- |
| Scouting | Scout | Information depends on survival and coverage. |
| Tax and provincial administration | Eunuch | Conscription is confirmed; exact output is unresolved. |
| Mundane command | General; Prince General | The Prince General consumes a capital turn and is not a default upgrade. |
| Priesthood | Ceremonial Master H1; Minister of Rituals H2; Master of the Way H1; Celestial Master H2 | Holy level does not supply missing magical paths. |
| Cheap path specialists | Apothecary N1; Imperial Geomancer E1S1 | Low cost and guaranteed paths make roles reproducible. |
| Random generalists | Minister of Magic; Alchemist of the Five Elements; Master of the Way | Final paths must be recorded before assignment. |
| Capital depth | Imperial Alchemist; Celestial Master | Stronger access competes with every other capital recruit. |
| Conventional line | Footmen, Ministry troops, Imperial troops | Gold, resources, recruitment points, shields, and weapons differ. |
| Mobile line | Horseman; Heavy Horseman; Imperial Horseman | Map movement and battlefield performance remain contextual. |
| Capital sacred | Red Guard | Capital-only, sacred, and expensive in gold relative to ordinary infantry. |

## T'ien Ch'i guaranteed mage and priest floor

The repeatable non-capital floor is N1 from Apothecaries, E1S1 from Imperial Geomancers, H2 from Ministers of Rituals, and W1H1 from Masters of the Way before their random. Ministers of Magic have no fixed magical path but receive one guaranteed four-path draw. Alchemists of the Five Elements begin at N1 and receive one guaranteed elemental draw.

This floor matters more than the theoretical ceiling. Celestial Servant is guaranteed on an Imperial Geomancer, and Thousand Year Ginseng is guaranteed on an N1 recruit once researched and funded. Many other national spells require a capital mage or a rare two-path result.

## Master of the Way random portfolio

A Master of the Way has W1H1 and one guaranteed draw from Air, Water, Astral, Nature, or Glamour. Each result is one fifth of the portfolio: A1W1H1, W2H1, W1S1H1, W1N1H1, or W1G1H1.

This makes W2 repeatable in probability but not guaranteed on a particular purchase. It also spreads useful search and support roles across one recruitment record. Recruitment plans should use the 20% branches as expected distributions over many recruits, never as a promise for the next mage.

## Minister of Magic random portfolio

A Minister of Magic receives one guaranteed draw from Air, Water, Earth, or Astral, followed by an independent 10% draw from the same four paths. The first draw gives each path a 25% share. Across both rolls, a particular path appears with probability 26.875%; a doubled result in one path occurs in 2.5% of all Ministers, and two distinct level-one paths occur in 7.5%.

Those aggregate numbers distinguish common single-path researchers from rare cross-path or level-two results. The individual named combination must still be recorded. A strategy that needs W1E1, for example, cannot budget every Minister as though the 1% unordered W/E result were already present.

## Alchemist of the Five Elements random portfolio

An Alchemist of the Five Elements begins at N1, receives one guaranteed draw from Fire, Air, Water, or Earth, and then has an independent 10% draw from Fire, Air, Water, Earth, or Nature. Each elemental path is the first result 25% of the time and appears somewhere in the two rolls 26.5% of the time. The secondary Nature result raises the mage to N2 in 2% of recruits.

The guaranteed elemental draw is the reliable feature; the second draw is a portfolio bonus. Two-path elemental thresholds, double elemental levels, and N2 should be assigned only after the recruit exists.

## Imperial Alchemist capital portfolio

An Imperial Alchemist begins at F1A1W1E1N2, then uses the same guaranteed elemental draw and independent 10% five-element draw as the ordinary Alchemist. This guarantees one elemental path at level two. A second roll can produce another elemental increase or N3, but none should be scheduled before recruitment reveals the result.

The base form already guarantees N2 rituals and W1E1 Living Mercury from the capital. Its breadth is powerful on paper, but each purchase also consumes four commander recruitment points and a capital turn that could have produced a Celestial Master, Prince General, or sacred troop capacity.

## Celestial Master capital portfolio

A Celestial Master begins at A1W2E1S1G1H2, receives one guaranteed draw from Air, Water, Astral, Nature, or Glamour, and has an independent 10% draw from the same pool. The fixed paths guarantee Internal Alchemy and the A1S1 threshold for Celestial Hounds. A random Air increase reaches A2 for Call Celestial Soldiers; across the two rolls, at least one Air increase occurs in 21.6% of recruits.

This record combines priesthood, high recruitment cost, four commander recruitment points, cross-path magic, and rare depth. It should be bought for a named portfolio need, not merely because it has the broadest row.

## T'ien Ch'i native path boundary

The national roster natively touches all seven paths named by the manual, but access is uneven.

| Access class | Reliable examples | Important limitation |
| --- | --- | --- |
| Guaranteed outside the capital | N1; E1S1; W1H1; H2 | Mostly low-path access. |
| Random outside the capital | A, W, E, S, N, G; rare doubled or cross-path results | A possible result is not an owned caster. |
| Guaranteed in the capital | F1A1W1E1N2; A1W2E1S1G1H2 | Capital queue and recruitment-point pressure. |
| Rare capital depth | Random increases on Imperial Alchemist and Celestial Master | Exact result must be observed after recruitment. |
| Hero-only additions | Death and higher Astral on named heroes | Hero arrival is not a repeatable schedule. |

Death is not part of the repeatable recruitable mage floor shown in the roster. A hero record does not convert it into dependable national access.

## T'ien Ch'i national spell and ritual reconciliation

The pinned restriction records contain ten T'ien Ch'i spells: one battle spell and nine rituals.

| Spell | School and level | Path | Printed cost or type |
| --- | --- | --- | --- |
| Celestial Chastisement | Evocation 5 | S3 | Battle spell, 20 fatigue |
| Celestial Servant | Conjuration 1 | E1S1 | 1 Earth gem |
| Ambush of Tigers | Conjuration 3 | N2 | 9 Nature gems |
| Herd of Buffaloes | Conjuration 3 | N2 | 8 Nature gems |
| Celestial Hounds | Conjuration 4 | A1S1 | 2 Air gems |
| Thousand Year Ginseng | Construction 4 | N1 | 4 Nature gems |
| Internal Alchemy | Alteration 5 | W2S1 | 5 Water gems |
| Living Mercury | Enchantment 5 | W1E1 | 6 Water gems |
| Contact Huli Jing | Conjuration 6 | N2 | 30 Nature gems |
| Call Celestial Soldiers | Conjuration 6 | A2S1 | 15 Air gems |

Names, schools, levels, requirements, and costs are source facts. Exact variable summon counts, battlefield targeting, friendly-fire behaviour, shape changes, and practical combat value remain observation questions unless the manual explicitly prints them.

## T'ien Ch'i ritual access from repeatable mages

| Ritual | Access from roster | Scheduling boundary |
| --- | --- | --- |
| Celestial Servant | Guaranteed Imperial Geomancer E1S1 | Earliest national ritual; still costs a mage-turn and Earth gem. |
| Thousand Year Ginseng | Guaranteed N1 recruit | Does not itself create every later Nature threshold. |
| Ambush of Tigers; Herd of Buffaloes; Contact Huli Jing | Guaranteed Imperial Alchemist N2; 2% N2 ordinary Alchemist | Capital access is reliable; non-capital access is rare. |
| Internal Alchemy | Guaranteed Celestial Master W2S1 | Capital-only guaranteed caster. |
| Celestial Hounds | Guaranteed Celestial Master A1S1; rare A/S Minister | Ordinary two-path access is an uncommon result. |
| Living Mercury | Guaranteed Imperial Alchemist W1E1; rare W/E ordinary random | Capital access is reliable. |
| Call Celestial Soldiers | Celestial Master needs an Air increase to reach A2S1 | At least one Air random occurs on 21.6% of Celestial Masters. |
| Celestial Chastisement | Needs S3 | No ordinary recruit guarantees S3; capital randoms, boosters, or other bridges are needed. |

This table separates national availability from legal casting. Researching a national spell before its caster and treasury exist can create no deployable package.

## T'ien Ch'i capital gem economy

The capital produces A1, W1, E1, and S2 each month. That income supports several national paths but produces no Nature gems, even though four national rituals use Nature. Site searching, trade, events, Pretender design, or other documented income must therefore supply the Nature treasury; national restriction alone does not fund it.

Separate ledgers should be kept for Air, Water, Earth, Astral, and Nature. The first three pay for national rituals directly, Astral supports other national magic and infrastructure, and Nature has a structural mismatch between ritual demand and starting site income.

## T'ien Ch'i national item boundary

Four items have explicit T'ien Ch'i links in the pinned data and manual descriptions.

| Item | National relation | Requirement |
| --- | --- | --- |
| Sword of the Five Elements | Restricted national item | Construction 3, F1W1 |
| Armor of the Five Elements | Restricted national item | Construction 3, E1A1 |
| Chi Shoes | National rebate | Construction 3, A1 |
| Jade Armor | National rebate | Construction 7, W2E1 |

The manual prints two Fire and two Water gems for the Sword, and two Earth and two Air gems for the Armor. The rebate fields establish that Chi Shoes and Jade Armor are discounted for T'ien Ch'i, but the final displayed live cost and interaction with other forge modifiers remain unresolved here.

## T'ien Ch'i hero records

The pinned nation records name three heroes: Ho Hsien-Ku, Lu Tung-Pin, and Li T'ieh-Kuai. Their corresponding forms provide A1N2; F1A1W2S3H2; and A2S2D2 respectively, with the first two marked sacred in the structured snapshot.

These records document possible capabilities, including hero-only Death and direct S3. They do not make those paths repeatable. Arrival timing, event conditions, alternate forms, and live behaviour remain unresolved unless an official source or versioned observation establishes them.

## T'ien Ch'i patch reconciliation

The current baseline is Dominions 6.36, released on 17 August 2026. The local official patch ledger was searched through its 6.35 endpoint, and the separate official 6.36 announcement was checked; neither supplies a direct Middle Age T'ien Ch'i or named-roster correction for this chapter. This negative search is not proof that no indirect engine change matters; it means only that no nation-specific correction can safely be attached from the available named notes.

The structured object snapshot remains pinned to 6.35, so the manual and official 6.36 ledger take precedence where they conflict. Any later discrepancy should be recorded as a new source-reconciliation issue rather than silently normalised.

## T'ien Ch'i opening priorities

1. Identify whether each fort site is limited by gold, resources, recruitment points, or commander turns.
2. Use the cheapest troop line that answers the observed independent province instead of defaulting to Imperial equipment.
3. Add scouting and mundane leadership without spending mage turns on jobs a General or Scout can perform.
4. Record every random mage's final paths before assigning research, search, forge, ritual, or combat duty.
5. Protect the capital queue for the specific Red Guard, Prince General, Imperial Alchemist, or Celestial Master requirement that the plan names.
6. Track Nature demand separately because the capital sites supply no Nature gems.

These are planning controls, not tested expansion prescriptions. Exact party sizes, formations, scripts, and casualty expectations remain open.

## T'ien Ch'i recruitment packages to evaluate from reports

### Cheap foot and missile package

Footmen and Archers preserve gold for forts and mages, but their weapons, armour, shields, and morale differ. The package should be selected against the reported province rather than treated as one undifferentiated mass.

### Ministry middle line

Ministry Guardsmen and Footmen trade more gold, resources, and recruitment points for stronger equipment and morale. Glaives, spear-and-shield, and man catchers have different target profiles; none is a universal upgrade.

### Imperial protected line

Imperial Footmen, City Guards, Guards, Archers, and Crossbowmen offer heavier profiles at greater production cost. The right mixture depends on local resources, enemy armour and shields, missile conditions, and whether the fort must also produce cavalry.

### Cavalry response group

Horsemen, Heavy Horsemen, and Imperial Horsemen offer three price and equipment tiers. Map speed does not by itself establish expansion safety or battlefield value, so route, fatigue, formation, and target selection remain report-dependent.

### Capital Red Guard reserve

Red Guards are sacred, capital-only, and cost fifty gold. A bless and capital allocation should solve a defined problem before the nation pays that opportunity cost.

## T'ien Ch'i research response tree

### Branch A: guaranteed low-path utility

Construction 4 reaches Thousand Year Ginseng for N1, while Conjuration 1 reaches Celestial Servant for E1S1. This branch uses guaranteed non-capital paths, but its value still depends on gems, mage-turns, and what the summoned or transformed asset contributes.

### Branch B: capital cross-path rituals

Alteration 5 Internal Alchemy, Enchantment 5 Living Mercury, and Conjuration 4 Celestial Hounds align with guaranteed capital mage paths. The capital must recruit those casters before the research becomes an operational package.

### Branch C: Nature summons

Conjuration 3 opens Ambush of Tigers and Herd of Buffaloes; Conjuration 6 opens Contact Huli Jing. Imperial Alchemists guarantee N2, but the capital provides no Nature income. Research and treasury therefore have to be planned together.

### Branch D: higher Air and Astral thresholds

Conjuration 6 Call Celestial Soldiers requires A2S1, normally a Celestial Master with an Air increase. Evocation 5 Celestial Chastisement requires S3 and is not guaranteed on ordinary recruits. This branch should wait for an actual caster or a documented bridge.

## T'ien Ch'i battlefield packages

### Conventional line with separate command

A General leads the selected infantry or cavalry while mages preserve their actions for spells. This separation is useful only if the army has enough mundane leadership and the chosen line answers the enemy's protection, weapons, mobility, and numbers.

### Mixed missile and protected line

Archers or crossbowmen operate behind a shielded or armoured line. Range, weather, friendly obstruction, enemy shields, armour, and closing speed determine value; the source tables cannot settle those battlefield outcomes.

### Broad-mage support group

Recorded Ministers, Alchemists, Geomancers, and Masters of the Way are selected for actual paths rather than names. This prevents a nominally broad squad from arriving without the cross-path or depth the script assumes.

### Capital ritual-supported force

Imperial Alchemists or Celestial Masters turn researched national rituals into assets. The full package must include the capital recruitment turn, research, gem source, ritual turn, commander, and route to the front.

## T'ien Ch'i Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Economy and infrastructure | Funds forts, laboratories, commanders, and a large conventional roster | Gold does not create local resources or extra capital queue capacity. |
| Nature-income bridge | Supports the national Nature ritual suite | A path without site income, search, trade, or gems is not a treasury. |
| High-path bridge | Supplies reliable S3, deeper Air, or another missing threshold | Native random access should be counted before paying twice for it. |
| Sacred design | Supports Red Guards and sacred commanders or summons | Most ordinary troops are not sacred. |
| Awake expander | Supplies early province-taking while human infrastructure develops | Afflictions, counters, scales, and opportunity cost remain map-dependent. |

No exact design is endorsed without settings, map, opponents, legal chassis, and a versioned test or game record.

## T'ien Ch'i matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Footprint, missiles, cavalry, protected lines, and reachable area effects | Buying the most expensive Imperial record by default. |
| Heavy armour | Crossbows, high-damage weapons, buffs, fatigue, and armour-answering magic | Assuming every glaive or spell solves every protection value. |
| Fast flankers or flyers | Guards, reserves, mage spacing, and local response forces | Exposing rare random or capital mages in one rear cluster. |
| High Defence, ethereal, or Glamour targets | Area effects, magic weapons, attack support, and control | Treating broad national magic as proof that the required caster exists. |
| High Magic Resistance or mindless units | Conventional pressure, buffs, summons, and non-MR effects | Building the battle around a single Astral resistance check. |
| Raiding and dispersed pressure | Scouts, fortified cities, Eunuchs, local troops, and reserve commanders | Concentrating every useful recruit in the capital. |
| Gem denial | Guaranteed low-path tools and mundane roster depth | Researching a ritual tree that the treasury cannot fund. |

## Monthly T'ien Ch'i audit

- Is each fort limited by gold, resources, recruitment points, or commander turns?
- Is every random mage labelled by final paths and assigned a role that uses them?
- Are mundane commanders available where using a mage would lose research or ritual tempo?
- Is the capital queue reserved for a named Red Guard, Prince General, Imperial Alchemist, or Celestial Master job?
- Are Air, Water, Earth, Astral, and Nature balances tracked separately?
- Does each national ritual have research, a legal caster, gems, a mage-turn, and a delivery plan?
- Is conscription being treated as confirmed without inventing its exact composition or scaling?
- Does the troop mix answer the reported armour, weapons, missiles, mobility, and morale?
- Are hero paths excluded from schedules that must be repeatable?
- Has any 6.35 structured field been checked against the 6.36 manual and patch ledger before publication?

## T'ien Ch'i unresolved evidence boundary

The following claims remain open:

1. exact expansion-party sizes, formations, scripts, and casualty ranges for every infantry, missile, cavalry, and Red Guard package;
2. exact Eunuch conscription composition, growth rate, interaction with province defence, and live display;
3. live 6.36 presentation and timing of every random-magic result;
4. summon counts or composition where the manual does not print a fixed result;
5. Celestial Chastisement targeting, resistance, friendly-fire risk, and battlefield value;
6. Internal Alchemy transformation details and persistence beyond the printed ritual description;
7. Living Mercury, Celestial Hound, Celestial Soldier, Huli Jing, tiger, buffalo, and Celestial Servant scripting and combat behaviour;
8. final displayed rebate costs for Chi Shoes and Jade Armor under combined forge modifiers;
9. hero arrival timing, alternate forms, and live behaviour;
10. specific Pretender designs, blesses, matchups, and map performance.

These are evidence gaps, not invitations to guess. No runtime test or new test asset was prepared during this unit. R-047, R-058, and the wider hands-on testing queue remain parked until testing is explicitly resumed.

# Part XXVII: Middle Age Machaka, Reign of Sorcerors

## Machaka one-page command brief

Middle Age Machaka combines cheap human troops, heavy hoplites, forest recruitment, poisonous spider cavalry, assassins, and a broad mage corps using Fire, Earth, Death, Nature, Glamour, and Holy magic. Its capital contains two sites producing five gems each month and most of its specialised spider troops and mages. Ordinary forts still recruit the Sorcerer, which is the key repeatable ritual chassis because every one has F1 D1 N2 G1 plus a guaranteed random level.

The basic plan is:

- use the cheap human roster and hoplites according to the local gold, resource, and recruitment-point budget;
- recruit Witch Doctors from forests where their low research penalty is acceptable and their F1 D1 N1 access has a real job;
- treat Sorcerers as recorded five-way portfolios rather than assuming the path needed next will appear;
- protect the capital queue for Black Sorcerers, Anansi, Spider Sorceresses, Bane Spiders, and sacred spider forces;
- keep the Nature ritual budget separate from the capital's Fire, Earth, Nature, and Glamour income;
- use scouts, spies, forest recruitment, and assassins to improve information and apply pressure without pretending their live outcomes are guaranteed.

Machaka's main strategic problem is coordination. The roster offers many specialised pieces, but its strongest spider units, deepest mages, and best cross-paths are capital-bound or random-dependent. A plan fails when it counts every possible random as one mage, spends the capital queue on unrelated jobs, or researches a ritual without its gems and legal caster.

## Machaka evidence and ruleset

This chapter covers unmodded Middle Age Machaka on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, recruitment locations, printed paths, national summary, mounts, sites, and ritual tables. Nation ID 76, site records, random masks, hero assignments, spell restrictions, disabled rows, and item rebates are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The sources do not prove current random-path presentation, expansion results, dominion-summon timing, assassin outcomes, web or poison behaviour, mount survival, final forge costs, or hero arrival timing. Those remain unresolved. No runtime test, replay, save, or new test asset was used for this dossier.

## Machaka conversion chain

```text
cheap human bodies, hoplites, forest recruits, and five capital gems
-> expansion forces, borders, and recruitment centres
-> recorded Sorcerer and capital-mage portfolios
-> research plus separate Nature, Death, Earth, Fire, and Glamour budgets
-> national rituals, forging, battlefield support, and spider pressure
-> surviving armies, reserves, sieges, and claims
```

The fragile arrows are capital time, Nature-gem accumulation, and cross-path access. The nation can possess many paths across its roster while still lacking the one mage, gem stock, laboratory, or safe turn needed for a particular job.

## Machaka national rules that shape planning

| Rule or asset | Source-backed fact | Planning consequence |
| --- | --- | --- |
| Prefers Heat 2 | The manual states that Machaka prefers Heat 2. | Climate preference is an economic and fatigue input, not a complete scales prescription. |
| Heat limit +1 | Pretender design may move Heat one step beyond the ordinary limit. | The value depends on the entire design and cannot be judged in isolation. |
| Standard Forts | Machaka uses the standard fort family. | Fort timing still competes with laboratories, temples, troops, and commanders. |
| Forest recruitment | Witch Doctors and Spider Archers are available in all forests. | Forest forts can add national options, but only when geography and infrastructure justify them. |
| Capital spider complex | Most specialised spider troops and four major commander types are home-site recruits. | Capital commander and troop capacity must be budgeted separately. |
| Intelligence tools | Scouts, a spy-priest, Anansi spies, patrolling priests, and assassins are printed in the roster. | Better information is possible, but detection and assassination outcomes remain engine and matchup questions. |

## Machaka capital sites and recruitment geography

| Site | Verified fields | Recruitment consequence |
| --- | --- | --- |
| God Forest, site 60 | F1 N1 | Black Hunter and Spider Archer troop records; Voice of the Hunters commander |
| God Mountain, site 61 | E2 G1; ritual-range bonus 1 | Spider Warrior; Black Sorcerer, Anansi, Spider Sorceress, and Bane Spider |

The two sites produce F1 E2 N1 G1, five gems per month. They produce no Air, Water, Astral, Death, or Blood gems. This matters because the mage roster has strong Death access but no capital Death income, while all three confirmed national rituals consume Nature gems.

Witch Doctors and Spider Archers also have forest recruitment outside the capital. Other spider units are not generalised into forest recruits without a source field.

## Complete Machaka commander membership

| Commander | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Machaka Scout | 35 | 3 | 1 | Forts |
| Machaka Chief | 55 | 2 | 1 | Forts |
| Machaka Commander | 95 | 27 | 1 | Forts |
| Spider Lord | 125 | 25 | 1 | Forts |
| Eye of the Lord | 90 | 4 | 1 | Forts |
| Voice of the Lord | 160 | 2 | 2 | Forts |
| Ear of the Lord | 150 | 3 | 2 | Forts |
| Witch Doctor | 110 | 1 | 2 | Forts and all forests |
| Sorcerer | 300 | 1 | 2 | Forts |
| Voice of the Hunters | 230 | 33 | 1 | Capital only |
| Bane Spider | 150 | 38 | 2 | Capital only |
| Spider Sorceress | 230 | 1 | 2 | Capital only |
| Anansi | 280 | 1 | 4 | Capital only |
| Black Sorcerer | 325 | 6 | 4 | Capital only |

Nine ordinary and five capital records reconcile to fourteen commanders. The two-point Sorcerer is available outside the capital; the four-point Anansi and Black Sorcerer compete directly for the home queue.

## Complete Machaka troop membership

| Troop | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Pygmy | 5 | 2 | 2 | Forts |
| Machaka Militia | 7 | 2 | 3 | Forts |
| Machaka Archer | 10 | 3 | 9 | Forts |
| Machaka Warrior, spear and javelin | 10 | 3 | 9 | Forts |
| Machaka Warrior, Machaka spear | 10 | 4 | 9 | Forts |
| Spider Archer | 12 | 4 | 20 | Capital and all forests |
| Machaka Hoplite | 14 | 27 | 18 | Forts |
| Spider Rider | 25 | 4 | 9 | Forts |
| Spider Knight | 30 | 25 | 21 | Forts |
| Spider Warrior | 20 | 36 | 31 | Capital only |
| Black Hunter | 100 | 36 | 31 | Capital only |

Nine ordinary or forest-accessible records and two capital-only records reconcile to eleven troops. The two Machaka Warrior entries are distinct equipment records and should remain separate in tables and search results.

## Machaka troop jobs

| Unit | Source-backed role | Important limit |
| --- | --- | --- |
| Pygmy | Extremely cheap short-bow body | Size, low Hit Points, low Morale, and low combat skills sharply limit what five gold buys. |
| Machaka Militia | Cheap spear frontage | Low Morale and light protection make it a screen rather than a durable line. |
| Machaka Archer | Low-cost conventional missile unit | Range, armour, shields, weather, and friendly obstruction decide results. |
| Machaka Warriors | Light spear line with either javelin or dedicated spear profile | Light protection makes positioning and target choice important. |
| Machaka Hoplite | Heavily armoured spear line | Twenty-seven resources, encumbrance, and movement limit mass production and redeployment. |
| Spider Archer | Forest-accessible poison-bow unit | Twenty recruitment points and poison interaction require a target-specific reason. |
| Spider Rider | Mobile mixed spear and bow rider | Rider and mount outcomes are not inferred from the roster entry. |
| Spider Knight | Armoured spider cavalry | Gold, resources, and recruitment points compete with hoplites and commanders. |
| Spider Warrior | Capital stealth troop with two weapons | Capital-only, resource-heavy, and dependent on a protected delivery plan. |
| Black Hunter | Expensive sacred hunter-spider cavalry | One hundred gold and capital-only recruitment make every loss consequential. |

## Machaka commander and mage portfolio

| Commander | Paths or ability | Main source-backed jobs | Recruitment warning |
| --- | --- | --- | --- |
| Machaka Scout | Stealth 40; forest and mountain survival | Scouting and route information | Information depends on survival and coverage. |
| Machaka Chief | Leadership 75 | Cheap mundane command | Lightly protected. |
| Machaka Commander | Leadership 100 | Armoured line command | Twenty-seven resources compete with hoplites. |
| Spider Lord | Leadership 100; Great Spider mount | Mobile command | Mounted combat and mount survival remain runtime questions. |
| Eye of the Lord | H1; Patrol Bonus 15 | Patrolling and low priest work | Patrol outcomes depend on local stealth and force strength. |
| Voice of the Lord | H2; Leadership 100 | Medium priest and army command | Costs two recruitment points. |
| Ear of the Lord | G1 H1; Stealth 60; Spy | Intelligence, priest work, and low Glamour access | Spy reports and detection remain observation-dependent. |
| Witch Doctor | F1 D1 N1; Research -4 | Forest recruitment, low cross-path work, site searching, and forging | The research penalty must be justified by a real job. |
| Sorcerer | F1 D1 N2 G1 plus one random | Main ordinary-fort mage, national rituals, research, and mixed magic | Record the five-way random before assigning a specialised role. |
| Voice of the Hunters | H1; sacred; Hunter Spider mount | Capital sacred command | Competes with all other capital commanders. |
| Bane Spider | G1; Stealth 50; assassin; Scale Walls | Assassination and covert pressure | Outcomes, patience value, and wall interaction remain live questions. |
| Spider Sorceress | F1 E1 D1 G1 plus one random; dominion summoner | Capital mixed magic | Dominion-summon timing and output are unresolved. |
| Anansi | D1 N1 G2 plus two random slots; spy; heretic | Deep Glamour, spying, and mixed ritual support | Four recruitment points and a second roll that triggers only 10% of the time. |
| Black Sorcerer | F2 E2 D1 G1 plus two random slots | Deep capital magic, forging, and cross-path work | Four recruitment points; the secondary roll triggers only 10% of the time. |

## Reading the Sorcerer random

Every Sorcerer has F1 D1 N2 G1 and one guaranteed level from a five-way F/E/D/N/G mask.

| Branch | Final relevant paths | Probability |
| --- | --- | ---: |
| Fire | F2 D1 N2 G1 | 20% |
| Earth | F1 E1 D1 N2 G1 | 20% |
| Death | F1 D2 N2 G1 | 20% |
| Nature | F1 D1 N3 G1 | 20% |
| Glamour | F1 D1 N2 G2 | 20% |

Every Sorcerer can cast Herd of Elephants and God Brood once the research and Nature gems exist. Only particular branches deepen Fire, Death, Nature, or Glamour, and only the Earth branch supplies Earth on this chassis.

## Reading the Spider Sorceress random

Every Spider Sorceress has F1 E1 D1 G1 and one guaranteed F/E/D level. The three outcomes are F2, E2, or D2 at one third each. The printed dominion-summoner ability is recorded, but no monthly Great Spider rate or current timing is assigned without observation.

## Reading the Anansi randoms

Every Anansi has D1 N1 G2. The first random is one guaranteed D/N/G level; the second is an independent 10% F/E/D/N/G level.

- the primary result is D2, N2, or G3 at one third each;
- 90% receive no second level;
- each named secondary path appears on 2% of recruits;
- a secondary Earth result is the only pinned route for an Anansi to combine E1 with its fixed N1;
- rare secondary results are possibilities, not a dependable recruitment schedule.

## Reading the Black Sorcerer randoms

Every Black Sorcerer has F2 E2 D1 G1. The first random is one guaranteed F/E/D level; the second is an independent 10% F/E/D/N/G level.

- the primary result reaches F3, E3, or D2 at one third each;
- 90% receive no secondary level;
- each named secondary path appears on 2% of recruits;
- Nature exists only through that rare secondary slot on this chassis;
- the capital queue and four recruitment-point cost are part of every probability plan.

## Machaka native path boundary

| Path | Repeatable access | Boundary |
| --- | --- | --- |
| Fire | Fixed F1 Witch Doctor and Sorcerer; F1 Spider Sorceress; F2 Black Sorcerer | Random branches reach F2 or F3, but the deepest access is capital-bound. |
| Earth | Fixed E1 Spider Sorceress and E2 Black Sorcerer | Ordinary Sorcerers gain E1 only on their 20% Earth branch. |
| Death | Fixed D1 on all four mage families | Random branches reach D2; the capital produces no Death gems. |
| Nature | Fixed N1 Witch Doctor, N2 Sorcerer, N1 Anansi | Sorcerers reach N3 on one branch; no recruit reaches N4 unaided. |
| Glamour | G1 Ear and Bane Spider; G1 Sorcerer and Spider Sorceress; G2 Anansi and G1 Black Sorcerer | Anansi can reach G3; battlefield and detection behaviour remain unresolved. |
| Holy | H1 Eye, Ear, and Voice of the Hunters; H2 Voice of the Lord | No recruitable H3 priest is established. |
| Air, Water, Astral, Blood | No recruitable mage | Require a Pretender, independents, empowerment, summons, heroes, or another proved bridge. |

## Machaka national ritual reconciliation

| ID | Ritual | School | Requirement | Cost | Printed result |
| ---: | --- | --- | --- | ---: | --- |
| 340 | Herd of Elephants | Conjuration 3 | N2 | 20 Nature gems | Five or more Elephants |
| 341 | God Brood | Conjuration 4 | N2 D1 | 12 Nature gems | Six Hunter Spiders |
| 343 | Weavers of the Wood | Enchantment 5 | N4 | 6 Nature gems | Forest patrol enchantment; one month plus three months per extra gem |

The pinned restriction table also contains disabled spell ID 342 named `xxx`. It is retained as metadata, not presented as a castable ritual. `Herd of Gnus` appears with a pinned Machaka restriction but is absent from the revision-2 age-two ritual table. That mismatch remains unresolved rather than silently adding or deleting a live option.

## Machaka ritual access

Every Sorcerer has N2 D1 and can cast both Herd of Elephants and God Brood after the required research. Witch Doctors do not meet either threshold without a path increase. The Nature branch of the Sorcerer reaches N3, still one level below Weavers of the Wood.

Weavers therefore needs a named bridge such as a booster, empowerment, Pretender, suitable summon, or another verified source of N4. The chapter does not assume that a theoretical item exists in the treasury or that a hero arrives when needed.

## Machaka national item metadata

| Item record | Pinned relation | Requirement | Native access note |
| --- | --- | --- | --- |
| Bane Blade, one-handed | Nation rebate | Construction 3, D1 | All four mage families meet D1. |
| Bane Blade, two-handed | Nation rebate | Construction 3, D1 | Separate equipment record despite the shared name. |
| Totem Shield | Nation rebate | Construction 5, D1 G1 | Sorcerer and the capital mage families meet the cross-path. |
| Spirit Mask | Nation rebate | Construction 5, D2 N1 | A Death-random Sorcerer qualifies; other routes depend on rarer combinations. |
| Kithaironic Lion Pelt | Nation rebate in its second path | Construction 3, N1 E1 | Earth-random Sorcerer qualifies; other native routes are capital-bound or rare. |
| Fever Fetish | Nation rebate | Construction 9, F1 N1 | Witch Doctor and Sorcerer meet the path requirement. |

These are pinned item fields. Exact 6.36 displayed costs and the interaction between nation rebates, forge bonuses, hammers, sites, or other modifiers remain unresolved.

## Machaka hero records

| Fixed name | Unit name | Verified magic | Boundary |
| --- | --- | --- | --- |
| Ainra | Lady of Spiders | F1 E3 D3 G2 | Powerful non-repeatable capital-path expansion; timing unresolved |
| Abasi | Hero | None | Does not add a magic path |
| Yasini | King Triumphant | H3 | Hero-only high priest access |
| Mwaka | Crowned Ape | H1 | Hero record only |
| Mchumba | Ape Oracle | N1 | Hero record only |

Hero paths are not counted in schedules that must work every game. Arrival timing, probability, and live special behaviour are not established by the structured row alone.

## Machaka opening priorities

The opening should maintain three budgets: enough troops to take and hold provinces, enough infrastructure to recruit Sorcerers outside the capital, and enough capital capacity for the specialised spider roster. Five- and seven-gold troops can add bodies cheaply, but low Morale and protection change what those bodies can safely do. Hoplites offer heavy armour at a much higher resource cost.

Exact party sizes and scripts remain open because map settings, scales, opposition, formation, bless, and combat rolls change them. The safe procedure is to record casualties, identify whether gold, resources, recruitment points, or commander turns are binding, and change the next force accordingly.

## Machaka recruitment packages to compare

### Cheap screen and supported line

Pygmies, Militia, Archers, or light Warriors can cover cheap frontage and missiles while hoplites or spider units perform a narrower job. This preserves gold only when low Morale and light protection do not cause the screen to collapse before the expensive element can work.

### Hoplite centre

Machaka Hoplites provide the roster's conventional heavy line. Their fourteen-gold price is modest, but twenty-seven resources and eighteen recruitment points can make local production the real limit. Armour, fatigue, mobility, and enemy damage still decide whether the line fits the battle.

### Forest recruitment package

A forest fort can recruit Witch Doctors and Spider Archers. This can spread commander production and add poison missiles, but a forest is not automatically a good fort site. Income, resources, position, construction cost, laboratory timing, and the need for other mages remain part of the decision.

### Spider cavalry package

Spider Riders and Spider Knights combine riders with Great Spiders, while Black Hunters use Hunter Spiders and are sacred. Their speed, poison, webs, armour, gold cost, and recruitment demands point toward specialised use. Rider-and-mount damage, routing, targeting, and survival remain runtime questions.

### Capital stealth package

Spider Warriors, Bane Spiders, Anansi, and supporting scouts or spies can create covert pressure. Stealth values and printed abilities are facts; detection, assassination, siege entry, and campaign effect depend on the engine state and the opponent's precautions.

## Machaka research response tree

### Branch A: Conjuration and national bodies

Conjuration 3 opens Herd of Elephants for every Sorcerer with twenty Nature gems. Conjuration 4 opens God Brood for twelve Nature gems. The choice is not just research level: the army needs the correct body, enough gems, a mage-turn, command, and a route to the front.

### Branch B: low-path battlefield support

Witch Doctors, Sorcerers, and capital mages cover several low Fire, Earth, Death, Nature, and Glamour thresholds. Research should answer a named problem—protection, damage, fatigue, resistance, mobility, or control—using the paths actually recruited. No universal opening tree is claimed.

### Branch C: Construction and discounted items

Construction 3 reaches both Bane Blade records and Kithaironic Lion Pelt. Construction 5 reaches Totem Shield and Spirit Mask. Fever Fetish sits at Construction 9. A discount is valuable only when the item has a legal forger, affordable gems, a bearer, and a job worth the forge turn.

### Branch D: Weavers of the Wood

Enchantment 5 unlocks Weavers of the Wood, but no recruitable mage reaches N4 unaided. Researching it before naming the bridge produces a dead endpoint. Its detection, interception, added-spider combat, and caster-departure behaviour remain bound to the printed description until runtime evidence is resumed.

## Machaka battlefield packages

### Conventional line with mage support

Hoplites or selected light infantry hold space while Sorcerers or Witch Doctors use spells their actual paths support. Mundane commanders should carry leadership where doing so preserves mage actions and research. The exact formation and script must respond to the enemy.

### Missile and poison pressure

Machaka Archers, Pygmies, Spider Archers, and mounted bows provide several missile profiles. Armour, shields, range, weather, poison resistance, friendly obstruction, and closing speed determine which profile has value. The roster does not prove a fixed ratio.

### Mobile spider wing

Spider Riders, Spider Knights, or Black Hunters can form a faster wing around a slower centre. Mount size, rider protection, enemy reach, morale, terrain, and formation influence the result. This remains a package to evaluate, not a guaranteed flank solution.

### Capital mixed-mage group

Spider Sorceresses, Anansi, and Black Sorcerers bring useful fixed cross-paths and different random depth. Each mage should be labelled by final paths, given gems that match its script, and protected according to its cost. A list of possible paths is not a deployable squad.

## Machaka information and pressure network

Machaka Scouts supply conventional stealth. Ears of the Lord and Anansi add spies, Eyes of the Lord add patrol strength, and Bane Spiders add assassination. Weavers of the Wood prints a strong forest-patrol and invisible-detection effect while maintained by its caster.

These tools form an information network only when placed and protected. Spy report detail, patrol detection, invisible detection outside the ritual, assassin targeting, and counter-assassination remain unresolved live behaviour. The dossier therefore recommends coverage and record-keeping without inventing success rates.

## Machaka Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Nature-depth bridge | Supplies dependable N4 or supports the national ritual treasury | A path alone does not create Nature gems or a safe ritual turn. |
| Missing-path bridge | Adds Air, Water, Astral, Blood, or another absent threshold | Native Fire, Earth, Death, Nature, and Glamour access should be counted first. |
| Economy and infrastructure | Funds forts, laboratories, Sorcerers, and capital specialists | Gold does not create local resources or additional capital recruitment points. |
| Sacred design | Supports Black Hunters, Voices of the Hunters, and other sacred assets | Most of the ordinary roster is not sacred. |
| Awake expander | Supplies early province-taking while the recruitment system develops | Afflictions, counters, scales, and opportunity cost remain map-dependent. |

No exact design is endorsed without settings, map, opponents, legal chassis, and versioned evidence.

## Machaka matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Missiles, protected frontage, elephants, spiders, and reachable area effects | Buying only premium capital troops. |
| Heavy armour | High-damage attacks, buffs, fatigue, poison where applicable, and armour-answering magic | Assuming ordinary arrows or light spears solve every protection value. |
| Fast flankers or flyers | Guards, reserves, mage spacing, and mobile spiders | Leaving expensive capital mages in one exposed rear cluster. |
| Poison-resistant or poison-immune forces | Conventional weapons, hoplites, non-poison magic, and different summons | Paying for poison as if resistance were irrelevant. |
| High Defence, ethereal, or Glamour targets | Area effects, magic weapons, attack support, control, and verified counters | Treating national Glamour access as proof that every perception problem is solved. |
| Raiding and covert pressure | Scouts, spies, patrol priests, Bane Spiders, forest forts, and reserves | Assuming stealth or assassination succeeds automatically. |
| Gem denial | Mundane roster depth and low-gem support | Researching national rituals that the Nature treasury cannot fund. |

## Monthly Machaka audit

- Is each fort limited by gold, resources, recruitment points, or commander turns?
- Is every Sorcerer and capital random mage labelled by final paths?
- Is the capital queue reserved for a named commander or troop job?
- Are mundane commanders available where using a mage would lose research or ritual tempo?
- Are Fire, Earth, Death, Nature, and Glamour gem balances tracked separately?
- Does each planned ritual have research, a legal caster, gems, a mage-turn, and delivery?
- Are forest recruits being used only where the forest fort itself is worthwhile?
- Does the troop mix answer the reported armour, missiles, mobility, poison resistance, and morale?
- Are hero paths excluded from schedules that must be repeatable?
- Has any pinned-only field been kept separate from current observed behaviour?

## Machaka unresolved evidence boundary

The following remain open:

1. exact expansion-party sizes, formations, scripts, and casualty ranges;
2. live 6.36 random-path display and timing for all four random-mage families;
3. Spider Sorceress dominion-summon timing, rate, and conditions;
4. the current player-facing availability of the structured-only Herd of Gnus restriction;
5. Weavers of the Wood detection, interception, added-spider, duration, and caster-movement edge cases;
6. web, poison, rider, mount, assassination, Scale Walls, and stealth interactions;
7. exact displayed item costs and rebate stacking;
8. hero arrival timing and live special behaviour;
9. specific Pretender designs, blesses, matchups, and map performance;
10. R-047, R-058, and all other parked engine-dependent investigations.

These are evidence gaps, not invitations to guess. Runtime testing and preparation of new test assets remain paused.

# Part XXVIII: Middle Age Shinuyama, Land of the Bakemono

## Shinuyama one-page command brief

Middle Age Shinuyama combines very cheap Bakemono, stealthy bandits, amphibious Kappa, heavily armed Dai Bakemono, large O-bakemono, assassins, and three recruitable mage families using Fire, Water, Earth, Death, Nature, and Holy magic. Its capital site produces five gems each month, weighted toward Death. The nation has no sacred troop line in the manual, but it has an unusually large catalogue of twenty-one national Conjuration rituals.

The basic plan is:

- use the cheap Bakemono records for bodies, missiles, and terrain recruitment without pretending that low price removes their Morale and protection limits;
- add Dai Bakemono or O-bakemono when their higher gold, resources, and recruitment points answer a specific target;
- use highland and mountain forts to spread the three named Bakemono commander lines and light troop production;
- use Kappa recruitment from land or underwater forts when amphibious access matters;
- record every Shaman, Uba, and Sorcerer's final paths before assigning research, forging, site searching, ritual, or battle duty;
- separate the Nature and Air ritual plans from the capital gem income, which supplies neither path;
- treat summons as a ladder of specific bodies and mages, not one automatic late-game solution.

Shinuyama's main strategic problem is conversion. It has broad recruitable magic and a deep summon catalogue, but many rituals require Air or Nature gems the capital does not produce, a random path, or a high threshold reached by only a small share of very expensive Sorcerers. A successful plan joins the roster, actual mage results, research, gems, commander time, and delivery into one package.

## Shinuyama evidence and ruleset

This chapter covers unmodded Middle Age Shinuyama on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, terrain recruitment, printed paths, nation summary, capital site, and ritual table. Nation ID 70, site ID 106, random masks, hero assignments, spell restrictions, and the absence of national item rows are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The sources do not prove the exact cave-fort bonus, mountain rebate calculation, current random-path display, variable summon rolls, retinue or shape behaviour, assassin outcomes, hero timing, or battle performance. Those remain unresolved. The official 6.08 ledger carries a Shinuyama/Caelum spell-assignment correction, but its abbreviated metadata is not expanded into guessed wording. No runtime test, replay, save, or new test asset was used for this dossier.

## Shinuyama conversion chain

```text
cheap terrain recruits, large Bakemono, Kappa, and five capital gems
-> provinces, cave or mountain recruitment centres, and protected laboratories
-> labelled Shaman, Uba, and Sorcerer path portfolios
-> research plus separate Fire, Water, Earth, Death, Nature, and Air budgets
-> national summons, battlefield support, mobility, and magical path expansion
-> surviving forces, replacement capacity, sieges, and claims
```

The fragile arrows are Morale, infrastructure, gem mismatch, and mage cost. A 545-gold Sorcerer cannot simultaneously research, search, forge, summon, and lead a ritual plan. Cheap troops do not solve that commander-turn bottleneck.

## Shinuyama national rules that shape planning

| Rule or asset | Source-backed fact | Planning consequence |
| --- | --- | --- |
| Turmoil limit +1 | Pretender design may move Turmoil one step beyond the ordinary limit. | The extra design range is not a recommendation to take it. |
| Magic limit +1 | Pretender design may move Magic one step beyond the ordinary limit. | Research value must be considered with the entire economy and design. |
| Primitive Forts | Shinuyama uses the primitive fort family. | Construction time, administration, defence, and recruitment capacity should be checked rather than assumed equal to standard forts. |
| Cave-fort economy | The manual states that cave forts provide extra gold and resources. | Cave placement can matter, but the exact calculation remains unresolved here. |
| Mountain rebate | The manual states that lesser Bakemono are rebated in mountains. | The live eligible set and displayed amount must not be inferred from the summary alone. |
| No sacred troops | The manual explicitly states that Shinuyama has no sacred troop line. | A bless should justify its commanders, summons, or Pretender rather than assuming a mass sacred army. |
| Many national summons | Twenty-one national Conjuration records are confirmed. | Conjuration offers breadth, but each ritual still needs research, caster, gems, a mage-turn, command, and delivery. |

## Mount Shinuyama and the capital economy

Mount Shinuyama is capital site ID 106. The pinned row carries F1, W1, E1, and D2 gem fields, producing five gems per month. It does not produce Air or Nature gems even though ten of the twenty-one national rituals use Air or Nature as their first path and therefore consume those gems.

The opening ledger should track each path separately. Death supports the largest portion of the summon ladder; Fire, Water, and Earth each fund narrower branches. Air and Nature require site searching, trade, events, Pretender support, or another documented source before their rituals become repeatable purchases.

## Complete Shinuyama commander membership

| Commander | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Bakemono Scout | 30 | 7 | 1 | Forts; all highlands and mountains |
| Noppera-bo | 150 | 5 | 1 | Forts |
| Bandit Leader | 60 | 16 | 1 | Forts |
| Bakemono Chief | 60 | 8 | 1 | Forts; all highlands and mountains |
| Kappa Chief | 70 | 1 | 1 | Land and underwater forts |
| Bakemono General | 115 | 27 | 1 | Forts |
| Shuten-doji | 150 | 1 | 1 | Forts |
| Bakemono Shaman | 115 | 1 | 2 | Forts; all highlands and mountains |
| Uba | 190 | 1 | 2 | Forts |
| Bakemono Sorcerer | 545 | 2 | 4 | Forts |

Ten commander records reconcile. The ordinary roster does not contain a capital-only mage, so additional forts can recruit all three mage families. Terrain access still differs: highlands and mountains add Scout, Chief, and Shaman recruitment, while underwater forts add Kappa Chief recruitment rather than the full land roster.

## Shinuyama commander jobs

| Commander | Source-backed role | Important limit |
| --- | --- | --- |
| Bakemono Scout | Cheap stealth reconnaissance with short bow | Scouting does not itself establish report detail or survival. |
| Noppera-bo | Stealthy, fear-causing assassin with Spirit Sight | Assassin and detection outcomes remain engine-dependent. |
| Bandit Leader | Stealthy leader with Pillage bonus | Pillaging has diplomatic and economic costs as well as immediate output. |
| Bakemono Chief | Cheap terrain-accessible leader | Leadership 50 limits the size of forces it can carry. |
| Kappa Chief | Amphibious commander with recuperation | Underwater access does not prove combat suitability in either environment. |
| Bakemono General | Leadership 100 conventional commander | Gold and resources compete with the troop line. |
| Shuten-doji | Supernatural leader with Sleep Aura, invulnerability, and mixed leadership | Aura, protection, and life-drain outcomes require matchup evidence. |
| Bakemono Shaman | H1 random mage and terrain recruit | Research penalty and one random level constrain efficiency and certainty. |
| Uba | W1 D1 N1 random mage with strong undead leadership | No Holy path; Nature and Water depth depend on the random result. |
| Bakemono Sorcerer | F2 W1 E2 D2 H1 random mage with broad leadership | 545 gold and four recruitment points make every non-mage task expensive. |

## Complete Shinuyama troop membership

| Troop | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Bakemono-Sho, club | 7 | 1 | 3 | Forts; all highlands and mountains |
| Bakemono-Sho, yari | 7 | 2 | 3 | Forts; all highlands and mountains |
| Bakemono Archer, light | 7 | 3 | 3 | Forts; all highlands and mountains |
| Bakemono-Sho, armoured yari | 8 | 6 | 9 | Forts |
| Bakemono Archer, armoured | 8 | 7 | 9 | Forts |
| Bandit, yari | 9 | 11 | 5 | Forts |
| Bandit, wakizashi and bow | 9 | 16 | 5 | Forts |
| Bakemono Warrior | 9 | 8 | 12 | Forts |
| Kappa | 20 | 1 | 8 | Land and underwater forts |
| Dai Bakemono, no-dachi | 25 | 27 | 19 | Forts |
| Dai Bakemono, no-dachi and long bow | 25 | 31 | 19 | Forts |
| O-bakemono | 25 | 2 | 4 | Forts |

Twelve troop records reconcile. Duplicate display names remain separate because equipment, armour, cost, or recruitment demand differs. The three seven-gold light records carry the highland-and-mountain exception; the armoured eight-gold records do not inherit it from their names.

## Shinuyama troop jobs

| Troop | Source-backed role | Important limit |
| --- | --- | --- |
| Light Bakemono-Sho | Extremely cheap club or yari frontage with stealth | Low Hit Points, Morale, protection, and combat skills limit durability. |
| Light Bakemono Archer | Cheap short-bow missile body with stealth | Low Morale and protection make return fire and contact dangerous. |
| Armoured Bakemono | Better-protected yari or bow profiles | Higher resources and recruitment points reduce the mass advantage. |
| Bandits | Stealthy medium infantry with yari or mixed bow profile | Pillage bonus and stealth do not guarantee successful raiding. |
| Bakemono Warrior | Better-skilled wakizashi infantry | Still a small, moderately protected body rather than a heavy line. |
| Kappa | Amphibious, recuperating claw-and-koppo troop | High encumbrance and environment-specific value need battle evidence. |
| Dai Bakemono | Large, armoured heavy infantry with melee or long-bow profile | Twenty-five gold, high resources, and size change frontage and replacement cost. |
| O-bakemono | Large high-Strength great-club attacker with low resource cost | Modest protection and defence expose it while closing and after attacking. |

## Recruitment geography and infrastructure

Shinuyama has three overlapping recruitment networks. Ordinary forts support the full land roster. Highlands and mountains add the light Bakemono troops plus Scout, Chief, and Shaman even where the ordinary fort table is not the controlling route. Land and underwater forts add Kappa and Kappa Chief.

This makes terrain a production question rather than flavour. A cave or mountain position may combine national economic or rebate rules with terrain recruits, while a water-connected fort can create amphibious command. The exact cave bonus, mountain discount, legal fort interaction, and underwater campaign value remain untested; each site should still be judged by income, resources, position, construction time, and intended output.

## Reading the Shinuyama random paths

The pinned masks use Fire 128, Air 256, Water 512, Earth 1024, Astral 2048, Death 4096, Nature 8192, Glamour 16384, and Blood 32768. Mask `5760` is Water, Earth, or Death. Mask `13824` is Water, Death, or Nature.

| Mage | Guaranteed roll | Independent extra roll |
| --- | --- | --- |
| Bakemono Shaman | one W/E/D level, 33.33% each | none |
| Uba | one W/D/N level, 33.33% each | none |
| Bakemono Sorcerer | one W/E/D level, 33.33% each | 10% chance of one W/E/D level |

These are portfolio probabilities, not delivery dates. Several recruits can fail to produce the named path, and the high price and four-point recruitment demand of Sorcerers make large-sample assumptions costly.

## Bakemono Sorcerer probability boundary

Every Sorcerer begins F2 W1 E2 D2 H1. For any one named W/E/D path, the chance that at least one of the two random slots adds that path is 35.56%. The chance that both slots add the same named path is 1.11%. Across the whole second slot, 90% receive no extra level, 3.33% repeat the guaranteed path, and 6.67% add a different W/E/D path.

The rare double-Death result reaches D4 and meets Summon Dai Oni's D4F1 threshold natively. That is a legal possibility in the pinned scheme, not a recruit that can be scheduled to arrive by a particular turn.

## Shinuyama native path boundary

| Path | Repeatable recruitable access | Boundary |
| --- | --- | --- |
| Fire | Sorcerer F2 | No other recruitable mage carries Fire. |
| Air | None | Requires a summon, hero, Pretender, independent, empowerment, or another verified bridge. |
| Water | Uba W1; Sorcerer W1; random depth on all three mage families | Uba or Sorcerer can reach W2; rare Sorcerer reaches W3. |
| Earth | Sorcerer E2; random Shaman or Sorcerer depth | Sorcerer reaches E3 commonly enough to plan as a portfolio, but not on demand; rare result reaches E4. |
| Astral | None | Hero Tamamo-no-Mae carries S2, but heroes are not repeatable access. |
| Death | Uba D1; Sorcerer D2; random depth on all three families | Sorcerer reaches D3 on 35.56% and D4 on 1.11% of pinned outcomes. |
| Nature | Uba N1 with W/D/N random | One-third of Ubas reach N2; no recruitable mage reaches N3 unaided. |
| Glamour | None | Hero and summoned access do not make it recruitable. |
| Blood | None | Requires an external verified bridge. |
| Holy | Shaman H1; Sorcerer H1 | No recruitable H2 or sacred troop line is established. |

## Shinuyama national rituals: Oni and underworld branch

| Ritual | Level | Requirement | Cost | Printed result |
| --- | ---: | --- | ---: | --- |
| Summon Ko-Oni | 1 | D1 | 4 Death gems | five or more Ko-Oni |
| Summon Ao-Oni | 2 | W1 D1 | 7 Water gems | five or more Ao-Oni |
| Summon Aka-Oni | 3 | F1 D1 | 7 Fire gems | five or more Aka-Oni |
| Ghost General | 4 | D3 | 10 Death gems | one Shura |
| Summon Oni | 4 | E1 D1 | 8 Earth gems | five or more Oni |
| Summon Kuro-Oni | 5 | D2 F1 | 9 Death gems | five or more Kuro-Oni |
| Summon Gozu Mezu | 6 | D3 | 6 Death gems | one Ox-head and one Horse-face |
| Summon Oni General | 6 | D2 F1 | 20 Death gems | one Oni Shugo |
| Summon Dai Oni | 8 | D4 F1 | 45 Death gems | one Dai Oni |

The Sorcerer directly meets Ko-Oni, Ao-Oni, Aka-Oni, Oni, Kuro-Oni, and Oni General thresholds. A Death-deep Sorcerer reaches Ghost General and Gozu Mezu; only the rare double-Death Sorcerer reaches D4 for Dai Oni without another bridge.

## Shinuyama national rituals: Tengu, spirit, and monster branch

| Ritual | Level | Requirement | Cost | Printed result |
| --- | ---: | --- | ---: | --- |
| Summon Karasu Tengus | 2 | N1 A1 | 2 Nature gems | three Karasu Tengu |
| Summon Konoha Tengus | 3 | A1 E1 | 3 Air gems | five or more Konoha Tengu |
| Summon Omukade | 4 | E2 D1 | 5 Earth gems | one Omukade |
| Contact Dai Tengu | 5 | A2 E1 | 55 Air gems | one Dai Tengu, ten Tengu Warriors, fifteen Karasu Tengu |
| Contact Nushi | 5 | W2 N1 | 25 Water gems | one Nushi |

Every Sorcerer meets Summon Omukade. A Water-random Uba meets Contact Nushi. The three Tengu rituals need Air, which no recruitable mage provides and the capital does not fund. Their national status does not make them immediately castable.

## Shinuyama national rituals: animal and shapeshifter branch

| Ritual | Level | Requirement | Cost | Printed result |
| --- | ---: | --- | ---: | --- |
| Summon Okami | 3 | N1 | 4 Nature gems | ten or more Okami |
| Contact Bakeneko | 3 | N2 | 8 Nature gems | one Bakeneko |
| Ambush of Tigers | 3 | N2 | 9 Nature gems | fifteen or more Tigers |
| Contact Mujina | 5 | N2 | 21 Nature gems | one Mujina |
| Contact Tanuki | 5 | N2 | 26 Nature gems | one Tanuki |
| Contact Jorogumo | 6 | N2 D1 | 32 Nature gems | one Jorogumo |
| Contact Kitsune | 6 | N2 | 30 Nature gems | one Kitsune |

Every Uba can cast Summon Okami. A Nature-random Uba reaches N2 and can cast the remaining Nature rituals, including Contact Jorogumo because Ubas already have D1. The capital produces no Nature gems, so caster access and treasury access must be solved separately.

## Shinuyama ritual access ladder

| Access class | Rituals | Reliable caster route |
| --- | --- | --- |
| Fixed Sorcerer | Ko-Oni, Ao-Oni, Aka-Oni, Oni, Omukade, Kuro-Oni, Oni General | Every Sorcerer has the printed thresholds. |
| Fixed Uba | Okami | Every Uba has N1. |
| One-third Uba branch | Bakeneko, Tigers, Mujina, Tanuki, Nushi, Jorogumo, Kitsune | N-random Uba for N2 group; W-random Uba for Nushi. |
| Death-deep Sorcerer | Ghost General, Gozu Mezu | At least one added Death level; 35.56% in pinned scheme. |
| Rare double-Death Sorcerer | Dai Oni | Both random slots add Death; 1.11% in pinned scheme. |
| External Air bridge | Karasu Tengus, Konoha Tengus, Dai Tengu | No recruitable Air mage. |

This ladder should be checked against the actual recruited portfolio before research and gems are committed. A path probability is not a caster standing in the correct laboratory.

## Shinuyama summon boundary

The manual prints fixed results for some rituals and `x+` for others. The plus sign is retained without inventing its random distribution. Summoned commanders print paths, leadership, retinues, shapes, stealth, auras, or other abilities, but those object descriptions do not establish how every form, follower, item slot, battle script, or strategic order behaves in 6.36.

Summons can extend paths and army types, but each extension should be recorded in a chain: legal initial caster, research, gem cost, resulting unit, resulting paths, any further booster or ritual, and the total turns and gems spent. Skipping a link turns possible access into imaginary access.

## Shinuyama national item boundary

No pinned item row names nation 70 in its six restriction fields or two nation-rebate fields. The safe conclusion is narrow: this audit found no Shinuyama-specific item or rebate record in the pinned snapshot.

Shinuyama can still forge generic items when a mage meets the Construction and path requirements. Summoned or hero mages may widen that access, but neither their arrival nor an item treasury should be assumed. Final costs under forge bonuses, sites, hammers, or other modifiers remain separate evidence questions.

## Shinuyama hero records

| Fixed name | Unit name | Verified magic | Boundary |
| --- | --- | --- | --- |
| Yukinaga | Heart Hider | F1 D1 | Hero record only; timing unresolved |
| Sojobo | Tengu King | A4 E1 N2 H2 | Pinned late-hero value 10; timing semantics unresolved |
| Tamamo-no-Mae | Kitsune | S2 N2 G3 | Pinned late-hero value 10; timing semantics unresolved |
| Zennyo Ryuo | Dragon of the Cave | W2 N2 | Pinned late-hero value 10; timing semantics unresolved |

The hero table shows major possible Air, Astral, Glamour, Nature, and Holy extensions. None belongs in a schedule that must work every game. The raw late-hero field is not converted into a turn, chance, or event rule without a current authoritative explanation.

## Shinuyama patch reconciliation

The current baseline is Dominions 6.36, released on 17 August 2026. The local official ledger records a 6.08 correction involving Shinuyama, Caelum, and a `Call` spell. Its abbreviated terms are enough to flag a historical assignment problem but not enough to reconstruct the exact sentence safely.

The revision-2 manual and pinned spell restrictions agree on the twenty-one active rituals in this chapter. That agreement controls the present dossier, while the 6.08 entry remains a warning against older spell lists. No direct Shinuyama correction was identified in the separate 6.36 announcement.

## Shinuyama opening priorities

1. Record whether the starting bottleneck is gold, resources, recruitment points, commander turns, or Morale support.
2. Match light Bakemono, armoured Bakemono, O-bakemono, Dai Bakemono, or Kappa to the reported province instead of defaulting to one line.
3. Use cheap Chiefs or Generals for mundane command so expensive mage turns remain available.
4. Label every random mage by final paths immediately.
5. Establish additional mage recruitment where terrain, economy, and position justify the fort.
6. Track Death, Nature, and Air ritual plans separately from research progress.
7. Keep a reserve that can replace fragile cheap troops or respond to raiding without recalling the entire field army.

These are planning controls, not tested expansion scripts. Exact formations, party sizes, target order, and casualty expectations remain open.

## Shinuyama recruitment packages to compare

### Light Bakemono mass

Seven-gold club, yari, and bow records provide cheap bodies and terrain recruitment. Their low Hit Points, Morale, and protection mean numbers must be paired with leadership, formation, target selection, and a replacement plan. A mountain rebate may improve price, but its exact live effect remains unresolved.

### Armoured Bakemono line

The eight-gold yari and bow records buy more protection at higher resource and recruitment-point cost. They can reduce immediate fragility without becoming a high-Morale heavy line. Compare their local production limit against simply adding more light bodies or saving resources for Dai Bakemono.

### Large Bakemono package

Dai Bakemono provide armoured no-dachi or long-bow profiles; O-bakemono provide high Strength and a great club at low resource cost. Size, frontage, protection, Defence, and enemy weapon damage change which profile fits. Neither “large” nor “strong” proves survivability.

### Stealth and raiding package

Bandits, their Leader, Bakemono Scouts, Noppera-bo, and light Bakemono offer stealth-linked pressure. Reports, detection, patrols, assassination, movement, fort interaction, and diplomatic cost decide results. The package should be used to create a specific threat rather than because a stealth value exists.

### Kappa water-link package

Kappa and Kappa Chiefs can be recruited from land and underwater forts and are amphibious. This can connect theatres or hold water access, but high encumbrance, local opposition, leadership, supply, and underwater combat conditions remain part of the decision.

## Shinuyama research response tree

### Branch A: early Conjuration bodies

Conjuration 1-3 opens Ko-Oni, Ao-Oni, Karasu Tengus, Aka-Oni, Konoha Tengus, Okami, Bakeneko, and Tigers. Fixed Sorcerers and Ubas cover several thresholds, but Tengu rituals need external Air and the N2 rituals need a Nature-random Uba. Research should follow the actual caster and treasury.

### Branch B: Sorcerer core summons

Conjuration 4-6 opens Oni, Omukade, Ghost General, Kuro-Oni, Gozu Mezu, and Oni General. Every Sorcerer covers Oni, Omukade, Kuro-Oni, and Oni General; Death depth gates the other two. This branch aligns well with the capital's D2 income but still spends rare, expensive mage-turns.

### Branch C: Nature commander ladder

Conjuration 5-6 opens Mujina, Tanuki, Nushi, Jorogumo, and Kitsune. A correctly randomed Uba covers each threshold, but the capital has no Nature income. The operational package therefore requires search, trade, or another treasury source before the research pays off.

### Branch D: high Conjuration and Dai Oni

Conjuration 8 plus D4F1 and 45 Death gems reaches Summon Dai Oni. Only a rare double-Death Sorcerer reaches the threshold natively in the pinned scheme. The branch should not be scheduled until the caster exists or another explicit D4 bridge is documented.

### Branch E: ordinary battlefield and Construction needs

The nation also needs research that helps its actual troops and mages survive current enemies. Fire, Water, Earth, Death, Nature, and Holy provide many possible buffs, attacks, and protections, while Construction can convert paths into generic items. No universal sequence is claimed because opposition, sites, gems, and recruited randoms change the answer.

## Shinuyama battlefield packages

### Cheap line with mage support

Light or armoured Bakemono occupy space while a labelled Shaman, Uba, or Sorcerer casts effects its actual paths support. Mundane commanders should provide leadership where possible. Low Morale and protection make guards, spacing, reserves, and the enemy's attack profile important.

### Large-unit striking group

Dai Bakemono or O-bakemono concentrate stronger attacks and larger bodies. They need a line, formation, or target that lets those attacks arrive without wasting their size and cost. Enemy reach, armour, Defence, missiles, fatigue, and control effects remain report-dependent.

### Missile mix

Short bows, long bows, and the mixed Bandit profile create several missile options. Range, precision, enemy shields and armour, weather, friendly obstruction, ammunition, and closing speed determine value. The roster does not prove a fixed archer ratio.

### Summon-supported force

Oni, spirits, Tengus, monsters, animals, or summoned commanders can add specialised bodies. The complete package includes gems, ritual turns, leadership, magic leadership where required, supply, route, and a battlefield job. A summoned unit is not useful merely because it is national.

## Shinuyama information and pressure network

Bakemono Scouts provide cheap reconnaissance. Bandits and Bandit Leaders add stealth and pillaging. Noppera-bo add assassination, patience, fear, and Spirit Sight. Several national summons also print stealth or unusual perception and leadership abilities.

This is a toolkit, not a success rate. Report quality, Glamour and invisible detection, patrol interaction, assassin battles, counter-assassination, and stealth movement remain engine-dependent. The safe practice is to layer scouts, record observations, protect expensive specialists, and avoid making a war plan depend on an unverified detection channel.

## Shinuyama Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Air bridge | Makes the Tengu ritual branch legally reachable and can support Air site searching | A path does not create the large Air treasury required by Contact Dai Tengu. |
| Nature economy | Funds the broad animal and shapeshifter ritual branch | Native N2 is random and the capital produces no Nature gems. |
| Economy and infrastructure | Funds forts, laboratories, large armies, and 545-gold Sorcerers | Gold does not create local resources, recruitment points, or mage-turns. |
| High Death bridge | Makes D4 access reliable for Dai Oni | The 45-gem ritual and Conjuration 8 remain substantial costs. |
| Sacred or awake design | Supports sacred commanders or supplies early province-taking | The recruitable troop roster has no sacred line. |

No exact design is endorsed without settings, map, opponents, legal chassis, and versioned evidence.

## Shinuyama matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Cheap frontage, bows, large attackers, summons, and reachable area effects | Spending every resource on a small premium line. |
| Heavy armour | Dai or O-bakemono attacks, buffs, fatigue, armour-answering magic, and suitable summons | Assuming short bows or light clubs solve protection. |
| High Defence, ethereal, or Glamour targets | Area effects, magic weapons, attack support, control, and verified perception | Treating Spirit Sight on one assassin as a universal answer. |
| Fast flankers or flyers | Guards, reserves, mage spacing, and layered lines | Clustering 545-gold Sorcerers behind fragile troops. |
| Fire, cold, poison, or fatigue pressure | Resistance, spacing, alternative troops, and matching summons | Assuming all Bakemono or Oni share the same resistances. |
| Underwater pressure | Kappa route, suitable summons, independents, and water magic | Treating amphibious access as automatic underwater superiority. |
| Gem denial | Conventional roster depth and low-gem magic | Researching twenty-one rituals as though every treasury were funded. |
| Raiding and covert pressure | Scouts, reserves, patrols, forts, and redundant mage recruitment | Relying on one capital-adjacent laboratory or one expensive mage stack. |

## Monthly Shinuyama audit

- Is each production centre limited by gold, resources, recruitment points, commander turns, or terrain?
- Are light, armoured, large, stealth, and amphibious troops assigned jobs that fit their recorded profiles?
- Is every Shaman, Uba, and Sorcerer labelled by final paths?
- Are mundane commanders available where using a mage would lose research or ritual tempo?
- Are cave bonuses and mountain rebates still described only at the evidence level actually established?
- Are Fire, Water, Earth, Death, Nature, and Air gem balances tracked separately?
- Does every planned ritual have research, a legal caster, gems, a mage-turn, leadership, and delivery?
- Are variable summon quantities left as printed notation rather than converted into invented averages?
- Are hero and summoned paths excluded from schedules that must be repeatable?
- Has any pinned-only field been kept separate from current observed behaviour?

## Shinuyama unresolved evidence boundary

The following remain open:

1. exact cave-fort gold and resource bonuses, eligible buildings, stacking, and live display;
2. the exact lesser-Bakemono mountain rebate, eligible records, stacking, and live display;
3. expansion-party sizes, formations, scripts, and casualty ranges for each troop package;
4. live 6.36 random-path display and timing for Shamans, Ubas, and Sorcerers;
5. exact probability distributions behind every printed `x+` summon result;
6. summoned unit shapes, retinues, item slots, magic paths after transformation, and strategic-order behaviour;
7. Noppera-bo assassination, fear, Spirit Sight, stealth, and counter-detection outcomes;
8. Kappa underwater performance and land-water campaign conversion;
9. the exact wording and superseded state addressed by the abbreviated 6.08 Shinuyama/Caelum spell correction;
10. hero arrival timing, late-hero field semantics, and live special behaviour;
11. final generic-item costs under combined forge modifiers;
12. specific Pretender designs, blesses, matchups, and map performance;
13. R-047, R-058, and all other parked engine-dependent investigations.

These are evidence gaps, not invitations to guess. Runtime testing and preparation of new test assets remain paused.

# Part XXIX: Middle Age C'tis, Miasma

## C'tis one-page command brief

Middle Age C'tis combines cheap lizard infantry, slave troops, sacred capital guards, large Sobek warriors, strong priests, Nature and Death magic, and a dominion that changes the land around it. Its two capital sites produce five gems each month and unlock separate sacred, Sobek, poison, and commander lines. The Marshmaster supplies the nation's main repeatable magical depth, while the Lizard Shaman, Empoisoner, and priest hierarchy cover narrower jobs.

The basic plan is:

- use ordinary infantry and slaves for replaceable line work instead of spending every capital resource on elite troops;
- reserve capital recruitment for Poison Slingers, Swamp Guards, Sobek bodies, and Empoisoners when their specific jobs matter;
- record every Marshmaster's final paths before assigning research, searching, forging, summoning, or battle duty;
- use mundane commanders for ordinary leadership so expensive mage and priest turns remain available;
- treat Miasma as a strategic environment with documented qualitative effects, not as a licence to invent percentages or disease timing;
- connect Conjuration research to the actual caster and gem treasury, especially for Sacred Crocodile, Monster Toads, Couatl, and the externally gated Scorpion Man;
- protect additional forts and laboratories so the nation can replace researchers, priests, and field mages outside the capital.

C'tis converts heat, swamps, dominion, gold, recruitment, gems, and mage-turns into a war plan. Its main risks are slow troops, cold-blooded fatigue, dependence on a small mage portfolio, and the temptation to treat Miasma or poison resistance as a complete answer to an enemy army.

## C'tis evidence and ruleset

This chapter covers unmodded Middle Age C'tis on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, recruitment limits, printed paths, Miasma description, and national ritual table. Nation ID 75, random masks, capital sites, spell restrictions, the Jade Mask restriction, and hero assignments are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The sources do not prove exact Miasma income percentages, disease-check timing, terrain-conversion probability, hosting order, cold-blooded fatigue outcomes, summon behaviour, assassin results, hero timing, or battle performance. Those remain unresolved. No runtime test, replay, save, or new test asset was used for this dossier.

## C'tis conversion chain

```text
heat preference, ordinary troops, capital specialists, Miasma, and five capital gems
-> provinces, protected forts, temples, laboratories, and dominion coverage
-> labelled Marshmasters, Shamans, Empoisoners, and priest turns
-> research, searching, Conjuration, forging, and battlefield support
-> surviving armies, replacement capacity, sieges, claims, and hostile economic pressure
```

The fragile arrows are cold, movement, capital congestion, mage-turn competition, and incomplete knowledge of Miasma's exact live calculations. A special dominion shapes the board, but it does not replace scouting, troop matching, logistics, or a reserve.

## C'tis national rules that shape planning

| Rule or asset | Source-backed fact | Planning consequence |
| --- | --- | --- |
| Heat preference | The race summary prefers Heat +2; Pretender design has a Heat limit of +1. | Cold provinces create a documented fatigue concern for cold-blooded troops, but exact battle loss is not assumed. |
| Thick hides | The manual describes the lizard races as naturally protected. | Low-resource troops are not unarmoured humans, yet their full durability still depends on the attack faced. |
| Poison resistance | Ordinary C'tissians carry partial poison resistance; several capital records carry more. | Poison is part of the roster's identity, not universal immunity. |
| Miasma | Dominion changes non-sea land, harms outsiders, and favours C'tis economically. | Dominion placement matters strategically, but exact modifiers and timing remain unresolved. |
| Underwater exception | Underwater provinces are not affected by Miasma's special effects. | Water borders and disciples must not be analysed as though the land rule applied unchanged. |
| Two capital sites | The Temple Marsh and Empoisoners Guild divide capital recruitment and produce W1 D2 N2 gems in total. | Capital queues and five monthly gems must be tracked separately. |
| Strong priests | Recruitable H1, H2, and H3 priests are verified. | Temple work and sacred leadership are available without pretending every priest is also a researcher. |

## Miasma evidence boundary

The manual states that C'tis dominion brings heavy rain, turns non-sea land into swamps or drip caves, slightly increases income in provinces owned by C'tis, and severely reduces income in enemy provinces. Warm-blooded beings without Swamp Survival are subject to disease. The Pretender and sacred units are described as immune; disciples otherwise suffer the enemy treatment. Underwater provinces are excluded.

Those statements establish direction, eligibility, and broad strategic pressure. They do not establish the numeric income modifiers, how frequently disease is checked, whether all changes occur in the same hosting step, the probability or rate of terrain conversion, or every interaction with ownership changes and allied armies. This dossier uses Miasma to frame decisions while keeping those calculations open.

## C'tis capital sites and gem economy

| Site | ID | Verified fields |
| --- | ---: | --- |
| The Temple Marsh | 62 | W1 D2 N2; Swamp Guard, Sobek Warrior, Sobek Sacred Guard, and Sobek General recruitment records |
| Empoisoners Guild | 12 | Empoisoner and Poison Slinger recruitment records |

The sites supply one Water, two Death, and two Nature gems each month. This directly funds several national Conjuration branches, but not Contact Scorpion Man's Earth cost. Site membership establishes legal capital recruitment, not the order in which those units should consume the queue.

## Complete C'tis commander membership

| Commander | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Taskmaster | 40 | 2 | 1 | Forts |
| Commander of C'tis | 55 | 15 | 1 | Forts |
| Lizard Lord | 95 | 21 | 1 | Forts |
| Hierodule | 40 | 1 | 1 | Forts |
| High Priest of C'tis | 115 | 1 | 2 | Forts |
| Lizard King | 340 | 5 | 4 | Forts |
| Lizard Shaman | 125 | 2 | 2 | Forts |
| Marshmaster | 330 | 1 | 2 | Forts |
| Sobek General | 200 | 31 | 1 | Capital only |
| Empoisoner | 125 | 6 | 2 | Capital only |

Ten commander records reconcile. The ordinary forts can recruit the complete priest ladder and both non-capital mage families. The capital adds the Sobek General and Empoisoner, so using that queue for specialist commanders has an opportunity cost even before troops are considered.

## C'tis commander jobs

| Commander | Source-backed role | Important limit |
| --- | --- | --- |
| Taskmaster | Cheap leader with Taskmaster +2 | Slave morale interaction and final rout outcomes remain battle questions. |
| Commander of C'tis | Leadership 75 conventional commander | Resource cost competes with protected troops. |
| Lizard Lord | Leadership 100 protected commander | More expensive than the ordinary commander and has no magic. |
| Hierodule | Cheap H1 priest | Low leadership and no research path limit broader use. |
| High Priest of C'tis | H2 priest and modest leader | Two recruitment points and 115 gold compete with mages. |
| Lizard King | H3 priest with leadership 150 | Four recruitment points and 340 gold make routine command expensive. |
| Lizard Shaman | S1 N1 sacred mage-priest | Narrow fixed paths and two recruitment points constrain volume. |
| Marshmaster | W1 D2 N2 random mage with undead leadership | Every turn spent outside research or magic carries a large opportunity cost. |
| Sobek General | Sacred, protected capital commander with Taskmaster | Capital-only and resource-heavy. |
| Empoisoner | Stealthy D1 N1 assassin with poison weapons | Assassination, patience, poison, and survival outcomes remain unresolved. |

## Complete C'tis troop membership

| Troop | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Militia | 7 | 2 | 5 | Forts |
| C'tissian Heavy Infantry | 10 | 15 | 11 | Forts |
| City Guard | 10 | 10 | 11 | Forts |
| C'tissian Light Infantry | 10 | 5 | 11 | Forts |
| Runner | 12 | 2 | 7 | Forts |
| Slave Warrior | 13 | 3 | 8 | Forts |
| Falchioneer | 13 | 17 | 18 | Forts |
| Elite Warrior | 15 | 9 | 9 | Forts |
| Poison Slinger | 24 | 6 | 32 | Capital only |
| Sobek Warrior | 30 | 34 | 13 | Capital only |
| Swamp Guard | 19 | 21 | 22 | Capital only, sacred |
| Sobek Sacred Guard | 55 | 37 | 33 | Capital only, sacred, maximum two per month |

Twelve troop records reconcile. The capital-only group contains four distinct jobs rather than one obvious default: poison missiles, a large protected Sobek body, a smaller sacred guard, and a very expensive limited Sobek sacred.

## C'tis troop jobs

| Troop | Source-backed role | Important limit |
| --- | --- | --- |
| Militia | Very cheap spear body | Low Morale and combat skill restrict independent use. |
| Heavy Infantry | Protected spear line | Resources and cold-blooded encumbrance can limit sustained fighting. |
| City Guard | Middle protected spear line | Does not carry the Heavy Infantry's full armour. |
| Light Infantry | Mobile spear-and-javelin profile | Lower protection exposes it to missiles and contact. |
| Runner | Fast spear-and-bite body | Low protection and Morale make speed alone insufficient. |
| Slave Warrior | Trident-and-bite slave profile | Needs suitable leadership and should not be treated as ordinary morale. |
| Falchioneer | Ambidextrous two-falchion attacker | Recruitment and resource demand are high for a non-sacred body. |
| Elite Warrior | Better-skilled trident infantry | Moderate protection still leaves matchup dependence. |
| Poison Slinger | Capital poison missile specialist | High recruitment-point cost and live poison results need target evidence. |
| Sobek Warrior | Large, heavily protected capital fighter | Thirty-four resources and capital dependence constrain replacement. |
| Swamp Guard | Sacred protected falchion line | Capital-only and recruitment-point heavy. |
| Sobek Sacred Guard | Large sacred halberd body | Fifty-five gold, thirty-seven resources, thirty-three points, and a two-per-month limit prevent mass assumptions. |

## C'tis capital queue doctrine

The capital supplies four troop specialists and two commander specialists. Poison Slingers compete with sacred and Sobek production through recruitment points. Sobek Warriors and both sacred guards also consume substantial resources. Empoisoners consume mage-capable commander turns, while Sobek Generals occupy the same capital commander system.

A useful capital plan therefore begins with the job required: poison delivery, sacred staying power, large protected bodies, specialist assassination, or capital leadership. The answer changes with resources, bless value, enemy composition, and the number of non-capital forts already producing Marshmasters and Shamans.

## Reading the Marshmaster random paths

Every Marshmaster begins W1 D2 N2. The pinned record adds one guaranteed level from Water, Astral, Death, or Nature, then an independent ten-percent second level from the same four-path pool.

| Final addition | Probability |
| --- | ---: |
| No named path among either roll | 73.125% for any one chosen W/S/D/N path |
| Exactly one level in a chosen path | 26.25% |
| Two levels in the same chosen path | 0.625% |
| Any second random level occurs | 10% |
| Second roll repeats the first path | 2.5% overall |
| Second roll adds a different path | 7.5% overall |

A chosen path appears at least once with probability 26.875%. Several recruits can still miss it, and the 330-gold cost means probability should be used for portfolio planning rather than an assumed delivery turn.

## Marshmaster final-path portfolio

| Primary result | Ordinary final paths before the second roll | Primary probability |
| --- | --- | ---: |
| Water | W2 D2 N2 | 25% |
| Astral | W1 S1 D2 N2 | 25% |
| Death | W1 D3 N2 | 25% |
| Nature | W1 D2 N3 | 25% |

The second roll can deepen the same path or add one of the other three. Rare W3, S2, D4, or N4 outcomes exist at 0.625% for each named path. They are possible assets, not infrastructure that a plan may assume before recruitment.

## C'tis native path boundary

| Path | Repeatable recruitable access | Boundary |
| --- | --- | --- |
| Fire | None | Requires Pretender, independent, summon, empowerment, or another verified bridge. |
| Air | None | Requires an external bridge. |
| Water | Marshmaster W1; random depth to W2 or rarely W3 | Sacred Crocodile requires W2. |
| Earth | None | Contact Scorpion Man requires both Earth and Fire. |
| Astral | Lizard Shaman S1; random Marshmaster S1 or rarely S2 | Shaman already meets Contact Couatl's Astral requirement. |
| Death | Empoisoner D1; Marshmaster D2, random D3 or rarely D4 | Native strength is repeatable but concentrated in Marshmasters. |
| Nature | Shaman and Empoisoner N1; Marshmaster N2, random N3 or rarely N4 | Every Marshmaster meets Monster Toads' N2 requirement. |
| Glamour | None | Requires an external verified bridge. |
| Blood | None | Requires an external verified bridge. |
| Holy | Hierodule H1, High Priest H2, Lizard King H3, Shaman H1 | Strong priest access is separate from research magic. |

## C'tis national ritual reconciliation

| Ritual | Level | Requirement | Cost | Printed result |
| --- | ---: | --- | ---: | --- |
| Sacred Crocodile | Conjuration 4 | N2 W2 | 1 Nature gem | one Sacred Crocodile |
| Summon Monster Toads | Conjuration 5 | N2 | 5 Nature gems | three Monster Toads |
| Contact Couatl | Conjuration 7 | N1 S1 | 40 Nature gems | one Couatl |
| Contact Scorpion Man | Conjuration 8 | E1 F1 | 12 Earth gems | one Scorpion Man |

The manual and pinned nation restrictions agree on all four records. The table proves printed requirements, costs, and results. It does not prove summoned forms, item slots, command behaviour, battle performance, or later path access beyond the printed unit description.

## C'tis ritual access ladder

| Access class | Ritual | Repeatable route |
| --- | --- | --- |
| Every Marshmaster | Summon Monster Toads | Fixed N2 |
| Water-random Marshmaster | Sacred Crocodile | W2 plus fixed N2; 26.875% have at least one added Water level |
| Every Lizard Shaman | Contact Couatl | Fixed S1 N1 |
| External Fire-and-Earth bridge | Contact Scorpion Man | No recruitable C'tis mage has Fire or Earth |

Caster access must be joined to research, the correct gem type, a laboratory, and a free mage-turn. Contact Couatl is legally easy for the Shaman but costs forty Nature gems; Contact Scorpion Man has a modest cost but no native caster.

## C'tis national item: The Jade Mask

The Jade Mask is item ID 226, a Construction 9 helmet requiring D6 N3 and twenty Death gems. The manual lists Death Magic +2, Magic Resistance +3, regeneration, poison resistance, fear, darkvision, and Rigor Mortis. The pinned item row restricts it to the three C'tis nation IDs 27, 75, and 113 and records no national rebate.

The restriction does not create the D6 N3 forger. A rare Marshmaster can reach D4 or N4, but no recruitable result supplies the complete threshold alone. Any forging plan must show the exact boosters, empowerment, summon, hero, Pretender, or other bridge rather than treating a national artifact as automatically available.

## C'tis hero records

| Fixed name | Unit name | Verified magic | Boundary |
| --- | --- | --- | --- |
| Niklatu | Lizard Hero | none | Hero record only |
| Murmur | Guild Master | D3 N3 | Pinned late-hero value 5; timing unresolved |
| Kabti'ili | Ancient Shaman | S2 N2 H1 | Hero record only |
| Nakhtun Eshash | Sobek High Priest | H3 | Hero record only |
| Atun Shar | Sobek Sauromancer | W2 D3 N2 | Pinned late-hero value 5; timing unresolved |

These records can widen a particular game's priest and magic portfolio, but none belongs in a schedule that must work every game. The raw late-hero field is not translated into an arrival formula without a current authoritative explanation.

## C'tis patch reconciliation

The current baseline is Dominions 6.36, released on 17 August 2026. The retained official ledger contains no directly named correction for C'tis, Miasma, Marshmaster, Empoisoner, Sobek, or the Jade Mask through that release.

This absence is not proof that every historical value was unchanged. The revision-2 manual controls current player-facing descriptions, while the pinned 6.35 data remains labelled as a structured cross-check. Any later discrepancy must be recorded rather than silently harmonised.

## C'tis opening priorities

1. Check whether the first recruitment bottleneck is gold, resources, recruitment points, or commander turns.
2. Match spear lines, javelins, slaves, dual weapons, or elites to the reported province instead of defaulting to one unit.
3. Use ordinary commanders for expansion leadership where their capacity is enough.
4. Label every Marshmaster by final paths immediately.
5. Build additional mage recruitment so research and field support do not remain capital-dependent.
6. Track Water, Death, and Nature gems separately even though the capital provides all three.
7. Maintain a reserve for raiding, cold-weather problems, or replacement of slow armies.

These are planning controls, not tested expansion scripts. Exact party sizes, formations, scripts, target order, and casualty ranges remain open.

## C'tis recruitment packages to compare

### Cheap spear screen

Militia, Light Infantry, City Guard, and Slave Warriors provide several prices and levels of protection. They can cover space while expensive mages remain behind the line. Morale, leadership, cold, and the enemy's damage profile decide which mixture survives.

### Protected infantry line

Heavy Infantry, City Guard, Falchioneers, and Elite Warriors trade more resources or recruitment points for armour, attacks, or skill. They should be compared against the local resource ceiling rather than assumed superior because their individual profile is stronger.

### Capital sacred group

Swamp Guards and Sobek Sacred Guards convert the capital, resources, recruitment points, and any useful bless into sacred force. The larger Sobek is limited to two per month and costs heavily in every queue. A bless should be judged against the actual number and role of sacreds that can be delivered.

### Sobek line

Sobek Warriors and Sacred Guards provide large, well-protected bodies with strong attacks. Their cost, size, resource demand, movement, fatigue, and replacement route matter as much as their raw durability.

### Poison pressure group

Poison Slingers and Empoisoners create ranged or covert poison threats. Poison resistance, missile accuracy, target selection, friendly exposure, assassin battles, and the exact effect sequence remain matchup and runtime questions.

## C'tis research response tree

### Branch A: national Conjuration opening

Conjuration 4 and 5 unlock Sacred Crocodile and Monster Toads. Every Marshmaster can cast the toad ritual; a Water-random Marshmaster reaches the crocodile threshold. The branch uses Nature gems and should be compared against site searching and other Nature expenditure.

### Branch B: Couatl bridge

Conjuration 7 unlocks Contact Couatl. Every Lizard Shaman has N1 S1, so the caster is repeatable even though the forty-gem cost is substantial. The summoned Couatl's printed paths can widen the portfolio, but its live strategic and battlefield behaviour remains untested here.

### Branch C: high Conjuration and external paths

Conjuration 8 unlocks Contact Scorpion Man at E1 F1. C'tis has neither path on a recruitable mage. Researching the ritual before documenting a legal caster and Earth treasury creates a dead endpoint.

### Branch D: Death and Nature support

Marshmasters naturally support Death and Nature research families, while Empoisoners and Shamans cover lower thresholds. The useful school depends on the opponent: protection, fatigue, undead, battlefield control, resistance, and troop survival all change the answer.

### Branch E: Construction and path bridges

Construction can convert W/S/D/N access into generic items and later support the Jade Mask chain. The artifact itself sits at Construction 9 and D6 N3, so the forge plan must be written as a sequence of actual path gains and costs rather than a nation label.

## C'tis battlefield packages

### Infantry line with Marshmaster support

Ordinary spear or elite infantry holds space while a labelled Marshmaster casts from its actual W/S/D/N paths. A mundane commander handles leadership where possible. Cold, fatigue, friendly exposure, and enemy attack type determine which support package is legal and useful.

### Sacred capital force

Swamp Guards and Sobek Sacred Guards form a smaller premium line under priest support. The package includes capital recruitment, resource limits, bless value, H1-H3 availability, and replacement time. Sacred status does not prove that the line fits every opponent.

### Sobek striking group

Sobek Warriors or sacred guards provide large protected bodies for a chosen point of contact. Frontage, weapon reach, defence, fatigue, enemy armour answers, and route speed can all turn high individual statistics into poor conversion.

### Poison and harassment package

Poison Slingers pressure at range while Empoisoners threaten commanders or isolated targets. This package is evidence-sensitive: poison resistance, patrols, bodyguards, scripts, accuracy, and assassination resolution must be checked rather than assumed.

## C'tis information and pressure network

C'tis has no recruitable scout named in its national commander table, so ordinary independent scouting and other verified sources remain important. Empoisoners supply stealth and assassination, but using a 125-gold capital mage as an information tool carries queue and survival costs.

Miasma adds territorial pressure by changing the environment of dominion-covered land. That pressure does not reveal enemy orders or replace reports. The safe information plan layers scouts, province reports, reserves, and protected commanders while keeping unverified disease and conversion timing outside operational promises.

## C'tis Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Fire and Earth bridge | Makes Contact Scorpion Man legally reachable and can add missing site-search paths | A caster does not create an Earth treasury or Conjuration 8. |
| Jade Mask forger | Supplies high Death/Nature or a shorter booster chain | Construction 9, twenty Death gems, and exact path steps still matter. |
| Economy and infrastructure | Funds forts, laboratories, temples, Marshmasters, and capital elites | Gold does not create local resources, recruitment points, or commander turns. |
| Sacred support | Improves the limited capital sacred line | The strongest sacred is capped at two per month and remains capital-only. |
| Awake expansion body | Reduces pressure on the slow early roster | Performance depends on map, scales, bless, chassis, and opponent evidence. |

No exact design is endorsed without game settings, map, opponents, legal chassis, and versioned evidence.

## C'tis matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Protected line, dual attacks, poison pressure, summons, and reachable area effects | Spending the entire capital queue on a tiny elite group. |
| Heavy armour | Falchioneers, Sobek attacks, buffs, fatigue, poison where relevant, and armour-answering magic | Assuming spears and slings solve protection unaided. |
| Cold pressure | Resistance, fatigue control, shorter battles, alternative bodies, and route choice | Treating cold-blooded as flavour text. |
| Poison-resistant enemies | Conventional damage, magic, sacreds, and non-poison summons | Building the whole battle plan around Poison Slingers. |
| Fast flankers or flyers | Guards, reserves, layered lines, and mage spacing | Leaving Marshmasters exposed behind slow infantry. |
| Undead or lifeless forces | Priests, Death/Nature options, suitable summons, and physical damage | Assuming disease or poison affects every target. |
| Dominion resistance | Temples, priests, strategic concentration, and ordinary economic strength | Treating Miasma as guaranteed control without candles. |
| Raiding | Scouts, reserves, forts, and distributed recruitment | Depending on one slow capital army to answer every incursion. |

## Monthly C'tis audit

- Is each fort limited by gold, resources, recruitment points, or commander turns?
- Is the capital queue producing a specific specialist rather than merely the most expensive record?
- Is every Marshmaster labelled by final paths?
- Are mundane commanders handling work that does not require magic or priesthood?
- Are Miasma claims still limited to the exact qualitative evidence available?
- Are Water, Death, and Nature gem balances tracked separately?
- Does every national ritual have research, a legal caster, the correct gems, a laboratory, and a free mage-turn?
- Are heroes and rare double-randoms excluded from schedules that must be repeatable?
- Are cold, movement, supply, fatigue, poison resistance, and replacement routes checked before battle?
- Has any pinned 6.35 field been kept separate from current observed behaviour?

## C'tis unresolved evidence boundary

The following remain open:

1. exact Miasma income increases and reductions, eligibility, rounding, and stacking;
2. disease-check frequency, hosting order, resistance, immunity, and ownership-change interactions;
3. swamp and drip-cave conversion rate, selection, timing, and interface display;
4. live 6.36 Marshmaster random-path presentation and timing;
5. exact cold-blooded fatigue outcomes across temperature, battle length, and unit profiles;
6. expansion-party sizes, formations, scripts, and casualty ranges;
7. Poison Slinger and Empoisoner targeting, poison, assassination, patience, and survival outcomes;
8. summoned-unit forms, magic, slots, leadership, and strategic-order behaviour;
9. hero arrival timing, late-hero field semantics, and live special behaviour;
10. the complete legal Jade Mask forging chain and final costs under combined modifiers;
11. disciple, allied-army, and underwater edge cases beyond the manual's explicit wording;
12. specific Pretender designs, blesses, matchups, and map performance;
13. R-047, R-058, and all other parked engine-dependent investigations.

These are evidence gaps, not invitations to guess. Runtime testing and preparation of new test assets remain paused.

# Part XXX: Middle Age Pangaea, Age of Bronze

## Pangaea one-page command brief

Middle Age Pangaea turns forests, mobile halfmen, recuperating troops, broad Nature magic, and a small capital Blood branch into strategic reach. Ordinary forts offer the full conventional roster, while forests add cheap local recruitment and sacred Hierophants. The capital contributes Pandemoniacs and White Centaurs through separate sites. Pans are the main research and ritual engine; Dryads and the two Hierophant families provide cheaper priesthood and random Water, Earth, Nature, or Glamour access.

The basic plan is:

- use forest recruitment to widen replacement and raiding capacity without pretending it replaces forts;
- match cheap Satyrs, missile Centaurs, protected Hoplites, mobile Warriors, and trampling Minotaurs to the reported target;
- label every Hierophant, Hierophantide, Dryad, Pan, and Pandemoniac by final paths as soon as recruitment completes;
- spend mundane commander turns on ordinary leadership so expensive mages remain available for research, searching, rituals, and battle magic;
- treat recuperation as a documented national advantage while leaving its exact eligibility, rate, and timing unresolved;
- connect each national ritual to its actual caster, research level, gem treasury, laboratory, terrain, and free mage-turn;
- protect secondary forests and forts so losses do not reduce the nation to one capital queue.

Pangaea converts forests, gold, resources, recruitment points, mage-turns, and Nature gems into mobility and repeated pressure. Its main risks are expensive researchers, uneven protection, low morale among cheap troops, capital congestion, narrow native answers outside Earth and Nature, and overconfidence in stealth, trample, berserk, recuperation, or Magical Tunes without matchup evidence.

## Pangaea evidence and ruleset

This chapter covers unmodded Middle Age Pangaea on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, recruitment markings, visible paths, national summary, capital sites, spell tables, and ritual descriptions. Nation ID 52, recruitment memberships, random masks, site fields, spell restrictions, the absence of national item rows, and hero assignments are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The sources do not prove exact recuperation checks, live recruitment-interface grouping, stealth outcomes, tune resolution, ritual implementation, hero timing, or battle performance. Those remain unresolved. No runtime test, replay, save, or new test asset was used for this dossier.

## Pangaea conversion chain

```text
forests, cheap local recruits, mobile troops, capital specialists, and Nature income
-> provinces, protected forest nodes, forts, temples, laboratories, and scouting reach
-> labelled Hierophants, Dryads, Pans, Pandemoniacs, and preserved mage-turns
-> research, searching, tunes, rituals, forging, and battlefield support
-> surviving armies, replacements, raids, sieges, claims, and strategic depth
```

The fragile arrows are morale, armour, capital congestion, the cost of Pans, limited native Astral and Death access, and incomplete knowledge of several special abilities. Forest access and stealth create options, but neither supplies information automatically or guarantees a successful raid.

## Pangaea national rules that shape planning

| Rule or asset | Source-backed fact | Planning consequence |
| --- | --- | --- |
| Forest beings | The roster is dominated by units with Forest Survival, and eleven records have explicit forest recruitment. | Forest provinces can become recruitment and movement nodes, but local capacity still depends on ownership, infrastructure, and queue limits. |
| Recuperating troops | The manual says troops heal battle afflictions and marks the roster with Recuperation. | Valuable survivors may recover, but no exact chance or timing is budgeted. |
| Stealth | Most light Satyr and Centaur lines, all five mage families, and both forest commanders carry Stealth. | Scouting, concentration, and raiding options improve, but detection and movement outcomes remain evidence questions. |
| Growth limit | Pretender design has a Growth limit of +1. | Scale planning can lean toward population and supplies, but the limit is not itself an economic recommendation. |
| Primitive Forts | The nation uses the Primitive Fort family. | Fort cost, build time, administration, and siege strength must be taken from the current fort table rather than assumed from the label. |
| Forest temples | Temples cost 300 gold in forests. | Forest dominion infrastructure receives a clear discount and should be considered alongside laboratories and forts. |
| Magical Tunes | Three national Enchantment-0 spells require N1 and five fatigue. | Nature casters gain immediate battlefield options, while their exact live behaviour remains unresolved. |

## Pangaea recruitment geography

The ordinary fort roster contains eight commanders and fourteen troops. The capital adds Pandemoniac and White Centaur through Hidden Grove and The Grove of Gaia. Forests separately recruit four commanders and seven troops: Black Harpy, Satyr Commander, Centaur Hierophant, Centauride Hierophantide, Harpy, Satyr Sneak, both basic Satyr variants, Minotaur, Centauride, and Centaur.

These categories overlap rather than replace one another. A forest fort can access ordinary-fort records as well as forest recruits, while an unfortified forest can provide the explicit terrain group. The exact live interface and every terrain edge case were not observed, so the chapter treats the structured memberships as legal-source boundaries rather than a screenshot of the current client.

## Complete Pangaea commander membership

| Commander | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Black Harpy | 35 | 1 | 1 | Forts and forests |
| Satyr Commander | 60 | 23 | 1 | Forts and forests |
| Minotaur Lord | 95 | 31 | 1 | Forts |
| Centaur Commander | 105 | 32 | 1 | Forts |
| Centaur Hierophant | 170 | 4 | 2 | Forts and forests |
| Centauride Hierophantide | 170 | 3 | 2 | Forts and forests |
| Dryad | 310 | 1 | 2 | Forts |
| Pan | 425 | 1 | 4 | Forts |
| Pandemoniac | 355 | 1 | 4 | Capital only |

Nine commander records reconcile. Forests can supply cheap scouts, ordinary leadership, and both H1 random-mage families without consuming a fort's ordinary commander identity. Pans and Dryads remain fort recruits; the Blood-capable Pandemoniac remains capital-only.

## Pangaea commander jobs

| Commander | Source-backed role | Important limit |
| --- | --- | --- |
| Black Harpy | Flying stealth scout and very cheap commander | Leadership 10 restricts army command. |
| Satyr Commander | Stealth leader for ordinary troops | Twenty-three resources compete with protected units. |
| Minotaur Lord | Protected leadership-75 trampler | No magic; resource-heavy and matchup-dependent. |
| Centaur Commander | Mobile leadership-100 commander | Thirty-two resources and Inspirational -1 make the role costly. |
| Centaur Hierophant | Sacred H1 with E/N random and longbow | Two recruitment points and only one magic level. |
| Centauride Hierophantide | Sacred H1 with W/N random and short bow | Two recruitment points and only one magic level. |
| Dryad | Sacred N1 H2 mage-priest with W/E/N/G random, Awe, and Seduction | 310 gold; seduction resolution and survival remain untested. |
| Pan | E2 N3 random mage and main researcher | 425 gold and four recruitment points create a large opportunity cost. |
| Pandemoniac | Capital N3 B2 mage with a rare E/N/B random | Capital-only, four recruitment points, and no priest path. |

## Complete Pangaea troop membership

| Troop | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Harpy | 7 | 1 | 3 | Forts and forests |
| Satyr Sneak | 9 | 3 | 6 | Forts and forests |
| Satyr, spear and javelin | 9 | 4 | 6 | Forts and forests |
| Satyr, spear only | 9 | 4 | 6 | Forts and forests |
| Satyr Hoplite | 14 | 24 | 24 | Forts |
| Reveler | 16 | 3 | 14 | Forts |
| Centaur | 25 | 4 | 12 | Forts and forests |
| Centauride | 25 | 3 | 12 | Forts and forests |
| Centauride Warrior | 30 | 11 | 17 | Forts |
| Centauride Cataphract | 30 | 28 | 17 | Forts |
| Centaur Cataphract | 35 | 32 | 21 | Forts |
| Centaur Warrior | 35 | 11 | 21 | Forts |
| Minotaur | 40 | 6 | 6 | Forts and forests |
| War Minotaur | 50 | 23 | 18 | Forts |
| White Centaur | 55 | 12 | 29 | Capital only, sacred |

Fifteen troop records reconcile. The two basic Satyrs share a displayed name but remain separate objects with different weapons and Defence. The roster offers cheap bodies, bows, javelins, protected formations, mobile striking units, tramplers, berserkers, and a capital sacred rather than one universal line.

## Pangaea troop jobs

| Troop | Source-backed role | Important limit |
| --- | --- | --- |
| Harpy | Cheap flying stealth body | Low morale and protection restrict direct fighting. |
| Satyr Sneak | High-stealth spear screen | Light protection and Morale 9 demand leadership and target selection. |
| Satyr with javelin | Cheap spear body with one ranged option | Still lightly protected and low-morale. |
| Satyr with spear | Slightly higher Defence than the javelin variant | Gives up the ranged weapon. |
| Satyr Hoplite | Protected spear line | Heavy resource and recruitment-point demand. |
| Reveler | Stealthy berserking spear-and-hoof attacker | Light armour and berserk commitment can become liabilities. |
| Centaur | Mobile longbow unit with hoof attack | Low protection and cost require useful range and positioning. |
| Centauride | More precise shortbow unit | Shorter weapon range and light protection. |
| Centauride Warrior | Fast high-Defence spear, hoof, and javelin fighter | Moderate protection remains vulnerable to the wrong attack. |
| Centauride Cataphract | Armoured lance, hoof, and javelin fighter | High resources and encumbrance reduce easy replacement. |
| Centaur Cataphract | Heaviest protected lance body | Thirty-two resources and modest Defence create matchup dependence. |
| Centaur Warrior | Mobile lance-and-hoof berserker | More exposed than the cataphract line. |
| Minotaur | Cheap-for-size trampler and berserker | Low Attack and Defence make trample target selection important. |
| War Minotaur | Better-armoured trampling line | More resources and encumbrance without solving every counter. |
| White Centaur | Capital sacred mobile striker | Capital-only, expensive, and recruitment-point heavy. |

## Recuperation evidence boundary

The manual marks every national commander and troop with Recuperation and summarizes the nation as having troops that heal battle afflictions. This supports treating affliction recovery as part of the roster's long-term value.

It does not establish which afflictions qualify, the chance per turn, whether commanders and troops follow identical rules, when checks occur, or every interaction with healing, disease, transformation, and temporary forms. The dossier therefore tracks valuable survivors without predicting a recovery date.

## Reading Pangaea's random paths

| Recruit | Fixed magic | Random structure |
| --- | --- | --- |
| Centaur Hierophant | H1 | Guaranteed E1 or N1, 50% each |
| Centauride Hierophantide | H1 | Guaranteed W1 or N1, 50% each |
| Dryad | N1 H2 | Guaranteed W1, E1, N1, or G1, 25% each |
| Pan | E2 N3 | Guaranteed E1 or N1, then an independent 10% E1/N1/B1 roll |
| Pandemoniac | N3 B2 | Independent 10% E1/N1/B1 roll |

These probabilities are derived from pinned masks `9216`, `8704`, `26112`, and `41984`. They are portfolio probabilities, not promises about a finite recruitment run or claims about the live display order.

## Pan final-path portfolio

| Final paths | Probability |
| --- | ---: |
| E3 N3 | 45% |
| E2 N4 | 45% |
| E4 N3 | 1.667% |
| E2 N5 | 1.667% |
| E3 N4 | 3.333% |
| E3 N3 B1 | 1.667% |
| E2 N4 B1 | 1.667% |

Every Pan gains either Earth or Nature. A named primary path appears at least once on 51.667% of Pans because the rare roll can repeat it; double Earth and double Nature each occur on 1.667%. Rare depth is useful when it appears but should not be scheduled before recruitment.

## Pandemoniac rare-path portfolio

Every Pandemoniac begins N3 B2. Ninety percent receive no additional level. Earth, Nature, and Blood each occur on 3.333% of recruits, producing E1 N3 B2, N4 B2, or N3 B3 respectively.

This capital line is the only repeatable native Blood access. A B3 result is possible but rare, so a Blood plan should distinguish the guaranteed B2 floor from a branch that may take many capital recruitments to appear.

## Pangaea native path boundary

| Path | Repeatable recruitable access | Boundary |
| --- | --- | --- |
| Fire | None | Requires Pretender, independent, summon, empowerment, or another verified bridge. |
| Air | None | Hero Arcopythera is not a repeatable solution. |
| Water | W-random Hierophantide or Dryad at W1 | No recruitable native depth beyond W1. |
| Earth | Pan E2, usually E3 and rarely E4; E-random Hierophant or Dryad at E1 | Strong repeatable Earth is concentrated in expensive Pans. |
| Astral | None | Requires an external bridge. |
| Death | None | Requires an external bridge. |
| Nature | Dryad N1; Pan N3, usually N4 and rarely N5; Pandemoniac N3 or rarely N4 | Nature is the broadest and deepest native path. |
| Glamour | G-random Dryad at G1 | Repeatable chance, but only one-quarter of Dryads. |
| Blood | Pandemoniac B2 or rarely B3; rare Pan B1 | Guaranteed access is capital-only. |
| Holy | Hierophants H1; Dryad H2 | Priest access exists in forests and forts. |

## Pangaea capital sites and gem economy

| Site | ID | Verified fields |
| --- | ---: | --- |
| The Grove of Gaia | 14 | N5 monthly gems; Growth scale limit 2; White Centaur recruitment record |
| Hidden Grove | 19 | Pandemoniac recruitment record |

The capital produces five Nature gems each month. That income directly matches all three national rituals, but it does not make every ritual affordable on schedule: research, caster access, other Nature spending, and mage-turn competition still matter.

## Pangaea national Magical Tunes

| Spell | Level | Requirement | Cost | Printed fields |
| --- | ---: | --- | ---: | --- |
| Tune of Fear | Enchantment 0 | N1 | 5 fatigue | Range 0, area 25; armour-negating, mind-affecting boundary |
| Tune of Growth | Enchantment 0 | N1 | 5 fatigue | Range 0, area 25 |
| Tune of Dancing Death | Enchantment 0 | N1 | 5 fatigue | Range 0, area 25; 31+ damage, armour-negating, magic resistance applies |

All three spells are national, immediately researched, and printed as unusable underwater. Every Dryad, Pan, and Pandemoniac meets N1; Nature-random Hierophants and Hierophantides also qualify. Legal access does not establish whether a tune is tactically safe or effective.

## Magical Tune evidence boundary

The manual establishes requirements, fatigue, range, area, broad targeting text, damage where printed, resistance fields, and the underwater prohibition. It does not fully establish target selection, pulse timing, friendly inclusion, mind-immunity handling, interruption, or how the area is placed in a live battle.

The dossier therefore treats the Tunes as available tools that require report-driven scripting. It does not promise a morale break, regeneration outcome, or damage result against a particular formation.

## Pangaea national ritual reconciliation

| Ritual | Level | Requirement | Cost | Printed result |
| --- | ---: | --- | ---: | --- |
| Monster Boar | Conjuration 5 | N3 | 10 Nature gems | Anonymous remote Monster Boar that creates unrest until found and slain |
| Awaken Hamadryad | Enchantment 5 | N4 | 25 Nature gems | One Hamadryad |
| Fort of the Ancients | Alteration 5 | N4 | 35 Nature gems | Complete fortress in a forest or shallow-sea province |

The manual and pinned nation restrictions agree on all three records. Printed requirements, costs, and headline results are source facts. Remote resolution, retinue realization, exact summoned abilities, terrain edge cases, fort type, and hosting order remain open.

## Pangaea ritual access ladder

| Access class | Ritual | Repeatable route |
| --- | --- | --- |
| Every Pan or Pandemoniac | Monster Boar | Fixed N3 |
| Nature-primary Pan | Awaken Hamadryad and Fort of the Ancients | N4 on 50% of Pans before the rare roll |
| Any Pan with at least one added Nature level | Awaken Hamadryad and Fort of the Ancients | 51.667% when the rare roll is included |
| Rare Pandemoniac | Awaken Hamadryad and Fort of the Ancients | N4 on 3.333% of Pandemoniacs |

The manual's Hamadryad description prints N3, Growth Power 1, Research -4, and a 3d6 Harpy retinue. Those fields help identify the intended result but do not establish live retinue rolling, persistence, shapes, or every command interaction. Fort of the Ancients additionally requires a legal target province; Monster Boar additionally requires a useful remote target and tolerance for uncertain resolution.

## Pangaea national item boundary

The pinned `BaseI.csv` snapshot assigns nation 52 to none of its restriction or nation-rebate fields. The supported conclusion is narrow: there is no pinned Pangaea-restricted or Pangaea-rebate item record.

Pangaea still forges general items through its actual paths. Strong Earth and Nature on Pans support a substantial generic Construction portfolio, while Water, Glamour, and Blood branches require labelled recruits. No item chain is treated as free merely because the nation can eventually reach its path.

## Pangaea hero records

| Fixed name | Unit name | Verified magic | Boundary |
| --- | --- | --- | --- |
| Rams Head | White Satyr | none | Hero record only |
| Arcopythera | Harpy Queen | A2 N2 | Hero record only |
| Taurotyrannos | Black Bull | E1 N3 B3 | Pinned late-hero value 5; timing unresolved |

These heroes can widen a particular game's mobility or magic portfolio, especially into Air or deeper Blood. None belongs in a repeatable research, forging, or ritual schedule. The raw late-hero field is not translated into a turn or probability formula.

## Pangaea patch reconciliation

The current baseline is Dominions 6.36, released on 17 August 2026. The retained official ledger contains no directly named correction for Pangaea, Pandemoniac, Hamadryad, Monster Boar, Fort of the Ancients, or the national Tunes through that release.

This absence is not proof that every historical value was unchanged. The revision-2 manual controls current player-facing descriptions, while the pinned 6.35 data remains labelled as a structured cross-check. Any later discrepancy must be recorded rather than silently harmonised.

## Pangaea opening priorities

1. Identify whether gold, resources, recruitment points, or commander turns limit the first expansion cycle.
2. Use province reports to choose cheap Satyrs, missiles, protection, mobility, or trample instead of defaulting to one troop.
3. Recruit mundane leadership where magic is unnecessary.
4. Label every random mage immediately and keep rare branches out of guaranteed schedules.
5. Secure useful forests for local replacement, scouting reach, and discounted temples.
6. Build additional fort and laboratory capacity before Pan recruitment becomes a single-queue bottleneck.
7. Track the Nature treasury against rituals, searching, forging, and emergency battlefield use.
8. Keep a mobile reserve for raiding, flankers, and replacement of stealth forces that fail.

These are planning controls, not a tested expansion script. Exact party sizes, formations, scripts, target order, stealth routes, and casualty ranges remain open.

## Pangaea recruitment packages to compare

### Cheap forest screen

Satyr Sneaks and the two basic Satyr variants provide inexpensive spear bodies from forts or forests. The javelin version adds one ranged attack, while the spear-only version has higher Defence. Low Morale and light protection make leadership, numbers, and the enemy attack profile decisive.

### Protected Bronze line

Satyr Hoplites and both Cataphracts trade large resource costs for protection and stronger contact profiles. This package suits resource-rich forts and known physical threats, but it should not consume every queue when mobility, missiles, or cheap replacement matter more.

### Centaur missile group

Centaurs and Centaurides combine bows, speed, stealth, and hoof attacks. Longbow range and shortbow precision create different roles. Their low protection means that missile exchange, formation, screening, and fast enemy contact require explicit planning.

### Mobile warrior wing

Centauride Warriors and Centaur Warriors provide speed, Defence, javelins or lances, and extra contact attacks. They can reinforce or pressure distant provinces, but cost, frontage, berserk behaviour, and enemy attack accuracy can reverse their paper advantage.

### Minotaur trample group

Minotaurs and War Minotaurs offer size, strength, trample, and berserk. The cheaper forest Minotaur is easy to distribute; the War Minotaur adds armour at greater resource cost. Size of target, formation, fatigue, morale, and anti-large damage remain essential matchup questions.

### Capital White Centaur reserve

White Centaurs are sacred, mobile, stealthy, high-Defence, and berserking. Their 55 gold and 29 recruitment points compete directly with other capital production. Bless value must be measured against the number the capital can actually deliver.

## Pangaea research response tree

### Branch A: immediate Enchantment tools

Enchantment 0 already provides all three Magical Tunes. Early Enchantment research can continue from a tool the roster can cast immediately, but the branch should be chosen for the enemy and the wider spell list rather than the national label alone.

### Branch B: Monster Boar pressure

Conjuration 5 unlocks Monster Boar for every Pan and Pandemoniac. Ten Nature gems and a mage-turn buy a remote unrest threat, not a guaranteed province loss. Detection, response cost, unrest timing, and target value must be evaluated separately.

### Branch C: Hamadryad access

Enchantment 5 unlocks Awaken Hamadryad. A Nature-primary Pan reaches N4, and the capital's five Nature gems can fund the ritual over time. The summoned commander's printed N3 and Harpy retinue may extend Nature operations, but the live result remains bounded by the unresolved summon details.

### Branch D: strategic fort creation

Alteration 5 unlocks Fort of the Ancients for N4 casters. The spell can convert thirty-five Nature gems and a mage-turn into a complete fortress in printed legal terrain. Its value depends on fort type, location, timing, treasury, and opportunity cost rather than research level alone.

### Branch E: Construction and generic path conversion

Construction converts common Earth and Nature access into equipment and can use rarer Water, Glamour, or Blood recruits when labelled. Because Pangaea has no national item restriction or rebate in the pinned snapshot, every item plan should use ordinary requirements and current cost rules.

## Pangaea battlefield packages

### Satyr line with Nature support

Cheap Satyrs hold space while a labelled Dryad, Pan, or Hierophant provides legal support. Protected Hoplites can anchor selected points. Morale, arrows, armour, fatigue, and the exact Tune interaction determine whether the package works.

### Centaur mobile force

Warriors or Cataphracts create the contact line while Centaurs and Centaurides add missiles. A mundane Centaur Commander carries leadership where possible. Terrain speed, formation width, missile exposure, and anti-large counters must be checked before committing.

### Minotaur breakthrough group

Minotaurs concentrate trample and berserk attacks on a chosen section. Satyrs or Centaurs can cover space around them. The package fails when targets, fatigue, morale, friendly congestion, or anti-large damage make trample inefficient.

### Sacred White Centaur group

White Centaurs combine speed, Defence, stealth, berserk, sacred status, and several attacks. The full package includes capital recruitment, bless value, priest support, replacement time, and a plan for counters. Sacred status does not prove expansion or battlefield results.

### Stealth pressure group

Satyr Sneaks, Revelers, Centaur Warriors, White Centaurs, and stealth commanders can assemble pressure away from the visible line. Legal stealth is source-backed; detection, coordination, movement resolution, patrol interaction, and combat success remain runtime questions.

## Pangaea information and pressure network

Black Harpies supply cheap flying stealth scouts from forts and forests. Many national units can move stealthily, allowing force concentration to remain partially concealed. This strengthens report gathering and threat projection only when orders, detection risk, leadership, and fallback routes are managed.

Monster Boar adds remote economic pressure, while forest recruitment broadens local recovery after losses. Neither mechanic reveals enemy orders. A safe information plan still layers scouts, province reports, army estimates, protected laboratories, and a reserve.

## Pangaea Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Fire, Air, Astral, or Death bridge | Adds paths missing from repeatable recruitment and widens searching or counters | A path on the Pretender does not create researchers, gems, or safe availability. |
| Blood acceleration | Reduces dependence on the capital Pandemoniac queue | Hunters, slaves, laboratories, unrest control, and opportunity cost still matter. |
| Economy and infrastructure | Funds Pans, forts, laboratories, temples, and protected troops | Gold does not create local resources, recruitment points, or mage-turns. |
| White Centaur bless | Improves the capital sacred line | Capital throughput and 29 recruitment points per unit limit mass. |
| Awake expansion body | Reduces pressure on lightly protected early troops | Performance depends on map, scales, chassis, bless, scripting, and opponents. |

No exact design is endorsed without game settings, map, opponents, legal chassis, and versioned evidence.

## Pangaea matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Satyr numbers, missiles, Minotaur trample, reachable area effects, and battlefield control | Sending expensive Centaurs into poor frontage without support. |
| Heavy armour | Minotaur strength, buffs, fatigue plans, Earth/Nature magic, and suitable weapons or summons | Assuming javelins and hooves solve protection unaided. |
| Accurate missiles | Protection, screens, speed, stealth approach, and target disruption | Exposing light Centaurs and Satyrs in open exchanges. |
| High-Defence elites | Multiple attacks, buffs, morale pressure, fatigue, and magic that avoids Defence | Relying on low-Attack Minotaurs alone. |
| Large or trample-resistant targets | Protected lines, missiles, Centaur attacks, magic, and other counters | Treating trample as universal damage. |
| Fast flankers or flyers | Guards, layered formations, reserves, and mage spacing | Leaving expensive Pans exposed behind a thin line. |
| Mindless or mind-immune forces | Physical damage, suitable magic, and non-morale plans | Building the script around Tune of Fear. |
| Raiding and patrol pressure | Cheap scouts, forest recruits, mobile reserves, forts, and route discipline | Assuming stealth makes an army undetectable. |

## Monthly Pangaea audit

- Is each fort or forest node limited by gold, resources, recruitment points, or commander turns?
- Are the two same-name Satyr variants recorded separately in recruitment plans?
- Is the capital queue producing a deliberate Pandemoniac or White Centaur rather than an automatic default?
- Is every random mage labelled by final paths?
- Are mundane commanders handling jobs that do not require magic or priesthood?
- Are recuperation and stealth claims still limited to the evidence available?
- Are Nature gems reserved against all three rituals, searching, forging, and emergencies?
- Does every ritual have research, a legal caster, the correct gems, a laboratory, a legal target, and a free mage-turn?
- Are heroes and rare Pan or Pandemoniac outcomes excluded from schedules that must be repeatable?
- Are morale, armour, movement, fatigue, supply, patrols, and replacement routes checked before battle?

## Pangaea unresolved evidence boundary

The following remain open:

1. exact Recuperation eligibility, chance, timing, affliction coverage, and interaction rules;
2. live 6.36 random-path display and ordering for all five mage families;
3. forest-recruitment interface grouping, terrain edge cases, and queue presentation;
4. Magical Tune targeting, pulse timing, resistance, friendly inclusion, immunity, interruption, and underwater implementation;
5. expansion-party sizes, formations, scripts, stealth routes, and casualty ranges;
6. stealth movement, detection, patrol, seduction, and survival outcomes;
7. Minotaur trample, berserk, fatigue, congestion, and target-selection outcomes;
8. Awaken Hamadryad retinue roll, shapes, persistence, command, and complete live abilities;
9. Monster Boar detection, unrest timing, resolution order, and target response;
10. Fort of the Ancients terrain legality, fort type, hosting order, ownership, and shallow-sea edge cases;
11. hero arrival timing, late-hero semantics, and live special behaviour;
12. specific Pretender designs, blessings, matchups, and map performance;
13. R-047, R-058, and all other parked engine-dependent investigations.

These are evidence gaps, not invitations to guess. Runtime testing and preparation of new test assets remain paused.

# Part XXXI: Middle Age Vanheim, Arrival of Man

## Vanheim one-page command brief

Middle Age Vanheim combines inexpensive human infantry, berserkers, skinshifters, flying capital troops, mounted Vanir, stealth, sailing, and a concentrated Air–Glamour–Earth–Blood mage corps. Ordinary forts supply the conventional army and the two mobile Vanir leaders. The capital alone supplies Dwarven Smiths, Vanadrotts, Fay Boars, Valkyries, and Vans, so its commander and troop queues carry several competing jobs.

The dependable magical floor is narrower than the nation summary first suggests. Vanherse provide A1 G1 H1, Vanjarls A2 G1 B1 H2, Dwarven Smiths E2 plus a guaranteed five-path random, and Vanadrotts A2 G2 B1 H2 plus a guaranteed five-path random. Fire and Death exist only through those randoms. Water, Astral, and Nature have no repeatable recruitable entry point.

Run the nation through reports rather than reputation:

1. record whether gold, resources, recruitment points, or capital turns are the present constraint;
2. separate human line troops, Einheres, Skinshifters, and capital units by job;
3. recruit mundane leadership where magic is unnecessary;
4. label every Dwarven Smith and Vanadrott by final paths;
5. treat the rare second random as a bonus, never as an opening promise;
6. track Air, Earth, Glamour, Blood, and Death spending separately;
7. use stealth and sailing as route options only after checking the actual order and destination;
8. keep a conventional reserve behind raiders and mobile groups;
9. test each battlefield package against the enemy's armour, morale, size, mobility, and magic;
10. preserve every unresolved transformation, mounted, summon, and movement claim.

## Vanheim evidence and ruleset

This chapter covers unmodded Middle Age Vanheim on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, recruitment markings, visible paths, national summary, sites, and national spell tables. Nation ID 78, ordinary-fort memberships, random masks, capital-site fields, spell restrictions, item-rebate links, and hero assignments are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

This is a planning dossier, not a claim that every legal order or battle result was observed. Sailing routes, trace-income resolution, shape changes, mounted interactions, random-path presentation, summon implementation, hero timing, and battlefield performance remain outside the verified layer.

## Vanheim conversion chain

| Input | Conversion | Output | Control question |
| --- | --- | --- | --- |
| Gold and resources | Ordinary troop recruitment | Human line, Einheres, and Skinshifters | Is the fort limited by gold, resources, or recruitment points? |
| Gold and commander turns | Vanherse and Vanjarls | Air, Glamour, priesthood, Blood, leadership, stealth, and sailing options | Does this job require an expensive mage-commander? |
| Capital commander turns | Dwarven Smiths and Vanadrotts | Earth forging, broad random access, stronger Air/Glamour/Blood, and high leadership | Which capital-only role is currently missing? |
| Capital troop turns | Fay Boars, Valkyries, and Vans | Supply, flying sacred pressure, or mounted Vanir | Is this worth displacing another capital recruit? |
| Research and gems | National and general magic | Battlefield Valkyries, Draugar, forging, buffs, summons, and counters | Is there a legal repeatable caster, not merely a theoretical path? |
| Scouts, stealth, and movement options | Information and pressure | Better route coverage and concealed threats | What report confirms the route, target, and fallback? |
| Blood access and slaves | Sacrifice or Blood magic | Dominion pressure and a wider spell economy | Are hunting, unrest, transport, and mage-turn costs funded? |

The chain fails when the capital queue is asked to solve every problem, rare paths are treated as guaranteed, or mobile forces move beyond report coverage and replacement support.

## Vanheim national rules that shape planning

The manual describes ocean sailing, trace income across oceans, flying troops, illusions, a Cold +1 preference, average priests who can perform blood sacrifices, and Standard Forts. It also describes a military built from heavy infantry, skinshifters, Valkyries, berserkers, and Vanir, with Air, Glamour, Earth, Blood, and some Fire and Death magic.

These are operational categories, not complete formulas. Cold preference can guide scale planning; sailing can alter route choice; flying and stealth can change threat geometry; and blood sacrifice can convert slaves into dominion pressure. None removes the need to check legal destinations, leadership, detection, income, supply, fatigue, or order resolution.

## Sailing and trace-income evidence boundary

Vanherse, Vanjarls, and Vanadrotts print Army Sailing and Ship Size 5. The nation summary prints ocean sailing and trace income across oceans. Those fields establish that a special movement and economic identity exists, but this chapter does not invent capacity totals, route blockers, coast requirements, collection timing, rounding, or interaction with hostile control.

Before relying on an ocean route, record the origin, destination, commander, carried units, unit sizes, intervening provinces, ownership, and the order shown by the current interface. Before budgeting trace income, use actual treasury and province reports rather than a derived rate that the cited tables do not provide.

## Vanheim capital sites and recruitment geography

| Site | ID | Verified fields |
| --- | ---: | --- |
| The Halls of Andvare | 15 | E3 monthly gems; Dwarven Smith and Fay Boar recruitment records |
| Vanhalla | 35 | A1 and G1 monthly gems; Vanadrott, Van, and Valkyrie recruitment records |

The capital therefore produces five gems each month: three Earth, one Air, and one Glamour. It also contains both capital commander lines and all three capital troop lines. Losing access to the capital queue is more damaging than the gem total alone suggests.

## Complete Vanheim commander membership

| Commander | Gold | Resources | Recruitment points | Location | Verified magic or job |
| --- | ---: | ---: | ---: | --- | --- |
| Scout | 35 | 4 | 1 | Ordinary forts | Stealth 50, forest and mountain survival, short bow |
| Herse | 55 | 22 | 1 | Ordinary forts | Mundane leadership 75 |
| Vanherse | 235 | 16 | 2 | Ordinary forts | A1 G1 H1, leadership 75, glamour, stealth, sailing, mounted |
| Vanjarl | 440 | 18 | 2 | Ordinary forts | A2 G1 B1 H2, leadership 100, glamour, stealth, sailing, mounted |
| Dwarven Smith | 195 | 2 | 4 | Capital, Halls of Andvare | E2 plus two structured random rolls, Master Smith 1 |
| Vanadrott | 595 | 19 | 4 | Capital, Vanhalla | A2 G2 B1 H2 plus two structured random rolls, leadership 150, glamour, stealth, sailing, mounted |

The manual and pinned memberships reconcile four ordinary-fort commanders and two capital-site commanders. The ordinary Scout is not the Early Age Van Scout, and the two capital mages must not be treated as universally recruitable.

## Vanheim commander jobs

- **Scout:** report gathering and route confirmation without consuming a mage turn.
- **Herse:** conventional leadership when a force does not require priesthood, magic leadership, stealth, or sailing.
- **Vanherse:** cheaper mobile Air–Glamour priest and commander; useful where A1 G1 H1 is enough.
- **Vanjarl:** stronger Air, H2 priesthood, native B1, and higher leadership from an ordinary fort.
- **Dwarven Smith:** capital Earth researcher and forger whose guaranteed random determines its additional role.
- **Vanadrott:** expensive capital Air–Glamour–Blood leader and priest whose final randoms may open rare thresholds.

The first economy control is to avoid paying Vanjarl or Vanadrott prices for a Herse's job. The second is to avoid turning every Smith into a generic researcher when its final paths make it the only available specialist for a planned spell or item.

## Complete Vanheim troop membership

| Troop | Gold | Resources | Recruitment points | Location | Printed distinction |
| --- | ---: | ---: | ---: | --- | --- |
| Huskarl, axe | 10 | 12 | 9 | Ordinary forts | Axe and javelin, Defence 11 |
| Huskarl, spear | 10 | 12 | 9 | Ordinary forts | Spear and javelin, Defence 12 |
| Hirdman, spear | 12 | 20 | 14 | Ordinary forts | Protection 16, spear, Defence 12 |
| Hirdman, broad sword | 12 | 22 | 14 | Ordinary forts | Protection 16, broad sword, Defence 13 |
| Einhere | 25 | 21 | 31 | Ordinary forts | Two weapons, Ambidextrous 1, Berserker +5 |
| Skinshifter | 25 | 7 | 36 | Ordinary forts | Great sword, forest survival, printed regeneration 10% |
| Fay Boar | 100 | 1 | 30 | Capital, Halls of Andvare | Trample, forest survival, Supply 100 |
| Valkyrie | 45 | 15 | 29 | Capital, Vanhalla | Flying, glamour, sacred, stealth 65, spirit sight |
| Van | 60 | 16 | 21 | Capital, Vanhalla | Mounted, glamour, sacred, stealth 65, lance and javelin |

Same-name Huskarls and Hirdmen remain separate objects. The capital-only troops come from site records and should not be counted as ordinary fort recruitment.

## Vanheim troop jobs

- **Axe Huskarl:** cheap javelin screen whose axe gives a different contact profile from the spear variant.
- **Spear Huskarl:** cheap javelin screen with a spear and one additional printed Defence point.
- **Spear Hirdman:** protected line body with the spear's attack profile.
- **Broad-sword Hirdman:** slightly more resource-intensive protected line with one additional printed Defence point.
- **Einhere:** costly two-weapon berserker that needs a deliberate target and fatigue plan.
- **Skinshifter:** resource-light great-sword body with printed regeneration and an unresolved transformation chain.
- **Fay Boar:** capital supply carrier and trampler; its economic and combat value must be assessed separately.
- **Valkyrie:** flying sacred stealth unit for mobility, flanking, or concentrated attack after route and counter checks.
- **Van:** mounted sacred stealth unit with high Defence, lance contact, and capital-only replacement.

These labels identify candidate jobs. They do not establish expansion counts, formations, casualty rates, transformation results, or the best unit against an unknown enemy.

## Vanheim capital queue doctrine

Vanheim's capital commander queue must choose between the 195-gold Dwarven Smith and the 595-gold Vanadrott. The Smith is the repeatable Earth and forging base; the Vanadrott provides stronger Air, Glamour, Blood, priesthood, leadership, sailing, and a different five-path mask. Neither is an automatic default.

The capital troop queue separately chooses among Fay Boars, Valkyries, and Vans. Fay Boars address supply and size-based contact; Valkyries address flying sacred reach; Vans provide mounted sacred reach. The correct choice depends on the active constraint, enemy, bless, route, and replacement horizon.

## Reading Vanheim's random paths

Dwarven Smiths and Vanadrotts each receive one guaranteed one-level random and one independent ten-percent one-level random. Each roll selects uniformly from its own five-path mask. The rare roll can repeat the guaranteed path.

For any named path inside either mask:

- the guaranteed roll selects it on 20% of recruits;
- the rare roll adds it on 2% of all recruits;
- it appears at least once on 21.6% of recruits;
- it appears on both rolls on 0.4% of recruits.

The rare roll fires on ten percent of all recruits. It repeats the guaranteed path on two percent of all recruits and selects a different path on eight percent. These figures are arithmetic from the pinned masks, not live samples.

## Dwarven Smith final-path portfolio

The Dwarven Smith begins E2. Its mask is Fire, Air, Earth, Death, or Glamour.

| Final branch | Probability |
| --- | ---: |
| F1 E2, A1 E2, E3, E2 D1, or E2 G1, each with no rare addition | 18% each |
| F2 E2, A2 E2, E4, E2 D2, or E2 G2, each from a repeated rare path | 0.4% each |
| Any particular mixed pair from F, A, E, D, and G | 0.8% each |

There are ten possible mixed pairs. Together the five ordinary branches account for 90%, the five repeated-path branches for 2%, and the ten mixed branches for 8%. Every Smith has Earth 2; additional Earth produces E3 or rarely E4, while Fire, Air, Death, and Glamour remain branch-dependent.

## Vanadrott final-path portfolio

The Vanadrott begins A2 G2 B1 H2. Its mask is Air, Earth, Death, Glamour, or Blood.

| Final branch | Probability |
| --- | ---: |
| One added A, E, D, G, or B with no rare addition | 18% each |
| The same named path added twice | 0.4% each |
| Any particular mixed pair from A, E, D, G, and B | 0.8% each |

The strongest rare native endpoints are A4, E2, D2, G4, or B3 on the relevant repeated branch. Mixed outcomes can combine thresholds, including the A3 D1 result required for Summon Valkyries, but a particular mixed pair appears on only 0.8% of Vanadrotts.

## Vanheim native path boundary

| Path | Repeatable recruitable access | Boundary |
| --- | --- | --- |
| Fire | Dwarven Smith F1 on 21.6%, rarely F2 on 0.4% | No fixed recruitable Fire. |
| Air | Vanherse A1; Vanjarl A2; Vanadrott A2, A3 on 21.6%, rarely A4; Smith random up to A2 | Broad Air access, but the highest thresholds are rare or need conversion. |
| Water | None | Requires Pretender, independent, summon, empowerment, or another verified bridge. |
| Earth | Every Smith E2; E3 on 21.6%, rarely E4; Vanadrott random up to E2 | Strong Earth is capital-dependent. |
| Astral | None | Requires an external bridge. |
| Death | Smith or Vanadrott D1 on 21.6%, rarely D2 | No fixed recruitable Death. |
| Nature | None | The manual's eastern dwarf result is a summon, not recruitable access. |
| Glamour | Vanherse and Vanjarl G1; Vanadrott G2, G3 on 21.6%, rarely G4; Smith random up to G2 | Glamour depth is concentrated in the capital Vanadrott queue. |
| Blood | Vanjarl and Vanadrott B1; Vanadrott B2 on 21.6%, rarely B3 | Repeatable fixed Blood exists, but depth is capital-random. |
| Holy | Vanherse H1; Vanjarl and Vanadrott H2 | Average priesthood with blood sacrifice. |

Rare maximums show what can exist, not what a schedule can assume. A plan should state its guaranteed floor, required random, expected recruitment burden, gems, boosters, and fallback.

## Vanheim national spell and ritual reconciliation

| Name | Type | Level | Requirement | Cost | Printed result |
| --- | --- | ---: | --- | ---: | --- |
| Summon Valkyries | Battlefield spell | Conjuration 6 | A3 D1 | 100 fatigue | Seven Valkyries; unusable underwater |
| Awaken Draugar | Ritual | Conjuration 4 | D2 | 12 Death gems | Four Draugar; unusable underwater |
| Summon Dwarf of the Four Directions | Ritual | Conjuration 8 | A4 E3 | 62 Air gems | One unique directional dwarf; unusable underwater |

The manual and pinned nation-restriction rows agree on these three active records. The table establishes legal thresholds, costs, counts, and the underwater prohibition. It does not establish placement, persistence, selection rules, or combat outcomes.

## Vanheim national-magic access ladder

| Spell or ritual | Unassisted repeatable access |
| --- | --- |
| Summon Valkyries | A Vanadrott must receive both Air and Death across its two rolls: 0.8% of Vanadrotts. Vanlade also qualifies, but is a hero and not repeatable. |
| Awaken Draugar | A Dwarven Smith or Vanadrott must receive Death on both rolls: 0.4% of either line. Vanlade qualifies but is not schedulable. |
| Summon Dwarf of the Four Directions | No unassisted repeatable recruit naturally combines A4 and E3. Path conversion, empowerment, a summon, or Pretender support is required. |

Researching a national spell does not create its caster. Vanheim should audit the mage roster before committing to a national-magic branch and keep a general-spell fallback when the required rare recruit has not appeared.

## Four Directions ritual boundary

The manual's Middle Age table prints Dwarf of the East, with A4 E3 N2 and Master Smith 2. The pinned structured record links North, South, East, and West candidates through a `dwarfs` selection group. This establishes a four-object relationship but not a chosen direction, deterministic order, repeat-cast handling, or uniqueness implementation.

The safe plan treats Conjuration 8, A4 E3, sixty-two Air gems, a laboratory, and a free mage-turn as necessary inputs while leaving the actual directional result unresolved. No strategy chain should depend on receiving one particular dwarf unless later versioned evidence closes that question.

## Vanheim national item metadata

No pinned item row restricts an item to nation 78. Six rows assign Vanheim a nation-rebate link:

| Item | ID | Construction | Requirement | Native access boundary |
| --- | ---: | ---: | --- | --- |
| Dwarven Hammer | 29 | 3 | E3 | A Smith reaches E3 on 21.6%; rarely E4. |
| Lightweight Scale Mail | 236 | 3 | A1 | Vanherse, Vanjarl, and Vanadrott qualify. |
| Weightless Scale Mail | 262 | 7 | A1 | Vanherse, Vanjarl, and Vanadrott qualify. |
| Pebble Skin Suit | 280 | 9 | B4 E1 | No unassisted repeatable recruit reaches B4. |
| Cauldron of the Elven Halls | 361 | 5 | G3 | A Vanadrott reaches G3 on 21.6%; rarely G4. |
| Draupnir | 435 | 9 | E5 | No unassisted repeatable recruit reaches E5. |

A rebate link is not a restriction and does not itself grant the required path. The chapter does not infer the current displayed price, rounding, stacking, or immediate forgeability from the metadata field alone.

## Vanheim hero records

| Fixed name | Unit identity | Verified magic | Boundary |
| --- | --- | --- | --- |
| Farbaute | Einhere | none | Hero assignment only |
| Vanlade | Vanadrott | A3 D2 G2 B2 H2 | Raw late-hero value 10; timing semantics unresolved |

Vanlade qualifies for Summon Valkyries and Awaken Draugar and widens several other thresholds. That makes the hero useful when present, not a repeatable research or ritual bridge. Farbaute's performance and both arrival conditions remain outside the source-backed schedule.

## Vanheim patch reconciliation

The current baseline is Dominions 6.36, released on 17 August 2026. The retained official ledger contains one 6.13 presentation record naming Vanheim and Helheim, published 15 May 2024, but no directly named mechanical correction for Vanadrott, Vanjarl, Dwarven Smith, Vanhalla, the Halls of Andvare, Awaken Draugar, or Summon Valkyries through 6.36.

The presentation record is not converted into a gameplay change. The revision-2 manual controls current player-facing descriptions, while the 6.35 structured export remains labelled as a pinned cross-check.

## Vanheim opening priorities

1. Identify whether gold, resources, recruitment points, or commander turns limit each fort.
2. Use Huskarls for cheap coverage and Hirdmen where protection is worth the resource cost.
3. Recruit mundane Herse leadership when a mage-commander adds no necessary capability.
4. Decide whether the next capital commander solves Earth/forging or Air/Glamour/Blood/leadership.
5. Label every Smith and Vanadrott immediately, including whether the rare roll appeared.
6. Keep Fire, Death, high Earth, high Glamour, and high Air plans conditional on the actual roster.
7. Add scouts before sailing, stealth, or flying forces outrun reliable province reports.
8. Track capital troop replacement separately from ordinary infantry replacement.
9. Match research to legal casters and the gem treasury rather than to national spell names alone.
10. Maintain a reserve that can answer raiders without recalling every forward mobile group.

These are planning controls. Exact expansion parties, routes, formations, scripts, blesses, and casualty expectations remain open.

## Vanheim recruitment packages to compare

### Cheap javelin screen

Both Huskarls cost ten gold and carry javelins. The spear variant has one more printed Defence; the axe variant changes the contact attack. They provide affordable bodies and opening missile pressure, but Morale 10, Protection 11, and ordinary human statistics make leadership and the enemy attack profile important.

### Protected Hirdman line

Both Hirdmen provide Protection 16 and Morale 11. The spear costs twenty resources; the broad-sword variant costs twenty-two and has one more printed Defence. This line converts resources into staying power, so it should be compared with the number of Huskarls, Skinshifters, or commanders the same fort could produce.

### Einhere striking group

Einheres combine two weapons, Ambidextrous 1, Berserker +5, Morale 13, and Protection 16. At twenty-five gold, twenty-one resources, and thirty-one recruitment points, they are not disposable line filler. Formation width, fatigue, target Defence, armour, and berserk consequences determine whether their extra attacks convert into value.

### Skinshifter group

Skinshifters cost twenty-five gold but only seven resources and print a great sword, forest survival, and regeneration. Their thirty-six recruitment points can become the limiting cost. The chapter does not assume how their shape chain, wounds, equipment, regeneration, or post-battle state resolve.

### Capital flying reserve

Valkyries combine flight, sacred status, glamour, stealth, spirit sight, and a light lance. They can threaten exposed units or distant points, but forty-five gold and twenty-nine recruitment points compete with every other capital troop. Flight does not remove the need for priest support, route confirmation, formation, or a counter plan.

### Capital mounted reserve

Vans combine high Defence, sacred status, glamour, stealth, a lance, a javelin, and a Fay Horse. Their sixty-gold cost and capital-only replacement make unsupported trades expensive. Mounted damage, rider–mount interaction, and remounting remain unresolved.

## Vanheim research response tree

### Branch A: ordinary Air and Glamour support

Vanherse and Vanjarls provide repeatable A1–A2 and G1 from every fort, while Vanadrotts provide A2 G2. Early research can therefore favour general spells these guaranteed paths can cast. The exact branch still depends on enemy armour, mobility, resistance, battlefield size, and the gems available.

### Branch B: Construction and the Smith economy

Every Dwarven Smith has E2 and Master Smith 1. Construction turns that guaranteed floor and the Smith's random into general equipment, while the six rebate links create additional candidates. A forge schedule must still record the final path, current price, required gems, research, laboratory, and lost research or ritual turn.

### Branch C: Conjuration 4 and Draugar

Awaken Draugar requires D2, which only a same-path double random supplies naturally on a Smith or Vanadrott at 0.4% per recruit. Conjuration 4 should therefore be justified by the general spell list as well as a ritual that may lack a caster. If D2 appears, twelve Death gems and a mage-turn produce the printed four Draugar.

### Branch D: Conjuration 6 and battlefield Valkyries

Summon Valkyries requires A3 D1. A Vanadrott obtains the necessary mixed Air–Death pair on 0.8% of recruits, while Vanlade qualifies if the hero arrives. Research, the legal caster, Air-gem availability for the 100-fatigue spell, battlefield placement, and the underwater prohibition all belong in the pre-battle check.

### Branch E: Conjuration 8 and the Four Directions project

The national ritual needs A4 E3 and sixty-two Air gems. No unassisted repeatable recruit supplies both paths together, so the project begins with a path-conversion design rather than with research alone. The directional result is also unresolved. This is a late infrastructure project, not a default national milestone.

### Branch F: Blood and dominion pressure

Vanjarl and Vanadrott provide fixed B1, with Vanadrotts occasionally reaching B2 or rarely B3. That makes a repeatable Blood entry possible, but not free. Hunting, unrest, laboratory coverage, slave movement, sacrifice, research, and the cost of diverting expensive commanders must all be included.

## Vanheim battlefield packages

### Human line with separate command

Huskarls or Hirdmen hold frontage under a Herse while mages remain in protected positions. This preserves expensive Vanir turns for magic or specialist leadership. The package must be adjusted for morale, missiles, armour, fatigue, and enemy breakthrough speed.

### Berserker and Skinshifter strike group

Einheres provide multiple berserk attacks while Skinshifters add great swords and a different resource profile. A human screen can absorb initial contact. The package fails when fatigue, poor target choice, congestion, missile damage, or unresolved transformation behaviour overwhelms its contact damage.

### Mounted Vanir wing

Vans or mounted commander-led elements can create a mobile contact group. High Defence, glamour, stealth, lances, and javelins suggest pressure rather than invulnerability. Anti-large attacks, accurate weapons, fatigue, formation, and mounted resolution must be checked.

### Valkyrie flying group

Valkyries can concentrate flying sacred bodies against a selected part of the field. Their low count, capital replacement, protection, morale, and landing target matter. A flying order without guards, priest support, report coverage, and a fallback can expose the most expensive troop line.

### Sailing pressure group

Vanherse, Vanjarls, or Vanadrotts can anchor an army-sailing force if the carried group and route are legal. The package can alter strategic geometry, but exact capacity and route resolution are not supplied here. Verify the current order interface and keep a conventional land route or reserve.

### Rare-path mage group

Labelled Smiths and Vanadrotts can combine Fire, Air, Earth, Death, Glamour, and Blood tools that the fixed roster cannot. Build the script from the mages actually present. Do not design a standard army around a 0.4% or 0.8% branch and then substitute an unqualified caster.

## Vanheim information and pressure network

Scouts provide cheap report coverage, while Vanir commanders and several capital troops print stealth. Flying Valkyries and sailing commanders can threaten routes that ordinary armies cannot. These capabilities widen the set of possible orders but do not reveal enemy orders or guarantee concealment.

A safe pressure network layers scouts, province reports, labelled commanders, protected laboratories, gem and slave transport, fallback provinces, and a reserve. Trace-income and blood-sacrifice plans should be reconciled against actual treasury and dominion reports rather than folded into an assumed passive advantage.

## Vanheim Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Water, Astral, or Nature bridge | Adds paths absent from repeatable recruitment | A Pretender path does not create researchers, gems, or safe availability. |
| Four Directions enabler | Helps assemble A4 E3 for the national ritual | Sixty-two Air gems, research, mage-turns, and unresolved direction selection remain. |
| Blood acceleration | Adds hunting or higher Blood thresholds | Hunters, slaves, unrest control, laboratories, and opportunity cost still matter. |
| Economy and scales | Funds expensive Vanir, capital mages, forts, and laboratories | Gold does not create capital turns, resources, recruitment points, or rare randoms. |
| Sacred bless | Improves Valkyries and Vans | Both lines are capital-only and compete with other capital production. |
| Awake expansion body | Reduces pressure on ordinary human troops | Performance depends on settings, map, chassis, scales, bless, script, and opponents. |

No exact design is endorsed without the game settings, map, opponents, legal chassis, and a versioned performance record.

## Vanheim matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Javelins, protected frontage, multiple Einhere attacks, available area effects, and controlled flanks | Paying only for elite capital units when cheap bodies are the constraint. |
| Heavy armour | Great swords, axes, buffs, fatigue plans, Earth magic, and suitable rare-path spells | Assuming ordinary spears and javelins solve protection unaided. |
| Accurate missiles | Hirdman protection, screens, speed, stealth approaches, and target disruption | Exposing lightly protected Skinshifters, mages, or landing Valkyries. |
| High-Defence elites | Multiple attacks, buffs, fatigue, morale pressure, and magic that avoids Defence | Relying on one expensive lance contact. |
| Large or trample-resistant targets | Protected lines, Einhere attacks, Skinshifter weapons, magic, and other counters | Treating Fay Boar trample as universal damage. |
| Fast flankers or flyers | Guards, layered formations, reserves, and mage spacing | Leaving capital mages behind a thin human line. |
| Stealth raiders | Scouts, patrol plans, forts, mobile response, and route discipline | Assuming Vanheim's own stealth automatically reveals the enemy. |
| Underwater pressure | Coastal defence, legal amphibious assets, allies, summons, or other verified bridges | Scheduling national spells explicitly marked unusable underwater. |
| Magic-resistant elites | Physical packages, buffs, fatigue, multiple attack types, and resistance-aware spells | Treating Glamour or morale tools as guaranteed control. |

## Monthly Vanheim audit

- Is each fort limited by gold, resources, recruitment points, or commander turns?
- Are both Huskarl and both Hirdman records kept distinct?
- Is the capital commander queue solving a named Smith or Vanadrott requirement?
- Is the capital troop queue producing a deliberate Fay Boar, Valkyrie, or Van?
- Is every Smith and Vanadrott labelled by final paths?
- Are 0.4% repeated and 0.8% mixed branches excluded from guaranteed schedules?
- Are mundane commanders handling jobs that do not require magic, priesthood, stealth, or sailing?
- Are Earth, Air, Glamour, Blood, and Death gems or slaves reserved against research and forging plans?
- Does every national spell have research, a legal caster, resources, a laboratory where required, and a free mage-turn?
- Are sailing, trace-income, mounted, transformation, and summon claims still kept within their evidence boundary?
- Are heroes excluded from plans that must be repeatable?
- Are report coverage, fallback routes, supply, fatigue, morale, and replacement checked before battle?

## Vanheim unresolved evidence boundary

The following remain open:

1. live 6.36 random-path display and ordering for Dwarven Smiths and Vanadrotts;
2. ocean-sailing capacity, route blockers, coast rules, ownership interactions, and order resolution;
3. trace-income collection, timing, rounding, and hostile-control interactions;
4. glamour, illusion, stealth, detection, and patrol outcomes;
5. Skinshifter shape changes, wound transfer, equipment, regeneration, and post-battle state;
6. rider–mount damage, fatigue, separation, death, and remounting behaviour;
7. Fay Boar trample, supply contribution, congestion, and target selection;
8. Summon Valkyries placement, persistence, scripting, targeting, and combat behaviour;
9. Awaken Draugar forms, equipment, leadership use, persistence, and live resolution;
10. Four Directions selection order, repeat casting, uniqueness, and the complete live result;
11. item-rebate display, price, rounding, stacking, and version-specific forge interaction;
12. blood hunting, sacrifice, dominion, unrest, and transport outcomes;
13. hero arrival timing, late-hero semantics, and live special behaviour;
14. expansion-party sizes, formations, scripts, blessings, matchup performance, and casualty ranges;
15. R-047, R-058, and every comparable parked engine-dependent investigation.

These are evidence gaps, not invitations to guess. Runtime testing and preparation of new test assets remain paused.

# Part XXXII: Middle Age Caelum, Reign of the Seraphim

## Caelum one-page command brief

Middle Age Caelum turns flying recruitment, strong repeatable Air magic, cold-resistant ice troops, cheap specialist mages, and a large national summon list into reach. Every fort can recruit all eight national commanders and eight ordinary troop types. The capital adds Wingless, Temple Guards, and Blizzard Warriors through two sites, but it does not monopolise the main mage line. This makes additional forts useful immediately rather than waiting for a capital-only research engine.

The basic plan is:

- use flying troops to shorten concentration time while confirming every route and supply position;
- match cheap Spire Horn bodies, archers, protected Airya infantry, Storm Guards, Iceclads, and Mammoths to the reported target;
- recruit mundane leadership when a mage's paths are not required for command;
- use Ice Crafters, Spire Horn Seraphs, and Caelian Seraphs for repeatable Water and Air work;
- label every High Seraph by its final W/S/D rolls and keep rare branches out of guaranteed schedules;
- treat the Seraphine's pinned Fire random as disputed metadata until the manual conflict is resolved;
- connect each national spell to its actual caster, research level, gem type, and free mage-turn;
- protect laboratories, forts, and fallback provinces so mobility does not outrun replacement and information.

Caelum converts gold, resources, recruitment points, Air and Water income, flying movement, mage-turns, and research into rapid concentration. Its main risks are fragile low-hit-point troops, temperature-dependent equipment, expensive High Seraphs, capital-only sacred replacement, narrow native access to Astral and Death, almost no secure Fire, and a national ritual list whose names promise more than ordinary recruitment can immediately cast.

## Caelum evidence and ruleset

This chapter covers unmodded Middle Age Caelum on the Book I 6.36 live baseline. The revision-2 official manual controls the player-facing roster, costs, recruitment markings, visible paths, national summary, spell tables, and ritual descriptions. Nation ID 71, recruitment memberships, random masks, site fields, spell restrictions, item rebates, and hero assignments are cross-checked against the pinned 6.35 Inspector export at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The Seraphine sources conflict: the manual prints H1 without a random marker, while the pinned object row carries a 20% F1 roll. That branch is preserved as pinned metadata and excluded from any plan that must work in the current client. Exact flying movement, storm resolution, ice-armour scaling, Ice Fort protection, Guardian Spirits, Mammoth mounts, national summon behaviour, remote Drugvant outcomes, hero timing, and battlefield performance remain unresolved. No runtime test, replay, save, or new test asset was used.

## Caelum conversion chain

```text
flying recruitment, cold preference, ice equipment, ordinary-fort mages, and capital sites
-> provinces, forts, laboratories, temples, scouts, replacement routes, and gem income
-> labelled Water, Air, Astral, and Death access with protected mage-turns
-> research, searching, forging, battlefield magic, and conditional national rituals
-> surviving armies, rapid concentration, raids, sieges, claims, and strategic depth
```

The fragile arrows are troop durability, morale, temperature, supply, laboratory coverage, the cost of High Seraphs, and the gap between possessing a national spell and possessing its caster. Flight increases reach but does not supply intelligence, legal routes, safe landings, or replacements.

## Caelum national rules that shape planning

| Rule or asset | Source-backed fact | Planning consequence |
| --- | --- | --- |
| Flying population | Most ordinary commanders and troops fly. | Forces can concentrate quickly, but the exact strategic route must still be legal and confirmed. |
| Cold preference | The nation prefers Cold +3 and has a Cold scale limit of +1. | Cold is part of the roster's equipment and resistance environment, not merely an aesthetic scale choice. |
| Ice equipment | Several units carry Ice Armor and magical ice weapons. | Protection and weapon properties matter, but exact temperature conversion remains outside this chapter's evidence. |
| Partial shock resistance | Spire Horn units commonly carry shock resistance and Storm Immunity. | Storm and lightning plans can be considered by unit, but neither trait is universal across the roster. |
| Ice Forts | Caelum uses Ice Forts, and the manual says forts reduce cold-scale deaths by one step. | Fort planning has a national climate consequence; exact timing and eligibility remain unresolved. |
| Guardian Spirits | The manual lists Guardian Spirits under priests. | Priest recruitment has a national role, but trigger and target behaviour are not assumed. |
| National magic split | Positive Yazata rituals use Astral; Daeva rituals use Death and Fire. | Research must follow legal path construction rather than the theme of the spell list. |

## Caelum recruitment geography

All eight national commanders appear in the ordinary-fort membership. Eight troop types also appear in the ordinary-fort list. The capital sites add three troops: Ravens Vale supplies Wingless, while the Citadel of Frozen Crystal supplies Temple Guards and Blizzard Warriors.

This is a favourable decentralisation pattern. New forts can recruit scouts, leaders, priests, forge specialists, Air mages, Water–Air mages, and High Seraphs without waiting on the capital. Capital congestion falls mainly on the three site troops. The dossier keeps site membership distinct because capital-only availability is a real replacement constraint.

## Complete Caelum commander membership

| Commander | Gold | Resources | Rec points | Printed paths | Verified recruitment |
| --- | ---: | ---: | ---: | --- | --- |
| Caelian Scout | 35 | 13 | 1 | none | Forts |
| Airya Noble | 70 | 38 | 1 | none | Forts |
| Storm General | 95 | 36 | 1 | none | Forts |
| Seraphine | 95 | 2 | 1 | H1 | Forts |
| Ice Crafter | 65 | 3 | 2 | W1 | Forts |
| Spire Horn Seraph | 65 | 1 | 2 | A1 | Forts |
| Caelian Seraph | 175 | 2 | 2 | A2 W1 | Forts |
| High Seraph | 355 | 3 | 4 | A3 W2 ?1 | Forts |

Eight commander records reconcile. The roster offers cheap scouting, two mundane leaders, inexpensive single-path specialists, a repeatable A2 W1 mage, and an expensive high-path random mage from every fort.

## Caelum commander jobs

| Commander | Source-backed role | Important limit |
| --- | --- | --- |
| Caelian Scout | Flying stealth scout | Thirty-five gold and thirteen resources are not free if reports can be supplied more cheaply elsewhere. |
| Airya Noble | Flying leadership-75 commander | High resource cost and no magic make it a deliberate army purchase. |
| Storm General | Flying leadership-100 commander with Storm Immunity | Thirty-six resources compete with protected troops. |
| Seraphine | Sacred H1 priest, stealthy flying leader | Fire access is disputed; Guardian Spirit behaviour remains unresolved. |
| Ice Crafter | Cheap W1 mage with Forge Bonus 1 | Two recruitment points; live rebate and forge-bonus arithmetic were not observed. |
| Spire Horn Seraph | Cheap A1 researcher and support mage | Low leadership and only one fixed path. |
| Caelian Seraph | Repeatable A2 W1 mage | More than twice the gold of either single-path specialist. |
| High Seraph | A3 W2 random mage, research and high-path platform | 355 gold and four recruitment points make every turn expensive. |

## Complete Caelum troop membership

| Troop | Gold | Resources | Rec points | Verified recruitment |
| --- | ---: | ---: | ---: | --- |
| Spire Horn Militia | 8 | 5 | 5 | Forts |
| Spire Horn Archer | 10 | 6 | 9 | Forts |
| Airya Light Infantry | 10 | 11 | 9 | Forts |
| Spire Horn Warrior | 10 | 7 | 9 | Forts |
| Airya Infantry | 10 | 16 | 9 | Forts |
| Iceclad | 15 | 40 | 21 | Forts |
| Storm Guard | 15 | 31 | 21 | Forts |
| Mammoth Rider | 120 | 5 | 9 | Forts |
| Wingless | 10 | 11 | 9 | Capital only, via Ravens Vale |
| Temple Guard | 20 | 42 | 23 | Capital only, sacred |
| Blizzard Warrior | 20 | 13 | 23 | Capital only, sacred |

Eleven troop records reconcile. The separate Mammoth and Mammoth Archer records describe the Mammoth Rider's mount and co-riders; they are not counted again as independent recruits.

## Caelum troop jobs

| Troop | Source-backed role | Important limit |
| --- | --- | --- |
| Spire Horn Militia | Very cheap flying spear body | Morale 8 and Protection 6 make it a screen, not a reliable elite. |
| Spire Horn Archer | Flying short-bow unit with Storm Immunity | Protection 6 and ordinary bow output require target and formation discipline. |
| Airya Light Infantry | Flying ice-lance infantry | Better Defence than militia, but still low hit points and moderate protection. |
| Spire Horn Warrior | Cheap flying lance infantry with Storm Immunity | Contact performance depends on fatigue, formation, and target protection. |
| Airya Infantry | Flying Ice Armor 1 sword line | Sixteen resources buy more protection but still only nine hit points. |
| Iceclad | Heavily protected flying ice-lance line | Forty resources and twenty-one recruitment points sharply limit volume. |
| Storm Guard | Protected flying storm line | Thirty-one resources and twenty-one recruitment points compete with other premium troops. |
| Mammoth Rider | Mounted trampling package with two co-riders | Mount, trample, routing, and co-rider resolution remain runtime questions. |
| Wingless | Grounded high-morale capital infantry | Capital-only and unable to join the roster's normal flight pattern. |
| Temple Guard | Heavily protected sacred capital guard | Forty-two resources and capital-only replacement constrain scale. |
| Blizzard Warrior | Sacred capital frost-bow unit | Low protection and capital-only replacement make target choice important. |

## Caelum capital sites

| Site | ID | Verified fields | Planning boundary |
| --- | ---: | --- | --- |
| The Citadel of Frozen Crystal | 11 | A3 and W2 monthly gems, Cold scale cap 2 field, Temple Guard and Blizzard Warrior recruitment | Supplies the main gem income and two sacred troop queues; hidden effects are not inferred. |
| Ravens Vale | 18 | Death-path classification and Wingless recruitment | Provides no monthly Death-gem field in the pinned row. |

The capital begins with strong Air and Water income, but the negative ritual branch demands Death and Fire. Ravens Vale's Death classification must not be mistaken for printed monthly Death gems. Death and Fire treasuries still require searching, events, trades, or another verified source.

## Caelum capital-queue control

The capital commander queue is not uniquely privileged: every national commander is available from ordinary forts. This lets the capital recruit the same research or leadership mix as other forts while its troop queue handles the three site troops.

Capital troop choices should answer a named need. Wingless provide grounded morale and low-cost bodies. Temple Guards convert large resource and recruitment-point budgets into protected sacreds. Blizzard Warriors supply sacred frost bows with a much lower resource cost. Recruiting the most expensive option by habit can waste the capital's particular advantage.

## Caelum recruitable magic access

| Path floor | Repeatable source | Reliability |
| --- | --- | --- |
| A1 | Spire Horn Seraph | guaranteed |
| A2 W1 | Caelian Seraph | guaranteed |
| A3 W2 | High Seraph | guaranteed |
| H1 | Seraphine | guaranteed |
| W1 and Forge Bonus 1 | Ice Crafter | guaranteed |
| W3, S1, or D1 on High Seraph | one guaranteed W/S/D roll | one branch per recruit |
| Second W, S, or D on High Seraph | independent 10% W/S/D roll | rare |
| F1 on Seraphine | pinned 20% row only | disputed against manual |

The fixed core is Air and Water. Astral and Death arrive through High Seraph randoms. Fire has no uncontested recruitable path in the manual. National spell planning must preserve those distinctions.

## Seraphine Fire-path discrepancy

The manual prints the Seraphine as H1 with no `?1`. The pinned 6.35 object row gives one 20% roll from mask `128`, which resolves to Fire. The records cannot both describe the same visible path line completely.

The safe rule is narrow: Seraphines are guaranteed H1. A 20% F1 branch exists in the pinned structured record but is not scheduled, counted as live access, or used to justify Fire research. If a current authoritative export or observed recruitment record later confirms it, the correction can be made locally.

## High Seraph random-path probabilities

The High Seraph has fixed A3 W2, one guaranteed pick from W/S/D, and an independent 10% pick from the same three-path mask.

| Final random class | Probability | Examples |
| --- | ---: | --- |
| Guaranteed pick only | 90% | W1, S1, or D1 at 30% each |
| Same path twice | 3.333% total | W2, S2, or D2 at 1.111% each |
| Two different paths | 6.667% total | W1S1, W1D1, or S1D1 at 2.222% each |

Including the fixed paths, a named W/S/D random appears at least once on 35.556% of recruits. Water is always present at W2 before randoms, so the random outcomes produce W3 or rarely W4 rather than a new path. These probabilities are derived from the pinned masks and are not a sample of live recruitment.

## Caelum dependable path jobs

- Ice Crafters provide cheap W1 searching, forging, and low-path Water work.
- Spire Horn Seraphs provide cheap A1 research, searching, and low-path Air work.
- Caelian Seraphs provide repeatable A2 W1 mixed access without relying on a random.
- High Seraphs provide repeatable A3 W2 and carry every recruitable Astral or Death branch.
- Seraphines provide H1 priesthood and ordinary sacred support.

Mundane commanders should handle army leadership when their lower price or stronger leadership preserves a mage-turn. A flying mage is still an expensive researcher, searcher, forger, ritualist, or combat caster whose turn has an opportunity cost.

## Caelum rare-path endpoints

| Endpoint | Unassisted recruitable route | Frequency boundary |
| --- | --- | --- |
| A3 D1 for Parting of the Soul | High Seraph with at least one D pick | 35.556% in pinned distribution |
| S2 for Summon Yazatas | High Seraph with double S | 1.111% |
| S2 W1 for Call Ahurani | High Seraph with double S; fixed W2 already qualifies | 1.111% |
| S3 or higher | none unassisted | requires another bridge |
| D2 F1 for Call Daevas | none uncontested on one recruit | requires Fire plus Death construction |
| D3 F1, D3 F2, or D4 F1/F2 | none unassisted | late path project |

National access is therefore uneven. Parting of the Soul is repeatably reachable through a common High Seraph branch. The first two positive rituals require a rare double Astral result. The higher positive and all negative rituals require boosters, empowerment, summons, a Pretender, or another verified bridge.

## Caelum national spell map

| Name | Research | Requirement | Cost | Access warning |
| --- | --- | --- | ---: | --- |
| Parting of the Soul | Thaumaturgy 6 | D1 A1 | 40 fatigue | D-random High Seraph qualifies. |
| Call Ahurani | Conjuration 5 | S2 W1 | 12 pearls | Double-S High Seraph qualifies. |
| Summon Yazatas | Conjuration 5 | S2 | 12 pearls | Double-S High Seraph qualifies. |
| Call Celestial Yazad | Conjuration 6 | S4 | 40 pearls | No unassisted recruit qualifies. |
| Call Fravashi | Conjuration 7 | S3 | 30 pearls | No unassisted recruit qualifies. |
| Call Amesha Spenta | Conjuration 8 | S5 | 60 pearls | No unassisted recruit qualifies. |
| Call Daevas | Conjuration 5 | D2 F1 | 12 Death gems | No uncontested unassisted recruit qualifies. |
| Call Jahi | Conjuration 5 | D3 F1 | 15 Death gems | No unassisted recruit qualifies. |
| Call Yata | Conjuration 6 | D3 F2 | 40 Death gems | No unassisted recruit qualifies. |
| Call of the Drugvant | Thaumaturgy 7 | D4 F1 | 15 Death gems | No unassisted recruit qualifies. |
| Call Greater Daeva | Conjuration 8 | D4 F2 | 60 Death gems | No unassisted recruit qualifies. |

Researching a national spell does not create the missing path, gems, laboratory, or mage-turn. Each row is a project with five gates: research, caster, path construction, treasury, and opportunity cost.

## Positive summon branch

Call Ahurani and Summon Yazatas are the only positive rituals an unassisted recruit can reach, and only a double-S High Seraph does so. That result appears on 1.111% of High Seraphs in the pinned distribution. The nation cannot build a reliable opening around finding it.

Call Fravashi, Call Celestial Yazad, and Call Amesha Spenta require S3, S4, and S5. A legal plan must name the booster, empowerment, summoned mage, Pretender, or other bridge that creates each threshold. The printed summoned paths may open further work, but their live arrival state, slots, uniqueness, and strategic behaviour remain untested here.

## Negative summon branch

The Daeva line begins at D2 F1 and rises to D4 F2. High Seraphs can rarely reach D2 but have no uncontested Fire. The disputed Seraphine branch, even if present, sits on a separate commander. Paths on two commanders cannot be combined to cast one ritual.

This branch therefore starts with path construction and a Death-gem economy. Call Daevas, Call Jahi, Call Yata, and Call Greater Daeva should be treated as conditional objectives. The spell list is strategically relevant because it defines possible payoffs, but it does not prove routine access.

## Call of the Drugvant boundary

Call of the Drugvant is a Thaumaturgy-7 remote ritual requiring D4 F1 and fifteen Death gems. The manual describes a range-four hostile-province effect that greatly increases unrest and brings bandits and Daevas.

The description establishes purpose, not exact resolution. Unrest amount, force composition, ownership checks, defence, event timing, immunity, and repeated-cast behaviour remain unresolved. Version 6.08 removed Shinuyama's unintended access while retaining Caelum's national restriction.

## Caelum item rebates

| Item | Construction | Requirement | Immediate source |
| --- | ---: | --- | --- |
| Ice Sword | 1 | W1 | Ice Crafter, Caelian Seraph, or High Seraph |
| Ice Lance | 1 | W1 | Ice Crafter, Caelian Seraph, or High Seraph |
| Ice Aegis | 3 | W2 | High Seraph |
| Ice Helmet | 3 | W1 | Ice Crafter, Caelian Seraph, or High Seraph |

The pinned snapshot records four rebate links and no Caelum-restricted item row. This makes Ice Crafters natural forge candidates, but the dossier does not claim an exact live price or a stacking formula between the national rebate and Forge Bonus 1. Every forge order still consumes gems, research, a laboratory, and a mage-turn.

## Caelum hero boundary

| Fixed name | Structured identity | Paths | Safe use |
| --- | --- | --- | --- |
| Caelos | Sacred One | H1 | contingent sacred leadership or priest support |
| Zaelinys | Harab Seraphine | D2 H2 | contingent Death and priest access |

Neither hero belongs in a schedule that must work every game. Zaelinys can change the Death threshold if present, but arrival timing and special behaviour remain unresolved.

## Caelum patch reconciliation

Dominions 6.08, published 6 March 2024, corrected Shinuyama's unintended access to Call of the Drugvant. This confirms the spell-assignment boundary without changing Caelum's own access. Dominions 6.12, published 29 April 2024, divided Ice Protection into Ice Protection and Ice Armor; the current manual uses the later terminology.

No later official ledger entry through 6.36 directly names the High Seraph, Seraphine, Caelian capital sites, Parting of the Soul, or Caelum's summon list. Silence is not proof that every historical value remained unchanged; the manual controls player-facing descriptions and the pinned data remains labelled 6.35.

## Caelum opening priorities

1. Check whether gold, resources, recruitment points, or commander turns limit each fort.
2. Use cheap flying bodies for coverage only where their morale and protection are adequate.
3. Decide whether the next mage-turn needs W1, A1, A2 W1, priesthood, or the High Seraph's A3 W2 random package.
4. Label every High Seraph immediately and keep S2 or D2 branches out of guaranteed plans.
5. Keep the Seraphine Fire discrepancy out of the baseline plan.
6. Add report coverage before fast armies move beyond reliable information.
7. Track Air and Water income separately from the Death, Fire, and Astral costs of national projects.
8. Protect the capital troop queue and choose Wingless, Temple Guards, or Blizzard Warriors for a named role.
9. Build additional forts because they reproduce the entire commander roster.
10. Maintain a grounded or conventional response plan for terrain, weather, or enemies that punish flight.

These are planning controls. Exact expansion parties, flight routes, formations, scripts, blesses, and casualty expectations remain open.

## Caelum recruitment packages to compare

### Cheap flying screen

Spire Horn Militia cost eight gold and five resources, while ordinary Spire Horn Warriors and Airya Light Infantry cost ten gold. The package produces bodies and rapid concentration at low gold cost. Low morale, low hit points, limited protection, and fatigue make leadership and target selection decisive.

### Archer wing

Spire Horn Archers provide flying short bows and Storm Immunity. They can reposition and add missile pressure, but short-bow damage, accuracy, ammunition, landing risk, and enemy armour decide value. Flight does not require the archers to be sent into unsupported melee.

### Protected ice line

Airya Infantry, Iceclads, and Storm Guards exchange resources and recruitment points for higher protection. Iceclads are the most resource-heavy ordinary unit at forty resources. Storm Guards add the Spire Horn resistance and storm package. A fort's production should compare number of bodies, formation width, and replacement speed rather than protection alone.

### Mammoth package

Mammoth Riders cost 120 gold but only five resources and nine recruitment points in the manual table. They provide a mounted trampling option that uses a different bottleneck from Iceclads. Morale, size, congestion, friendly displacement, target size, mount damage, co-riders, routing, and remounting all remain matchup or runtime questions.

### Capital grounded sacreds

Temple Guards and Blizzard Warriors are sacred but do not print flight. Temple Guards supply a protected contact line at high resource cost; Blizzard Warriors supply frost bows with lower resources. Wingless are not sacred but provide capital-only grounded infantry with Morale 14. The package should be judged as a capital replacement system, not simply folded into the ordinary flying army.

## Caelum research response tree

### Branch A: repeatable Air support

Spire Horn Seraphs, Caelian Seraphs, and High Seraphs provide A1, A2, and A3 from every fort. Research can therefore favour general Air spells at thresholds the recruited roster actually meets. The correct branch depends on enemy shock resistance, formation, weather, battlefield size, fatigue, and available Air gems.

### Branch B: Water, Construction, and ice forging

Ice Crafters provide cheap W1 and Forge Bonus 1; Caelian Seraphs add A2 W1; High Seraphs begin at W2. Construction 1 and 3 expose all four rebate-linked ice items. The branch must still compare forging against research, searching, combat casting, gem reserves, and unresolved price stacking.

### Branch C: Thaumaturgy and Parting of the Soul

Thaumaturgy 6 unlocks Parting of the Soul at D1 A1. Any High Seraph with a Death pick qualifies because A3 is fixed. This is the most accessible national spell outside the disputed Seraphine field, but target immunity, magic resistance, range, fatigue, and battlefield conditions still control use.

### Branch D: Conjuration 5 positive summons

Call Ahurani and Summon Yazatas both require S2. Only a double-S High Seraph reaches that threshold unassisted, at 1.111% per High Seraph. Conjuration 5 should therefore be justified by its general spell list unless the caster already exists.

### Branch E: higher Astral summons

Call Fravashi, Call Celestial Yazad, and Call Amesha Spenta require S3 through S5. The plan begins with an explicit bridge and pearl budget. Researching Conjuration 6-8 before the path chain exists can create a costly dead endpoint.

### Branch F: Death–Fire summons and remote pressure

The negative branch requires D2 F1 through D4 F2. No uncontested unassisted recruit qualifies. A viable route must document Death gems, Fire access, boosters or empowerment, laboratory turns, and the final caster. Call of the Drugvant also requires Thaumaturgy 7 and preserves its remote-event uncertainty.

## Caelum battlefield packages

### Flying line with separate command

Cheap Spire Horn or Airya troops hold frontage under an Airya Noble or Storm General while mages remain protected. The package preserves mage-turns and lets the army concentrate quickly. Low hit points, morale, missiles, fatigue, and enemy breakthrough speed remain central.

### Storm-compatible group

Spire Horn Archers, Warriors, Storm Guards, Scouts, and Storm Generals print Storm Immunity. Other Airya elements do not universally share it. A storm plan must therefore check every unit and caster rather than treating Caelum as one homogeneous flying roster.

### Protected flying group

Iceclads, Storm Guards, and Airya Infantry provide progressively expensive protected bodies. Buffs and Air support can improve the package, but temperature, armour-piercing or negating damage, fatigue, and replacement cost determine whether protection converts into survival.

### Mammoth breakthrough group

Mammoths can be placed behind or beside a line intended to create a controlled contact point. The package requires leadership, morale support, formation space, and a plan for targets that resist trample. Exact mount and co-rider resolution remains open.

### Capital sacred group

Temple Guards and Blizzard Warriors use the bless and capital recruitment in different ways. One is a protected grounded guard; the other is a lightly protected frost-bow unit. Priests, resource limits, replacement time, and the opponent decide whether either belongs in the main army.

### Random-path High Seraph group

High Seraphs with Water, Astral, Death, or mixed results should be labelled and scripted from their actual paths. A D-random enables Parting of the Soul; a double-S result enables two Conjuration-5 rituals. Rare results are opportunities, not the baseline identity of every High Seraph.

## Caelum information and pressure network

Caelian Scouts combine flight and stealth, while most of the army can move rapidly. That reach can reveal threats, reinforce distant fronts, and threaten weak points, but it does not reveal enemy orders or make every route legal.

A safe network layers scouts, province reports, laboratories, fallback forts, mundane commanders, gem transport, and local reserves. Flying groups should arrive where replacements, supply, retreat routes, and supporting mages can follow. Speed without reporting can produce isolated armies rather than strategic pressure.

## Caelum Pretender families

| Family | What it can solve | What it must not conceal |
| --- | --- | --- |
| Astral bridge | Makes S3-S5 national summons practical | Pearls, research, boosters, laboratories, and mage-turns still matter. |
| Death–Fire bridge | Opens Daevas, Jahi, Yata, Drugvant, and Greater Daeva projects | The path pair does not create a Death-gem treasury or safe caster availability. |
| Economy and infrastructure | Funds forts, High Seraphs, laboratories, and resource-heavy ice troops | Gold does not create local resources, recruitment points, gems, or capital sacred turns. |
| Sacred bless | Improves Temple Guards, Blizzard Warriors, Seraphines, and national summons | The two recruitable sacred troops are capital-only and grounded. |
| Awake expansion body | Reduces pressure on fragile early troops | Performance depends on settings, map, chassis, scales, script, and opponents. |
| Resistance or climate support | Complements cold and shock themes or covers missing defences | National flavour is not proof of the best bless or scale package. |

No exact design is endorsed without the game settings, map, opponents, legal chassis, and a versioned performance record.

## Caelum matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Archers, protected frontage, Mammoths where legal, Air magic, and rapid concentration | Using only expensive Iceclads when cheap width is the constraint. |
| Heavy armour | Buffs, fatigue, magic, Mammoth pressure where suitable, and higher-damage weapons | Assuming short bows and ordinary ice spears solve protection unaided. |
| Accurate missiles | Screens, protected units, speed, battlefield control, and target disruption | Exposing nine-hit-point mages and archers without spacing or guards. |
| Shock-resistant enemies | Water, physical troops, buffs, fatigue, and non-shock spells | Building the complete research plan around lightning. |
| Fire pressure | Cold resistance does not equal Fire resistance; use spacing, protection, counters, and faster contact | Treating the climate theme as universal elemental defence. |
| Storms or anti-flight conditions | Check Storm Immunity per unit, use grounded capital troops, and preserve conventional formations | Assuming every Caelian flies under every condition. |
| Large or trample-resistant targets | Protected lines, magic, concentrated attacks, and other counters | Treating Mammoths as universal breakthrough. |
| Fast flankers or flyers | Guards, layered formations, reserves, and mage spacing | Leaving fragile Seraphs behind a thin airborne line. |
| Underwater pressure | Coastal defence, legal amphibious summons, allies, or another verified bridge | Scheduling spells marked unusable underwater or assuming flight solves the boundary. |
| Raiding and dispersed threats | Scouts, flying reserves, forts, and distributed commander recruitment | Sending every mobile unit into one offensive concentration. |

## Monthly Caelum audit

- Is each fort limited by gold, resources, recruitment points, or commander turns?
- Are mundane commanders handling jobs that do not need magic or priesthood?
- Is the next mage purchase solving W1, A1, A2 W1, priesthood, or a High Seraph threshold?
- Is every High Seraph labelled by final W/S/D paths?
- Is the Seraphine Fire branch still excluded from guaranteed plans?
- Are ordinary and capital-site troop replacements tracked separately?
- Are Air and Water income being confused with the pearls, Death gems, and Fire access required by national rituals?
- Does every national spell have research, a legal caster, the correct treasury, a laboratory where required, and a free mage-turn?
- Are rare S2 and D2 outcomes excluded from schedules that must be repeatable?
- Are scouts and fallback routes keeping pace with flying armies?
- Are temperature, storm, supply, fatigue, morale, and retreat routes checked before battle?
- Are heroes excluded from plans that must work every game?

## Caelum unresolved evidence boundary

The following remain open:

1. whether the Seraphine's pinned 20% F1 random is present and displayed in live 6.36;
2. live High Seraph random-path display and ordering;
3. strategic flying routes, terrain permissions, blockers, and order resolution;
4. storm creation, flight suppression, Storm Immunity, and mixed-army behaviour;
5. Ice Armor protection across temperature, stacking, and equipment changes;
6. Ice Fort cold-scale death protection, eligibility, timing, and ownership changes;
7. Guardian Spirit trigger, target, duration, replacement, and combat behaviour;
8. Mammoth mount, co-rider, trample, displacement, routing, death, and remounting resolution;
9. national summon placement, arrival state, slots, leadership, uniqueness, and repeat casting;
10. Call of the Drugvant unrest, attackers, ownership, defence, and event timing;
11. item-rebate display, live price, rounding, and interaction with Forge Bonus 1;
12. hero arrival timing and live special behaviour;
13. expansion-party sizes, formations, scripts, blesses, matchup performance, and casualty ranges;
14. disciple, allied-army, and underwater edge cases beyond explicit manual wording;
15. R-047, R-058, and every comparable parked engine-dependent investigation.

These are evidence gaps, not invitations to guess. Runtime testing and preparation of new test assets remain paused.

<!-- GENERATED REMAINING MA DOSSIERS START -->

# Part XXXIII: Middle Age Phlegra, Deformed Giants

## Phlegra one-page command brief

Middle Age Phlegra converts enslaved human levies and scarce giant elites into expansion, research, and strategic pressure. The pinned roster resolves 9 commander identities and 6 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 6 active nation-restricted spell records. Its chief planning risks are giant recruitment limits, unrest, and replacement speed.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Phlegra evidence and ruleset

This dossier covers unmodded Middle Age Phlegra on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 51, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Phlegra object without a named official record. No runtime test, replay, save, or new test asset was used.

## Phlegra conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Phlegra recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 7 | 6 | Direct pinned membership rows |
| Regional or coastal | 0 | 1 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 2 | 0 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Phlegra commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3129 | Trophimos Commander | none | 100 |
| 3130 | Trophimos Priest | H1; random: 100% ×1 mask 1920 link 1 | 50 |
| 3131 | Trophimos Sage | none; random: 100% ×1 mask 1920 link 2 | 10 |
| 3161 | Shackled Mage | none; random: 100% ×1 mask 1920 link 1 | 0 |
| 3162 | Trophimos Oppressor | F1 E1; random: 100% ×1 mask 768 link 1 | 50 |
| 3135 | Cyclops Chieftain | none | 20 |
| 3141 | Cyclops Shepherd Shaman | N1 | 35 |
| 3139 | Phlegran Tyrant | F3 E2 D1; random: 100% ×1 mask 5504 link 1; 10% ×1 mask 5504 link 1 | 90 |
| 3138 | Elder Cyclops | F2 A1 E2; random: 100% ×1 mask 1920 link 1; 10% ×1 mask 1920 link 1 | 50 |


## Phlegra troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 3132 | Helote Archer | 10 | 0 | 6 | ordinary body |
| 3133 | Helote Warrior | 10 | 0 | 7 | ordinary body |
| 3134 | Helote Soldier | 10 | 0 | 7 | ordinary body |
| 3136 | Cyclops Warrior | 42 | 5 | 13 | ordinary body |
| 3137 | Cyclops Hurler | 42 | 5 | 13 | ordinary body |
| 3140 | Gigante Warrior | 62 | 9 | 14 | ordinary body |


## Phlegra mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3130 | Trophimos Priest | H1; random: 100% ×1 mask 1920 link 1 | 50 |
| 3131 | Trophimos Sage | none; random: 100% ×1 mask 1920 link 2 | 10 |
| 3161 | Shackled Mage | none; random: 100% ×1 mask 1920 link 1 | 0 |
| 3162 | Trophimos Oppressor | F1 E1; random: 100% ×1 mask 768 link 1 | 50 |
| 3141 | Cyclops Shepherd Shaman | N1 | 35 |
| 3139 | Phlegran Tyrant | F3 E2 D1; random: 100% ×1 mask 5504 link 1; 10% ×1 mask 5504 link 1 | 90 |
| 3138 | Elder Cyclops | F2 A1 E2; random: 100% ×1 mask 1920 link 1; 10% ×1 mask 1920 link 1 | 50 |


The highest fixed recruitable paths resolved in these rows are Fire 3, Air 1, Earth 2, Death 1, Nature 1, Holy 1. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Phlegra capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 196 | The Burning Fields | F1, E1, D1 | Phlegran Tyrant |
| 197 | Fortress of the Cyclopes | F1, E1 | Elder Cyclops |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Phlegra national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 254 | Summon Hound of Twilight | Conjuration 5 | E2 D1 | 3 |
| 255 | Sow Dragon Teeth | Enchantment 6 | E2 | 1 |
| 256 | Bind Keres | Conjuration 6 | D2 | 12 |
| 264 | Gigantomachia | Thaumaturgy 7 | E4 F4 | 60 |
| 270 | Forge Brass Bull | Construction 6 | F3 E3 | 25 |
| 369 | Procession of the Underworld | Conjuration 5 | D3 | 13 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Phlegra national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 133 | God-Slayer Spear | 3 | E1 | restricted |
| 224 | Oppressors Headband | 1 | E3 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Phlegra hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3163 | Theurg Tyrant | F1 A2 E2 S3 H3 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Phlegra army identities

- Sacred roster: no sacred troop identified in the reconciled recruit rows.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: enslaved human levies and scarce giant elites.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Phlegra opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Phlegra fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Phlegra, the most likely planning failure is giant recruitment limits, unrest, and replacement speed. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Phlegra research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Phlegra magic-access ladder

The fixed-path ceiling is Fire 3, Air 1, Earth 2, Death 1, Nature 1, Holy 1. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Phlegra battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Phlegra Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Phlegra matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Phlegra monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Phlegra unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Phlegra source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XXXIV: Middle Age Asphodel, Carrion Woods

## Asphodel one-page command brief

Middle Age Asphodel converts Carrion Woods freespawn, stealth, and Death–Nature magic into expansion, research, and strategic pressure. The pinned roster resolves 8 commander identities and 10 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 12 active nation-restricted spell records. Its chief planning risks are population decline, freespawn composition, and living infrastructure.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Asphodel evidence and ruleset

This dossier covers unmodded Middle Age Asphodel on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 53, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Asphodel object without a named official record. No runtime test, replay, save, or new test asset was used.

## Asphodel conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Asphodel recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 8 | 10 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 0 | 0 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Asphodel commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 430 | Black Harpy | none | 10 |
| 2485 | Satyr Commander | none | 50 |
| 1534 | Minotaur Lord | none | 75 |
| 2311 | Centaur Hierophant | H1; random: 100% ×1 mask 12288 link 1; 10% ×1 mask 1024 link 1 | 50 |
| 2312 | Centauride Hierophantide | H1; random: 100% ×1 mask 12288 link 1; 10% ×1 mask 512 link 1 | 50 |
| 901 | Black Dryad | D1 N1 G1 H2 | 50 |
| 2480 | Dryad Hag | D1 N2 G1 H2; random: 100% ×1 mask 22016 link 1; 10% ×1 mask 22016 link 1 | 10 |
| 709 | Panic Apostate | D2 N3; random: 100% ×1 mask 13824 link 1; 10% ×1 mask 13824 link 1 | 100 |


## Asphodel troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 239 | Harpy | 7 | 0 | 8 | flying, stealthy |
| 227 | Satyr Sneak | 12 | 1 | 9 | stealthy |
| 228 | Satyr | 12 | 1 | 9 | stealthy |
| 1532 | Satyr Warrior | 14 | 1 | 10 | ordinary body |
| 234 | Minotaur | 25 | 4 | 13 | ordinary body |
| 1533 | Minotaur Warrior | 27 | 4 | 14 | ordinary body |
| 2156 | Centauride | 18 | 3 | 11 | stealthy |
| 27 | Centaur | 20 | 3 | 11 | stealthy |
| 2157 | Centauride Warrior | 18 | 3 | 12 | stealthy |
| 1704 | Centaur Warrior | 22 | 3 | 12 | stealthy |


## Asphodel mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2311 | Centaur Hierophant | H1; random: 100% ×1 mask 12288 link 1; 10% ×1 mask 1024 link 1 | 50 |
| 2312 | Centauride Hierophantide | H1; random: 100% ×1 mask 12288 link 1; 10% ×1 mask 512 link 1 | 50 |
| 901 | Black Dryad | D1 N1 G1 H2 | 50 |
| 2480 | Dryad Hag | D1 N2 G1 H2; random: 100% ×1 mask 22016 link 1; 10% ×1 mask 22016 link 1 | 10 |
| 709 | Panic Apostate | D2 N3; random: 100% ×1 mask 13824 link 1; 10% ×1 mask 13824 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Death 2, Nature 3, Glamour 1, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Asphodel capital and national sites

No capital-site association row was found. Hidden, generated, or special national effects are not inferred.


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Asphodel national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 427 | Carrion Centaur | Enchantment 0 | N1 D1 | 8 |
| 428 | Carrion Lady | Enchantment 0 | N1 D1 | 16 |
| 429 | Carrion Lord | Enchantment 0 | N3 D2 | 35 |
| 430 | Quick Roots | Enchantment 0 | H1 | 0 |
| 431 | Regrowth | Enchantment 0 | H2 | 0 |
| 432 | Mend the Dead | Enchantment 0 | H2 | 0 |
| 433 | Puppet Mastery | Enchantment 0 | H3 | 0 |
| 434 | Carrion Growth | Enchantment 0 | H4 | 0 |
| 435 | Dark Slumber | Enchantment 4 | N4 D2 | 15 |
| 436 | Sleep Vines | Conjuration 3 | N1 G1 | 0 |
| 437 | Vengeful Vines | Conjuration 4 | N1 D1 | 0 |
| 1458 | Carrion Fortress | Alteration 0 | N3 D2 | 45 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Asphodel national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 38 | Thorn Spear | 3 | N1 | rebate |
| 39 | Thorn Staff | 3 | N1 | rebate |
| 40 | Vine Whip | 3 | N2 | rebate |
| 68 | Skull Standard | 5 | N2 D1 | rebate |
| 153 | Vine Bow | 5 | N1 | rebate |
| 522 | Carrion Seed | 5 | N1 D1 | restricted |
| 523 | Carrion Bow | 5 | N1 D1 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Asphodel hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 861 | Ettin Mandragora | H1 | assignment only; timing unresolved |
| 863 | Apostatic Warrior | D1 N2 H1 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Asphodel army identities

- Sacred roster: no sacred troop identified in the reconciled recruit rows.
- Flying roster: Harpy.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: Carrion Woods freespawn, stealth, and Death–Nature magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Asphodel opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Asphodel fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Asphodel, the most likely planning failure is population decline, freespawn composition, and living infrastructure. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Asphodel research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Asphodel magic-access ladder

The fixed-path ceiling is Death 2, Nature 3, Glamour 1, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Asphodel battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Asphodel Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Asphodel matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Asphodel monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Asphodel unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Asphodel source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XXXV: Middle Age Ermor, Ashen Empire

## Ermor one-page command brief

Middle Age Ermor converts dominion-created undead and powerful Death magic into expansion, research, and strategic pressure. The pinned roster resolves 0 commander identities and 0 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 23 active nation-restricted spell records. Its chief planning risks are population destruction, freespawn control, and hostile dominion.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Ermor evidence and ruleset

This dossier covers unmodded Middle Age Ermor on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 54, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Ermor object without a named official record. No runtime test, replay, save, or new test asset was used.

## Ermor conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Ermor recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 0 | 0 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 0 | 0 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Ermor commander roster

No ordinary membership rows are present in the pinned snapshot; site, freespawn, event, or special recruitment must be read separately.


## Ermor troop roster

No ordinary membership rows are present in the pinned snapshot; site, freespawn, event, or special recruitment must be read separately.


## Ermor mage and priest portfolio

No ordinary membership rows are present in the pinned snapshot; site, freespawn, event, or special recruitment must be read separately.


The highest fixed recruitable paths resolved in these rows are no fixed recruitable path in the ordinary/site commander rows. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Ermor capital and national sites

No capital-site association row was found. Hidden, generated, or special national effects are not inferred.


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Ermor national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 372 | Unholy Command | Divine 0 | H1 | 0 |
| 373 | Unholy Protection | Divine 0 | H1 | 0 |
| 374 | Unholy Blessing | Divine 0 | H1 | 0 |
| 375 | Unholy Power | Divine 0 | H1 | 0 |
| 376 | Unholy Protection | Divine 0 | H2 | 0 |
| 377 | Unholy Blessing | Divine 0 | H2 | 0 |
| 379 | Unholy Power | Divine 0 | H3 | 0 |
| 380 | Unholy Blessing | Divine 0 | H3 | 0 |
| 381 | Protection of the Sepulchre | Divine 0 | H3 | 0 |
| 382 | Power of the Sepulchre | Divine 0 | H4 | 0 |
| 383 | Revive Lictor | Conjuration 0 | D2 | 3 |
| 384 | Revive Censor | Conjuration 0 | D2 | 4 |
| 385 | Revive Acolyte | Conjuration 0 | D2 | 10 |
| 386 | Revive Bishop | Conjuration 0 | D2 | 16 |
| 387 | Revive Arch Bishop | Conjuration 0 | D3 | 23 |
| 388 | Revive Spectator | Conjuration 0 | D2 | 12 |
| 389 | Revive Dusk Elder | Conjuration 0 | D3 | 20 |
| 390 | Revive Wailing Lady | Conjuration 2 | D2 | 8 |
| 391 | Lictorian Guard | Conjuration 3 | D2 | 10 |
| 392 | Lamentation | Conjuration 5 | D3 | 25 |
| 393 | Great Lamentation | Conjuration 7 | D5 | 33 |
| 394 | Lictorian Legion | Conjuration 8 | D4 | 35 |
| 395 | Ermorian Legion | Enchantment 6 | D4 | 15 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Ermor national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 119 | Sword of Injustice | 9 | D4 | rebate |
| 229 | Black Laurel | 3 | D2 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Ermor hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 183 | Wraith King | D3 H2 | assignment only; timing unresolved |
| 555 | Arch Censor | none | assignment only; timing unresolved |
| 537 | Forgotten King | H3 | assignment only; timing unresolved |
| 2068 | Dusk Elder | F2 S3 D4 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Ermor army identities

- Sacred roster: no sacred troop identified in the reconciled recruit rows.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: dominion-created undead and powerful Death magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Ermor opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Ermor fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Ermor, the most likely planning failure is population destruction, freespawn control, and hostile dominion. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Ermor research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Ermor magic-access ladder

The fixed-path ceiling is no fixed recruitable path in the ordinary/site commander rows. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Ermor battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Ermor Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Ermor matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Ermor monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Ermor unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Ermor source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XXXVI: Middle Age Sceleria, The Reformed Empire

## Sceleria one-page command brief

Middle Age Sceleria converts Roman infantry, communions, and deliberate undead production into expansion, research, and strategic pressure. The pinned roster resolves 8 commander identities and 12 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 11 active nation-restricted spell records. Its chief planning risks are communion safety, upkeep, and mage-turn pressure.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Sceleria evidence and ruleset

This dossier covers unmodded Middle Age Sceleria on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 55, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Sceleria object without a named official record. No runtime test, replay, save, or new test asset was used.

## Sceleria conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Sceleria recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 6 | 10 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 2 | 2 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Sceleria commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 426 | Scout | none | 0 |
| 428 | Assassin | none | 0 |
| 671 | Centurion | none | 100 |
| 1386 | Legatus Legionis | none | 150 |
| 2244 | Scelerian Cultist | H1 | 10 |
| 669 | Thaumaturg | S1 D1 H2 | 10 |
| 1655 | Censor | none | 50 |
| 670 | Grand Thaumaturg | S2 D2 H3; random: 100% ×1 mask 6912 link 1; 10% ×1 mask 6912 link 1 | 10 |


## Sceleria troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 50 | Slinger | 10 | 0 | 7 | ordinary body |
| 662 | Velite | 10 | 0 | 10 | ordinary body |
| 663 | Alae Legionnaire | 10 | 0 | 10 | ordinary body |
| 664 | Hastatus | 10 | 0 | 11 | ordinary body |
| 665 | Principe | 11 | 0 | 12 | ordinary body |
| 666 | Triarius | 12 | 0 | 13 | ordinary body |
| 667 | Praetorian Guard | 13 | 0 | 14 | ordinary body |
| 668 | Standard | 10 | 0 | 10 | ordinary body |
| 11 | Retiarius | 12 | 0 | 14 | ordinary body |
| 12 | Gladiator | 12 | 0 | 14 | ordinary body |
| 1654 | Lictor | 12 | 0 | 14 | sacred |
| 809 | Shadow Vestal | 9 | 0 | 12 | sacred, undead, stealthy |


## Sceleria mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2244 | Scelerian Cultist | H1 | 10 |
| 669 | Thaumaturg | S1 D1 H2 | 10 |
| 670 | Grand Thaumaturg | S2 D2 H3; random: 100% ×1 mask 6912 link 1; 10% ×1 mask 6912 link 1 | 10 |


The highest fixed recruitable paths resolved in these rows are Astral 2, Death 2, Holy 3. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Sceleria capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 55 | Temple of the Dead | D3 | Censor, Lictor |
| 64 | Temple of the Spheres | S1 | Grand Thaumaturg |
| 148 | Campus Sceleris | D1 | Shadow Vestal |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Sceleria national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 372 | Unholy Command | Divine 0 | H1 | 0 |
| 373 | Unholy Protection | Divine 0 | H1 | 0 |
| 374 | Unholy Blessing | Divine 0 | H1 | 0 |
| 375 | Unholy Power | Divine 0 | H1 | 0 |
| 376 | Unholy Protection | Divine 0 | H2 | 0 |
| 377 | Unholy Blessing | Divine 0 | H2 | 0 |
| 378 | Apostasy | Divine 0 | H3 | 0 |
| 379 | Unholy Power | Divine 0 | H3 | 0 |
| 380 | Unholy Blessing | Divine 0 | H3 | 0 |
| 381 | Protection of the Sepulchre | Divine 0 | H3 | 0 |
| 382 | Power of the Sepulchre | Divine 0 | H4 | 0 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Sceleria national item boundary

No nation restriction or rebate link appears in the pinned item rows. This does not establish live forge pricing or exclude undocumented behaviour.


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Sceleria hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 868 | Scythe Wielder | S2 D3 H2 | assignment only; timing unresolved |
| 977 | Grand Thaumaturg | S2 D4 H2 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Sceleria army identities

- Sacred roster: Lictor, Shadow Vestal.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: Roman infantry, communions, and deliberate undead production.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Sceleria opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Sceleria fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Sceleria, the most likely planning failure is communion safety, upkeep, and mage-turn pressure. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Sceleria research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Sceleria magic-access ladder

The fixed-path ceiling is Astral 2, Death 2, Holy 3. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Sceleria battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Sceleria Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Sceleria matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Sceleria monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Sceleria unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Sceleria source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XXXVII: Middle Age Na'Ba, Queens of the Desert

## Na'Ba one-page command brief

Middle Age Na'Ba converts desert recruitment, human armies, and Jinn-backed magic into expansion, research, and strategic pressure. The pinned roster resolves 9 commander identities and 8 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 14 active nation-restricted spell records. Its chief planning risks are terrain access, rare paths, and elite replacement.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Na'Ba evidence and ruleset

This dossier covers unmodded Middle Age Na'Ba on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 65, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Na'Ba object without a named official record. No runtime test, replay, save, or new test asset was used.

## Na'Ba conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Na'Ba recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 7 | 7 | Direct pinned membership rows |
| Regional or coastal | 4 | 2 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 1 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Na'Ba commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3347 | Nabaean Scout | none | 0 |
| 3334 | Sheikh | none | 75 |
| 3358 | Karib | E1 H1 | 10 |
| 3337 | 'Adite General | none | 100 |
| 3357 | Mukarrib | S1 H2 | 50 |
| 3343 | Jann Emir | F1 A1 G1 H1; random: 100% ×1 mask 17792 link 1 | 150 |
| 3340 | Sahir | F2 A2 E1 G1; random: 100% ×1 mask 3200 link 1 | 50 |
| 3339 | Hermit Sahir | F1 A1 G1; random: 100% ×1 mask 17792 link 1 | 0 |
| 3341 | Malikah | F3 A2 G2 H1; random: 100% ×1 mask 28032 link 1; 10% ×1 mask 28032 link 1 | 100 |


## Na'Ba troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 3332 | Nabaean Desert Warrior | 10 | 0 | 10 | stealthy |
| 3333 | Nabaean Camel Rider | 12 | 0 | 12 | stealthy |
| 3356 | Nabaean Light Infantry | 10 | 0 | 10 | ordinary body |
| 3338 | Nabaean Soldier | 10 | 0 | 10 | ordinary body |
| 3355 | 'Adite Light Infantry | 24 | 1 | 12 | ordinary body |
| 3336 | 'Adite Archer | 24 | 1 | 10 | ordinary body |
| 3335 | 'Adite Elite Soldier | 25 | 1 | 13 | ordinary body |
| 3342 | Jann Guard | 22 | 1 | 13 | sacred, stealthy |


## Na'Ba mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3358 | Karib | E1 H1 | 10 |
| 3357 | Mukarrib | S1 H2 | 50 |
| 3343 | Jann Emir | F1 A1 G1 H1; random: 100% ×1 mask 17792 link 1 | 150 |
| 3340 | Sahir | F2 A2 E1 G1; random: 100% ×1 mask 3200 link 1 | 50 |
| 3339 | Hermit Sahir | F1 A1 G1; random: 100% ×1 mask 17792 link 1 | 0 |
| 3341 | Malikah | F3 A2 G2 H1; random: 100% ×1 mask 28032 link 1; 10% ×1 mask 28032 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Fire 3, Air 2, Earth 1, Astral 1, Glamour 2, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Na'Ba capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 209 | Jannah | F1, A1, E1 | Malikah, Jann Guard |
| 210 | Great Dam | W1 | none in explicit recruit fields |
| 211 | The Vault of Incense and Marvels | G1 | none in explicit recruit fields |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Na'Ba national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 539 | Contact Jinn | Conjuration 4 | F2 A1 | 18 |
| 540 | Summon Jinn Warriors | Conjuration 5 | F2 A1 | 13 |
| 541 | Contact Houri | Conjuration 6 | A2 G1 | 26 |
| 542 | Summon Hinn | Conjuration 6 | A1 F1 | 4 |
| 543 | Summon Ifrit | Blood 5 | B1 F3 | 58 |
| 544 | Summon Shaytan | Blood 6 | B1 F3 | 73 |
| 545 | Summon Marid | Conjuration 8 | F4 A2 | 66 |
| 547 | Scorching Wind | Evocation 4 | A2 F1 | 0 |
| 548 | Smokeless Flame | Evocation 6 | F3 A1 | 0 |
| 550 | Awaken Jinn Block | Thaumaturgy 5 | E1 H1 | 5 |
| 551 | Feast for Ghuls | Blood 4 | B1 | 16 |
| 552 | Summon Ghulah | Blood 5 | B1 | 31 |
| 553 | Summon Binn | Conjuration 6 | W1 A1 | 4 |
| 554 | Summon Si'lat | Conjuration 6 | A2 | 21 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Na'Ba national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 356 | Flying Carpet | 5 | A3 | rebate |
| 409 | Stone Idol | 7 | E2 S2 | rebate |
| 419 | Mirage Crystal | 7 | G3 E2 | rebate |
| 433 | The Magic Lamp | 9 | A5 F4 | rebate |
| 478 | Companion Bracelet | 5 | A2 | restricted |
| 480 | Jinn Bottle | 7 | A1 E1 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Na'Ba hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3385 | Queen of Na'Ba | F4 A3 G3 H1 | assignment only; timing unresolved |
| 3474 | Banu Si'lat | F1 A1 G1; random: 100% ×1 mask 17792 link 1 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Na'Ba army identities

- Sacred roster: Jann Guard.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: desert recruitment, human armies, and Jinn-backed magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Na'Ba opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Na'Ba fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Na'Ba, the most likely planning failure is terrain access, rare paths, and elite replacement. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Na'Ba research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Na'Ba magic-access ladder

The fixed-path ceiling is Fire 3, Air 2, Earth 1, Astral 1, Glamour 2, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Na'Ba battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Na'Ba Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Na'Ba matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Na'Ba monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Na'Ba unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Na'Ba source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XXXVIII: Middle Age Ind, Magnificent Kingdom of Exalted Virtue

## Ind one-page command brief

Middle Age Ind converts capital authority and geographically divided tributary recruitment into expansion, research, and strategic pressure. The pinned roster resolves 10 commander identities and 4 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 8 active nation-restricted spell records. Its chief planning risks are regional availability, slow concentration, and sacred replacement.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Ind evidence and ruleset

This dossier covers unmodded Middle Age Ind on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 67, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Ind object without a named official record. No runtime test, replay, save, or new test asset was used.

## Ind conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Ind recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 1 | 0 | Direct pinned membership rows |
| Regional or coastal | 4 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 5 | 4 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Ind commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3284 | Abbot Sage | S1 H2 | 50 |
| 3313 | Cannibal Warlord | none | 50 |
| 3297 | Cannibal Shaman Chief | B1; random: 100% ×1 mask 47104 link 1 | 50 |
| 3290 | Bishop Vicomte | H2 | 100 |
| 3291 | Viceroy Primate | H3 | 40 |
| 3289 | Primate King | S1 H3; random: 100% ×1 mask 9856 link 1 | 150 |
| 3286 | Abbot Magus Supreme | F1 E1 S3 H2; random: 100% ×1 mask 9856 link 1; 10% ×1 mask 11904 link 1 | 50 |
| 3285 | Abbot Magus | F1 E1 S2 H2 | 50 |
| 3288 | Archbishop Marshal | H2 | 150 |
| 3287 | Bishop General | H2 | 100 |


## Ind troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 3281 | Baculite | 12 | 0 | 13 | sacred |
| 3280 | Mirror Guard | 12 | 0 | 13 | sacred |
| 3282 | Soldier Priest | 10 | 0 | 12 | sacred |
| 3283 | Archer Priest | 10 | 0 | 11 | sacred |


## Ind mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3284 | Abbot Sage | S1 H2 | 50 |
| 3297 | Cannibal Shaman Chief | B1; random: 100% ×1 mask 47104 link 1 | 50 |
| 3290 | Bishop Vicomte | H2 | 100 |
| 3291 | Viceroy Primate | H3 | 40 |
| 3289 | Primate King | S1 H3; random: 100% ×1 mask 9856 link 1 | 150 |
| 3286 | Abbot Magus Supreme | F1 E1 S3 H2; random: 100% ×1 mask 9856 link 1; 10% ×1 mask 11904 link 1 | 50 |
| 3285 | Abbot Magus | F1 E1 S2 H2 | 50 |
| 3288 | Archbishop Marshal | H2 | 150 |
| 3287 | Bishop General | H2 | 100 |


The highest fixed recruitable paths resolved in these rows are Fire 1, Earth 1, Astral 3, Blood 1, Holy 3. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Ind capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 205 | Sublime Palace | F1, S1 | Primate King, Baculite |
| 206 | The Great Mirror | S1 | Abbot Magus Supreme, Abbot Magus, Mirror Guard |
| 207 | The Onyx Court | E1 | Archbishop Marshal, Bishop General, Soldier Priest, Archer Priest |
| 208 | Fountain of Youth | W1 | none in explicit recruit fields |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Ind national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 352 | Call Malakh | Conjuration 4 | S2 | 9 |
| 353 | Call Hashmal | Conjuration 6 | S3 F1 | 21 |
| 354 | Call Arel | Conjuration 7 | S4 N1 | 39 |
| 355 | Call Ophan | Conjuration 8 | S5 F2 | 49 |
| 356 | Call Merkavah | Conjuration 9 | S7 F3 | 222 |
| 357 | Release Lord of Civilization | Blood 9 | B8 | 177 |
| 536 | Call Cyclops Tribe | Conjuration 3 | E2 | 9 |
| 537 | Call the Birds of Splendor | Conjuration 6 | F2 N1 | 7 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Ind national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 181 | Immaculate Shield | 9 | F3 S2 | rebate |
| 282 | Salamander Silk Garments | 5 | F1 | restricted |
| 428 | The Ark | 9 | F5 S5 | rebate |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Ind hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3378 | Arch Pope | F1 W1 E1 S3 N1 H4 | assignment only; timing unresolved |
| 3380 | Protopope | H4 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Ind army identities

- Sacred roster: Baculite, Mirror Guard, Soldier Priest, Archer Priest.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: capital authority and geographically divided tributary recruitment.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Ind opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Ind fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Ind, the most likely planning failure is regional availability, slow concentration, and sacred replacement. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Ind research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Ind magic-access ladder

The fixed-path ceiling is Fire 1, Earth 1, Astral 3, Blood 1, Holy 3. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Ind battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Ind Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Ind matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Ind monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Ind unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Ind source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XXXIX: Middle Age Bandar Log, Land of the Apes

## Bandar Log one-page command brief

Middle Age Bandar Log converts mass ape infantry, sacred White Ones, and Astral–Nature mages into expansion, research, and strategic pressure. The pinned roster resolves 9 commander identities and 17 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 31 active nation-restricted spell records. Its chief planning risks are morale, armour, rare path rolls, and expensive sacreds.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Bandar Log evidence and ruleset

This dossier covers unmodded Middle Age Bandar Log on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 68, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Bandar Log object without a named official record. No runtime test, replay, save, or new test asset was used.

## Bandar Log conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Bandar Log recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 8 | 16 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 1 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Bandar Log commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 1119 | Markata Scout | none | 0 |
| 1127 | Atavi Chieftain | none | 50 |
| 1128 | Vanara Captain | none | 75 |
| 1135 | Bandar Commander | none | 100 |
| 1136 | Bandar Noble | none | 150 |
| 1146 | Brahmin | H1 | 10 |
| 1145 | Yogi | S1 | 10 |
| 1143 | Guru | S2 N1 | 10 |
| 1144 | Rishi | S3 N2; random: 100% ×1 mask 11776 link 1; 10% ×1 mask 11776 link 1 | 10 |


## Bandar Log troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 1118 | Markata | 5 | 0 | 7 | ordinary body |
| 1120 | Markata Archer | 5 | 0 | 7 | ordinary body |
| 1121 | Atavi Archer | 10 | 1 | 8 | stealthy |
| 1122 | Atavi Infantry | 10 | 1 | 8 | stealthy |
| 1123 | Vanara Archer | 10 | 1 | 9 | ordinary body |
| 1124 | Vanara Chakram Thrower | 10 | 1 | 9 | ordinary body |
| 1125 | Vanara Infantry | 10 | 1 | 9 | ordinary body |
| 1126 | Vanara Swordsman | 11 | 1 | 10 | ordinary body |
| 1130 | Light Bandar Archer | 18 | 3 | 12 | ordinary body |
| 1131 | Bandar Archer | 18 | 3 | 12 | ordinary body |
| 1351 | Light Bandar Warrior | 18 | 3 | 12 | ordinary body |
| 1132 | Bandar Warrior | 18 | 3 | 12 | ordinary body |
| 1133 | Bandar Warrior | 18 | 3 | 12 | ordinary body |
| 1134 | Royal Swordsman | 20 | 3 | 13 | ordinary body |
| 1142 | White One | 11 | 1 | 12 | sacred |
| 1147 | Elephant Rider | 10 | 1 | 8 | ordinary body |
| 1141 | Tiger Rider | 12 | 1 | 14 | sacred |


## Bandar Log mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 1146 | Brahmin | H1 | 10 |
| 1145 | Yogi | S1 | 10 |
| 1143 | Guru | S2 N1 | 10 |
| 1144 | Rishi | S3 N2; random: 100% ×1 mask 11776 link 1; 10% ×1 mask 11776 link 1 | 10 |


The highest fixed recruitable paths resolved in these rows are Astral 3, Nature 2, Holy 1. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Bandar Log capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 78 | The Lotus Gardens | S3, N2 | Rishi, Tiger Rider |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Bandar Log national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 555 | Summon Angiri | Conjuration 3 | F2 | 5 |
| 556 | Summon Nagas | Conjuration 3 | W2 E1 | 15 |
| 557 | Summon Apsaras | Conjuration 3 | S2 | 3 |
| 558 | Summon Vidyadhara | Conjuration 4 | S2 | 15 |
| 559 | Contact Yaksha | Conjuration 4 | N2 E1 | 25 |
| 560 | Contact Yakshini | Conjuration 4 | N2 W1 | 25 |
| 561 | Contact Nagini | Conjuration 4 | W2 E1 | 25 |
| 562 | Summon Gandharvas | Conjuration 5 | S2 | 15 |
| 563 | Summon Kimpurushas | Conjuration 5 | N2 S1 | 15 |
| 564 | Contact Nagaraja | Conjuration 5 | W2 E1 | 30 |
| 565 | Summon Garudas | Conjuration 6 | S2 | 21 |
| 566 | Summon Maruts | Conjuration 6 | S2 | 18 |
| 567 | Summon Kinnara | Conjuration 6 | S3 | 25 |
| 568 | Contact Nagarishi | Conjuration 6 | W3 E1 | 40 |
| 569 | Summon Siddha | Conjuration 7 | S4 | 35 |
| 570 | Summon Devata | Conjuration 8 | S5 | 45 |
| 571 | Summon Devala | Conjuration 9 | S5 | 55 |
| 572 | Summon Rudra | Conjuration 9 | S5 | 55 |
| 573 | Celestial Music | Thaumaturgy 6 | S3 | 1 |
| 574 | Summon Rakshasas | Blood 1 | B1 | 8 |
| 575 | Feast of Flesh | Blood 2 | B1 N1 | 50 |
| 576 | Summon Asrapas | Blood 3 | B2 | 8 |
| 577 | Summon Rakshasa Warriors | Blood 4 | B2 | 21 |
| 578 | Summon Sandhyabalas | Blood 5 | B2 D1 | 25 |
| 579 | Summon Dakini | Blood 6 | B4 A1 | 81 |
| 580 | Summon Samanishada | Blood 7 | B3 D1 | 35 |
| 581 | Summon Mandeha | Blood 8 | B5 D2 | 133 |
| 582 | Summon Danavas | Blood 8 | B5 | 70 |
| 583 | Summon Daitya | Blood 8 | B5 | 45 |
| 584 | Host of Ganas | Conjuration 2 | D1 | 9 |
| 585 | Summon Vetalas | Conjuration 5 | D2 | 10 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Bandar Log national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 140 | Vajra | 5 | S2 | restricted |
| 227 | Headdress of the Bull | 5 | N1 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Bandar Log hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 2270 | Tathagata | H2 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Bandar Log army identities

- Sacred roster: White One, Tiger Rider.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: mass ape infantry, sacred White Ones, and Astral–Nature mages.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Bandar Log opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Bandar Log fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Bandar Log, the most likely planning failure is morale, armour, rare path rolls, and expensive sacreds. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Bandar Log research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Bandar Log magic-access ladder

The fixed-path ceiling is Astral 3, Nature 2, Holy 1. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Bandar Log battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Bandar Log Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Bandar Log matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Bandar Log monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Bandar Log unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Bandar Log source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XL: Middle Age Nazca, Kingdom of the Sun

## Nazca one-page command brief

Middle Age Nazca converts flying armies, sacred Sun Guards, and reanimation into expansion, research, and strategic pressure. The pinned roster resolves 12 commander identities and 11 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 5 active nation-restricted spell records. Its chief planning risks are fragile bodies, corpse supply, leadership, and capital pressure.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Nazca evidence and ruleset

This dossier covers unmodded Middle Age Nazca on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 72, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Nazca object without a named official record. No runtime test, replay, save, or new test asset was used.

## Nazca conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Nazca recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 9 | 9 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 3 | 2 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Nazca commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2666 | Runancha | none | 0 |
| 2647 | Kuraka | none | 75 |
| 2654 | Apu | none | 75 |
| 2655 | Apusqispay | none | 100 |
| 2656 | Aclla | F1 A1 H1 | 10 |
| 2657 | Hurin Priest | E1 D2 H2; random: 100% ×1 mask 3328 link 1 | 10 |
| 2660 | Mallqui | none | 20 |
| 2661 | Mallqui Priestess | F1 A1 H1 | 20 |
| 2662 | Mallqui Priest | E1 D2 H2; random: 100% ×1 mask 3328 link 1 | 20 |
| 2658 | Inca | F2 A2 H3; random: 10% ×1 mask 2432 link 1 | 100 |
| 2659 | Coya | E2 S2 D2 H2; random: 30% ×1 mask 7552 link 1 | 50 |
| 2663 | Royal Mallqui | F2 A2 E2 S2 D2 H3; random: 10% ×1 mask 7552 link 1 | 20 |


## Nazca troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 2643 | Human Warrior | 10 | 0 | 10 | ordinary body |
| 2644 | Human Warrior | 10 | 0 | 10 | ordinary body |
| 2645 | Human Warrior | 10 | 0 | 10 | ordinary body |
| 2646 | Human Warrior | 10 | 0 | 10 | ordinary body |
| 2648 | Hatun Runa | 11 | 0 | 7 | flying |
| 2652 | Aucac Runa Archer | 11 | 0 | 10 | flying |
| 2649 | Aucac Runa Spearman | 11 | 0 | 11 | flying |
| 2650 | Aucac Runa Maceman | 11 | 0 | 11 | flying |
| 2651 | Aucac Runa Axeman | 11 | 0 | 11 | flying |
| 2653 | Sun Guard | 13 | 0 | 13 | sacred, flying |
| 2667 | Condor Warrior | 13 | 0 | 12 | sacred, flying |


## Nazca mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2656 | Aclla | F1 A1 H1 | 10 |
| 2657 | Hurin Priest | E1 D2 H2; random: 100% ×1 mask 3328 link 1 | 10 |
| 2661 | Mallqui Priestess | F1 A1 H1 | 20 |
| 2662 | Mallqui Priest | E1 D2 H2; random: 100% ×1 mask 3328 link 1 | 20 |
| 2658 | Inca | F2 A2 H3; random: 10% ×1 mask 2432 link 1 | 100 |
| 2659 | Coya | E2 S2 D2 H2; random: 30% ×1 mask 7552 link 1 | 50 |
| 2663 | Royal Mallqui | F2 A2 E2 S2 D2 H3; random: 10% ×1 mask 7552 link 1 | 20 |


The highest fixed recruitable paths resolved in these rows are Fire 2, Air 2, Earth 2, Astral 2, Death 2, Holy 3. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Nazca capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 172 | Palace of the Sun Kings | F1, A1, S1 | Inca, Coya, Sun Guard |
| 173 | Tombs of the Sun Kings | E1, D1 | Royal Mallqui, Condor Warrior |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Nazca national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 472 | Geoglyphs | Enchantment 5 | S3 E2 | 18 |
| 473 | Eyes of the Condors | Enchantment 2 | A2 | 1 |
| 474 | Summon Condors | Conjuration 3 | A2 | 8 |
| 475 | Summon Huacas | Conjuration 5 | S2 | 12 |
| 476 | Summon Supayas | Conjuration 5 | D2 | 8 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Nazca national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 228 | Huaca Headdress | 5 | F2 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Nazca hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 2712 | Apostate Seraph | F1 A3 W2 S2 | assignment only; timing unresolved |
| 2713 | First Couple | F2 A2 E2 S2 D4 H3 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Nazca army identities

- Sacred roster: Sun Guard, Condor Warrior.
- Flying roster: Hatun Runa, Aucac Runa Archer, Aucac Runa Spearman, Aucac Runa Maceman, Aucac Runa Axeman, Sun Guard, Condor Warrior.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: flying armies, sacred Sun Guards, and reanimation.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Nazca opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Nazca fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Nazca, the most likely planning failure is fragile bodies, corpse supply, leadership, and capital pressure. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Nazca research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Nazca magic-access ladder

The fixed-path ceiling is Fire 2, Air 2, Earth 2, Astral 2, Death 2, Holy 3. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Nazca battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Nazca Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Nazca matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Nazca monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Nazca unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Nazca source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLI: Middle Age Mictlan, Reign of the Lawgiver

## Mictlan one-page command brief

Middle Age Mictlan converts broad elemental priests, sacred warriors, and Blood access into expansion, research, and strategic pressure. The pinned roster resolves 11 commander identities and 9 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 13 active nation-restricted spell records. Its chief planning risks are blood-hunting opportunity cost, priest turns, and lightly protected troops.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Mictlan evidence and ruleset

This dossier covers unmodded Middle Age Mictlan on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 73, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Mictlan object without a named official record. No runtime test, replay, save, or new test asset was used.

## Mictlan conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Mictlan recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 5 | 7 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 6 | 2 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Mictlan commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 729 | Scout | none | 0 |
| 730 | Tribal King | none | 100 |
| 1189 | Mictlan Priest | H1; random: 100% ×1 mask 10880 link 1 | 10 |
| 1361 | Nahualli | S1 N2; random: 10% ×1 mask 47104 link 1 | 10 |
| 1888 | Sky Priest | A1 H1; random: 10% ×1 mask 10880 link 1 | 10 |
| 1192 | Moon Priest | S2 H2 | 10 |
| 1193 | Sun Priest | F2 H2 | 50 |
| 1191 | Rain Priest | W2 H2 | 10 |
| 1907 | High Priest of the Sky | A2 H3; random: 100% ×1 mask 10880 link 1; 10% ×1 mask 11136 link 1 | 50 |
| 1190 | Priest King | N2 H3; random: 10% ×1 mask 11136 link 1 | 150 |
| 1194 | Couatl | S3 N1 H2; random: 100% ×2 mask 8448 link 1; 10% ×1 mask 10496 link 1 | 100 |


## Mictlan troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 721 | Warrior | 10 | 0 | 10 | ordinary body |
| 1545 | Warrior | 10 | 0 | 10 | ordinary body |
| 1546 | Warrior | 10 | 0 | 10 | ordinary body |
| 1547 | Warrior | 10 | 0 | 10 | ordinary body |
| 1548 | Feathered Warrior | 10 | 0 | 11 | ordinary body |
| 1883 | Moon Warrior | 12 | 0 | 12 | ordinary body |
| 726 | Eagle Warrior | 12 | 0 | 11 | sacred |
| 725 | Sun Warrior | 12 | 0 | 13 | sacred |
| 727 | Jaguar Warrior | 12 | 0 | 12 | sacred |


## Mictlan mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 1189 | Mictlan Priest | H1; random: 100% ×1 mask 10880 link 1 | 10 |
| 1361 | Nahualli | S1 N2; random: 10% ×1 mask 47104 link 1 | 10 |
| 1888 | Sky Priest | A1 H1; random: 10% ×1 mask 10880 link 1 | 10 |
| 1192 | Moon Priest | S2 H2 | 10 |
| 1193 | Sun Priest | F2 H2 | 50 |
| 1191 | Rain Priest | W2 H2 | 10 |
| 1907 | High Priest of the Sky | A2 H3; random: 100% ×1 mask 10880 link 1; 10% ×1 mask 11136 link 1 | 50 |
| 1190 | Priest King | N2 H3; random: 10% ×1 mask 11136 link 1 | 150 |
| 1194 | Couatl | S3 N1 H2; random: 100% ×2 mask 8448 link 1; 10% ×1 mask 10496 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Fire 2, Air 2, Water 2, Astral 3, Nature 2, Holy 3. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Mictlan capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 89 | Temple of the Moon | S1 | Moon Priest |
| 90 | Temple of the Sun | F1 | Sun Priest, Sun Warrior |
| 88 | High Temple of the Sky and the Rain | A1, W1 | Rain Priest, High Priest of the Sky |
| 87 | High Temple of the Land | N1 | Priest King, Couatl, Jaguar Warrior |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Mictlan national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 504 | Summon Jaguar Toads | Conjuration 1 | N1 H1 | 2 |
| 505 | Summon Jaguars | Conjuration 3 | N2 H1 | 20 |
| 506 | Summon Jade Serpents | Conjuration 4 | W2 | 3 |
| 507 | Summon Monster Toad | Conjuration 5 | N2 | 1 |
| 508 | Contact Couatl | Conjuration 6 | N1 S1 | 40 |
| 509 | Summon Tlaloque | Conjuration 7 | W4 | 60 |
| 510 | Bind Beast Bats | Blood 2 | B1 | 8 |
| 511 | Bind Jaguar Fiends | Blood 4 | B1 F1 | 16 |
| 512 | Contact Civateteo | Blood 5 | B2 D2 | 36 |
| 513 | Bind Tzitzimitl | Blood 6 | B2 S2 | 10 |
| 514 | Contact Tlahuelpuchi | Blood 6 | B3 | 42 |
| 515 | Contact Onaqui | Blood 7 | B4 | 101 |
| 516 | Rain of Jaguars | Blood 8 | B6 F2 | 40 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Mictlan national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 43 | Jade Knife | 3 | N1 B1 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Mictlan hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 933 | King of Legends | D3 B3 H3 | assignment only; timing unresolved |
| 1884 | Priest King | F2 A2 S3 N2 H4 | assignment only; timing unresolved |
| 1886 | Priest King | A3 S3 N2 H3 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Mictlan army identities

- Sacred roster: Eagle Warrior, Sun Warrior, Jaguar Warrior.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: broad elemental priests, sacred warriors, and Blood access.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Mictlan opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Mictlan fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Mictlan, the most likely planning failure is blood-hunting opportunity cost, priest turns, and lightly protected troops. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Mictlan research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Mictlan magic-access ladder

The fixed-path ceiling is Fire 2, Air 2, Water 2, Astral 3, Nature 2, Holy 3. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Mictlan battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Mictlan Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Mictlan matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Mictlan monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Mictlan unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Mictlan source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLII: Middle Age Xibalba, Flooded Caves

## Xibalba one-page command brief

Middle Age Xibalba converts cave recruitment, flying Zotz, amphibious forces, and Blood magic into expansion, research, and strategic pressure. The pinned roster resolves 7 commander identities and 9 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 13 active nation-restricted spell records. Its chief planning risks are terrain splits, weak bodies, underwater logistics, and random paths.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Xibalba evidence and ruleset

This dossier covers unmodded Middle Age Xibalba on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 74, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Xibalba object without a named official record. No runtime test, replay, save, or new test asset was used.

## Xibalba conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Xibalba recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 4 | 6 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 3 | 3 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Xibalba commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2715 | Muuch Ajaw | H1 | 100 |
| 2718 | Ah Itz | W1 D1 | 10 |
| 2717 | Ah Ha' | W1 E1 H1 | 10 |
| 2716 | Muuch K'uhul | W2 E1 D1 H1; random: 100% ×1 mask 13824 link 1 | 50 |
| 2732 | Chak Muuch Assassin | none | 0 |
| 2714 | Bacab | W3 E2 D1 H2; random: 100% ×1 mask 13824 link 1; 10% ×1 mask 13824 link 1 | 150 |
| 2719 | Camazotz | D2 B1; random: 100% ×1 mask 34048 link 1 | 10 |


## Xibalba troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 2721 | Muuch Militia | 12 | 2 | 8 | amphibious |
| 2722 | Muuch Dart Thrower | 14 | 2 | 10 | amphibious |
| 2723 | Muuch Warrior | 14 | 2 | 10 | amphibious |
| 2724 | Muuch Warrior | 14 | 2 | 10 | amphibious |
| 2725 | Muuch Warrior | 14 | 2 | 10 | amphibious |
| 2726 | Muuch Warrior | 14 | 2 | 10 | amphibious |
| 2730 | Chak Muuch Dart Thrower | 14 | 2 | 11 | sacred, amphibious |
| 2731 | Chak Muuch Obsidian Warrior | 15 | 2 | 13 | sacred, amphibious |
| 2729 | Wo' Muuch | 26 | 6 | 14 | sacred, amphibious |


## Xibalba mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2715 | Muuch Ajaw | H1 | 100 |
| 2718 | Ah Itz | W1 D1 | 10 |
| 2717 | Ah Ha' | W1 E1 H1 | 10 |
| 2716 | Muuch K'uhul | W2 E1 D1 H1; random: 100% ×1 mask 13824 link 1 | 50 |
| 2714 | Bacab | W3 E2 D1 H2; random: 100% ×1 mask 13824 link 1; 10% ×1 mask 13824 link 1 | 150 |
| 2719 | Camazotz | D2 B1; random: 100% ×1 mask 34048 link 1 | 10 |


The highest fixed recruitable paths resolved in these rows are Water 3, Earth 2, Death 2, Blood 1, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Xibalba capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 177 | The Sacred Cenote | W1 | Chak Muuch Assassin, Chak Muuch Dart Thrower, Chak Muuch Obsidian Warrior |
| 178 | The Flooded City | W2, E1 | Bacab, Wo' Muuch |
| 179 | The Cave of Perpetual Darkness | D1 | Camazotz |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Xibalba national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 504 | Summon Jaguar Toads | Conjuration 1 | N1 H1 | 2 |
| 506 | Summon Jade Serpents | Conjuration 4 | W2 | 3 |
| 507 | Summon Monster Toad | Conjuration 5 | N2 | 1 |
| 519 | Break the First Soul | Blood 2 | B1 | 0 |
| 520 | Break the Second Soul | Thaumaturgy 2 | E1 | 0 |
| 521 | Break the Third Soul | Thaumaturgy 2 | A1 | 0 |
| 522 | Break the Fourth Soul | Thaumaturgy 2 | D1 | 0 |
| 523 | Gift of the First Soul | Blood 3 | B1 | 0 |
| 524 | Gift of the Second Soul | Thaumaturgy 3 | E1 | 0 |
| 525 | Gift of the Third Soul | Thaumaturgy 3 | A1 | 0 |
| 526 | Gift of the Fourth Soul | Thaumaturgy 3 | D1 | 0 |
| 527 | Summon Balam | Conjuration 7 | N4 | 60 |
| 528 | Summon Chaac | Conjuration 8 | A4 | 75 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Xibalba national item boundary

No nation restriction or rebate link appears in the pinned item rows. This does not establish live forge pricing or exclude undocumented behaviour.


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Xibalba hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3260 | Grandmother Earth | W2 E2 D2 H4 | assignment only; timing unresolved |
| 3261 | Red Face | W2 E2 D1 H2 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Xibalba army identities

- Sacred roster: Chak Muuch Dart Thrower, Chak Muuch Obsidian Warrior, Wo' Muuch.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: Muuch Militia, Muuch Dart Thrower, Muuch Warrior, Muuch Warrior, Muuch Warrior, Muuch Warrior, Chak Muuch Dart Thrower, Chak Muuch Obsidian Warrior, Wo' Muuch.
- Core identity: cave recruitment, flying Zotz, amphibious forces, and Blood magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Xibalba opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Xibalba fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Xibalba, the most likely planning failure is terrain splits, weak bodies, underwater logistics, and random paths. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Xibalba research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Xibalba magic-access ladder

The fixed-path ceiling is Water 3, Earth 2, Death 2, Blood 1, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Xibalba battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Xibalba Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Xibalba matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Xibalba monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Xibalba unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Xibalba source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLIII: Middle Age Phaeacia, Isle of the Dark Ships

## Phaeacia one-page command brief

Middle Age Phaeacia converts sailing, Colossi, and a broad island mage corps into expansion, research, and strategic pressure. The pinned roster resolves 8 commander identities and 8 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 9 active nation-restricted spell records. Its chief planning risks are gold-intensive elites, sailing boundaries, and coastal replacement.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Phaeacia evidence and ruleset

This dossier covers unmodded Middle Age Phaeacia on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 77, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Phaeacia object without a named official record. No runtime test, replay, save, or new test asset was used.

## Phaeacia conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Phaeacia recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 6 | 7 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 2 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Phaeacia commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3153 | Phaeacian Scout | none | 0 |
| 3154 | Phaeacian Captain | none | 75 |
| 3166 | Phaeacian Priest | H1 | 10 |
| 3151 | Mage Pilot | A1 W1 | 50 |
| 3155 | Colossi Weaver | A1 S1; random: 100% ×1 mask 20224 link 1 | 10 |
| 3156 | Colossi Storm Captain | A2 W1 | 100 |
| 3158 | Prince Consort | A3 W2 H1; random: 100% ×1 mask 18176 link 1; 10% ×1 mask 18176 link 1 | 10 |
| 3157 | Colossi Queen | A2 W2 S1 G1 H2; random: 100% ×1 mask 19200 link 1; 10% ×1 mask 19200 link 1 | 100 |


## Phaeacia troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 3143 | Phaeacian Militia | 10 | 0 | 8 | ordinary body |
| 3144 | Phaeacian Archer | 10 | 0 | 8 | ordinary body |
| 3145 | Phaeacian Light Infantry | 10 | 0 | 10 | ordinary body |
| 3146 | Phaeacian Infantry | 10 | 0 | 10 | ordinary body |
| 3147 | Phaeacian Heavy Infantry | 10 | 0 | 11 | ordinary body |
| 3165 | Colossi Light Infantry | 20 | 1 | 12 | ordinary body |
| 3148 | Colossi Heavy Infantry | 20 | 1 | 12 | ordinary body |
| 3159 | Orichalcum Guard | 24 | 1 | 14 | sacred |


## Phaeacia mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3166 | Phaeacian Priest | H1 | 10 |
| 3151 | Mage Pilot | A1 W1 | 50 |
| 3155 | Colossi Weaver | A1 S1; random: 100% ×1 mask 20224 link 1 | 10 |
| 3156 | Colossi Storm Captain | A2 W1 | 100 |
| 3158 | Prince Consort | A3 W2 H1; random: 100% ×1 mask 18176 link 1; 10% ×1 mask 18176 link 1 | 10 |
| 3157 | Colossi Queen | A2 W2 S1 G1 H2; random: 100% ×1 mask 19200 link 1; 10% ×1 mask 19200 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Air 3, Water 2, Astral 1, Glamour 1, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Phaeacia capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 198 | The Orichalcum Palace | A1, G1 | Prince Consort, Colossi Queen, Orichalcum Guard |
| 199 | Black Korkyra | W1, E1 | none in explicit recruit fields |
| 200 | Gold Apple Tree | F1 | none in explicit recruit fields |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Phaeacia national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 254 | Summon Hound of Twilight | Conjuration 5 | E2 D1 | 3 |
| 255 | Sow Dragon Teeth | Enchantment 6 | E2 | 1 |
| 256 | Bind Keres | Conjuration 6 | D2 | 12 |
| 265 | Contact Hesperide | Conjuration 6 | F3 S1 | 35 |
| 266 | Call Ladon | Conjuration 6 | F3 N2 | 15 |
| 267 | Dogs of Gold and Silver | Construction 4 | E1 | 7 |
| 268 | Dog of Gold | school -1 1 | special | 0 |
| 269 | Craft Keledone | Construction 6 | E2 S2 | 5 |
| 270 | Forge Brass Bull | Construction 6 | F3 E3 | 25 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Phaeacia national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 281 | Purple Silk Garments | 3 | S1 W1 | restricted |
| 283 | Silver Silk Garments | 7 | S1 A1 | restricted |
| 477 | Windcatcher Sail | 5 | A2 | restricted |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Phaeacia hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3173 | Aegaeide | W3 N3 | assignment only; timing unresolved |
| 3174 | Phaeacian Princess | A2 W1 S1 G1 H1 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Phaeacia army identities

- Sacred roster: Orichalcum Guard.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: sailing, Colossi, and a broad island mage corps.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Phaeacia opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Phaeacia fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Phaeacia, the most likely planning failure is gold-intensive elites, sailing boundaries, and coastal replacement. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Phaeacia research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Phaeacia magic-access ladder

The fixed-path ceiling is Air 3, Water 2, Astral 1, Glamour 1, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Phaeacia battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Phaeacia Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Phaeacia matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Phaeacia monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Phaeacia unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Phaeacia source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLIV: Middle Age Vanarus, Land of the Chuds

## Vanarus one-page command brief

Middle Age Vanarus converts human infantry, Chud elites, stealth, and forest-linked magic into expansion, research, and strategic pressure. The pinned roster resolves 7 commander identities and 10 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 16 active nation-restricted spell records. Its chief planning risks are mixed troop quality, limited armour, and dispersed specialist roles.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Vanarus evidence and ruleset

This dossier covers unmodded Middle Age Vanarus on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 79, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Vanarus object without a named official record. No runtime test, replay, save, or new test asset was used.

## Vanarus conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Vanarus recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 6 | 8 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 1 | 2 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Vanarus commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2353 | Scout | none | 0 |
| 2354 | Vanarusian Herse | none | 75 |
| 2355 | Vanarusian Jarl | none | 100 |
| 2356 | Vanarusian Gode | H1 | 10 |
| 2341 | Vanarusian Sage | A1; random: 100% ×1 mask 9600 link 1; 100% ×1 mask 53248 link 1 | 10 |
| 2357 | Chud Jarl | H1 | 100 |
| 2342 | Vanabog | A2 D1 G1 B1 H2; random: 100% ×1 mask 53632 link 1; 10% ×1 mask 53632 link 1 | 150 |


## Vanarus troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 2343 | Vanarusian Archer | 10 | 0 | 8 | ordinary body |
| 2344 | Vanarusian Huskarl | 10 | 0 | 10 | ordinary body |
| 2345 | Vanarusian Huskarl | 10 | 0 | 10 | ordinary body |
| 2346 | Vanarusian Hirdman | 10 | 0 | 11 | ordinary body |
| 2347 | Vanarusian Hirdman | 10 | 0 | 11 | ordinary body |
| 2348 | Vanarusian Hirdman | 10 | 0 | 11 | ordinary body |
| 3071 | Vanarusian Berserker | 12 | 0 | 12 | ordinary body |
| 2350 | Chud Hirdman | 17 | 2 | 13 | ordinary body |
| 2349 | Oath-Bound | 14 | 0 | 13 | sacred, stealthy |
| 2352 | Chud Skinshifter | 18 | 2 | 13 | ordinary body |


## Vanarus mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2356 | Vanarusian Gode | H1 | 10 |
| 2341 | Vanarusian Sage | A1; random: 100% ×1 mask 9600 link 1; 100% ×1 mask 53248 link 1 | 10 |
| 2357 | Chud Jarl | H1 | 100 |
| 2342 | Vanabog | A2 D1 G1 B1 H2; random: 100% ×1 mask 53632 link 1; 10% ×1 mask 53632 link 1 | 150 |


The highest fixed recruitable paths resolved in these rows are Air 2, Death 1, Glamour 1, Blood 1, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Vanarus capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 155 | Novgård | F1, A1, G1 | Vanabog, Oath-Bound |
| 156 | Pine of Skulls | D1, N1 | Chud Skinshifter |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Vanarus national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 322 | Summon Simargl | Conjuration 2 | A1 | 1 |
| 323 | Summon Firebird | Conjuration 3 | F1 S1 | 2 |
| 324 | Send Lady Midday | Conjuration 5 | A3 D1 | 5 |
| 325 | Contact Sirin | Conjuration 3 | S2 | 8 |
| 326 | Send Vodyanoy | Conjuration 4 | W2 | 20 |
| 327 | Summon Rusalka | Conjuration 4 | W1 D1 | 16 |
| 328 | Summon Likho | Conjuration 4 | D1 | 10 |
| 329 | Contact Alkonost | Conjuration 4 | S2 | 15 |
| 330 | Summon Zmey | Conjuration 5 | F2 | 5 |
| 331 | Send Bukavac | Conjuration 5 | W4 | 5 |
| 332 | Contact Gamayun | Conjuration 5 | S3 | 25 |
| 333 | Contact Beregina | Conjuration 6 | W3 E1 | 35 |
| 334 | Contact Mountain Vila | Conjuration 7 | N4 | 40 |
| 335 | Contact Cloud Vila | Conjuration 7 | A4 | 40 |
| 336 | Contact Leshiy | Conjuration 8 | N6 | 60 |
| 493 | Awaken Draugar | Conjuration 4 | D2 | 12 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Vanarus national item boundary

No nation restriction or rebate link appears in the pinned item rows. This does not establish live forge pricing or exclude undocumented behaviour.


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Vanarus hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3257 | Last Perkunu | A4 S1 N3 H1 | assignment only; timing unresolved |
| 1958 | Hag | A3 W1 D3 N2 | assignment only; timing unresolved |
| 3259 | Varyag | A2 D1 G2 H1 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Vanarus army identities

- Sacred roster: Oath-Bound.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: human infantry, Chud elites, stealth, and forest-linked magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Vanarus opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Vanarus fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Vanarus, the most likely planning failure is mixed troop quality, limited armour, and dispersed specialist roles. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Vanarus research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Vanarus magic-access ladder

The fixed-path ceiling is Air 2, Death 1, Glamour 1, Blood 1, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Vanarus battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Vanarus Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Vanarus matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Vanarus monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Vanarus unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Vanarus source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLV: Middle Age Jotunheim, Iron Woods

## Jotunheim one-page command brief

Middle Age Jotunheim converts giant infantry, sacred Jotuns, and Death–Nature magic into expansion, research, and strategic pressure. The pinned roster resolves 10 commander identities and 15 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 8 active nation-restricted spell records. Its chief planning risks are high gold per body, low formation width, and replacement tempo.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Jotunheim evidence and ruleset

This dossier covers unmodded Middle Age Jotunheim on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 80, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Jotunheim object without a named official record. No runtime test, replay, save, or new test asset was used.

## Jotunheim conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Jotunheim recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 8 | 13 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 2 | 2 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Jotunheim commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 283 | Chief | none | 50 |
| 786 | Jotun Scout | none | 0 |
| 437 | Jotun Herse | none | 75 |
| 274 | Jotun Jarl | H1 | 100 |
| 275 | Jotun Gode | H2 | 50 |
| 913 | Vaetti Hag | none; random: 100% ×1 mask 63488 link 1 | 10 |
| 3429 | Jotun Skratti | W2 B2; random: 100% ×1 mask 53760 link 1 | 10 |
| 3397 | Gygja | D1 G1 B1; random: 100% ×1 mask 63488 link 1 | 50 |
| 3398 | Jarnvidja | D1 G1 B1; random: 100% ×3 mask 63488 link 1; 10% ×1 mask 63488 link 1 | 50 |
| 3399 | Thrymsgode | W1 H2; random: 100% ×1 mask 20992 link 1 | 100 |


## Jotunheim troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 3423 | Vaetti Archer | 8 | 0 | 7 | stealthy |
| 541 | Vaetti | 8 | 0 | 9 | stealthy |
| 282 | Wolf Rider | 8 | 0 | 9 | stealthy |
| 1085 | Moose Rider | 8 | 0 | 7 | stealthy |
| 277 | Jotun Bondi | 31 | 5 | 11 | ordinary body |
| 276 | Jotun Javelinist | 33 | 5 | 12 | ordinary body |
| 300 | Jotun Hurler | 33 | 5 | 12 | ordinary body |
| 278 | Jotun Spearman | 33 | 5 | 12 | ordinary body |
| 279 | Jotun Axeman | 33 | 5 | 12 | ordinary body |
| 841 | Godihuskarl | 36 | 5 | 13 | ordinary body |
| 840 | Jotun Huskarl | 35 | 5 | 13 | ordinary body |
| 842 | Jotun Hirdman | 38 | 5 | 13 | ordinary body |
| 845 | Niefel Giant | 69 | 7 | 14 | sacred |
| 1310 | Ulfhedin | 40 | 6 | 15 | ordinary body |
| 3400 | Thrymshirding | 41 | 6 | 14 | sacred |


## Jotunheim mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 274 | Jotun Jarl | H1 | 100 |
| 275 | Jotun Gode | H2 | 50 |
| 913 | Vaetti Hag | none; random: 100% ×1 mask 63488 link 1 | 10 |
| 3429 | Jotun Skratti | W2 B2; random: 100% ×1 mask 53760 link 1 | 10 |
| 3397 | Gygja | D1 G1 B1; random: 100% ×1 mask 63488 link 1 | 50 |
| 3398 | Jarnvidja | D1 G1 B1; random: 100% ×3 mask 63488 link 1; 10% ×1 mask 63488 link 1 | 50 |
| 3399 | Thrymsgode | W1 H2; random: 100% ×1 mask 20992 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Water 2, Death 1, Glamour 1, Blood 2, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Jotunheim capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 16 | Iron Woods | S1, D2, G1 | Jarnvidja, Ulfhedin |
| 212 | Thrymsheim | W1 | Thrymsgode, Thrymshirding |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Jotunheim national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 491 | Summon Dwarf of the Four Directions | Conjuration 8 | A4 E3 | 62 |
| 494 | Seith Curse | Thaumaturgy 5 | D1 S1 | 3 |
| 495 | Summon Glosos | Conjuration 3 | D2 | 13 |
| 496 | Brood of Garm | Conjuration 4 | N2 | 10 |
| 497 | Awaken Jotun Draugar | Conjuration 4 | D2 | 15 |
| 498 | Summon Rimvaettir | Conjuration 5 | W2 | 5 |
| 499 | Winter's Call | Blood 6 | B3 W2 | 86 |
| 500 | Illwinter | Blood 6 | B5 W3 | 120 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Jotunheim national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 33 | Duskdagger | 3 | D1 S1 | rebate |
| 114 | The Sword of Aurgelmer | 9 | G6 | rebate |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Jotunheim hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 1382 | Abductor | A3 W3 D3 H2 | assignment only; timing unresolved |
| 586 | Great Hag | S3 D3 N2 G3 B3 | assignment only; timing unresolved |
| 508 | Wolf Lord | none | assignment only; timing unresolved |
| 3424 | Undying | S2 D2 N3 G2 B1 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Jotunheim army identities

- Sacred roster: Niefel Giant, Thrymshirding.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: giant infantry, sacred Jotuns, and Death–Nature magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Jotunheim opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Jotunheim fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Jotunheim, the most likely planning failure is high gold per body, low formation width, and replacement tempo. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Jotunheim research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Jotunheim magic-access ladder

The fixed-path ceiling is Water 2, Death 1, Glamour 1, Blood 2, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Jotunheim battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Jotunheim Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Jotunheim matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Jotunheim monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Jotunheim unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Jotunheim source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLVI: Middle Age Nidavangr, Bear, Wolf and Crow

## Nidavangr one-page command brief

Middle Age Nidavangr converts Dwarven smiths, skinshifters, and terrain-linked recruitment into expansion, research, and strategic pressure. The pinned roster resolves 9 commander identities and 6 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 3 active nation-restricted spell records. Its chief planning risks are expensive specialists, transformation behaviour, and regional access.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Nidavangr evidence and ruleset

This dossier covers unmodded Middle Age Nidavangr on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 81, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Nidavangr object without a named official record. No runtime test, replay, save, or new test asset was used.

## Nidavangr conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Nidavangr recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 7 | 5 | Direct pinned membership rows |
| Regional or coastal | 6 | 4 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 2 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Nidavangr commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3672 | Crow Clan Scout | none | 0 |
| 3671 | Nidherse | none | 75 |
| 3670 | Nidajarl | none | 100 |
| 3830 | Seithberender Apprentice | none; random: 100% ×1 mask 15872 link 1 | 10 |
| 3682 | Bear Clan Cub-Mother | none | 50 |
| 3679 | Bear Clan Seithberender | E1 N2 H1 | 10 |
| 3680 | Wolf Clan Seithberender | W2 N1 H1 | 10 |
| 3681 | Crow Clan Seithberender | A1 S2 D2 H1; random: 100% ×2 mask 39168 link 1; 10% ×1 mask 39168 link 1 | 10 |
| 3685 | Nidhere | H1 | 50 |


## Nidavangr troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 3673 | Crow Clan Archer | 11 | 0 | 11 | stealthy |
| 3676 | Bear Clan Warrior | 14 | 0 | 13 | ordinary body |
| 3675 | Cub-Warrior | 11 | 0 | 14 | ordinary body |
| 3674 | Wolf Clan Reaver | 12 | 0 | 12 | stealthy |
| 3678 | Nidylva | 12 | 0 | 13 | ordinary body |
| 3677 | Nidbathed | 15 | 0 | 18 | sacred |


## Nidavangr mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 3830 | Seithberender Apprentice | none; random: 100% ×1 mask 15872 link 1 | 10 |
| 3679 | Bear Clan Seithberender | E1 N2 H1 | 10 |
| 3680 | Wolf Clan Seithberender | W2 N1 H1 | 10 |
| 3681 | Crow Clan Seithberender | A1 S2 D2 H1; random: 100% ×2 mask 39168 link 1; 10% ×1 mask 39168 link 1 | 10 |
| 3685 | Nidhere | H1 | 50 |


The highest fixed recruitable paths resolved in these rows are Air 1, Water 2, Earth 1, Astral 2, Death 2, Nature 2, Holy 1. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Nidavangr capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 226 | Nidakettil | A1, S1, D3 | Crow Clan Seithberender, Nidhere, Nidbathed |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Nidavangr national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 491 | Summon Dwarf of the Four Directions | Conjuration 8 | A4 E3 | 62 |
| 494 | Seith Curse | Thaumaturgy 5 | D1 S1 | 3 |
| 503 | Command Draugar | Conjuration 4 | D2 | 12 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Nidavangr national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 460 | Soulstone of the Wolves | 9 | N6 E1 | rebate |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Nidavangr hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 3881 | Seithmathr Bear | E2 N3 H1 | assignment only; timing unresolved |
| 3883 | Seithmathr Wolf | W2 D3 N2 H1 | assignment only; timing unresolved |
| 3885 | Seithmathr Crow | A2 S3 D4 H1 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Nidavangr army identities

- Sacred roster: Nidbathed.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: no aquatic or amphibious troop identified in the reconciled recruit rows.
- Core identity: Dwarven smiths, skinshifters, and terrain-linked recruitment.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Nidavangr opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Nidavangr fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Nidavangr, the most likely planning failure is expensive specialists, transformation behaviour, and regional access. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Nidavangr research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Nidavangr magic-access ladder

The fixed-path ceiling is Air 1, Water 2, Earth 1, Astral 2, Death 2, Nature 2, Holy 1. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Nidavangr battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Nidavangr Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Nidavangr matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Nidavangr monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Nidavangr unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Nidavangr source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLVII: Middle Age Ys, Morgen Queens

## Ys one-page command brief

Middle Age Ys converts amphibious Morgen nobility, sacred knights, and coastal mobility into expansion, research, and strategic pressure. The pinned roster resolves 10 commander identities and 9 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 2 active nation-restricted spell records. Its chief planning risks are land–sea transitions, glamour interactions, and elite replacement.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Ys evidence and ruleset

This dossier covers unmodded Middle Age Ys on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 85, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Ys object without a named official record. No runtime test, replay, save, or new test asset was used.

## Ys conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Ys recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 4 | 5 | Direct pinned membership rows |
| Regional or coastal | 3 | 3 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 3 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Ys commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2912 | Ysian Scout | none | 0 |
| 2913 | Ysian Commander | none | 75 |
| 2914 | Ysian Druid | W1 E1 H1; random: 100% ×1 mask 11776 link 1 | 10 |
| 2931 | Knight Commander of Ys | none | 100 |
| 2900 | Kernou Chieftain | none | 75 |
| 2928 | Swanherd | none | 50 |
| 2901 | Kernou Druid | E1 S1 H1; random: 100% ×1 mask 11776 link 1 | 10 |
| 2917 | Morgen Champion | W1 G1 H1 | 100 |
| 2919 | Morgen Princess | W1 G2 H2 | 150 |
| 2921 | Morgen Sorceress | W2 E1 G3 H2; random: 100% ×1 mask 18048 link 1; 10% ×1 mask 18048 link 1 | 50 |


## Ys troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 2907 | Ysian Militia | 14 | 2 | 8 | amphibious |
| 2908 | Ysian Spearman | 14 | 2 | 10 | amphibious |
| 2923 | Ysian Infantry | 14 | 2 | 10 | amphibious |
| 2909 | Ysian Man at Arms | 15 | 2 | 11 | amphibious |
| 2910 | Knight of Ys | 16 | 2 | 13 | amphibious |
| 2897 | Kernou Warrior | 10 | 0 | 10 | ordinary body |
| 2898 | Kernou Noble Warrior | 12 | 0 | 11 | ordinary body |
| 2899 | Kernou Cavalry | 12 | 0 | 11 | ordinary body |
| 2915 | Morvarc'h Knight | 14 | 0 | 14 | sacred, amphibious |


## Ys mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2914 | Ysian Druid | W1 E1 H1; random: 100% ×1 mask 11776 link 1 | 10 |
| 2901 | Kernou Druid | E1 S1 H1; random: 100% ×1 mask 11776 link 1 | 10 |
| 2917 | Morgen Champion | W1 G1 H1 | 100 |
| 2919 | Morgen Princess | W1 G2 H2 | 150 |
| 2921 | Morgen Sorceress | W2 E1 G3 H2; random: 100% ×1 mask 18048 link 1; 10% ×1 mask 18048 link 1 | 50 |


The highest fixed recruitable paths resolved in these rows are Water 2, Earth 1, Astral 1, Glamour 3, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Ys capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 185 | Ker-Ys | W1, E2, G2 | Morgen Champion, Morgen Princess, Morgen Sorceress, Morvarc'h Knight |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Ys national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 447 | Herd of Morvarc'h | Conjuration 4 | G2 W1 | 12 |
| 1294 | Geas | Thaumaturgy 3 | G2 | 0 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Ys national item boundary

No nation restriction or rebate link appears in the pinned item rows. This does not establish live forge pricing or exclude undocumented behaviour.


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Ys hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 2924 | Queen of the North | F3 W2 E2 G3 H2 | assignment only; timing unresolved |
| 2926 | Morgen Queen | F1 W3 E2 G4 H2 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Ys army identities

- Sacred roster: Morvarc'h Knight.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: Ysian Militia, Ysian Spearman, Ysian Infantry, Ysian Man at Arms, Knight of Ys, Morvarc'h Knight.
- Core identity: amphibious Morgen nobility, sacred knights, and coastal mobility.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Ys opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Ys fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Ys, the most likely planning failure is land–sea transitions, glamour interactions, and elite replacement. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Ys research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Ys magic-access ladder

The fixed-path ceiling is Water 2, Earth 1, Astral 1, Glamour 3, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Ys battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Ys Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Ys matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Ys monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Ys unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Ys source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLVIII: Middle Age Pelagia, Triton Kings

## Pelagia one-page command brief

Middle Age Pelagia converts deep-water recruitment, Triton armies, and Water–Astral magic into expansion, research, and strategic pressure. The pinned roster resolves 16 commander identities and 10 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 2 active nation-restricted spell records. Its chief planning risks are aquatic geography, land projection, and commander coverage.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Pelagia evidence and ruleset

This dossier covers unmodded Middle Age Pelagia on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 86, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Pelagia object without a named official record. No runtime test, replay, save, or new test asset was used.

## Pelagia conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Pelagia recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 11 | 6 | Direct pinned membership rows |
| Regional or coastal | 3 | 2 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 3 | 2 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Pelagia commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 1050 | Merman Scout | none | 0 |
| 1052 | Wave Lord | none | 75 |
| 1069 | Pelagian Captain | none | 75 |
| 2421 | Amber Clan Noble | none | 100 |
| 1696 | Merman Priest | H1 | 10 |
| 1415 | Pelagian Mermage | W1; random: 100% ×1 mask 9984 link 1 | 10 |
| 2823 | Pelagian Mystic | A1 W1 E1; random: 100% ×1 mask 3840 link 1 | 10 |
| 1418 | Amber Clan Priest | H1 | 50 |
| 1417 | Amber Clan Mage | F1 W2; random: 100% ×1 mask 9728 link 1 | 50 |
| 2422 | Pearl Clan Priest | H2 | 50 |
| 2423 | Pearl Mage | W2 S1; random: 100% ×1 mask 11008 link 1 | 10 |
| 2825 | Merman Commander | none | 75 |
| 2867 | Daduchos | F1; random: 100% ×1 mask 3840 link 1 | 10 |
| 1061 | Triton Prince | none | 150 |
| 1088 | Triton King | W4; random: 100% ×2 mask 10496 link 1; 10% ×1 mask 11008 link 1 | 100 |
| 2865 | Conqueror of the Closed Realm | H1; random: 100% ×1 mask 3328 link 1 | 100 |


## Pelagia troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 1046 | Merman | 10 | 1 | 10 | amphibious |
| 1048 | Wave Warrior | 10 | 1 | 12 | amphibious |
| 1056 | Pelagian Militia | 12 | 1 | 9 | aquatic |
| 1057 | Pelagian Soldier | 15 | 1 | 11 | aquatic |
| 2416 | Coral Clan Hoplite | 16 | 1 | 12 | aquatic |
| 1419 | Amber Clan Guard | 16 | 1 | 13 | aquatic |
| 2821 | Merman Hoplite | 10 | 1 | 11 | amphibious |
| 2869 | Apostate of the Closed Realm | 13 | 1 | 13 | amphibious |
| 1059 | Knight of the Deeps | 16 | 1 | 14 | sacred, aquatic |
| 2863 | Champion of the Closed Realm | 13 | 1 | 13 | sacred, amphibious |


## Pelagia mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 1696 | Merman Priest | H1 | 10 |
| 1415 | Pelagian Mermage | W1; random: 100% ×1 mask 9984 link 1 | 10 |
| 2823 | Pelagian Mystic | A1 W1 E1; random: 100% ×1 mask 3840 link 1 | 10 |
| 1418 | Amber Clan Priest | H1 | 50 |
| 1417 | Amber Clan Mage | F1 W2; random: 100% ×1 mask 9728 link 1 | 50 |
| 2422 | Pearl Clan Priest | H2 | 50 |
| 2423 | Pearl Mage | W2 S1; random: 100% ×1 mask 11008 link 1 | 10 |
| 2867 | Daduchos | F1; random: 100% ×1 mask 3840 link 1 | 10 |
| 1088 | Triton King | W4; random: 100% ×2 mask 10496 link 1; 10% ×1 mask 11008 link 1 | 100 |
| 2865 | Conqueror of the Closed Realm | H1; random: 100% ×1 mask 3328 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Fire 1, Air 1, Water 4, Earth 1, Astral 1, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Pelagia capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 160 | Palace of Pearls | W4, N1 | Triton Prince, Triton King, Conqueror of the Closed Realm, Knight of the Deeps, Champion of the Closed Realm |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Pelagia national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 367 | Summon Hekateride | Conjuration 5 | N3 W1 | 30 |
| 368 | Summon Daktyl | Conjuration 6 | E3 A1 | 30 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Pelagia national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 329 | Clam of Pearls | 3 | W1 N1 | rebate |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Pelagia hero boundary

No fixed hero-slot identity was resolved from attributes 139–149. Hero arrival and timing remain unscheduled.


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Pelagia army identities

- Sacred roster: Knight of the Deeps, Champion of the Closed Realm.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: Merman, Wave Warrior, Pelagian Militia, Pelagian Soldier, Coral Clan Hoplite, Amber Clan Guard, Merman Hoplite, Apostate of the Closed Realm, Knight of the Deeps, Champion of the Closed Realm.
- Core identity: deep-water recruitment, Triton armies, and Water–Astral magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Pelagia opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Pelagia fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Pelagia, the most likely planning failure is aquatic geography, land projection, and commander coverage. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Pelagia research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Pelagia magic-access ladder

The fixed-path ceiling is Fire 1, Air 1, Water 4, Earth 1, Astral 1, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Pelagia battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Pelagia Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Pelagia matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Pelagia monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Pelagia unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Pelagia source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part XLIX: Middle Age Oceania, Mermidons

## Oceania one-page command brief

Middle Age Oceania converts aquatic armies, Capricorns, and Water–Nature magic into expansion, research, and strategic pressure. The pinned roster resolves 8 commander identities and 12 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 1 active nation-restricted spell records. Its chief planning risks are sea expansion variance, land access, and mixed habitat limits.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Oceania evidence and ruleset

This dossier covers unmodded Middle Age Oceania on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 87, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Oceania object without a named official record. No runtime test, replay, save, or new test asset was used.

## Oceania conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Oceania recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 7 | 9 | Direct pinned membership rows |
| Regional or coastal | 3 | 2 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 1 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Oceania commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2370 | Ichtysatyr Scout | none | 0 |
| 2372 | Ichtysatyr Commander | none | 50 |
| 2410 | Ichtycentaur Commander | none | 100 |
| 2392 | Aphroi Hierophant | H1; random: 100% ×1 mask 8704 link 1 | 50 |
| 1054 | Siren | A1 W2 G2 | 0 |
| 2861 | Haliade | W2 N2 H2; random: 100% ×1 mask 9984 link 1; 10% ×1 mask 9984 link 1 | 100 |
| 1038 | Capricorn | W2 E1 N4; random: 100% ×1 mask 1792 link 1; 10% ×1 mask 9984 link 1 | 100 |
| 2399 | Aphroi Lord | none | 100 |


## Oceania troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 2404 | Ichtysatyr | 12 | 2 | 8 | amphibious, stealthy |
| 2406 | Ichtysatyr | 12 | 2 | 9 | amphibious, stealthy |
| 2408 | Ichtysatyr Soldier | 12 | 2 | 9 | amphibious |
| 1043 | Ichtysatyr Soldier | 12 | 2 | 9 | amphibious |
| 1045 | Mermidon | 14 | 2 | 11 | amphibious |
| 2412 | Ichtytaur | 30 | 4 | 12 | amphibious |
| 2414 | Ichtytaur Warrior | 30 | 4 | 12 | amphibious |
| 1408 | Ichtycentaur | 20 | 4 | 12 | amphibious |
| 1410 | Ichtycentaur Cataphract | 22 | 4 | 14 | amphibious |
| 2376 | Ichtysatyr | 12 | 2 | 9 | amphibious, stealthy |
| 2378 | Ichtysatyr Warrior | 12 | 2 | 9 | amphibious |
| 2401 | Aphroi | 24 | 4 | 14 | sacred, amphibious |


## Oceania mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 2392 | Aphroi Hierophant | H1; random: 100% ×1 mask 8704 link 1 | 50 |
| 1054 | Siren | A1 W2 G2 | 0 |
| 2861 | Haliade | W2 N2 H2; random: 100% ×1 mask 9984 link 1; 10% ×1 mask 9984 link 1 | 100 |
| 1038 | Capricorn | W2 E1 N4; random: 100% ×1 mask 1792 link 1; 10% ×1 mask 9984 link 1 | 100 |


The highest fixed recruitable paths resolved in these rows are Air 1, Water 2, Earth 1, Nature 4, Glamour 2, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Oceania capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 162 | The Grove of Aphros | W1, N3, G1 | Aphroi Lord, Aphroi |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Oceania national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 337 | Grow Fortress | Alteration 0 | N4 | 35 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Oceania national item boundary

No nation restriction or rebate link appears in the pinned item rows. This does not establish live forge pricing or exclude undocumented behaviour.


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Oceania hero boundary

No fixed hero-slot identity was resolved from attributes 139–149. Hero arrival and timing remain unscheduled.


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Oceania army identities

- Sacred roster: Aphroi.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: Ichtysatyr, Ichtysatyr, Ichtysatyr Soldier, Ichtysatyr Soldier, Mermidon, Ichtytaur, Ichtytaur Warrior, Ichtycentaur, Ichtycentaur Cataphract, Ichtysatyr, Ichtysatyr Warrior, Aphroi.
- Core identity: aquatic armies, Capricorns, and Water–Nature magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Oceania opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Oceania fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Oceania, the most likely planning failure is sea expansion variance, land access, and mixed habitat limits. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Oceania research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Oceania magic-access ladder

The fixed-path ceiling is Air 1, Water 2, Earth 1, Nature 4, Glamour 2, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Oceania battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Oceania Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Oceania matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Oceania monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Oceania unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Oceania source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part L: Middle Age Atlantis, Kings of the Deep

## Atlantis one-page command brief

Middle Age Atlantis converts armoured amphibious troops and Water–Earth–Death magic into expansion, research, and strategic pressure. The pinned roster resolves 9 commander identities and 13 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 1 active nation-restricted spell records. Its chief planning risks are resource-heavy troops, cold-water geography, and land transition.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## Atlantis evidence and ruleset

This dossier covers unmodded Middle Age Atlantis on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 88, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any Atlantis object without a named official record. No runtime test, replay, save, or new test asset was used.

## Atlantis conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## Atlantis recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 6 | 11 | Direct pinned membership rows |
| Regional or coastal | 3 | 2 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 1 | 1 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## Atlantis commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 432 | Scout | none | 0 |
| 207 | Shambler Chief | none | 75 |
| 441 | Consort | H1 | 100 |
| 112 | Coral Queen | H3 | 200 |
| 322 | King of the Deep | W3; random: 100% ×1 mask 3712 link 2; 10% ×1 mask 3712 link 1 | 50 |
| 3096 | Mage of the Deep | W2; random: 100% ×1 mask 3712 link 1 | 10 |
| 102 | Initiate of the Deep | W1 | 10 |
| 2859 | Witness of the Deep | W2 S1 | 10 |
| 104 | Deep Seer | W3 S2 H1 | 50 |


## Atlantis troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 110 | Atlantian Militia | 12 | 2 | 8 | amphibious |
| 111 | Atlantian Shield Bearer | 12 | 2 | 10 | amphibious |
| 107 | Atlantian Light Infantry | 12 | 2 | 10 | amphibious |
| 1621 | Atlantian Infantry | 12 | 2 | 10 | amphibious |
| 1620 | Reef Warrior | 13 | 2 | 12 | amphibious |
| 108 | Coral Guard | 14 | 2 | 13 | amphibious |
| 1622 | Coral Guard | 14 | 2 | 13 | amphibious |
| 206 | Shambler | 22 | 6 | 11 | amphibious |
| 2862 | Shambler Guard | 22 | 6 | 12 | amphibious |
| 208 | War Shambler | 23 | 6 | 13 | amphibious |
| 211 | Lobster Rider | 13 | 2 | 11 | amphibious |
| 2860 | Soldier of the Deep | 10 | 0 | 12 | poor amphibian |
| 209 | Mother Guard | 25 | 6 | 14 | sacred, amphibious |


## Atlantis mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 441 | Consort | H1 | 100 |
| 112 | Coral Queen | H3 | 200 |
| 322 | King of the Deep | W3; random: 100% ×1 mask 3712 link 2; 10% ×1 mask 3712 link 1 | 50 |
| 3096 | Mage of the Deep | W2; random: 100% ×1 mask 3712 link 1 | 10 |
| 102 | Initiate of the Deep | W1 | 10 |
| 2859 | Witness of the Deep | W2 S1 | 10 |
| 104 | Deep Seer | W3 S2 H1 | 50 |


The highest fixed recruitable paths resolved in these rows are Water 3, Astral 2, Holy 3. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## Atlantis capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 2 | The Coral Towers | W5 | Deep Seer, Mother Guard |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## Atlantis national spell map

| ID | Spell | School | Requirement | Cost field |
| ---: | --- | --- | --- | ---: |
| 370 | Summon Monster Fish | Conjuration 6 | W3 | 6 |


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## Atlantis national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 18 | Coral Blade | 3 | W1 | rebate |
| 443 | Orb of Atlantis | 9 | W4 E1 | rebate |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## Atlantis hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 373 | Coral Prince | W1 H2 | assignment only; timing unresolved |
| 558 | Seer King | W4 S3 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## Atlantis army identities

- Sacred roster: Mother Guard.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: Atlantian Militia, Atlantian Shield Bearer, Atlantian Light Infantry, Atlantian Infantry, Reef Warrior, Coral Guard, Coral Guard, Shambler, Shambler Guard, War Shambler, Lobster Rider, Soldier of the Deep, Mother Guard.
- Core identity: armoured amphibious troops and Water–Earth–Death magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## Atlantis opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## Atlantis fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For Atlantis, the most likely planning failure is resource-heavy troops, cold-water geography, and land transition. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## Atlantis research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## Atlantis magic-access ladder

The fixed-path ceiling is Water 3, Astral 2, Holy 3. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## Atlantis battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## Atlantis Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## Atlantis matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## Atlantis monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## Atlantis unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## Atlantis source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


# Part LI: Middle Age R'lyeh, Fallen Star

## R'lyeh one-page command brief

Middle Age R'lyeh converts mind control, aquatic slave troops, and powerful Astral magic into expansion, research, and strategic pressure. The pinned roster resolves 8 commander identities and 13 troop identities across ordinary, regional, coastal, and site-linked recruitment, plus 0 active nation-restricted spell records. Its chief planning risks are slave morale, magic leadership, land access, and friendly-fire risk.

The safe operating plan is to keep recruitment geography visible, buy commanders for named jobs, label every random mage, connect research to casters already owned, and preserve a replacement route before committing elite or capital-limited troops. Exact expansion parties, scripts, formations, spell targets, freespawn composition, transformation results, and combat outcomes remain open unless a source below states them directly.

## R'lyeh evidence and ruleset

This dossier covers unmodded Middle Age R'lyeh on the Dominions 6.37 executable baseline. Player-facing rules are governed by the revision-2 official manual and official patches through 9 September 2026. Nation ID 89, roster memberships, unit fields, random masks, sites, spell restrictions, item links, and hero assignments are cross-checked against the pinned Inspector 6.35 commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

The structured snapshot is not relabelled as live 6.37 data. The 6.37 patch's unspecified statistic corrections are not assigned to any R'lyeh object without a named official record. No runtime test, replay, save, or new test asset was used.

## R'lyeh conversion chain

```text
verified recruitment and national assets
-> provinces, forts, laboratories, temples, scouts, and replacement routes
-> labelled fixed and random path access
-> research, searching, forging, rituals, and battlefield support
-> surviving armies, sieges, claims, raids, and strategic depth
```

## R'lyeh recruitment geography

| Recruitment layer | Commanders | Troops | Evidence boundary |
| --- | ---: | ---: | --- |
| Ordinary forts | 7 | 13 | Direct pinned membership rows |
| Regional or coastal | 0 | 0 | Non-fort and coast membership rows; exact terrain availability remains source-dependent |
| Site-linked | 1 | 0 | Explicit site recruit fields; capital grouping follows the nation-site association |

Empty ordinary rows do not prove that a nation lacks forces. Freespawn, reanimation, events, summoning, dominion effects, and special recruitment remain separate mechanisms.

## R'lyeh commander roster

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 432 | Scout | none | 0 |
| 444 | Traitor Prince | none | 100 |
| 1527 | Slave Priest | H1 | 10 |
| 1518 | Slave Mage | W2 S1; random: 100% ×1 mask 11776 link 1 | 10 |
| 445 | Illithid Lord | none | 50 |
| 443 | Star Child | S1 | 0 |
| 333 | Starspawn | W1 S2 H2; random: 100% ×1 mask 19968 link 1 | 10 |
| 332 | Starspawn | W1 S3; random: 100% ×2 mask 19968 link 1; 10% ×1 mask 19968 link 1 | 10 |


## R'lyeh troop roster

| ID | Unit | HP | Protection | Morale | Traits |
| ---: | --- | ---: | ---: | ---: | --- |
| 1517 | Slave Trooper | 15 | 1 | 7 | aquatic |
| 1526 | Slave Guardian | 15 | 1 | 7 | aquatic |
| 1515 | Slave Trooper | 10 | 1 | 7 | amphibious |
| 1524 | Slave Guardian | 10 | 1 | 7 | amphibious |
| 335 | Slave Trooper | 12 | 2 | 7 | amphibious |
| 1619 | Slave Guardian | 12 | 2 | 7 | amphibious |
| 336 | Slave Guardian | 12 | 2 | 7 | amphibious |
| 337 | Lobo Guard | 13 | 2 | 50 | magic being, amphibious |
| 424 | Meteorite Guard | 14 | 2 | 12 | amphibious |
| 425 | Shambler Thrall | 24 | 7 | 50 | magic being, amphibious |
| 243 | Crab Hybrid | 25 | 14 | 14 | aquatic |
| 331 | Illithid | 28 | 5 | 10 | magic being, amphibious |
| 407 | Illithid Soldier | 28 | 5 | 10 | magic being, amphibious |


## R'lyeh mage and priest portfolio

| ID | Commander | Fixed and random magic | Leadership |
| ---: | --- | --- | ---: |
| 1527 | Slave Priest | H1 | 10 |
| 1518 | Slave Mage | W2 S1; random: 100% ×1 mask 11776 link 1 | 10 |
| 443 | Star Child | S1 | 0 |
| 333 | Starspawn | W1 S2 H2; random: 100% ×1 mask 19968 link 1 | 10 |
| 332 | Starspawn | W1 S3; random: 100% ×2 mask 19968 link 1; 10% ×1 mask 19968 link 1 | 10 |


The highest fixed recruitable paths resolved in these rows are Water 2, Astral 3, Holy 2. Random masks are printed as raw pinned fields because mask interpretation, linked-roll behaviour, and live display should not be guessed. A rare result is an opportunity after recruitment, never a guaranteed research or ritual schedule.

## R'lyeh capital and national sites

| ID | Site | Monthly fields | Recruits recorded |
| ---: | --- | --- | --- |
| 17 | The Sunken City | W2, S3 | none in explicit recruit fields |
| 45 | The Void Gate | no gem field | Starspawn |


Site rows prove only their explicit fields. Hidden effects, event behaviour, recruitment timing, ownership transitions, and live interface grouping remain unresolved.

## R'lyeh national spell map

No active nation-restricted spell row was found for this nation in the pinned snapshot. Absence here is a metadata boundary, not proof that no shared or special spell exists.


Research does not create the caster, gems, slaves, corpses, laboratory, target, or free mage-turn. Every national spell remains a gated project: research, access, treasury, legal target, and opportunity cost must all be present.

## R'lyeh national item boundary

| ID | Item | Construction | Paths | Link |
| ---: | --- | ---: | --- | --- |
| 134 | Anemone Mace | 3 | W1 | restricted |
| 137 | Jellyberd | 7 | S1 F1 | restricted |
| 248 | Armor of Meteoritic Iron | 5 | E1 S1 | rebate |


Restriction and rebate fields establish metadata links, not displayed prices, rounding, stacking, or live forge availability. Those remain open unless the official manual supplies the exact result.

## R'lyeh hero boundary

| ID | Hero record | Magic | Boundary |
| ---: | --- | --- | --- |
| 560 | Stargazer | W2 S5 G1 H2 | assignment only; timing unresolved |
| 660 | Aboleth | W3 S4 G2 | assignment only; timing unresolved |
| 622 | Traitor King | W5 | assignment only; timing unresolved |


Heroes are contingent capacity. None belongs in an opening, research, or path plan that must work every game.

## R'lyeh army identities

- Sacred roster: no sacred troop identified in the reconciled recruit rows.
- Flying roster: no flying troop identified in the reconciled recruit rows.
- Aquatic or amphibious roster: Slave Trooper, Slave Guardian, Slave Trooper, Slave Guardian, Slave Trooper, Slave Guardian, Slave Guardian, Lobo Guard, Meteorite Guard, Shambler Thrall, Crab Hybrid, Illithid, Illithid Soldier.
- Core identity: mind control, aquatic slave troops, and powerful Astral magic.

These labels help assemble testable packages; they do not establish the best formation, script, bless, target, or casualty rate.

## R'lyeh opening and expansion controls

1. Identify whether gold, resources, recruitment points, commander points, corpses, population, slaves, or a special national mechanism limits the first queue.
2. Separate ordinary, regional, coastal, and site-linked recruitment before planning reinforcement.
3. Use mundane leadership where it preserves a valuable mage-turn.
4. Label random mages immediately and keep rare paths out of guaranteed schedules.
5. Add scouts and retreat routes before extending beyond reliable information.
6. Record expansion results rather than publishing an untested party size.

## R'lyeh fort and recruitment doctrine

Additional forts are valuable when they reproduce the commander or troop required by the next job. Regional and coastal recruitment must be evaluated where it exists rather than averaged into a fictional universal roster. Capital or site-linked units need a replacement ledger because their opportunity cost competes with every other capital-limited purchase.

For R'lyeh, the most likely planning failure is slave morale, magic leadership, land access, and friendly-fire risk. The remedy is a visible queue showing location, bottleneck, expected role, and replacement time.

## R'lyeh research response tree

- **Fixed-path branch:** begin with spells the repeatable mage roster can cast without a random, booster, hero, or Pretender.
- **Random-path branch:** open only after the qualifying mage is recruited and labelled.
- **National-spell branch:** verify the exact research level, caster, cost, target, and free mage-turn from the spell table.
- **Construction branch:** compare each forge turn against research, searching, ritual work, and army support; item metadata alone does not prove a discount.
- **Summon or reanimation branch:** account for gems, corpses, slaves, laboratory access, leadership, and unresolved arrival behaviour.

## R'lyeh magic-access ladder

The fixed-path ceiling is Water 2, Astral 3, Holy 2. Access above that line needs a named bridge: booster, empowerment, communion or chorus where legal, summoned mage, hero, Pretender, or another directly verified source. Two partial paths on different commanders cannot be combined to cast one spell.

## R'lyeh battlefield packages

### Line and support package

Use the most replaceable suitable troops as frontage, place commanders according to actual leadership, and protect mages whose turns are needed for research or rituals. Armour, morale, fatigue, size, formation width, and the opponent decide whether the line survives.

### Elite or sacred package

Use sacred or elite troops only when their recruitment location, bless, priest coverage, and replacement rate justify the commitment. Capital scarcity is a strategic cost even when the unit performs well.

### Mobility or habitat package

Flying, stealthy, sailing, aquatic, amphibious, cave, forest, or wasteland tools must be checked against legal movement, supply, retreat, and reinforcement. A trait is not permission to ignore geography.

### Mage package

Script from paths actually present on the recruited commanders. Keep gem use, fatigue, friendly fire, magic resistance, battlefield size, and enemy resistances visible; no generic script is treated as verified performance.

## R'lyeh Pretender families

| Family | What it can solve | What it cannot conceal |
| --- | --- | --- |
| Missing-path bridge | Opens a named booster, ritual, or battlefield threshold | Research, gems, laboratories, and mage-turns remain required |
| Economy and infrastructure | Funds forts, laboratories, temples, commanders, and replacements | Gold does not create local resources, gems, corpses, slaves, or commander points |
| Sacred support | Improves a verified sacred package | Recruitment limits, priest coverage, and counters remain |
| Awake expansion body | Reduces pressure on the starting roster | Performance depends on settings, map, chassis, scales, script, and opponents |
| Resistance package | Covers a documented roster weakness | One resistance is not universal defence |

## R'lyeh matchup and failure matrix

| Enemy problem | First answer to examine | Avoid |
| --- | --- | --- |
| Massed light units | Replaceable width, area effects, morale pressure, and reserves | Spending every scarce elite turn on basic frontage |
| Heavy armour | Higher damage, armour-piercing or negating magic, fatigue, and buffs | Assuming ordinary weapons solve protection unaided |
| Accurate missiles | Screens, protection, spacing, speed, and disruption | Exposing commanders or fragile elites without guards |
| Elemental resistance | Shift damage type and use physical or fatigue pressure | Building the complete research plan around one element |
| Fast raiders or flyers | Scouts, local leadership, layered defence, and mobile reserves | Concentrating every commander in one army |
| Large targets | Concentrated attacks, debuffs, control, and size-aware counters | Treating trampling or low-damage swarms as universal |
| Underwater or land transition | Verified amphibious access, coastal staging, summons, or allies | Assuming a habitat transition works because a related unit can cross |

## R'lyeh monthly audit

- Which recruitment layer supplies each current army and mage role?
- What is the active bottleneck at every fort?
- Are random mages labelled and excluded from guaranteed schedules until present?
- Does each research target have a legal caster and treasury?
- Are capital, coastal, regional, freespawn, and ordinary replacements tracked separately?
- Are scouts, laboratories, temples, leadership, supply, and retreat routes keeping pace?
- Are heroes excluded from plans that must work every game?
- Have uncertain mechanics remained marked as uncertain?

## R'lyeh unresolved evidence boundary

The dossier does not claim exact expansion counts, formation performance, script outcomes, random-path display, freespawn or reanimation composition, special-dominion timing, transformation or mount resolution, summon arrival state, item-price stacking, hero timing, stealth detection, sailing routes, underwater transition, event outcomes, or battlefield casualty ranges. Nation-specific mechanics implied by names or summaries remain qualitative unless an explicit source field settles them. R-047, R-058, and every comparable engine-dependent investigation remain parked.

## R'lyeh source note

- *Dominions 6 Manual*, revision 2: nation summary, visible roster, recruitment markings, national rules, and spell descriptions.
- Official Dominions patch history through 6.37: current executable chronology; generic 6.37 statistic fixes are not assigned to unnamed objects.
- Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`: nation ID, membership rows, unit fields, random masks, sites, spell restrictions, item links, and hero assignments.
- Strategy sections are bounded doctrine derived from verified capacity. They are not runtime test results.


<!-- GENERATED REMAINING MA DOSSIERS END -->

## Dossier source register

### Official

- *Dominions 6 Manual*, revision 2: all 37 unmodded Middle Age nation pages; national spells and rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; sailing; flying; forging; habitat transitions; and fort construction.
- Illwinter official patch history through 6.37, including the current Send Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, Agartha's 6.04 Oracle-shape note, and 6.37's bounded research, drowning, and Drake corrections. Generic statistic fixes are not assigned to unnamed nation objects.

### Structured snapshot

- Dominions 6 Data Inspector, commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, pinned to the 6.35 data update; used for mage random masks, recruitment records, capital sites, national spell restrictions, national item fields, and current object cross-checks.

### Interpretation boundary

Roster entries, path masks, costs, site income, item restrictions, and national ritual requirements are source facts. Openings, research trees, Pretender families, battlefield packages, and matchup advice are strategy. Expansion counts, random-result timing, Blood returns, crossbreeding outputs, displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, ancestor-summon behaviour, conscription output, variable summon quantities, retinue and shape behaviour, flying and storm resolution, ice-equipment scaling, Guardian Spirit behaviour, remote ritual outcomes, spell targeting, and combat outcomes remain observation questions until a versioned raw set is published.
