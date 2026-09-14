# Foundation Book IV: Armies and Battle

## Why battles need a systems view

Dominions 6 battles are not decided by a single comparison between two armies. They are decided by a sequence of contacts, checks, delays, target choices, damage rolls, fatigue thresholds, morale failures, and retreat outcomes. A force can possess more gold value, more bodies, and more nominal damage yet still lose because it reaches the wrong part of the field, exhausts itself, exposes its commanders, or begins routing before its strength can be applied.

> **Foundation rule:** An army is not a collection of units. It is a timed delivery system for damage, control, morale pressure, and magic.

The early chapters make the Army Setup screen and battle replay readable. Later chapters deal with formation timing, combat arithmetic, counter design, and the difference between winning one battle and preserving a force for the next. The manual explains much of the arithmetic unusually well, but it does not expose every targeting weight, pathfinding choice, cooldown, or rounding step. Hidden values stay labelled as such.

## Edition note

The ruleset and evidence terms come from Book I. Book IV owns battlefield resolution: hit checks, damage, protection, fatigue, morale, retreat, and the combat side of spellcasting. Book V uses those rules to build magical strategy rather than printing them again. Exact DE and Divinitus object changes belong to Book IX and the later nation dossiers.

## Current-version corrections that matter

Several post-manual changes materially affect battle analysis:

| Version | Current rule or correction | Practical consequence |
| --- | --- | --- |
| 6.23 | Fear can reduce morale by no more than the Fear value, with an absolute maximum reduction of 10 | Older descriptions can overstate rapid morale collapse |
| 6.23 | Floating mounts are no longer impeded by non-floating riders | Mixed rider-and-mount movement should be judged from the current unit |
| 6.23 | Spellcasters do not receive the multiple-weapon fatigue penalty | Armed mages should not be analysed with the ordinary extra-weapon fatigue rule |
| 6.25 | Fatigue from flying and trampling was corrected for non-mounted units | Old replays or tests may understate the cost of repeated mobility and trampling |
| 6.25 | Battlefield-wide spells cannot normally be cast indoors; holy spells are excepted | Fort interiors and many assassination fields require different spell plans |
| 6.31 | Regeneration now follows its percentage accurately rather than old hit-point brackets | Current healing estimates should use the displayed percentage |
| 6.34 | Temporary battle effects are correctly removed from Twiceborn units | Persistent-state assumptions from older replays can be wrong |
| 6.35 | Innate spellcasters no longer skip their script after recovering from unconsciousness | Script evaluation for innate casters must use current behaviour |
| 6.35 | Units that automatically regain mounts now do so at the end of the turn | Post-battle mount recovery affects the next turn’s readiness |
| 6.36 | Rust now takes effect even when the attack causes no HP damage | Zero final damage does not prove that an equipment-degrading rider failed |

Patch corrections do not invalidate the manual’s combat structure. They identify the places where an otherwise sound model produces the wrong current result.

## Finding the right section

For the first few battles, concentrate on reading unit cards, forming squads, protecting commanders, placing the line, understanding fatigue and morale, and reviewing the replay. The deeper combat chapters become valuable when a matchup turns on shields, repel, trampling, magic resistance, contact geometry, or a precise rout threshold.

# Part I: What a Battle Decides

## Victory is normally a rout

A Dominions battle is generally fought until one side leaves the field. It is not necessary to kill every enemy. Squads rout when they fail morale checks, all eligible troops rout when their eligible commanders are gone, and an army automatically routs after losing 75% of its weighted total hit points.

This produces four different outcomes that the word “win” can conceal:

| Outcome | Field result | Strategic result |
| --- | --- | --- |
| Clean victory | Enemy routs with few friendly losses | Force remains ready to expand, raid, or fight again |
| Pyrrhic victory | Enemy routs after severe friendly losses | Province gained, campaign tempo lost |
| Productive defeat | Friendly force routs after destroying valuable enemy assets | Field lost, exchange may still improve the war |
| Catastrophic defeat | Command, mages, or retreat routes fail | Army value is destroyed rather than merely displaced |

Kills are an incomplete measure. A spell that causes no direct kills may still win by exhausting, immobilising, frightening, or separating an army. A cheap line can succeed by holding long enough for decisive magic, even if it dies. A killer with an impressive summary can still fail strategically by chasing irrelevant bodies while the centre collapses.

## The five layers of battle

Every battle can be read through five layers:

1. **Delivery:** whether a unit, weapon, spell, or aura reaches a relevant target.
2. **Conversion:** whether contact becomes a hit, failed resistance check, damage, fatigue, or control effect.
3. **Persistence:** whether the effect survives protection, resistance, regeneration, recovery, or replacement.
4. **Cohesion:** whether squads and command remain functional under casualties, fear, fatigue, and displacement.
5. **Preservation:** whether the surviving force retreats safely, retains mounts and commanders, and can fight again.

Most poor diagnoses stop at conversion: “the weapon could not hurt the armour.” Expert diagnosis starts earlier and ends later. The weapon may never have reached the armoured target. The armour may have worked until fatigue enabled armour-defeating hits. The troops may have routed while still physically healthy. The retreat may have converted a recoverable loss into annihilation.

## The open-ended random roll

Dominions commonly uses a **DRN**, an open-ended two-die roll:

```text
DRN = 2d6, open-ended
```

When a die shows 6, one is subtracted, the die is rolled again, and the new result is added. Another 6 continues the process. Extreme results are rare, but they remain possible.

The actor normally has to exceed the opposing value. At equal listed values, the actor’s chance is about 46%, not 50%, because a tied result fails unless the particular rule awards ties differently.

| Acting value minus opposing value | Approximate success |
| ---: | ---: |
| -10 | 3% |
| -8 | 6% |
| -6 | 11% |
| -4 | 18% |
| -2 | 30% |
| 0 | 46% |
| +2 | 62% |
| +4 | 76% |
| +6 | 86% |
| +8 | 92% |
| +10 | 95% |

This curve creates three lessons:

- small statistical advantages matter;
- no ordinary advantage produces certainty;
- repetition turns modest probability into reliable pressure.

An extra point of Attack, Defence, morale, penetration, or resistance is not a decorative improvement. Its value depends on the current difference and on how many times the comparison occurs.

## Long battles

The ordinary expectation is that one force breaks well before the hard limit. When it does not:

| Battle turn | Event |
| ---: | --- |
| 100 | Twilight: battle enchantments and temporary magic effects end; berserk ends; Precision suffers -2; Glamour magic receives +1 |
| 150 | Attacker routs; Darkness imposes -3 Attack, Defence, and Precision, or daylight replaces it in a night battle |
| 170 | Defender routs |
| 200 | All remaining units are killed |

The attacker carries a long-battle clock. Stall plans, fatigue traps, regeneration contests, and endless summoning must be judged against role and side. A plan that “cannot lose” in ordinary exchanges can still lose to that clock.

# Part II: Reading a Unit

## A stat line is a conditional promise

A unit’s displayed statistics describe what it can do before formation, fatigue, leadership, terrain, blesses, spells, injuries, and the enemy intervene. The useful question is not “Is this unit good?” It is:

> Under the expected battlefield conditions, which job can this unit perform repeatedly and at acceptable cost?

## The first-pass unit card

For a first evaluation, record:

| Field | Main question |
| --- | --- |
| Hit Points | How much damage can the body absorb, and how does HP weighting affect rout? |
| Size | How many fit in a square, what can be reached, displaced, mounted, or trampled? |
| Strength | How much melee damage, carrying capacity, siege force, and trample damage is available? |
| Attack | How reliably do directed melee attacks beat Defence? |
| Defence | How reliably are directed melee attacks avoided before harassment and fatigue? |
| Protection | How much physical damage is removed, and where are helmet and armour coverage weak? |
| Precision | How tightly do missiles and spells cluster around the target square? |
| Morale | How long does the squad remain coherent under losses and fear? |
| Magic Resistance | How well are binary magical effects resisted? |
| Encumbrance | How quickly do attacks and spellcasting degrade the unit? |
| Combat Speed | How quickly does the unit cross the field and finish movement cooldowns? |
| Map Move | How useful is the unit in the campaign rather than one isolated battle? |
| Resistances | Which elemental, poison, sleep, or other damage families are reduced? |
| Weapons | Reach, attack and defence modifiers, damage type, number of attacks, and special effects |
| Armour and shield | Body and head protection, Defence penalties, Parry, and shield Protection |
| Abilities | The rules that may dominate the ordinary statistics |

## Build the effective line

The displayed line should be converted into an **effective line** for the planned battle:

```text
effective Attack
= displayed Attack
  + weapon and spell modifiers
  - fatigue penalty
  - underwater or injury penalties
  - multiple-weapon penalty

effective Defence
= displayed Defence
  + weapon and spell modifiers
  - armour and shield penalties already represented where displayed
  - fatigue penalty
  - harassment
  - rout penalty
```

The same method applies to morale, protection, speed, and resistance. A Defence 16 unit that expects to reach 60 fatigue and receive six rapid attacks is not a Defence 16 problem. A Protection 20 unit facing armour-negating shock is not a Protection 20 target. A Morale 15 squad led badly, mixed improperly, and placed in a sparse line may begin the battle far below the headline value.

## Roles rather than tiers

Common battlefield roles include:

