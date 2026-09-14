# Foundation Book VIII: Modding and Scenario Design

## Building Reliable Dominions 6 Rulesets, Events, AI Scaffolds, and Worlds

## The job of this volume

Dominions 6 modding begins with text commands, but reliable modding is not primarily a matter of remembering commands. It is a matter of controlling state.

A mod changes a shared registry of weapons, armour, monsters, sites, nations, spells, items, population types, mercenaries, AI templates, and events. Those objects refer to one another. Several mods may alter the same object. Updates can change legal commands or object numbers. Events retain codes and variables across turns. Maps establish the topology on which every strategic system operates.

The job is larger than writing a `.dm` file. A dependable project must answer:

- which game version and manual revision define the rules;
- which object is being selected;
- which attributes are inherited, cleared, or overwritten;
- when the parser processes each category;
- which identifiers belong to the project;
- how multiple mods interact;
- what changes are safe for an ongoing game;
- what the AI can be encouraged to do;
- what requires an event system rather than an AI command;
- how a map changes strategic value before a nation is chosen;
- how every claim will be checked.

Book VIII begins with the smallest safe patch, then moves through events, maps, AI hints, compatibility work, and release testing. Illwinter's manuals remain the authority for commands. The aim here is to show how individual commands become a mod that survives other mods, game updates, and actual play.

## Technical baseline

**Game baseline:** Dominions 6.36.  
**Official Modding Manual:** version 6.34, 65 pages.  
**Official Event Modding Manual:** labelled version 6.29, 20 pages.  
**Official Map Making Manual:** version 6.26, 11 pages.  
**Official File Formats document:** current one-page `d6m` specification.  
**Source case studies:** Dominions Enhanced 2.16 and Divinitus 1.15.3 DE.  
**Intended combined order:** Dominions Enhanced first, Divinitus DE second.  
**Last verified:** 31 July 2026.

The manuals do not all carry the same version number, and that is not an error in the archive. The official documentation page currently distributes a 6.34 modding manual, a 6.29-labelled event manual, and a 6.26 map manual while the public game is 6.36. Patch notes published after those revisions form part of the technical baseline. Book XIV marks five event commands introduced in 6.36 as official patch-only because the announcement does not supply their full syntax.

Book I's evidence labels remain in force. Source syntax appears only when the command itself matters; the surrounding explanation is independent of the manuals.

## Suggested paths

The first-mod path runs from the parser model through project structure, selection, copying, clearing, error isolation, and validation. Content creators can then move into objects, nations, spells, items, and blessings. Event and diplomacy work begins with state, eligibility, codes, variables, targets, and anti-loop safeguards. Mapmakers can go directly to topology and scenario packaging, while compatibility work depends on the parser chapters, identifier registries, object reconstruction, and regression testing. Book IX now holds the detailed DE and Divinitus case study.

# Part I: The Object-and-Parser Model

## The most useful mental model

A `.dm` file is a sequence of instructions that changes a collection of global object tables. It is not a complete database and it is not a conventional program with private objects.

The basic unit of work is a stateful block:

```text
#select... or #new...
commands that alter the active object
#end
```

The selector establishes the active object. Commands after it belong to that object until `#end`. A missing selector, a missing `#end`, an accidental `#clear`, or an unexpected later mod can change the meaning of an otherwise correct line.

Five operations explain most mod source:

| Operation | Purpose | Principal risk |
| --- | --- | --- |
| Select | Open an existing object for alteration | Wrong name or number |
| Create | Allocate a new object | Collision or unstable automatic number |
| Copy | Inherit an existing object's properties | Hidden attributes come with the copy |
| Clear | Remove some or all inherited properties | Required defaults vanish |
| Set | Replace or add a property | Later source may overwrite it |

The central expert question is not, “What commands appear in this block?” It is, “What is the final object after every inherited value, clear operation, setter, parser phase, and later mod has been applied?”

## Commands are stateful

Consider the pattern:

```text
#selectmonster 311
#gcost 180
#poorleader
#end
```

This does not define a new monster. It alters monster 311. Attributes not addressed by the block continue to come from the base game or an earlier mod. The resulting monster is the old object plus the specified changes.

Now consider:

```text
#newmonster 7200
#copystats 311
#name "Example Adept"
#gcost 200
#end
```

This creates a new identity, inherits a source object's characteristics, and then changes selected fields. The copy is economical, but it also carries properties that may be easy to overlook: leadership, item slots, movement, age, path cost, recruitment limits, stealth, shape relationships, and hidden flags can all matter.

The safe method is:

1. name the source object and version;
2. state why it is being copied;
3. list inherited systems that must be audited;
4. override deliberately;
5. inspect the final in-game detail card;
6. test any behaviour not visible on the card.

## Text order and parser order are different

Within each mod, Dominions processes object categories in a fixed order:

| Parser phase | Category |
| ---: | --- |
| 1 | Mod information |
| 2 | Weapons |
| 3 | Armour |
| 4 | Units and monsters |
| 5 | Names |
| 6 | Blessings |
| 7 | Sites |
| 8 | Nations |
| 9 | Spells |
| 10 | Magic items |
| 11 | General rules |
| 12 | Population types |
| 13 | Mercenaries |
| 14 | Events |

This has two consequences.

First, physical placement in the file does not create an ordinary top-to-bottom dependency between categories. A weapon definition may be written after a monster block in the text, yet the weapon phase is processed before the monster phase.

Second, entire mods are loaded separately. One mod is processed through its phases, then another mod is processed. A reference by name to an object created in another mod is not reliable merely because the other mod is listed first. The official manual warns that cross-mod name references cannot be trusted.

For compatibility work:

- use numbers when a known shared identity is intentionally targeted;
- avoid assuming that another mod's names form a stable public interface;
- treat two mods altering the same object as a conflict requiring inspection;
- record combined load order;
- reconstruct the final object rather than describing either source in isolation.

## Overlap does not create a clean merge contract

It is tempting to assume that two mods “merge” because each changes different fields on the same monster. Sometimes the observed final object resembles such a merge. That is not a safe general contract.

The official warning is stronger: two mods should not try to modify the same thing because the result may be unpredictable. A dependable compatibility patch cannot rely on accidental non-overlap. It explicitly reasserts the intended final state after both parent mods.

The source-level rule is:

```text
shared selector
-> enumerate every parent modification
-> identify clears and copies
-> determine final setters
-> create explicit compatibility block
-> verify final object
```

## Names are convenient; numbers are identities

Many selectors accept either a quoted name or a numeric identifier. Names are readable, but they are not always unique and can be changed. Numbers are less readable, but they identify a specific registry entry.

Use names when:

- working entirely within one self-contained project;
- the object is a stable base-game object with a unique name;
- readability outweighs cross-mod coupling;
- a command only accepts a name.

Use numbers when:

- diagnosing an existing unit through `ctrl+i`;
- modifying a known base-game identity;
- two objects share a name;
- creating explicit monsters, sites, weapons, or armour;
- a compatibility patch deliberately targets another mod's object.

Always comment numbers:

```text
#selectmonster 311 -- Mystic, MA Arcoscephale
```

A number without provenance becomes technical debt.

## Bitmasks are sets represented as integers

A bitmask combines several independent flags by addition. It should be read as a set, not as an unexplained large number.

For a custom magic random, the documented path-mask values begin:

| Path | Mask |
| --- | ---: |
| Fire | 128 |
| Air | 256 |
| Water | 512 |
| Earth | 1024 |
| Astral | 2048 |
| Death | 4096 |
| Nature | 8192 |
| Glamour | 16384 |
| Blood | 32768 |
| Priest | 65536 |

Thus `384` is `128 + 256`, meaning a Fire-or-Air random. The source should retain the decomposition:

```text
#custommagic 384 100 -- F/A, one guaranteed pick
```

For every bitmask:

- keep the human-readable components in a comment;
- do not reuse a terrain bitmask in a site command;
- do not assume similarly named masks share values across manuals;
- calculate the sum twice or generate it from a small table;
- inspect the result in game.

The Map Making Manual explicitly warns that its terrain masks are not the same as the terrain masks used for site modding.

## Object numbers and the manual's internal boundaries

The final “Modding Number Limits” table in the 6.34 manual gives:

| Object | Total documented range | Recommended mod range |
| --- | ---: | ---: |
| Sound | 0-248 | 150+ |
| Weapon | 0-3999 | 1000+ |
| Armour | 0-1999 | 400+ |
| Monster | 0-19999 | 5000+ |
| Nametype | 100-399 | 170+ |
| Spell | 0-7999 | 2000+ |
| Enchantment | 0-9999 | 200+ |
| Item | 0-1999 | 700+ |
| Magic site | 0-3999 | 1700+ |
| Nation | 0-499 | 150+ |
| Population type | 0-249 | 125+ |

The same manual contains older-looking local limits in individual sections. Examples include monsters described as 5000-8999, armour as 300-999, spells as 1300-3999, and items as beginning at 400. These statements cannot all describe the same final ceiling.

The evidence-based policy for 6.36 is:

- treat the final consolidated limits table as the current broad capacity;
- recognize that older projects may occupy lower legacy mod ranges;
- allocate from a written project registry rather than “the next number that looks free”;
- prefer the narrower historical range when broad portability matters;
- verify numbers above an older local ceiling in the target game version;
- do not silently rewrite another mod's allocation.

Dominions Enhanced demonstrates that current mods can use monster numbers above 8999. That source evidence resolves current parser capacity for the supplied ruleset, but it does not remove collision risk.

## Automatic allocation is convenient but fragile

Some `#new...` commands accept explicit numbers; others allocate automatically.

| Object | Explicit identity available in documented command? | Safe update policy |
| --- | --- | --- |
| Weapon | Yes | Allocate from project registry |
| Armour | Yes | Allocate from project registry |
| Monster | Optional explicit number | Use explicit number |
| Site | Optional explicit number | Use explicit number |
| Nation | Automatic free nation number | Avoid relying on order outside project |
| Spell | Automatic | Append-only or reserved placeholders |
| Item | Automatic | Append-only or reserved placeholders |

The official manual specifically warns that inserting new automatically numbered monsters, sites, or spells into the middle of a released mod can change later identities and break ongoing games. Explicit numbering solves part of the problem. For automatically allocated categories, the practical protection is:

- append new objects;
- never reorder released objects casually;
- reserve inert placeholders when future expansion is likely;
- record generated identities from `ctrl+i`;
- make save compatibility an explicit release decision.

## A mod can change an ongoing game

When the source used by a saved game changes, object modifications can apply when the game is loaded again. Existing militia can acquire a changed weapon; existing commanders can acquire new statistics. This is useful for testing and dangerous for releases.

Changes fall into three classes:

| Class | Example | Ongoing-game risk |
| --- | --- | --- |
| Presentation | Description correction | Usually low |
| Existing-object mutation | Cost, weapon, path, shape, spell effect | Immediate and potentially strategic |
| Registry mutation | Inserted new monster, spell, site, or item | Identity shift and possible corruption |

Every release should state one of:

- safe for new games only;
- expected to be compatible with existing games;
- compatibility not guaranteed;
- migration release with exact host instructions.

# Part II: Project Structure and the First Working Mod

## Locating the user data directory

The safest method is the in-game **Game Tools -> Open User Data Directory** action. Default locations are:

| Platform | Default user data directory |
| --- | --- |
| Windows | `%APPDATA%\dominions6\` |
| Linux | `~/.dominions6/` |
| macOS | `~/.dominions6/` |

Relevant subdirectories include:

- `mods`
- `maps`
- `savedgames`

The in-game button should take precedence over assumptions about operating-system paths.

## The Dominions 6 mod folder rule

Every mod must reside in its own folder. The folder and `.dm` file should share a simple filename:

```text
mods/
  example_balance/
    example_balance.dm
    banner.png
    sprites/
      example_unit.png
