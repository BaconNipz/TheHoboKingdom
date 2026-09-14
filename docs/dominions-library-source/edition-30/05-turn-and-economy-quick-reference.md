# Turn and Economy Quick Reference

## Scope and use

This is the library's field sheet: the small amount of deliberate repetition kept beside the turn screen. Foundation Book I owns hosting order and Foundation Book II owns the economic rules. The sheet simply keeps their most-used facts in one place while answering four immediate questions:

1. What resolves first?
2. What limits recruitment here?
3. What will this province actually produce?
4. What state change will matter this month rather than next month?

**Ruleset:** Unmodded Dominions 6.36 unless a modded note is explicitly shown.  
**Primary source:** Dominions 6 Manual, revision 2.  
**Verification date:** 25 August 2026.  
**Evidence rule:** A dagger symbol is not used; uncertainties are written out beside the affected rule.

## The hosting spine

The official hosting sequence contains 63 steps. The following spine preserves the steps that most often decide an order-writing problem.

| Step | Resolution | Immediate consequence |
| ---: | --- | --- |
| 1 | Messages and attached resources | Transfers leave before almost every danger or ownership change. |
| 2 | Research | A researcher killed later still contributes this month. |
| 3 | Recruitment | New defenders exist before attacks and movement. |
| 4 | Empowerment | Permanent path increases are applied. |
| 5 | Forging | New items enter the national inventory but are not retroactively equipped. |
| 6-8 | Preaching, heretics, Throne claims | These religious actions precede battles and general dominion spread. |
| 10 | Rituals | Casters resolve in random order. |
| 11-12 | Remote attacks and magic battles | Magical attacks and movement can strike before conventional movement. |
| 14 | Site searches | Search orders finish before ordinary conquest. |
| 15-18 | Prophets, Call God, awakening, Blood Hunting | These resolve before assassinations and ordinary movement. |
| 20 | Assassinations | A killed commander may strand an army before movement. |
| 24-25 | Friendly movement, then other movement | Conventional movement is divided into two steps. |
| 26-27 | Movement battles, then castle storming | A relieving army can fight before a storm attempt. |
| 28-33 | Globals, events, effect battles, sneak discovery | Several late battle groups remain after movement. |
| 35 | Building construction and demolition | A new fort, temple, or lab is too late for this month's earlier actions. |
| 36 | Special-order allies | Reanimated or summoned allies created here are too late for this month's battles. |
| 37 | Pillage | Population and unrest damage precede income. |
| 38 | Income | Gold is collected after conquest and pillage, before upkeep. |
| 39 | Unrest alterations | Most ordinary unrest reduction is too late to improve this month's income. |
| 40 | Starvation | Armies fight before newly applied starvation. |
| 41 | Upkeep and desertion | This month's income is available before the charge. |
| 42-44 | Dominion spread, dominion effects, site effects | Ordinary dominion spread occurs after most battles and the economy. |
| 48 | Healing and disease | Battle survivors heal or suffer disease after the combat sequence. |
| 54 | Conscription | Automatic minimum PD is created for future turns. |
| 56-57 | Elimination, then victory | Both checks occur before immortals reform. |
| 60-63 | Immortals, unsupported PD, artifacts, cleanup | End-state maintenance prepares the next order phase. |

## Provincial gold

### Base and final income

```text
Base income = population / 100

Modified income =
  (population / 100)
  x dominion-scale modifiers
  x (1 + fort Administration / 200)

Final income =
  modified income / (1 + unrest x 0.02)
```

The number displayed by the province interface is already modified. Exact intermediate rounding is an implementation detail and should not be reconstructed from the final number when a one-gold difference matters.

### Tax trace

A province produces no income for the turn if it cannot trace an unbroken line of friendly provinces to a friendly fort. In disciple games, allied territory can carry the trace.

This is a collection rule, not a resource rule. A cut tax line can remove gold income without removing the province's local resources, recruitment capacity, or supplies.

### Unrest multipliers