| Role | Primary success condition | Common failure |
| --- | --- | --- |
| Line holder | Occupies contact space long enough for the plan to mature | Dies or routs before support resolves |
| Damage dealer | Converts attacks into relevant damage quickly | Attacks the wrong defence layer or cannot reach |
| Flanker | Reaches exposed sides or rear | Targeting, zones of control, or congestion redirects it |
| Screen | Absorbs arrows, charges, spells, or first contact cheaply | Causes friendly obstruction or premature army rout |
| Missile unit | Applies damage or effects before melee contact | Range, Precision, shields, armour, or friendly fire |
| Tramper | Converts size, speed, and mass into repeated displacement and AP damage | Fatigue, high Defence, anti-large damage, or friendly congestion |
| Bodyguard | Prevents assassination or rear access to a commander | Too few, badly placed, or inappropriate against area effects |
| Buffer | Raises friendly effective statistics before contact | Casts too late, wrong targets, or is interrupted |
| Controller | Restricts movement, actions, morale, or targeting | Resistance, immunity, range, or poor spell selection |
| Finisher | Exploits fatigue, rout, or broken protection | Arrives before the target is softened |
| Summoner | Adds bodies, time, and replacement HP during battle | Exhausts, summons too slowly, or feeds rout weighting |
| Commander | Maintains leadership, formation, morale, and orders | Exposed command death collapses the army |

A unit can occupy several roles, but every additional assumption increases the ways the plan can fail.

## Cost must include the campaign

Gold, resources, Recruitment Points, Holy Points, Commander Points, fort access, mage turns, gems, and map mobility all belong in unit valuation. A body that is exceptionally efficient in one battle may still be a poor campaign unit if it is capital-limited, slow to recruit, unable to reach the front, or dependent on a scarce mage package.

# Part III: Command, Squads, and Army Construction

## Squads are the unit of morale and orders

A commander can lead up to five squads. Each squad receives its own formation, position, and order, and calculates morale separately. Dividing an army into squads is a tactical choice, not clerical organisation.

Splitting troops can:

- produce different target orders;
- stagger contact;
- protect specialised troops behind a screen;
- create flank or rear starting positions;
- prevent one local morale failure from routing every similar unit;
- allow a standard or inspirational commander to support the intended group.

Splitting also carries costs:

- leadership morale bonuses can fall when too many squads are assigned;
- small squads make special morale conditions more relevant;
- more scripts and positions create more opportunities for error;
- a commander’s death can still remove every squad under that command from coherent control.

## Leadership and squad morale

The manual defines leadership bands:

| Base Leadership | Squad allowance before penalty | Morale effect |
| ---: | --- | --- |
| 10 | One squad already penalised | -1 with one squad; another -1 to all squads for each extra squad |
| 50 | Two squads | 0 for one or two; -1 to all for each further squad |
| 100 | Three squads | +1 for up to three; each squad above three reduces the bonus by 1 |
| 150 | Four squads | +2 for up to four; a fifth reduces all to +1 |
| 200 | Five squads | +3 to all five |

These morale effects use the commander’s **base leadership band**. Experience can increase capacity without moving the commander into a better morale band.

Experience modifies leadership capacity:

| Experience level | Normal leadership bonus | Poor leader bonus |
| ---: | ---: | ---: |
| 1 | +25 | +5 |
| 2 | +50 | +10 |
| 3 | +50 | +10 |
| 4 | +50 | +10 |
| 5 | +50 | +10 |

This distinction matters when a veteran commander can physically hold a large force but still supplies the original weak morale environment.

## Special leadership

Undead and demons require undead leadership. Magic beings require magic leadership. A unit that is both undead and magical uses undead leadership for command.

Mixing categories can reduce morale:

- one undisciplined unit makes the squad undisciplined and imposes -1 morale;
- mixing undead and living units imposes -1 morale;
- mixing demons with ordinary units imposes -1 morale.

An army can fit under the displayed numeric capacity while still being illegally or badly commanded.

## Command redundancy

If every eligible commander is killed or routed, the troops rout. A large army under one fragile commander has a single structural hit point.

Command redundancy asks:

- How many eligible commanders can remain if the front commander dies?
- Are they protected from arrows, flyers, assassins, remote damage, and area effects?
- Are magical, undead, and ordinary troops each backed by the correct leadership?
- If a commander retreats, will its troops have a safe route?
- Does a redundant commander carry enough leadership to prevent an immediate secondary failure?

Redundancy is not obtained merely by adding an unrelated scout. The replacement must be eligible to command the affected units and must survive in a relevant position.

## Standards, inspiration, and taskmasters

Squad morale can receive:

- home-province bonus;
- friendly-dominion bonus;
- leadership-band modifier;
- Inspiration;
- the highest applicable Standard;
- +1 while blessed.

Standards and Inspiration are not substitutes for correct formation and command. They improve the morale comparison after the triggering condition occurs. They do not prevent command death, excessive fatigue, paralysis, or an automatic 75% army rout.

Taskmasters are primarily relevant to slave leadership and the specific units they govern. A label such as “slave”, “undisciplined”, “mindless”, or “magic being” must be read as an engine category with its own command implications, not as flavour text.

## The command audit

Before every important battle:

1. Count squads under every commander.
2. Check the commander’s base leadership band.
3. Check ordinary, magic, and undead capacity separately.
4. Remove harmful mixing unless it serves a deliberate purpose.
5. Confirm at least one practical command backup.
6. Protect the commanders whose loss triggers the widest collapse.
7. Verify that retreating commanders have friendly destinations.

# Part IV: Formation, Density, and Placement

## The square

A battlefield square normally holds ten size points. Three size-3 humans fit because nine size points are used. Formation Fighter permits greater density.

Density changes:

- the number of melee attacks that can be delivered from a square;
- vulnerability to area effects, trampling, clouds, and missiles;
- the amount of space occupied by the line;
- congestion behind the line;
- the rate at which replacements reach contact;
- missile hit probability through size points in the target square.

There is no universally best density. Dense troops convert frontage into attacks; sparse troops convert frontage into area coverage and reduced clustering.

## Formation types

| Formation | Shape | Requirement | Morale effect | Main use |
| --- | --- | --- | ---: | --- |
| Box | Compact block | Any disciplined squad | 0 | Depth, compact defence, concentrated movement |
| Line | One rank | Good commander | 0 | Maximum frontage and simultaneous contact |
| Double line | Two ranks | Good commander | 0 | Balance of frontage and replacement depth |
| Sparse line | Line with empty squares | Good commander | -1 | Wide screen, reduced clustering |
| Skirmish | Checkerboard | Any; forced for undisciplined | -1 | Separation, missile or area-risk management |

Skirmisher removes the -1 morale penalty from skirmish and sparse line. Tight Rein allows a commander’s undisciplined units to use disciplined formations and specific orders.

## Frontage and depth

A wide line places more weapons into early contact, which is valuable when:

- the squad wins individual exchanges;
- weapon reach or repel rewards simultaneous coverage;
- the plan needs to envelop a smaller formation;
- the enemy relies on a narrow, high-value centre.

Depth is valuable when:

- the front rank will die or fatigue;
- replacements must sustain a holding action;
- the force is protecting a compact magical core;
- the enemy uses flyers or rearward pressure;
- the formation must absorb displacement.

The trade is temporal. Width spends bodies early. Depth reserves bodies for later.

## Placement is a timing instruction

The Army Setup position determines where a squad begins, not where it is guaranteed to fight. A rear squad on Attack Rear may meet a screening unit. A forward mage can still spend several actions preparing a spell. A fast unit behind a slow block can waste its speed in congestion.

Placement should answer:

- Which squad should make first contact?
- Which should still be unengaged on turns three, five, or ten?
- Which friendly square blocks another unit’s path?
- Which commander is visible to flyers or missiles?
- Where will a summoned unit appear relative to the line?
- If the enemy deploys at the opposite extreme, does the timing still work?

## Staggered contact

Staggering is created through position, speed, formation, and Hold orders. It can:

- let buffs resolve before the valuable line enters danger;
- make a cheap screen absorb the first charge;
- prevent every squad from suffering the same opening area spell;
- create fresh troops against an already fatigued enemy;
- keep a finisher away from the initial harassment.

It can also fail by feeding squads separately into a stronger enemy. A stagger is useful only if the earlier wave creates time or degradation that the later wave can exploit.

## Formation checklist

- Does width or depth serve the unit’s actual weapon and role?
- Does the chosen formation impose a morale penalty?
- Can the commander legally provide that formation?
- Is friendly congestion likely?
- Does density worsen the expected enemy counter?
- Will rear or flank placement expose command?
- Is the contact schedule robust to enemy deployment on either side?

# Part V: Orders and Scripting

## Squad orders

General squad orders include:

| Order | Behaviour |
| --- | --- |
| None | The combat AI decides |
| Attack | Advance and fight toward the selected target category |
| Fire | Use missile weapons against the selected target category |
| Guard Commander | Remain near and protect the commander; eligible guards may appear in assassination battles |
| Hold and Attack | Hold for two rounds, firing if able, then attack |
| Hold and Fire | Hold for two rounds, then fire and move into range as required |
| Fire and Keep Distance | Fire while attempting to preserve distance |
| Retreat | Behave as routing and attempt to leave |

The common target categories are:

- none or random;
- Archers;
- Cavalry or fast units;
- Fliers;
- Large Monsters, normally size 7 or greater and otherwise size 6;
- Closest;
- Rearmost.

Target orders express preference rather than a teleporting command. Zones of control, blocked paths, range, target availability, and the unit’s current contact can prevent the preferred target from being reached.

## “Rear” is not a destination

Attack Rear selects a rearward target according to the engine’s targeting and pathing. It does not guarantee commander assassination. The squad can:

- collide with a screen;
- be caught by zones of control;
- choose a rear troop block rather than a commander;
- take a path altered by obstacles;
- lose its target and retarget.

Rear pressure is a system made from mobility, placement, survival, and target access. The order is one component.

## Hold is exactly two rounds

Hold and Attack and Hold and Fire delay for two rounds. They do not create an indefinite wait. A plan requiring a longer delay must use starting distance, speed, obstacles, spell timing, or a different unit rather than assuming that repeated holding exists for squads.