```

The 6.34 manual requires the `.dm` file to be inside a folder with the same name, excluding the extension. Files used by the mod should remain within that folder or its subdirectories.

Network-safe filenames:

- contain no spaces;
- avoid special characters;
- use consistent case;
- use forward slashes inside mod references, including on Windows.

Case matters for mod and image filenames.

## Image and sound formats

Mod graphics may use PNG or Targa images. Targa files must be uncompressed or RLE and use 24- or 32-bit colour. For 24-bit Targa graphics, the manual describes black as transparent and magenta as a half-transparent shadow colour.

The dedicated mod banner used by `#icon` should be 128x32 or 256x64 pixels.

Sound sources use:

- `.sw`: mono, signed 16-bit, 22 kHz;
- `.sw2`: stereo, signed 16-bit, 22 kHz.

Sound effects should be mono. Music may use either form. New sound slots are documented from 150 upward, with 248 as the maximum.

## The minimum useful metadata block

```text
#modname "Example Balance Patch"
#description "Small, versioned adjustments for Dominions 6.36."
#version 0.10
#domversion 6.36
```

`#icon` is optional. `#domversion` is also optional, but it is valuable once the project depends on commands or fixes added after release.

A good description states:

- what the mod changes;
- which game version it targets;
- whether it requires another mod;
- required load order;
- whether it is intended for new games only.

## The smallest safe first project

The first project should modify one visible property of one existing object. It should not begin with a new nation, a multi-stage event chain, or a custom global enchantment.

Example:

```text
#modname "Mystic Cost Test"
#description "Controlled test for MA Arcoscephale Mystic cost."
#version 0.01
#domversion 6.35

#selectmonster 311 -- Mystic
#gcost 185
#end

```

The trailing blank line is deliberate. Current community troubleshooting repeatedly identifies a missing final newline as a cause of the last command, often `#end`, not being parsed. This behaviour is not stated in the official 6.34 manual, so it remains a community-tested compatibility precaution. It is cheap and should be standard.

Verification:

1. enable only the test mod;
2. start a fresh MA Arcoscephale game;
3. inspect the Mystic's recruitment card;
4. press `ctrl+i` where useful;
5. confirm no unrelated property changed;
6. disable the mod and confirm the baseline returns.

## The patch-before-creation progression

A safe learning ladder is:

1. change an existing monster's gold cost;
2. change an existing weapon's damage;
3. copy a monster into a new fixed ID;
4. give the copy a copied or existing weapon;
5. add the new monster to one nation's recruitment;
6. create one site that recruits it;
7. create one spell or item;
8. create one bounded event;
9. build a complete nation;
10. add compatibility and AI layers.

Each step introduces one new category of failure.

## Selector discipline

Every block should visibly contain:

- selector or creator;
- identity comment;
- copy or clear operation, if any;
- grouped setters;
- `#end`;
- blank separation from the next block.

Example:

```text
-- Unit 7200: Bronze Sentinel
#newmonster 7200
#copystats 118 -- chosen source recorded in registry
#name "Bronze Sentinel"
#clearweapons
#weapon 8 -- Broad Sword
#gcost 22
#rcost 2
#end
```

The comment does not change behaviour. It preserves the reason behind a number.

## Copy-first and clear-first are different designs

### Copy-first

Copy-first preserves a coherent base object:

```text
#newmonster 7201
#copystats 311
#name "Senior Mystic"
#magicskill 4 2
#gcost 260
#end
```

Advantages:

- fast;
- inherits functional defaults;
- good for variants.

Risks:

- inherits hidden or irrelevant properties;
- a parent modification can change the copy's starting point;
- can produce accidental Pretender, recruitment, leadership, or shape behaviour.

### Clear-first

Clear-first creates a more explicit object:

```text
#newmonster 7202
#clear
#name "Test Construct"
#hp 20
#size 4
#str 16
#att 10
#def 8
#prec 8
#mr 14
#mor 30
#mapmove 12
#ap 10
#end
```

Advantages:

- makes the intended state visible;
- reduces inherited surprises.

Risks:

- easy to omit a required or sensible default;
- more work;
- may produce a technically valid but unusable object.

Use copy-first for a close variant and clear-first for a genuinely new body. In both cases the final card, movement, recruitment, leadership, and combat behaviour must be checked.

## Error isolation

When a mod fails to appear or load:

1. verify it is inside its own correctly named folder;
2. verify the file extension is really `.dm`, not `.dm.txt`;
3. verify `#modname`;
4. remove or comment out `#icon`;
5. confirm filenames contain no spaces or special characters;
6. confirm case and forward slashes;
7. confirm every stateful block ends;
8. add a final blank line;
9. reduce the source to metadata plus one known-safe block;
10. restore sections by binary search.

Binary search is faster than rereading a five-thousand-line file:

- disable half the source;
- load;
- choose the failing half;
- repeat until the minimal failing block remains.

When the mod loads but an object does not appear:

- inspect its selector and number;
- check recruitment or site assignment;
- check era and nation;
- for Pretenders, check Pretender-defining attributes and nation or home-realm assignment;
- check whether a later mod clears recruitment or gods;
- inspect the combined final object, not only the definition.

## Reloading source during development

Officially, changing a mod can affect a saved test game. If Dominions remains open, the documented reload method is:

1. load a game using different mods or no mods;
2. return to the main menu;
3. load the test game again.

This forces the target mod to reload. For registry changes and anything involving new game setup, a fresh game is still the safer test.

# Part III: Weapons, Armour, and Combat Effects

## Design from combat role

A weapon is not balanced by damage alone. Relevant dimensions include:

- number of attacks;
- attack and defence modifiers;
- length;
- strength contribution;
- damage type;
- armour interaction;
- magic and resistance flags;
- range, precision contribution, and ammunition;
- secondary effects;
- clouds and after-effects;
- interactions with size, morale, defence, or magic resistance.

A unit carrying a weapon adds another layer:

- wielder strength and attack;
- number of arms;
- ambidexterity;
- fatigue and encumbrance;
- formation density;
- recruitment cost;
- mount attacks;
- blesses and battlefield buffs.

Balance the delivered attack package, not the isolated weapon card.

## Selecting and creating weapons

Core patterns:

```text
#selectweapon 8
...changes...
#end
```

```text
#newweapon 1200
#name "Test Falx"
#dmg 8
#att 1
#def -1
#len 2
#slash
#armorpiercing
#sound 8
#end
```

For new weapons:

- allocate an explicit ID;
- set the name first;
- use `#copyweapon` first when inheriting;
- remember that `#clear` removes the copied properties;
- use `#range` only when the weapon is meant to become missile-only;
- inspect all derived text in game.

## Damage and armour interaction

The important distinction goes beyond physical versus magical.

| Layer | Examples |
| --- | --- |
| Damage family | Slash, pierce, blunt, fire, cold, shock, poison, fatigue |
| Armour rule | Normal, armour piercing, armour negating |
| Resistance rule | Resistance applies, MR negates, size or strength interaction |
| Delivery | Melee, missile, area, beam, cloud, after-effect |
| Conditional effect | On hit, on damage, against demon, undead, magic being, or illusion |

A high base-damage attack with ordinary armour interaction may be a poor anti-elite tool. A lower attack with armour negation can invalidate protection. An after-effect may bypass the intended counter class. Every weapon design should state the defence class it is intended to defeat.

## Range and ammunition

`#range` converts a weapon into a missile weapon that cannot be used in melee. `#ammo` controls the ordinary shot count; current patch notes also record later support for fatigue-based ammunition behaviour.

Missile testing should record:

- actual maximum range;
- precision at several distances;
- firing cadence;
- ammunition exhaustion;
- behaviour after ammunition;
- friendly fire and area;
- interaction with shields and Air Shield;
- underwater legality;
- spell-created versus recruited use.

## Secondary and after-effects

Weapon after-effects can create some of the most severe balance errors because one attack can deliver several independent tests.

For each effect, record:

- trigger: swing, hit, or damage;
- target: original square, target, wielder, area, or cloud;
- defence: armour, resistance, MR, size, strength, or none;
- stacking behaviour;
- duration;
- whether a killed target still produces the effect;
- whether a mount, rider, secondary shape, or illusion is separately affected.

Official updates have repeatedly fixed weapon and cloud edge cases. Patch history is part of a weapon's evidence, not background trivia.

## Armour and barding

Armour types documented by the manual include:

| Type value | Use |
| ---: | --- |
| 4 | Shield |
| 5 | Body armour |
| 6 | Helmet |
| 9 | Barding |

New armour uses an explicit number. The consolidated current mod range begins at 400, while the local armour section still mentions a legacy starting point of 300. A project registry should use a range that does not overlap enabled mods.

Armour evaluation includes:

- protection by body location;
- defence penalty;
- encumbrance;
- resource cost;
- magic-item consequences;
- mounted interaction;
- whether a form retains legal slots;
- whether copied armour contains unexpected type or sprite data.

## Combat-effect audit

Before releasing a weapon or armour change:

| Test | Minimum comparison |
| --- | --- |
| Baseline damage | Unarmoured human |
| Armour performance | Light, medium, and heavy protection |
| Defence interaction | Low and high Defence Skill |
| Size interaction | Human and giant |
| Resistance | Relevant resistance 0, partial, and high |
| Mount interaction | Rider hit and mount hit |
| Shape interaction | Primary and secondary form |
| Buff interaction | Strength, weapon, protection, and resistance buffs |
| Scale | One attacker and massed formation |

The purpose is not to prove that a weapon can kill. It is to identify which battlefield class it makes obsolete.

# Part IV: Monsters, Mounts, Shapes, and Commanders

## A monster is a bundle of systems

“Monster” is the modding category for ordinary troops, commanders, mages, heroes, Pretenders, mounts, animals, constructs, undead, and many summoned beings.

A complete monster audit covers:

1. identity and visuals;
2. body statistics;
3. weapons and armour;
4. item slots;
5. movement;
6. creature type and tags;
7. leadership;
8. magic;
9. recruitment rules and costs;
10. shape and mount relationships;
11. special abilities;
12. AI recruitment instructions;
13. death, rebirth, and transformation behaviour.

## Base statistics are not independent

Changing Size can affect:

- square occupancy;
- repel and weapon length interactions;
- trampling eligibility;
- strength and hit expectations;
- mount and rider geometry;
- item and shape assumptions.

Changing action points affects how rapidly a unit crosses a battlefield and may interact with weapon timing. Changing encumbrance affects fatigue, which in turn changes Defence Skill, attack performance, spellcasting, and eventual collapse. Changing morale affects rout timing and formation stability.

The final role must be tested as a system.

## Cost has three distinct channels

Monster cost is not one number:

- **gold cost** controls treasury and upkeep;
- **resource cost** reflects base body plus equipment;
- **recruitment-point cost** controls throughput.

A unit can be cheap in gold but impossible to mass from one fort because of recruitment points. A mage can be affordable but consume several commander points. A heavily equipped unit may be limited by resources even when gold is abundant.

Cost doctrine:

- compare per fort-turn, not only per unit;
- include upkeep;
- include commander support;
- include resource scales and terrain;
- compare battlefield role against the nearest national alternative;
- test massed availability.

## Automatic gold-cost calculation

Dominions can calculate parts of monster cost from attributes. Manual cost setters and automatic components can interact. A displayed final recruitment price is more authoritative than a single source line.

When modifying a copied unit:

- record the displayed parent price;
- record every cost-related source command;
- record the displayed child price;
- do not label an isolated `#gcost` argument as the final cost without inspection.

This rule was necessary in the Arcoscephale DE dossier, where copied or selected objects could not be safely summarized from one cost line.

## Recruitment flags are strategic rules

Recruitment commands can constrain a monster by:

- capital status;
- terrain;
- fort or no fort;
- coast or sea;
- season;
- commander points;
- recruitment points;
- holy or sacred limits;
- nation lists and sites.

The unit card does not by itself answer where and how often the unit can be produced. Nation and site source must also be read.

## Leadership is typed

Normal, magic, and undead leadership are separate capacities. Morale modifiers, taskmaster-like abilities, formation permissions, and undisciplined-unit control can alter the practical command package.

For each commander, test:

- maximum normal troops;
- maximum magic beings;
- maximum undead;
- squad morale effect;
- formation options;
- bodyguard capacity;
- movement of the slowest assigned unit;
- behaviour after shapechange or dismount.

## Magic paths and randoms

Fixed paths use path numbers:

| Number | Path |
| ---: | --- |
| 0 | Fire |
| 1 | Air |
| 2 | Water |
| 3 | Earth |
| 4 | Astral |
| 5 | Death |
| 6 | Nature |
| 7 | Glamour |
| 8 | Blood |
| 9 | Priest |
| 50 | Random |
| 51 | Elemental |
| 52 | Sorcery |
| 53 | All |

`#magicskill` assigns a fixed path. Holy magic also requires the monster to be made a priest through the appropriate priest attribute.

`#custommagic` uses path masks and a percentage. Multiple `#custommagic` lines represent multiple rolls. They do not automatically describe one combined roll.

For every random mage:

- write each roll separately;
- state whether its chance is 100%, 50%, 10%, or another value;
- identify which paths share one mask;
- calculate threshold probability;
- check impossible combinations;
- distinguish source probability from observed distribution.

The manual warns that a custom random containing only Priest can crash the mod. Random holy levels should not be used casually.

## Ritual mastery and range

`#masterrit` changes effective paths for ritual casting without simply granting an ordinary path level. Path-specific range commands increase ritual reach by provinces and battlefield range in percentage steps.

These abilities can create access that an ordinary path list misses. A mage audit asks:

- displayed path;
- effective ritual path;
- range modifiers;
- research bonus;
- gem production;
- path boosts;
- item restrictions;
- automatic spells;
- communion or chorus role.

## Mounts are separate monsters

Dominions 6 models the mount separately from the rider. A mounted design may involve:

- rider monster;
- mount monster;
- mount assignment;
- rider placement;
- mount statistics;
- mount weapons;
- barding;
- size and item-slot interaction;
- dismounted continuation;
- remount or mount-regeneration behaviour.

A mounted unit can fail in several distinct ways:

- the mount dies and leaves a functioning rider;
- the rider dies while the mount is hit separately;
- an area effect hits both;
- a gateway or movement effect interacts with the mounted state;
- a shapechange loses or duplicates mount state;
- event-created unique riders behave differently.

Patch notes have repeatedly addressed mounted crashes and inconsistencies. Mounted content needs its own regression suite.

## Shape relationships form graphs

Shapechanging changes far more than the sprite. It can affect:

- statistics;
- magic;
- items and disabled slots;
- age;
- afflictions;
- mount state;
- death and rebirth;
- battle-only changes;
- seasonal changes;
- bug or swarm forms;
- Pretender recognition.

Represent the relationship as a graph:

```text
strategic form
-> battle form
-> wounded or death form
-> restored form
```

Then test each edge and what state survives it:

- experience;
- afflictions;
- heroic ability;
- prophet status;
- magic paths and boosts;
- items;
- name;
- orders;
- mount;
- event target eligibility.

The Arcoscephale Grand Hierophant case demonstrates why this matters: an event transforms an ordinary Mystic into a Mystic Prophet and later events may boost that transformed object. The relevant question is not only which unit appears, but which state is preserved through transformation.

## Pretender qualification

A monster does not become an available Pretender merely because it has impressive statistics. Relevant design elements include:

- starting dominion;
- new-path cost;
- initial paths;
- chassis status and slots;
- home realm;
- explicit addition to nation god lists;
- awakening restrictions;
- nation availability.

When a custom Pretender exists but does not appear:

- verify Pretender-defining attributes;
- verify home realm;
- verify `#addgod` or equivalent national inclusion;
- verify era and nation;
- verify later `#cleargods`;
- verify the final `#end` was parsed.

# Part V: Sites, Nations, and Recruitment Architecture

## Sites are content containers

Magic sites can provide:

- gem income;
- gold, resources, supply, scales, or unrest effects;
- recruitable units and commanders;
- conjuration or ritual access;
- scrying and ritual range;
- path or research effects;
- Throne effects;
- unique national infrastructure.

This makes sites a powerful compatibility technique. A site can add recruitment without rebuilding a nation's ordinary recruit list. It can also scope content to a capital, terrain, or discovered location.

## Site identity and discovery

Sites can be hidden or known. Event requirements distinguish:

- site present;
- discovered;
- hidden;
- nearby;
- claimed or unclaimed Throne;
- free site slots.

An event that adds a site should normally require a free site slot. An event referring to a site by name may require the exact site name embedded in brackets at the end of its message, depending on the command. The Event Manual's bracket convention is easy to miss and should be copied exactly when relevant.

Current official correction: Dominions 6.35 fixed `#revealsite` and `#removesite` so they work when several sites share the same name. Earlier behaviour should not be assumed when reading old reports.

## Nation blocks define conversion rules

A nation is not only a list of troops. It defines:

- name, epithet, era, colours, flag, and description;
- preferred and hated terrain;
- capital and start sites;
- recruitment lists;
- terrain and fort recruitment;
- starting commander and armies;
- province defence;
- forts, laboratories, and temples;
- dominion and scale modifiers;
- Pretender list and realms;
- undead reanimation;
- AI hints;
- national spells and items through references elsewhere.

Changing recruitment can alter the entire national economy.

## `#clearrec` is a major operation

`#clearrec` removes the nation's ordinary recruitable units and commanders, but not its gods. It should be treated like a schema migration.

After clearing, reconstruct:

- ordinary units;
- ordinary commanders;
- fort and foreign recruitment;
- terrain-specific recruitment;
- capital-site recruitment;
- starting commander and troops;
- commander-point coverage;
- scouts and priests;
- siege and leadership access.

Dominions Enhanced uses this kind of recruitment rewrite for MA Arcoscephale. The final roster cannot be inferred from the base game plus a list of new units; it must be rebuilt from the post-clear additions and site recruitment.

## Ordinary, foreign, terrain, fort, and site recruitment

Recruitment sources should be recorded separately:

| Source | Strategic meaning |
| --- | --- |
| Ordinary national recruit | Available through normal national recruitment rules |
| Foreign recruit | Available without a fort where permitted |
| Fort-terrain recruit | Depends on both fort and terrain |
| Site recruit | Depends on owning a specific site |
| Capital-site recruit | Capital-only even if not in ordinary list |
| Event-added recruit | Depends on event state |

A complete nation diff names both the object and its source.

## Starting armies are their own system

Changing `#startcom` removes old starting troops and establishes a new starting-command context. Starting squads and counts must then be restored explicitly.

The manual recommends increasing Dominions 5 starting armies by roughly half when converting to Dominions 6 because army scale increased. This is guidance, not a universal balance formula. The new army must still be tested against current neutral provinces.

## Province defence

Province defence has:

- commanders;
- troop types;
- thresholds;
- quantities per defence points;
- separate underwater definitions.

PD is part of national strategic identity. A cheap raiding unit becomes much stronger if opposing modded nations have brittle PD; an event attack becomes oppressive if it repeatedly strikes a nation with no suitable PD answer.

Test:

- PD 1;
- first threshold;
- second threshold;
- PD 10 and 20;
- commander survival;
- patrol and siege interaction;
- underwater version;
- gold efficiency against common raiders.

## Buildings and infrastructure

National fort, laboratory, and temple commands change:

- construction cost;
- construction time;
- defence;
- recruitment;
- economic conversion;
- research spread;
- dominion spread.

The strategic unit is not “a cheap fort.” It is:

```text
gold and commander turns
-> completed infrastructure
-> recruitment and research throughput
-> defended territory
```

Balance should compare the whole conversion.

## Dominion is a rules engine

Nation modding can change:

- scale limits;
- scale spread;
- automatic effects;
- population and income interactions;
- special dominion;
- bless availability;
- temple and priest behaviour.

Dominion effects can reach every friendly or hostile province, giving them far greater reach than a unit adjustment. Every special dominion should specify:

- eligible provinces;
- dominion threshold;
- frequency;
- stacking;
- effect on allies and enemies;
- event interaction;
- siege behaviour;
- counterplay;
- performance cost.

## Home realms and god lists

Home realms allow Pretenders belonging to a realm to enter a nation's default god pool. A nation can also add or clear gods explicitly.

Compatibility risk:

- one mod adds a Pretender;
- a later nation block clears gods;
- the Pretender remains defined but disappears from selection.

The final nation block determines availability.

## Nation design audit

A new nation is not ready when the roster appears. It is ready when it can complete the game's strategic conversions.

| System | Minimum question |
| --- | --- |
| Expansion | Can at least two coherent parties take normal independents? |
| Leadership | Can starting and recruited armies legally move? |
| Siege | Can the nation take and hold forts? |
| Research | Can it build a functioning research economy? |
| Magic | Are path randoms, gems, and national rituals coherent? |
| Priests | Can it bless, preach, claim, and recover its god? |
| Infrastructure | Do forts, labs, and temples fit costs and roster? |
| Defence | Does PD resist trivial raiding without becoming oppressive? |
| Water | Is water access intentionally absent, partial, or native? |
| AI | Can the AI recruit and research a usable subset? |
| Pretenders | Are several legal strategic families possible? |
| Counterplay | Which common tools defeat its strongest package? |

# Part VI: Spells, Items, Blessings, and Supporting Objects

## Spell design begins with delivery

A spell definition combines:

- name, description, and detail text;
- research school and level;
- one or two path requirements;
- fatigue and gem or blood-slave cost;
- combat or ritual effect;
- damage or effect argument;
- area;
- range and precision;
- number of effects;
- targeting restrictions;
- environmental restrictions;
- global-enchantment identity;
- national access;
- AI preference.

A strategically meaningful spell description must answer:

1. Who can cast it naturally?
2. Who can cast it after ordinary boosters?
3. When does the research arrive?
4. What gem, slave, fatigue, or mage-turn cost is paid?
5. How is the effect delivered?
6. What resists it?
7. What battlefield or map condition invalidates it?
8. Will the AI cast it sensibly?

## Schools and path numbers

Spell schools are:

| Number | School |
| ---: | --- |
| -1 | Not researchable |
| 0 | Conjuration |
| 1 | Alteration |
| 2 | Evocation |
| 3 | Construction |
| 4 | Enchantment |
| 5 | Thaumaturgy |
| 6 | Blood |
| 7 | Divine |

Spell path values are:

| Number | Path |
| ---: | --- |
| -1 | None |
| 0 | Fire |
| 1 | Air |
| 2 | Water |
| 3 | Earth |
| 4 | Astral |
| 5 | Death |
| 6 | Nature |
| 7 | Glamour |
| 8 | Blood |
| 9 | Priest |

The required level applies to the corresponding requirement slot. A two-path spell must set the path and level for each intended slot.

## Fatigue cost also encodes ritual cost

The manual states that each full 100 points of fatigue cost raises the gem or slave requirement by one. Rituals also use `#fatiguecost` to establish their cost.

This makes fatigue a dual-purpose design field:

- in combat, it affects whether and how often the caster can act;
- for rituals, it establishes gem or slave expenditure.

A copied spell can retain an unexpected economic cost even after its effect has been changed.

## Area notation

Spell area supports special values. The manual documents:

- ordinary square counts;
- values above 1000 that scale area with caster level;
- `666` for the entire battlefield;
- special fractional-battlefield values.

Large-area effects must be tested for:

- performance;
- friendly fire;
- resistance density;
- interaction with obstacles;
- repeated casting;
- whether stronger casters scale the area;
- whether an AI preference creates spell spam.

## Effects are an engine interface

`#effect` selects an internal effect family. The manual documents many useful values but explicitly does not present every internal possibility. `ctrl+i` on an existing spell can expose modding information.

The safest creation method is:

1. find a base-game spell with the closest delivery and resolution;
2. copy it;
3. rename before writing the new description;
4. change one dimension at a time;
5. retain a source note identifying the parent;
6. test target selection and resistance;
7. compare battle logs.

Changing a copied spell's name removes its description, so the order of name and description commands matters.

## A spell's access may be more important than its effect

Balance errors frequently come from access:

- research too early;
- path too common;
- gem cost too low;
- battlefield range too long;
- ritual range bypassing borders;
- national restriction omitted;
- item casting bypassing the intended mage requirement;
- communion or path-master interaction;
- AI casting in every marginal situation.

Spell balance should compare total delivery cost:

```text
research + mage recruitment + path access + gems + laboratory + travel + script slot
```