| Unrest | Income retained | Resources retained |
| ---: | ---: | ---: |
| 0 | 100% | 100% |
| 10 | about 83% | about 91% |
| 25 | about 67% | 80% |
| 50 | 50% | about 67% |
| 75 | 40% | about 57% |
| 100 | about 33% | 50% |
| 150 | 25% | 40% |
| 200 | 20% | about 33% |

At unrest 100 or greater, ordinary unit and commander recruitment is prohibited.

## Provincial resources

An unfortified province makes only half of its potential resource value available for local recruitment. A fortified province uses its full local potential and may draw a percentage of the potential resources of eligible adjacent provinces.

```text
Final local resource pool =
  calculated resources / (1 + unrest x 0.01)
```

Fort resource draw is governed by Administration:

- a fort draws its Administration percentage from each eligible adjacent province's potential resources;
- land forts do not draw from sea provinces, and sea forts do not draw from land;
- a fort does not draw from an adjacent province containing another fort;
- a fort does not draw from an enemy-held province;
- two forts may draw from the same third province when that third province is adjacent to both and contains no fort.

Resources are local and do not accumulate. Unused resources vanish at hosting rather than moving to the treasury.

## Recruitment capacity

### Recruitment Points

Start with 20 Recruitment Points, then add the contribution from each population band reached.

| Population band | Contribution from that band |
| ---: | ---: |
| Base | 20 |
| First 5,000 | population in band / 100 |
| 5,001-10,000 | population in band / 200 |
| 10,001-20,000 | population in band / 300 |
| 20,001-40,000 | population in band / 400 |
| Above 40,000 | population in band / 500 |

Example for 6,000 population:

```text
20 + 5,000/100 + 1,000/200 = 75 Recruitment Points
```

The fort's recruitment bonus is applied afterward. Order or Turmoil changes Recruitment Points by 10% per scale step. Exact fractional rounding remains assigned to controlled testing.

### The four recruitment gates

| Gate | What it limits | Common misunderstanding |
| --- | --- | --- |
| Gold | Units, commanders, buildings, PD, and upkeep | A rich treasury does not create more local resources or points. |
| Resources | Equipment-heavy troops in that province | Resources do not transfer or stockpile. |
| Recruitment Points | Ordinary troop throughput | Cheap, lightly equipped units can still exhaust local organisation. |
| Commander Points | Commander throughput | Extra gold and resources do not bypass the local commander rate. |

Sacred recruitment adds a fifth gate: Holy Points. Limited recruits may add a sixth: a unit-specific cap.

### Commander Point ladder

```text
ordinary Commander Points = 1 base + current fort bonus
```

| Location | Total CP |
| --- | ---: |
| Unfortified province or Palisades | 1 |
| Fortress or Castle | 2 |
| Citadel or Grand Citadel | 3 |

Multi-point commanders accumulate progress over more than one month when the local pool is too small. `#slowrec` changes the commander's cost rather than increasing or decreasing the province pool. AI difficulty bonuses do not modify Commander Points or Holy Points.

### Queue behaviour

- Gold must be available when the order is placed.
- A shortage of resources or Recruitment Points can leave units queued for a later month.
- Sacred units can remain queued behind the Holy Point limit.
- A province can hold at most 250 queued units.
- Commander recruitment uses Commander Points; some commanders cost more than one point.
- Recruitment occurs at hosting step 3. A unit appearing then can defend that month but cannot receive a new strategic order until the next order phase.

## Upkeep

The manual's ordinary monthly rule is:

```text
ordinary gold-recruited unit upkeep = gold cost / 15
sacred or slave upkeep = gold cost / 30
```

Most summoned units have no upkeep. Exceptions can be assigned additional upkeep. The in-game unit panel commonly presents annual upkeep, equal to twelve monthly charges.

Versioned 6.33 observations establish that Sacred and Slave reductions stack, producing gold cost divided by 60, and that mounted upkeep uses separate rider and mount bases. Patch review through 6.36 finds no later general change. These rules are Community-tested rather than official manual wording. Shapechanged upkeep and fractional monthly aggregation remain unresolved.

Observed annual entries for 7- and 16-gold ordinary units are 6 and 13. Those samples exclude simply flooring the final annual decimal, but do not establish how monthly fractions reach the treasury. Use the Income Overview when the margin is one gold.