## Commander scripts

A commander can receive five specific orders followed by a general order.

Specific orders include:

- Hold one turn;
- Hold or Fire a weapon;
- Hold or Cast an AI-selected spell;
- Cast a named spell;
- Attack one turn;
- Fly Attack one turn.

General orders include:

- Stay Behind Troops;
- Attack;
- Cast Spells;
- Advance and Cast;
- Retreat.

If a named spell lacks the required gems or a valid target in range, the caster can fall back to an AI-selected spell. A script is a preferred branch, not an infallible playback.

## Conservative gem use

Conservative gem use makes a mage spend gems sparingly and primarily on scripted spells. It can prevent waste in routine fights, but it can also withhold power from an unscripted emergency. The setting belongs in the battle plan:

- scripted gem expenditure;
- intended post-script behaviour;
- expected enemy strength;
- value of gems compared with the force at risk.

“Save gems” is not automatically conservative when the result is the loss of the mage carrying them.

## Script construction

A robust script is built in this order:

1. **State the battle objective.** Hold, kill, rout, delay, break a siege, extract a raider, or destroy a specific asset.
2. **State the enemy defence layers.** Protection, Defence, shields, resistance, MR, regeneration, size, morale, mobility.
3. **Assign answers.** Each important defence layer needs a delivery mechanism.
4. **Create the contact schedule.** Decide which friendly element meets the enemy first.
5. **Place enabling effects before dependent effects.** Accuracy, resistance, mobility, protection, path boosts, and battlefield conditions often need sequencing.
6. **Write failure branches.** Named spell unavailable, target out of range, caster interrupted, screen destroyed, enemy deploys elsewhere.
7. **Set gem policy.**
8. **Protect command and retreat.**
9. **Test both attacker and defender sides.**

## Timing templates

### Screen and strike

- cheap or resistant screen forward;
- decisive troops delayed or placed behind;
- buffers script enabling effects;
- damage package begins as contact fixes the enemy.

Failure: the screen routs so early that morale or pathing disrupts the strike.

### Armour break

- hold the line;
- apply armour-piercing, armour-negating, rust, Strength, or fatigue pressure;
- commit ordinary damage after the protection layer has been weakened.

Failure: the anti-armour component targets the wrong bodies or arrives after the line collapses.

### Fatigue collapse

- survive early damage;
- impose heat, cold, shock, spell fatigue, trampling cost, repeated attack cost, or exhaustion;
- exploit falling Attack and Defence;
- finish unconscious targets.

Failure: the enemy kills faster than fatigue accumulates or possesses sufficient resistance and reinvigoration.

### Morale break

- cause heavy losses or fear near selected squads;
- remove leadership or standards;
- force repeated checks;
- preserve enough mobile pressure to turn rout into strategic loss.

Failure: mindless, berserk, high-morale, or well-led troops ignore the intended pressure.

### Rear disruption

- occupy the main line;
- send suitable mobile units around or over it;
- threaten fragile command and casters;
- prevent the rear force from being intercepted or stranded.

Failure: Attack Rear is treated as a guarantee rather than a pathfinding preference.

## Script audit

- Are all named spells researched?
- Does each caster have the correct gems?
- Are path boosts active before the spell that requires them?
- Is the target likely to exist and be in range?
- Does the spell work underwater, indoors, in a storm, or in the current plane?
- What does the mage do after the fifth order?
- Will fatigue make the final scripted spell impossible or suicidal?
- Are duplicated battlefield enchantments wasting actions?
- Is every commander protected during preparation time?
- Does the plan survive an enemy Hold, flank deployment, or fast charge?

# Part VI: Movement, Contact, and Time

## Combat speed and cooldown

A move of one square costs roughly one point of combat speed; diagonal movement costs about 50% more. Units act individually. After moving or striking they receive a cooldown. A strike generally creates a long cooldown of about a round; movement creates a shorter cooldown influenced mainly by combat speed with some randomness.

When adjacent units are ready, the one whose cooldown finishes first attacks. Combat speed affects more than time to contact. It influences:

- path crossing;
- replacement into gaps;
- disengaged movement;
- how quickly a unit acts after a step;
- whether a fast unit can exploit a displaced or newly exposed square.

It does not multiply melee attacks as though every point were an attack-speed statistic.

## Zones of control

An adjacent enemy creates a zone of control that normally halts movement. Routing units ignore zones of control.

Zones of control turn screens into spatial tools. A cheap body can stop or redirect a more valuable unit even if it cannot defeat that unit. Conversely, a fast flanker that touches the wrong enemy may lose its strategic role.

## Displacement

A unit at least three size points larger than each displaced unit can enter an otherwise full square by displacing smaller occupants, at an additional cost of one combat-speed point. Non-routing tramplers avoid displacing friendly units because doing so would harm them.

Displacement can:

- break a neat line;
- expose units behind it;
- create congestion;
- change targeting and adjacency;
- move victims even when trample damage is avoided.

## Obstacles and battlefield terrain

Obstacles, gates, walls, caves, water, storms, darkness, and indoor battlefields can alter legal movement and spell use. The manual establishes the large rules but not every pathfinding weight. Exact obstacle navigation belongs to map-specific observation and tests.

Treat battlefield terrain as a component of the script:

- Can the wide line physically deploy?
- Will large units fit through a gate?
- Can flyers operate under the current condition?
- Is the battle indoors, preventing most battlefield-wide magic?
- Does darkness penalise the army more than its opponent?
- Is the weather changing fire, cold, Precision, or storm-dependent abilities?

# Part VII: Melee Resolution

## The hit check

For a directed melee attack:

```text
Attack roll  = Attack + DRN - fatigue penalty
Defence roll = Defence + DRN - fatigue penalty
```

The attacker must exceed the defender. The defender wins ties.

Fatigue penalties are:

```text
Defence penalty = floor(Fatigue / 10)
Attack penalty  = floor(Fatigue / 20)
```

Defence collapses twice as quickly as Attack. This asymmetry is one reason fatigue turns stable lines into sudden massacres.

## Damage and protection

After a hit:

```text
Damage roll     = Strength + weapon Damage + DRN
Protection roll = relevant Protection + DRN
                  + shield Protection on a shield hit
```

Damage is inflicted only when the damage roll exceeds the protection roll.

The displayed damage figure for a weapon may already incorporate Strength and weapon rules in the interface. The formula explains resolution; it should not be used to add Strength twice to a value already presented as final damage.

## Shields: avoidance and absorption

A shield has:

- Defence implications included in the unit’s effective Defence;
- a Parry value;
- a Protection value.

If the attack beats Defence but not Defence plus Parry, it is a **shield hit** and shield Protection is added to the protection roll. If it also beats Defence plus Parry, it is a **clean hit** and the shield does not add Protection.

Shields create two defensive layers:

1. a wider band in which an attack strikes the shield;
2. added protection when that occurs.

They are not a flat chance to cancel all attacks.

## Armour-defeating protection rolls

An unusually low protection die can produce an armour-defeating hit that bypasses 25% of protection:

| Target state | Protection die results that qualify |
| --- | --- |
| Below 50 fatigue | 2 |
| 50 or more fatigue | 2-3 |
| 100 or more fatigue | 2-4 |
| Immobilised or unconscious | Treated as 100 fatigue |

Protection remains valuable, but fatigue increases the tail risk that heavy armour is partly bypassed. This is another mechanism by which fatigue converts time into lethality.

## Shield damage

Shield resistance is:

```text
shield resistance = shield Protection + 5 if magical
```

Break force uses the incoming damage before ordinary protection:

- slashing attacks receive +50% for shield breaking;
- blunt attacks receive +25%;
- at three times resistance, the shield is damaged;
- at five times resistance, it breaks;
- a damaged shield hit again has a 25% chance to break.

A damaged shield loses 20% of its Protection; a broken shield loses 50%. Damaged magical shields repair after battle, but a broken magical shield is permanently destroyed. Mundane shields require spare provincial resources for repair.

## Hit locations and reach

The ordinary hit-location distribution is:

| Location | Chance |
| --- | ---: |
| Torso | 50% |
| Arms | 20% |
| Legs | 20% |
| Head | 10% |

Reach limits which locations can be struck:

- head requires attacker size plus weapon length at least target size;
- torso requires one less;
- arms require two less.

Some low-bodied monsters are easier to reach. An attacker significantly larger than the target shifts the normal distribution toward head hits: head rises to 20% and legs fall to 10%. For mounted attackers, mount size is used for this comparison.

Damage to an arm, leg, or non-essential head is capped at half the target’s maximum HP during melee resolution. Location still matters greatly because affliction type and armour coverage depend on it.

## Weapon damage types

| Type | Effect |
| --- | --- |
| Blunt | +25% damage on head hits before protection; +25% shield-breaking force |
| Slashing | +25% damage after protection; +50% shield-breaking force; can sever a struck limb or head when the hit costs at least half maximum HP |
| Piercing | Reduces protection by 15% |
| Armour Piercing | Reduces protection by 50% |
| Piercing plus Armour Piercing | Total protection reduction of 65% |
| Armour Negating | Ignores ordinary protection entirely |

Two-handed weapons add 125% of Strength rather than the ordinary Strength contribution to damage.

Weapons with several damage types can select among them according to the weapon definition. A label such as slash/pierce should not be analysed as if both protection modifications always apply simultaneously.

## Underwater weapon penalties

Underwater:

- slashing and blunt attacks receive an Attack penalty equal to weapon length;
- piercing attacks receive no such penalty;
- mixed piercing weapons halve the penalty;
- flails receive another -1.

A weapon that works well on land can become a liability underwater even when the unit itself can breathe.