## National and restricted spells

National restriction commands can allow or forbid particular nations. A restriction using the last manipulated nation is convenient inside a self-contained file and fragile when source is reorganized.

For maintainability:

- comment every numeric nation;
- avoid relying on “last manipulated nation” across distant blocks;
- keep nation creation and its restricted content in a controlled order;
- include restrictions in the public spell card audit;
- verify the spell under every intended ruleset.

## Spell AI hints

Three central controls are:

| Command | Function |
| --- | --- |
| `#ainocast` | Prevents ordinary AI selection while allowing a scripted cast |
| `#aibadlvl` | Stops AI selection at or above a specified required path level |
| `#aispellmod` | Raises or lowers AI preference |

The documented `#aispellmod` scale includes:

- `-50`: roughly half as attractive;
- `100`: roughly twice as attractive;
- `-100`: never cast, even if scripted;
- values up to `1000`.

These are hints, not a full targeting language. They cannot make a spell understand a diplomatic plan, reserve gems for a specific future war, or evaluate a bespoke combined-arms doctrine.

AI spell testing needs:

- unscripted independent caster;
- scripted caster;
- high-path caster;
- communion;
- low and high fatigue;
- friendly and hostile target mixes;
- early and late battle;
- routing side;
- gem availability;
- several map contexts for rituals.

## Global enchantments require an event layer

A custom global enchantment is usually a spell plus events that check its enchantment identity.

The structure is:

```text
global ritual
-> enchantment identity becomes active
-> recurring global or provincial events check identity
-> effects occur under bounded requirements
-> events stop when the enchantment disappears
```

This separates the act of casting from the monthly consequences.

Every custom global requires:

- unique enchantment number;
- owner and hostile checks;
- province eligibility;
- per-month cap;
- message policy;
- dispel and replacement behaviour;
- performance estimate;
- end-state test.

## Items are persistent force multipliers

Magic items can change:

- paths and spell access;
- resistances and statistics;
- movement;
- leadership;
- ritual range;
- automatic spells;
- summoning;
- curses and afflictions;
- shape and mount interaction;
- national cost or availability.

Unlike a battlefield spell, an item can persist across many battles and move between commanders. A small numerical bonus may have a large campaign value.

## Item creation and automatic identity

`#newitem` automatically creates an item. The consolidated manual places modded items at 700 and above, while older local text may describe a lower legacy boundary.

The stable-release policy is:

- append items rather than insert;
- record observed item numbers;
- preserve object order;
- reserve placeholders if the project expects expansion;
- test save compatibility after any registry change.

## Construction level has special values

The manual documents ordinary Construction levels and special unforgeable values:

| Value | Meaning |
| ---: | --- |
| 1, 3, 5, 7, 9 | Forgeable tiers |
| 11 | Unforgeable item |
| 13 | Unforgeable unique artifact |
| 15 | Unforgeable unique-per-nation artifact |

Item type and slot must also match the intended user. Barding is a distinct item type and depends on a legal mount slot.

## Item access audit

For every item:

- main and secondary paths;
- Construction tier;
- nominal gem cost;
- forge bonuses and rebates;
- national restrictions;
- slot;
- legal bodies;
- whether it is recoverable after battle;
- whether it is unique;
- whether the AI forges it;
- whether a spell or event creates it;
- whether it grants another ritual or summon.

An item can collapse a path-access ladder. If a nation gains a low-tier booster, every ritual above it must be reconsidered.

## Blessing design

Blessing modding changes the Pretender-design economy and every sacred unit that can receive the effect.

A blessing needs:

- path and point requirements;
- scale requirements;
- incarnate status where relevant;
- effect text;
- interaction with mounts;
- interaction with weapons;
- passive versus blessed-state behaviour;
- AI suitability;
- nation-specific exclusion or access.

Test at least:

- ordinary sacred troop;
- sacred commander;
- sacred mount;
- shapeshifter;
- undead or inanimate sacred;
- ranged sacred;
- communion mage if applicable;
- global enchantment and battlefield-buff interactions.

The nation-level AI hints `#aigoodbless`, `#aicheapholy`, and `#aiholyranged` can encourage an appropriate Pretender family, but they do not evaluate the full roster as a human designer would.

## Names, population types, mercenaries, and general rules

These categories are smaller than monsters or spells but still global.

### Nametypes

Custom nametypes give cultural coherence to commanders. Allocate them from the documented mod range, avoid collision, and verify pluralization and generated forms.

### Population types

Population types affect independent recruitment and the character of a province. They can change the strategic value of terrain, so they need a scenario-wide review.

### Mercenaries

A mercenary band defines:

- arrival tier;
- commander;
- unit type;
- unit count;
- names and price-related behaviour.

Mercenaries are globally available content. A nation-specific balance patch should not create a universally dominant mercenary without intending to alter every game.

### General commands

General modding affects shared game rules. It has the widest compatibility surface. Every general command should be treated as an explicit ruleset dependency and placed in the mod's description and change log.

# Part VII: Event Modding as a State Machine

## Events are advanced modding

Event modding uses the same `.dm` file but adds:

- probabilistic selection;
- province eligibility;
- nation eligibility;
- commander targeting;
- persistent province codes;
- global variables;
- delayed and global execution;
- world effects;
- event chains.

An event is best understood as a state transition:

```text
current game state
+ event eligibility
+ event selection
-> effects
-> new state
```

The source block must answer three questions:

1. When can this event be considered?
2. Who or what does it target?
3. Which persistent state changes after it fires?

## Event anatomy

```text
#newevent
#rarity ...
#req_...
#req_...
#msg "..."
#effect...
#code ...
#end
```

Requirements are combined unless a command explicitly allows several alternatives. Adding more requirements narrows eligibility; it does not necessarily make the event less frequent after eligibility unless rarity or probability also changes.

## Event rarity classes

| Value | Class | Practical use |
| ---: | --- | --- |
| 0 | Always | One ordinary always event per province per month |
| 1 | Common bad | Random bad event pool |
| 2 | Uncommon bad | Rarer bad event |
| 5 | Always, unlimited | Several can occur in one province; use carefully |
| -1 | Common good | Random good event pool |
| -2 | Uncommon good | Rarer good event |
| 10 | Always global | Planned global processing |
| 11 | Common global | Global random event |
| 12 | Uncommon global | Rarer global event |
| 13 | Always immediate global | Immediate global processing |

The official manual states that most global events are planned seven months before execution so fortune tellers can foresee them. Rarity 13 is immediate.

Rarity 5 is powerful and dangerous. An unrestricted rarity-5 event can be considered across many provinces every month and can create event storms or hosting cost.

## Probability is conditional

`#req_rare 20` does not mean a 20% monthly chance for a nation in isolation. It means the event has a 20% validity chance when considered, after the event system and other requirements bring it into scope.

Similarly:

```text
#req_domchance 5
```

multiplies eligibility by dominion strength: at **c** candles the documented chance factor is **5c%**, provided the event would otherwise occur.

Probability statements should specify:

- event rarity;
- eligible province count;
- per-month limits;
- dominion or turn factor;
- uniqueness;
- owner and target conditions.

## Requirements are filters

Major requirement families include:

| Family | Examples of questions |
| --- | --- |
| Generic | Era, turn, month, season, story events, AI |
| Nation | In play, recipient, excluded nation or ally |
| Treasury | Gold, gem type, active-path gems |
| Research | School and minimum level |
| Province | Population, unrest, PD, terrain, plane, fort, lab, temple |
| Site | Present, hidden, discovered, nearby, Throne, free slots |
| Dominion | Owner, candle strength, god form, awake state |
| Scales | Order, Productivity, Heat, Growth, Luck, Magic |
| Monster | Monster present or absent |
| Mage | Paths, type, order, characteristics |
| Target | Legal commander selected for effect |
| Code | Province and world event-chain state |
| Enchantment | Global active, owner, hostile, target |
| Variable | Global integer state |

The safest event begins with the narrowest stable identity:

- intended nation;
- intended terrain or site;
- intended turn window;
- intended target order;
- uniqueness or variable gate.

## Province event codes

Events can place numeric codes on provinces. Later events can require, forbid, locate, or remove those codes.

The official manual recommends negative codes from `-300` to `-5000`, with `0` as the default/reset state. Two mods using the same code can scramble chains.

Create a code registry:

| Range | System |
| --- | --- |
| -300 to -399 | Tutorial and introduction |
| -400 to -499 | Diplomacy warnings |
| -500 to -599 | Grudges and sanctions |
| -600 to -699 | Coalition escalation |
| -700 to -799 | Scenario objectives |

The exact allocation is project-specific. What matters is that it is written, checked against dependencies, and never recycled casually.

## Event variables

Event variables are global integers numbered 0-9999. They begin at zero and can be checked or altered.

Special negative references are translated:

| Reference | Documented interpretation |
| ---: | --- |
| -1 | Nation receiving the event |
| -2 | 500 + player number |
| -3 | 1000 + province number |
| -4 | 3000 + province number |

These mappings reserve broad portions of the variable space implicitly. The manual warns that `-1` can alter variables up to 499, while province-derived forms can reach higher blocks.

Use variables for:

- once-per-player events;
- relationship scores;
- warning stages;
- global objectives;
- cooldowns;
- campaign chapters;
- counted thresholds.

Use province codes for:

- local state;
- marked borders;
- regional event chains;
- site or province transformations.

Do not substitute one for the other without considering scope.

## Once-per-player pattern

A reliable conceptual pattern is:

```text
require the recipient's variable to be zero
apply the event
increment that recipient's variable
```

Using the special nation variable reference provides one state cell per recipient. A public community explanation by experienced modder Sombre confirms this interpretation and matches the Event Manual's stated purpose.

## Targets are not automatically “any mage”

Many effects require a valid target commander. Requirements can filter:

- monster type;
- humanoid or other body class;
- path levels;
- sight or gem possession;
- current order;
- positive or absent paths;
- properties such as Pretender, prophet, or special status.

An event intended to affect a site-searching mage should require the site-search order. An event intended for a temple-based teacher should require the appropriate province and target class.

Target testing records:

- no eligible commander;
- one eligible commander;
- several eligible commanders;
- same commander with different orders;
- commander in and outside fort;
- prophet, Pretender, mounted, transformed, and disguised cases;
- ally or disciple where relevant.

## Messages can carry required object names

Some site and item commands read the exact object name from square brackets at the end of the event message.

Consequences:

- spelling and capitalization must match;
- a localization-like prose edit can break mechanics;
- renaming an object requires an event-message audit;
- brackets should be treated as data, not decoration.

Keep the required name on a dedicated final line in source comments even if the public message is rewritten.

## Event chains

A bounded chain has:

1. initial eligibility;
2. first effect;
3. state marker;
4. follow-up eligibility;
5. follow-up effect;
6. reset or terminal marker.

Conceptual example:

```text
Stage 0: no warning
-> expansion threshold crossed
Stage 1: warning code or variable
-> threshold remains crossed after cooldown
Stage 2: grievance and local penalties
-> repeated violation or war state
Stage 3: coalition invitation
-> resolution
Terminal: reset, peace, victory, or permanent hostility
```

Every chain needs:

- terminal state;
- re-entry policy;
- cooldown;
- uniqueness scope;
- recovery path;
- compatibility namespace.

Without a terminal state, an event chain becomes an accidental recurring tax.

## Delays and the global event calendar

Events can be delayed or added to the global calendar. The calendar holds planned global events for the coming seven months.

Delayed systems must answer:

- can the initiating condition cease before execution?
- should the delayed event recheck ownership or war?
- can the target die?
- can the province change owner?
- can several copies queue?
- is there a purge or cancellation path?

The most common narrative error is treating delayed execution as if the original state were frozen.

## Global-enchantment events

The Event Manual provides a simple pattern in which an enchantment identity enables immediate or recurring events. A robust global uses separate events for:

- owner income or boon;
- hostile-province effect;
- terrain-specific effect;
- dominion-scaled effect;
- messaging;
- cleanup or cessation.

Every recurring event should use the narrowest rarity and a per-month cap where possible.

## Event effects and transactional thinking

Effects include:

- gold, gems, items, and treasure;
- scales, population, unrest, defence, terrain, and sites;
- commanders and units;
- afflictions, healing, path boosts, transformation, and items;
- enchantment and world effects;
- event codes and variables;
- delays and calendar manipulation;
- victory requirements.

Treat a multi-effect event as a transaction:

```text
validate all prerequisites
-> alter local state
-> grant or remove assets
-> write chain state last
```

Although the engine does not provide database rollback, this order makes the design easier to reason about and reduces half-complete chains.

## Event performance

An event system can be logically correct and operationally expensive.

Cost rises with:

- rarity-5 checks across every province;
- broad monster requirements;
- several global scans;
- repeated nearby-code checks;
- many always events;
- unbounded spawning;
- event chains that never terminate.

The 6.29 update reported a major performance improvement for events using monster-presence requirements, which confirms that event-query cost is material.

Performance doctrine:

- filter by nation and terrain early;
- avoid worldwide checks where a per-player variable is sufficient;
- cap monthly executions;
- make dormant stages ineligible;
- use one scheduler event to enable narrower local events;
- measure hosting time on a large map.

# Part VIII: Simulating Diplomacy and Strategic Reaction

## What event modding can accomplish

An event system can create:

- warnings after expansion thresholds;
- consequences for dominion pressure;
- responses to claimed Thrones;
- retaliation against repeated raiding;
- defensive reinforcements;
- temporary sanctions;
- border unrest;
- hostile summons;
- coalition-themed messages;
- gifts or concessions after restraint;
- campaign reputation;
- AI-only bonuses triggered by a human threat.

This can make the world react coherently.

## What it cannot honestly claim

Ordinary modding does not expose a general rewrite of the AI's strategic mind. It does not provide an open-ended diplomatic planner capable of:

- understanding free-form promises;
- evaluating arbitrary treaties;
- remembering nuanced betrayal;
- planning coalition manoeuvres as a human group;
- reasoning about every modded unit and spell;
- negotiating outside the supported diplomacy systems.

Events can simulate consequences and staged attitudes. AI hints can influence recruitment, Pretender design, research, rituals, and spell preference. That combination can create convincing strategic theatre, but it should not be described as a new general intelligence.

## The reaction-layer architecture

A practical diplomacy overhaul has five layers:

| Layer | Responsibility |
| --- | --- |
| Observation | Detect measurable state such as Thrones, borders, dominion, wars, ownership, or turn |
| Memory | Store province codes and player variables |
| Interpretation | Convert thresholds into warning, grievance, hostility, or coalition stage |
| Response | Apply messages, troops, resources, attacks, or restrictions |
| Recovery | Reduce hostility, expire sanctions, or reset after peace |

The structure is deliberately finite. Each grievance is a state machine with explicit inputs and outputs.

## Observable proxies

When the desired concept is not directly exposed, use a measurable proxy.

| Desired concept | Possible proxy |
| --- | --- |
| Rapid expansion | Province ownership checked over staged turn windows |
| Border pressure | Codes in neighbouring provinces |
| Religious aggression | Dominion ownership and candle thresholds |
| Throne threat | Claimed Throne requirements and Ascension Point state |
| Warmonger | War-related state combined with repeat counters |
| Broken warning | Prior warning variable plus continued trigger |
| Coalition concern | Several nations independently reaching hostility stage |
| Restraint | Cooldown without further violations |

The proxy must be disclosed in design notes. A player should be able to understand why the world reacted.

## Warning before punishment

A believable system escalates:

1. observation;
2. warning;
3. opportunity to change;
4. limited response;
5. severe response;
6. recovery or permanent feud.

Immediate punishment teaches the trigger but does not feel diplomatic. A warning creates agency.

## Avoiding hidden rubber-banding

AI assistance should be legible and bounded.

Good assistance:

- named emergency levy after a capital threat;
- temporary resources after a formal warning;
- faction-specific defenders;
- one coalition response after a Throne threshold.

Poor assistance:

- silent monthly gold;
- infinite unannounced armies;
- bonuses that remain after the threat disappears;
- punishment aimed only at the leading human regardless of cause.

Scenario difficulty should arise from declared rules.

## Relationship-state registry

With **N** nations, pairwise relationship storage can become expensive. A full directed matrix requires **N(N-1)** cells. For 20 nations that is 380 directional relationships.

Event variables are limited and shared. A first design should avoid a full matrix.

Prefer:

- one reputation score per player;
- one global threat stage per player;
- province-local border markers;
- specific scripted rivalries only where necessary;
- separate coalition flags for major objectives.

Pairwise state should be reserved for campaign scenarios with a controlled roster.

## Anti-loop rules

Every diplomacy response needs:

- once-per-stage gating;
- cooldown;
- maximum reinforcements;
- owner recheck;
- game-alive recheck;
- target recheck;
- terminal resolution;
- no valid-target behaviour.

A coalition event that summons troops every month until a province is recaptured can become an infinite unit generator if the target becomes unreachable.

## Fairness matrix

| Question | Acceptable design |
| --- | --- |
| Is the trigger visible? | Message, rule sheet, or inspectable threshold |
| Can the response be avoided? | At least one strategic alternative |
| Is the response proportional? | Escalation matches offence stage |
| Does the AI receive value? | Enough to act, not infinite replacement |
| Can hostility fall? | Cooldown, concession, peace, or objective change |
| Can the system target allies incorrectly? | Ally exclusions and ownership rechecks |
| Does it work for AI offenders? | Explicit AI/human scope |
| Does it scale with map size? | Thresholds tied to settings or scenario |

## A recommended first diplomacy module

Begin with one grievance: early Throne pressure.

State:

- player threat variable;
- one warning-fired variable;
- one sanction-fired variable.

Inputs:

- turn window;
- claimed Throne requirement;
- Ascension threshold;
- whether story events are enabled.

Responses:

- warning message;
- temporary unrest or diplomatic penalty in marked border provinces;
- one defensive grant to threatened AI nations;
- final coalition-themed global message.

Recovery:

- fixed expiry;
- no recurring unit creation;
- no hidden permanent income.

This module is small enough to prove the structure before adding expansion, dominion, and raiding grievances.

# Part IX: Maps and Scenario Design

## The map is a ruleset

A map decides:

- who can meet;
- how quickly capitals can be reached;
- where armies can retreat;
- which terrain recruits and rituals are available;
- how valuable sailing, flying, mountain movement, and amphibious access become;
- how many fronts a nation must defend;
- whether caves and the Nexus matter;
- how difficult a Throne is to contest;
- whether remote spells can reach strategic centres.

Visual beauty matters, but topology and strategic distribution matter first.

## Hand-drawn map assets

The Map Making Manual requires a Targa image for the principal hand-drawn map:

- at least 256x256 pixels;
- 24- or 32-bit colour;
- a practical example size around 1600x1200;
- no problematic alpha channel;
- legal filename without spaces or special characters.

Province centres are defined by individual pure-white pixels with RGB `255,255,255`. Ordinary white artwork should use a near-white such as `253,253,253` so it is not mistaken for an extra province.

Province pixels should be:

- one pixel;
- on a separate image layer during creation;
- merged only for export;
- counted before import.

An accidental white pixel is an accidental province.

## Province borders and areas

Visible borders are not technically required, but they communicate adjacency. Keep them on a separate layer so the map editor can use a border-only image.

Province areas matter for:

- mouse selection;
- dominion overlay;
- terrain-change graphics;
- readable map feedback.

The editor supports an area workflow:

1. switch to Province Area mode;
2. import or paint border areas;
3. expand areas to fill gaps;
4. remove stray pixels;
5. inspect every province;
6. test dominion overlay.

## Connections are strategic edges

The map editor can create:

- ordinary connections;
- mountain passes;
- river borders;
- bridges;
- impassable connections;
- roads.

The manual's special-border values are:

| Value | Border |
| ---: | --- |
| 0 | Standard |
| 1 | Mountain pass |
| 2 | River |
| 4 | Impassable |
| 8 | Road |

An impassable connection can still matter for spell targeting. A line that appears decorative may affect range or adjacency.

Connection audit:

- every visual border matches mechanical adjacency;
- every non-visual connection is intentionally signalled;
- capitals have comparable exit counts;
- no province is accidentally isolated;
- retreats do not create one-way traps;
- wrap connections are readable;
- bridge and pass effects match the artwork.

## Required map commands

Every hand-drawn map file needs:

```text
#dom2title "Map Title"
#imagefile "mapname.tga"
#mapsize <width> <height>
```

The historical command name `#dom2title` remains in use.

Useful metadata includes:

- `#domversion`;
- `#description`;
- plane name;
- hidden-map behaviour;
- cave-plane controls.

## Terrain masks

Common terrain-mask components include:

| Value | Terrain or property |
| ---: | --- |
| 0 | Plains |
| 1 | Small province |
| 2 | Large province |
| 4 | Sea |
| 8 | Freshwater |
| 16 | Highlands or gorge |
| 32 | Swamp |
| 64 | Waste |
| 128 | Forest or kelp forest |
| 256 | Farm |
| 512 | No random start |
| 1024 | Many sites |
| 2048 | Deep, combined with sea |
| 4096 | Cave |
| 8388608 | Mountains |
| 33554432 | Good Throne location |
| 67108864 | Good start location |
| 134217728 | Bad Throne location |
| 1073741824 | Warmer |
| 2147483648 | Colder |
| 68719476736 | Cave wall |

Values are added. The official example `1601` is:

\[
1 + 64 + 512 + 1024
\]

meaning small, waste, no-start, and many-sites.

Rare site-bias components include Fire through Holy site biases. These are advanced and must be added to the map-editor mask manually.

Do not hand-calculate terrain masks without retaining the decomposition.

## Terrain density

The official manual advises that a province generally contain only one adverse terrain type, or at most two. Forest, waste, highland, swamp, and cave combinations slow movement. Too many mixed provinces can make a beautiful map strategically inert.

Terrain audit:

- percentage of provinces by terrain;
- mixed-adverse percentage;
- capital-ring terrain;
- chokepoint terrain;
- recruit and summon access;
- supply;
- underwater distribution;
- national start preferences;
- seasonal and extreme-scale changes.

## Starts

Starting fairness is not equal distance alone.

For every start, record:

- adjacent province count;
- adjacent income and population;
- adjacent resources;
- terrain;
- water access;
- cave access;
- nearest neighbour distance;
- nearest Throne distance;
- number of defensible approaches;
- expansion dead ends;
- nearby high-site provinces.

`#nostart` and the terrain mask value 512 exclude random starts. If a province is marked as both a start and no-start, no-start wins.

`#specstart` assigns a particular nation to a particular start. Scripted maps must use current Dominions 6 nation numbers.

## Thrones

Throne placement shapes diplomacy and victory timing.

Audit:

- total Ascension Points;
- central versus peripheral Thrones;
- level distribution;
- capital proximity;
- underwater Thrones;
- plane distribution;
- chokepoint control;
- ability to attack and retreat;
- whether one start can claim safely without revealing itself.

Good and bad Throne-location terrain masks guide placement but do not replace manual review.

## Province contents

After selecting an active land, map commands can set:

- ownership;
- name;
- population;
- defence;
- unrest;
- fort;
- laboratory;
- temple;
- sites;
- commanders;
- units;
- commander equipment and magic.

This allows designed independents, campaign characters, guarded objectives, and asymmetrical starts.

A placed commander can be altered with map-specific commands for:

- name;
- bodyguards;
- units;
- experience;
- random equipment;
- exact item;
- magic paths.

If the commander is a modded monster, the map may need to refer to it by name rather than number. This creates a dependency on the mod and should be documented.

## Scenario gods and scales

Maps can force a Pretender, dominion strength, and scales for a nation. Human-controlled nations that violate ordinary design-point limits can trigger cheat detection.

Use forced designs for:

- campaigns;
- puzzle scenarios;
- historical rematches;
- AI bosses;
- controlled test maps.

Do not use them casually in an ordinary multiplayer map.

## Multiple planes

Dominions 6 maps can contain up to eight planes: the main plane and seven additional planes.