Upkeep resolves at step 41, after income at step 38. A nation can spend down to a narrow treasury during the order phase and rely on that month's income for upkeep. Any interruption to income can turn that small margin into desertion.

## Supplies and starvation

### Population supply

| Population band | Base supply |
| ---: | ---: |
| First 15,000 | 1 supply per 30 population |
| Above 15,000 | 1 supply per 60 population |

Growth or Death modifies this value first. Heat or Cold modifies it second.

### Fort supply projection

```text
Supply from a fort =
  (Administration x 6) / (distance + 1)
```

The maximum distance is four provinces. Where several forts are in range, only the highest fort contribution is used.

The manual's printed multiplier table and one worked example instead follow `(Administration x 4)/(distance + 1)`. Another official adjacent-province example agrees with the multiplier of six. The current community reference follows six, but distance scaling remains scheduled for a versioned test.

### Supply usage

- Size 0 uses no supply.
- Size 1 and Size 2 use one-half supply.
- Larger units normally use Size minus 2.
- Animals use half the ordinary amount.
- A mounted unit consumes supply for both rider and mount.
- Nature magic indirectly contributes 10 supply per path level.
- Update 6.35 fixed stale Supply Usage after magic-item changes; recheck the displayed total after changing relevant equipment.

### Starvation

When usage exceeds available supplies, units whose combined usage is approximately the deficit are selected to starve.

| State | Effect |
| --- | --- |
| First month selected | Starving condition, -4 morale, 5% disease chance |
| Selected while already starving | 50% disease chance |
| Appropriate survival skill | 50% chance to avoid starvation; a further 50% chance to avoid disease |
| Supply restored | Starving ends; existing disease remains |

Starvation resolves at step 40, after battles. It usually becomes a problem for the next battle, although disease or an existing Starving condition may already be causing harm.

Need Not Eat is the explicit immunity tag. Official update 6.18 confirms that transformation into a non-eating form removes Starving. Supply consumption and starvation eligibility are distinct: some objects can consume supplies while remaining unable to starve. Commanders are commonly reported to receive feeding priority, but generic commander immunity is not established.

## Fortification table

Each cost and time is for that upgrade stage. Statistics replace the previous fort's values; they do not stack.

| Fort | Gold | Months | Admin | Commander Points | Recruitment bonus | Siege storage | Wall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Palisades | 1,000 | 5 | 15 | +0 | +50% | 150 | 200 |
| Fortress | 600 | 3 | 30 | +1 | +75% | 750 | 500 |
| Castle | 600 | 3 | 45 | +1 | +100% | 2,500 | 1,000 |
| Citadel | 600 | 3 | 60 | +2 | +125% | 7,500 | 1,500 |
| Grand Citadel | 1,000 | 5 | 70 | +2 | +150% | 10,000 | 2,000 |

The standard maximum is Fortress in the Early Age, Castle in the Middle Age, and Citadel in the Late Age. Primitive or advanced national fort access and the Mason ability can alter this.

## Buildings

| Building | Standard cost | Constructor | Principal functions |
| --- | ---: | --- | --- |
| Fort | Stage-specific | Any commander | Protection, resources, supply projection, income through Administration, recruitment bonuses |
| Temple | 600 gold | Sacred commander | Dominion spread, preaching bonus, Blood Sacrifice access where applicable |
| Laboratory | 600 gold | Mage | Research, rituals, national gem/item pool, site functions that require a lab |

Nation and terrain exceptions can change these costs.

Construction completes at hosting step 35. A lab finished this month cannot enable step-2 research, step-5 forging, or step-10 rituals during the same month. A temple finishes after preaching and Throne claims. A fort finishes after recruitment and all ordinary battles.

Any commander can demolish a fort or laboratory in one month. Temples cannot be demolished by order; an enemy temple is automatically destroyed when its province is conquered. A fort cannot be demolished while under siege.

## Siege calculation

```text
reduction strength = Strength squared
repair strength = Strength squared / 2
```

Modifiers:

- Flying doubles reduction or repair contribution.
- Mindless defenders contribute one-eighth of calculated repair.
- Animals contribute half repair.
- Undisciplined units contribute half repair.
- Only commanders and units assigned to Maintain Siege contribute.
- Castle Guards and Wall Defenders add repair strength.