## Multiple weapons and attacks

A unit wielding several ordinary weapons suffers an Attack penalty equal to the sum of their lengths. Ambidextrous offsets this penalty. Bonus and natural weapons do not create the ordinary multiple-weapon penalty.

Each additional wielded weapon after the first adds one Encumbrance. Current official rules exempt spellcasters from the multiple-weapon **fatigue** penalty, but not from every possible attack interaction of the weapons themselves.

Multiple attacks matter because they:

- create more hit checks;
- create more harassment;
- can threaten multiple units;
- trigger more defensive and strikeback effects;
- spend fatigue and expose the attacker to repel interactions.

## Harassment

Every directed melee attack against a unit gives one point of harassment penalty. Each point reduces Defence by one. The penalty decays over time by a percentage rather than disappearing all at once.

- a weapon with multiple attacks gives harassment per attack;
- ranged and area-effect attacks do not;
- rider and mount are separate harassment targets.

Harassment is why a crowd of weak attackers can make a high-Defence elite vulnerable to the attack that matters. The weak attacks need not cause damage to create value.

The precise Dominions 6 decay function is not stated in the manual. A published Dominions 5 result multiplied the remaining penalty by 95% every `16/375` of a round, removing roughly 70% over a fully idle round. That old value is a useful regression-test hypothesis, not a Dominions 6 rule. Edition 27 leaves the current decay test pending.

## Repel

When the defender’s weapon is longer, it automatically attempts to repel the directed melee attack.

The sequence is:

1. a repel attack-and-defence comparison occurs;
2. if the repel attack would hit, the attacker makes a morale comparison;
3. failure aborts the attack;
4. success permits a repel damage roll;
5. if the repel causes any damage, it is capped at one and the original attack then continues.

The morale comparison is:

```text
attacker = Morale + DRN - weapon-length difference
repeller = 10 + DRN + half the margin by which the repel attack won
```

The repelling unit acquires a lingering -2 repel penalty after repeated repel attempts; it decays with time. Size-6 or larger giants count their weapons as one length longer for repel.

Repel combines Attack, weapon length, morale, and tempo. A long weapon on an inaccurate, exhausted unit is not automatically good at repelling attacks.

## Melee resolution order

The manual gives this useful order:

1. Determine target, including rider or mount.
2. Resolve early strikeback effects such as Awe or petrifying gaze; abort if the attacker becomes immobilised.
3. Resolve repel.
4. Resolve later strikeback effects such as Slimer, Sight Vengeance, or Horror Mark Attacker; abort if immobilised.
5. Resolve Attack against Defence.
6. Resolve damage against protection.
7. Resolve defensive abilities such as Mirror Image, Protective Force, Luck, or Mossbody.
8. Apply limb damage cap.
9. Apply redistribution such as Damage Reversal, Blood Bond, or Vengeance.
10. Deal damage, including shield consequences.

If damage redistribution kills the attacker at step nine, the attack is not retroactively cancelled.

# Part VIII: Missiles and Ranged Delivery

## Deviation

A projectile begins to deviate when range exceeds roughly half Precision minus two.

The manual gives:

```text
deviation = range x 1.25 / Precision
```

Precision above 10 receives double value for the excess: Precision 12 is treated as 14 for this purpose.

The formula is best read as expected scatter around a targeted square rather than a direct chance to hit one individual.

## The square hit check

After a projectile reaches a square, a target is selected with size weighting. The hit comparison is:

```text
attacker = DRN + half the size points in the square + 2 if the weapon is magical
defender = DRN + twice shield Parry - Fatigue / 20
```

The attacker must exceed the defender.

This produces several non-obvious results:

- crowded squares are easier to hit;
- large bodies attract more hits within a square;
- shields are central missile defence;
- fatigue reduces missile defence;
- magical missiles gain accuracy at the square-hit stage.

## Ranged damage

Missile damage then uses the ordinary damage-versus-protection structure. Many missiles add half Strength rather than full Strength. Crossbows and similar weapons often gain armour-piercing properties. Lightning is commonly armour negating; fire is commonly armour piercing. The actual weapon definition controls the result.

Missiles can hit friendly units. Screens, line width, range, and the timing of melee contact all affect friendly-fire risk.

## Evaluating archery

Archery value is the product of:

```text
number of shots
x probability of relevant square delivery
x probability of hitting a body
x probability of defeating protection
x strategic value of the target
```

“Many arrows” can be useful without many kills if they:

- damage shields;
- interrupt casters;
- inflict poison or elemental effects;
- remove fragile command;
- force the enemy into a resistant but less efficient composition.

They can also be almost irrelevant against the wrong armour and shield layer.

## Ranged audit

- Is the target category likely to select the intended units?
- Is range beyond the accurate envelope?
- Are friendly troops about to enter the target squares?
- Are shields, Air Shield, protection, resistance, or mist negating the package?
- Does ammunition last long enough?
- Does Hold and Fire change the contact schedule usefully?
- Would a wider or sparser formation improve delivery or survival?

# Part IX: Mounts, Trampling, and Size

## Rider and mount are separate

Dominions 6 treats rider and mount as separate targets with separate HP, statistics, attacks, morale interactions, and afflictions. Area effects and lightning can hit both.

An evaluation of cavalry asks:

- what protects the rider;
- what protects the mount;
- which attacks each performs;
- what happens if one component routs or dies;
- whether equipment affects one or both;
- how replacement and mount recovery work after battle.

## Hitting mounted units

The mount becomes more likely to be targeted when much larger than the rider:

| Mount size advantage | Additional mount targeting rule |
| ---: | --- |
| 3 | 25% |
| 4 | 50% |
| 5 or more | 75% |

Otherwise:

- missiles have a 50% chance to target the mount;
- if mount size is at least reach plus two, the mount is targeted;
- otherwise mount chance is `30% + 10% x mount size - 10% x reach`, with a 10% minimum.

Trample always targets the mount. Area effects and lightning hit both components.

These targeting rules are official. The remaining mounted research question concerns carry, mixed-component movement, and the order in which every exceptional modifier is applied; it no longer treats ordinary target selection as wholly unknown.

## Mounted combat

Both rider and mount can attack. A rider using a two-handed weapon while mounted receives -3 Attack. Skilled Rider improves the mount’s morale and Defence; the amount of usable Defence is affected by mount armour Encumbrance.

Magic items on the rider do not automatically apply every effect to the mount. The item or effect must say so. Mount armour uses the barding slot where available.

## Mounted morale

Fear can affect rider and mount. If the rider routs, the mount leaves with the rider. If only the mount breaks, the rider can be thrown and the mount routs. Falling damage is an open-ended armour-negating comparison based on size difference; chariots avoid ordinary falling damage.

A normal riderless mount routs. A mount with the relevant bravery can remain. The battle summary and replay should be inspected at component level because “cavalry loss” may mean a dead rider, lost mount, or temporary separation.

## Mount recovery

A surviving rider without a mount can claim a matching riderless mount. Otherwise the rider returns home and can be recruited again at half cost while retaining identity, experience, and afflictions. Suitable intelligent mounts can return in a similar fashion.

Mounted commanders remain and can use Reclaim Mount or claim a suitable unit. Some units automatically regain mounts. As of 6.35, automatic recovery occurs at the end of the turn, ensuring the new turn begins mounted.

## Trampling

A trampler entering a square displaces the smaller units to adjacent squares. Each victim checks:

```text
Defence - floor(Fatigue / 10) against 3d6
```

On failure:

```text
trample damage = 7 + trampler Size
```

The damage is armour piercing. An ethereal trampler deals half normal trample damage. A victim that passes the Defence check is still displaced and takes one damage. A trampled unit always takes at least one damage regardless of protection.

Trampling is simultaneously:

- movement;
- displacement;
- repeated Defence pressure;
- armour-piercing damage;
- fatigue expenditure;
- formation disruption.

## Trample failure modes

Tramplers are vulnerable to:

- high Defence before fatigue;
- targets too large to trample;
- anti-large weapons and concentrated damage;
- cold, shock, and other fatigue pressure;
- poor morale;
- congestion around friendly troops;
- repeated trampling cost;
- mount targeting when the trampler is a mount.

Trampling weak units can look dominant while exhausting the trampler for the decisive contact.

# Part X: Fatigue, Recovery, and Collapse

## The hidden battle economy

Fatigue is a stock accumulated by actions and effects. It reduces combat performance before it causes unconsciousness:

```text
Defence penalty = floor(Fatigue / 10)
Attack penalty  = floor(Fatigue / 20)
```

At 50 fatigue, Defence has fallen by 5 and Attack by 2. At 90, the penalties are 9 and 4. A unit can remain upright while its original stat line has ceased to exist.

## Gaining fatigue

Ordinary melee attacks add current Encumbrance. Spellcasting adds:

```text
listed spell fatigue / (1 + path skill above minimum)
+ base Encumbrance
+ twice armour Encumbrance
```

The listed spell component is divided by excess path skill. The Encumbrance component is not.

Other sources include:

- flying and trampling;
- heat or cold effects;
- shock and fatigue damage;
- bleeding;
- special weapons, spells, and auras;
- extreme battlefield conditions.

## Thresholds

| Fatigue | Consequence |
| ---: | --- |
| Every 10 | -1 Defence |
| Every 20 | -1 Attack |
| 50+ | More protection rolls can become armour defeating |
| 100 | Unit falls unconscious |
| Below 100 again | Unit can regain consciousness |
| 200 | Additional fatigue damage begins converting to HP damage |

An unconscious unit recovers five fatigue per turn until it falls below 100. Reinvigoration and battle effects can accelerate recovery according to their rules. The manual does not fully specify ordinary recovery while a unit remains active.