Each plane requires its own map and image files using the documented naming pattern such as `_plane2`. The map editor should be opened through the first plane so related planes are loaded together.

Event plane requirements can refer to:

- default plane;
- numbered extra planes;
- cave plane;
- Nexus plane.

Plane design questions:

- how is entry obtained?
- can a nation begin there?
- which gates connect it?
- can remote rituals cross?
- what happens if the gate province falls?
- are objectives distributed across planes?
- does the AI understand the route well enough?

## Gates

Map gates connect provinces that share a gate number. A gate network can:

- bypass distance;
- create a contested hub;
- link planes;
- support a campaign chapter;
- undermine ordinary chokepoints.

Every gate needs:

- visible explanation;
- reciprocal test;
- ownership test;
- siege test;
- AI pathing test;
- remote-spell adjacency review.

## Terrain graphics

Dominions 6 can display altered terrain using additional image layers:

```text
mymap.tga
mymap_winter.tga
mymap_forest.tga
mymap_waste.tga
mymap_farm.tga
mymap_swamp.tga
mymap_highland.tga
mymap_plain.tga
mymap_kelp.tga
mymap_water.tga
```

Winter variants can add `w`. Multiple-plane filenames place the plane component before the terrain component.

Missing terrain images do not necessarily prevent play; the default look is used. They do reduce visual accuracy when terrain changes.

## Random map generator

The RMG creates a playable starting point and stores geography in `.d6m` files. It does not remove the need for human inspection.

After generation:

- inspect connection logic;
- inspect capital spacing;
- inspect lakes and cave relationships;
- inspect wrap edges;
- inspect Throne candidates;
- inspect provinces whose artwork implies a connection that does not exist;
- inspect strategic islands.

The binary `d6m` format stores the shape of lands, capital coordinates, a height field, and province ownership pixels. Terrain and other game information remain in the map file. The file-format document is mainly relevant to automated map generators.

## Workshop packaging

A Workshop map folder contains:

```text
maps/
  Antworld/
    Antworld.map
    Antworld.tga
    banner.png
    dom6ws.txt
```

The folder, map, and main image should share the same name.

The Workshop banner is 256x256 or 512x512 PNG. `dom6ws.txt` sets visibility to Public, Friends, or Private. The platform creates an additional persistent ID file after first upload; deleting it can create a new Workshop entry rather than updating the old one.

## Scenario-design ladder

### Symmetric competitive map

Focus:

- start equivalence;
- comparable expansion;
- Throne fairness;
- readable connections.

### Asymmetric cooperative map

Focus:

- declared role differences;
- shared enemy pressure;
- comeback routes;
- objective pacing.

### Campaign map

Focus:

- placed forces;
- scripted chapters;
- persistent event state;
- named characters;
- narrative gates.

### AI challenge map

Focus:

- AI-compatible routes;
- controlled advantages;
- reinforcements with limits;
- clear victory condition;
- no reliance on human-like diplomacy.

### Test harness map

Focus:

- minimum provinces;
- deterministic contents;
- short travel;
- exact terrain;
- isolated experiments;
- reproducible turn-one setup.

# Part X: AI Modding

## Three different AIs

It is useful to separate:

1. **Strategic AI**: recruitment, expansion, forts, armies, rituals, and research.
2. **Spell AI**: battlefield spell selection and targeting.
3. **Scripted event response**: bonuses, attacks, warnings, and scenario state.

They interact, but they are not one system.

## Nation-level AI hints

The Modding Manual exposes several nation hints:

| Hint | Purpose |
| --- | --- |
| Elemental or sorcery path nation hints | Encourage a Pretender with that path |
| `#bloodnation` | Encourage Blood research and hunting |
| `#aigoodbless` | Raise chance of a powerful bless |
| `#aimusthavemag` | Require at least level 3 in one specified path |
| `#aicheapholy` | Signal cheap expendable sacreds |
| `#aiholyranged` | Signal sacred ranged troops |
| `#aiheavyrec` | Encourage resource-heavy troop recruitment |
| `#aimagerec` | Encourage mage recruitment |
| `#aiholdgod` | Keep the Pretender in the home province |
| `#aiawake` | Raise the chance of an awake Pretender |

These commands alter preferences. They do not prove that the resulting strategy is coherent.

## Unit-level recruitment hints

`#ainorec` tells the AI not to recruit a monster. `#aisinglerec` tells it to recruit only one in a batch.

Use `#ainorec` when a unit:

- requires a human-only trick;
- is a trap for the AI;
- is a ceremonial or transformation object not intended for ordinary recruitment;
- consumes resources without filling a usable AI role.

Use `#aisinglerec` for:

- expensive support;
- rare specialists;
- units whose value does not scale linearly;
- commanders or troop-like objects that should not fill a queue.

## AI Pretender templates

AI templates can specify:

- nation;
- chassis;
- awakening;
- paths;
- dominion strength;
- scales;
- blessings;
- research targets;
- favourite rituals or items.

The game can export a designed Pretender template with `ctrl+shift+s`. This is safer than hand-authoring a complex legal build.

Template design should include several viable plans rather than one brittle script:

- awake expander;
- dormant scales;
- bless;
- access or ritual chassis.

If several templates exist for one nation, the AI can choose among them.

## Research goals

`#researchgoal` names a spell or item the AI should work toward. Several goals are pursued in order, although the manual warns that research will not follow the list perfectly.

A research sequence should:

- contain reachable goals;
- match national paths;
- alternate survival and power;
- avoid an item the AI cannot forge;
- avoid a ritual the AI cannot fund;
- account for national spells.

Bad goal:

```text
late legendary spell
```

with no earlier battlefield package.

Better sequence:

```text
early defensive spell
-> first national summon
-> battlefield damage package
-> booster or key item
-> strategic ritual
```

## Favourite rituals and items

`#favrit` can encourage a ritual or item. It includes a research school and level after which the favourite is disabled, or a persistent setting.

Favourite design must consider:

- gem income;
- path availability;
- laboratory access;
- target availability;
- whether repeated casting is useful;
- whether the result has leadership;
- whether the AI will strand expensive summons.

## AI testing is behavioural sampling

An AI instruction is not validated by one game.

Record over several seeds:

- Pretender family;
- scales;
- first twenty commander recruits;
- troop mix;
- first three research targets reached;
- first forged items;
- first national rituals;
- expansion count;
- forts by turn;
- gem stockpiles;
- whether key mages enter combat;
- whether special units accumulate unused.

The goal is not identical behaviour. It is the absence of catastrophic patterns.

## AI bonuses versus AI competence

An AI can be made harder by:

- game difficulty settings;
- better roster;
- better template;
- better research goals;
- targeted event resources;
- scripted reinforcements;
- scenario terrain.

These are different interventions. A report should not attribute victory to “better AI” if the main change was an unannounced resource grant.

# Part XI: Compatibility Engineering

## A mod has dependencies even when it declares none

Dependencies include:

- game version;
- object numbers;
- copied parent objects;
- object names;
- parser phase;
- load order;
- event-code ranges;
- variable ranges;
- map names;
- Workshop identity;
- assumed base-game balance.

A compatibility record should name all of them.

## Freeze exact source

For every dependency, retain:

- filename;
- internal version;
- file size;
- cryptographic hash;
- acquisition date;
- intended order;
- known patch baseline.

“Latest DE” is not reproducible. `DomEnhanced2_16.dm` with a recorded hash is.

## Build an object-overlap matrix

Parse each source for selectors and new-object allocations:

| Object type | Mod A changes | Mod B changes | Overlap |
| --- | ---: | ---: | ---: |
| Monsters | Count | Count | Shared identities |
| Weapons | Count | Count | Shared identities |
| Armour | Count | Count | Shared identities |
| Sites | Count | Count | Shared identities |
| Spells | Count | Count | Shared identities |
| Items | Count | Count | Shared identities |
| Nations | Count | Count | Shared identities |
| Events | Count | Count | Code and variable collisions |

Book IX applies this matrix to the supplied DE and Divinitus files. Keeping the exact totals there prevents the modding method and the live compatibility record from drifting apart. The lesson retained here is that overlap marks an integration surface, not a proven bug count.

## Reconstruct a shared object

For one shared identity:

1. begin with base-game state;
2. apply the first mod's copy, clear, and setters;
3. apply the second mod's copy, clear, and setters;
4. include source invoked through shapes, mounts, items, sites, and events;
5. list visible final fields;
6. list invisible or behavioural fields;
7. mark uncertain engine interactions;
8. inspect and test.

## Worked examples

The Grand Hierophant reconstruction now lives with the Arcoscephale dossier in Book VII, while the broader DE/Divinitus identity and collision analysis lives in Book IX. Book VIII keeps the method so it can be reused with any pair of mods.

## Compatibility patch structure

A compatibility patch should:

```text
declare both dependencies and order
-> reselect every shared object that needs resolution
-> clear only when rebuilding completely
-> set the intended final fields explicitly
-> repair recruitment, sites, spells, items, and events
-> reserve its own codes and variables
-> provide a combined change log
```

Avoid copying an entire parent mod into the patch. That creates an unauthorized fork, obscures provenance, and makes updates harder.

## Conflict classes

| Class | Example | Resolution |
| --- | --- | --- |
| Direct setter conflict | Two costs on same monster | Choose and document final value |
| Clear conflict | Later `#clearrec` removes additions | Re-add intended recruitment |
| Identity collision | Two new weapons use same ID | Reallocate and repair references |
| Name dependency | Spell referenced by renamed name | Replace with stable identity where possible |
| Event code collision | Two chains use `-509` | Allocate new range and update chain |
| Variable collision | Both use player variable block | Registry and remap |
| Shape conflict | Parent form changed by one mod | Rebuild graph |
| Site conflict | Same recruitment site altered | Explicit combined site |
| AI conflict | One forbids a spell another favours | Combined AI policy |
| Map dependency | Scenario names a missing unit | Declare required mod and verify |

## Patch-aware command ledger

The public game can advance beyond the manual. Important current examples include:

- 6.24: new item, event, monster, weapon, and site commands plus fixes;
- 6.25: new spell, item, and event controls;
- 6.27: fort-terrain recruitment, battle summons, enchanted blood, and AI fixes;
- 6.29: `#copysite`, new weapon rolls, unseen, event realm checks, and performance work;
- 6.30: event-variable unit counts, optional site additions, new spell-cost controls, and new monster abilities;
- 6.33: spell home-realm command;
- 6.35: multiple-same-name site reveal and removal fix.

The ledger should record:

| Field | Meaning |
| --- | --- |
| Command or fix | Exact technical subject |
| Introduced | First official version |
| Manual present | Yes, no, or ambiguous |
| Project use | Files and blocks using it |
| Minimum version | Required `#domversion` |
| Regression | Test that proves current behaviour |

## Converting Dominions 5 projects

The official manual identifies changed numbers for:

- nations;
- magic items;
- sites;
- spells;
- forts;
- random events.

Dominions 6 also changes:

- mounted-unit architecture;
- Glamour and former Air illusion themes;
- army scale;
- mod folder layout;
- map start and mountain-border values;
- terrain-change imagery;
- new planes and systems.

Conversion order:

1. make the project load;
2. replace object numbers;
3. rebuild mounts;
4. review paths and Glamour;
5. review recruitment and starting armies;
6. review spells, items, sites, and events;
7. rebuild maps in the current editor;
8. add current metadata and folders;
9. conduct a full balance pass.

Compatibility is not proven by the absence of a load error.

# Part XII: Testing, Validation, and Release Engineering

## Four validation layers

| Layer | Question |
| --- | --- |
| Static | Is the source structurally plausible? |
| Load | Does the game parse and enable it? |
| Object | Do final cards and recruit lists match intent? |
| Behaviour | Does the system act correctly in battle, ritual, event, AI, and campaign play? |

No one layer replaces another.

## Static validation

Automated or manual checks should detect:

- missing final newline;
- unmatched object blocks;
- duplicate explicit IDs;
- duplicate event codes;
- variable-range overlap;
- illegal filenames;
- missing referenced images;
- mixed path separators;
- references to undeclared dependencies;
- accidental tabs or smart quotes where tools mishandle them;
- selectors without identity comments;
- source blocks inserted into a released automatic-ID sequence.

