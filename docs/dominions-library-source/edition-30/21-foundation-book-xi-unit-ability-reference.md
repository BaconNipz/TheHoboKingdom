# Foundation Book XI - Units, Abilities, Experience, and Conditions

## A Systematic Reference for Reading Every Unit

Baseline: Dominions 6.36; vanilla rules unless a ruleset is named; research edition 30 August 2026. Structured object examples remain pinned to the auditable 6.35 Inspector snapshot.

## 1. Purpose

A Dominions unit is not defined by its attack, defence, protection, and hit points alone. Its type determines who can command it, which spells can affect it, whether it consumes supplies, how it heals, what happens when leadership disappears, and sometimes whether it can cross a border at all. Its special abilities add another layer of exceptions. Experience changes the same body over time. Afflictions and other conditions may then change it again.

Book XI is where unit facts are looked up and interpreted. It should answer five questions quickly:

1. What kind of being is this?
2. What does this icon or named ability change?
3. Does the effect matter on the strategic map, in battle, or both?
4. What normally counters, suppresses, or invalidates it?
5. How certain is the explanation under the current version?

The official manual says that Dominions contains roughly five hundred special abilities and explains only a selection. The Modding Manual exposes a wider technical vocabulary, but a mod command is not always a complete player-facing specification. The unit window remains the final current description of a particular unit, while patch notes can supersede older manual language.

It combines three kinds of reference:

- interpretive chapters that explain families of abilities and the questions they raise;
- compact records for the most consequential classes, abilities, and conditions;
- an evidence boundary that keeps official statements, current corrections, derived implications, and community reverse engineering visibly separate.