The current community reference states that every active unit removes one fatigue per combat round and then adds its Reinvigoration. This is the best current working rule, but the page does not publish a version-matched frame-by-frame reproduction. Edition 27 therefore labels it **current community reference**, while the five-point unconscious rule remains official.

At 200 fatigue, each further 50 fatigue damage produces one HP damage. A smaller remainder produces a chance equal to two percent per fatigue point.

## Fatigue as offence

Fatigue warfare can defeat protection without directly ignoring it:

1. Defence falls.
2. More attacks hit.
3. Armour-defeating protection results become more frequent.
4. The unit falls unconscious.
5. Further fatigue converts into damage.
6. The stationary target receives concentrated attacks.

This is why reinvigoration, low Encumbrance, resistance, and relief effects are offensive enablers as well as defensive statistics.

## Fatigue budget

For a key unit, estimate:

```text
starting fatigue
+ scripted action costs
+ expected contact costs
+ environmental and enemy pressure
- recovery
= fatigue at decisive turn
```

The number need not be exact to expose a bad plan. A mage expected to cast five expensive spells in heavy armour or a trampler expected to cross the field and overrun many squares may already be committed past useful performance.

# Part XI: Morale, Fear, Rout, and Retreat

## Squad morale

Squad morale begins from the members’ average and receives applicable modifiers:

- +1 in the home province;
- +1 in friendly dominion;
- leadership-band modifier;
- Inspiration;
- the highest applicable Standard;
- +1 while blessed;
- temporary magic morale.

Magic morale can range from -10 to +1. Negative magic morale recovers gradually, approximately one point every two rounds; positive magic morale persists.

## When squads check

A squad can check morale when:

- it suffers heavy losses since its last check and has at least 20% overall casualties;
- it has four or fewer members and any member is damaged that round;
- it is exposed to nearby Fear;
- Terror or a similar effect forces a check;
- the army has lost at least 50% of its weighted total HP, causing checks each turn thereafter.

At most one ordinary morale check occurs for a squad in a round.

For this purpose, a **wound** is a damage event that leaves a unit at no more than 80% of normal HP. Heavy losses are one wound per two squad members.

## The morale comparison

The manual gives:

```text
morale roll = squad Morale + DRN + survivor bonus from 0 to 5
fear roll   = 14 + DRN
```

The squad routs when the fear roll is greater. Under this wording, a tie is safe.

The current community formula is:

```text
survivor bonus = nearest whole number of
(5 x surviving proportion of the original squad)
```

That matches the manual's `0-5` description, but the published page does not supply a current raw test set and notes uncertainty for commanders. Edition 27 therefore records the formula as a **current community reference**, not an official or reproduced result. Boundary rounding and commander handling remain test pending.

## Army-level rout

At 50% weighted army HP loss, surviving squads begin checking every turn. At 75%, the army automatically routs.

The army total weights some bodies differently:

| Body type | HP weight |
| --- | ---: |
| Ordinary unit | 100% |
| Mount | 25% |
| Province Defence | 25% |
| Slave | 50% |

This weighting affects how a screen, summon, mount, or PD contingent contributes to army-wide collapse. It does not tell whether that body is tactically useful.

## Fear

Fear can reduce magic morale and force squad or individual checks. Current official rules cap morale reduction at the Fear effect’s value and at an absolute ten points.

Fear is strongest when combined with:

- existing casualties;
- command loss;
- fatigue;
- weak leadership;
- small squads;
- blocked or dangerous retreat.

It is weaker against mindless units, berserk behaviour, high morale, strong leadership, and effects that prevent or mitigate fear.

Frighten-like limited effects can reduce morale by no more than their stated amount and do not automatically create every broader Fear interaction. Exact effect text matters.

## Routing units

A routing unit suffers -4 Defence and spends its activity moving toward a friendly battlefield edge. It ignores zones of control. Poison, burning, bleeding, and similar pending damage can still kill it after it leaves.

Mindless units do not rout normally. Without eligible leadership, they can become immobile, attack adjacent enemies, and have a one-third chance per turn to dissolve. Magic or undead troops without the required leadership rout.

## Retreat destination

Each commander has a 75% chance to make a smart retreat. A commander in native terrain receives a second 50% chance after failure.

A smart commander:

- retreats into a friendly fort in the same province if available;
- otherwise chooses a random friendly adjacent province.

A failed smart retreat chooses a random adjacent province, including an enemy province. A unit retreating into enemy territory is killed.

Troops attempt to follow their commander with a morale check:

- squad morale bonus counts double;
- undisciplined units suffer -3;
- skirmish morale penalty applies.

Leaderless troops or troops that fail to follow make individual smart checks at 50%, with the native-terrain second chance still applying.

## Retreat while defending a fort

Units retreating while defending their fort hide inside if the battle is won and they made a smart retreat. If the battle is lost, all such units are killed. Non-smart defenders are killed. Commanders are always smart in this special case, and lone units gain another 50% opportunity.

## Preservation audit

Before committing:

- Which adjacent provinces are friendly?
- Is a friendly fort available?
- Are retreat provinces likely to be cut this turn?
- Are commanders native to the terrain?
- Are undisciplined troops likely to follow?
- Will poison, burning, or bleeding kill retreaters?
- Is a fort defence an all-or-nothing trap?
- Does a nominal victory preserve the force for the next operation?

# Part XII: Resistances and Special Damage

## Resistance

Elemental resistance works like an additional protection layer against its damage family, followed by percentage reduction. Each point corresponds to twice that percentage; resistance 50 gives immunity.

For elemental fatigue effects, resistance counts at double strength when reducing the fatigue component.

Resistance is not interchangeable with protection:

- armour negation can ignore protection but not the relevant resistance;
- poison resistance reduces initial poison application but not the later duration of poison already received;
- immunity thresholds and special interactions differ by damage family.

## Fire and burning

Fire is commonly armour piercing. The chance to catch fire is:

```text
pre-protection fire damage x 4%
```

Fire fatigue counts as one-third for this ignition calculation.

A burning unit suffers `(1dSize) / 2` damage, rounded up, each round: a size-8 unit rolls `1d8`, then halves the result. Fire Resistance 5 halves burning damage. The chance to extinguish is:

```text
25% + Fire Resistance + 5% per Cold scale + 100% in rain
```

with a minimum of 1%. Fire vulnerability is negative resistance. Fire Resistance 10 or more, chill aura, Mistform, and Ethereal prevent burning.

## Cold and freezing

A freezing unit suffers 2d6 additional fatigue each round until it thaws.

The thaw chance is:

```text
25% + Cold Resistance + 5% per Heat scale
```

with a minimum of 1%. Cold Resistance 10 or more, heat aura, and Ethereal prevent freezing.

Fire and cold affect both damage and fatigue.

## Bleeding

Profuse bleeding inflicts:

```text
10 fatigue + 5% of maximum HP per round
```

The chance to stop is 10% plus regeneration. Underwater combat halves the chance that bleeding stops; it does not halve the listed damage.

## Poison

Poison is stored and then applied over time, approximately ten percent of the remaining total per round as evenly as possible.

Poison also reduces Attack and Defence by 25% for each full maximum-HP dose currently stored, capped at 50%. The penalty falls as stored poison is consumed.

Poison Resistance reduces the initial amount. It does not shorten poison already received.

This delay makes poison strategically unusual:

- the victim may win the immediate exchange and die afterward;
- battle summaries can conceal post-contact lethality;
- retreating poison victims can be lost after leaving;
- regeneration and healing do not simply erase the stored schedule.

## Shock and stun

Shock can stun. The chance is:

```text
5% + half the percentage of maximum HP lost to the hit
```

Shock Resistance protects against shock damage and receives the elemental-resistance treatment against fatigue effects. Twist Fate and similar effects must be evaluated with current patch behaviour rather than old assumptions.

## Acid and rust

Iron equipment can rust:

- rust chance is pre-protection acid damage times 4%;
- armour can be damaged based on damage before armour after shield interaction;
- rusty weapons have a chance to become damaged when used.

A damaged weapon suffers -2 damage, or -1 if blunt. Rust converts repeated minor exposure into declining equipment quality. Since 6.36, the rust effect can apply even when the attack causes no HP damage; inspect equipment state rather than using the health bar as a proxy for the secondary effect.

## Life drain

Full life drain:

- heals half the damage;
- removes fatigue equal to twice the damage;
- can raise HP to 150% of maximum plus ten.

Weapons with partial life drain treat only the first five points of damage as drain; further damage is ordinary. Lifeless targets take only 25% of the post-protection drain result and do not heal the attacker. A lifeless attacker can still receive the ordinary benefit of its own life-draining attack.

## Paralysis

Paralysis duration is:

```text
(damage - Size) / 2
```

Repeated paralysis uses the larger duration and can add limited damage from the overlap. Size acts as a defence even when ordinary protection is not the main check.

## False damage

Illusions and many Glamour effects cause false damage. It:

- can kill when real plus false damage reaches HP;
- causes no ordinary afflictions except death;
- is not healed by regeneration, life drain, or ordinary healing;
- does not trigger Damage Reversal, Blood Vengeance, or Blood Bond;
- dissipates at two per round if all enemy Glamour mages are dead.

Current official rules make false damage count toward HP-based rout. A force can be routed by damage that later disappears.

## Clouds and auras

Cloud effects are armour negating and decay by roughly one level per round. Clouds of the same type do not ordinarily overlap; they spread and can increase level only within their limits. Heat and frost clouds cancel one another.

Monster auras commonly create level-one clouds that can accumulate to level two. Spells and items can create stronger clouds.

Clouds transform position and time into damage. The important questions are:

- who occupies the square;
- how long they remain;
- what resistance applies;
- whether the cloud moves, spreads, cancels, or decays;
- whether friendly troops are also exposed.