The difference between total reduction and repair damages or restores the wall, never above its original integrity. A fort not under siege repairs fully. The defender sees exact wall integrity; an attacker normally receives only a descriptive estimate.

A storm order becomes available after the wall has reached zero and the next order phase opens. Storming resolves after conventional movement battles, so a relief force can defeat or weaken the besiegers before the gate battle.

### Supply inside a siege

```text
fort supply this siege month =
  Supply Storage / consecutive siege turn
```

A fort with 300 storage supplies 300, 150, 100, 75, and 60 during the first five consecutive siege months. This storage concerns units inside the besieged fort. Administration's supply projection is a different system.

## Province Defence

The first PD point is free. Buying each later point costs gold equal to the level being purchased.

```text
cumulative cost to PD n =
  n(n + 1)/2 - 1
```

| PD | Total gold | Notes |
| ---: | ---: | --- |
| 1 | 0 | First commander and troops |
| 6 | 20 | Cheap raid tax; roster quality still matters |
| 10 | 54 | Official additional-benefit threshold |
| 15 | 119 | Stealth detection begins |
| 20 | 209 | Additional troop and commander types |
| 25 | 324 | Patrol strength 11 |
| 30 | 464 | Expensive static commitment |
| 40 | 819 | Usually a specialised defence decision |
| 50 | 1,274 | Severe opportunity cost |
| 100 | 5,049 | Hard maximum |

Every full 10 PD reduces unrest by 1 each turn. Beginning at PD 15, patrol strength equals `PD - 14`; the manual's example gives PD 25 a patrol strength of 11.

PD costs no upkeep and fully returns after a battle if control is retained. It cannot be voluntarily reduced. It requires 10 population per point and is reduced at hosting step 61 when population cannot support it. Capture wipes existing PD. Relinquishing a province in a disciple game reduces it by 25%.

PD is a local delay mechanism and raid tax, not a mobile army. Its national roster, magic support, terrain, attacker's script, and retreat situation determine its actual combat value.

## Magic sites and gems

- Forests, wastes, deep seas, and several unusual terrains tend to have more sites; plains and farms tend to have fewer.
- Hidden sites have difficulty 1 through 4.
- A searching mage finds sites in a path up to that mage's path level.
- Path level 4 is the highest needed for ordinary manual searching.
- Path-search rituals reveal every site of their path in the target province.
- Acashic Knowledge reveals every magic site there.
- A site may provide gems, gold, recruits, entry orders, discounts, unrest, disease, or other effects.
- Harmful site effects can operate while the site is undiscovered.
- A captured national recruitment site may continue to yield gems without granting its former nation's special recruits.
- Some site recruitment requires a laboratory.

Search orders resolve at step 14. Site effects resolve at step 44. Discovery does not retroactively create earlier recruitment or ritual orders.

## Blood Hunting

For an ordinary hunter, the manual gives three checks:

```text
Blood success chance = 10% + 30% x Blood level
Population success chance = population / 75 percent
Unrest failure chance = unrest / 4 percent
```

If all checks succeed:

```text
slaves found = d6 + Blood level
unrest gained = d(slaves x 3 + 4)
```

If any check fails, no slaves are found and unrest rises by `d6 - 1`.

Population reaches a 100% nominal population check at 7,500. A Blood 3 hunter reaches a 100% nominal Blood check. Unrest can still cause failure. Site frequency changes the average yield by 0.5 slaves for every five percentage points away from 50%. Strong friendly dominion reduces the risk of hostile commoners attacking; the manual states that dominion 10 makes such resistance almost disappear.

Blood Hunting is not free gem generation. It converts mage-turns, population, patrol labour, gold income, and attention into slaves.

## Scale effects used in economic calculations

The current unmodded 6.36 baseline uses the following ordinary per-step effects. Growth and Death use the newer official Modding Manual default rather than the stale one-percent entry in the revision-2 main manual.