Static validation cannot prove engine semantics.

## Load validation

Test configurations:

1. project alone;
2. dependency alone;
3. project plus each dependency;
4. full intended order;
5. reversed order where diagnosis matters;
6. dedicated/network-lobby path;
7. text-only or headless host path where relevant.

Record exact error text and the minimal failing source.

## Object validation

For every changed object:

- inspect `ctrl+i`;
- record final number;
- record visible stats;
- record recruit source;
- record spell or item restriction;
- compare against baseline;
- capture a screenshot or exported record;
- mark hidden behaviour for live testing.

## Behaviour validation

### Unit

- attack, defence, fatigue, route;
- equipment;
- mount;
- shapes;
- leadership;
- recruitment;
- upkeep;
- death and retreat.

### Spell

- legal caster;
- cost;
- targeting;
- resistance;
- AI;
- range;
- environment;
- ritual result;
- global identity.

### Event

- eligibility;
- probability conditions;
- target;
- state write;
- follow-up;
- duplication;
- no-target case;
- ownership change;
- game-alive check;
- performance.

### Map

- provinces;
- areas;
- connections;
- starts;
- Thrones;
- planes;
- gates;
- terrain visuals;
- AI travel.

## Minimal reproduction mods

When a behaviour is uncertain, create a mod containing:

- metadata;
- one copied or selected object;
- one changed command;
- one test event or map;
- no unrelated dependency.

Then compare:

- command absent;
- command present with low value;
- command present with high value;
- interaction case.

A full overhaul is evidence of a bug only after the problem survives reduction.

## Test harness maps

Maintain small maps for:

- melee and missile damage;
- mounts and area effects;
- shapechanges;
- ritual range;
- site events;
- dominion events;
- global enchantments;
- gates and planes;
- AI recruitment;
- siege and fort recruitment.

Each harness should specify:

- game version;
- enabled mods and order;
- exact nations;
- start province;
- seed if available;
- commands;
- expected result;
- observed result.

## Regression matrix

| Test ID | System | Baseline | Changed | Combined | Status |
| --- | --- | --- | --- | --- | --- |
| MNT-01 | Mount death | Base game | Project | Full mod stack | Pass/fail |
| EVT-01 | Once per player | No event | Project | Full mod stack | Pass/fail |
| MAP-01 | Gate link | No gate | Scenario | Dependencies | Pass/fail |
| AI-01 | Mage recruitment | Vanilla AI | Template | Full stack | Distribution |

Every fixed bug receives a regression test. Otherwise the same defect returns during unrelated work.

## Balance records

Balance notes should distinguish:

- observed fact;
- intended role;
- comparison object;
- economic cost;
- counter class;
- problem;
- change;
- expected consequence;
- retest result.

“Too strong” is not a diagnosis. Better:

> At 18 gold and 9 recruitment points, the unit replaces both the national line holder and damage dealer, wins the heavy-infantry comparison without mage support, and remains more mobile. Raise throughput cost or narrow its damage class.

## Versioning

Use a predictable scheme:

- major: save-breaking redesign or dependency shift;
- minor: new compatible content or important balance revision;
- patch: corrections that preserve object order and intended play.

Each release records:

- game version;
- dependency versions;
- load order;
- save compatibility;
- new object IDs;
- new event-code and variable ranges;
- balance changes;
- fixed defects;
- known issues.

## Release candidates

A release candidate is frozen except for fixes.

Checklist:

- source hash recorded;
- no placeholder descriptions;
- all filenames legal;
- dependencies declared;
- standalone and combined load tests complete;
- network test complete;
- new-game requirement stated;
- change log complete;
- Workshop visibility correct;
- regression suite complete;
- public guide updated.

## Research questions that can be resolved without the project owner

Questions are suitable for independent resolution when they can be answered through:

- current official manuals;
- official patch notes;
- exact supplied source;
- a reliable published reproduction with version and method;
- a locally available game executable and controlled harness.

Questions remain pending when:

- source describes intent but engine resolution is ambiguous;
- community statements lack version or procedure;
- the result depends on the user's private save or settings;
- the game executable is unavailable;
- several current sources conflict.

No user action is needed merely to preserve a pending label.

# Part XIII: Complete Project Workflows

## Workflow A: A one-object balance patch

### Objective

Change one existing object's role without altering unrelated systems.

### Research

Record:

- game and mod version;
- object number and name;
- current final card;
- recruitment source;
- comparison objects;
- reason for change.

### Source

```text
#modname "Example Role Patch"
#description "Versioned adjustment for Dominions 6.36."
#version 0.10
#domversion 6.36

#selectmonster <number> -- name and provenance
#gcost <value>
#rpcost <value>
#end

```

### Validation

- loads alone;
- loads with intended mod stack;
- final cost appears;
- no equipment or magic changed;
- recruitment source remains;
- AI still recruits a sensible quantity;
- ongoing-game policy stated.

### Release record

> Reduced or increased throughput to preserve the unit's battlefield role while preventing it from replacing the nearest alternatives.

This is more useful than “nerfed unit.”

## Workflow B: A new national troop

### Objective

Add one unit that fills a missing role rather than duplicating a superior version of an existing unit.

### Design statement

Name:

- role;
- intended target;
- intended counter;
- gold, resource, and recruitment-point constraint;
- recruitment location;
- national theme.

### Source architecture

```text
new or copied weapon
-> new fixed-ID monster
-> equipment and cost
-> nation or site recruitment
-> AI hint
```

### Audit

| Question | Evidence |
| --- | --- |
| Does it replace an existing troop? | Fort-turn and battle comparison |
| Does it erase a counter? | Defence-class tests |
| Is it recruitable at intended scale? | Resource and recruitment calculations |
| Can the AI use it? | Recruitment samples |
| Does it affect starting armies or PD? | Nation-source check |
| Does it require a dependency? | Copy and equipment provenance |

### Failure signs

- best damage, protection, and mobility in one body;
- lower cost than the unit it replaces;
- no resource or recruitment bottleneck;
- AI fills every queue with it;
- national magic makes its designed counter irrelevant.

## Workflow C: A new mage

### Objective

Create access without accidentally giving a nation every threshold in a path.

### Magic portfolio

Write the mage as rolls:

```text
fixed paths
+ guaranteed random
+ independent partial random
+ rare random
```

Calculate:

- probability of each path at level 1;
- probability of important level-2 or level-3 thresholds;
- probability of crosspath combinations;
- expected recruits;
- 90% and 95% acquisition points;
- impossible combinations.

### Strategic audit

Check:

- new boosters;
- new site-search levels;
- new national rituals;
- new globals;
- new battlefield packages;
- communion or chorus role;
- research-to-gold ratio;
- capital or terrain restriction;
- commander-point pressure.

A single rare crosspath can be more important than the mage's common paths.

## Workflow D: A national spell-and-item ladder

### Objective

Give a nation a themed progression without creating a self-contained ladder that bypasses all external constraints.

### Ladder

```text
early spell
-> first battlefield role
-> construction item
-> higher path access
-> national summon or ritual
-> late strategic payoff
```

For each step:

- school and level;
- native caster probability;
- item requirement;
- gem source;
- mage-turn cost;
- effect;
- counter;
- AI goal.

### Test

- first legal turn in an ordinary game;
- earliest plausible rush;
- worst random-path delay;
- item-loss recovery;
- gem scarcity;
- counter-research timing;
- AI access.

## Workflow E: A bounded national event

### Objective

Grant one thematic effect under conditions that can be understood and tested.

### Pattern

```text
#newevent
#rarity 0
#req_fornation <nation>
#req_turn <minimum>
#req_unique 1
#req_rare <percent>
#req_... <stable condition>
#msg "Visible explanation."
#effect...
#end
```

This is a pattern, not a universal template. Rarity and requirements must match the intended scope.

### Required tests

- correct nation;
- wrong nation;
- before minimum turn;
- after minimum turn;
- condition absent;
- condition present;
- second attempted occurrence;
- multiplayer and disciple scope;
- no valid target.

## Workflow F: A three-stage grievance

### Objective

Make an AI nation respond to a visible strategic action.

### State

| Stage | Variable | Meaning |
| --- | ---: | --- |
| 0 | 0 | No grievance |
| 1 | 1 | Warning issued |
| 2 | 2 | Sanction active |
| 3 | 3 | Hostile response |

### Transition table

| Current | Trigger | Next | Effect |
| --- | --- | --- | --- |
| 0 | Threshold crossed | 1 | Warning |
| 1 | Trigger persists after cooldown | 2 | Limited sanction |
| 1 | Trigger clears | 0 | De-escalation |
| 2 | Repeated violation | 3 | Hostile response |
| 2 | Long restraint | 1 or 0 | Sanction expires |
| 3 | Objective resolved | Terminal | Stop reinforcements |

### Safeguards

- one transition per month;
- no response after recipient elimination;
- owner and ally checks;
- fixed reinforcement cap;
- no full pairwise relationship matrix;
- visible messages;
- permanent hostility only when declared.

## Workflow G: A custom global enchantment

### Objective

Create one ritual whose ongoing effects remain bounded and dispellable.

### Components

1. spell with unique enchantment identity;
2. owner-benefit event;
3. hostile-effect event;
4. terrain or dominion requirements;
5. per-month cap;
6. no-text internal events where appropriate;
7. cleanup verification.

### Load test

- first cast;
- second caster contest;
- dispel;
- caster death;
- owner elimination;
- target ownership changes;
- independent provinces;
- cave and Nexus planes;
- several simultaneous globals.

## Workflow H: A competitive map

### Objective

Produce a map that is strategically fair without making every start identical.

### Build

1. draw art and province centres;
2. import into map editor;
3. set connections;
4. paint areas;
5. assign terrain;
6. mark starts and Throne preferences;
7. generate or place sites and contents;
8. inspect capital rings;
9. run nation-start samples;
10. package and version.

### Start report

For each start:

| Metric | Value |
| --- | --- |
| Neighbours | Count |
| Land income potential | Estimate |
| Resources | Estimate |
| Adverse terrain | Count |
| Nearest capital | Steps |
| Nearest Throne | Steps |
| Water or cave access | Yes/no |
| Chokepoint exits | Count |

Outliers are then reviewed, not automatically erased. Some asymmetry is desirable; compound disadvantage is not.

## Workflow I: A campaign scenario

### Objective

Combine a designed map, forced starts, named commanders, and event chapters.

### Chapter architecture

```text
pregame setup
-> chapter variable
-> objective code
-> completion event
-> next chapter
-> terminal victory change or final event
```

### Failure handling

Campaign events need alternatives when:

- a named commander dies;
- an objective province changes hands early;
- a player is eliminated;
- a site is removed;
- a gate becomes inaccessible;
- an unexpected nation receives the event.

Do not let one missing narrative object stop the campaign forever.

## Workflow J: A compatibility patch

### Objective

Create one explicit final ruleset from two changing parents.

### Procedure

1. freeze exact parent files;
2. parse selected and new identities;
3. allocate compatibility codes and variables;
4. produce overlap matrix;
5. prioritize clears, recruitment, Pretenders, shapes, events, and globals;
6. reconstruct shared objects;
7. write the smallest explicit repair;
8. test parent A, parent B, A+B, and A+B+patch;
9. publish supported order;
10. repeat after either parent updates.

### Compatibility statement

> Supports Dominions Enhanced 2.16 followed by Divinitus 1.15.3 DE on the last tested baseline. Compatibility with Dominions 6.36 remains unverified until the combined files are loaded and exercised under that executable; other orders and versions are outside the verified ruleset.

That sentence is more valuable than a broad claim of compatibility.

# Part XIV: Design Essays

## Essay I: Load Order Is Part of Game Design

Load order is often treated as installation trivia: place one file before another until the game stops reporting an error. In Dominions it is part of the rules.

A selected monster is usually a partial modification. One mod may change cost, another paths, another recruitment, and an event may later transform the unit. The final object exists only after every layer has been applied. Reversing two layers may change the object without either source becoming invalid.

This means a guide tied to several mods cannot discuss them as independent add-ons. “DE gives this” and “Divinitus gives that” do not automatically describe the combined game. The relevant object is the combined final state.