# Part XIII: Afflictions, Regeneration, and Lasting Loss

## Affliction chance

When a hit causes damage, the basic chance of an affliction equals the percentage of maximum HP lost to that blow. A hit taking 20% of maximum HP produces a 20% base chance. Damage beyond 100% can produce several affliction opportunities.

The chance that an affliction is major is:

```text
affliction chance / 1.5
```

capped at 33%.

Regeneration reduces affliction risk. Since 6.31, regeneration follows its displayed percentage accurately rather than the older HP brackets.

## Location pools

| Location | Minor examples | Major examples |
| --- | --- | --- |
| Any | Battle Fright, Profuse Bleeding | - |
| Head | Eye Loss, Mute | Dementia, Feebleminded, Blind |
| Chest | Chest Wound, Never-Healing Wound | Diseased |
| Arm | Weakened | Lost Arm |
| Leg | Limp | Crippled |

Profuse Bleeding is temporary. Most other afflictions persist until an eligible healing mechanism succeeds.

## Campaign consequences

Affliction valuation depends on the unit:

- lost limbs can remove weapons or slots;
- lost eyes impair Precision and combat;
- feeblemindedness can destroy a mage’s strategic value;
- battle fright undermines command and morale;
- limp and cripple reduce map movement;
- disease creates ongoing attrition.

Troops with a limp can become crippled during long marches. Crippled troops can die while marching. An army that wins but accumulates movement injuries may cease to be an operational army.

## Healing categories

Recuperation, healer abilities, immortality interactions, transformation, and specific sites or spells do not all heal the same afflictions under the same conditions. Undead and lifeless beings are commonly excluded from ordinary affliction healing. Item-caused afflictions can require removal of the item.

The safe method is to inspect the exact ability and target category rather than use “healing” as one universal mechanic.

# Part XIV: Battle Magic within the Army

## Scope

The complete spell, communion, ritual, and research system belongs in Foundation Book V. This part establishes the combat mechanics required to understand an army that includes mages.

## Preparation and recovery

Most spells have a casting time of about one round:

- approximately half is preparation;
- approximately half is recovery.

Battle enchantments and gem-costing spells often take longer. If the caster is damaged during preparation, interruption chance is:

```text
percentage of maximum HP lost + 25%
```

Combat Caster and Mindless halve this chance. Innate spellcasters require no preparation and ignore ordinary casting-time differences. As of 6.35, an innate caster that falls unconscious and later recovers continues its script correctly.

## Spell accuracy

Spell delivery resembles missile delivery:

```text
spell aiming Precision = caster Precision + spell Precision
```

Range, scatter, target-square density, area, and friendly position all matter. A spell with excellent listed damage can be a poor answer if it arrives late, lands unpredictably, or covers the wrong area.

## Magic resistance

When “Magic resistance negates” applies:

```text
caster penetration
= 11 + DRN + half additional skill above the spell requirement

target resistance
= Magic Resistance + DRN + half target skill in the spell path
```

The caster wins ties.

“Easily negates” gives the caster -4 penetration. “Hard to resist” gives +4.

Excess path skill and relevant boosters improve penetration, while path-skilled targets can receive extra resistance against effects in that path.

## Spell fatigue

For a spell with listed fatigue:

```text
path fatigue
= listed fatigue / (1 + caster skill - minimum required skill)

casting encumbrance
= base Encumbrance + 2 x armour Encumbrance
```

The Encumbrance cost is paid per cast and is not reduced by excess skill. Heavy armour can make a high-path mage collapse even when the printed spell cost appears manageable.

## Battle enchantments

Battle enchantments can affect the whole battlefield or continuously alter the battle. They end when their caster dies. At Twilight, all battle enchantments and temporary magical effects are removed.

Current indoor rules prevent most battlefield-wide spells from being cast indoors; holy battlefield-wide spells are excepted. A fort-storming plan must distinguish gate, exterior, and interior conditions.

## Magic as a package

A useful battlefield-magic package identifies:

| Component | Question |
| --- | --- |
| Research | Is every required spell available now? |
| Access | Which mages can cast it without hypothetical boosters? |
| Gems | How many battles can the package sustain? |
| Timing | On which turn does each effect resolve? |
| Delivery | Which square or target category receives it? |
| Protection | How does the caster survive preparation? |
| Fatigue | What remains after the script? |
| Redundancy | What happens if one caster dies or is interrupted? |
| Counter | Which resistance, battlefield condition, or enemy script defeats it? |

## The fifth-order problem

After five specific orders, the general order governs. Many battle plans are excellent for five actions and incoherent thereafter. The post-script state must be designed:

- should the mage remain behind troops;
- advance to reach targets;
- continue casting;
- conserve gems;
- retreat after a task;
- avoid walking into melee?

The sixth action is often where a nominal support mage becomes an expensive casualty.

# Part XV: Sieges, Storming, and Battle Context

## Siege arithmetic

The wall-reduction formulas, repair modifiers, and supply progression belong to Book II and the field reference. Book IV begins where the battle problem starts: only the correct siege orders contribute, and reaching zero wall integrity makes storming available on the next relevant order.

## Storm sequence

Storming occurs after any other battle in the province. A relieving or intercepting battle can weaken or destroy the besieger before the fort assault.

If a commander ordered to Storm Castle is killed before the storming battle, troops under that commander do not participate in the storm.

This creates a two-battle problem:

- preserve storm commanders through the exterior battle;
- retain enough force and scripting for the fort battle;
- account for changed gems, fatigue resets, casualties, and command structure;
- respect indoor restrictions.

## Gates and constrained contact

Fort battles compress frontage and change pathing. Large formations can be delayed by gates, while concentrated area effects can gain value. Exact fort layouts vary and should be inspected in the replay or test game.

A storm script copied from an open field is suspect until it answers:

- which units pass through the gate first;
- where the command core begins;
- whether battlefield-wide magic is legal;
- how defenders exploit interior depth;
- where retreating defenders go.

## Siege supply

A fort’s storage is divided by the number of consecutive siege turns. Storage 300 yields 300, 150, 100, 75, then 60 supply in the first five months. Starvation and disease can weaken a garrison before the storm without changing its roster.

The battle card should include starvation, disease, fatigue-related afflictions, and any shortage of replacement equipment.

# Part XVI: Counter Construction

## Counters are layered

A counter should state which layer it attacks:

| Enemy layer | Candidate answers |
| --- | --- |
| High Defence | Harassment, area effects, trampling, immobilisation, fatigue |
| High Protection | Armour piercing, armour negating, Strength, rust, fatigue, MR effects |
| Shields | High Attack for clean hits, shield breaking, area effects, armour negation |
| Regeneration | Burst damage, decay, disease where applicable, paralysis, control, morale |
| High MR | More penetration, non-MR damage, fatigue, mundane control |
| Elemental resistance | Different damage family, physical damage, MR effects, morale |
| Massed low-HP troops | Area damage, clouds, trampling, fear |
| Giants | Anti-large damage, repeated attacks, control, poison where relevant |
| Flyers and rear pressure | Bodyguards, rear screens, protected redundancy, anti-air or area control |
| Mages | Fast contact, missiles, interruption, assassins, battlefield conditions, resistance |
| Summon spam | Area damage, fatigue control, source elimination, long-battle clock |
| Fear | Morale, leadership, standards, mindless or berserk counters, source removal |
| Tramplers | Defence, size, fatigue, anti-large damage, spacing |

The counter must then pass four tests:

1. **Access:** the nation can produce it in time.
2. **Delivery:** it reaches the intended target.
3. **Scale:** enough instances exist for the enemy force.
4. **Survival:** it remains functional until its work is done.

## Avoid nominal counters

An armour-negating spell is not a counter to armour if:

- research is not complete;
- only one fragile caster can use it;
- the caster lacks range;
- the target resists or kills the caster first;
- the gem cost cannot be sustained;
- the spell AI selects something else;
- indoor conditions prohibit the package.

The correct unit of strategy is the delivered package, not the tooltip.

## Counter-counter planning

After selecting the answer, ask how the opponent adapts:

- changes formation;
- adds resistance;
- changes deployment;
- attacks the caster;
- uses decoys;
- splits the army;
- changes battlefield conditions;
- refuses the battle.

An expert plan is not one unbeatable script. It is a branch with a tolerable response to the most likely counter.

# Part XVII: Battle Replay as Evidence

## Why the summary is insufficient

The summary reports numbers present, kills, and losses. It does not by itself explain:

- who made first contact;
- which spells were interrupted;
- where fatigue crossed a threshold;
- whether a shield or resistance worked;
- which squad failed morale first;
- why a target order redirected;
- whether a commander or mount died before the apparent collapse;
- which damage occurred after retreat.

Kills reward the last damaging event, not every enabling action.

## First replay method

For a new player:

1. Pause at deployment.
2. Use F1 to inspect all units and commanders.
3. Use F2 to inspect weather and dominion.
4. Identify the first-contact squads.
5. Watch once at normal speed without chasing individuals.
6. Watch again with battle-log detail increased.
7. Select a key unit and use its combat log.
8. Record the first irreversible failure.

Useful replay controls include pause, speed changes, grid display, F1 unit list, F2 weather and dominion, and battle-log detail levels one through four.

## The first irreversible failure

The decisive event is often earlier than the visible rout:

- a buff was interrupted;
- a screen made contact one round early;
- a commander stood inside an area effect;
- tramplers became exhausted on decoys;
- missiles stopped when melee geometry changed;
- an MR spell failed repeatedly;
- a squad’s leadership penalty lowered its margin;
- a retreat province was enemy-controlled.

Finding the earliest event that made later failure likely produces a reusable lesson. Recording only the final kill does not.