| Scale step | Income | Resources | Recruitment Points | Supplies | Population |
| --- | ---: | ---: | ---: | ---: | ---: |
| Order | +3% | +2% | +10% | - | - |
| Turmoil | -3% | -2% | -10% | - | - |
| Productivity | +3% | +15% | - | - | - |
| Sloth | -3% | -15% | - | - | - |
| Heat/Cold away from preference | -5% | - | - | -10% | - |
| Growth | +2% | - | - | +10% | +0.2% per month |
| Death | -2% | - | - | -10% | -0.2% per month |

Evidence boundary:

- Modding Manual 6.34 defines the unmodded `#deathincome` default as 2. No official announcement through 6.36 changes that general default. The current baseline uses 2% income per Growth/Death step; the revision-2 main-manual entry remains only as a documented older conflict.
- The revision-2 main manual gives Order/Turmoil resources as 2% per step, and no later official announcement changes it. Unsourced three-percent tables are not used as current evidence.

Exact integer rounding remains unresolved. A calculation near an integer boundary should still defer to the displayed in-game province value.

## Active mod economy deltas

The exact supplied files define the combined ruleset as Dominions Enhanced 2.16 loaded before Divinitus 1.15.3 DE.

Dominions Enhanced changes these global values:

| Global rule | Unmodded source value | DE 2.16 |
| --- | ---: | ---: |
| Order/Turmoil income per step | 3% | 4% |
| Productivity/Sloth income per step | 3% | 4% |
| Growth/Death income per step | 2% | 2% |
| Growth/Death population change per step | 0.2% | 0.25% |
| Fortune/Misfortune event frequency per step | 5% | 7% |

Divinitus does not redefine those five global commands, so its later load position does not reset them.

Both mods contain many object-, site-, event-, item-, unit-, and nation-specific economic effects. A global table cannot safely predict a specific nation until its roster and source overrides are examined.

## Order-writing audit

Before submission:

- Check the treasury after both recruitment and construction.
- Check projected upkeep against income, including isolated provinces.
- Scan local resources and Recruitment Points for greyed-out queues.
- Check Commander Points and Holy Points separately from troop capacity.
- Trace tax lines from vulnerable provinces to a friendly fort.
- Compare army Supply Usage against both the destination and every likely battle province.
- Inspect unrest in recruiting and income-critical provinces.
- Confirm that new infrastructure is not being treated as operational one step too early.
- Distinguish the province outside a fort from the fort interior.
- Confirm which siege commanders remain on Maintain Siege.
- Recalculate PD cost cumulatively rather than valuing only the next point.
- Check whether a site search, Blood Hunt, patrol, or research assignment consumes the mage-turn needed elsewhere.

After hosting:

- Read battle and event reports before changing queues.
- Check for recruitment that remained queued.
- Compare treasury income and upkeep totals.
- Inspect new unrest before projecting the next month's income.
- Check supply, Starving, disease, and attritions on every large army.
- Recheck tax traces and besieged forts.
- Record new sites and whether their benefits require a lab.
- Check wall condition from the correct side's available information.
- Confirm unsupported PD reductions in depopulated provinces.

## Source note and unresolved tests

**Official core:** Dominions 6 Manual, revision 2, especially pages 21-29, 51-57, and 71-72.  
**Global defaults:** Dominions 6 Modding Manual, version 6.34.  
**Mod values:** exact source of `DomEnhanced2_16.dm` and `Divinitus_1.15.3_DE.dm`.  
**Official plus current community evidence:** ordinary Commander Point base behaviour, sacred-and-slave upkeep stacking, and mounted upkeep decomposition.  
**Community details retained provisionally:** exact unrest reductions to Recruitment Points and Commander Points, and generic commander feeding priority.

Priority reproductions:

1. Recruitment Point rounding at population-band and scale boundaries.
2. Fort supply at distance zero through four.
3. Resource rounding and overlapping fort draw.
4. Shapechanged upkeep and fractional monthly aggregation.
5. Unrest effects on Recruitment Points and Commander Points.
6. Commander feeding priority and starvation eligibility.

Growth/Death income and Order/Turmoil resources are resolved at 2% per step, and the ordinary Commander Point ladder is closed. Future tests of those values are regression checks, not prerequisites for using the published baseline.