Load order also determines strategic value. A later `#clearrec` can remove a unit that justified an earlier balance change. A later path adjustment can unlock a ritual. A later item restriction can close it again. A later event can create the same mage with additional paths. None of these changes are cosmetic.

The design response is not to fear overlap. It is to make overlap explicit. Dependencies are frozen. Shared selectors are inventoried. Clears are treated as destructive. Final objects are written into evidence records. Compatibility patches become small declarations of intended state.

Once load order is documented this way, it stops being a mysterious source of bugs. It becomes a versioned design decision.

## Essay II: An Event System Is a Small Political Engine

Dominions events are often introduced as random rewards and disasters. Their deeper value lies in memory and transition.

A province code remembers that something happened in one place. A variable remembers that something happened to a nation or the world. Requirements observe present conditions. Effects move the state forward. Together these create a finite political engine.

The engine does not understand betrayal as a human concept. It can understand that a warning was issued, a threshold remains crossed, a Throne was claimed, a border province bears a marker, and a sanction has not yet expired. That is enough to produce an intelligible sequence:

```text
action
-> warning
-> choice
-> response
-> recovery or escalation
```

Believability comes from causation, not unlimited complexity. A short chain with visible triggers can feel more political than a large table of random punishments.

The main design danger is memory without decay. If every offence creates a permanent counter, the game trends towards universal hostility. Recovery is essential. Grievances need cooldowns, concessions, terminal states, or deliberate permanent-feud rules.

The second danger is hidden compensation. If an AI receives armies whenever a player succeeds, the system becomes rubber-banding. If threatened nations receive one declared levy after a warning, the same mechanical assistance becomes part of the world's politics.

Event modding cannot create unrestricted diplomatic intelligence. It can create a political grammar: actions have legible meanings and bounded consequences.

## Essay III: AI Scaffolding Is Not an AI Rewrite

The exposed AI controls are meaningful. Pretender templates can prevent disastrous designs. Research goals can lead toward usable spells. Recruitment hints can reduce trap purchases. Favourite rituals can help a nation express its theme. Spell preferences can suppress destructive casting.

Yet these controls remain scaffolding around an existing decision-maker.

This distinction matters because design claims determine expectations. A mod advertised as “smarter AI” should be evaluated on decisions. A mod that grants gold, troops, and scripted attacks may be an excellent challenge system, but its difficulty comes partly from resources and scenario rules.

The strongest design uses all three AI layers honestly:

- templates make the starting plan coherent;
- hints reduce recurrent tactical and economic mistakes;
- events create strategic pressure when the ordinary AI cannot model a bespoke objective.

The result can feel much more capable. It is still important to record why.

This honesty also improves balancing. If the AI fails because it recruits the wrong unit, change the hint or roster. If it fails because it cannot understand a gate network, change the scenario. If it fails because it lacks economy, decide whether a visible subsidy fits. Calling every remedy “intelligence” hides the actual lever and makes later refinement harder.

## Essay IV: Map Topology Precedes Army Balance

Two armies with identical statistics can have different value on different maps.

Sailing is ordinary on a dense landmass and decisive across chains of sea provinces. Slow heavy infantry can dominate a compact front and fail on a wide wraparound map. Remote rituals gain value when chokepoints hold armies in predictable provinces. Cave access can be a curiosity or an entire second theatre.

The map establishes the exchange rate between movement and force.

Topology also determines diplomacy. A nation with two neighbours can sustain stable borders. A central nation with five exits cannot treat the same army count as equivalent security. A nearby Throne creates conflict before a message is sent. An isolated Throne invites concealed accumulation.

For this reason competitive map testing should not begin with decorative polish. It begins with edges, starts, rings, routes, planes, and objectives. Art then communicates those rules clearly.

The same principle applies to scenarios. A scripted coalition is less important than whether coalition armies can reach the threat. A narrative gate is not meaningful if the AI cannot use it. A fortress is not a defence if every approach bypasses it.

Mapmaking is not the container around game design. It is the first layer of game design.

## Essay V: Balance Is a Conversion Rate

Individual statistics are attractive because they are easy to compare. Dominions balance emerges from conversion.

Gold becomes troops. Resources determine equipment throughput. Recruitment points determine bodies per fort. Commander points become mages, scouts, and leaders. Research becomes packages. Gems become battlefield or ritual effects. Movement converts force into presence. Siege converts victory into ownership.

A unit is overpowered when it converts one or more inputs into strategic effect too efficiently, especially when it replaces several alternatives. A mage may be too efficient even with ordinary paths if research, recruitment points, and randoms combine favourably. A spell may be too efficient because its native caster is common, not because the text is spectacular.

This suggests a better balance note:

```text
input
-> throughput
-> delivered role
-> counter
-> campaign consequence
```

It also explains why copying a cost from a similar unit is insufficient. The new nation may have different forts, scales, buffs, leaders, or magic. The same body enters a different conversion chain.

Good balance preserves decisions. If one recruit, research target, or item dominates every nearby alternative, the game has fewer decisions even if win rates remain uncertain.

## Essay VI: Compatibility Is a Public Interface

Large mods become platforms. Other projects refer to their monsters, spells, sites, and nations even when no formal interface exists.

The moment another project depends on an object number, allocation order becomes public. The moment a compatibility file selects a monster, that monster's identity becomes shared. The moment an event uses a common code, the code occupies global namespace.

This creates responsibility:

- do not reorder automatic objects casually;
- publish dependency versions;
- reserve identifiers;
- document breaking changes;
- retain deprecated placeholders when practical;
- provide migration notes;
- make load order visible.

The objective is not permanent backward compatibility. Some redesigns justify a break. The objective is an intentional break rather than an accidental one.

Compatibility habits also help solo work. Six months later, the original author is another developer trying to remember why monster 9322 exists.

## Essay VII: A Test Harness Turns Modding into Knowledge

Without a harness, modding knowledge remains anecdotal.

A battle was won, but the seed changed. An event occurred, but its rarity and eligible-province count were unknown. A combined Pretender displayed a path, but the source of that path was not traced. An AI cast a spell once, but no comparison existed.

A harness removes irrelevant variation. One unit faces one defence class. One event has one eligible province. One map has one gate pair. One AI receives one template. Expected results are written before observation.

The harness also protects future work. When a patch changes mounts, the mount suite is rerun. When a dependency updates, the overlap and regression matrix show what to inspect. When an argument becomes disputed, the library can point to conditions and results rather than confidence.

Not every question requires live testing. Official text, source, and arithmetic resolve many. The test harness is for the boundary between documented intent and engine resolution.

# Part XV: Quick References and Checklists

## New-mod preflight

- separate mod folder;
- matching folder and `.dm` basename;
- legal filenames;
- correct case;
- forward-slash paths;
- metadata block;
- minimum game version;
- every object block ended;
- final newline;
- identifier registry;
- no undeclared dependency.

## Object-block preflight

- correct selector or creator;
- object identity comment;
- copy source recorded;
- clear scope understood;
- fields grouped;
- cost channels reviewed;
- references valid;
- `#end`;
- final card inspected.

## Event preflight

- rarity;
- recipient nation;
- province and plane;
- target and order;
- turn or month window;
- probability;
- uniqueness;
- code range;
- variable range;
- effect;
- state transition;
- cooldown;
- terminal state;
- no-target behaviour;
- per-month cap;
- ally and ownership checks.

## Map preflight

- legal filename;
- image mode and alpha;
- one white pixel per province;
- required commands;
- province areas;
- connections;
- special borders;
- terrain decomposition;
- start audit;
- Throne audit;
- plane and gate audit;
- AI-route audit;
- Workshop package.

## AI preflight

- at least one legal Pretender template;
- scale and bless logic;
- reachable research goals;
- forgeable favourite items;
- castable favourite rituals;
- trap units suppressed;
- mage recruitment sampled;
- spell preferences tested;
- bonuses disclosed;
- several seeds observed.

## Compatibility preflight

- exact parent versions;
- hashes;
- supported load order;
- object overlap;
- ID collision;
- event-code collision;
- variable collision;
- clear operations;
- recruitment reconstruction;
- shape and mount graph;
- final object cards;
- regression suite;
- save policy.

## Troubleshooting decision tree

### Mod absent from list

Check folder, extension, metadata, filename, final newline.

### Mod reports parse error

Reduce by binary search; check quotes, arguments, selectors, and `#end`.

### Object exists but is unavailable

Check nation, site, terrain, era, god list, and later clears.

### Object has wrong statistics

Trace copy, clear, automatic cost, equipment, and later selectors.

### Combined mods behave differently

Freeze order; build overlap matrix; reconstruct shared objects.

### Event never fires

Check rarity, every requirement, recipient, target order, codes, variables, uniqueness, and eligible province count.

### Event fires repeatedly

Check rarity 5, uniqueness, state write, reset, and per-month limit.

### AI ignores content

Check legal access, path, gems, research goal, recruitment hint, and whether the desired reasoning is exposed at all.

### Map looks right but plays wrong

Check mechanical connections, province areas, terrain mask, starts, and gates.

## Project registries

Maintain:

- object IDs;
- event codes;
- event variables;
- enchantment numbers;
- map gate numbers;
- copied parent objects;
- dependency names and hashes;
- test IDs;
- known unresolved behaviours.

## Open research register

The following questions remain suitable for controlled verification:

1. exact automatic allocation behaviour at the current high object ceilings;
2. parser treatment of every cross-mod name reference category;
3. which copied hidden attributes are absent from `ctrl+i`;
4. event-variable overflow and negative-value edge cases;
5. event execution order when several rarity-5 systems alter the same state;
6. performance curves for large always-event libraries;
7. AI use of multi-plane gates in varied scenarios;
8. AI template selection distributions;
9. save compatibility for inserted automatic spell and item objects;
10. combined transformation preservation for prophet, mount, heroic, and item state;
11. exact event targeting when several equally eligible commanders exist;
12. network-lobby behaviour for every filename and dependency edge case.

These remain visible rather than being converted into unsupported claims.

# Part XVI: Source Register

## Official sources

1. [Dominions 6 documentation page](https://illwinter.com/dom6/docs.html) - current official manual index.
2. [Dominions 6 Modding Manual, version 6.34](https://illwinter.com/dom6/dom6modman.pdf) - primary command authority for objects, nations, AI templates, and limits.
3. [Dominions 6 Event Modding Manual, labelled version 6.29](https://illwinter.com/dom6/dom6eventman.pdf) - event requirements, effects, codes, variables, and examples.
4. [Dominions 6 Map Making Manual, version 6.26](https://illwinter.com/dom6/dom6mapman.pdf) - map images, editor, commands, terrain, planes, and Workshop packaging.
5. [Dominions 6 File Formats](https://illwinter.com/dom6/dom6fileformats.pdf) - binary `d6m` structure.
6. [Dominions 6 official update announcements](https://steamcommunity.com/app/2511500/announcements/) - commands and fixes introduced after earlier manual revisions.
7. [Illwinter Dominions 6 changes](https://www.illwinter.com/dom6/changes.html) - major system changes from Dominions 5.

## Supplied source files

Dominions Enhanced 2.16 and Divinitus 1.15.3 DE serve as the running compatibility examples. Their hashes, exact sizes, object counts, overlap matrix, and live findings are maintained in Book IX so that this methods volume does not become a second, stale inventory.

## Community evidence

Community material is used only where:

- the version is identifiable;
- the source states a procedure or exact syntax;
- the finding is consistent with official documentation;
- the claim is labelled community-tested when not reproduced.

The once-per-player variable explanation and final-newline troubleshooting pattern meet that limited use. Unversioned recollections, wish-list commands, and isolated outcome reports are not promoted to confirmed mechanics.

## Revision policy

Book VIII should be revised when:

- the public game version changes;
- any official modding manual changes;
- a relied-upon command is fixed;
- DE or Divinitus changes;
- a pending behaviour is reproduced;
- the diplomacy project allocates live code and variable ranges;
- a real compatibility patch is created.

Every revision must retain the prior ruleset label so published scenarios and saved games can still be interpreted.