## Replay worksheet

| Stage | Record |
| --- | --- |
| Deployment | Side, positions, formations, squad sizes, command |
| Conditions | Weather, scales, darkness, storm, indoor or underwater |
| Opening | First spells, first shots, first movement |
| Contact | Turn and location of each squad’s contact |
| Degradation | Fatigue, poison, rust, afflictions, lost mounts, shield damage |
| Cohesion | First morale check, first rout, commander loss |
| Resolution | Automatic rout, long-battle event, or decisive destruction |
| Retreat | Destinations, post-retreat deaths, trapped units |
| Strategic result | Province, gems, mages, commanders, readiness next turn |

## Do not learn from one roll

Open-ended dice produce tails. A controlled comparison should be repeated enough times to distinguish a structural advantage from one improbable result. The goal is not to eliminate randomness. It is to learn whether the plan remains acceptable across it.

# Part XVIII: Active Mod Ruleset

## What the supplied files establish

The frozen combined ruleset loads:

1. `DomEnhanced2_16.dm`;
2. `Divinitus_1.15.3_DE.dm`.

Direct source counts demonstrate the scale of object-level battle changes.

| Command family | DE 2.16 | Divinitus 1.15.3 DE |
| --- | ---: | ---: |
| New monsters | 3,553 | 346 |
| Selected existing monsters | 4,227 | 373 |
| New weapons | 389 | 34 |
| Selected existing weapons | 142 | 0 |
| Selected spells | 2,816 | 17 |
| New spell blocks | 0 | 26 |
| Attack edits | 2,038 | 276 |
| Defence edits | 2,114 | 278 |
| Protection edits | 1,612 | 238 |
| Morale edits | 1,692 | 229 |
| Encumbrance edits | 1,186 | 163 |
| Mount assignments | 178 | 9 |
| Skilled Rider edits | 437 | 1 |
| Trample assignments | 39 | 12 |

Counts are syntactic occurrences, not numbers of distinct final objects. Repeated selections, copied statistics, inherited fields, and later load-order edits can change the effective count.

## What the files do not establish

The supplied `.dm` files create and alter monsters, weapons, spells, items, sites, nations, blessings, and object abilities. They do not present a global rewrite of the engine’s DRN, ordinary Attack-versus-Defence equation, ten-size-point square capacity, 75% army-rout rule, or general retreat algorithm.

Accordingly:

- the foundation mechanics remain the starting model;
- every unit, weapon, spell, mount, and Pretender must be read from the effective combined data;
- unmodded balance conclusions cannot be transferred merely because the core formula is unchanged;
- Divinitus loads second and can overwrite shared selections made by DE.

## Modded battle-analysis rule

For a combined guide:

```text
engine mechanic
+ effective DE object
+ later Divinitus overwrite
+ national availability
+ current patch correction
= claim that can be published
```

The name of an object is not enough. A DE or Divinitus version may share a familiar name while changing damage, paths, fatigue, attack count, resistances, abilities, or recruitment.

## Foundation versus faction work

Book IV does not declare any specific modded faction or god optimal. It supplies the method used later:

1. extract the final combined roster;
2. classify roles;
3. calculate effective combat lines;
4. build packages;
5. test scripts;
6. record match-ups and counters.

# Part XIX: Controlled-Test Programme

## Test standard

Every test record should include:

- Dominions version;
- exact mod list and load order;
- map and province;
- attacker and defender;
- unit IDs and quantities;
- commander statistics and orders;
- formations and positions;
- gems and items;
- weather, scales, dominion, terrain, and indoor state;
- random seed if available;
- number of repetitions;
- result distribution;
- replay or log notes.

Change one important variable at a time.

## Test 1: DRN tie direction

Purpose: verify tie behaviour in Attack, MR, and morale checks.

Method:

- create equal-value opposed cases;
- use the highest battle-log detail;
- record explicit equal totals;
- confirm which side wins each rule’s tie.

## Test 2: Harassment decay

Purpose: measure the hidden decay rate.

Method:

- expose one high-Defence unit to a known burst of harmless directed attacks;
- stop new attacks through controlled spacing;
- inspect Defence or logs over time;
- repeat across different initial penalties.
- compare the result with the historical Dominions 5 hypothesis of a 5% reduction every `16/375` of a round without assuming that value survived into Dominions 6.

## Test 3: Cooldown and combat speed

Purpose: distinguish movement time, recovery, and attack cadence.

Method:

- compare otherwise identical units with controlled Combat Speed;
- record timestamps for steps and attacks;
- repeat with diagonal movement and no movement.

## Test 4: Formation Fighter density

Purpose: document exact square capacity at several ability values and sizes.

Method:

- deploy uniform squads in each formation;
- count bodies per square;
- repeat with mixed sizes.

## Test 5: Repel sequence

Purpose: confirm current repel bonuses, lingering penalty, giant length, and magic-weapon interaction.

Method:

- use non-damaging or highly protected targets;
- vary weapon length, Attack, morale, size, and interval between attacks;
- record repel rolls at log level four.

## Test 6: Shield damage and repair

Purpose: verify current rounding and post-battle repair.

Method:

- strike known mundane and magical shields with controlled slash and blunt damage;
- record damaged and broken thresholds;
- vary available provincial resources;
- inspect the next turn.

## Test 7: Mounted targeting

Purpose: reproduce target weights for rider, mount, reach, missiles, and area effects.

Method:

- use fixed rider size and several mount sizes;
- count hundreds of directed attacks;
- repeat with different weapon lengths and missiles.

## Test 8: Trample fatigue

Purpose: measure current flying and trampling fatigue after the 6.25 correction.

Method:

- compare mounted and non-mounted tramplers;
- control Encumbrance, distance, number of victims, and resistance;
- record fatigue per displacement.

## Test 9: Morale survivor bonus

Purpose: derive the manual’s 0-5 survivor bonus.

Method:

- create squads at controlled original and remaining sizes;
- force identical checks;
- extract morale totals from detailed logs;
- test the current community hypothesis `round(5 x surviving proportion)` at every rounding boundary;
- test commanders separately from squads.

## Test 10: Army HP rout weights

Purpose: verify mounts, slaves, and PD weighting in mixed armies.

Method:

- construct armies with one weighted category at a time;
- cause controlled casualties;
- record the first 50% checks and 75% automatic rout.

## Test 11: Retreat intelligence

Purpose: confirm smart-retreat rates and priority.

Method:

- provide a fort, friendly province, and enemy province;
- repeat commander retreats in native and non-native terrain;
- separately test leaderless troops and undisciplined followers.

## Test 12: Ordinary fatigue recovery

Purpose: resolve active-unit recovery not fully specified by the manual.

Method:

- give controlled fatigue without further actions;
- compare active, unconscious, reinvigorated, and spellcasting units;
- log fatigue every round.
- test the current community hypothesis of one point per active round plus Reinvigoration against the official five-point unconscious recovery.

## Test 13: Regeneration and rounding

Purpose: reproduce the post-6.31 percentage rule.

Method:

- use several maximum HP values and regeneration percentages;
- inflict constant damage;
- record healing across many rounds.

## Test 14: False damage and rout

Purpose: verify current HP-rout contribution and dissipation.

Method:

- apply only false damage;
- kill all hostile Glamour mages at controlled times;
- record morale triggers and two-per-round removal.

## Test 15: Indoor battlefield magic

Purpose: catalogue which whole-field effects remain legal.

Method:

- attempt ordinary, holy, start-of-battle, innate, and item-created field effects in fort interiors and assassination maps;
- record script fallback and gem use.

## Test 16: Modded regression suite

Purpose: detect future DE or Divinitus changes that invalidate published packages.

Method:

- preserve a small set of representative battles;
- rerun after each mod update;
- compare unit IDs, final fields, scripts, and outcomes;
- classify differences as source edits, load-order overwrites, or engine changes.

# Part XX: Operational Checklists

## Pre-battle audit

### Objective

- What must the battle accomplish?
- Is taking the province enough?
- Which enemy assets matter most?
- What friendly losses are acceptable?

### Command

- Are all troop categories legally led?
- Are squad-count morale penalties understood?
- Is there useful command redundancy?
- Are key commanders protected?

### Formation

- Which squad contacts first?
- Is width, depth, or spacing appropriate?
- Are undisciplined restrictions active?
- Will friendly units obstruct one another?

### Script

- Are spells researched and gems carried?
- Are targets in range?
- What happens after five orders?
- What happens if the named spell fails?
- Are indoor, underwater, storm, or darkness restrictions checked?

### Defence layers

- What answers Protection?
- What answers Defence?
- What answers shields?
- What answers resistance and MR?
- What answers regeneration, size, flight, fear, or mindlessness?

### Persistence

- When does fatigue become dangerous?
- Can the line survive until the decisive turn?
- Are poison, bleeding, clouds, or rust cumulative threats?

### Preservation

- Where will the army retreat?
- Are routes friendly after simultaneous movement?
- Is the fort battle an annihilation risk?
- Can the force fight again next turn?

## Post-battle audit

1. What was the first irreversible failure?
2. Did placement produce the intended contact order?
3. Which scripts completed?
4. Which spells were interrupted or replaced by AI choices?
5. When did key units cross 50 or 100 fatigue?
6. Which squad routed first and why?
7. Did command loss trigger a general collapse?
8. Did the counter attack the correct defence layer?
9. Which losses occurred during retreat or from delayed damage?
10. What is the smallest change likely to improve the result?

## New-player minimum

Before ending a turn with an important army:

- assign every troop to a legal commander;
- separate units that need different orders;
- choose formations deliberately;
- protect commanders;
- check mage gems and scripts;
- inspect likely retreat provinces;
- view the replay even after an easy victory.

# Part XXI: Essays