[Book IV](#b4-foundation-book-iv-armies-and-battle) remains the authority for combat arithmetic, battle order, morale resolution, fatigue, damage, affliction chance, and counter construction. Book XI explains what a label means and where its consequences appear. It links to Book IV when a full resolution procedure would otherwise be repeated.

## 2. Evidence Key and Version Discipline

| Code | Meaning in this volume | Proper use |
| --- | --- | --- |
| OM | Official main manual, revision 2 | Stated rules, definitions, thresholds, and broad exceptions |
| MM | Official Modding Manual, version 6.36 | Engine-facing ability names, parameters, categories, and technical relationships |
| OP | Official patch announcement through 6.36 | Current changes that correct or supersede older behaviour |
| UI | Current in-game unit or ability description | The live description for a particular object; not independently captured for every record here |
| CT | Community-tested or reverse-engineered | Useful evidence that is not an official specification and may be version-sensitive |
| D | Derived | A stated consequence derived from confirmed inputs |
| TP | Test pending | A disputed, hidden, or version-sensitive detail that still lacks reliable current confirmation |

An evidence label applies to the defined fact, not to every possible consequence. For example, the official manual defines Ethereal as causing three quarters of nonmagical strikes to miss. The recommendation to use inexpensive magical weapons against an ethereal raider is doctrine derived from that fact, not an additional official rule.

The public baseline is Dominions 6.36, released on 17 August 2026 UTC. The main manual is older than several current changes. Notable ability-facing corrections include exact percentage regeneration in 6.31; Spiritform protection from bleeding, frozen, and burning conditions in 6.30; Disease Resistance applying to disease spells in 6.27; restored script continuity for innate spellcasters after temporary unconsciousness in 6.35; and corrected swimming-mount river crossing, charm allegiance, and mounted recruitment state in 6.36. These corrections are integrated where relevant and retained in the version notes near the end.

The live Modding Manual now identifies itself as version 6.36. Book XI uses that current file for ability semantics. Book XIV's larger command-locator export remains tied to its declared 6.34 extraction until the whole token and page-locator set is rebuilt; that older extraction is not used to settle the perception rules below.

# Part I: How to Read an Ability

## 3. Begin with the Body, Not the Icon

The fastest reliable reading order is:

`body and type -> leadership requirement -> movement environment -> defences and recovery -> offence and auras -> conditional modifiers -> experience and conditions`

This order prevents a common failure. An impressive offensive ability can draw attention away from the fact that its unit cannot be led by the available commander, cannot enter the intended terrain, dissolves without leadership, or cannot recover from the damage expected along the route.

The body layer includes size, living or nonliving status, unit classes, shape, mount, and environments in which the unit can exist. The command layer determines whether the unit can join the proposed army at all. The recovery layer determines whether a favourable exchange can be repeated. Only then should an ability's immediate battle output dominate evaluation.

### 3.1 A seven-question unit audit

For an unfamiliar unit, record:

| Question | What to inspect | Why it changes the decision |
| --- | --- | --- |
| What is it? | All type tags, body, shape, size, mount | Targeting, leadership, healing, supplies, and immunity can follow from class. |
| Who can command it? | Normal, magic, and undead leadership; special squad limits | A legal recruitment or summon can still create an unusable army. |
| Where can it go? | Water status, flight, floating, survival, sailing, teleport restrictions | Strategic reach and retreat routes can matter more than raw statistics. |
| How does it stay functional? | Regeneration family, recuperation, immortality, disease and age | Recovery determines repeatable force, not merely survival in one battle. |
| What changes contact? | Awe, fear, auras, shields, stealth, vision, trample, swallow | These effects alter who can engage and what happens before ordinary damage decides the exchange. |
| When are the numbers conditional? | Seasonal, scale, dominion, darkness, storm, and shape modifiers | A unit card seen in one province may not describe the intended battlefield. |
| What has changed since recruitment? | Experience, heroic abilities, afflictions, curse, horror mark, disease, items | Two units with the same name can have materially different current value. |

## 4. Tags, Values, and Descriptions

Some abilities are binary: a unit is Aquatic or it is not. Others carry a value. The meaning of that value is ability-specific. It may represent points, a percentage, an area, a bonus, capacity, range, number of creatures, or a threshold modifier. A value of 5 on Fear is not interpreted in the same way as 5 on Regeneration, Reinvigoration, Standard, or Sailing.

Three checks are mandatory:

- read the ability's own description rather than inferring a universal scale;
- distinguish a displayed total from an innate contribution or item contribution;
- verify whether the number is applied directly, converted by a formula, or used to choose a tier.

The Modding Manual is particularly useful for discovering whether an ability has a parameter, but its command value may be transformed before it reaches the unit card. Player-facing records should preserve the displayed meaning where verified and avoid pretending that every mod parameter is the final battle number.

## 5. Innate, Granted, Shape-Bound, and Contextual Effects

An ability may come from the unit's base form, a mount, an item, a bless, a spell, a heroic trait, a province, dominion, a season, or a temporary battle effect. These sources do not have identical lifetimes.

| Source | Persistence question | Typical trap |
| --- | --- | --- |
| Base form | Does shapechanging replace the form? | Assuming a tag survives every alternate shape. |
| Mount | Does dismounting or mount death remove it? | Reading the combined card as one indivisible creature. |
| Item | Is the effect active only while equipped, and is the item cursed? | Treating an item-caused affliction as healable while its cause remains. |
| Bless | Is the unit sacred and currently blessed; is the effect Incarnate? | Pricing a sacred as if every battle begins blessed. |
| Spell | What is the duration and can it be resisted, dispelled, or interrupted? | Confusing a scripted plan with a permanent statistic. |
| Heroic ability | Is the commander still in the Hall of Fame, and how has the value grown? | Treating a community-derived formula as an official guarantee. |
| Environment | Which scale, season, dominion, terrain, light, storm, or plane is checked? | Testing in favourable conditions and deploying elsewhere. |

Shape changes deserve special care. A unit name may remain familiar while weapons, armour, size, hit points, movement, leadership, magic, or type tags change. When a strategy depends on an ability, verify the form that will actually be present at the relevant hosting step and battle round.

## 6. Stacking, Precedence, and the Best-Only Rule

There is no single universal stacking law. Effects fall into several patterns:

- **best only:** the official manual states that only the best Standard in a squad applies;
- **additive or cumulative:** experience gains build across thresholds, and horror marks can deepen through repeated marking;
- **source-limited:** an item or form may supply the effect only while that source remains;
- **mutually exclusive state:** a unit cannot simultaneously be asleep and acting normally, or mounted and voluntarily dismounted in the same form;
- **layered defence:** multiple defences may apply at different resolution steps rather than adding into one value;
- **unknown or object-specific:** the interface or a controlled test is required.

When a stacking rule is not explicit, the safe record is not “stacks” or “does not stack.” The safe record is “stacking unverified.” This matters because many expensive designs fail not from weak ingredients but from buying the same non-stacking benefit twice.

### 6.1 Confirmed Current Cases

Source type does not determine stacking by itself. A form, item, bless, or spell supplies an effect, but the receiving effect's own rule decides whether values add, compete, replace one another, or resolve as separate layers.

| Effect or family | Current rule | Evidence | Planning consequence |
| --- | --- | --- | --- |
| Standard | Multiple standards in one squad do not stack; only the highest value counts | MM 6.36, `#standard` | A second lower Standard in the same squad adds no morale bonus |
| Inspiring Researcher | Only the highest value in a province counts | MM 6.36, `#inspiringres` | Several copies improve coverage or redundancy, not the province bonus |
| Blur, Displacement, and Invisibility | Displacement does not stack with Blur or Invisibility | UI description in the pinned 6.35 Inspector snapshot; no 6.36 patch changes this family | Do not budget for additive melee Attack penalties from these states |
| Experience thresholds | Earned bonuses accumulate at the published star thresholds | OM plus the official 6.13 and 6.14 corrections | Later stars retain earlier threshold gains |
| Horror Mark | Repeated marking can deepen the same condition | OM | Treat severity as cumulative state, not duplicate independent icons |
| Different defence families | Each defence keeps its own resolution step unless an explicit rule merges or replaces it | OM and D | Protection, resistance, miss chance, morale gates, and recovery are not one additive statistic |

This closes the assumption that all same-named benefits stack merely because they come from different sources. It does not establish a global item-versus-bless-versus-spell precedence rule. Unlisted abilities remain ability-specific, and form or source loss still requires a separate lifetime check.

## 7. Counters Are Usually Gate Removal

An ability creates value by imposing a gate. Ethereal asks for magical attacks. Awe asks attackers to pass a morale check. Regeneration asks for enough damage, disablement, or attrition to overcome recovery. Flying asks for protection of vulnerable rear areas and attention to storm interaction. Stealth asks for patrol coverage and information discipline.

The cleanest counter normally removes the gate at an acceptable cost. It does not need to destroy the target in isolation. A counter record should identify:

1. the gate the ability imposes;
2. the cheapest broad class of answer;
3. the conditions that make that answer unreliable;
4. the operational cost of delivering it.

This is why Book XI does not assign a universal power score. An ability's value is the price of the question it asks in the position where it appears.

# Part II: Unit Classes and Status Tags

## 8. Classes Can Overlap

Dominions uses overlapping tags rather than one exclusive biological taxonomy. A being can be both Undead and Magic Being, Demon and Magic Being, Animal and Sacred, or Inanimate and Mindless. Each relevant tag can alter leadership, spell targeting, supplies, morale, healing, or special interactions.

The official manuals explicitly resolve one important overlap: a unit that is both Undead and Magic Being, or Demon and Magic Being, requires undead leadership rather than magic leadership. More generally, a tag should not be erased merely because another tag seems more descriptive. The correct question is what each tag contributes.

## 9. The Ordinary Living Baseline

An ordinary living unit without a special command tag can be led by normal leadership. It consumes supplies according to size, can suffer disease and ordinary afflictions, and can normally benefit from living regeneration and appropriate healing. This baseline is not itself an icon; it is the background against which exceptional types are read.

The absence of a tag is still information. A human soldier lacking Spiritform, Inanimate, Undead, Demon, Animal, Mindless, or Magic Being avoids the special command burdens and immunities attached to those tags. Ordinary does not mean weak. It often means logistically compatible.

## 10. Animal

Animals can be led by normal commanders. They use half as many supplies as a humanoid of the same size. The manual states that animals without arms contribute only half their normal value to siege and fort defence; monkeys are the named exception to the armless-animal reduction.

Animal is also a targeting class. Animal-affecting magic and Animal Awe can distinguish it from an ordinary soldier. Beast Mastery or Beast Master leadership can improve the practical command of animal-heavy forces, but the exact benefit belongs to the displayed leadership effect rather than to the Animal tag itself.

Operational reading:

- reduced supply use supports large formations and long routes;
- weak siege contribution can make a victorious animal army poor at converting a field win into a fort;
- animal-specific control and fear effects can create sharp counters;
- normal leadership makes integration easier than for undead or magical beings.

## 11. Magic Being

Magic Beings require magic leadership. Without suitable leadership they rout, and the manual describes leaderless magical beings as dissolving on the battlefield. The tag also makes them valid or invalid targets for effects that distinguish magical beings.

Magic leadership is not ordinary leadership with a different colour. A commander may have ample normal capacity and still be unable to command one magic being. Path-based indirect bonuses can grant magic leadership, especially through Earth and Blood, but the displayed value should be checked before assigning squads.

When a magic-being army is evaluated, include command redundancy. A force whose only magic leader can be assassinated, swallowed, routed, or killed may collapse even while most bodies remain intact.

## 12. Mindless

Mindless units have morale 50 and do not rout while a suitable commander controls them. Without that control they dissolve on the battlefield. They cannot share a squad with non-mindless units. The tag also produces numerous immunities or targeting exclusions because the unit has no ordinary mind.

Mindless does not mean independent. It means exceptionally stable under command and exceptionally fragile when command is lost. The army exchanges ordinary squad morale problems for a leadership problem.

Important consequences:

- mind-affecting effects often fail or treat them differently;
- the squad cannot be padded with ordinary troops;
- leader protection is part of the unit's effective defence;
- their morale value should not be read as a promise that the army survives army-wide rout or loss of control under every circumstance; [Book IV](#b4-mindless-troops) owns battle-wide resolution.

## 13. Undead

Undead units require undead leadership and are subject to banishment. They are immune to disease and ordinary affliction-healing effects, and they rout if suitable leadership is absent. Mixing living and undead troops in the same squad causes a morale penalty according to the official manual.

Undead is both a logistical advantage and a recovery constraint. Many undead do not need to eat, but the exact supply property should still be read separately. Their immunity to ordinary disease prevents one attrition channel, while their inability to use ordinary healing makes battle damage and accumulated afflictions harder to repair. Corporeal undead can have special exceptions such as a Corpse Stitcher.

The class attracts dedicated counters: banishment, anti-undead weapons, and effects restricted to undead. The existence of a counter is not the same as its availability. An undead army can be oppressive when the opponent cannot deliver sufficient priests or specialised damage in the relevant theatre.

## 14. Demon

Demons require undead leadership, are subject to banishment, and are immune to disease. They are not undead under another name. Demon and Undead are distinct tags with different targeting lists, national interactions, and spell families, even though their command requirement overlaps.

Many demons also possess Need Not Eat, elemental resistances, fear, flight, dark power, or spirit sight, but none of those should be inferred from Demon alone. The correct record lists each separately.

## 15. Inanimate and Lifeless

The main manual describes Lifeless beings as immune to disease, ordinary regeneration, life drain, and ordinary affliction healing. The Modding Manual exposes Inanimate as the technical creature-status command used for bodies such as constructs. In player-facing analysis, the displayed class and its actual immunities should be recorded rather than assuming every stony or mechanical-looking body behaves identically.

Ordinary regeneration does not repair inanimate bodies. Reconstruction is the corresponding regeneration family for inanimate units. A powerful construct with no Reconstruction or specialised repair may survive a battle yet lose long-term value through unhealed afflictions.

Life-drain immunity has two sides: the target avoids the ordinary effect, but an attacker that relies on draining to recover receives no normal healing from the lifeless victim. This can reverse a matchup that appears favourable from weapon damage alone.

## 16. Spiritform

Spiritform beings are immune to transformation, disease, and ordinary affliction healing. Current 6.30 patch notes also state that Spiritform, like non-ethereal protection in that change, prevents bleeding, frozen, and burning conditions. Spiritform is not synonymous with Ethereal. A unit can possess one without the other, and each must be read independently.

Spiritform affects both target eligibility and recovery. It can shut down several condition-based plans while leaving magical damage, specialised spirit effects, or ordinary attrition available. Check the exact spell or weapon; “ghost” is not a complete rules category.

## 17. Plant, Stone Being, Illusion, Horror, and Divine Status

Several further tags primarily matter through targeting and exceptions.

### 17.1 Plant

Plant marks a plant-type being. It can change eligibility for plant-specific spells and effects. It does not by itself state every resistance, supply rule, or mind status; a vine creature may also be Mindless or Magic Being, but those are separate facts.

### 17.2 Stone Being

Stone Being identifies creatures that interact with stone-specific effects. It should not be used as a shorthand for Inanimate unless both are displayed or confirmed. Material appearance is not a reliable substitute for tags.

### 17.3 Illusion

Illusion marks an illusory being. The 6.36 Modding Manual defines it as a Spiritform-like technical class whose members can still be affected by illusion magic even when Mindless. The tag is distinct from Glamour, Invisibility, Unseen, and Ethereal. Glamour creates strategic concealment and a mirror-image defence; Illusion classifies the creature.

### 17.4 Horror

Lesser Horror, Greater Horror, and Doom Horror identify horror classes. They influence horror-related targeting and behaviour. Horror Mark does not turn its bearer into a Horror; it makes the bearer a preferred future victim of horror attacks.

### 17.5 Sacred, Holy, Divine Being, Pretender, and Prophet

Sacred determines eligibility for blessing and Holy recruitment limits. Holy levels belong to priestly or divine capability. Divine Being, Pretender, and Prophet carry further rules and targeting consequences. These terms overlap but are not interchangeable. A sacred troop is not automatically a priest; a priest is not automatically sacred; and a Pretender's divine continuity belongs to [Book III](#b3-part-viii-death-of-a-god).

## 18. Cold Blood, Blindness, Sex, and Other Body Tags

Cold Blooded creatures suffer additional fatigue in cold environments. Blind units depend on special senses or effects that do not require ordinary sight. Sex and body-form tags can affect seduction, transformation, item eligibility, and events. Polyimmune bodies resist transformations that would otherwise replace their shape.

These tags are easy to dismiss because they do not always add a visible combat number. They frequently become decisive only when another system asks a categorical question. A sound database retains them even when a current strategy does not use them.

# Part III: Movement, Terrain, Water, and Position

## 19. Water Status Is a Permission System

The water tags answer different questions:

| Tag | Core permission | Principal caution |
| --- | --- | --- |
| Aquatic | Lives and operates underwater | Ordinarily cannot operate on land without a separate exception or form. |
| Amphibian | Operates on land and underwater | Underwater performance may still be altered by weapons, spells, mounts, or other tags. |
| Poor Amphibian | Can cross the land-water boundary with penalties | Treat the penalty as part of the unit, not a cosmetic label. |
| Swimming | Can move through water under its defined rules | Does not automatically grant every underwater combat permission. |
| Gift of Water | Can support or convey water access according to its value | Capacity and persistence must be checked. |

Water access is not one binary “amphibious” property. An army's legal route depends on the commander, every unit, mounts, items, spells, and available capacity. Book VI owns the operational route and interception problem; Book XI identifies the permissions that must be present.

## 20. Flying, Floating, and Storms

Flying changes strategic movement and battlefield contact. It can bypass many terrain constraints, reach rear areas quickly, and alter which opponents can intercept or screen. It does not make a unit immune to storms. Storm Immunity is a separate ability.

Floating is also distinct. A floating body may pass certain terrain or battlefield obstacles and may interact differently with mounts and current patch rules. It should not be read as full flight.

Current practice requires four checks:

1. Can the commander use the movement mode?
2. Can every assigned unit and mount accompany it?
3. Does a storm or other environmental effect suppress the mode?
4. Where can the force retreat if the destination battle is lost?

## 21. Terrain Survival and Snow Movement

Forest, mountain, swamp, and wasteland survival reduce the strategic burden of their matching terrain and can affect which movement routes are legal or efficient. Snow movement supports travel in snowy conditions. These tags are most valuable as an army-level property: one incompatible unit can constrain a formation that is otherwise highly mobile.

Terrain survival does not mean immunity to every environmental effect in that terrain. It is a movement and survival permission with a specific engine meaning, not a general declaration that the unit is “at home” there.

## 21A. Riders and mounts are linked records

A mounted unit combines a rider record with a mount record. The two components can carry different movement, sacred, shape, and condition data; the combined unit card should not be treated as proof that every property belongs to both. Version 6.36 establishes three current boundaries:

- a swimming mount is sufficient for the mounted unit to cross rivers;
- when a knight is charmed in the corrected tavern encounter, the mount changes side as well;
- removing a repeated mounted-commander recruitment from the queue no longer incurs the corrected gold charge.

These are specific movement, allegiance, and queue rules. They do not establish a universal rule that every blessing, item effect, affliction, experience value, or transformed state automatically transfers between rider and mount. Book III owns blessing eligibility; the unresolved lifetime sequence remains R-052.

## 22. Sailing

Sailing lets a commander carry a force across water according to ship size and maximum passenger size. The official manual notes that sailing permits crossing water but not remaining in a water province. Capacity, commander ownership of the ability, passenger size, start and destination, and the exact route must all be legal.

Sailing is best treated as transport, not only as a troop trait. Its value comes from turning water barriers into possible attack lanes. Counterplay includes coastal scouting, route denial, and defence of landing provinces as well as battle strength.

## 23. Teleportation, Blink, and Immobility

Teleport and map teleport grant unusual movement that can ignore ordinary routes. Blink is a battlefield displacement effect. Unteleportable blocks relevant movement magic. Immobile units cannot use ordinary strategic movement. No River Pass forbids a class of crossings even where a normal unit could pass.

Current rules permit commanders with teleport movement to leave a besieged fort. That 6.35 operational exception remains in force under 6.36 and should not be inferred for every ritual or movement effect. The order and hosting timing remain in [Book X](#b10-orders) and [Book I](#b1-phase-iii-movement-and-conquest).

# Part IV: Leadership, Squads, and Command Support

## 24. Three Leadership Pools

Dominions separates normal, magic, and undead leadership. A commander can have different capacity in each pool.

| Leadership | Primary followers | Failure if absent |
| --- | --- | --- |
| Normal | Ordinary living troops and animals | Units cannot be assigned beyond valid capacity; squad quality may suffer with weak leaders. |
| Magic | Magic Beings | Uncontrolled magical beings rout or dissolve in battle. |
| Undead | Undead and demons; also the precedence case for undead/demon plus magic | Uncontrolled units rout or dissolve; banishment vulnerability remains. |

The displayed capacity is only the first question. Leadership quality also changes squad morale, and special abilities can modify particular followers. Experience increases command capacity. Poor leaders receive reduced experience increments: the manual's leadership chapter gives a base-10 poor leader +5 at the first star and +10 for later thresholds, rather than the ordinary +25 and then +50 sequence.

## 25. Standard and Inspirational

Standard raises the morale of the squad. Only the best Standard in the squad applies; multiple standards do not add. This makes distribution more important than concentration. A spare standard bearer may provide redundancy, but it does not normally double the current bonus.

Inspirational modifies the morale of troops commanded by that commander. Its value can be positive or negative. Because Standard belongs to the squad and Inspirational belongs to command, they should not be collapsed into one label even when both affect morale.

## 26. Taskmaster, Beast Master, and Special Followers

Taskmaster improves the command of slaves and changes their morale treatment. Beast Master improves command of animals. Similar special-leadership effects exist for particular classes. These abilities should be evaluated against the actual roster rather than as free generic leadership.

A commander with narrow but powerful command support can be more valuable than a higher ordinary leadership number when the army is composed of the matching followers. The reverse is also true: special leadership attached to the wrong roster is unused capacity.

## 27. Formation Fighter, Tight Reins, and Undisciplined Units

Formation Fighter changes how densely units can occupy and fight within battlefield squares. Its value is formation-wide only if enough bodies in the relevant line possess it. Book IV owns square capacity, placement, and contact consequences.

Tight Reins concerns control of mounts. Undisciplined units cannot follow the full ordinary order set and can undermine carefully scripted squad behaviour. A red squad marker in Army Setup is a command warning, not an aesthetic category.

## 28. Bodyguards and Warning

Units ordered to Guard Commander may appear in assassination battles according to the bodyguard system. Warning improves protection against assassination and related surprise. The bodyguard value must be treated as a chance or capacity within that system, not as a promise that the commander cannot be reached.

Patch 6.35 fixed an exploit in which bodyguards assigned to a distant commander could be used improperly. Current procedures should not rely on the older behaviour.

# Part V: Concealment, Perception, and Covert Action

## 29. Stealth Is a Contest, Not Invisibility

Stealth allows units and commanders to sneak in hostile territory. Discovery depends on patrol pressure and relevant modifiers. A stealth value grants movement permission and contributes to concealment. It does not make the unit absent from every information source or immune to every patrol.

Army stealth is constrained by composition. A stealthy commander cannot carry ordinary visible troops while sneaking unless another effect makes the whole group eligible. Size, number, terrain, patrols, and specialised abilities can all matter.

## 30. Spy, Assassin, and Infiltration Families

Spy permits intelligence and unrest-oriented covert work. Assassin creates assassination attempts. Seduction, Corruption, Dream Seduction, and related abilities use distinct target restrictions, events, checks, and failure battles. They should not be generalised from the word “assassin.”

The operational procedure is in [Book X's strategic-order reference](#b10-orders); strategic use and patrol counterplay are in [Book VI](#b6-patrol-and-stealth). Book XI supplies the reading rule: check the exact ability, target class, location, patience requirement, and consequence of failure.

## 31. Glamour, Invisibility, Unseen, and Illusion

These names cover four different rule paths. The 6.36 documentation and pinned current-description layer establish the following division.

| Effect | Strategic-map rule | Combat rule | Boundary |
| --- | --- | --- | --- |
| Glamour trait | Cannot be discovered by scouts; the main manual describes Glamour units as undetectable in friendly provinces. If the unit already has Stealth, the trait adds 25; it does not grant Stealth by itself | Grants a mirror-image defence | Mirror Image is an image-selection defence, not the Invisibility Attack penalty |
| Invisibility | A sneaking invisible unit can be found only by patrollers with Spirit Sight | Melee attackers suffer −10 Attack unless they have Spirit Sight | The revision-2 main manual's −9 is older wording; MM 6.36 supplies the live value |
| Unseen | Inherits the documented Invisible behaviour | Ends when the unit is hit | The current Invisibility spell grants Unseen, so its invisibility can end on a hit |
| Illusion class | No generic strategic concealment follows from the class alone | Spiritform-like technical class; illusion magic can affect it despite Mindless | It is a creature class, not a miss-chance synonym |
| Spiritform class | No generic strategic concealment follows from the class alone | Spirit-like class with specific immunities, including the documented Stoneskin and Polymorph examples | It supplies no generic Invisibility or Mirror Image rule |

Blur and Displacement belong to the same practical counter search but remain separate battle states. Blur applies a −2 melee Attack penalty. Displacement applies −10 to the first strike against each affected unit and −5 thereafter; its current description says it does not stack with Blur or Invisibility. True Sight, Spirit Sight, and blindness ignore Blur and Displacement. The current Mirror Image spell description separately states that True Sight does not negate its images.

The category-level R-048 question is therefore complete at an Official plus current-description tier. R-058 now has two narrow official strategic answers: Arcoscephale's special dominion scrying reveals enemy units using Glamour to hide, and The Eyes of God detects non-stealthing glamoured or invisible troops inside the caster's dominion. These permissions do not establish a universal scrying rule. Spirit Sight and blindness against innate Glamour's Mirror Image, generic scrying, Spy reports, and the stated limits of those two special channels remain controlled-test questions.

## 32. Darkvision, Spirit Sight, True Sight, and Blindness

Darkvision reduces darkness penalties according to its value; 100 is perfect Darkvision. It does not help a blind unit and does not itself answer Invisibility, Glamour, Blur, Displacement, Illusion, or Spiritform.

Spirit Sight removes darkness penalties, sees invisible units, and is the explicit strategic patrol requirement for finding sneaking Invisible units. The current UI description also says it sees invisible and glamoured units for what they are. True Sight sees through illusions and glamour and removes penalties when attacking Invisible or glamour-enchanted targets such as Blur. The pinned UI descriptions confirm that both Spirit Sight and True Sight ignore Blur and Displacement.

Blindness is not a superior version of either sight ability. A blind attacker already operates without normal vision, so the official descriptions exempt it from additional Invisibility, Blur, and Displacement penalties. Blindness does not thereby grant strategic detection, illuminate darkness, reveal scouts, or remove every illusion effect.

Sight is an attack-enabling system. A unit can have an excellent nominal Attack or Precision score and still deliver poorly when darkness or concealment denies reliable contact. Conversely, specialised sight has little value when the opponent offers no corresponding gate. Its price belongs to the matchup.

# Part VI: Defence, Recovery, and Persistence

## 33. Resistances Are Typed Defences

Fire, cold, shock, poison, acid, disease, and other resistances answer matching effects. Physical resistance families such as pierce, slash, and blunt resistance reduce their relevant damage classes. Invulnerability supplies protection under its defined restrictions. Air Shield reduces the chance of relevant missiles hitting.

A resistance value should always be paired with the incoming effect's type and penetration rule. “Has resistance” is not enough. A force may resist the primary damage while remaining vulnerable to fatigue, armour damage, secondary conditions, Magic Resistance effects, morale pressure, or a different damage type.

Book IV owns exact damage and protection resolution. The retrieval rule here is to inventory layers rather than add unlike numbers together.

## 34. Ethereal, Twist Fate, Luck, and Glamour

These are separate defensive gates.

- **Ethereal:** the official manual gives a 75 percent miss chance to nonmagical strikes and permits passage through fort walls while storming.
- **Twist Fate:** negates a qualifying damaging event and is then expended.
- **Luck:** creates its own chance-based survival layer.
- **Glamour:** supplies mirror images that attacks can remove.

Magical attacks answer Ethereal directly, but not every other defence. A high volume of attacks may clear images and one-use protection, while accurate high-value attacks can still be wasted on decoys. A counter plan should list the order in which the defences are expected to be consumed.

## 35. Regeneration Families

Regeneration heals a percentage of maximum hit points during battle and reduces the chance of affliction from damage. Since patch 6.31, regeneration is calculated to the exact percentage rather than older bracket behaviour. Ordinary regeneration does not work on inanimate bodies. Reconstruction is the corresponding inanimate form, while Reforming Flesh or undead regeneration supports eligible undead bodies.

The displayed percentage is not a complete survival estimate. Regeneration is strongest when incoming damage arrives in survivable packets and combat lasts long enough for repeated healing. It is weaker against overwhelming single hits, disablement, soul destruction, swallowing, routes, or damage that exceeds recovery tempo.

False regeneration and enchanted-blood effects are specialised variants and should be read from their current descriptions. Patch 6.35 improved the printed Magic Resistance bonus from Enchanted Blood; older guides may omit or misstate it.

## 36. Reinvigoration

Reinvigoration removes fatigue over time. It increases the sustainable rate of attacks, spellcasting, and other exertion, but it does not erase the consequences of already becoming unconscious or critically fatigued. A low-encumbrance unit with modest reinvigoration may outperform a nominally stronger body in a long fight; a short decisive fight may make the same investment nearly irrelevant.

Fatigue thresholds and critical-hit consequences remain in [Book IV](#b4-part-x-fatigue-recovery-and-collapse).

## 37. Recuperation and Healers

Recuperation attempts to heal battle afflictions over time, except those caused by old age. Ordinary Healer abilities assist eligible living units. Disease Healer addresses disease. Special bodies require special routes, and some item-caused afflictions cannot be removed while the item remains equipped.

The manual lists further recovery sources including Gift of Health, the Chalice, Miraculous Cure-all Elixir, rituals, sites, and Corpse Stitchers for eligible corporeal undead. Each route has eligibility limits and affliction difficulty. Recovery planning should record the damaged unit's body class, cause of affliction, and available healer type. Counting healer icons is not enough.

## 38. Immortality, Reformation, and Extra Lives

Immortality and dominion immortality return an eligible unit after death under their defined conditions and delay. Reformation abilities provide related return mechanics for particular bodies. Extra Lives permit a form of repeated survival or transformation.

Return is not the same as preventing defeat. A dead immortal may still surrender a battle, province, items, tempo, or access to the location from which it returns. Soul destruction, hostile dominion, remote planes, or ability-specific restrictions can bypass or delay the ordinary promise. Pretender death and Call God remain in [Book III](#b3-part-viii-death-of-a-god).

# Part VII: Auras, Reactive Effects, and Contact Abilities

## 39. Awe, Sun Awe, Fear, and Dread

Awe makes an attacker pass a morale check before carrying out an attack. The official manual expresses the check against `10 + Awe`. Sun Awe follows the same family but is disabled in darkness or underground conditions. Awe is consequently strongest when it forces many low-quality attackers to make repeated checks and weakest against attackers with strong morale, immunity, or a way to avoid ordinary contact.

Fear affects morale in an area. The manual describes a base check of 10, a base area of 6, and increased area or difficulty from higher values. Current Fear behaviour has received patch corrections, so [Book IV's morale chapter](#b4-part-xi-morale-fear-rout-and-retreat) is the authority for the exact current battle procedure. Dread belongs to the same broad pressure family but must be read from its own description rather than treated as merely a larger Fear number.

These abilities win by changing participation. Awe may prevent attacks that were otherwise legal. Fear may make a squad or army leave before hit points are exhausted. Their counters are morale, leadership, mindless or other relevant immunity, range, fast killing, and the removal of the fear source.

## 40. Heat, Chill, Poison, Disease, Sleep, and Nightmare Auras

Combat auras create persistent local hazards around a unit.

| Aura | Main pressure | Common answer family |
| --- | --- | --- |
| Heat | Fatigue and fire-related attrition | Fire resistance, temperature planning, range, rapid removal |
| Chill | Fatigue and cold-related attrition | Cold resistance, temperature planning, range, rapid removal |
| Poison Cloud | Poison accumulation | Poison resistance, spacing, ranged removal, regeneration only as support |
| Disease or Plague | Persistent disease and battlefield spread | Disease Resistance, avoidance, cure capacity, expendable separation |
| Sleep Aura | Unconsciousness or lost action | Relevant resistance, range, rapid killing, immunity |
| Nightmare Aura | Fear or sleep-related disruption according to the ability | Morale, appropriate resistance, range, source removal |

The manual gives a default aura size of 3 for Heat and Chill and explains their interaction with temperature scales. Poison clouds can persist and overlap. Patch 6.27 states that Disease Resistance applies against disease spells, including Plague. Check resistance even when disease arrives through magic instead of monthly attrition.

An aura's real value depends on time and density. A narrow crowded front can make a modest aura affect many bodies for many rounds. A dispersed missile battle may leave the same aura nearly unused.

## 41. Fire Shields, Acid, Spikes, Slime, and Entanglement

Reactive effects punish contact or successful strikes. Fire Shield damages qualifying attackers. Acid Shield and acid effects can damage or corrode. Spikes punish bodies that press into contact. Slime and entanglement can reduce mobility or prevent ordinary action. Some reactive effects require a hit; others require only an attack or adjacency.

This distinction changes the counter. High Defence may reduce on-hit retaliation but does not necessarily avoid a response that triggers on attack. Long weapons, missiles, spells, disposable attacks, resistance, or a different target order may remove the need for the vulnerable unit to touch the effect at all.

## 42. Damage Reversal, Blood Vengeance, Curses, and Horror Marks

Damage Reversal and Blood Vengeance return consequences to an attacker under their own resistance and trigger rules. They are particularly dangerous to high-output attackers whose own offence becomes the delivery mechanism. Small attacks may be inefficient if every trigger invokes a fixed test; enormous attacks may be catastrophic if the reflected consequence scales. The exact current description must decide which case applies.

Curse-on-contact and Horror Mark effects create consequences beyond the immediate exchange. A curse changes future misfortune and affliction risk. A horror mark creates a monthly chance of horror attack; repeated marks can increase its hidden severity, and horrors prefer marked targets. Stronger marks can attract stronger horrors.

These are persistence weapons. Killing the source does not necessarily remove a mark already applied. The value of an irreplaceable commander must include post-battle contamination, not only current hit points.

## 43. Petrification and Other Hard Stops

Petrification can stop or destroy attackers through a resistance interaction. Paralysis, stun, sleep, entanglement, frozen states, and swallowing can similarly remove action without first reducing hit points to zero.

Hard control is often the correct answer to regeneration, life drain, heroic defences, or other sustain because it attacks participation rather than the health pool. It is also unreliable when the target is immune, has high Magic Resistance, possesses specialised protection, or can reform after the relevant effect. A counter plan needs both a delivery mechanism and an answer to the target's class.

## 44. Ambidextrous, Clumsy, Berserker, and Multiweapon Bodies

Ambidextrous reduces the attack penalty from using multiple weapons by its value. It does not remove the additional weapon encumbrance. Clumsy imposes a corresponding handling problem. The value of Ambidextrous depends on the number and quality of actual attacks and on sustainable fatigue, not only the presence of the icon.

Berserker can activate when a wounded unit passes the specified morale test. While berserk, the unit gains its listed bonuses and continues fighting until dead rather than routing normally. Becoming unconscious ends the current berserk state, though the unit can enter it again after recovering and being wounded. Berserk is both a morale solution and a control cost: the unit cannot make ordinary retreat decisions after the state takes hold.

## 45. Trample

Trample lets a larger unit enter a square occupied by smaller units, displace them, and inflict armour-piercing damage through a Defence minus fatigue contest. The manual gives the failed-check damage as `7 + trampler Size`; an ethereal trampler deals half damage, and even a successful defence check still causes 1 point while displacement occurs.

The full procedure, square capacity, mount interaction, fatigue, and counter formation belong to [Book IV](#b4-trampling). The ability record adds three interpretive warnings:

- trample output depends on reaching smaller bodies and on available squares;
- fatigue reduces the victims' defence in the check and also degrades the trampler over time;
- size is part of both offence and target eligibility, so transformation, mounts, and opposing body size can reverse the plan.

## 46. Swallow, Digest, and Incorporate

Swallow removes a target from the battlefield until the swallower dies or the ability releases it. Digest damages the swallowed target each round. Incorporate converts some of that process into benefit for the swallowing creature.

The manual warns that swallowing prevents many life-saving effects. It can bypass plans based on allies, immortality timing, transformation, regeneration, or escape. Size and target restrictions are central. Counterplay usually means killing or disabling the swallower quickly, preventing contact, or presenting bodies it cannot legally swallow.

## 47. Life Drain, Raise-on-Kill, and Kill-Dependent Effects

Life Drain converts suitable damage into recovery and fatigue relief under its defined rules. Lifeless targets greatly reduce the damage after protection and do not heal the attacker through ordinary life drain. Raise-on-kill and soul-collection effects transform casualties into new bodies, gems, or other resources.

Kill-dependent abilities are nonlinear. They are weak before the first suitable victim dies, then can accelerate as new bodies or recovery increase contact. Denying legal victims, using lifeless or resistant screens, maintaining range, and destroying the carrier before the first conversion are more effective than evaluating the final snowball at full strength.

# Part VIII: Conditional, Economic, Magical, and Summoning Abilities

## 48. Seasonal Powers

Spring, Summer, Autumn, and Winter Power change a unit's statistics or capabilities with the season. A year-turn effect may transform forms or attributes as the calendar changes. The unit shown in one month is not necessarily stable across the year.

Seasonal units should be recorded as a schedule:

| Field | Record |
| --- | --- |
| Strong season | The months in which the positive modifier applies |
| Weak season | The months in which output or survival declines |
| Form change | Whether the body, magic, items, or command changes |
| Campaign deadline | The last hosting turn on which the intended operation retains the favourable state |
| Opponent option | Whether waiting, delaying a siege, or forcing an early battle changes the matchup |

Season is thus a strategic resource. It can create a predictable timing attack and an equally predictable window for avoidance.

## 49. Scale and Environmental Powers

Chaos, Cold, Fire, Death, Growth, Darkness, Storm, Magic, Sloth, and related powers change a unit in matching conditions. Dominion Power keys performance to dominion. These abilities mean the unit's statistics are partly provincial.

The correct comparison is not one card against another. It is the card in the likely battlefield province after forecast scale movement, dominion contest, storm creation, and light conditions. An enemy may counter the unit by changing the environment rather than fighting its favourable profile directly.

## 50. Supply, Siege, Patrol, Pillage, and Resource Effects

Need Not Eat removes ordinary supply consumption. Supply Bonus creates supplies. Siege Bonus, Siege Defence, Patrol Bonus, and Pillager modify state actions. Resource, gold, tax, gem, and unrest-related abilities convert a unit or commander into an economic object.

These abilities should be costed by use-month rather than by icon. A Supply Bonus on a commander who remains in the capital creates little value. The same commander on a long enemy route may preserve hundreds of troops. A Siege Bonus matters only when a fort is being converted or protected. A Patrol Bonus can be worth more than combat statistics in a blood economy or stealth war.

Book II owns the economic formulas; Book VI owns strategic conversion. Book XI records the permission and reminds the reader to count months of actual employment.

## 51. Research, Forge, Search, and Ritual Support

Research Bonus increases research output. Forge Bonus reduces eligible forging costs. Dousing and path-specific search bonuses improve Blood Hunting or site searching. Innate Spellcaster changes how a unit casts and can protect parts of its script from ordinary interruption rules.

Patch 6.35 corrected innate spellcasters that could skip their script after becoming temporarily unconscious. Current planning should use the restored behaviour and still account for the turns lost while unconscious.

Support abilities convert commander-turns. Their opportunity cost is central. A researcher moved to lead a patrol is not producing research. A forge specialist who spends every turn moving has no realised forge bonus. [Book V](#b5-foundation-book-v-magic) owns the resulting magic economy.

## 52. Summoner, Retinue, Dominion Summoner, and Battle Summoner

Summoning abilities create followers on a schedule or at a trigger. Retinues accompany or regenerate around a commander. Dominion Summoners depend on dominion or local conditions. Battle Summoners add bodies during combat.

Every summoning record needs five fields:

1. what is created;
2. when creation occurs;
3. whether the result persists;
4. what leadership it requires;
5. what cap, condition, or random range applies.

The created unit's own class may impose a new command burden. A commander can generate troops faster than the army can legally organise or transport them.

# Part IX: Experience and Veteran Units

## 53. How Experience Is Gained

The official manual states that units usually gain 1 experience point per month. A battle grants 4 experience if the unit does not retreat and 1 if it retreats, with battle experience awarded at most once in a month. A melee strike or trample action grants 1 experience. Community investigation adds finer descriptions for attack flurries, trampled squares, arena victories, events, and particular sites or items; those details are useful but remain version-sensitive unless reproduced against 6.36.

Mindless units are an important exception to ordinary monthly learning in community references, but the current official manual's general wording is not a full class-by-class specification. Where exact passive gain matters, inspect the live unit over controlled turns or use a current engine export.

Experience stays with the unit, not the unit type. Recruitment cost understates the replacement cost of a veteran formation.

## 54. Experience Thresholds

The official thresholds are 15, 50, 100, 200, and 400 experience points. Each threshold adds a star and a package of improvements.

| Total XP | New star's official incremental gains |
| --- | --- |
| 15 | Attack +1, Defence +1, Precision +1, Morale +1, Leadership +25, Research +1 |
| 50 | Attack +1, Defence +1, Precision +1, Morale +1, Leadership +50, Research +1 |
| 100 | Attack +1, Defence +1, Precision +1, Morale +1, Strength +1, Hit Points +1, Leadership +50, Research +1 |
| 200 | Attack +1, Defence +1, Precision +1, Morale +1, Hit Points +1, Encumbrance -1, Leadership +50, Research +1 |
| 400 | Attack +1, Defence +1, Precision +1, Morale +1, Strength +1, Hit Points +1, Magic Resistance +1, Leadership +50, Research +1 |

The five-star total is **+3 Hit Points**. This is not inferred from the table alone: official version 6.13 changed experience to grant +1 HP at every star from the third onward, version 6.14 corrected HP-stat handling for experience, and the current revision-2 manual prints +1 HP at 100, 200, and 400 XP. The familiar cumulative +2 table traces to Dominions 5.53 and is retained only as a historical pre-change result. A current calculator should therefore display +3 at five stars and label its version boundary.

Poor leadership receives smaller command gains. The official leadership section states that a base-10 poor leader receives +5 at the first star and +10 at each later threshold. For normal leadership, the displayed high-experience capacity can greatly exceed the commander's original value, while some morale-quality effects still refer to base leadership.

## 55. Experience Changes Roles Unevenly

The same star package has different value on different bodies.

- Attack and Defence compound the value of elite melee units that survive repeated contacts.
- Precision matters only when the unit delivers attacks or spells that use it.
- Morale improves formation reliability but adds little to a mindless body already using its special morale rule.
- Strength matters more for strength-scaled weapons and some siege or carrying interactions.
- Encumbrance reduction can change long-fight performance disproportionately.
- Magic Resistance is especially valuable on expensive targets that attract control magic.
- Research bonuses make surviving mage-commanders economically productive even when their paths do not change.
- Leadership gains can transform a marginal commander into a genuine army organiser.

Experience is not a flat percentage bonus. It changes the jobs a unit can perform.

## 56. Veteran Preservation

Veterans should be preserved when their added reliability is scarce and replaceable when preservation costs more than the advantage.

| Factor | Preservation favoured when | Replacement favoured when |
| --- | --- | --- |
| Recruitment | Slow, cap-only, sacred, or commander-point constrained | Cheap, local, and immediately replaceable |
| Star value | Attack, Defence, MR, Encumbrance, or Leadership crosses a functional threshold | Bonuses do not alter the current matchup |
| Afflictions | Healthy or recoverable | Limp, chest wound, feeblemind, or lost limbs remove the gained role |
| Position | A safe rotation route exists | Withdrawal exposes the army or abandons the objective |
| Time | Campaign is long enough to exploit future months | Victory deadline is immediate |

The Army Setup experience filter supports separation of veterans. Mixing them indiscriminately with recruits can waste the opportunity to assign different risk, formation, or leadership.

# Part X: Hall of Fame and Heroic Abilities

## 57. What Is Officially Established

The Hall of Fame ranks commanders that survive many battles or kill many enemies. Non-Pretender commanders in the Hall receive a heroic ability, shown by a yellow star in a red circle, and that ability improves while the commander remains listed. Unique beings such as Elemental Royalty cannot enter. Pretenders do not receive an ordinary heroic ability through this system.

The hosting sequence updates the Hall of Fame and graphs before heroic abilities improve. That timing can matter when a commander enters, leaves, or rises within the list.

The main manual does not publish the full current scoring formula, ability selection weights, or growth formulas. Exact heroic arithmetic circulating online is community reverse engineering, much of it inherited from Dominions 5. It should be used as a hypothesis and planning aid, not as a current official contract.

### 57.1 Edition 28 Formula Boundary

R-047 advances from queued to in progress, but no formula is promoted. The official evidence establishes eligibility, the existence and growth of a heroic ability while listed, and the hosting position of the Hall-of-Fame update. It does not expose the score weights for battles, kills, survival, rank ties, heroic-family selection, or per-turn growth.

A publishable 6.36 formula now requires a raw observation series rather than another prose summary. The Edition 28 source bundle includes `data/edition-28-hall-of-fame-observation-template.csv` with fields for version, seed, commander identity, Pretender and unique status, battles, kills, rank before and after hosting, heroic family, displayed value before and after hosting, survival, Hall membership, and screenshot or save evidence. Tests should hold map, Hall size, unit type, opponent, battle count, and kill allocation constant while changing one factor at a time.

The first series should answer three smaller questions in order:

1. whether zero-kill survival and credited kills make separable score contributions;
2. how exact ties are ordered when otherwise identical commanders enter on the same hosting;
3. whether a displayed heroic value changes once per hosting, once per Hall update, or by an ability-specific schedule.

Until that series or an engine-backed trace exists, the community families below remain a discovery aid and the exact formulas remain withheld.

## 58. Community-Derived Heroic Families

Older reverse engineering identifies common heroic families such as Strength, Battle Prowess, Lightning Reflexes, Iron Will, Valor, Tough Skin, Heroic Toughness, Heroic Quickness, Precision, Endurance, Obesity, and Extraordinary Agility. Rarer reported families include Awesome Presence, Battle Bellow, Legendary Command of Undead, Adept Research, Third Eye, Daftness, Cruelty, Soul Butcher, Fast Casting, and Troll Blood.

The practical descriptions are safer than exact old formulas:

| Family | Reported growth | Principal use |
| --- | --- | --- |
| Enormous Strength | Strength | Damage, carrying, and strength-based tasks |
| Battle Prowess | Attack | More reliable melee contact |
| Lightning Reflexes | Defence | Avoiding ordinary attacks |
| Iron Will | Magic Resistance | Resisting hostile magic |
| Valor | Morale, leadership, inspiration | Army command and rout resistance |
| Tough Skin | Natural protection | Physical survival before armour interaction |
| Heroic Toughness | Percentage hit points | Larger health pool, especially on high-base-HP bodies |
| Heroic Quickness | Faster action interval and combat movement in community models | More actions and faster contact; exact 6.36 formula unverified |
| Heroic Precision | Precision | Ranged and spell delivery where Precision applies |
| Heroic Endurance | Reinvigoration | Sustainable action in long battles |
| Extraordinary Agility | Attack, Defence, ambidexterity | Multiweapon melee performance |
| Fast Casting | Casting speed | More spell actions; rare and version-sensitive |
| Troll Blood | Regeneration | Percentage recovery; rare and version-sensitive |

Community formulas commonly model a hidden heroic value that begins near 100 and grows by random increments while the commander remains in the Hall. Because the best-known source predates Dominions 6 and current verification is incomplete, this edition does not promote those formulas into the official register.

## 59. Evaluating a Heroic Commander

A heroic ability should be evaluated as a new role constraint, not a trophy.

1. Record the commander's base job.
2. Identify whether the heroic gain strengthens that job or opens a different one.
3. Recalculate equipment, script, bodyguards, and retreat plan.
4. Price the loss of Hall growth if the commander leaves the ranking.
5. Separate a current displayed bonus from a projected community formula.

Heroic Toughness on a large body can create much more absolute health than on a human. Fast Casting on a battle mage may alter an entire script. Valor on a poor commander may create a new army leader. Conversely, melee heroics on a researcher do not automatically justify risking years of accumulated research output.

# Part XI: Conditions and Lasting State

## 60. Conditions Are State, Not Flavour Text

A condition may alter statistics, action, targeting, recovery, loyalty, or future events. Some expire during battle. Others remain for months, survive shape changes, or cannot ordinarily be removed. A unit card reports the current state; it is not a permanent template.

The first distinction is duration:

| Duration class | Examples | Audit question |
| --- | --- | --- |
| Immediate or one-resolution | Stun, short paralysis, a consumed Twist Fate | Does the unit act before the next decisive event? |
| Battle-persistent | Poison, bleeding, burning, frozen, fatigue, entanglement | Can resistance, recovery, or battle end remove it? |
| Month-persistent | Disease, insanity, many afflictions | What happens during hosting and can treatment occur first? |
| Indefinite mark | Curse, Horror Mark, some taints | Is there any ordinary removal route? |
| Source-bound | Item-caused affliction, shape, mount state | Must the source be removed or changed before recovery? |

## 61. Afflictions

An affliction is a lasting injury. The official manual gives the base chance as the percentage of normal maximum hit points lost to a damaging strike, with hit location determining what injuries are possible. Major and minor afflictions differ. A unit can accumulate several, shown by a red-heart icon.

Examples include lost eyes, lost arms, weakened limbs, chest wounds, never-healing wounds, battle fright, feeblemind, mute, crippled, and disease. The consequences vary from small statistic penalties to destruction of the unit's original role. A lost arm is far more serious for a two-handed weapon user than for a spellcaster that retains all required paths and casting faculties; feeblemind can reverse that evaluation.

Healing follows eligibility and difficulty, not sentiment. Recuperation excludes Old Age afflictions. Ordinary healers cannot repair many undead, inanimate, or spiritform bodies. Special recovery routes exist but must match the body. Cursed-item injuries may require item removal. [Book IV](#b4-part-xiii-afflictions-regeneration-and-lasting-loss) owns the exact chance, hit-location table, and battle consequences.

## 62. Disease and Old Age

Disease causes continuing deterioration and may add afflictions. Undead, demons, lifeless beings, and spiritforms have relevant immunities according to their classes. Disease Resistance reduces eligible disease effects, and patch 6.27 extended its protection to disease spells such as Plague.

Old age is a separate risk process tied to current age and maximum age. Maximum age is modified by magic paths according to body: Death for undead, Earth for inanimate bodies, Blood for demons, and Nature for most ordinary beings. Fire can reduce maximum age for bodies whose age is Nature-modifiable. Recuperation does not heal afflictions whose cause is old age.

The operational lesson is to distinguish a diseased young commander, an old commander accumulating age afflictions, and a diseased old commander. They require different forecasts even when the red-heart display looks similar.

## 63. Curse and Horror Mark

Curse increases the chance of suffering afflictions from future wounds and is not ordinarily removed. Horror Mark creates a hidden accumulated severity and a monthly chance of attack by horrors. Horrors prioritise marked units, and stronger marks can attract more dangerous attackers.

Neither condition should be confused with an affliction. Ordinary healing is not the answer. Horror marks may lessen while a unit is dead in some return systems, but exact current reduction is ability-specific and should not be assumed as a universal cleansing method.

## 64. Insanity, Tainted, Yearning, and Homesickness

Insanity can cause a commander to take an unwanted monthly action instead of the assigned order. Tainted and Yearning impose their own recurring risks or location dependencies. Homesickness harms or pressures units away from their proper home or plane.

These conditions convert reliability into probability. The unit may look fully capable and still fail to perform the one strategic order on which a turn depends. Redundancy, safe roles, location planning, and command audits are their primary counters. A critical ritual should not be assigned to an insane commander without an accepted failure branch.

## 65. Poison, Burning, Bleeding, Frozen, and Corrosion

Poison accumulates delayed damage and, since patch 6.30, also reduces Precision. Burning and bleeding cause continuing harm under their rules. Frozen impairs the unit and can combine with cold pressure. Rust and acid can damage armour rather than merely the body.

Patch 6.30 clarified that Spiritform, rather than Ethereal, protects against bleeding, frozen, and burning states. A visual ghost or mist sprite is not enough; the actual tag must be present.

These conditions matter because resistance to the initial strike may not answer the secondary state. Battle review should inspect both damage numbers and icons.

## 66. Stun, Paralysis, Sleep, Entanglement, and Confusion

Stun and paralysis remove or delay actions. Sleep produces unconsciousness. Entanglement holds a unit in place until it escapes or the effect ends. Confusion disrupts normal behaviour. These conditions win time, and time converts into attacks, spell completions, fatigue recovery for one side, and aura exposure for the other.

The correct measure is not only duration. It is the number and value of actions denied before the unit recovers. A one-round stop on a fast caster or trampler may be worth more than a long disable on an irrelevant rear unit.

## 67. Charm, Enslave, Transformation, and Control Loss

Charm and enslavement can change ownership or control. Transformation changes the body and can replace important tags, magic, equipment eligibility, or movement. Polyimmune and other class immunities can prevent specified transformations.

Control effects attack the investment rather than the hit-point pool. Magic Resistance, penetration, body-class immunity, range, and killing the controller or target may all matter. Their strategic consequence includes information and item loss as well as battle output.

# Part XII: Master Ability and Condition Register

## 68. How to Use the Register

The following records are deliberately concise. They identify the first-order rule, the main caveat or counter, and the strongest preserved evidence layer. They are not substitutes for the live description of a specific unit or for Book IV's combat procedures.

Evidence codes are defined in [Section 2](#b11-2-evidence-key-and-version-discipline). “UI check” means that the current value or object-specific wording should be read in the game before committing a design.

<!-- DATA:BEGIN abilities -->
| Name | Category | Core function | Principal caveat or counter | Evidence | Primary anchor |
| --- | --- | --- | --- | --- | --- |
| Animal | Class | Normal-led creature; half ordinary supply use; reduced armless siege value except monkeys | Animal-specific control and awe; siege contribution | OM, MM | b11-10-animal |
| Magic Being | Class | Requires magic leadership | Leader loss; magic-being targeting; undead-plus-magic uses undead leadership | OM, MM | b11-11-magic-being |
| Mindless | Class | Morale 50 under control; many mind effects fail | Cannot mix with non-mindless; dissolves without suitable leader | OM, MM | b11-12-mindless |
| Undead | Class | Requires undead leadership; disease immune; banishable | Ordinary healing restrictions; anti-undead effects; harmful living mix | OM, MM | b11-13-undead |
| Demon | Class | Requires undead leadership; disease immune; banishable | Demon-specific effects; do not infer undead or elemental traits | OM, MM | b11-14-demon |
| Inanimate or Lifeless | Class | Nonliving body with disease, life-drain, and ordinary-healing immunities | Needs Reconstruction or specialised repair; class wording is object-specific | OM, MM | b11-15-inanimate-and-lifeless |
| Spiritform | Class | Spirit body; transformation, disease, and ordinary-healing immunity | Not identical to Ethereal; specialised spirit effects remain | OM, OP | b11-16-spiritform |
| Plant | Class | Plant-type target category | Does not imply Mindless, Inanimate, or resistances | MM | b11-17-1-plant |
| Stone Being | Class | Stone-specific target category | Do not infer Inanimate unless separately present | MM | b11-17-2-stone-being |
| Illusion | Class | Illusory creature category | Distinct from Glamour, Invisibility, and Ethereal | MM | b11-17-3-illusion |
| Horror | Class | Lesser, Greater, or Doom Horror category | Horror Mark does not grant this class | MM | b11-17-4-horror |
| Sacred | Religion | Eligible for blessing and Holy recruitment rules | Must be blessed; Incarnate effects require proper god state | OM | b11-17-5-sacred-holy-divine-being-pretender-and-prophet |
| Cold Blooded | Body | Suffers additional fatigue in cold | Cold scales and chill pressure; verify exact current modifier | OM, MM | b11-18-cold-blood-blindness-sex-and-other-body-tags |
| Aquatic | Movement | Operates underwater | Usually land-incompatible without another form or effect | OM, MM | b11-19-water-status-is-a-permission-system |
| Amphibian | Movement | Operates on land and underwater | Underwater weapons, mounts, and spells still matter | OM, MM | b11-19-water-status-is-a-permission-system |
| Poor Amphibian | Movement | Cross-environment permission with penalties | Penalties can make nominal access tactically poor | OM, MM | b11-19-water-status-is-a-permission-system |
| Flying | Movement | Strategic and battlefield flight | Storms, retreat routes, squad compatibility, anti-flyer screens | OM, MM | b11-20-flying-floating-and-storms |
| Floating | Movement | Passes relevant ground or terrain constraints | Not full flight; mount interaction is separate | MM, OP | b11-20-flying-floating-and-storms |
| Storm Immunity | Movement | Retains relevant function during storms | Does not grant flight by itself | MM | b11-20-flying-floating-and-storms |
| Terrain Survival | Movement | Reduces matching terrain movement burden | One incompatible army member can constrain route | OM, MM | b11-21-terrain-survival-and-snow-movement |
| Sailing | Movement | Carries eligible force across water | Capacity, passenger size, route, and no underwater stay | OM, MM | b11-22-sailing |
| Teleport | Movement | Unusual strategic movement | Unteleportable, legality, timing, and retreat; 6.35 siege exception is narrow | MM, OP | b11-23-teleportation-blink-and-immobility |
| Immobile | Movement | Cannot use ordinary strategic movement | Requires summons, remote influence, or special movement | MM | b11-23-teleportation-blink-and-immobility |
| Magic Leadership | Command | Commands Magic Beings | Capacity and leader survival; does not replace undead precedence | OM, MM | b11-24-three-leadership-pools |
| Undead Leadership | Command | Commands undead and demons | Capacity and leader survival; anti-leader attacks | OM, MM | b11-24-three-leadership-pools |
| Standard | Command | Raises squad morale | Only best Standard in squad applies | OM, MM | b11-25-standard-and-inspirational |
| Inspirational | Command | Modifies morale of commanded troops | Can be negative; commander-bound rather than squad item | OM, MM | b11-25-standard-and-inspirational |
| Taskmaster | Command | Improves slave command and morale | Valuable only with matching followers | OM, MM | b11-26-taskmaster-beast-master-and-special-followers |
| Beast Master | Command | Improves animal command | Animal-specific; ordinary roster gains little | OM, MM | b11-26-taskmaster-beast-master-and-special-followers |
| Formation Fighter | Command | Permits denser fighting formation | Needs formation-wide support; crowding and area effects remain | OM, MM | b11-27-formation-fighter-tight-reins-and-undisciplined-units |
| Undisciplined | Command | Restricts ordinary squad orders | Reduces script control; separate from low morale | OM, MM | b11-27-formation-fighter-tight-reins-and-undisciplined-units |
| Bodyguard | Command | Chance for guards to join assassination defence | Not certainty; current exploit fixed in 6.35 | OM, OP | b11-28-bodyguards-and-warning |
| Stealthy | Covert | Permits sneaking and contributes concealment | Patrol contest, composition, terrain, and size | OM, MM | b11-29-stealth-is-a-contest-not-invisibility |
| Spy | Covert | Enables intelligence and covert unrest work | Patrols and order-specific exposure | OM, MM | b11-30-spy-assassin-and-infiltration-families |
| Assassin | Covert | Attempts assassination | Bodyguards, Warning, target restrictions, failure battle | OM, MM | b11-30-spy-assassin-and-infiltration-families |
| Seduction family | Covert | Attempts special recruitment, corruption, or assassination outcomes | Sex, target, patience, location, checks, and failure differ by ability | OM, MM | b11-30-spy-assassin-and-infiltration-families |
| Glamour | Concealment | Mirror images in battle; hidden in friendly provinces | Images can be stripped; specialised sight; not Illusion | OM, MM | b11-31-glamour-invisibility-unseen-and-illusion |
| Invisibility or Unseen | Concealment | Makes detection or targeting difficult | Exact perception counter is ability-specific | MM, UI | b11-31-glamour-invisibility-unseen-and-illusion |
| Darkvision | Perception | Reduces darkness penalties | Percentage or value matters; does not answer every concealment | OM, MM | b11-32-darkvision-spirit-sight-true-sight-and-blindness |
| Spirit Sight | Perception | Detects relevant spiritual or ethereal targets | Not a universal True Sight substitute | OM, MM | b11-32-darkvision-spirit-sight-true-sight-and-blindness |
| True Sight | Perception | Counters specified deception | Check exact effect; darkness may remain separate | MM, UI | b11-32-darkvision-spirit-sight-true-sight-and-blindness |
| Elemental Resistance | Defence | Reduces matching fire, cold, shock, poison, or acid pressure | Secondary effects and other damage types can bypass the plan | OM, MM | b11-33-resistances-are-typed-defences |
| Physical Resistance | Defence | Reduces matching pierce, slash, or blunt damage | Wrong weapon type bypasses; exact layer in Book IV | OM, MM | b11-33-resistances-are-typed-defences |
| Air Shield | Defence | Reduces chance of relevant missiles hitting | Spells and nonmissile delivery; exact percentage | OM, MM | b11-33-resistances-are-typed-defences |
| Ethereal | Defence | 75 percent of nonmagical strikes miss; passes fort walls | Magical attacks; other layers still apply | OM | b11-34-ethereal-twist-fate-luck-and-glamour |
| Twist Fate | Defence | Negates a qualifying damaging event, then ends | Multiple attacks or prior expendable hit | OM, MM | b11-34-ethereal-twist-fate-luck-and-glamour |
| Luck | Defence | Chance-based survival layer | High attack volume; verify interaction order | OM, MM | b11-34-ethereal-twist-fate-luck-and-glamour |
| Regeneration | Recovery | Heals exact percentage of maximum HP per round and reduces affliction risk | Burst damage, disablement, inanimate immunity, soul effects | OM, OP | b11-35-regeneration-families |
| Reconstruction | Recovery | Regeneration for inanimate bodies | Verify percentage and body eligibility | OM, MM | b11-35-regeneration-families |
| Undead Regeneration | Recovery | Regeneration family for eligible undead | Not every undead has it; burst and control remain | OM, MM | b11-35-regeneration-families |
| Reinvigoration | Recovery | Removes fatigue over time | Cannot restore actions already lost; short fights may not use it | OM, MM | b11-36-reinvigoration |
| Recuperation | Recovery | Attempts to heal eligible battle afflictions over months | Excludes old age; class and affliction difficulty restrictions | OM, MM | b11-37-recuperation-and-healers |
| Healer | Recovery | Attempts to heal eligible units | Body and affliction eligibility; healer value and difficulty | OM, MM | b11-37-recuperation-and-healers |
| Immortality | Persistence | Returns after death under defined conditions | Delay, dominion, soul destruction, position, and lost battle | OM, MM | b11-38-immortality-reformation-and-extra-lives |
| Awe | Aura | Forces attacker morale check against 10 plus Awe | Morale, immunity, missiles, spells, rapid removal | OM, MM | b11-39-awe-sun-awe-fear-and-dread |
| Sun Awe | Aura | Awe family dependent on light | Disabled underground or in darkness | OM, MM | b11-39-awe-sun-awe-fear-and-dread |
| Fear | Aura | Applies local morale pressure | Leadership, morale, mindless, range, source removal; exact current procedure in Book IV | OM, OP | b11-39-awe-sun-awe-fear-and-dread |
| Heat or Chill Aura | Aura | Applies local fatigue and elemental pressure | Matching resistance, scales, spacing, range | OM, MM | b11-40-heat-chill-poison-disease-sleep-and-nightmare-auras |
| Poison Cloud | Aura | Accumulates poison in an area | Poison resistance, spacing, ranged removal | OM, MM | b11-40-heat-chill-poison-disease-sleep-and-nightmare-auras |
| Disease or Plague Aura | Aura | Applies persistent disease pressure | Disease Resistance, separation, cure capacity | OM, OP | b11-40-heat-chill-poison-disease-sleep-and-nightmare-auras |
| Sleep Aura | Aura | Causes nearby units to become unconscious | Resistance or immunity, range, rapid removal | MM, UI | b11-40-heat-chill-poison-disease-sleep-and-nightmare-auras |
| Fire Shield | Reactive | Damages qualifying attackers in contact | Fire resistance, range, long weapons, disposable attacks | OM, MM | b11-41-fire-shields-acid-spikes-slime-and-entanglement |
| Damage Reversal | Reactive | Returns a consequence to attacker | Exact trigger and resistance; nonqualifying attacks | OM, MM | b11-42-damage-reversal-blood-vengeance-curses-and-horror-marks |
| Blood Vengeance | Reactive | Punishes damage through a resistance interaction | Magic Resistance, attack selection, ranged or disposable delivery | OM, MM | b11-42-damage-reversal-blood-vengeance-curses-and-horror-marks |
| Petrification | Reactive | Hard-stop effect against qualifying attackers | Magic Resistance, immunity, noncontact delivery | OM, MM | b11-43-petrification-and-other-hard-stops |
| Ambidextrous | Combat | Reduces multiweapon attack penalty by value | Does not remove extra weapon encumbrance | OM, MM | b11-44-ambidextrous-clumsy-berserker-and-multiweapon-bodies |
| Berserker | Combat | Wounded morale check can enter no-rout combat state with bonuses | Loss of control; unconsciousness ends current state | OM, MM | b11-44-ambidextrous-clumsy-berserker-and-multiweapon-bodies |
| Trample | Combat | Displaces smaller units and deals size-based armour-piercing damage | Large targets, fatigue, formation, space, ranged disablement | OM, MM | b11-45-trample |
| Swallow or Digest | Combat | Removes and damages eligible target inside swallower | Size restriction; kill or disable swallower; blocks many life-saving effects | OM, MM | b11-46-swallow-digest-and-incorporate |
| Life Drain | Combat | Converts suitable damage into recovery | Lifeless targets; range; resistance; rapid killing | OM, MM | b11-47-life-drain-raise-on-kill-and-kill-dependent-effects |
| Seasonal Power | Conditional | Changes attributes in a matching season | Predictable weak months; year-turn or form changes | MM | b11-48-seasonal-powers |
| Scale Power | Conditional | Changes attributes in matching scales or environment | Change scales, light, storm, or battlefield location | MM | b11-49-scale-and-environmental-powers |
| Need Not Eat | Economy | Consumes no ordinary supplies | Does not imply disease, undead, or inanimate status | OM, MM | b11-50-supply-siege-patrol-pillage-and-resource-effects |
| Supply Bonus | Economy | Produces supplies | Value realised only where supply is binding | OM, MM | b11-50-supply-siege-patrol-pillage-and-resource-effects |
| Siege or Patrol Bonus | Economy | Improves matching province action | No value while action is unused; exact formula elsewhere | OM, MM | b11-50-supply-siege-patrol-pillage-and-resource-effects |
| Research Bonus | Magic support | Adds research output | Commander-turn opportunity cost | OM, MM | b11-51-research-forge-search-and-ritual-support |
| Forge Bonus | Magic support | Reduces eligible forge cost | Item and path eligibility and rounding; only while forging | OM, MM | b11-51-research-forge-search-and-ritual-support |
| Innate Spellcaster | Magic support | Uses innate casting rules | Current 6.35 script fix; fatigue and unconsciousness still matter | OM, OP | b11-51-research-forge-search-and-ritual-support |
| Summoner or Retinue | Summoning | Creates or restores followers on a trigger or schedule | Leadership, cap, persistence, and created class | MM, UI | b11-52-summoner-retinue-dominion-summoner-and-battle-summoner |
| Experience | Development | Adds star packages at 15, 50, 100, 200, and 400 XP | Role-specific value; official and community cumulative HP discrepancy | OM, CT | b11-54-experience-thresholds |
| Heroic Ability | Development | Hall-of-Fame commander gains a growing special trait | Exact formula and rarity are community-derived and version-sensitive | OM, CT | b11-57-what-is-officially-established |
| Affliction | Condition | Lasting injury with body-part and difficulty rules | Correct healer and body eligibility; role can be lost | OM | b11-61-afflictions |
| Disease | Condition | Continuing deterioration and affliction risk | Disease Resistance, immunity, Disease Healer; distinct from old age | OM, OP | b11-62-disease-and-old-age |
| Curse | Condition | Persistent increased misfortune and affliction exposure | Not ordinarily removable; avoid contamination | OM | b11-63-curse-and-horror-mark |
| Horror Mark | Condition | Hidden stacked severity and monthly horror-attack chance | Not ordinary affliction; conceal, protect, or accept long risk | OM | b11-63-curse-and-horror-mark |
| Insanity | Condition | Chance of unwanted monthly behaviour | Redundancy and noncritical assignments | OM, MM | b11-64-insanity-tainted-yearning-and-homesickness |
| Old Age | Condition | Age-driven deterioration beyond body-adjusted maximum age | Recuperation does not heal age afflictions | OM | b11-62-disease-and-old-age |
| Poison | Condition | Delayed accumulating damage; also reduces Precision since 6.30 | Poison resistance, recovery, battle duration | OM, OP | b11-65-poison-burning-bleeding-frozen-and-corrosion |
| Burning, Bleeding, or Frozen | Condition | Persistent battle impairment or damage | Relevant immunity or resistance; Spiritform protected in 6.30 | OP, UI | b11-65-poison-burning-bleeding-frozen-and-corrosion |
| Stun, Paralysis, or Sleep | Condition | Denies actions | Resistance, immunity, recovery time, source removal | OM, MM | b11-66-stun-paralysis-sleep-entanglement-and-confusion |
| Entanglement | Condition | Prevents movement or action until escape | Strength or ability-specific escape; ranged support | OM, MM | b11-66-stun-paralysis-sleep-entanglement-and-confusion |
| Charm or Enslave | Condition | Changes control or ownership | Magic Resistance, immunity, range, killing target or caster | OM, MM | b11-67-charm-enslave-transformation-and-control-loss |
| Transformation | Condition | Replaces body or form | Polyimmune, targeting immunity, form-specific loss | OM, MM | b11-67-charm-enslave-transformation-and-control-loss |
<!-- DATA:END abilities -->

# Part XIII: Retrieval and Audit Tools

## 69. The Unit-Card Translation Sheet

For important commanders, sacreds, summons, and unusual independents, use one compact record:

| Field | Entry |
| --- | --- |
| Ruleset and version | Patch, mod stack, object source |
| Current form | Unit ID or name, mount, alternate shapes |
| Classes | Every displayed or confirmed type tag |
| Leadership need | Normal, magic, undead; capacity and redundancy |
| Movement permissions | Land, water, air, terrain, teleport, sailing |
| Defensive gates | Protection, resistance, Ethereal, Glamour, Luck, recovery |
| Offensive gates | Range, magic weapon, aura, trample, swallow, control |
| Conditional values | Scale, season, dominion, darkness, storm, bless |
| Development | XP, stars, Hall position, heroic ability |
| Current damage | Afflictions, disease, curse, horror mark, age, insanity |
| Evidence | OM, MM, OP, UI, CT, D, TP |
| Links | Canonical Book IV, V, or VI section and object record |

This sheet makes a unit comparable across turns. It also exposes when a conclusion came from a favourable form or environment rather than the permanent object.

## 70. Army Compatibility Audit

Before movement or battle scripting, verify:

1. Every unit has the correct leadership type and capacity.
2. Mindless and non-mindless bodies are not assigned to an illegal shared squad.
3. Water, flight, sailing, teleport, and terrain permissions cover the entire force.
4. Supply demand includes riders and mounts and accounts for animal reductions and Need Not Eat.
5. Darkness, storm, temperature, season, scale, and dominion assumptions match the destination.
6. Recovery routes match actual body classes.
7. Standard distribution uses best-only stacking rather than redundant concentration.
8. Veteran and afflicted units occupy formations appropriate to their current statistics.
9. A leader-loss branch exists for magical beings, undead, demons, and mindless troops.
10. A retreat route exists for every movement mode and plane involved.

## 71. Counter-Construction Matrix

| Enemy gate | First answer family | Secondary check | Frequent false answer |
| --- | --- | --- | --- |
| Ethereal | Magical attacks | Accuracy, damage, other defence layers | More nonmagical elite attacks |
| Glamour or Invisibility | Image-clearing volume and suitable perception | Darkness and target eligibility | Treating every concealment tag as Illusion |
| Awe | Morale, leadership, immunity, range | Attack count and fear support | Raw damage on attackers that never complete attacks |
| Fear | Morale system, mindless where suitable, source removal | Army-rout weight and commander survival | Only increasing individual hit points |
| Regeneration | Burst, disablement, sustained damage above recovery | Affliction resistance and immortality | Slow chip damage into favourable sustain |
| Trample | Comparable size, formation depth, fatigue, or ranged control | Displacement space and mount form | A thin line of high-Defence small units |
| Swallow | Ineligible size, range, rapid swallower removal | Life-saving effects blocked inside | Relying on the swallowed unit's ordinary sustain |
| Auras | Matching resistance, spacing, range, source removal | Duration and density | Buying resistance to only the initial weapon |
| Life Drain | Lifeless screen, range, burst | Weapon type and target selection | Feeding weak living bodies one at a time |
| Mindless army | Kill or disable command, exploit army-rout structure | Redundant leaders | Ordinary morale damage aimed only at troops |
| Immortality | Win position, deny return conditions, soul effects where available | Delay and item loss | Treating one kill as permanent strategic removal |
| Stealth | Patrol coverage and intelligence | Terrain, size, false-army effects | Province Defence alone without patrol plan |
| Seasonal or scale power | Delay, relocate, or change environment | Opponent's ability to restore condition | Evaluating only the favourable unit card |
| Heroic commander | Attack current role and retreat plan | Hidden value formulas unverified | Countering the heroic label instead of the actual bonuses |

## 72. Battle Review Questions

After an unfamiliar interaction, preserve the battle and ask:

- Which tag made the target legal or illegal?
- Which layer acted first: perception, morale, avoidance, protection, resistance, recovery, or return?
- Was the displayed ability innate, item-granted, blessed, spell-granted, mounted, heroic, or environmental?
- Did a condition deny actions even though hit points remained?
- Did leader loss change morale or control?
- Did the battle occur under the expected scales, season, light, storm, and dominion?
- Did the replay show a current patch correction that an older guide lacks?
- Is the conclusion official, directly observed, derived, community-tested, or still pending?

The answer should be recorded at the narrowest reliable level. One battle can show that a particular interaction occurred; it cannot establish every probability or stacking rule.

# Part XIV: Essays

## Essay I: The Icon Is a Rule, Not Decoration

Dominions presents much of its complexity as small symbols and short descriptions. That presentation invites two opposite mistakes. A new player can ignore an icon because the basic statistics look understandable. An experienced player can recognise the icon's name and import a remembered rule from another version. Both mistakes replace the current object with an assumption.

An icon is best understood as a link to a rule family. Undead links a unit to leadership, banishment, disease immunity, recovery restrictions, and targeting. Flying links it to strategic reach, battlefield contact, storms, squad compatibility, and retreat. Recuperation links it to time, affliction cause, body eligibility, and healing difficulty. The symbol is small because the interface cannot print the whole dependency graph on every card.

Mastery does not mean memorising five hundred isolated definitions. It means learning the questions raised by each family. A class icon asks, “what can command and target this body?” A movement icon asks, “who can accompany it and where can it retreat?” A recovery icon asks, “which damage is actually permanent?” An aura asks, “how many bodies remain inside it, and for how many rounds?”

This approach scales. A new icon can be placed into a known family before every edge case is understood. The unknown details remain visible, but the largest category errors can already be avoided.

## Essay II: Overlapping Classes Are the Grammar of Exceptions

Many games assign one creature type and let it explain the whole unit. Dominions instead permits several tags to overlap. This is not clutter. It is the grammar by which the engine expresses exceptions.

Consider an undead magic being. Undead determines banishment, disease, ordinary healing restrictions, and the relevant command precedence. Magic Being creates another targeting identity, but it does not replace the undead command rule. Add Mindless and the morale system changes again. Add Amphibian and the strategic theatre expands. Add Sacred and the same body can receive a blessing. No one adjective is a complete description.

This explains why visual intuition fails so often. A stone statue may be Inanimate, Stone Being, Mindless, Magic Being, Sacred, or only some of them. A ghost may be Spiritform, Ethereal, Undead, Magic Being, Invisible, or a different combination. Art suggests a fiction; tags define the interaction.

For nation design, overlapping classes are also an access problem. The army needs commanders that satisfy the strongest command requirement, magic that can support the body, movement that can transport it, and recovery that matches it. A roster containing individually powerful units can be strategically weak if its class infrastructure is incomplete.

## Essay III: Experience Is Stored Reliability

Experience seems modest because each star adds small numbers. Those numbers sit on contested rolls that occur repeatedly. One Attack point can turn many near misses into hits. One Defence point can prevent many contacts. One Morale point can preserve a formation at the check that would otherwise break it. Encumbrance reduction can delay a critical-hit spiral. Magic Resistance can save the commander on whom the army's leadership depends.

The value is stored because the recruitment price has already been paid. Months, battles, and survived contacts have been converted into a unit that cannot be purchased directly from the queue. This does not make every veteran sacred. Afflictions can consume the role that the stars improved, and a victory deadline can make preservation irrational. It does mean that replacement should compare current function rather than printed recruitment cost.

Veteran management is a form of capital allocation. Elite squads can be rotated away from low-value attrition, assigned to the contact where their thresholds matter, or preserved for siege relief. Experienced commanders can become better leaders and researchers. An army that treats every survivor as interchangeable throws away a resource recorded by the interface but not priced by the treasury.

## Essay IV: Conditions Turn Battles into Logistics

A battle report that ends with surviving units can conceal a strategic defeat. Disease, lost limbs, chest wounds, curses, horror marks, and insanity follow the survivors into later turns. Poison or fatigue may have decided who escaped. A unit that won while receiving a cursed item injury may remain damaged until equipment changes. A recuperating army may need months and a safe province before it becomes the same army again.

Conditions connect the battlefield to logistics. They create treatment routes, replacement decisions, staging requirements, and deadlines. Different bodies need different forms of repair. Living healers cannot mend every construct or ghost. Recuperation cannot undo old age. Immortality may restore the body while still losing the month's position and tempo.

The useful measure of victory is not bodies left on the final frame. It is force available for the next necessary action. Book IV explains how the damage occurred; Book XI explains why the icons remaining afterward are part of the campaign state.

## Essay V: Evidence Boundaries Are Part of Expert Play

Dominions rewards exact knowledge, but an old formula printed confidently can imitate exactness. Heroic abilities are the clearest example. Community reverse engineering offers detailed scoring and growth models that are far more useful than vague folklore. The official manual confirms only the broad Hall-of-Fame process, and much of the detailed public work predates Dominions 6.

The correct response is neither to discard the investigation nor to publish it as current law. It is to label the layer. Official rules support the stable core. Current patch notes correct superseded behaviour. Community work supplies hypotheses and often excellent working estimates. Controlled tests decide the interactions that matter enough to verify.

This boundary improves play. A plan based on an official permission can be treated as reliable. A plan based on a community probability needs a failure branch. A plan based on a hidden heroic growth formula should not risk a campaign unless the current displayed value already justifies it. Uncertainty becomes an operational input rather than an embarrassment concealed by prose.

# Part XV: Version Notes, Open Questions, and Sources

## 73. Current Ability-Facing Patch Notes

| Version | Current correction relevant to this book |
| --- | --- |
| 6.36 | Swimming mounts suffice for river crossing; a tavern-charmed knight's mount changes side; repeated mounted-commander recruitment no longer creates the corrected removal charge; Gift of Water Breathing can protect against Lost Land. |
| 6.35 | Innate spellcasters no longer skip the script after temporary unconsciousness; units that automatically regain mounts do so at end of turn; a bodyguard exploit was fixed; supply use updates when items change; Enchanted Blood prints its Magic Resistance bonus; teleport-moving commanders can leave besieged forts. |
| 6.31 | Regeneration uses the exact displayed percentage rather than old percentage brackets. |
| 6.30 | Poison also reduces Precision; Spiritform rather than Ethereal prevents bleeding, frozen, and burning; mounted commanders gained strategic movement changes; gods and prophets cannot fail the ordinary retreat morale roll. |
| 6.27 | Disease Resistance protects against disease spells, including Plague; Enchanted Blood was added as a monster and item command. |
| 6.25 | Praise was added as an ability; battle version display was added for evidence capture. |
| 6.23 | Fear and several battle interactions were corrected; current combat details remain canonical in Book IV. |
| 6.14 | HP-stat handling for experience was corrected immediately after the veteran-HP change. |
| 6.13 | Experience now grants +1 HP for every star at three stars and above. |

Patch notes are a correction layer, not a replacement for the manual. Records should name the version in which a behaviour changed and retain the older rule only when it helps diagnose historical guides or saved games.

## 74. Open Verification Queue

| Priority | Question | Reliable resolution route | Publication status |
| --- | --- | --- | --- |
| Completed | Does a current five-star unit receive cumulative +2 or +3 Hit Points from experience? | Official 6.13 and 6.14 corrections plus the current manual table | Resolved as cumulative +3 HP; +2 retained only as pre-change historical evidence |
| P1 | Which Hall-of-Fame scoring and heroic-growth formulas remain unchanged in 6.36? | Reproducible current tests or engine-backed reverse engineering using the Edition 28 observation template | In progress; official boundary and controlled series defined, formulas withheld |
| Completed | How do current perception abilities divide Glamour, Invisibility, Unseen, Illusion, and Spiritform targets? | Current official 6.36 definitions plus pinned current descriptions; narrower runtime edges split to R-058 | Category division resolved without treating the effects as synonyms |
| P1 | Which ability sources stack, use best-only, or replace one another across form, item, bless, and spell? | Targeted tests and live descriptions | In progress; Standard, Inspiring Researcher, experience, Horror Mark, and the Blur/Displacement/Invisibility group classified |
| P1 | Do Spirit Sight or blindness alter innate Glamour's Mirror Image resolution, and which non-scout information channels reveal Glamour units in friendly provinces? | Reproduce the two explicit official strategic channels, then run the controlled 6.36 battle and information matrix in the Edition 29 working paper | In progress as R-058; Arcoscephale dominion scrying and The Eyes of God have narrow official answers, while the battle edges and generic channels remain open |
| P2 | What are the exact current passive XP exceptions for Mindless units and special sites or items? | Controlled monthly observation and current data export | Official general gain and battle sources published |
| P2 | Which condition immunities follow from each technical class versus a separate hidden tag? | Current object export plus controlled spell matrix | Only explicit official relationships published |
| P2 | How do mount loss, Reclaim Mount, automatic return, and shape changes transfer experience and conditions? | Controlled mounted commander series under 6.36 | Cross-link and patch note only |

## 75. Source Record

### Official sources

- [Illwinter's Dominions 6 documentation page](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual, revision 2](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Modding Manual, version 6.36](https://www.illwinter.com/dom6/dom6modman.pdf)
- [Official Dominions 6 announcements and change notes](https://steamcommunity.com/app/2511500/announcements/)

### Community references

- [Illwiki: Dominions 6 unit abilities](https://illwiki.com/dom5/dom6/unit-abilities)
- [Illwiki: Dominions 6 experience](https://illwiki.com/dom5/dom6/experience)
- [Illwiki: Hall of Fame reverse engineering](https://illwiki.com/dom5/hall-of-fame)
- [Dominions 6 Heroic Quickness discussion](https://steamcommunity.com/app/2511500/discussions/0/4139438760462545927/)

The community sources are retained for taxonomy, test leads, and older reverse engineering. They do not override the current official manual, patch notes, or a reproducible 6.36 result.

### Edition 28 Perception Evidence Record

- ruleset: unmodded Dominions 6.36;
- verified: 30 August 2026;
- official main manual revision 2 SHA-256: `65f430fd97c9f27285d63b797b43bc7fe3844241fdf40230b1d25a901ab9f33f`;
- official Modding Manual 6.36 SHA-256: `9d4a7d2c5101679de7080455ceebed41b25a1e9beba275985e293183269399cf`;
- current-description layer: pinned 6.35 Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`;
- patch check: official 6.36 announcement reviewed; no perception-family correction found;
- unresolved runtime edge: R-058 only.

## 76. Closing Reference

A complete unit reading has six layers:

`class -> command -> movement -> ability -> development -> condition`

Skipping a layer turns an apparent rule into a surprise. Reading all six turns the unit card into a compact map of permissions, gates, risks, and stored value. That method is the foundation on which later nation dossiers, object records, calculators, and matchup essays can be built without restating the same five hundred definitions every time.