## Essay I: Morale and the Shape of Defeat

Dominions gives armies bodies, weapons, armour, and magic, but it ends most battles through cohesion. This is not a cosmetic concession to realism. It is the mechanism that connects local violence to army-level outcomes.

A soldier’s HP asks whether the body can continue. Squad morale asks whether a group still accepts the battle. Command asks whether that group remains part of an army. Army HP asks whether the whole force has absorbed so much destruction that continued resistance is no longer possible. Retreat then asks whether defeat remains recoverable.

These layers explain why two identical casualty totals can have different results. Ten losses spread among several large, well-led squads may be tolerable. The same losses concentrated in a small forward squad can trigger a rout, expose a flank, and place fear next to another squad. The second squad then checks under worse conditions. Once movement turns away from the enemy, Defence falls, zones of control no longer matter, and the enemy converts retreat into further damage.

Morale has geometry. A fear aura beside one squad is not the same as a global numerical debuff. A standard supports a particular command structure. A commander killed behind the line can matter more than a warrior killed at the front. A sparse formation’s -1 seems modest until it moves an already marginal squad down the DRN curve.

The strategic conclusion is not as simple as “buy morale.” The army needs a controlled way to fail. Squads can be divided so that one rout stays local. Command can be duplicated. Valuable troops can be kept from taking the first casualty threshold. Fear can be attacked at its source. Retreat provinces can be preserved so a rout displaces the army instead of destroying it.

The strongest armies are not those that never fail a morale check. Random rolls and extreme effects make that impossible. They are armies whose first failure does not automatically become total defeat.

## Essay II: Fatigue, the Hidden Battle Economy

Gold buys the unit and resources equip it, but fatigue determines how long the purchased statistics remain real.

A fresh high-Defence unit can look nearly untouchable. Every ten fatigue removes one Defence. Directed attacks add harassment. At fifty fatigue, the same body suffers five less Defence and a broader range of armour-defeating protection results. At one hundred it falls unconscious. The transition is not gradual in battlefield effect: a stable formation can appear to hold, then collapse rapidly as many members cross the same thresholds.

Fatigue also binds ordinary troops and mages into one system. Heavy armour protects a caster from arrows but charges twice its armour Encumbrance on every spell. A trampler destroys light infantry but pays for movement and trampling. A berserker produces more offence but continues accumulating cost. Fire, cold, shock, bleeding, and spell effects can attack the fatigue stock even when direct HP damage is unimpressive.

This makes time a resource. A cheap screen may buy three rounds for buffs, or force the enemy to spend three rounds attacking and building Encumbrance fatigue. A resistant line does not need an immediate kill if every exchange makes the next one more favourable. Reinvigoration does more than extend endurance; it preserves Attack, Defence, casting, and the reliability of protection.

A proper comparison between two units includes their fatigue over time. “Who wins the first attack?” is often less important than “Who still has a functioning stat line on the tenth?”

## Essay III: Formation Is the Management of Time

Formation appears spatial, but its principal strategic effect is temporal. It decides how many bodies enter contact now, how many wait, which square receives area damage, how long replacements take to arrive, and when a fast unit becomes trapped behind a slow one.

A line spends frontage early. It seeks simultaneous contact and converts many weapons into immediate checks. A box stores bodies behind the first rank. It may accept less initial damage output in exchange for depth and protection of the centre. A sparse line spreads risk and coverage but pays morale and density costs. A skirmish pattern gives each square room yet can allow enemies to penetrate or surround.

Placement adds another time instruction. Forward deployment advances the squad’s personal clock. Hold adds two rounds. Combat speed changes travel and cooldown. The enemy’s placement changes the actual meeting point. The resulting schedule determines whether a buff precedes contact, whether arrows receive three volleys or one, and whether a finisher arrives against fresh or fatigued targets.

This is why copying a formation without copying its purpose fails. “Put infantry in a line” is not a rule. A line is correct when early frontage is worth more than depth and clustering risk. “Put mages at the rear” is incomplete. The rear can be exposed to flyers, and excessive distance can place spells out of range.

Formation is best designed as a timeline: first contact, second contact, decisive effect, expected rout. The map is the clock face.

## Essay IV: Protection Is a Probability Distribution

Protection is often treated as subtraction: damage fifteen against protection twenty should do nothing. Dominions instead rolls both sides, permits open-ended results, distinguishes body and head, applies weapon types, includes shield hits, and allows low protection rolls to become armour defeating.

Protection changes the damage distribution. It reduces ordinary damage and makes severe results rarer, but it does not create a hard wall. The tail can still contain clean shield bypasses, head hits, high damage rolls, armour-piercing reductions, and armour defeat caused by fatigue.

This perspective improves both defence and offence. Adding protection to an already protected unit may still matter if it removes many ordinary wounds and their affliction chances. Against that unit, a large number of weak attacks may be poor at direct damage but valuable for harassment and fatigue. A smaller number of armour-negating attacks may attack the correct layer but fail if their delivery is unreliable.

The important question becomes: which part of the distribution must change? If ordinary hits are killing the line, more protection or shields may work. If rare head hits kill expensive sacreds, helmet coverage, Luck, body count, or regeneration may matter. If fatigue is widening the armour-defeating tail, reinvigoration may preserve effective protection better than another armour point.

The defence layer is never just the number printed beside the shield icon.

## Essay V: Scripting under Uncertainty

A Dominions script is neither direct control nor a prophecy. It is a commitment made before seeing exact enemy deployment and resolved through range, targets, pathing, fatigue, damage, and AI fallback.

This makes scripting a form of robust planning. A brittle script succeeds brilliantly in one anticipated battle and fails when the enemy deploys one formation-width away. A robust script may sacrifice theoretical perfection to retain useful behaviour across several plausible enemy plans.

Robustness begins with dependencies. If spell four requires spell one to boost a path, the caster must survive the preparation time, spend the correct fatigue, and still have a legal target. If a screen must hold for three rounds, its morale and matchup must support that duration. If a flier must kill commanders, the path must remain open and the flier must ignore irrelevant rear targets.

Failure branches should be written deliberately. When the target is absent, what will the AI cast? When the caster is interrupted, does the army still have resistance? When the enemy holds, do friendly damage spells fire into empty space or remain useful? After five orders, does the mage stay safe?

The ideal script is not the one with the most exact sequence. It is the one whose likely deviations remain acceptable.

## Essay VI: Winning the Battle, Saving the Army

Field victory is one event in a campaign. The surviving commanders, mages, mounts, gems, afflictions, and retreat routes determine whether the event creates lasting advantage.

An army that wins with its commanders dead can become stranded or badly organised. A force that routs into friendly territory may remain a strategic asset. A cavalry army can retain riders while losing mounts and tempo. Poison and bleeding can kill units after their visible escape. A failed fort defence can annihilate every unit that had nowhere to retreat.

Preservation begins before battle. Friendly adjacent provinces are part of army design. Command redundancy protects against battlefield collapse and the reorganisation that follows. Gem expenditure should reflect the value at risk. A commander carrying a laboratory’s worth of gems is a caster and a moving treasury.

There are moments when preservation should be sacrificed. Destroying a unique enemy global caster, breaking a throne defence, or exhausting the only relief army may justify severe losses. The decision should be explicit. “The replay said victory” is not a strategic valuation.

The useful post-battle question is: how much future action did this result purchase? Provinces, siege turns, mage survival, research continuity, and readiness belong in the answer.

## Essay VII: Combined Arms as Counter Architecture

Combined arms is sometimes described as variety for its own sake. In Dominions it is better understood as a set of linked answers to layered defences.

A conventional line may hold space but fail against heavy armour. Mages may negate armour but require time and protection. Archers may interrupt the enemy’s mages but fail against shields. Flyers may threaten command but need the centre fixed in place. Fear may rout ordinary troops but do little to mindless bodies. Each component covers a failure mode of another.

Combined arms works when every component follows the same timing plan. A screen that dies before the debuff resolves has not supported the mage. A flanker that arrives before the centre engages can be surrounded. An armour-breaking effect cast after the damage line routs is irrelevant.

Combined arms also imposes organisational costs: more commander types, more scripts, more recruitment gates, more research branches, and more ways to misdeploy. Variety becomes strength only when every component has a named job and a dependency it satisfies.

The aim is not maximum variety. We want the smallest useful combination: enough distinct mechanisms to answer the expected defences, all delivered on one coherent clock.

# Sources and Open Questions

## Principal sources

- Illwinter, *Dominions 6 Manual*, revision 2, especially the statistics, special abilities, Army Setup, Combat, afflictions, sieges, retreats, and Battle Magic sections.
- Illwinter, *Dominions 6 Modding Manual*, version 6.34.
- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html).
- [Illwinter Dominions 6 changes](https://www.illwinter.com/dom6/changes.html).
- [Dominions 6 official Steam page](https://store.steampowered.com/app/2511500/Dominions_6__Rise_of_the_Pantokrator/).
- Supplied `DomEnhanced2_16.dm`.
- Supplied `Divinitus_1.15.3_DE.dm`.

Current community references are used to identify test questions and terminology, not to override the manual or current official corrections without evidence.

## Open questions

The following still require controlled current-game tests:

- exact harassment decay;
- complete cooldown constants;
- Formation Fighter capacity at every value and mixed size;
- current-version reproduction of the survivor-bonus rounding boundaries and commander handling;
- frame-by-frame current-version confirmation of active-unit fatigue recovery outside the manual's explicit unconscious rule;
- some obstacle and targeting weights;
- full mounted carry and movement arithmetic;
- precise current rounding in shield damage, regeneration, paralysis, and several special effects;
- effective combined data for every DE and Divinitus object.

Until then, they remain research tasks rather than confident approximations.
