# Foundation Book XIV: The Command and Terminology Lexicon

## Official syntax, context, provenance, and search discipline

## The job of this volume

Dominions modding is written in a compact language whose commands often look self-explanatory. That appearance is deceptive. A token can be correctly spelled and still be unusable because it appears outside the right object block, follows the wrong selector, carries the wrong argument form, relies on an undocumented expansion, or belongs to a newer executable than the manual that a project was built against. A patch announcement can prove that a command existed or changed without explaining its complete syntax. A current manual can list a token without describing its behaviour. Several different object types can even use the same command spelling for different fields.

This volume supplies the retrieval layer needed to navigate that language. Its canonical subjects are:

- official command spellings and syntax locators;
- object context and command-domain classification;
- current-manual, reference-list, mention-only, template, and patch provenance;
- controlled reconciliation of patch-note shorthand and spelling discrepancies;
- safe lookup, testing, versioning, and maintenance procedures;
- a complete searchable locator for the current official manuals;
- a website-ready command register with stable records and aliases.

Book VIII remains the canonical explanation of parser state, object design, events, maps, AI scaffolding, compatibility, and testing. Book XIII remains the canonical release chronology. Book XIV does not repeat either volume. It answers a narrower question: *what exactly is this token, where is it officially located, what kind of evidence supports it, and which chapter owns the surrounding design problem?*

The result serves two audiences at once. A new modder can identify the right manual and avoid common syntax traps. An experienced maintainer can search by command, domain, version, patch record, template expansion, documentation status, or canonical destination without manually combing through several PDFs.

## Technical baseline

The ruleset baseline is unmodded Dominions 6.37. The currently published official documents carry different internal versions, while the compiled locator retains its separately labelled extraction revision:

| Official source | Document version | Pages | Role in this lexicon |
|---|---:|---:|---|
| Dominions 6 Modding Manual | 6.36 live; 6.34 locator snapshot | 65 | General mod syntax and the principal object languages |
| Dominions 6 Event Modding Manual | 6.29 | 20 | Event requirements, effects, variables, targets, and message substitutions |
| Dominions 6 Map Making Manual | 6.26 | 11 | Map-file structure, provinces, connections, starts, scenario state, and planes |
| Official update announcements | 6.01-6.37 | 33 announcements | Additions, corrections, deprecations, and historical provenance |

This version difference matters. “Current download,” “locator snapshot,” and “same version as the executable” are not synonyms. The live Modding Manual is one release behind the game baseline, while the complete token locator is still pinned to its 6.34 extraction; the Event and Map Making manuals remain older separately versioned sources. Nothing in that observation makes the documents unreliable. It means their claims must be labelled precisely and supplemented by later official patch evidence where necessary.

The compiled register contains 1,609 distinct official hash tokens found across the three-manual locator snapshot. Of these, 1,540 have an official definition or syntax line, 60 occur only in an official reference list or example-style block, and nine are mentioned without a complete definition line. The total also includes 29 double-hash message substitutions and thirteen documented command templates. Template expansion creates 97 additional lookup aliases without pretending that those aliases were separately printed as definitions. Book XIII names 226 patch-note tokens through 6.37: 221 are reconciled in the locator snapshot, while the five event commands introduced by 6.36 remain official patch-only records pending a full current-manual locator rebuild. Version 6.37 introduced no additional hash commands.

## Evidence key

The following labels appear throughout the volume and its data register.

| Label | Meaning | What it permits |
|---|---|---|
| Defined | A bold command definition or syntax line appears in a current official manual | The printed syntax and context can be used as an official locator |
| Reference-only | The token appears in an official list or example-style block without a full definition line | Existence is supported; complete behaviour still requires caution |
| Mentioned-only | The token appears in official prose without a definition or reference entry | The mention may guide research but does not establish complete syntax |
| Template alias | A literal lookup term is derived from an official terrain or numeric template | The alias is searchable, while the template remains the cited definition |
| Exact patch match | An official update token matches a current-manual token | History and present documentation can be linked directly |
| Spelling mismatch | The update announcement and current manual use different spellings | Both forms are preserved; the discrepancy is not silently repaired |
| Family shorthand | A patch expression names several related commands rather than one literal token | The expression is expanded only through a controlled mapping |
| Message placeholder | A double-hash substitution is text grammar rather than a mod command | It belongs in message construction, not an object block as a command |
| Runtime-pending | Official text does not settle the operational result | A minimal reproduction remains necessary before a behavioural claim is promoted |

The evidence label answers *how the token is known*. It does not say that the token is strategically wise, compatible with every other mod, or safe to add to an ongoing game.

# Part I: Reading the Modding Language

## A command is an instruction inside a stateful document

Every ordinary Dominions mod command begins with a single hash sign. The parser does not read each line as an isolated request. A selector or creation command establishes the current object, following commands alter that object, and `#end` closes the block where the language requires it. The same spelling can therefore mean different things under different selectors.

Consider `#name`. The token is defined for weapons, armour, monsters, blessings, sites, nations, spells, magic items, and mercenaries. A search result that merely says “`#name` exists” is almost useless. The operative questions are which object is active, which syntax variant is printed for that object, which parser phase handles it, and which closing rule applies. The register therefore stores every official definition context instead of collapsing all occurrences into a single undifferentiated sentence.

Book VIII, Part I owns the full parser model. The compact rule for lookup is simpler:

> Command spelling identifies a language feature; the active object block determines what that feature addresses.

## Command, argument, value, and block

A command is the hash-prefixed keyword. An argument is information supplied after that keyword. A value is the concrete number, string, name, filename, or mask substituted for the argument notation. A block is the span between an object selector or creator and its terminating `#end`, where one is required.

The manual notation is descriptive rather than literal:

| Notation | Reading rule | Example interpretation |
|---|---|---|
| `#command` | Literal command spelling | Type the hash and command name |
| `<arg>` | Required argument | Replace the entire bracketed label with a value |
| `[<arg>]` | Optional argument | Supply the argument only when the documented form requires it |
| `A \| B` | Alternative arguments | Use the left or right form, not both |
| `"<text>"` | String argument | Replace the label while retaining quotation marks where the syntax shows them |
| `<number>` | Integer or numeric identifier | Supply a valid number within the documented domain |
| `<percent>` | Percentage represented as an integer | A value may exceed 100 when the command permits it |
| `<bitmask>` | Sum of enabled bit values | Combine flags arithmetically rather than typing their labels |
| `#family1...5` | Numeric command template | Use one literal member such as `#family1` or `#family5` |
| `#(terrain)rec` | Word-substitution template | Replace `(terrain)` with an allowed terrain word |
| `##name##` | Message substitution | Insert inside supported message text; do not treat it as a command line |

Angle brackets are not normally typed. A line such as `#gcost <gold>` means that `<gold>` is replaced by an integer. Square brackets in the printed syntax mark an optional component; they are not usually literal punctuation either. Quotation marks are different: when the manual prints a string in quotes, the quotes are part of the practical syntax.

## Comments and explanatory text

Two consecutive hyphens begin a comment. The parser ignores the remainder of that line. Comments are not decoration in a serious project. They preserve intent, source version, ownership, compatibility decisions, reserved identifiers, and reasons for non-obvious values.

A useful comment records something that cannot be recovered by reading the command alone:

```text
-- Reserved unit range 9100-9149; do not allocate automatically.
-- Vanilla 6.37; syntax located in the 6.34 command-locator snapshot, p. 13.
#newmonster 9100
```

Comments that merely repeat a token add little. “Set the name” above `#name` will not help a later maintainer understand why an identifier is fixed, why a copied field is retained, or which combined-mod collision was avoided.

## The four principal argument classes

The Modding Manual identifies integer, percentage, string, and bitmask arguments. Their failure modes differ.

An integer is a whole number. It may be a quantity, identifier, level, code, index, flag value, or enumerated choice. Treating every integer as a quantity causes subtle errors: a path number is not a path level, a monster number is not a count, and an effect number is not a magnitude.

A percentage is also written as an integer. The command defines how that integer is interpreted. Some percentages accept values above 100; others describe chances bounded by a conventional range; still others act as modifiers rather than probabilities. The argument label is therefore not a universal validation rule.

A string is text. Names and filenames are strings, but they carry different operational constraints. Object names can create ambiguous references when several objects share a name. Filenames are case-sensitive and must obey lobby-safe naming rules. Quotation marks protect spaces in string values; they do not remove filename restrictions.

A bitmask represents a set as a sum of powers of two. Bitmask errors are rarely obvious to the eye because an incorrect sum is still a valid integer. A proper record keeps both the decimal total and its component flags. When a terrain mask, path mask, damage mask, or event mask changes, the components should be recalculated rather than adjusted by guesswork.

## Names and numbers are different forms of reference

Many selectors accept either an object name or number. Names are readable but can be ambiguous, can change between versions, and cannot reliably cross every mod boundary. Numbers are precise but can collide, can be allocated differently when content order changes, and are difficult to understand without a registry.

The safest choice depends on the project:

- a small private balance patch may prefer names for untouched vanilla objects;
- a distributable content mod benefits from fixed IDs and a published allocation register;
- a compatibility patch needs explicit knowledge of both source projects' identities;
- an ongoing-game update must preserve the identifiers already embedded in the save;
- a cross-mod reference should never assume that a name provides a stable linking contract.

Book VIII owns allocation and collision engineering. Book XIV records whether syntax allows a name, a number, or either form.

## Binary commands and clearing state

A command printed without an argument commonly enables a fixed attribute. Its absence does not necessarily mean “false” after an object has been copied. A copied object may already carry the field, and a clearing command may be needed to remove inherited state.

This is why `#copy...`, `#clear`, specialised clearing commands, and zero-valued arguments cannot be treated as interchangeable. Their behaviour depends on the object language. Copy-first and clear-first create different starting states. The lexicon locates the commands; Book VIII, Section “Copy-first and clear-first are different designs” owns the design consequences.

## Optional arguments are branches, not decorative hints

Square-bracket arguments represent alternative valid forms. The short form and long form may not be semantically identical. Optional identifiers can affect automatic allocation. Optional names can change display behaviour. Optional values can select defaults that later game versions revise.

For maintainable source, the chosen form should be deliberate and documented. Omitting an argument because the notation looked complicated is not the same as selecting the default knowingly.

## The vertical bar means exclusive alternatives

The manual uses a vertical bar to mean “or”. In syntax such as:

```text
#selectweapon "<weapon name>" | <weapon nbr>
```

the selector takes a name or a number. The entire expression is not typed. Mixing both forms can produce a parse error or leave unexpected trailing input. Website presentation must escape the bar inside Markdown tables so it is not mistaken for a column boundary.

## Templates describe a grammar

Thirteen official entries are templates rather than literal commands. Four substitute terrain words, while nine describe numeric ranges. `#(terrain)fortrec` is not a line to paste into a mod. It is a compact grammar covering forms such as `#forestfortrec`, `#plainfortrec`, and `#dripfortrec`, subject to the terrain restrictions printed beside the template.

The same principle governs `#hero1...10`, `#multihero1...7`, `#battlesum1...5`, and similar families. The ellipsis describes a range. It is not part of a literal command. Search systems should resolve a concrete family member back to the template without rewriting the official definition.

Template generation carries two risks. First, not every visually plausible substitution is legal. Sea, deep-sea, and kelp recruitment use special rules in the fort variants. Second, family notation in a patch announcement can be looser than the formal template in a manual. Controlled alias records solve the retrieval problem while retaining those qualifications.

## Double-hash substitutions are not commands

Event and global-enchantment messages support substitutions such as `##landname##`, `##godname##`, and `##targname##`. These tokens are interpreted inside supported text. A single-hash command controls the event or object; a double-hash substitution changes the message produced by that object.

Capitalisation can be meaningful. The official reference includes both lower-case and capitalised pronoun forms. The lexicon therefore preserves exact case for double-hash tokens even though ordinary command lookup is normalised for search.

# Part II: Context Is Part of Syntax

## The same spelling can serve several object languages

The register identifies 107 tokens whose official definition contexts span more than one command domain. Familiar examples include `#name`, `#descr`, `#clear`, `#end`, `#att`, `#def`, `#range`, `#sound`, `#sample`, `#homerealm`, and `#magic`.

This is not accidental duplication. Dominions exposes related fields through separate object parsers. A command can therefore be legitimate in several places while accepting different arguments or changing different records. A flat alphabetical glossary that retains only one definition will inevitably mislead readers.

Every context-sensitive record in the data layer retains:

- each official manual;
- the manual's internal version;
- the printed page;
- section and subsection;
- evidence strength;
- the syntax line where one is present;
- a domain-specific canonical destination.

## Selection establishes the target

Selectors such as `#selectweapon`, `#selectarmor`, `#selectmonster`, `#selectnation`, `#selectspell`, and their counterparts establish which object receives subsequent changes. Creation commands such as `#newweapon`, `#newmonster`, and `#newspell` create a target and then open its modification context.

The selector line is part of the meaning of every command beneath it. Removing a selector while copying a snippet can redirect valid commands into the preceding object. This failure can survive superficial review because each individual line is spelled correctly.

## `#end` closes a context, not a universal transaction

`#end` appears throughout the manuals. Its practical role is determined by the active parser. A missing `#end` can cause later commands to be swallowed by the wrong block; an extra one can close a block early. Source formatting should make block boundaries visually obvious even though indentation itself is not the primary parser rule.

A robust block convention uses:

- one blank line before a selector or creator;
- a comment naming the object's stable ID and purpose;
- consistent indentation for commands inside the block;
- an explicit `#end` aligned with the opening selector;
- a validation check that counts and pairs block openings with endings where the language permits that static test.

## Load order changes what context can see

Dominions parses object categories in a documented order and loads each mod as a whole. A reference that appears later in the file can still work when its object category is parsed earlier, while a reference into a different enabled mod may fail even when the other file appears above it in a user's preference screen.

The command lexicon does not attempt to encode every cross-object dependency. It supplies domain and manual context. Book VIII, Part I owns parser order; Book VIII, Part XI owns compatibility engineering.

## A syntax locator is not a compatibility promise

An officially defined command can still be unsafe in a particular project. Common causes include:

- both mods selecting and altering the same vanilla object;
- automatic IDs shifting after new content is inserted;
- a copied object inheriting fields that a later version added;
- event codes colliding between unrelated projects;
- a template alias being legal only for some terrain variants;
- a command added after the minimum game version declared by the mod;
- a mid-game change altering the meaning of identities already stored in the save.

The presence of a command in this lexicon establishes retrievability, not project compatibility.

# Part III: The Evidence Ladder and Version Drift

## Official definition

A defined token has a bold syntax or definition line in one of the current official manuals. This is the strongest documentation state in the register. It establishes the printed spelling, argument form, page, and object context. It may also supply constraints in the surrounding manual prose that the website register deliberately does not reproduce.

The register is a locator, not a replacement copy of the manuals. After a command is found, the cited page remains the authoritative place to read its complete official explanation.

## Official reference-only entry

Sixty tokens occur only in an official list or example-style block. Several monster abilities fall into this category, including commands gathered in the Modding Manual's compact monster-command pages. Other entries are message substitutions printed as reference tables.

Reference-only does not mean unofficial. It means the official document supports the spelling or existence without supplying a full definition line. Behavioural summaries should not be invented to fill that gap. A verified mod example or controlled runtime test can add evidence later, but it must remain labelled separately from the manual.

## Official mention-only entry

Nine tokens have only prose mentions in the current documents: `#afflictions`, `#airattuned`, `#coldrec`, `#dom6title`, `#fireattuned`, `#forestrec`, `#heatrec`, `#multihero1`, and `#nogeosrc`.

Some are understandable through a nearby template or surrounding discussion. Others expose a documentation gap. Mention-only status prevents an incidental sentence from being promoted into a complete syntax contract.

## Official patch evidence

Patch announcements answer historical questions: when a token was added, corrected, expanded, deprecated, or discussed. They rarely define the entire command. Book XIII preserves the complete announcement chronology and record identity. Book XIV links each extracted token to that chronology and then asks whether current manual documentation matches it.

Of the 221 patch-note tokens:

- 196 match current official definitions exactly;
- two match current official reference-only entries;
- sixteen resolve through official templates;
- three require controlled spelling reconciliation;
- three are family shorthand rather than literal commands;
- one is a double-hash message placeholder rather than a command.

This distribution is the clearest reason not to publish a raw patch-token list as a command manual.

## Patch wording can be historically exact and operationally incomplete

The official announcement is preserved as the historical source even when a later manual clarifies a different spelling. The patch ledger should not be rewritten to make the historical text look cleaner. The command lexicon instead creates a reconciliation record containing the patch token, present locator, resolution status, note, version, record ID, and source locator.

That separation protects both forms of truth:

- Book XIII answers what the announcement said;
- Book XIV answers how that expression relates to the current official documentation.

## Three controlled spelling discrepancies

### `#addseduction` and `#addseductions`

The 6.12 announcement says `#addseduction`. The Event Modding Manual 6.29 defines `#addseductions <value>`. The lexicon preserves the singular patch token and resolves it to the plural manual command. No claim is made that both spellings are accepted by the executable.

### `#illusionimmune` and `#illusionsimmune`

The 6.08 announcement says `#illusionimmune`. The Modding Manual 6.34 defines `#illusionsimmune`. The plural form receives the manual locator; the singular form remains a historical alias marked as a mismatch.

### `#res_mnrbs` and `#req_mnrbs`

The 6.34 announcement says `#res_mnrbs`. The Event Modding Manual 6.29 defines `#req_mnrbs`. Since the manual predates the announcement, the difference could represent a patch-note typo, a renamed command, or an undocumented second form. Official text alone does not determine which spellings the 6.35 executable accepts. The controlled mapping supports retrieval, while runtime acceptance remains a separate question.

## Three family expressions

The extracted token `#not` comes from the announcement expression `#not(dis)mounted`. It resolves to `#notmounted` and `#notdismounted`; there is no literal `#not` command claim.

The extracted token `#force` comes from `#force...vis`. It resolves to the documented forced-gem event-effect family: `#force1d3vis`, `#force1d6vis`, `#force2d4vis`, `#force2d6vis`, `#force3d6vis`, and `#force4d6vis`.

The expression `#battlesum1dX` uses a capital X as a family placeholder. The current manual defines `#battlesum1d2` and `#battlesum1d3`. The lexicon links the patch expression to both.

## The patch placeholder `##varXXX##`

The 6.16 announcement describes `##varXXX##` for printing event variables in messages. The patch importer captured the inner `#varXXX` token because it was designed to find hash expressions. Book XIV corrects the *classification*, not the historical record: this is a double-hash message pattern, not a command line.

# Part IV: Command Domains

## Why domains matter

Alphabetical search is good for a known spelling. Domain search is better when the desired operation is known but the command name is not. The register assigns each occurrence to an object language using its official manual, page, section, and subsection. A token can belong to more than one domain.

| Domain | Distinct tokens | What the domain controls | Canonical design route |
|---|---:|---|---|
| Monster modding | 584 | Units, commanders, attributes, movement, leadership, magic, forms, mounts, and abilities | Book VIII, Part IV |
| Event modding | 403 | Event requirements, targets, effects, variables, codes, messages, and global events | Book VIII, Part VII |
| Nation modding | 169 | National identity, recruitment, defence, gods, forts, dominion, and reanimation | Book VIII, Part V |
| Weapon modding | 121 | Damage, delivery, qualifiers, secondary effects, and after-effects | Book VIII, Part III |
| Site modding | 112 | Site identity, income, recruitment, scales, rituals, and throne effects | Book VIII, Part V |
| Spell modding | 105 | Research, paths, fatigue, effects, targeting, AI hints, and globals | Book VIII, Part VI |
| Magic-item modding | 102 | Construction, paths, powers, restrictions, and carried abilities | Book VIII, Part VI |
| Map making | 69 | Map identity, provinces, neighbours, terrain, starts, scenario contents, and planes | Book VIII, Part IX |
| General modding | 40 | Cross-object and global configuration | Book VIII, Parts I-II |
| Bless modding | 21 | Bless identity, requirements, effects, and scale conditions | Book VIII, Part VI |
| Mercenary modding | 16 | Company identity, units, price, timing, and availability | Book VIII, Part VI supporting objects |
| Armour modding | 15 | Protection, defence, encumbrance, material, and type | Book VIII, Part III |
| Population-type modding | 13 | Independent population recruitment packages | Book VIII, Part VI supporting objects |
| Sound modding | 11 | Samples, modes, loops, and audio import | Book VIII, Part II |
| AI modding | 10 | Template construction, Pretender design, and research targets | Book VIII, Part X |
| Mod metadata | 5 | Display name, description, icon, version, and required game version | Book VIII, Part II |
| Name modding | 4 | Name-table selection, clearing, and addition | Book VIII, Part VI supporting objects |

Counts overlap where a token has several contexts. They measure retrievable language surface, not relative strategic importance.

## Mod metadata and sound

Metadata commands make a mod identifiable to the game and to players. A stable display name, meaningful version, clear description, and suitable icon are part of release engineering. `#domversion` deserves particular attention because it communicates a minimum executable version; leaving it absent does not make newer commands compatible with older builds.

Sound commands form a compact object language with selectors, import paths, sample modes, and looping rules. Filename and network-lobby constraints apply just as strongly to audio assets as to sprites and map files.

## Weapons and armour

Weapon syntax separates base damage, number of attacks, attack and defence modifiers, length, range, ammunition, damage type, resistance interactions, targeting qualifiers, secondary effects, and post-hit effects. Similar-looking commands can belong to spell or item contexts as well, so the domain locator should be checked before reusing a line.

Armour commands are fewer but strongly coupled: protection, defence, encumbrance, resource cost, armour type, and material interact with unit statistics and damage resolution. The lexicon identifies syntax; Book IV owns combat interpretation and Book VIII owns object construction.

## Monsters, commanders, mounts, and forms

Monster modding is the largest language surface in the general manual. It includes statistics, costs, recruitment rules, body types, slots, creature status, movement, stealth, healing, reduction, immortality, auras, seasonal powers, combat abilities, non-combat abilities, shape changes, summons, mounts, leadership, paths, research, gem production, and special magic.

The compact monster-command reference also contains dozens of reference-only tokens. Their presence is official, but complete semantics cannot be inferred from the spelling alone. A command named like a familiar in-game ability may expose only part of that ability or accept values whose interpretation is not shown in the list.

## Names and blessings

Name-table modding is small but identity-sensitive. Clearing a name table and adding names changes a shared resource, not merely one unit's display label.

Bless modding uses familiar generic tokens such as `#name` within a specialised block. Its scale and path requirements are access rules, while effect commands alter sacred units. Strategic blessing design remains in Book III; the lexicon supplies only the language locator.

## Sites and nations

Sites can grant income, recruitment, scales, ritual access, scrying, special effects, and throne powers. Nation blocks then assemble recruitment, province defence, gods, infrastructure, dominion, reanimation, and AI hints into a playable state.

Terrain recruitment is the main template-heavy area. Literal forms such as `#forestrec` and `#dripfortcom` resolve to `(terrain)` definitions. Fort and non-fort variants are distinct, and underwater cases carry explicit exceptions. Search aliases should never erase those restrictions.

## Spells and magic items

Spell commands define access and delivery as well as effects. Research school, level, path requirements, fatigue cost, range, targeting, area, damage, precision, effect numbers, chaining, special attributes, global-enchantment behaviour, rare caster requirements, and AI hints can all matter.

Magic-item commands combine construction access with persistent abilities. Many monster abilities are reused in item context, which makes command collisions common. A token documented for monsters is not automatically documented for items; the entry must contain the item domain or an explicit cross-context statement.

## Events

Event commands are divided into requirements and effects. Requirements filter when, where, for whom, and against which target an event is valid. Effects alter state after selection. Event codes and variables create memory across events. Message substitutions expose names and state inside text. Global events extend the scope beyond one province.

The event language is especially vulnerable to plausible but false assumptions. Several requirements can be combined, repeated, or negated; target requirements do not always select a target by themselves; and a perfectly valid event can remain practically impossible because its conditions never overlap.

## Maps

Map commands define identity, image, size, provinces, connections, names, terrain, colours, starts, victory restrictions, scenario ownership, contents, magic, dominion, scales, and planes. Some commands act on an explicitly numbered province; others operate on the currently active province selected by `#land` or `#setland`.

The distinction between global map state and active-province state is another form of parser context. A copied line can be valid yet alter the wrong province if the selector context is missing.

## AI and general commands

AI modding exposes bounded hints and templates, not a general programmable strategic brain. The language can shape Pretender design, research targets, and some preferences. Book VIII, Part X owns the capability boundary.

General commands affect broader game or mod state. Their apparent simplicity makes them easy to place without considering version, load order, or campaign consequences. Each should be treated as a project-level change.

# Part V: A Safe Lookup Workflow

## Beginner route: from desired result to a valid line

1. Define the object being changed: weapon, armour, monster, site, nation, spell, item, event, map, or another supported type.
2. Search the domain rather than guessing a command name.
3. Open the cited official page and read the surrounding explanation.
4. Confirm whether the entry is defined, reference-only, mentioned-only, or a template.
5. Copy the printed command spelling and replace argument labels deliberately.
6. Confirm the selector or creator that establishes the active object.
7. Confirm whether `#end` is required.
8. Load the smallest possible mod containing only the relevant block.
9. Inspect the resulting object or event before integrating the change into a larger project.
10. Record the game version, manual version, and result.

This route is slower than pasting an isolated line and much faster than debugging a large file whose parser context is already uncertain.

## Expert route: from token to maintenance decision

1. Search the normalised token and all aliases.
2. Review every context when the token is marked context-sensitive.
3. Compare current-manual syntax with every linked patch record.
4. Check the mod's declared minimum game version.
5. Inspect neighbouring source for selector state, copied fields, clearing operations, and identifier ownership.
6. Check combined-load-order overlap with other active mods.
7. Decide whether the change is static, load-validated, object-validated, or behaviour-validated.
8. Preserve a minimal reproduction when runtime evidence adds knowledge beyond the official text.

## When a command is known but its meaning is not

A reference-only or mention-only token should trigger a bounded evidence search:

- read the full surrounding official page;
- search later official patch announcements;
- inspect current official examples if available;
- inspect a reputable working mod while treating it as implementation evidence, not official documentation;
- create a minimal reproduction;
- vary one argument at a time;
- record accepted syntax separately from observed effect;
- avoid generalising beyond the tested version and context.

The absence of an official description is not permission to replace it with a confident guess.

## When a patch token fails to parse

The reconciliation table should be checked before assuming the game rejected a once-valid command. The token may be:

- a family expression such as `#force...vis`;
- a terrain template member;
- a numeric template member;
- a manual spelling mismatch;
- a message placeholder;
- a command added after the running executable;
- a command valid only in another object context.

If none applies, the failure becomes a research item rather than an invitation to cycle through arbitrary spellings.

## Minimal reproduction structure

The smallest useful test file contains metadata, one object, one disputed command, and no unrelated content:

```text
#modname "Command Test"
#description "Isolates one syntax question."
#version 0.01
#domversion 6.37

-- One fixed object, one command under review, one expected result.
#selectmonster 123
  #command_under_test <value>
#end
```

The selected object and command must be appropriate to the test. A disposable copy is preferable when altering a vanilla object would contaminate comparison. Event and map tests require their own minimal harnesses.

## Four different validation claims

| Claim | Evidence required | What remains unproven |
|---|---|---|
| The file parses | Load without a parse error | The command may still have no intended effect |
| The object changes | Inspect the resulting object or exported data | Battle, event, AI, or campaign behaviour may differ |
| The behaviour occurs | Controlled runtime observation | Compatibility and long-term balance remain open |
| The project is releasable | Regression, multiplayer, compatibility, packaging, and version checks | Future patches can still invalidate assumptions |

These claims should not be collapsed into “works.”

## Deprecated commands

The official manuals mark `#coastunit1...3` and `#coastcom1...2` as deprecated. Their presence in the locator supports legacy-source diagnosis, not new use. A deprecated token should remain searchable because removing it would make old mods harder to audit. Search results should place the replacement route and warning ahead of convenience.

## Minimum game version

`#domversion` states the minimum Dominions version required by a mod. The value should follow the newest feature actually required, not the version on the developer's computer by habit. Patch provenance makes that decision more defensible: if a required command first appears in 6.30, a lower declaration needs specific evidence that the command existed earlier.

The first patch mention is not always the true introduction. Some announcements describe a fix to an existing command. Direction and classification must therefore be read with the version, not inferred from date alone.

# Part VI: Patch-to-Manual Reconciliation

## The controlled exceptions

The following table contains every patch token that does not resolve as an exact current-manual token. Exact matches remain available in the full patch index.

<!-- GENERATED:BEGIN patch-exceptions -->
| Patch token | Reconciliation | Resolves to | Version | Editorial note |
|---|---|---|---:|---|
| `#addseduction` | manual spelling mismatch | `#addseductions` | 6.12 | The update announcement uses the singular form; the Event Modding Manual defines the plural command. |
| `#battlesum1dx` | family shorthand | `#battlesum1d2`, `#battlesum1d3` | 6.27 | The capital X denotes the dice-size family rather than a literal lower-case command. |
| `#coastcom1` | template alias | `#coastcom1...2` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#coastfortcom` | template alias | `#(terrain)fortcom` | 6.05 | The literal form is generated by an official terrain or numeric command template. |
| `#coastfortrec` | template alias | `#(terrain)fortrec` | 6.05 | The literal form is generated by an official terrain or numeric command template. |
| `#coastunit1` | template alias | `#coastunit1...3` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#deeprec` | template alias | `#(terrain)rec` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#dripfortrec` | template alias | `#(terrain)fortrec` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#driprec` | template alias | `#(terrain)rec` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#force` | family shorthand | `#force1d3vis`, `#force1d6vis`, `#force2d4vis`, `#force2d6vis`, `#force3d6vis`, `#force4d6vis` | 6.06 | Extracted from #force...vis; resolve to the documented forced-gem event-effect family. |
| `#forestfortcom` | template alias | `#(terrain)fortcom` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#forestfortrec` | template alias | `#(terrain)fortrec` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#illusionimmune` | manual spelling mismatch | `#illusionsimmune` | 6.08 | The update announcement uses the singular form; the Modding Manual defines #illusionsimmune. |
| `#kelpcom` | template alias | `#(terrain)com` | 6.24 | The literal form is generated by an official terrain or numeric command template. |
| `#kelprec` | template alias | `#(terrain)rec` | 6.04, 6.24 | The literal form is generated by an official terrain or numeric command template. |
| `#not` | family shorthand | `#notmounted`, `#notdismounted` | 6.12 | Extracted from the official expression #not(dis)mounted; it is not a literal #not command. |
| `#plaincom` | template alias | `#(terrain)com` | 6.24 | The literal form is generated by an official terrain or numeric command template. |
| `#plainfortcom` | template alias | `#(terrain)fortcom` | 6.24 | The literal form is generated by an official terrain or numeric command template. |
| `#plainfortrec` | template alias | `#(terrain)fortrec` | 6.24 | The literal form is generated by an official terrain or numeric command template. |
| `#plainrec` | template alias | `#(terrain)rec` | 6.24 | The literal form is generated by an official terrain or numeric command template. |
| `#res_mnrbs` | manual spelling mismatch | `#req_mnrbs` | 6.34 | The 6.34 announcement says #res_mnrbs; the Event Modding Manual defines #req_mnrbs. |
| `#searec` | template alias | `#(terrain)rec` | 6.04 | The literal form is generated by an official terrain or numeric command template. |
| `#varxxx` | message placeholder | Message grammar; no command target | 6.16 | This is the ##varXXX## event-message substitution pattern, not a hash command. |
<!-- GENERATED:END patch-exceptions -->

## How to read the table

A template alias resolves a concrete spelling to the official template that defines the family. A spelling mismatch preserves both source forms. A family shorthand expands an announcement expression into documented members. A message placeholder changes grammar class. None of these mappings asserts that every displayed form is accepted literally by the executable.

## Exact matches still require context

An exact string match is not the end of analysis. `#clear`, `#name`, and `#end` all have exact definitions in several object contexts. The patch record establishes a historical change, while the manual entry establishes a current locator. The active object still determines practical meaning.

## A patch can correct behaviour without changing syntax

Many patch records say that a command “didn't work,” accepted a wider value, became valid in another context, or was deprecated. The syntax before and after the patch can be identical. A current command index therefore needs both syntax status and behavioural history.

Book XIII remains the place to inspect the full release context. The command register stores only the links needed to move between the present locator and the historical ledger.

# Part VII: Search and Website Architecture

## One content identity, several views

The PDF and website should not maintain separate command facts. Both are generated from the same record identity. The website can provide several views without duplicating content:

- alphabetical command search;
- domain browser;
- manual and page browser;
- patch-version browser;
- documentation-gap queue;
- context-collision view;
- template and alias explorer;
- deprecated-command list;
- message-substitution reference;
- canonical links into Book VIII and Book XIII.

## Command record fields

Each record contains:

| Field | Purpose |
|---|---|
| `id` | Stable website and data identity |
| `command` | Officially printed token spelling |
| `normalized_command` | Search key; ordinary commands are case-normalised |
| `command_kind` | Literal command, template, or message placeholder |
| `documentation_status` | Defined, reference-only, or mentioned-only |
| `domains` | Every official object-language context located |
| `families` | Search facets such as requirements, lifecycle, events, maps, or magic |
| `manual_entries` | Manual ID, version, page, section, evidence, and syntax locator |
| `patch_records` | Linked version, patch record, source, class, and direction |
| `canonical_section_ids` | Reader destinations that own the surrounding explanation |
| `cautions` | Context, template, and documentation-gap warnings |
| `record_hash` | Stable integrity fingerprint for change detection |

## Alias records are explicit

An alias record contains the searchable literal form, the official template it resolves to, the derivation basis, and a synthetic flag. It does not copy the template definition into a second command record. This keeps search convenient without creating false official entries.

## Patch reconciliation is a separate relation

The patch relation retains the historical token even when it differs from the current manual. Its status and note explain the mapping. This design prevents a later manual update from rewriting the patch archive and prevents a historical typo from contaminating current syntax search.

## Useful search filters

Practical website filters include:

- exact spelling;
- substring or prefix;
- command kind;
- domain;
- manual version;
- documentation status;
- patch version;
- patch classification;
- direction such as added, corrected, deprecated, or changed;
- context-sensitive only;
- template-derived aliases only;
- entries needing runtime work.

Search results should show the caution before the syntax when an entry is ambiguous or incomplete.

## Search examples

| Research question | Effective query |
|---|---|
| Which commands control event targets? | Domain `event-modding`, prefix `#req_targ` |
| Where is a concrete terrain recruit command documented? | Search literal alias, then open its `(terrain)` template |
| Which patch-added commands still lack full definitions? | Has patch record, status `reference-only` or `mentioned-only` |
| Which spell commands changed after the Event Manual's version? | Domain `spell-modding`, patch version greater than the relevant manual baseline |
| Which spellings are unsafe to treat as literal? | Reconciliation status `family-shorthand` or `message-placeholder` |
| Which tokens need object context before use? | `cautions` contains context-sensitive warning |

## Schema and integrity checks

The JSON schema validates required identity, status, domain, locator, and hash fields. Additional semantic checks are still necessary:

- command and ID uniqueness;
- valid manual IDs;
- pages within each manual's page count;
- every alias target exists;
- every patch record ID exists in the official ledger;
- every patch token has one reconciliation outcome;
- no unresolved patch token is published as complete;
- status totals match the record collection;
- every canonical destination resolves in website navigation.

# Part VIII: Expert Essays

## Essay I: Syntax Is Not Semantics

Syntax answers whether a line belongs to the language. Semantics answers what state that line changes. Operational behaviour answers what happens when the state enters the game. Strategy answers whether that result is useful. Compatibility answers whether the project remains coherent beside other projects and across versions.

Dominions mod discussions often skip directly from syntax to strategy. A command is found, a line parses, and a broad claim follows. Each skipped layer creates a different risk. A correctly parsed event requirement may make an event impossible. A correctly displayed ability may apply to a mount rather than its rider. A correctly modified spell may never be selected by AI casting logic. A strategically interesting unit may collide with another mod's identifier.

The lexicon deliberately stops at retrieval and evidence. That limit makes it more useful, not less. A clear boundary allows every later claim to cite the right layer instead of treating a command name as proof of an entire system.

## Essay II: Command Context Is a Public Interface

A mod file looks like a private implementation detail, but every released command block becomes part of a public interface. Save files retain identities. Compatibility patches select objects. Other maintainers read names and number ranges. Players depend on declared versions and load order. Workshop updates replace files inside ongoing campaigns.

Context-sensitive commands reveal this interface most clearly. `#name` is not a single global naming function; it is a family of fields exposed through different object parsers. The selector, parser phase, object ID, and closing boundary are part of the contract.

Good source makes that contract legible. It freezes identifiers, documents ranges, isolates object blocks, states dependencies, and avoids unnecessary selection of shared vanilla objects. Poor source can still load, but it forces every later maintainer to reconstruct the contract from behaviour.

## Essay III: Patch Notes Are Change Evidence, Not a Replacement Manual

Patch notes are written to explain what changed. Compression is useful in that setting. `#force...vis` efficiently tells experienced modders that a family was fixed. `#not(dis)mounted` compactly names two related commands. “New nation commands: `#forestfortrec`, `#forestfortcom`, etc.” signals a broader addition without printing a grammar.

The same compression becomes hazardous when harvested into a reference. Ellipses look like literal characters. Parentheses look like optional text. Singular and plural spellings become competing commands. A message placeholder becomes a single-hash token after naive extraction.

The solution is not to distrust patch notes. It is to preserve their purpose. Book XIII stores change evidence. Book XIV reconciles expressions to present documentation. Neither source is forced to do the other's job.

## Essay IV: Templates Are Grammars, Not Abbreviations

A template such as `#(terrain)rec` defines a productive rule: substitute an allowed terrain word to create a literal command. This is more powerful than an ordinary abbreviation because it can generate forms not separately listed. It is also more dangerous because readers can generate plausible but invalid forms.

Formal grammar has constraints. The manual's terrain list, fort exceptions, and underwater alternatives define the valid language. A search system should expose those constraints with the template. Generating aliases without a target link produces convenient misinformation; refusing to generate aliases makes ordinary source unnecessarily hard to search.

The controlled alias is the middle path. It states that the concrete term is derived, records the official template, and retains the synthetic status. Search becomes broader while evidence remains exact.

## Essay V: Documentation Gaps Should Remain Visible

A reference-only command creates an uncomfortable blank. The token is official, but the intended value range or detailed behaviour may not be printed. There is a temptation to fill the gap with community consensus and remove the warning once a likely explanation appears.

That approach destroys useful information. A later reader can no longer tell which part came from Illwinter, which part came from a working mod, and which part came from a test. The confident summary may remain correct for years, yet its evidence chain has been lost.

A visible gap supports cumulative research. Official existence, community implementation, runtime acceptance, observed effect, version, and test conditions can each be recorded. Later evidence adds a layer instead of replacing the uncertainty with anonymous certainty.

# Part IX: Maintenance and Review Protocols

## Before adding a command to a project

- Confirm the object domain.
- Open the official locator rather than relying on the command name.
- Verify every argument and alternative form.
- Check whether the token is a template or message substitution.
- Check linked patch records.
- Confirm the minimum executable version.
- Inspect selector, copy, clear, and `#end` context.
- Check identifier ownership and combined-mod overlap.
- Build a minimal reproduction for incomplete behaviour.
- Record the evidence level beside the design decision.

## When reviewing a legacy mod

- Record the mod version and original game baseline.
- Extract every hash token without assuming all are commands.
- Resolve template members and deprecated families.
- Identify tokens absent from the current official register.
- Compare context-sensitive syntax against the active selector.
- Flag automatic IDs and shared event codes.
- Preserve old spellings until acceptance has been tested.
- Separate parser migration from balance changes.
- Test a clean new game before testing a historical save.
- Publish the compatibility boundary.

## When an official source disagrees with another official source

- Preserve both spellings or statements.
- Record source version and date.
- Determine whether one source describes history and the other current syntax.
- Search later official corrections.
- Avoid inventing a winner when runtime evidence is absent.
- Test both forms in the smallest valid context if acceptance matters.
- Report the result as versioned runtime evidence.

## When a new patch arrives

1. Archive the official announcement and metadata.
2. Rebuild the official patch ledger.
3. Extract candidate commands and message tokens.
4. Compare them with exact manual tokens.
5. Resolve templates, family expressions, and spelling discrepancies explicitly.
6. Download and hash any updated manuals.
7. Rebuild the command register and schema validation.
8. Review documentation-status changes.
9. Update Book XIII chronology only for historical change.
10. Update Book XIV only for syntax, context, provenance, or retrieval changes.
11. Re-run navigation, duplicate, voice, and visual checks.
12. Publish a bounded change note.

## Documentation-defect report

A useful report contains:

- game version;
- manual title and internal version;
- page and section;
- exact printed token;
- conflicting official token or patch record;
- minimal valid block;
- parser result;
- observed behaviour;
- save, mods, and load order where relevant;
- a statement separating observation from inference.

This format is far more actionable than “the command does not work.”

# Part X: Complete Search Locators

## How to use the appendices

The following appendices are mechanically generated from the validated command register. Their compact entries are locators rather than replacements for the official explanations. “Defined” points to an official syntax line. “Reference” marks an official list or example entry. “Mention” marks prose-only evidence. Template and message tokens retain their grammar class.

The first locator contains every distinct hash token found in the current official manuals. The patch column shows the first linked version when Book XIII contains a command record. The syntax column preserves the strongest official syntax line without copying the manual's explanatory prose.

<!-- GENERATED:BEGIN command-locator -->
### Templates

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#(path)attuned` | Defined | Monster | M6.34 p28 | `#(path)attuned <chance>` |
| `#(terrain)com` | Defined; template | Nation | M6.34 p45 | `#(terrain)com "<monster name>" \| <monster nbr>` |
| `#(terrain)fortcom` | Defined; template | Nation | M6.34 p45 | `#(terrain)fortcom "<monster name>" \| <monster nbr>` |
| `#(terrain)fortrec` | Defined; template | Nation | M6.34 p45 | `#(terrain)fortrec "<monster name>" \| <monster nbr>` |
| `#(terrain)rec` | Defined; template | Nation | M6.34 p45 | `#(terrain)rec "<monster name>" \| <monster nbr>` |

### 0-9

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#10d6units` | Defined | Event | E6.29 p14 | `#10d6units "name" \| <number>` |
| `#11d6units` | Defined | Event | E6.29 p14 | `#11d6units "name" \| <number>` |
| `#12d6units` | Defined | Event | E6.29 p14 | `#12d6units "name" \| <number>` |
| `#13d6units` | Defined | Event | E6.29 p14 | `#13d6units "name" \| <number>` |
| `#14d6units` | Defined | Event | E6.29 p14 | `#14d6units "name" \| <number>` |
| `#15d6units` | Defined | Event | E6.29 p14 | `#15d6units "name" \| <number>` |
| `#16d6units` | Defined | Event | E6.29 p15 | `#16d6units "name" \| <number>` |
| `#1d3units` | Defined | Event | E6.29 p14 | `#1d3units "name" \| <number>` |
| `#1d3vis` | Defined | Event | E6.29 p12 | `#1d3vis <gem type>` |
| `#1d6units` | Defined | Event | E6.29 p14 | `#1d6units "name" \| <number>` |
| `#1d6vis` | Defined | Event | E6.29 p12 | `#1d6vis <gem type>` |
| `#1unit` | Defined | Event | E6.29 p14 | `#1unit "name" \| <number>` |
| `#2com` | Defined | Event | E6.29 p14 | `#2com "name" \| <number>` |
| `#2d3units` | Defined | Event | E6.29 p14 | `#2d3units "name" \| <number>` |
| `#2d4vis` | Defined | Event | E6.29 p12 | `#2d4vis <gem type>` |
| `#2d6units` | Defined | Event | E6.29 p14; E6.29 p19; E6.29 p20 | `#2d6units "name" \| <number>` |
| `#2d6vis` | Defined | Event | E6.29 p12 | `#2d6vis <gem type>` |
| `#3castbattlespell` | Defined | Monster | M6.34 p35 | `#3castbattlespell "<spell name>" \| <nbr>` |
| `#3d3units` | Defined | Event | E6.29 p14 | `#3d3units "name" \| <number>` |
| `#3d6units` | Defined | Event | E6.29 p14; E6.29 p19 | `#3d6units "name" \| <number>` |
| `#3d6vis` | Defined | Event | E6.29 p12 | `#3d6vis <gem type>` |
| `#4com` | Defined | Event | E6.29 p14 | `#4com "name" \| <number>` |
| `#4d3units` | Defined | Event | E6.29 p14 | `#4d3units "name" \| <number>` |
| `#4d6units` | Defined | Event | E6.29 p14 | `#4d6units "name" \| <number>` |
| `#4d6vis` | Defined | Event | E6.29 p12 | `#4d6vis <gem type>` |
| `#5com` | Defined | Event | E6.29 p14 | `#5com "name" \| <number>` |
| `#5d6units` | Defined | Event | E6.29 p14; E6.29 p20 | `#5d6units "name" \| <number>` |
| `#6d6units` | Defined | Event | E6.29 p14 | `#6d6units "name" \| <number>` |
| `#7d6units` | Defined | Event | E6.29 p14 | `#7d6units "name" \| <number>` |
| `#8d6units` | Defined | Event | E6.29 p14 | `#8d6units "name" \| <number>` |
| `#9d6units` | Defined | Event | E6.29 p14 | `#9d6units "name" \| <number>` |

### A

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#acid` | Defined | Weapon | M6.34 p9 | `#acid` |
| `#aciddigest` | Defined | Monster | M6.34 p25; M6.34 p59 | `#aciddigest <dmg>` |
| `#acidres` | Defined | Item, Monster | M6.34 p22; M6.34 p56 | `#acidres <prot>` |
| `#acidshield` | Defined | Monster | M6.34 p24; M6.34 p59 | `#acidshield <damage>` |
| `#addascension` | Defined | Event | E6.29 p18 | `#addascension <AP>` |
| `#addequip` | Defined | Event | E6.29 p15 | `#addequip <equipment level>` |
| `#addforeigncom` | Defined | Nation | M6.34 p45 | `#addforeigncom "<monster name>" \| <monster nbr>` |
| `#addforeignunit` | Defined | Nation | M6.34 p45 | `#addforeignunit "<monster name>" \| <monster nbr>` |
| `#addgeo` | Defined | Event | E6.29 p13 | `#addgeo <terrain bitmask>` |
| `#addgod` | Defined | Nation | M6.34 p47 | `#addgod "<monster name>" \| <nbr>` |
| `#additem` | Defined | Map | P6.26 p9 | `#additem "<item name>"` |
| `#addkills` | Defined | Event | E6.29 p16 | `#addkills <value>` |
| `#addname` | Defined | Names | M6.34 p36 | `#addname "name"` |
| `#addrandomage` | Defined | Monster | M6.34 p21 | `#addrandomage <years>` |
| `#addreccom` | Defined | Nation, Poptype | M6.34 p45; M6.34 p63 | `#addreccom "<monster name>" \| <monster nbr>` |
| `#addrecunit` | Defined | Nation, Poptype | M6.34 p45; M6.34 p63 | `#addrecunit "<monster name>" \| <monster nbr>` |
| `#addseductions` | Defined | Event | E6.29 p16 | `#addseductions <value>` |
| `#addsite` | Defined | Event | E6.29 p13 | `#addsite <site number>` |
| `#addupkeep` | Defined | Monster | M6.34 p27; M6.34 p60 | `#addupkeep <gold>` |
| `#adeptsacr` | Defined | Monster | M6.34 p27; M6.34 p60 | `#adeptsacr <value>` |
| `#adventureruin` | Defined | Site | M6.34 p40 | `#adventureruin <success chance>` |
| `#afflictions` | Mention | Weapon | M6.34 p8 | `#afflictions` |
| `#aftercloud` | Defined | Weapon | M6.34 p12 | `#aftercloud <cloudstr> <cloudtype>` |
| `#aftercloudarea` | Defined | Weapon | M6.34 p12 | `#aftercloudarea <aoe>` |
| `#aiairnation` | Defined | Nation | M6.34 p44 | `#aiairnation` |
| `#aiassmod` | Defined | Spell | M6.34 p55 | `#aiassmod <bonus>` |
| `#aiastralnation` | Defined | Nation | M6.34 p44 | `#aiastralnation` |
| `#aiawake` | Defined | Nation | M6.34 p44 | `#aiawake <percent>` |
| `#aibadlvl` | Defined | Spell | M6.34 p55 | `#aibadlvl <level>` |
| `#aibloodnation` | Defined | Nation | M6.34 p44 | `#aibloodnation` |
| `#aicheapholy` | Defined | Nation | M6.34 p44 | `#aicheapholy` |
| `#aideathnation` | Defined | Nation | M6.34 p44 | `#aideathnation` |
| `#aiearthnation` | Defined | Nation | M6.34 p44 | `#aiearthnation` |
| `#aifirenation` | Defined | Nation | M6.34 p44 | `#aifirenation` |
| `#aiglamournation` | Defined | Nation | M6.34 p44 | `#aiglamournation` |
| `#aigoodbless` | Defined | Nation | M6.34 p44 | `#aigoodbless <0-100>` |
| `#aiheavyrec` | Defined | Nation | M6.34 p44 | `#aiheavyrec <0-99>` |
| `#aiholdgod` | Defined | Nation | M6.34 p44 | `#aiholdgod` |
| `#aiholyranged` | Defined | Nation | M6.34 p44 | `#aiholyranged` |
| `#aimagerec` | Defined | Nation | M6.34 p44 | `#aimagerec <0-99>` |
| `#aimusthavemag` | Defined | Nation | M6.34 p44 | `#aimusthavemag <magic path number>` |
| `#ainaturenation` | Defined | Nation | M6.34 p44 | `#ainaturenation` |
| `#ainocast` | Defined | Spell | M6.34 p55 | `#ainocast <0 or 1>` |
| `#ainorec` | Defined | Monster | M6.34 p15 | `#ainorec` |
| `#airattuned` | Mention | Monster | M6.34 p28 | `#airattuned` |
| `#airblessbonus` | Defined | Nation | M6.34 p47 | `#airblessbonus <0 - 9>` |
| `#airboost` | Defined | Event | E6.29 p16 | `#airboost "name" \| <number>` |
| `#airelementals` | Defined | Monster | M6.34 p30; M6.34 p61 | `#airelementals <bonus>` |
| `#airrange` | Defined | Monster, Site | M6.34 p33; M6.34 p39; M6.34 p60 | `#airrange <range>` |
| `#airshield` | Defined | Monster | M6.34 p23; M6.34 p59 | `#airshield <percent>` |
| `#aisinglerec` | Defined | Monster | M6.34 p15 | `#aisinglerec` |
| `#aispellmod` | Defined | Spell | M6.34 p55 | `#aispellmod <bonus>` |
| `#aiwaternation` | Defined | Nation | M6.34 p44 | `#aiwaternation` |
| `#alchemy` | Defined | Monster | M6.34 p27; M6.34 p60 | `#alchemy <percent>` |
| `#allowedplayer` | Defined | Map | P6.26 p5 | `#allowedplayer <nation nbr>` |
| `#allrange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#allrange <range>` |
| `#allret` | Defined | Monster | M6.34 p35; M6.34 p60 | `#allret <chance>` |
| `#almostliving` | Defined | Monster | M6.34 p32 | `#almostliving` |
| `#almostundead` | Defined | Monster | M6.34 p32 | `#almostundead` |
| `#altcost` | Defined | Site | M6.34 p39 | `#altcost <bonus>` |
| `#ambidextrous` | Defined | Monster | M6.34 p25; M6.34 p59 | `#ambidextrous <bonus>` |
| `#ammo` | Defined | Weapon | M6.34 p7 | `#ammo` |
| `#amphibian` | Defined | Monster | M6.34 p19 | `#amphibian` |
| `#animal` | Defined | Monster | M6.34 p19 | `#animal` |
| `#animalawe` | Defined | Monster | M6.34 p23; M6.34 p59 | `#animalawe <bonus>` |
| `#animated` | Defined | Monster | M6.34 p28 | `#animated "<monster name>" \| <monster nbr>` |
| `#aoe` | Defined | Spell, Weapon | M6.34 p10; M6.34 p51 | `#aoe <squares>` |
| `#ap` | Defined | Monster | M6.34 p17 | `#ap <action points>` |
| `#appetite` | Defined | Monster | M6.34 p26 | `#appetite <value>` |
| `#aquatic` | Defined | Monster | M6.34 p19 | `#aquatic` |
| `#arena` | Defined | Event | E6.29 p18 | `#arena` |
| `#arenagems` | Defined | General | M6.34 p62 | `#arenagems <amount>` |
| `#arenagold` | Defined | General | M6.34 p62 | `#arenagold <amount>` |
| `#armor` | Defined | Item, Weapon | M6.34 p17; M6.34 p56 | `#armor "<armor name>" \| <armor nbr>` |
| `#armornegating` | Defined | Weapon | M6.34 p9 | `#armornegating` |
| `#armorpiercing` | Defined | Weapon | M6.34 p9 | `#armorpiercing` |
| `#assassin` | Defined | Event, Monster | E6.29 p14; M6.34 p20; M6.34 p60 | `#assassin "name" \| <number>` |
| `#assencloc` | Defined | Monster | M6.34 p21 | `#assencloc <value>` |
| `#assfollower1` | Defined | Event | E6.29 p14 | `#assfollower1 "name" \| <number>` |
| `#assfollower1d3` | Defined | Event | E6.29 p14 | `#assfollower1d3 "name" \| <number>` |
| `#assfollower2` | Defined | Event | E6.29 p14 | `#assfollower2 "name" \| <number>` |
| `#assfollower3` | Defined | Event | E6.29 p14 | `#assfollower3 "name" \| <number>` |
| `#assowner` | Defined | Event | E6.29 p14 | `#assowner <nation number>` |
| `#assownerench` | Defined | Event | E6.29 p14 | `#assownerench <ench nbr>` |
| `#astralblessbonus` | Defined | Nation | M6.34 p47 | `#astralblessbonus <0 - 9>` |
| `#astralboost` | Defined | Event | E6.29 p16 | `#astralboost "name" \| <number>` |
| `#astralrange` | Defined | Monster, Site | M6.34 p33; M6.34 p39; M6.34 p60 | `#astralrange <range>` |
| `#att` | Defined | Item, Monster, Weapon | M6.34 p7; M6.34 p16; M6.34 p56; M6.34 p9 | `#att <attack>` |
| `#autoberserk` | Defined | Monster | M6.34 p25 | `#autoberserk <value>` |
| `#autobless` | Defined | Item | M6.34 p57 | `#autobless` |
| `#autocompete` | Defined | Item, Monster | M6.34 p19; M6.34 p58 | `#autocompete` |
| `#autocorpsehealer` | Defined | Monster | M6.34 p21 | `#autocorpsehealer <value>` |
| `#autodisgrinder` | Defined | Monster | M6.34 p21; M6.34 p59 | `#autodisgrinder <value>` |
| `#autodishealer` | Defined | Monster | M6.34 p21; M6.34 p59 | `#autodishealer <value>` |
| `#autohealer` | Defined | Monster | M6.34 p21; M6.34 p59 | `#autohealer <value>` |
| `#autospell` | Defined | Spell | M6.34 p56 | `#autospell "<spell name>"` |
| `#autospellrepeat` | Defined | Spell | M6.34 p56 | `#autospellrepeat <spells / round>` |
| `#autoundead` | Defined | Nation | M6.34 p49 | `#autoundead` |
| `#autumnshape` | Defined | Monster | M6.34 p28 | `#autumnshape "<monster name>" \| <monster nbr>` |
| `#awe` | Defined | Monster | M6.34 p24; M6.34 p59 | `#awe <bonus>` |

### B

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#badindpd` | Defined | Nation | M6.34 p46 | `#badindpd <0 or 1>` |
| `#banefireshield` | Defined | Monster | M6.34 p24; M6.34 p59 | `#banefireshield <damage>` |
| `#banished` | Defined | Event | E6.29 p15 | `#banished <value>` |
| `#barkskin` | Defined | Item | M6.34 p56 | `#barkskin` |
| `#batmap` | Defined | Map | P6.26 p8 | `#batmap "<battlemap.d3m>` |
| `#batstartsum1` | Reference | Monster | M6.34 p61 | `#batstartsum1` |
| `#batstartsum1...5` | Defined; template | Monster | M6.34 p29 | `#batstartsum1...5 "<monster name>" \| <monster nbr>` |
| `#batstartsum1d3` | Defined | Monster | M6.34 p29 | `#batstartsum1d3 "<monster name>" \| <monster nbr>` |
| `#batstartsum1d6` | Reference | Monster | M6.34 p61 | `#batstartsum1d6` |
| `#batstartsum1d6...9d6` | Defined; template | Monster | M6.34 p29 | `#batstartsum1d6...9d6 "<monster name>" \| <monster nbr>` |
| `#batstartsum2` | Reference | Monster | M6.34 p61 | `#batstartsum2` |
| `#batstartsum2d6` | Reference | Monster | M6.34 p61 | `#batstartsum2d6` |
| `#batstartsum3` | Reference | Monster | M6.34 p61 | `#batstartsum3` |
| `#batstartsum3d6` | Reference | Monster | M6.34 p61 | `#batstartsum3d6` |
| `#batstartsum4` | Reference | Monster | M6.34 p61 | `#batstartsum4` |
| `#batstartsum4d6` | Reference | Monster | M6.34 p61 | `#batstartsum4d6` |
| `#batstartsum5` | Reference | Monster | M6.34 p61 | `#batstartsum5` |
| `#batstartsum5d6` | Reference | Monster | M6.34 p61 | `#batstartsum5d6` |
| `#battleshape` | Defined | Monster | M6.34 p28 | `#battleshape "<monster name>" \| <monster nbr>` |
| `#battlesum1` | Reference | Monster | M6.34 p61 | `#battlesum1` |
| `#battlesum1...5` | Defined; template | Monster | M6.34 p29 | `#battlesum1...5 "<monster name>" \| <monster nbr>` |
| `#battlesum1d2` | Defined | Monster | M6.34 p29; M6.34 p61 | `#battlesum1d2 "<monster name>" \| <monster nbr>` |
| `#battlesum1d3` | Defined | Monster | M6.34 p29; M6.34 p61 | `#battlesum1d3 "<monster name>" \| <monster nbr>` |
| `#battlesum2` | Reference | Monster | M6.34 p61 | `#battlesum2` |
| `#battlesum3` | Reference | Monster | M6.34 p61 | `#battlesum3` |
| `#battlesum4` | Reference | Monster | M6.34 p61 | `#battlesum4` |
| `#battlesum5` | Reference | Monster | M6.34 p61 | `#battlesum5` |
| `#battlesumwarm` | Defined | Monster | M6.34 p29; M6.34 p61 | `#battlesumwarm "<monster name>" \| <monster nbr>` |
| `#beam` | Defined | Weapon | M6.34 p10 | `#beam` |
| `#beartattoo` | Defined | Monster | M6.34 p26 | `#beartattoo <value>` |
| `#beastmaster` | Defined | Monster | M6.34 p32; M6.34 p60 | `#beastmaster <bonus>` |
| `#beckon` | Defined | Monster | M6.34 p21; M6.34 p58 | `#beckon <value>` |
| `#bers` | Defined | Item | M6.34 p56 | `#bers` |
| `#berserk` | Defined | Monster | M6.34 p25; M6.34 p59 | `#berserk <bonus>` |
| `#bestowtomount` | Defined | Item | M6.34 p58 | `#bestowtomount` |
| `#bird` | Defined | Monster | M6.34 p18 | `#bird` |
| `#bless` | Defined | AI, Item | M6.34 p56; M6.34 p64 | `#bless` |
| `#blessairshld` | Defined | Site | M6.34 p41 | `#blessairshld <value>` |
| `#blessanimawe` | Defined | Site | M6.34 p40 | `#blessanimawe <value>` |
| `#blessatt` | Defined | Site | M6.34 p41 | `#blessatt <value>` |
| `#blessawe` | Defined | Site | M6.34 p40 | `#blessawe <value>` |
| `#blessbers` | Defined | Monster | M6.34 p25; M6.34 p59 | `#blessbers` |
| `#blessbonus` | Defined | Nation | M6.34 p47 | `#blessbonus <0 - 9>` |
| `#blesscoldres` | Defined | Site | M6.34 p41 | `#blesscoldres <value>` |
| `#blessdarkvis` | Defined | Site | M6.34 p41 | `#blessdarkvis <value>` |
| `#blessdef` | Defined | Site | M6.34 p41 | `#blessdef <value>` |
| `#blessdtv` | Defined | Site | M6.34 p41 | `#blessdtv <value>` |
| `#blessfireres` | Defined | Site | M6.34 p41 | `#blessfireres <value>` |
| `#blessfly` | Defined | Monster | M6.34 p25; M6.34 p59 | `#blessfly` |
| `#blesshp` | Defined | Site | M6.34 p40 | `#blesshp <value>` |
| `#blessmor` | Defined | Site | M6.34 p40 | `#blessmor <value>` |
| `#blessmr` | Defined | Site | M6.34 p40 | `#blessmr <value>` |
| `#blesspoisres` | Defined | Site | M6.34 p41 | `#blesspoisres <value>` |
| `#blessprec` | Defined | Site | M6.34 p41 | `#blessprec <value>` |
| `#blessreinvig` | Defined | Site | M6.34 p41 | `#blessreinvig <value>` |
| `#blessshockres` | Defined | Site | M6.34 p41 | `#blessshockres <value>` |
| `#blessstr` | Defined | Site | M6.34 p40 | `#blessstr <value>` |
| `#blind` | Defined | Monster | M6.34 p19 | `#blind` |
| `#blink` | Defined | Monster | M6.34 p20 | `#blink` |
| `#bloodblessbonus` | Defined | Nation | M6.34 p47 | `#bloodblessbonus <0 - 9>` |
| `#bloodboost` | Defined | Event | E6.29 p16 | `#bloodboost "name" \| <number>` |
| `#bloodcost` | Defined | Site | M6.34 p39 | `#bloodcost <bonus>` |
| `#bloodnation` | Defined | Nation | M6.34 p44 | `#bloodnation` |
| `#bloodrange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#bloodrange <range>` |
| `#bloodvengeance` | Defined | Monster | M6.34 p24; M6.34 p59 | `#bloodvengeance <strength>` |
| `#blunt` | Defined | Weapon | M6.34 p9 | `#blunt` |
| `#bluntres` | Defined | Monster | M6.34 p22; M6.34 p59 | `#bluntres` |
| `#boartattoo` | Defined | Monster | M6.34 p26 | `#boartattoo <value>` |
| `#bodyguard` | Defined | Monster | M6.34 p32; M6.34 p60 | `#bodyguard <bonus>` |
| `#bodyguards` | Defined | Map | P6.26 p8 | `#bodyguards <nbr> "<type>"` |
| `#bonus` | Defined | Weapon | M6.34 p10 | `#bonus` |
| `#bonusspells` | Defined | Monster | M6.34 p35; M6.34 p60 | `#bonusspells <spells per round>` |
| `#bossname` | Defined | Mercenary | M6.34 p63 | `#bossname "<name>"` |
| `#bowstr` | Defined | Weapon | M6.34 p9 | `#bowstr` |
| `#bravemount` | Defined | Monster | M6.34 p31 | `#bravemount <percent>` |
| `#brief` | Defined | Nation | M6.34 p42 | `#brief "<nation name>"` |
| `#bringeroffortune` | Reference | Monster | M6.34 p36; M6.34 p60 | `#bringeroffortune` |
| `#bug` | Defined | Monster | M6.34 p19 | `#bug` |
| `#bugreform` | Defined | Monster | M6.34 p23 | `#bugreform <nbr of bugs>` |
| `#bugshape` | Defined | Monster | M6.34 p23 | `#bugshape "<monster name>" \| <monster nbr>` |
| `#bugswarmshape` | Defined | Monster | M6.34 p23 | `#bugswarmshape "<monster name>" \| <monster nbr>` |
| `#bugswarmuwshape` | Defined | Monster | M6.34 p23 | `#bugswarmuwshape "<monster name>" \| <monster nbr>` |
| `#buguwshape` | Defined | Monster | M6.34 p23 | `#buguwshape "<monster name>" \| <monster nbr>` |
| `#buildcoastfort` | Defined | Nation | M6.34 p49 | `#buildcoastfort <fort nbr>` |
| `#buildfort` | Defined | Nation | M6.34 p49 | `#buildfort <fort nbr>` |
| `#builduwfort` | Defined | Nation | M6.34 p49 | `#builduwfort <fort nbr>` |

### C

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#cannotwin` | Defined | Map | P6.26 p6 | `#cannotwin <nation nbr>` |
| `#carcasscollector` | Defined | Monster | M6.34 p35; M6.34 p61 | `#carcasscollector <value>` |
| `#castledef` | Defined | Monster | M6.34 p26; M6.34 p60 | `#castledef <value>` |
| `#castleprod` | Defined | Nation | M6.34 p49 | `#castleprod <resource boost in percent>` |
| `#casttime` | Defined | Spell | M6.34 p53 | `#casttime <1-1000>` |
| `#caveinc` | Defined | Site | M6.34 p43 | `#caveinc <bonus>` |
| `#cavelabcost` | Defined | Nation | M6.34 p48 | `#cavelabcost <price>` |
| `#cavenation` | Defined | Site | M6.34 p43 | `#cavenation <0-3>` |
| `#caverecpt` | Defined | Site | M6.34 p43 | `#caverecpt <bonus>` |
| `#caveres` | Defined | Site | M6.34 p43 | `#caveres <bonus>` |
| `#cavetemplecost` | Defined | Nation | M6.34 p48 | `#cavetemplecost <price>` |
| `#champprize` | Defined | Item | M6.34 p58 | `#champprize` |
| `#chaospower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#chaospower <bonus>` |
| `#chaosrec` | Defined | Monster | M6.34 p15; M6.34 p58 | `#chaosrec <value>` |
| `#chaosrecscale` | Defined | Monster | M6.34 p15 | `#chaosrecscale <value>` |
| `#chaosscale` | Defined | Bless | M6.34 p37 | `#chaosscale <value>` |
| `#charge` | Defined | Weapon | M6.34 p10 | `#charge` |
| `#cheapgod20` | Defined | Nation | M6.34 p47 | `#cheapgod20 "<monster name>" \| <monster nbr>` |
| `#cheapgod40` | Defined | Nation | M6.34 p47 | `#cheapgod40 "<monster name>" \| <monster nbr>` |
| `#chestwound` | Defined | Item | M6.34 p57 | `#chestwound` |
| `#chorusmaster` | Defined | Monster | M6.34 p35; M6.34 p60 | `#chorusmaster` |
| `#chorusslave` | Defined | Monster | M6.34 p35; M6.34 p60 | `#chorusslave` |
| `#claim` | Defined | Site | M6.34 p40 | `#claim` |
| `#claimthrone` | Defined | Event | E6.29 p13 | `#claimthrone` |
| `#cleanshape` | Defined | Monster | M6.34 p28 | `#cleanshape` |
| `#clear` | Defined | Armour, Event, Item, Monster, Names, Site, Spell, Weapon | E6.29 p2; M6.34 p7; M6.34 p12; M6.34 p13; M6.34 p36; +3 | `#clear` |
| `#clearallevents` | Defined | Event | E6.29 p2 | `#clearallevents` |
| `#clearallitems` | Defined | Item | M6.34 p55 | `#clearallitems` |
| `#clearallspells` | Defined | Spell | M6.34 p50 | `#clearallspells` |
| `#cleararmor` | Defined | Monster, Weapon | M6.34 p13 | `#cleararmor` |
| `#cleardef` | Defined | Poptype | M6.34 p63 | `#cleardef` |
| `#clearfx` | Defined | Bless | M6.34 p37 | `#clearfx` |
| `#cleargods` | Defined | Nation | M6.34 p47 | `#cleargods` |
| `#clearmagic` | Defined | Map, Monster | P6.26 p9; M6.34 p13 | `#clearmagic` |
| `#clearmercs` | Defined | Mercenary | M6.34 p63 | `#clearmercs` |
| `#clearnation` | Defined | Nation | M6.34 p42 | `#clearnation` |
| `#clearrec` | Defined | Nation, Poptype | M6.34 p45; M6.34 p63 | `#clearrec` |
| `#clearscales` | Defined | Bless | M6.34 p37 | `#clearscales` |
| `#clearsites` | Defined | Site | M6.34 p43 | `#clearsites` |
| `#clearspec` | Defined | Monster | M6.34 p13 | `#clearspec` |
| `#cleartarg` | Defined | Event | E6.29 p15 | `#cleartarg` |
| `#clearvar` | Defined | Event | E6.29 p18 | `#clearvar <event var>` |
| `#clearweapons` | Defined | Monster, Weapon | M6.34 p13 | `#clearweapons` |
| `#clumsy` | Defined | Monster | M6.34 p25; M6.34 p59 | `#clumsy <0 or 1>` |
| `#cluster` | Defined | Site | M6.34 p40 | `#cluster <value>` |
| `#coastcom1...2` | Defined; template | Nation | M6.34 p45 | `#coastcom1...2 "<monster name>" \| <monster nbr>` |
| `#coastnation` | Defined | Site | M6.34 p43 | `#coastnation` |
| `#coastunit1...3` | Defined; template | Nation | M6.34 p45 | `#coastunit1...3 "<monster name>" \| <monster nbr>` |
| `#code` | Defined | Event | E6.29 p17; E6.29 p19 | `#code <event code>` |
| `#code2` | Defined | Event | E6.29 p17 | `#code2 <event code>` |
| `#codedelay` | Defined | Event | E6.29 p18 | `#codedelay <event code>` |
| `#codedelay2` | Defined | Event | E6.29 p18 | `#codedelay2 <event code>` |
| `#cold` | Defined | Monster, Weapon | M6.34 p9; M6.34 p23; M6.34 p59 | `#cold` |
| `#coldblood` | Defined | Monster | M6.34 p19 | `#coldblood` |
| `#coldifhit` | Defined | Weapon | M6.34 p12 | `#coldifhit <dmg>` |
| `#coldincome` | Defined | General | M6.34 p61 | `#coldincome <percent>` |
| `#coldpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#coldpower <bonus>` |
| `#coldrec` | Mention | Monster | M6.34 p15 | `#coldrec` |
| `#coldrecscale` | Defined | Monster | M6.34 p15 | `#coldrecscale <value>` |
| `#coldres` | Defined | Item, Monster | M6.34 p22; M6.34 p56 | `#coldres <prot>` |
| `#coldscale` | Defined | Bless | M6.34 p37 | `#coldscale <value>` |
| `#coldsupply` | Defined | General | M6.34 p61 | `#coldsupply <percent>` |
| `#color` | Defined | General, Nation | M6.34 p43; M6.34 p64 | `#color <red> <green> <blue>` |
| `#com` | Defined | Event, Mercenary, Monster | E6.29 p14; M6.34 p38; M6.34 p63; E6.29 p19; E6.29 p20 | `#com "name" \| <number>` |
| `#combatcaster` | Reference | Monster | M6.34 p36; M6.34 p60 | `#combatcaster` |
| `#command` | Defined | Monster | M6.34 p31; M6.34 p60 | `#command <value>` |
| `#commander` | Defined | Map | P6.26 p8 | `#commander "<type>"` |
| `#commaster` | Defined | Monster | M6.34 p35; M6.34 p60 | `#commaster` |
| `#comname` | Defined | Map | P6.26 p8 | `#comname "<name>"` |
| `#computerplayer` | Defined | Map | P6.26 p6 | `#computerplayer <nation nbr> <difficulty>` |
| `#comslave` | Defined | Monster | M6.34 p35; M6.34 p60 | `#comslave` |
| `#conjcost` | Defined | Site | M6.34 p39 | `#conjcost <bonus>` |
| `#constcost` | Defined | Site | M6.34 p39 | `#constcost <bonus>` |
| `#constlevel` | Defined | Item | M6.34 p55 | `#constlevel <level>` |
| `#copyarmor` | Defined | Armour | M6.34 p12 | `#copyarmor "<armor name>" \| <armor nbr>` |
| `#copyitem` | Defined | Item | M6.34 p55 | `#copyitem "<item name>" \| <item nbr>` |
| `#copysite` | Defined | Site | M6.34 p37 | `#copysite "<site name>" \| <site nbr>` |
| `#copyspell` | Defined | Spell | M6.34 p50 | `#copyspell "<spell name>" \| <spell nbr>` |
| `#copyspr` | Defined | Item, Monster | M6.34 p13; M6.34 p55 | `#copyspr <monster nbr>` |
| `#copystats` | Defined | Monster | M6.34 p13 | `#copystats <monster nbr>` |
| `#copyweapon` | Defined | Weapon | M6.34 p7 | `#copyweapon "<weapon name>" \| <weapon nbr>` |
| `#coridermnr` | Defined | Monster | M6.34 p30 | `#coridermnr "<monster name>" \| <monster nbr>` |
| `#corpseeater` | Defined | Monster | M6.34 p22 | `#corpseeater <value>` |
| `#corpselord` | Defined | Monster | M6.34 p30; M6.34 p61 | `#corpselord <nbr>` |
| `#corruptor` | Defined | Monster | M6.34 p20; M6.34 p59 | `#corruptor <value>` |
| `#cost0` | Defined | Bless | M6.34 p37 | `#cost0 <value>` |
| `#cost1` | Defined | Bless | M6.34 p37 | `#cost1 <value>` |
| `#crippled` | Defined | Item | M6.34 p58 | `#crippled` |
| `#crossbreeder` | Defined | Monster | M6.34 p35; M6.34 p60 | `#crossbreeder <value>` |
| `#cure` | Defined | Spell | M6.34 p54 | `#cure "text"` |
| `#curse` | Defined | Event, Item, Site | E6.29 p15; M6.34 p40; M6.34 p57 | `#curse <percent>` |
| `#cursed` | Defined | Item | M6.34 p57 | `#cursed` |
| `#curseluckshield` | Defined | Monster | M6.34 p24; M6.34 p59 | `#curseluckshield <penetration bonus>` |
| `#custommagic` | Defined | Monster | M6.34 p33 | `#custommagic <path mask> <chance>` |

### D

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##dishe##` | Reference; message | Spell | M6.34 p54 | `##dishe##` |
| `##dishim##` | Reference; message | Spell | M6.34 p54 | `##dishim##` |
| `##dishimself##` | Reference; message | Spell | M6.34 p54 | `##dishimself##` |
| `##disHis##` | Reference; message | Spell | M6.34 p54 | `##disHis##` |
| `##dishis##` | Reference; message | Spell | M6.34 p54 | `##dishis##` |
| `##disname##` | Reference; message | Event, Spell | E6.29 p11; M6.34 p54 | `##disname##` |
| `##disnat##` | Reference; message | Spell | M6.34 p54 | `##disnat##` |
| `#damage` | Defined | Event, Spell | M6.34 p51; E6.29 p20 | `#damage <dmg>` |
| `#damagemon` | Defined | Spell | M6.34 p51 | `#damagemon "<monster name>"` |
| `#damagerev` | Defined | Monster | M6.34 p24; M6.34 p59 | `#damagerev <strength>` |
| `#dancenof` | Defined | Weapon | M6.34 p58 | `#dancenof <nbr of sprites>` |
| `#dancenratt` | Defined | Weapon | M6.34 p58 | `#dancenratt <attacks>` |
| `#dancesize` | Defined | Weapon | M6.34 p58 | `#dancesize <size>` |
| `#dancespr` | Defined | Weapon | M6.34 p58 | `#dancespr <flysprite nbr>` |
| `#danceweapon` | Defined | Weapon | M6.34 p58 | `#danceweapon "<weapon name>" \| <weapon nbr>` |
| `#darkpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#darkpower <bonus>` |
| `#darkvision` | Defined | Monster | M6.34 p25; M6.34 p59 | `#darkvision <percent>` |
| `#deadhp` | Defined | Monster | M6.34 p22; M6.34 p59 | `#deadhp <value>` |
| `#deathbanish` | Defined | Monster | M6.34 p35; M6.34 p60 | `#deathbanish <-11 to -13>` |
| `#deathblessbonus` | Defined | Nation | M6.34 p47 | `#deathblessbonus <0 - 9>` |
| `#deathboost` | Defined | Event | E6.29 p16; E6.29 p19 | `#deathboost "name" \| <number>` |
| `#deathcurse` | Defined | Monster | M6.34 p26; M6.34 p59 | `#deathcurse` |
| `#deathdeath` | Defined | General | M6.34 p61 | `#deathdeath <0.01 percent>` |
| `#deathdisease` | Defined | Monster | M6.34 p26; M6.34 p59 | `#deathdisease <aoe>` |
| `#deathfire` | Defined | Monster | M6.34 p26; M6.34 p59 | `#deathfire <aoe>` |
| `#deathgrab` | Defined | Monster | M6.34 p26 | `#deathgrab <aoe>` |
| `#deathincome` | Defined | General | M6.34 p61 | `#deathincome <percent>` |
| `#deathparalyze` | Defined | Monster | M6.34 p26; M6.34 p59 | `#deathparalyze <aoe>` |
| `#deathpoison` | Defined | Monster | M6.34 p26 | `#deathpoison <aoe>` |
| `#deathpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#deathpower <bonus>` |
| `#deathrange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#deathrange <range>` |
| `#deathrec` | Defined | Monster | M6.34 p15 | `#deathrec <value>` |
| `#deathrecscale` | Defined | Monster | M6.34 p15 | `#deathrecscale <value>` |
| `#deathscale` | Defined | Bless | M6.34 p37 | `#deathscale <value>` |
| `#deathshock` | Defined | Monster | M6.34 p26 | `#deathshock <aoe>` |
| `#deathslime` | Defined | Monster | M6.34 p26 | `#deathslime <aoe>` |
| `#deathsupply` | Defined | General | M6.34 p61 | `#deathsupply <percent>` |
| `#dec10var` | Defined | Event | E6.29 p18 | `#dec10var <event var>` |
| `#decayres` | Defined | Item, Monster | M6.34 p22; M6.34 p56 | `#decayres <0 or 1>` |
| `#decscale` | Defined | Event, Monster, Site | E6.29 p12; M6.34 p27; M6.34 p39; M6.34 p60 | `#decscale <scale>` |
| `#decscale2` | Defined | Event | E6.29 p12 | `#decscale2 <scale>` |
| `#decscale3` | Defined | Event | E6.29 p12; E6.29 p19 | `#decscale3 <scale>` |
| `#decunrest` | Defined | Site | M6.34 p38 | `#decunrest <value>` |
| `#decvar` | Defined | Event | E6.29 p18 | `#decvar <event var>` |
| `#def` | Defined | Armour, Item, Monster, Weapon | M6.34 p7; M6.34 p12; M6.34 p16; M6.34 p56; M6.34 p9 | `#def <defense>` |
| `#defchaos` | Defined | Site | M6.34 p43 | `#defchaos <-5 - 5>` |
| `#defcom` | Defined | Monster | M6.34 p38 | `#defcom "<monster name>" \| <monster nbr>` |
| `#defcom1` | Defined | Nation, Poptype | M6.34 p45; M6.34 p63 | `#defcom1 "<monster name>" \| <monster nbr>` |
| `#defcom2` | Defined | Nation | M6.34 p46 | `#defcom2 "<monster name>" \| <monster nbr>` |
| `#defdeath` | Defined | Site | M6.34 p43 | `#defdeath <-5 - 5>` |
| `#defdrain` | Defined | Site | M6.34 p43 | `#defdrain <-5 - 5>` |
| `#defector` | Defined | Monster | M6.34 p15 | `#defector <percent>` |
| `#defence` | Defined | Event, Map | E6.29 p13; P6.26 p8 | `#defence <value>` |
| `#defmisfortune` | Defined | Site | M6.34 p43 | `#defmisfortune <-5 - 5>` |
| `#defmult` | Defined | Monster | M6.34 p38 | `#defmult <multiplier>` |
| `#defmult1` | Defined | Nation, Poptype | M6.34 p46; M6.34 p63 | `#defmult1 <multiplier>` |
| `#defmult1b` | Defined | Nation, Poptype | M6.34 p46; M6.34 p63 | `#defmult1b <multiplier>` |
| `#defmult1c` | Defined | Nation, Poptype | M6.34 p46; M6.34 p63 | `#defmult1c <multiplier>` |
| `#defmult1d` | Defined | Nation | M6.34 p46 | `#defmult1d <multiplier>` |
| `#defmult2` | Defined | Nation | M6.34 p46 | `#defmult2 <multiplier>` |
| `#defmult2b` | Defined | Nation | M6.34 p46 | `#defmult2b <multiplier>` |
| `#defroll` | Defined | Weapon | M6.34 p10 | `#defroll` |
| `#defsloth` | Defined | Site | M6.34 p43 | `#defsloth <-5 - 5>` |
| `#defunit` | Defined | Monster | M6.34 p38 | `#defunit "<monster name>" \| <monster nbr>` |
| `#defunit1` | Defined | Nation, Poptype | M6.34 p46; M6.34 p63 | `#defunit1 "<monster name>" \| <monster nbr>` |
| `#defunit1b` | Defined | Nation, Poptype | M6.34 p46; M6.34 p63 | `#defunit1b "<monster name>" \| <monster nbr>` |
| `#defunit1c` | Defined | Nation, Poptype | M6.34 p46; M6.34 p63 | `#defunit1c "<monster name>" \| <monster nbr>` |
| `#defunit1d` | Defined | Nation | M6.34 p46 | `#defunit1d "<monster name>" \| <monster nbr>` |
| `#defunit2` | Defined | Nation | M6.34 p46 | `#defunit2 "<monster name>" \| <monster nbr>` |
| `#defunit2b` | Defined | Nation | M6.34 p46 | `#defunit2b "<monster name>" \| <monster nbr>` |
| `#delay` | Defined | Event | E6.29 p17; E6.29 p19 | `#delay <value>` |
| `#delay25` | Defined | Event | E6.29 p17 | `#delay25 <value>` |
| `#delay50` | Defined | Event | E6.29 p17 | `#delay50 <value>` |
| `#delayskip` | Defined | Event | E6.29 p17 | `#delayskip <percent>` |
| `#delgod` | Defined | Nation | M6.34 p47 | `#delgod "<monster>" \| <monster nbr>` |
| `#demon` | Defined | Monster | M6.34 p19 | `#demon` |
| `#demononly` | Defined | Weapon | M6.34 p9 | `#demononly` |
| `#demonundead` | Defined | Weapon | M6.34 p9 | `#demonundead` |
| `#descr` | Defined | Event, General, Item, Monster, Nation, Spell | M6.34 p13; M6.34 p42; M6.34 p50; M6.34 p56; E6.29 p20; +1 | `#descr "<text description>"` |
| `#description` | Defined | General, Map, Metadata | P6.26 p3; M6.34 p5; M6.34 p64 | `#description "text"` |
| `#deserter` | Defined | Monster | M6.34 p15 | `#deserter <percent>` |
| `#details` | Defined | Spell | M6.34 p50 | `#details "<text>"` |
| `#digest` | Defined | Monster | M6.34 p25; M6.34 p59 | `#digest <dmg>` |
| `#disableoldnations` | Defined | Nation | M6.34 p43 | `#disableoldnations` |
| `#disbless` | Defined | Nation | M6.34 p49 | `#disbless "bless name" \| <nbr>` |
| `#disease` | Defined | Event, Item, Site | E6.29 p15; M6.34 p40; M6.34 p57 | `#disease <percent>` |
| `#diseasecloud` | Defined | Monster | M6.34 p23; M6.34 p59 | `#diseasecloud <size>` |
| `#diseaseres` | Defined | Monster | M6.34 p21; M6.34 p59 | `#diseaseres <percent>` |
| `#dispglobals` | Defined | Event | E6.29 p17 | `#dispglobals <str>` |
| `#dispimmune` | Defined | Spell | M6.34 p54 | `#dispimmune <0 - 2>` |
| `#divinebeing` | Defined | Monster | M6.34 p19 | `#divinebeing` |
| `#divineins` | Defined | Monster | M6.34 p34; M6.34 p60 | `#divineins` |
| `#djinn` | Defined | Monster | M6.34 p18 | `#djinn` |
| `#dmg` | Defined | Weapon | M6.34 p7; M6.34 p9 | `#dmg <damage>` |
| `#doheal` | Defined | Monster | M6.34 p22; M6.34 p59 | `#doheal` |
| `#dom2title` | Defined | Map | P6.26 p3 | `#dom2title <text>` |
| `#dom6title` | Mention | Map | P6.26 p3 | `#dom6title` |
| `#domdeathsense` | Defined | Nation | M6.34 p49 | `#domdeathsense` |
| `#domimmortal` | Defined | Monster | M6.34 p23 | `#domimmortal` |
| `#dominion` | Defined | Site | M6.34 p40 | `#dominion <temple checks per month>` |
| `#dominionstr` | Defined | Map | P6.26 p9 | `#dominionstr <nation nbr> <1-10>` |
| `#domkill` | Defined | Nation | M6.34 p49 | `#domkill <value>` |
| `#dompower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#dompower <bonus>` |
| `#domrec` | Defined | Monster | M6.34 p15 | `#domrec <dominion>` |
| `#domsail` | Defined | Nation | M6.34 p49 | `#domsail` |
| `#domshape` | Defined | Monster | M6.34 p28 | `#domshape "<monster name>" \| <monster nbr>` |
| `#domstr` | Defined | AI | M6.34 p64 | `#domstr <level>` |
| `#domsummon` | Defined | Monster | M6.34 p29; M6.34 p61 | `#domsummon "<monster name>" \| <monster nbr>` |
| `#domsummon2` | Defined | Monster | M6.34 p29; M6.34 p61 | `#domsummon2 "<monster name>" \| <monster nbr>` |
| `#domsummon20` | Defined | Monster | M6.34 p29; M6.34 p61 | `#domsummon20 "<monster name>" \| <monster nbr>` |
| `#domunrest` | Defined | Nation | M6.34 p49 | `#domunrest <value>` |
| `#domversion` | Defined | Map, Metadata | P6.26 p3; M6.34 p5 | `#domversion <version>` |
| `#domwar` | Defined | Nation, Site | M6.34 p41; M6.34 p49 | `#domwar <value>` |
| `#doomhorror` | Defined | Monster | M6.34 p19 | `#doomhorror` |
| `#douse` | Defined | Monster | M6.34 p35; M6.34 p60 | `#douse <bonus>` |
| `#dragonlord` | Defined | Monster | M6.34 p30; M6.34 p61 | `#dragonlord <nbr>` |
| `#drainimmune` | Defined | Monster | M6.34 p34; M6.34 p60 | `#drainimmune` |
| `#drainscale` | Defined | Bless | M6.34 p37 | `#drainscale <value>` |
| `#drake` | Defined | Monster | M6.34 p19 | `#drake` |
| `#drawsize` | Defined | Monster | M6.34 p13 | `#drawsize <value>` |
| `#dread` | Defined | Monster | M6.34 p24 | `#dread <value>` |
| `#dt_aff` | Defined | Weapon | M6.34 p8; M6.34 p9 | `#dt_aff` |
| `#dt_bouncekill` | Defined | Weapon | M6.34 p8 | `#dt_bouncekill` |
| `#dt_cap` | Defined | Weapon | M6.34 p8 | `#dt_cap` |
| `#dt_constructonly` | Defined | Weapon | M6.34 p8 | `#dt_constructonly` |
| `#dt_demon` | Defined | Weapon | M6.34 p8 | `#dt_demon` |
| `#dt_drain` | Defined | Weapon | M6.34 p8 | `#dt_drain` |
| `#dt_holy` | Defined | Weapon | M6.34 p8 | `#dt_holy` |
| `#dt_interrupt` | Defined | Weapon | M6.34 p8 | `#dt_interrupt` |
| `#dt_large` | Defined | Weapon | M6.34 p8 | `#dt_large` |
| `#dt_magic` | Defined | Weapon | M6.34 p8 | `#dt_magic` |
| `#dt_normal` | Defined | Weapon | M6.34 p7 | `#dt_normal` |
| `#dt_paralyze` | Defined | Weapon | M6.34 p8 | `#dt_paralyze` |
| `#dt_poison` | Defined | Weapon | M6.34 p7 | `#dt_poison` |
| `#dt_raise` | Defined | Monster, Weapon | M6.34 p8 | `#dt_raise` |
| `#dt_realstun` | Defined | Weapon | M6.34 p8 | `#dt_realstun` |
| `#dt_sizestun` | Defined | Weapon | M6.34 p8 | `#dt_sizestun` |
| `#dt_small` | Defined | Weapon | M6.34 p8 | `#dt_small` |
| `#dt_stun` | Defined | Weapon | M6.34 p8 | `#dt_stun` |
| `#dt_weakness` | Defined | Weapon | M6.34 p8 | `#dt_weakness` |
| `#dt_weapondrain` | Defined | Weapon | M6.34 p8 | `#dt_weapondrain` |
| `#dungeon` | Defined | Monster | M6.34 p19 | `#dungeon` |
| `#dyingdom` | Defined | Nation | M6.34 p49 | `#dyingdom` |

### E

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#earthblessbonus` | Defined | Nation | M6.34 p47 | `#earthblessbonus <0 - 9>` |
| `#earthboost` | Defined | Event | E6.29 p16 | `#earthboost "name" \| <number>` |
| `#earthelementals` | Defined | Monster | M6.34 p30; M6.34 p61 | `#earthelementals <bonus>` |
| `#earthrange` | Defined | Monster, Site | M6.34 p33; M6.34 p39; M6.34 p60 | `#earthrange <range>` |
| `#effect` | Defined | Event, Spell | M6.34 p51; E6.29 p20 | `#effect <eff>` |
| `#elegist` | Defined | Monster | M6.34 p26; M6.34 p60 | `#elegist <value>` |
| `#elementgems` | Defined | Monster | M6.34 p34; M6.34 p60 | `#elementgems <gems>` |
| `#elementrange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#elementrange <range>` |
| `#emigration` | Defined | Event | E6.29 p13 | `#emigration <percent>` |
| `#enc` | Defined | Armour, Monster | M6.34 p12; M6.34 p17 | `#enc <encumbrance>` |
| `#enchantedblood` | Defined | Item, Monster | M6.34 p23; M6.34 p57 | `#enchantedblood <points>` |
| `#enchcost` | Defined | Site | M6.34 p39 | `#enchcost <bonus>` |
| `#enchrebate10` | Defined | Monster | M6.34 p14 | `#enchrebate10 <enchantment number>` |
| `#enchrebate100` | Defined | Monster | M6.34 p15 | `#enchrebate100 <enchantment number>` |
| `#enchrebate20` | Defined | Monster | M6.34 p15 | `#enchrebate20 <enchantment number>` |
| `#enchrebate25p` | Defined | Monster | M6.34 p15 | `#enchrebate25p <enchantment number>` |
| `#enchrebate50` | Defined | Monster | M6.34 p15 | `#enchrebate50 <enchantment number>` |
| `#enchrebate50p` | Defined | Monster | M6.34 p15 | `#enchrebate50p <enchantment number>` |
| `#enchrebate75` | Defined | Monster | M6.34 p15 | `#enchrebate75 <enchantment number>` |
| `#end` | Defined | AI, Armour, Bless, Event, General, Item, Mercenary, Monster, Names, Nation, Poptype, Site, Sound, Spell, Weapon | E6.29 p2; M6.34 p5; M6.34 p6; M6.34 p12; M6.34 p13; +10 | `#end` |
| `#enemyimmune` | Defined | Weapon | M6.34 p9 | `#enemyimmune` |
| `#entangle` | Defined | Monster | M6.34 p24 | `#entangle` |
| `#epithet` | Defined | General, Nation | M6.34 p42; M6.34 p64 | `#epithet "<nation name>"` |
| `#era` | Defined | General, Nation | M6.34 p42; M6.34 p64 | `#era <era nbr>` |
| `#eramask` | Defined | Mercenary | M6.34 p63 | `#eramask <value>` |
| `#ethereal` | Defined | Monster | M6.34 p22; M6.34 p59 | `#ethereal` |
| `#eventisrare` | Defined | General | M6.34 p61 | `#eventisrare <percent>` |
| `#evil` | Defined | Site | M6.34 p41 | `#evil` |
| `#evocost` | Defined | Site | M6.34 p39 | `#evocost <bonus>` |
| `#exactgold` | Defined | Event | E6.29 p12 | `#exactgold <value>` |
| `#expertleader` | Defined | Monster | M6.34 p31 | `#expertleader` |
| `#expertmagicleader` | Defined | Monster | M6.34 p32 | `#expertmagicleader` |
| `#expertundeadleader` | Defined | Monster | M6.34 p32 | `#expertundeadleader` |
| `#explspr` | Defined | Sound, Weapon | M6.34 p11; M6.34 p52 | `#explspr <fx nbr>` |
| `#extralife` | Defined | Item | M6.34 p56 | `#extralife` |
| `#extralives` | Defined | Monster | M6.34 p22 | `#extralives <percent>` |
| `#extramsg` | Defined | Event | E6.29 p11 | `#extramsg <nation number>` |
| `#eyeloss` | Defined | Monster | M6.34 p24; M6.34 p59 | `#eyeloss` |
| `#eyes` | Defined | Monster | M6.34 p17 | `#eyes <nbr of eyes>` |

### F

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##fullgodname##` | Reference; message | Event, Spell | E6.29 p11; M6.34 p54 | `##fullgodname##` |
| `##fullplayergodname##` | Reference; message | Spell | M6.34 p54 | `##fullplayergodname##` |
| `##fullplayername##` | Reference; message | Spell | M6.34 p54 | `##fullplayername##` |
| `##fulltargname##` | Reference; message | Event | E6.29 p11 | `##fulltargname##` |
| `#fallpower` | Defined | Monster | M6.34 p24; M6.34 p59 | `#fallpower <percent>` |
| `#false` | Defined | Weapon | M6.34 p10 | `#false` |
| `#falsearmy` | Defined | Monster | M6.34 p21; M6.34 p58 | `#falsearmy <value>` |
| `#falseregen` | Defined | Monster | M6.34 p23 | `#falseregen <points>` |
| `#falsesupply` | Defined | Monster | M6.34 p26; M6.34 p60 | `#falsesupply <value>` |
| `#farsail` | Defined | Monster | M6.34 p20; M6.34 p58 | `#farsail <extra provinces>` |
| `#farsumcom` | Defined | Spell | M6.34 p53 | `#farsumcom "<monster name>" \| <monster nbr>` |
| `#farthronekill` | Defined | Monster | M6.34 p27; M6.34 p60 | `#farthronekill <part>` |
| `#fastcast` | Defined | Monster | M6.34 p35; M6.34 p60 | `#fastcast <speedup>` |
| `#fatiguecost` | Defined | Event, Spell | M6.34 p51; E6.29 p20 | `#fatiguecost <fat>` |
| `#favrit` | Defined | AI | M6.34 p64 | `#favrit <disschool> <level> "ritual name" \| "item name"` |
| `#faysummon` | Defined | Monster | M6.34 p30 | `#faysummon <nbr>` |
| `#fear` | Defined | Monster | M6.34 p24; M6.34 p59 | `#fear <value>` |
| `#fearofflood` | Defined | Monster | M6.34 p26; M6.34 p59 | `#fearofflood <value>` |
| `#feature` | Defined | Map | P6.26 p7 | `#feature "<site name>" \| <site nbr>` |
| `#features` | Defined | Map | P6.26 p4 | `#features <0-100>` |
| `#feeblemind` | Defined | Item | M6.34 p57 | `#feeblemind` |
| `#female` | Defined | Monster | M6.34 p18 | `#female` |
| `#fire` | Defined | Weapon | M6.34 p9 | `#fire` |
| `#fireattuned` | Mention | Monster | M6.34 p28 | `#fireattuned` |
| `#fireblessbonus` | Defined | Nation | M6.34 p47 | `#fireblessbonus <0 - 9>` |
| `#fireboost` | Defined | Event | E6.29 p16 | `#fireboost "name" \| <number>` |
| `#fireelementals` | Defined | Monster | M6.34 p30; M6.34 p61 | `#fireelementals <bonus>` |
| `#fireifhit` | Defined | Weapon | M6.34 p12 | `#fireifhit <dmg>` |
| `#firepower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#firepower <bonus>` |
| `#firerange` | Defined | Monster, Site | M6.34 p33; M6.34 p39; M6.34 p60 | `#firerange <range>` |
| `#fireres` | Defined | Item, Monster | M6.34 p22; M6.34 p56 | `#fireres <prot>` |
| `#fireshield` | Defined | Monster | M6.34 p24; M6.34 p59 | `#fireshield <damage>` |
| `#firstshape` | Defined | Monster | M6.34 p27 | `#firstshape "<monster name>" \| <monster nbr>` |
| `#fixedname` | Defined | Monster | M6.34 p13 | `#fixedname "<Name>"` |
| `#fixedresearch` | Defined | Monster | M6.34 p34 | `#fixedresearch <value>` |
| `#fixforgebonus` | Defined | Monster | M6.34 p35; M6.34 p60 | `#fixforgebonus <value>` |
| `#flag` | Defined | Nation | M6.34 p43 | `#flag "<imgfile>"` |
| `#flagland` | Defined | Event | E6.29 p17; E6.29 p19 | `#flagland < 0 \| 1 >` |
| `#flail` | Defined | Weapon | M6.34 p10 | `#flail` |
| `#flightspr` | Defined | Sound | M6.34 p52 | `#flightspr <flysprite nbr>` |
| `#float` | Defined | Item, Monster | M6.34 p19; M6.34 p57 | `#float` |
| `#fly` | Defined | Item | M6.34 p57 | `#fly` |
| `#flying` | Defined | Monster | M6.34 p19 | `#flying` |
| `#flyingimmune` | Defined | Weapon | M6.34 p9 | `#flyingimmune` |
| `#flyspr` | Defined | Weapon | M6.34 p11 | `#flyspr <flysprite nbr> <animation lgth>` |
| `#fogcol` | Defined | Map | P6.26 p8 | `#fogcol <red> <green> <blue>` |
| `#foolscouts` | Defined | Monster | M6.34 p21; M6.34 p59 | `#foolscouts <value>` |
| `#force1d3vis` | Defined | Event | E6.29 p12 | `#force1d3vis <gem type>` |
| `#force1d6vis` | Defined | Event | E6.29 p12 | `#force1d6vis <gem type>` |
| `#force2d4vis` | Defined | Event | E6.29 p12 | `#force2d4vis <gem type>` |
| `#force2d6vis` | Defined | Event | E6.29 p12 | `#force2d6vis <gem type>` |
| `#force3d6vis` | Defined | Event | E6.29 p12 | `#force3d6vis <gem type>` |
| `#force4d6vis` | Defined | Event | E6.29 p12 | `#force4d6vis <gem type>` |
| `#forceexactgold` | Defined | Event | E6.29 p12 | `#forceexactgold <value>` |
| `#forcegold` | Defined | Event | E6.29 p12 | `#forcegold <value>` |
| `#forcess` | Defined | Monster | M6.34 p28 | `#forcess` |
| `#forcetransform` | Defined | Event | E6.29 p15 | `#forcetransform "name" \| <number>` |
| `#foreignguardcom` | Defined | Nation | M6.34 p46 | `#foreignguardcom "<monster name>" \| <monster nbr>` |
| `#foreignguardmult` | Defined | Nation | M6.34 p46 | `#foreignguardmult <multiplier>` |
| `#foreignguardunit` | Defined | Nation | M6.34 p46 | `#foreignguardunit "<monster name>" \| <monster nbr>` |
| `#foreignshape` | Defined | Monster | M6.34 p28 | `#foreignshape "<monster name>" \| <monster nbr>` |
| `#foreignwallcom` | Defined | Nation | M6.34 p46 | `#foreignwallcom "<monster name>" \| <monster nbr>` |
| `#foreignwallmult` | Defined | Nation | M6.34 p46 | `#foreignwallmult <multiplier>` |
| `#foreignwallunit` | Defined | Nation | M6.34 p46 | `#foreignwallunit "<monster name>" \| <monster nbr>` |
| `#forestlabcost` | Defined | Nation | M6.34 p48 | `#forestlabcost <price>` |
| `#forestrec` | Mention | Nation | M6.34 p45 | `#forestrec` |
| `#forestshape` | Defined | Monster | M6.34 p28 | `#forestshape "<monster name>" \| <monster nbr>` |
| `#forestsurvival` | Defined | Monster | M6.34 p20 | `#forestsurvival` |
| `#foresttemplecost` | Defined | Nation | M6.34 p48 | `#foresttemplecost <price>` |
| `#forgebonus` | Defined | Monster | M6.34 p35; M6.34 p60 | `#forgebonus <percent>` |
| `#form` | Defined | AI | M6.34 p64 | `#form "monster name"` |
| `#formationfighter` | Defined | Monster | M6.34 p32; M6.34 p60 | `#formationfighter <xsize>` |
| `#fort` | Defined | Event, Map, Site | E6.29 p13; P6.26 p8; M6.34 p40 | `#fort <fort number>` |
| `#fortcoldscaleres` | Defined | Site | M6.34 p44 | `#fortcoldscaleres <steps>` |
| `#fortcost` | Defined | Nation | M6.34 p48 | `#fortcost <extra cost>` |
| `#fortera` | Defined | Nation | M6.34 p48 | `#fortera <0-4>` |
| `#fortheatscaleres` | Defined | Site | M6.34 p44 | `#fortheatscaleres <steps>` |
| `#fortkill` | Defined | Monster | M6.34 p27; M6.34 p60 | `#fortkill <chance>` |
| `#fortunrest` | Defined | Nation | M6.34 p49 | `#fortunrest <value>` |
| `#friendlyench` | Defined | Spell | M6.34 p53 | `#friendlyench <0 - 1>` |
| `#friendlyimmune` | Defined | Weapon | M6.34 p9 | `#friendlyimmune` |
| `#fullstr` | Defined | Weapon | M6.34 p9 | `#fullstr` |
| `#futuresite` | Defined | Site | M6.34 p43 | `#futuresite "<site name>"` |

### G

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##goddisname##` | Reference; message | Event | E6.29 p11 | `##goddisname##` |
| `##godhe##` | Reference; message | Spell | M6.34 p54 | `##godhe##` |
| `##godhim##` | Reference; message | Spell | M6.34 p54 | `##godhim##` |
| `##godhimself##` | Reference; message | Spell | M6.34 p54 | `##godhimself##` |
| `##godHis##` | Reference; message | Spell | M6.34 p54 | `##godHis##` |
| `##godhis##` | Reference; message | Spell | M6.34 p54 | `##godhis##` |
| `##godname##` | Reference; message | Event, Spell | E6.29 p11; M6.34 p54 | `##godname##` |
| `##godnat##` | Reference; message | Spell | M6.34 p54 | `##godnat##` |
| `##godthrone##` | Reference; message | Spell | M6.34 p54 | `##godthrone##` |
| `#gainaff` | Defined | Event | E6.29 p15 | `#gainaff <affliction bitmask>` |
| `#gainmark` | Defined | Event | E6.29 p15 | `#gainmark` |
| `#gate` | Defined | Map | P6.26 p4 | `#gate <province nbr> <gate nbr>` |
| `#gcost` | Defined | General, Monster | M6.34 p14; M6.34 p15 | `#gcost <gold>` |
| `#gemlongevity` | Defined | General | M6.34 p62 | `#gemlongevity <level>` |
| `#gemloss` | Defined | Event | E6.29 p12 | `#gemloss <gem type>` |
| `#gemlosslarge` | Defined | Event | E6.29 p12 | `#gemlosslarge <gem type>` |
| `#gemlosssmall` | Defined | Event | E6.29 p12 | `#gemlosssmall <gem type>` |
| `#gemprod` | Defined | Monster | M6.34 p34; M6.34 p60 | `#gemprod <type> <number>` |
| `#gems` | Defined | Site | M6.34 p38 | `#gems <path> <amount>` |
| `#ghostreanim` | Defined | Nation | M6.34 p50 | `#ghostreanim` |
| `#giftofwater` | Defined | Monster | M6.34 p20; M6.34 p58 | `#giftofwater <size points>` |
| `#glamour` | Defined | Monster | M6.34 p23 | `#glamour` |
| `#glamourboost` | Defined | Event | E6.29 p16 | `#glamourboost "name" \| <number>` |
| `#glamourmanip` | Defined | Monster | M6.34 p35; M6.34 p60 | `#glamourmanip <0 or 1>` |
| `#glamourrange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#glamourrange <range>` |
| `#globallook` | Defined | Spell | M6.34 p54 | `#globallook <1 - 9>` |
| `#god` | Defined | Map | P6.26 p9 | `#god <nation nbr> "<type>"` |
| `#goddomchaos` | Defined | Site | M6.34 p40 | `#goddomchaos <value>` |
| `#goddomcold` | Defined | Site | M6.34 p40 | `#goddomcold <value>` |
| `#goddomdeath` | Defined | Site | M6.34 p40 | `#goddomdeath <value>` |
| `#goddomdrain` | Defined | Site | M6.34 p40 | `#goddomdrain <value>` |
| `#goddomlazy` | Defined | Site | M6.34 p40 | `#goddomlazy <value>` |
| `#goddommisfortune` | Defined | Site | M6.34 p40 | `#goddommisfortune <value>` |
| `#godpathspell` | Defined | Spell | M6.34 p53 | `#godpathspell <-1 - 7>` |
| `#godrebirth` | Defined | Nation | M6.34 p47 | `#godrebirth` |
| `#godsite` | Defined | Monster | M6.34 p14 | `#godsite "<site name>" \| <site nbr>` |
| `#gold` | Defined | Event, Monster, Site | E6.29 p12; M6.34 p27; M6.34 p38; E6.29 p20; M6.34 p60 | `#gold <value>` |
| `#golemhp` | Defined | Nation | M6.34 p49 | `#golemhp <percent>` |
| `#goodleader` | Defined | Monster | M6.34 p31 | `#goodleader` |
| `#goodmagicleader` | Defined | Monster | M6.34 p32 | `#goodmagicleader` |
| `#goodundeadleader` | Defined | Monster | M6.34 p32 | `#goodundeadleader` |
| `#grandcom` | Defined | Monster | M6.34 p35; M6.34 p60 | `#grandcom <0 or 1>` |
| `#greaterhorror` | Defined | Monster | M6.34 p19 | `#greaterhorror` |
| `#greekreanim` | Defined | Nation | M6.34 p50 | `#greekreanim` |
| `#groundcol` | Defined | Map | P6.26 p8 | `#groundcol <red> <green> <blue>` |
| `#growhp` | Defined | Monster | M6.34 p28 | `#growhp <hit points>` |
| `#growthpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#growthpower <bonus>` |
| `#growthrecscale` | Defined | Monster | M6.34 p15 | `#growthrecscale <value>` |
| `#growthscale` | Defined | Bless | M6.34 p37 | `#growthscale <value>` |
| `#guardcom` | Defined | Nation | M6.34 p46 | `#guardcom "<monster name>" \| <monster nbr>` |
| `#guardmult` | Defined | Nation | M6.34 p46 | `#guardmult <multiplier>` |
| `#guardspirit` | Defined | Monster, Nation | M6.34 p49 | `#guardspirit "<monster name>" \| <nbr>` |
| `#guardspiritbonus` | Defined | Item, Monster | M6.34 p25; M6.34 p57 | `#guardspiritbonus <value>` |
| `#guardunit` | Defined | Nation | M6.34 p46 | `#guardunit "<monster name>" \| <monster nbr>` |

### H

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#halfdeathinc` | Defined | Nation | M6.34 p49 | `#halfdeathinc` |
| `#halfdeathpop` | Defined | Nation | M6.34 p49 | `#halfdeathpop` |
| `#halfstr` | Defined | Weapon | M6.34 p9 | `#halfstr` |
| `#haltheretic` | Defined | Monster | M6.34 p24; M6.34 p59 | `#haltheretic <bonus>` |
| `#hardmrneg` | Defined | Weapon | M6.34 p9 | `#hardmrneg` |
| `#hatesterr` | Defined | Site | M6.34 p44 | `#hatesterr <terrain mask>` |
| `#header` | Defined | Event | E6.29 p11 | `#header <type>` |
| `#heal` | Defined | Monster, Site | M6.34 p21; M6.34 p40 | `#heal` |
| `#healaff` | Defined | Event | E6.29 p15 | `#healaff <nbr>` |
| `#healer` | Defined | Monster | M6.34 p21; M6.34 p59 | `#healer <percent>` |
| `#heat` | Defined | Monster | M6.34 p23; M6.34 p59 | `#heat <value>` |
| `#heatrec` | Mention | Monster | M6.34 p15 | `#heatrec` |
| `#heatrecscale` | Defined | Monster | M6.34 p15 | `#heatrecscale <value>` |
| `#heatscale` | Defined | Bless | M6.34 p37 | `#heatscale <value>` |
| `#heavyitem` | Defined | Item | M6.34 p57 | `#heavyitem <0 or 1>` |
| `#heretic` | Defined | Monster | M6.34 p26; M6.34 p60 | `#heretic <value>` |
| `#hero1...10` | Defined; template | Nation | M6.34 p45 | `#hero1...10 <monster nbr>` |
| `#hiddenench` | Defined | Spell | M6.34 p53 | `#hiddenench <0 - 1>` |
| `#hiddensite` | Defined | Event | E6.29 p13 | `#hiddensite <site number>` |
| `#hidedom` | Defined | Nation | M6.34 p49 | `#hidedom <0 or 1>` |
| `#holy` | Defined | Monster | M6.34 p19 | `#holy` |
| `#holyboost` | Defined | Event | E6.29 p16 | `#holyboost "name" \| <number>` |
| `#holycost` | Defined | Monster | M6.34 p19 | `#holycost <holy points>` |
| `#holyfire` | Defined | Site | M6.34 p40 | `#holyfire <chance>` |
| `#holyifhit` | Defined | Weapon | M6.34 p11 | `#holyifhit <dmg>` |
| `#holypower` | Defined | Site | M6.34 p40 | `#holypower <chance>` |
| `#holyrange` | Defined | Monster | M6.34 p34; M6.34 p60 | `#holyrange <range>` |
| `#holystunifhit` | Defined | Weapon | M6.34 p11 | `#holystunifhit <dmg>` |
| `#homecoldscaleres` | Defined | Site | M6.34 p44 | `#homecoldscaleres <steps>` |
| `#homecom` | Defined | Monster | M6.34 p38 | `#homecom "<monster name>" \| <monster nbr>` |
| `#homefort` | Defined | Nation | M6.34 p48 | `#homefort <fort nbr>` |
| `#homeheatscaleres` | Defined | Site | M6.34 p44 | `#homeheatscaleres <steps>` |
| `#homemon` | Defined | Monster | M6.34 p38 | `#homemon "<monster name>" \| <monster nbr>` |
| `#homerealm` | Defined | General, Monster, Nation, Spell | M6.34 p14; M6.34 p47; M6.34 p53; M6.34 p64 | `#homerealm <realm nbr>` |
| `#homeshape` | Defined | Monster | M6.34 p28 | `#homeshape "<monster name>" \| <monster nbr>` |
| `#homesick` | Defined | Monster | M6.34 p21; M6.34 p59 | `#homesick <percent>` |
| `#horrordeserter` | Defined | Monster | M6.34 p15 | `#horrordeserter <percent>` |
| `#horrormark` | Defined | Monster, Site | M6.34 p24; M6.34 p40 | `#horrormark` |
| `#horsereanim` | Defined | Nation | M6.34 p50 | `#horsereanim` |
| `#horsetattoo` | Defined | Monster | M6.34 p26 | `#horsetattoo <value>` |
| `#hp` | Defined | Item, Monster | M6.34 p16; M6.34 p56 | `#hp <hit points>` |
| `#hpoverflow` | Defined | Monster | M6.34 p22; M6.34 p59 | `#hpoverflow` |
| `#humanoid` | Defined | Monster | M6.34 p18 | `#humanoid` |

### I

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#iceforging` | Defined | Monster | M6.34 p26; M6.34 p60 | `#iceforging <value>` |
| `#icenatprot` | Defined | Monster | M6.34 p22; M6.34 p59 | `#icenatprot <prot>` |
| `#iceprot` | Defined | Monster | M6.34 p22; M6.34 p59 | `#iceprot <prot>` |
| `#iceweapon` | Defined | Weapon | M6.34 p10 | `#iceweapon` |
| `#icon` | Defined | General, Metadata | M6.34 p5 | `#icon "<image.tga>"` |
| `#id` | Defined | Event | E6.29 p18 | `#id <eventid>` |
| `#idealcold` | Defined | Site | M6.34 p43 | `#idealcold <cold>` |
| `#illusion` | Defined | Monster | M6.34 p19 | `#illusion` |
| `#illusionsimmune` | Defined | Weapon | M6.34 p10 | `#illusionsimmune` |
| `#imagefile` | Defined | Map | P6.26 p3 | `#imagefile <filename>` |
| `#immobile` | Defined | Monster | M6.34 p19 | `#immobile` |
| `#immortal` | Defined | Monster | M6.34 p23 | `#immortal` |
| `#inanimate` | Defined | Monster | M6.34 p19 | `#inanimate` |
| `#inanimateimmune` | Defined | Weapon | M6.34 p9 | `#inanimateimmune` |
| `#inc10var` | Defined | Event | E6.29 p18 | `#inc10var <event var>` |
| `#inccorpses` | Defined | Event | E6.29 p13 | `#inccorpses <amount>` |
| `#incdom` | Defined | Event | E6.29 p13 | `#incdom <value>` |
| `#incorporate` | Defined | Monster | M6.34 p25; M6.34 p59 | `#incorporate <dmg>` |
| `#incpop` | Defined | Event | E6.29 p13 | `#incpop <dekapop>` |
| `#incprovdef` | Defined | Monster | M6.34 p27; M6.34 p60 | `#incprovdef <value>` |
| `#incscale` | Defined | Event, Monster, Site | E6.29 p12; M6.34 p27; M6.34 p39; M6.34 p60 | `#incscale <scale>` |
| `#incscale2` | Defined | Event | E6.29 p12; E6.29 p19 | `#incscale2 <scale>` |
| `#incscale3` | Defined | Event | E6.29 p12 | `#incscale3 <scale>` |
| `#incunrest` | Defined | Event, Monster | M6.34 p27; E6.29 p19; M6.34 p60 | `#incunrest <value>` |
| `#incvar` | Defined | Event | E6.29 p18 | `#incvar <event var>` |
| `#indepflag` | Defined | Nation | M6.34 p41 | `#indepflag "<imgfile>"` |
| `#indepmove` | Defined | Monster | M6.34 p20 | `#indepmove <percent>` |
| `#indepspells` | Defined | Monster | M6.34 p35 | `#indepspells <level>` |
| `#indepstay` | Defined | Monster | M6.34 p20 | `#indepstay <0 - 1>` |
| `#infernoret` | Defined | Monster | M6.34 p35; M6.34 p60 | `#infernoret <chance>` |
| `#inquisitor` | Defined | Monster | M6.34 p26; M6.34 p60 | `#inquisitor` |
| `#insane` | Defined | Monster | M6.34 p22 | `#insane <percent>` |
| `#insanify` | Defined | Monster | M6.34 p27; M6.34 p60 | `#insanify <percent>` |
| `#inspirational` | Defined | Monster | M6.34 p32; M6.34 p60 | `#inspirational <bonus>` |
| `#inspiringres` | Defined | Monster | M6.34 p34; M6.34 p60 | `#inspiringres <value>` |
| `#internal` | Defined | Weapon | M6.34 p10 | `#internal` |
| `#invisible` | Defined | Monster | M6.34 p25; M6.34 p59 | `#invisible` |
| `#invulnerable` | Defined | Monster | M6.34 p22; M6.34 p59 | `#invulnerable <prot>` |
| `#invvar` | Defined | Event | E6.29 p18 | `#invvar <event var>` |
| `#ironarmor` | Defined | Armour | M6.34 p13 | `#ironarmor` |
| `#ironskin` | Defined | Item | M6.34 p56 | `#ironskin` |
| `#ironvul` | Defined | Monster | M6.34 p23; M6.34 p59 | `#ironvul <points>` |
| `#ironweapon` | Defined | Weapon | M6.34 p10 | `#ironweapon` |
| `#islance` | Defined | Item | M6.34 p57 | `#islance` |
| `#islandnation` | Defined | Site | M6.34 p43 | `#islandnation` |
| `#islandsite` | Defined | Site | M6.34 p43 | `#islandsite "<site name>"` |
| `#item` | Defined | Mercenary | M6.34 p63 | `#item "<item name>"` |
| `#itemcost1` | Defined | Item | M6.34 p58 | `#itemcost1 <bonus>` |
| `#itemcost2` | Defined | Item | M6.34 p58 | `#itemcost2 <bonus>` |
| `#itemdrawsize` | Defined | Item | M6.34 p58 | `#itemdrawsize <value>` |
| `#itemslots` | Defined | Monster | M6.34 p18 | `#itemslots <slot value>` |
| `#ivylord` | Defined | Monster | M6.34 p30; M6.34 p61 | `#ivylord <nbr>` |

### K

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#kill` | Defined | Event | E6.29 p13 | `#kill <percent>` |
| `#kill2d6mon` | Defined | Event | E6.29 p15 | `#kill2d6mon "name" \| <number>` |
| `#killcappop` | Defined | Site | M6.34 p44 | `#killcappop <percent>` |
| `#killcom` | Defined | Event | E6.29 p15 | `#killcom "name" \| <number>` |
| `#killdemonifhit` | Defined | Weapon | M6.34 p11 | `#killdemonifhit <dmg>` |
| `#killfeatures` | Defined | Map | P6.26 p7 | `#killfeatures` |
| `#killmagicifhit` | Defined | Weapon | M6.34 p11 | `#killmagicifhit <dmg>` |
| `#killmon` | Defined | Event | E6.29 p15 | `#killmon "name" \| <number>` |
| `#killpop` | Defined | Event | E6.29 p13 | `#killpop <dekapop>` |
| `#killtarg` | Defined | Event | E6.29 p15 | `#killtarg` |
| `#knownfeature` | Defined | Map | P6.26 p8 | `#knownfeature "<site name>" \| <site nbr>` |
| `#kokytosret` | Defined | Monster | M6.34 p35; M6.34 p60 | `#kokytosret <chance>` |

### L

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##landname##` | Reference; message | Event | E6.29 p11 | `##landname##` |
| `#lab` | Defined | Event, Map, Site | E6.29 p13; P6.26 p8; M6.34 p40 | `#lab < 0 \| 1>` |
| `#labcost` | Defined | Nation | M6.34 p48 | `#labcost <price>` |
| `#labxpshape` | Defined | Monster | M6.34 p28 | `#labxpshape <xp value>` |
| `#lamialord` | Defined | Monster | M6.34 p30; M6.34 p61 | `#lamialord <nbr>` |
| `#lanceok` | Defined | Monster | M6.34 p19 | `#lanceok` |
| `#land` | Defined | Map | P6.26 p6 | `#land <province nbr>` |
| `#landcom` | Defined | Nation | M6.34 p45 | `#landcom "<monster name>" \| <monster nbr>` |
| `#landdamage` | Defined | Monster | M6.34 p21 | `#landdamage <percent>` |
| `#landgold` | Defined | Event | E6.29 p13 | `#landgold <value>` |
| `#landname` | Defined | Map | P6.26 p4 | `#landname <province nbr> "name"` |
| `#landprod` | Defined | Event | E6.29 p13 | `#landprod <value>` |
| `#landrec` | Defined | Nation | M6.34 p45 | `#landrec "<monster name>" \| <monster nbr>` |
| `#landshape` | Defined | Monster | M6.34 p28 | `#landshape "<monster name>" \| <monster nbr>` |
| `#latehero` | Defined | Monster | M6.34 p33 | `#latehero <min turn>` |
| `#len` | Defined | Weapon | M6.34 p7; M6.34 p9 | `#len <length>` |
| `#leper` | Defined | Monster | M6.34 p27; M6.34 p60 | `#leper <percent>` |
| `#lesserhorror` | Defined | Monster | M6.34 p19 | `#lesserhorror` |
| `#level` | Defined | Mercenary, Site | M6.34 p38; M6.34 p63 | `#level <level>` |
| `#lich` | Defined | Monster | M6.34 p28 | `#lich "<monster name>" \| <monster nbr>` |
| `#likespop` | Defined | Nation | M6.34 p47 | `#likespop <poptype>` |
| `#likesterr` | Defined | Site | M6.34 p43 | `#likesterr <terrain mask>` |
| `#limitedregen` | Defined | Item | M6.34 p57 | `#limitedregen <percent>` |
| `#linger` | Defined | Event | E6.29 p17 | `#linger <nbr of turns>` |
| `#lizard` | Defined | Monster | M6.34 p18 | `#lizard` |
| `#loc` | Defined | Site | M6.34 p37 | `#loc <locmask>` |
| `#localglobal` | Defined | Spell | M6.34 p54 | `#localglobal <0 - 1>` |
| `#localsun` | Defined | Monster | M6.34 p27; M6.34 p60 | `#localsun` |
| `#look` | Defined | Site | M6.34 p37 | `#look <site spr>` |
| `#loop` | Defined | Sound | M6.34 p5 | `#loop <sample nbr>` |
| `#loseeye` | Defined | Item | M6.34 p58 | `#loseeye` |
| `#luck` | Defined | Item | M6.34 p56 | `#luck` |
| `#luckevents` | Defined | General | M6.34 p61 | `#luckevents <percent>` |
| `#luckscale` | Defined | Bless | M6.34 p37 | `#luckscale <value>` |

### M

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#mag_air` | Defined | Map | P6.26 p9 | `#mag_air <level>` |
| `#mag_astral` | Defined | Map | P6.26 p9 | `#mag_astral <level>` |
| `#mag_blood` | Defined | Map | P6.26 p9 | `#mag_blood <level>` |
| `#mag_death` | Defined | Map | P6.26 p9 | `#mag_death <level>` |
| `#mag_earth` | Defined | Map | P6.26 p9 | `#mag_earth <level>` |
| `#mag_fire` | Defined | Map | P6.26 p9 | `#mag_fire <level>` |
| `#mag_glamour` | Defined | Map | P6.26 p9 | `#mag_glamour <level>` |
| `#mag_nature` | Defined | Map | P6.26 p9 | `#mag_nature <level>` |
| `#mag_priest` | Defined | Map | P6.26 p9 | `#mag_priest <level>` |
| `#mag_water` | Defined | Map | P6.26 p9 | `#mag_water <level>` |
| `#magic` | Defined | AI, Weapon | M6.34 p9; M6.34 p64 | `#magic` |
| `#magicarmor` | Defined | Armour | M6.34 p13 | `#magicarmor` |
| `#magicbeing` | Defined | Monster | M6.34 p19 | `#magicbeing` |
| `#magicboost` | Defined | Monster, Spell | M6.34 p33; M6.34 p56 | `#magicboost <path> <boost>` |
| `#magiccommand` | Defined | Monster | M6.34 p32; M6.34 p60 | `#magiccommand <value>` |
| `#magicimmune` | Defined | Monster | M6.34 p34; M6.34 p60 | `#magicimmune` |
| `#magicitem` | Defined | Event | E6.29 p11; E6.29 p19 | `#magicitem <rarity>` |
| `#magiconly` | Defined | Weapon | M6.34 p9 | `#magiconly` |
| `#magicpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#magicpower <bonus>` |
| `#magicscale` | Defined | Bless | M6.34 p37 | `#magicscale <value>` |
| `#magicskill` | Defined | Monster | M6.34 p33 | `#magicskill <path> <level>` |
| `#magicstudy` | Defined | Monster | M6.34 p35; M6.34 p60 | `#magicstudy <bonus>` |
| `#mainlevel` | Defined | Item | M6.34 p55 | `#mainlevel <path>` |
| `#mainpath` | Defined | Item | M6.34 p55 | `#mainpath <path>` |
| `#makecrater` | Defined | Sound | M6.34 p52 | `#makecrater <0 or 1>` |
| `#makemonsters1` | Reference | Monster | M6.34 p61 | `#makemonsters1` |
| `#makemonsters1...5` | Defined; template | Monster | M6.34 p29 | `#makemonsters1...5 "<monster name>" \| <monster nbr>` |
| `#makemonsters2` | Reference | Monster | M6.34 p61 | `#makemonsters2` |
| `#makemonsters3` | Reference | Monster | M6.34 p61 | `#makemonsters3` |
| `#makemonsters4` | Reference | Monster | M6.34 p61 | `#makemonsters4` |
| `#makemonsters5` | Reference | Monster | M6.34 p61 | `#makemonsters5` |
| `#makepearls` | Defined | Monster | M6.34 p35; M6.34 p60 | `#makepearls <value>` |
| `#manikinreanim` | Defined | Nation | M6.34 p50 | `#manikinreanim` |
| `#mapdomcol` | Defined | Map | P6.26 p4 | `#mapdomcol <red> <green> <blue> <alpha>` |
| `#mapmove` | Defined | Monster | M6.34 p17 | `#mapmove <speed>` |
| `#mapnohide` | Defined | Map | P6.26 p3 | `#mapnohide` |
| `#mapsize` | Defined | Map | P6.26 p3 | `#mapsize <width> <height>` |
| `#mapspeed` | Defined | Item | M6.34 p57 | `#mapspeed <value>` |
| `#mapteleport` | Defined | Monster | M6.34 p20 | `#mapteleport` |
| `#maptextcol` | Defined | Map | P6.26 p4 | `#maptextcol <red> <green> <blue> <alpha>` |
| `#mason` | Defined | Monster | M6.34 p27; M6.34 p60 | `#mason` |
| `#masterrit` | Defined | Monster | M6.34 p33 | `#masterrit <value>` |
| `#mastersmith` | Defined | Monster | M6.34 p35 | `#mastersmith <value>` |
| `#maxage` | Defined | Monster | M6.34 p21 | `#maxage <age>` |
| `#maxbounces` | Defined | Spell | M6.34 p54 | `#maxbounces <bounces>` |
| `#maxdeadhp` | Defined | Monster | M6.34 p22; M6.34 p59 | `#maxdeadhp <HP>` |
| `#maxprison` | Defined | Monster, Nation | M6.34 p14; M6.34 p47 | `#maxprison <0 - 2>` |
| `#maxsize` | Defined | Item | M6.34 p57 | `#maxsize <size>` |
| `#maybeaddsite` | Defined | Event | E6.29 p13 | `#maybeaddsite <site number>` |
| `#maybehiddensite` | Defined | Event | E6.29 p13 | `#maybehiddensite <site number>` |
| `#melee50` | Defined | Weapon | M6.34 p10 | `#melee50` |
| `#merccost` | Defined | Nation | M6.34 p45 | `#merccost <percent>` |
| `#minascension` | Defined | Event | E6.29 p18 | `#minascension <AP>` |
| `#mind` | Defined | Weapon | M6.34 p9 | `#mind` |
| `#mindcollar` | Defined | Monster | M6.34 p26; M6.34 p60 | `#mindcollar <dmg>` |
| `#mindslime` | Defined | Monster | M6.34 p24; M6.34 p59 | `#mindslime <area>` |
| `#mindvessel` | Defined | Monster | M6.34 p27 | `#mindvessel <0 or 1>` |
| `#minmen` | Defined | Mercenary | M6.34 p63 | `#minmen <value>` |
| `#minpay` | Defined | Mercenary | M6.34 p63 | `#minpay <gold>` |
| `#minprison` | Defined | Monster, Nation | M6.34 p14; M6.34 p47 | `#minprison <0 - 2>` |
| `#minsize` | Defined | Item | M6.34 p57 | `#minsize <size>` |
| `#minsizeleader` | Reference | Monster | M6.34 p36 | `#minsizeleader` |
| `#miscshape` | Defined | Monster | M6.34 p18 | `#miscshape` |
| `#misfortscale` | Defined | Bless | M6.34 p37 | `#misfortscale <value>` |
| `#misfortune` | Defined | General | M6.34 p61 | `#misfortune<percent>` |
| `#mobilearcher` | Defined | Monster | M6.34 p20; M6.34 p58 | `#mobilearcher <0 or 1>` |
| `#modname` | Defined | General, Metadata | M6.34 p5; M6.34 p64 | `#modname "<name>"` |
| `#mon` | Defined | Monster | M6.34 p38 | `#mon "<monster name>" \| <monster nbr>` |
| `#monpresentrec` | Defined | Monster | M6.34 p15 | `#monpresentrec "<monster name>" \| <monster nbr>` |
| `#montag` | Defined | Monster | M6.34 p29 | `#montag <value>` |
| `#montagweight` | Defined | Monster | M6.34 p30 | `#montagweight <weight>` |
| `#mor` | Defined | Monster | M6.34 p17 | `#mor <morale>` |
| `#morale` | Defined | Item | M6.34 p56 | `#morale <value>` |
| `#moregrowth` | Defined | Monster, Site | M6.34 p14; M6.34 p44 | `#moregrowth <-5 - 5>` |
| `#moreheat` | Defined | Monster, Site | M6.34 p14; M6.34 p44 | `#moreheat <-5 - 5>` |
| `#moreluck` | Defined | Monster, Site | M6.34 p14; M6.34 p44 | `#moreluck <-5 - 5>` |
| `#moremagic` | Defined | Monster, Site | M6.34 p14; M6.34 p44 | `#moremagic <-5 - 5>` |
| `#moreorder` | Defined | Monster, Site | M6.34 p14; M6.34 p44 | `#moreorder <-5 - 5>` |
| `#moreprod` | Defined | Monster, Site | M6.34 p14; M6.34 p44 | `#moreprod <-5 - 5>` |
| `#morroll` | Defined | Weapon | M6.34 p10 | `#morroll` |
| `#mountainsurvival` | Defined | Monster | M6.34 p20 | `#mountainsurvival` |
| `#mounted` | Defined | Monster | M6.34 p31 | `#mounted` |
| `#mountedhumanoid` | Defined | Monster | M6.34 p18 | `#mountedhumanoid` |
| `#mountiscom` | Defined | Monster | M6.34 p31 | `#mountiscom <0 or 1>` |
| `#mountlabcost` | Defined | Nation | M6.34 p48 | `#mountlabcost <price>` |
| `#mountmnr` | Defined | Monster | M6.34 p30 | `#mountmnr "<monster name>" \| <monster nbr>` |
| `#mounttemplecost` | Defined | Nation | M6.34 p48 | `#mounttemplecost <price>` |
| `#mr` | Defined | Item, Monster | M6.34 p17; M6.34 p56 | `#mr <magic resistance>` |
| `#mrhalf` | Defined | Weapon | M6.34 p9 | `#mrhalf` |
| `#mrnegates` | Defined | Weapon | M6.34 p9 | `#mrnegates` |
| `#mrnegateseasily` | Defined | Weapon | M6.34 p9 | `#mrnegateseasily` |
| `#msg` | Defined | Event | E6.29 p11; E6.29 p5; E6.29 p19; E6.29 p20 | `#msg "<message text>"` |
| `#multihero1` | Mention | Nation | M6.34 p45 | `#multihero1` |
| `#multihero1...7` | Defined; template | Nation | M6.34 p45 | `#multihero1...7 <monster nbr>` |
| `#mute` | Defined | Item | M6.34 p58 | `#mute` |

### N

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##natname##` | Reference; message | Event | E6.29 p11 | `##natname##` |
| `#naga` | Defined | Monster | M6.34 p18 | `#naga` |
| `#name` | Defined | Armour, Bless, Event, General, Item, Mercenary, Monster, Nation, Site, Spell, Weapon | M6.34 p7; M6.34 p12; M6.34 p13; M6.34 p37; M6.34 p42; +6 | `#name "<name>"` |
| `#nametype` | Defined | Monster | M6.34 p30 | `#nametype <name type nbr>` |
| `#napbreakrit` | Defined | Spell | M6.34 p54 | `#napbreakrit <value>` |
| `#nat` | Defined | Monster | M6.34 p38 | `#nat <nation nbr>` |
| `#natcom` | Defined | Monster | M6.34 p38 | `#natcom "<monster name>" \| <monster nbr>` |
| `#nation` | Defined | Event | E6.29 p11; E6.29 p19 | `#nation <nation number>` |
| `#nationench` | Defined | Event | E6.29 p11; E6.29 p20 | `#nationench <ench nbr>` |
| `#nationinc` | Defined | Nation | M6.34 p49 | `#nationinc <percent>` |
| `#nationrebate` | Defined | Item | M6.34 p57 | `#nationrebate <nation nbr> \| "nation name"` |
| `#natmon` | Defined | Monster | M6.34 p38 | `#natmon "<monster name>" \| <monster nbr>` |
| `#natural` | Defined | Weapon | M6.34 p7 | `#natural` |
| `#natureblessbonus` | Defined | Nation | M6.34 p47 | `#natureblessbonus <0 - 9>` |
| `#natureboost` | Defined | Event | E6.29 p16 | `#natureboost "name" \| <number>` |
| `#naturerange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#naturerange <range>` |
| `#neednoteat` | Defined | Monster | M6.34 p26 | `#neednoteat` |
| `#neighbour` | Defined | Map | P6.26 p4 | `#neighbour <province nbr> <province nbr>` |
| `#neighbourspec` | Defined | Map | P6.26 p4 | `#neighbourspec <land1> <land2> <spcnbr>` |
| `#newarmor` | Defined | Armour | M6.34 p12 | `#newarmor <armor nbr>` |
| `#newdom` | Defined | Event | E6.29 p13 | `#newdom <value>` |
| `#newevent` | Defined | Event | E6.29 p2; E6.29 p19; E6.29 p20 | `#newevent` |
| `#newitem` | Defined | Item | M6.34 p55 | `#newitem` |
| `#newmerc` | Defined | Mercenary | M6.34 p63 | `#newmerc` |
| `#newmonster` | Defined | General, Monster | M6.34 p13 | `#newmonster [<monster nbr>]` |
| `#newnation` | Defined | General, Item, Nation, Spell | M6.34 p42; M6.34 p64 | `#newnation` |
| `#newsite` | Defined | General, Site | M6.34 p37 | `#newsite [<site nbr>]` |
| `#newspell` | Defined | Event, General, Spell | M6.34 p50; E6.29 p20 | `#newspell` |
| `#newtemplate` | Defined | AI | M6.34 p63 | `#newtemplate <nation nbr>` |
| `#newweapon` | Defined | Weapon | M6.34 p7; M6.34 p9 | `#newweapon <weapon nbr>` |
| `#nextingeo` | Defined | Spell | M6.34 p51 | `#nextingeo <terrain mask>` |
| `#nextspell` | Defined | Spell | M6.34 p51 | `#nextspell "<spell name>" \| <nbr>` |
| `#nhwound` | Defined | Item | M6.34 p58 | `#nhwound` |
| `#nightmareaura` | Defined | Monster | M6.34 p24 | `#nightmareaura <area>` |
| `#noaging` | Defined | Item | M6.34 p58 | `#noaging <percent>` |
| `#noagingland` | Defined | Item | M6.34 p58 | `#noagingland <percent>` |
| `#nobadevents` | Defined | Monster | M6.34 p27; M6.34 p60 | `#nobadevents <value>` |
| `#nobarding` | Defined | Monster | M6.34 p31 | `#nobarding` |
| `#nocastmindless` | Defined | Spell | M6.34 p53 | `#nocastmindless <0 - 1>` |
| `#nocoldblood` | Defined | Item | M6.34 p57 | `#nocoldblood` |
| `#nodeathsupply` | Defined | Nation | M6.34 p49 | `#nodeathsupply` |
| `#nodeepcaves` | Defined | Map | P6.26 p3 | `#nodeepcaves` |
| `#nodeepchoice` | Defined | Map | P6.26 p3 | `#nodeepchoice` |
| `#nodemon` | Defined | Item | M6.34 p57 | `#nodemon` |
| `#nofalldmg` | Defined | Monster | M6.34 p31 | `#nofalldmg` |
| `#nofemale` | Defined | Item | M6.34 p57 | `#nofemale` |
| `#nofind` | Defined | Item | M6.34 p57 | `#nofind` |
| `#nofmounts` | Defined | Monster | M6.34 p30 | `#nofmounts <mounts>` |
| `#noforeignrec` | Defined | Nation | M6.34 p45 | `#noforeignrec` |
| `#noforgebonus` | Defined | Item | M6.34 p57 | `#noforgebonus` |
| `#nofriders` | Defined | Monster | M6.34 p30 | `#nofriders <riders>` |
| `#nogeodst` | Defined | Spell | M6.34 p52 | `#nogeodst <terrain mask>` |
| `#nogeosrc` | Mention | Spell | M6.34 p52 | `#nogeosrc` |
| `#noheal` | Defined | Monster | M6.34 p21 | `#noheal` |
| `#nohof` | Defined | Monster | M6.34 p27 | `#nohof` |
| `#nohomelandnames` | Defined | Map | P6.26 p5 | `#nohomelandnames` |
| `#noimmobile` | Defined | Item | M6.34 p57 | `#noimmobile` |
| `#noinanim` | Defined | Item | M6.34 p57 | `#noinanim` |
| `#noitem` | Defined | Monster | M6.34 p18 | `#noitem` |
| `#nolandtrace` | Defined | Spell | M6.34 p52 | `#nolandtrace <0 or 1>` |
| `#noleader` | Defined | Monster | M6.34 p31 | `#noleader` |
| `#nolog` | Defined | Event | E6.29 p11 | `#nolog` |
| `#nomagicleader` | Defined | Monster | M6.34 p32 | `#nomagicleader` |
| `#nomounted` | Defined | Item | M6.34 p57 | `#nomounted` |
| `#nomovepen` | Defined | Monster | M6.34 p20; M6.34 p58 | `#nomovepen` |
| `#nonamefilter` | Defined | Map | P6.26 p5 | `#nonamefilter` |
| `#nopreach` | Defined | Nation | M6.34 p49 | `#nopreach` |
| `#norange` | Defined | Monster | M6.34 p20; M6.34 p58 | `#norange <chance>` |
| `#noremount` | Defined | Monster | M6.34 p31 | `#noremount` |
| `#norepel` | Defined | Weapon | M6.34 p10 | `#norepel` |
| `#noreqlab` | Defined | Monster | M6.34 p15 | `#noreqlab` |
| `#noreqtemple` | Defined | Monster | M6.34 p15 | `#noreqtemple` |
| `#noriverpass` | Defined | Monster | M6.34 p20; M6.34 p58 | `#noriverpass` |
| `#noslowrec` | Defined | Monster | M6.34 p14 | `#noslowrec` |
| `#nospiritform` | Defined | Monster | M6.34 p19 | `#nospiritform` |
| `#nostart` | Defined | Map | P6.26 p6 | `#nostart <province nbr>` |
| `#nostr` | Defined | Weapon | M6.34 p9 | `#nostr` |
| `#notdismounted` | Defined | Weapon | M6.34 p11 | `#notdismounted` |
| `#notdomshape` | Defined | Monster | M6.34 p28 | `#notdomshape "<monster name>" \| <monster nbr>` |
| `#notext` | Defined | Event | E6.29 p11; E6.29 p20 | `#notext` |
| `#notfornation` | Defined | Item, Spell | M6.34 p53; M6.34 p57 | `#notfornation <nation nbr> \| "nation name"` |
| `#nothrowoff` | Defined | Monster | M6.34 p31 | `#nothrowoff` |
| `#notindoors` | Defined | Spell | M6.34 p54 | `#notindoors <-1 to 1>` |
| `#notmnr` | Defined | Spell | M6.34 p53 | `#notmnr "<monster name>" \| <monster nbr>` |
| `#notmounted` | Defined | Weapon | M6.34 p11 | `#notmounted <1 - 2>` |
| `#noundead` | Defined | Item | M6.34 p57 | `#noundead` |
| `#noundeadgods` | Defined | Nation | M6.34 p47 | `#noundeadgods` |
| `#noundeadleader` | Defined | Monster | M6.34 p32 | `#noundeadleader` |
| `#nouw` | Defined | Weapon | M6.34 p11 | `#nouw` |
| `#nowatertrace` | Defined | Spell | M6.34 p52 | `#nowatertrace <0 or 1>` |
| `#noweapon` | Defined | Monster | M6.34 p18 | `#noweapon <0 or 1>` |
| `#nowish` | Defined | Monster | M6.34 p15 | `#nowish` |
| `#nratt` | Defined | Weapon | M6.34 p7 | `#nratt <nbr of attacks>` |
| `#nreff` | Defined | Spell | M6.34 p52 | `#nreff <nbr of effects>` |
| `#nrunits` | Defined | Mercenary | M6.34 p63 | `#nrunits <value>` |

### O

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#okleader` | Defined | Monster | M6.34 p31 | `#okleader` |
| `#okmagicleader` | Defined | Monster | M6.34 p32 | `#okmagicleader` |
| `#okundeadleader` | Defined | Monster | M6.34 p32 | `#okundeadleader` |
| `#older` | Defined | Monster | M6.34 p21 | `#older <age>` |
| `#onebattlespell` | Defined | Monster | M6.34 p35 | `#onebattlespell "<spell name>" \| <nbr>` |
| `#onisummon` | Defined | Monster | M6.34 p30; M6.34 p61 | `#onisummon <0 - 100>` |
| `#onlyatsite` | Defined | Spell | M6.34 p52 | `#onlyatsite <"site name"> \| <site nbr>` |
| `#onlycoastsrc` | Defined | Spell | M6.34 p52 | `#onlycoastsrc <0 - 1>` |
| `#onlycoldblood` | Defined | Item | M6.34 p58 | `#onlycoldblood` |
| `#onlydemon` | Defined | Item | M6.34 p58 | `#onlydemon` |
| `#onlyfemale` | Defined | Item | M6.34 p58 | `#onlyfemale` |
| `#onlyfriendlydst` | Defined | Spell | M6.34 p52 | `#onlyfriendlydst <0 - 2>` |
| `#onlygeodst` | Defined | Spell | M6.34 p52 | `#onlygeodst <terrain mask>` |
| `#onlygeosrc` | Defined | Spell | M6.34 p52 | `#onlygeosrc <terrain mask>` |
| `#onlyimmobile` | Defined | Item | M6.34 p58 | `#onlyimmobile` |
| `#onlyinanim` | Defined | Item | M6.34 p58 | `#onlyinanim` |
| `#onlymnr` | Defined | Spell | M6.34 p53 | `#onlymnr "<monster name>" \| <monster nbr>` |
| `#onlymounted` | Defined | Item | M6.34 p58 | `#onlymounted` |
| `#onlyowndst` | Defined | Spell | M6.34 p52 | `#onlyowndst <0 or 1>` |
| `#onlysitedst` | Defined | Spell | M6.34 p52 | `#onlysitedst <"site name"> \| <site nbr>` |
| `#onlyundead` | Defined | Item | M6.34 p58 | `#onlyundead` |
| `#order` | Defined | Event | E6.29 p17 | `#order <order bitmask>` |
| `#orderrecscale` | Defined | Monster | M6.34 p15 | `#orderrecscale <value>` |
| `#orderscale` | Defined | Bless | M6.34 p37 | `#orderscale <value>` |
| `#overcharged` | Defined | Monster | M6.34 p24; M6.34 p59 | `#overcharged <dmg>` |
| `#owner` | Defined | Map | P6.26 p7 | `#owner <nation nbr>` |
| `#ownsmonrec` | Defined | Monster | M6.34 p15 | `#ownsmonrec "<monster name>" \| <monster nbr>` |

### P

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##playergodname##` | Reference; message | Spell | M6.34 p54 | `##playergodname##` |
| `##playergodthrone##` | Reference; message | Spell | M6.34 p54 | `##playergodthrone##` |
| `##playername##` | Reference; message | Spell | M6.34 p54 | `##playername##` |
| `##playerthrone##` | Reference; message | Spell | M6.34 p54 | `##playerthrone##` |
| `##profname##` | Reference; message | Event | E6.29 p11 | `##profname##` |
| `#path` | Defined | Event, Site, Spell | M6.34 p37; M6.34 p50; E6.29 p20 | `#path <path nbr>` |
| `#path0` | Defined | Bless | M6.34 p37 | `#path0 <path nbr>` |
| `#path1` | Defined | Bless | M6.34 p37 | `#path1 <path nbr>` |
| `#pathboost` | Defined | Event | E6.29 p16 | `#pathboost <path>` |
| `#pathcost` | Defined | Monster, Nation | M6.34 p14 | `#pathcost <design points>` |
| `#pathlevel` | Defined | Event, Spell | M6.34 p50; E6.29 p20 | `#pathlevel <reqnr> <level>` |
| `#patience` | Defined | Monster | M6.34 p20 | `#patience <value>` |
| `#patrolbonus` | Defined | Monster | M6.34 p26; M6.34 p60 | `#patrolbonus <value>` |
| `#pb` | Defined | Map | P6.26 p4 | `#pb <x> <y> <len> <province nbr>` |
| `#pen` | Defined | Spell | M6.34 p56 | `#pen <value>` |
| `#petrifyifhit` | Defined | Weapon | M6.34 p11 | `#petrifyifhit <dmg>` |
| `#pierce` | Defined | Weapon | M6.34 p9 | `#pierce` |
| `#pierceres` | Defined | Monster | M6.34 p23; M6.34 p59 | `#pierceres` |
| `#pillagebonus` | Defined | Monster | M6.34 p26; M6.34 p60 | `#pillagebonus <value>` |
| `#plaguedoctor` | Defined | Monster | M6.34 p21; M6.34 p59 | `#plaguedoctor <percent>` |
| `#plainshape` | Defined | Monster | M6.34 p28 | `#plainshape "<monster name>" \| <monster nbr>` |
| `#planename` | Defined | Map | P6.26 p3 | `#planename <text>` |
| `#plant` | Defined | Monster | M6.34 p19 | `#plant` |
| `#poison` | Defined | Event, Weapon | E6.29 p15; M6.34 p9 | `#poison <dmg>` |
| `#poisonarmor` | Defined | Monster | M6.34 p23; M6.34 p59 | `#poisonarmor <dmg>` |
| `#poisoncloud` | Defined | Monster | M6.34 p23; M6.34 p59 | `#poisoncloud <size>` |
| `#poisonifdmg` | Defined | Weapon | M6.34 p12 | `#poisonifdmg <dmg>` |
| `#poisonres` | Defined | Item, Monster | M6.34 p22; M6.34 p56 | `#poisonres <prot>` |
| `#poisonskin` | Defined | Monster | M6.34 p23; M6.34 p59 | `#poisonskin <0-500>` |
| `#polygetmagic` | Defined | Spell | M6.34 p53 | `#polygetmagic <0 - 1>` |
| `#polyimmune` | Defined | Item, Monster | M6.34 p19; M6.34 p57 | `#polyimmune` |
| `#pooramphibian` | Defined | Monster | M6.34 p19 | `#pooramphibian` |
| `#poorleader` | Defined | Monster | M6.34 p31 | `#poorleader` |
| `#poormagicleader` | Defined | Monster | M6.34 p32 | `#poormagicleader` |
| `#poorundeadleader` | Defined | Monster | M6.34 p32 | `#poorundeadleader` |
| `#popgrowth` | Defined | Site | M6.34 p40 | `#popgrowth <per mille>` |
| `#popkill` | Defined | Monster | M6.34 p27; M6.34 p60 | `#popkill <amount>` |
| `#poppergold` | Defined | General | M6.34 p61 | `#poppergold <people>` |
| `#poptype` | Defined | Map | P6.26 p6 | `#poptype <poptype nbr>` |
| `#population` | Defined | Map | P6.26 p8 | `#population <0-50000>` |
| `#portent` | Defined | Spell | M6.34 p54 | `#portent "text"` |
| `#powerofdeath` | Defined | Monster | M6.34 p26; M6.34 p59 | `#powerofdeath <limit>` |
| `#praise` | Defined | Monster | M6.34 p27; M6.34 p60 | `#praise <value>` |
| `#prec` | Defined | Item, Monster | M6.34 p16; M6.34 p56 | `#prec <precision>` |
| `#precision` | Defined | Spell | M6.34 p52 | `#precision <prec>` |
| `#priestreanim` | Defined | Nation | M6.34 p50 | `#priestreanim` |
| `#prison` | Defined | AI | M6.34 p64 | `#prison <nbr>` |
| `#prodscale` | Defined | Bless | M6.34 p37 | `#prodscale <value>` |
| `#prophetshape` | Defined | Monster | M6.34 p27 | `#prophetshape "<monster name>" \| <monster nbr>` |
| `#prot` | Defined | Armour, Monster | M6.34 p12; M6.34 p17 | `#prot <protection>` |
| `#protparts` | Defined | Armour | M6.34 p12 | `#protparts <head prot> <body prot>` |
| `#provrange` | Defined | Spell | M6.34 p52 | `#provrange <range>` |
| `#purgecalendar` | Defined | Event | E6.29 p18 | `#purgecalendar <attr>` |
| `#purgedelayed` | Defined | Event | E6.29 p18 | `#purgedelayed <attr>` |

### Q

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#quadruped` | Defined | Monster | M6.34 p18 | `#quadruped` |
| `#quickness` | Defined | Item | M6.34 p56 | `#quickness` |

### R

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#raiseonkill` | Defined | Monster | M6.34 p25; M6.34 p59 | `#raiseonkill <chance>` |
| `#raiseshape` | Defined | Monster | M6.34 p26; M6.34 p59 | `#raiseshape "<monster name>" \| <monster nbr>` |
| `#randequip` | Defined | Mercenary | M6.34 p63 | `#randequip <0-3>` |
| `#randomequip` | Defined | Map | P6.26 p9 | `#randomequip <rich>` |
| `#randomspell` | Defined | Monster, Spell | M6.34 p35; M6.34 p56 | `#randomspell <percent>` |
| `#range` | Defined | Spell, Weapon | M6.34 p7; M6.34 p52 | `#range` |
| `#range0` | Defined | Weapon | M6.34 p10 | `#range0` |
| `#range050` | Defined | Weapon | M6.34 p10 | `#range050` |
| `#raredomsummon` | Defined | Monster | M6.34 p29; M6.34 p61 | `#raredomsummon "<monster name>" \| <monster nbr>` |
| `#rarity` | Defined | Event, Site | E6.29 p2; M6.34 p38; E6.29 p19; E6.29 p20 | `#rarity <nbr>` |
| `#rcost` | Defined | Armour, Monster, Weapon | M6.34 p7; M6.34 p12; M6.34 p15 | `#rcost` |
| `#reanimator` | Defined | Monster | M6.34 p29 | `#reanimator <nbr>` |
| `#reanimpriest` | Defined | Monster, Nation | M6.34 p29; M6.34 p61 | `#reanimpriest` |
| `#recallgod` | Defined | Nation, Site | M6.34 p41; M6.34 p49 | `#recallgod <value>` |
| `#reclimit` | Defined | Monster | M6.34 p14 | `#reclimit <units / turn>` |
| `#reconst` | Defined | Monster | M6.34 p23 | `#reconst <percent>` |
| `#recrate` | Defined | Mercenary | M6.34 p63 | `#recrate <value>` |
| `#recuperation` | Defined | Item | M6.34 p58 | `#recuperation` |
| `#reform` | Defined | Monster | M6.34 p23 | `#reform <chance>` |
| `#reformtime` | Defined | Monster | M6.34 p23 | `#reformtime <extra months>` |
| `#regainmount` | Defined | Monster | M6.34 p31 | `#regainmount <0 or 1>` |
| `#regeneration` | Defined | Monster | M6.34 p22; M6.34 p59 | `#regeneration <percent>` |
| `#reinvigoration` | Defined | Monster | M6.34 p23; M6.34 p59 | `#reinvigoration <points>` |
| `#remgeo` | Defined | Event | E6.29 p13 | `#remgeo <terrain bitmask>` |
| `#remount` | Defined | Event | E6.29 p15 | `#remount` |
| `#removesite` | Defined | Event | E6.29 p13 | `#removesite <site number>` |
| `#req_2monsters` | Defined | Event | E6.29 p6 | `#req_2monsters "name" \| <number>` |
| `#req_5monsters` | Defined | Event | E6.29 p6 | `#req_5monsters "name" \| <number>` |
| `#req_ai` | Defined | Event | E6.29 p3 | `#req_ai <0 \| 1>` |
| `#req_anycode` | Defined | Event | E6.29 p10 | `#req_anycode <event code>` |
| `#req_arenadone` | Defined | Event | E6.29 p11 | `#req_arenadone <0 \| 1>` |
| `#req_capital` | Defined | Event | E6.29 p4 | `#req_capital < 0 \| 1 >` |
| `#req_cave` | Defined | Event | E6.29 p4 | `#req_cave < 0 \| 1 >` |
| `#req_chaos` | Defined | Event | E6.29 p6 | `#req_chaos <value>` |
| `#req_claimedthrone` | Defined | Event | E6.29 p5 | `#req_claimedthrone < 0 \| 1 >` |
| `#req_coast` | Defined | Event | E6.29 p4 | `#req_coast < 0 \| 1 >` |
| `#req_code` | Defined | Event | E6.29 p10; E6.29 p19 | `#req_code <event code>` |
| `#req_cold` | Defined | Event | E6.29 p6 | `#req_cold <value>` |
| `#req_commander` | Defined | Event | E6.29 p6 | `#req_commander < 0 \| 1 >` |
| `#req_crystal` | Defined | Event | E6.29 p5 | `#req_crystal < 0 \| 1 >` |
| `#req_deadmnr` | Defined | Event | E6.29 p7 | `#req_deadmnr "name" \| <number>` |
| `#req_death` | Defined | Event | E6.29 p6 | `#req_death <value>` |
| `#req_deep` | Defined | Event | E6.29 p4 | `#req_deep < 0 \| 1 >` |
| `#req_domchance` | Defined | Event | E6.29 p5 | `#req_domchance <0 - 100>` |
| `#req_dominion` | Defined | Event | E6.29 p5 | `#req_dominion <0 - 10>` |
| `#req_domowner` | Defined | Event | E6.29 p5 | `#req_domowner <nation number>` |
| `#req_drip` | Defined | Event | E6.29 p5 | `#req_drip < 0 \| 1 >` |
| `#req_ench` | Defined | Event | E6.29 p10; E6.29 p20 | `#req_ench <ench nbr>` |
| `#req_enchdom` | Defined | Event | E6.29 p10; E6.29 p20 | `#req_enchdom <ench nbr>` |
| `#req_enchnearby` | Defined | Event | E6.29 p10 | `#req_enchnearby <ench nbr>` |
| `#req_enchtarget` | Defined | Event | E6.29 p10 | `#req_enchtarget <ench nbr>` |
| `#req_era` | Defined | Event | E6.29 p3 | `#req_era <value>` |
| `#req_farm` | Defined | Event | E6.29 p4 | `#req_farm < 0 \| 1 >` |
| `#req_forest` | Defined | Event | E6.29 p4; E6.29 p20 | `#req_forest < 0 \| 1 >` |
| `#req_forestcave` | Defined | Event | E6.29 p4 | `#req_forestcave < 0 \| 1 >` |
| `#req_fornation` | Defined | Event | E6.29 p3 | `#req_fornation <nation number>` |
| `#req_fort` | Defined | Event | E6.29 p4 | `#req_fort < 0 \| 1 >` |
| `#req_fortid` | Defined | Event | E6.29 p4 | `#req_fortid <fort number>` |
| `#req_foundsite` | Defined | Event | E6.29 p5 | `#req_foundsite < 0 \| 1 >` |
| `#req_freesites` | Defined | Event | E6.29 p5 | `#req_freesites <value>` |
| `#req_freshwater` | Defined | Event | E6.29 p5 | `#req_freshwater < 0 \| 1 >` |
| `#req_friendlyench` | Defined | Event | E6.29 p10 | `#req_friendlyench <ench nbr>` |
| `#req_fullowner` | Defined | Event | E6.29 p5 | `#req_fullowner <nation number>` |
| `#req_gem` | Defined | Event | E6.29 p3 | `#req_gem <type>` |
| `#req_godawake` | Defined | Event | E6.29 p6 | `#req_godawake <0 - 1>` |
| `#req_godismnr` | Defined | Event | E6.29 p6 | `#req_godismnr "name" \| <number>` |
| `#req_godisnotmnr` | Defined | Event | E6.29 p6 | `#req_godisnotmnr "name" \| <number>` |
| `#req_gold` | Defined | Event | E6.29 p3 | `#req_gold <type>` |
| `#req_gorge` | Defined | Event | E6.29 p4 | `#req_gorge < 0 \| 1 >` |
| `#req_growth` | Defined | Event | E6.29 p6 | `#req_growth <value>` |
| `#req_heat` | Defined | Event | E6.29 p6 | `#req_heat <value>` |
| `#req_hiddensite` | Defined | Event | E6.29 p5; E6.29 p19 | `#req_hiddensite < 0 \| 1 >` |
| `#req_hostileench` | Defined | Event | E6.29 p10; E6.29 p20 | `#req_hostileench <ench nbr>` |
| `#req_humanoidres` | Defined | Event | E6.29 p7 | `#req_humanoidres` |
| `#req_indepok` | Defined | Event | E6.29 p2; E6.29 p20 | `#req_indepok < 0 \| 1 >` |
| `#req_kelp` | Defined | Event | E6.29 p4 | `#req_kelp < 0 \| 1 >` |
| `#req_lab` | Defined | Event | E6.29 p4 | `#req_lab < 0 \| 1 >` |
| `#req_land` | Defined | Event | E6.29 p4; E6.29 p19 | `#req_land < 0 \| 1 >` |
| `#req_lazy` | Defined | Event | E6.29 p6 | `#req_lazy <value>` |
| `#req_luck` | Defined | Event | E6.29 p6 | `#req_luck <value>` |
| `#req_magic` | Defined | Event | E6.29 p6 | `#req_magic <value>` |
| `#req_maxcorpses` | Defined | Event | E6.29 p5 | `#req_maxcorpses <dead>` |
| `#req_maxdef` | Defined | Event | E6.29 p4 | `#req_maxdef <value>` |
| `#req_maxdominion` | Defined | Event | E6.29 p5 | `#req_maxdominion <-10 - 10>` |
| `#req_maxglobals` | Defined | Event | E6.29 p10 | `#req_maxglobals <nbr>` |
| `#req_maxpop` | Defined | Event | E6.29 p4 | `#req_maxpop <dekapop>` |
| `#req_maxtroops` | Defined | Event | E6.29 p7 | `#req_maxtroops <value>` |
| `#req_maxturn` | Defined | Event | E6.29 p3 | `#req_maxturn <value>` |
| `#req_maxunrest` | Defined | Event | E6.29 p4 | `#req_maxunrest <value>` |
| `#req_mincorpses` | Defined | Event | E6.29 p5 | `#req_mincorpses <dead>` |
| `#req_mindef` | Defined | Event | E6.29 p4 | `#req_mindef <value>` |
| `#req_minglobals` | Defined | Event | E6.29 p10 | `#req_minglobals <nbr>` |
| `#req_minpop` | Defined | Event | E6.29 p4 | `#req_minpop <dekapop>` |
| `#req_minresearch` | Defined | Event | E6.29 p3 | `#req_minresearch <level>` |
| `#req_mintroops` | Defined | Event | E6.29 p7 | `#req_mintroops <value>` |
| `#req_minunrest` | Defined | Event | E6.29 p4 | `#req_minunrest <value>` |
| `#req_mnr` | Defined | Event | E6.29 p6 | `#req_mnr "name" \| <number>` |
| `#req_mnrbs` | Defined | Event | E6.29 p7 | `#req_mnrbs "name" \| <number>` |
| `#req_monster` | Defined | Event | E6.29 p6 | `#req_monster "name" \| <number>` |
| `#req_monsterbs` | Defined | Event | E6.29 p7 | `#req_monsterbs "name" \| <number>` |
| `#req_month` | Defined | Event | E6.29 p3 | `#req_month <0 - 11>` |
| `#req_mountain` | Defined | Event | E6.29 p4; E6.29 p19; E6.29 p20 | `#req_mountain < 0 \| 1 >` |
| `#req_mydominion` | Defined | Event | E6.29 p5 | `#req_mydominion < 0 \| 1 >` |
| `#req_myench` | Defined | Event | E6.29 p10; E6.29 p20 | `#req_myench <ench nbr>` |
| `#req_nation` | Defined | Event | E6.29 p3 | `#req_nation <nation number>` |
| `#req_nativesoil` | Defined | Event | E6.29 p5 | `#req_nativesoil` |
| `#req_nearbycapital` | Defined | Event | E6.29 p4 | `#req_nearbycapital < 0 \| 1 >` |
| `#req_nearbycode` | Defined | Event | E6.29 p10 | `#req_nearbycode <event code>` |
| `#req_nearbysite` | Defined | Event | E6.29 p5 | `#req_nearbysite < 0 \| 1 >` |
| `#req_nearbythrone` | Defined | Event | E6.29 p5 | `#req_nearbythrone < 0 \| 1 >` |
| `#req_nearowncode` | Defined | Event | E6.29 p10 | `#req_nearowncode <event code>` |
| `#req_noench` | Defined | Event | E6.29 p10 | `#req_noench <ench nbr>` |
| `#req_noera` | Defined | Event | E6.29 p3 | `#req_noera <value>` |
| `#req_nomnr` | Defined | Event | E6.29 p6 | `#req_nomnr "name" \| <number>` |
| `#req_nomonster` | Defined | Event | E6.29 p6 | `#req_nomonster "name" \| <number>` |
| `#req_nonation` | Defined | Event | E6.29 p3 | `#req_nonation <nation number>` |
| `#req_nopathair` | Defined | Event | E6.29 p7 | `#req_nopathair <level>` |
| `#req_nopathall` | Defined | Event | E6.29 p8 | `#req_nopathall <level>` |
| `#req_nopathastral` | Defined | Event | E6.29 p7 | `#req_nopathastral <level>` |
| `#req_nopathblood` | Defined | Event | E6.29 p8 | `#req_nopathblood <level>` |
| `#req_nopathdeath` | Defined | Event | E6.29 p7 | `#req_nopathdeath <level>` |
| `#req_nopathearth` | Defined | Event | E6.29 p7 | `#req_nopathearth <level>` |
| `#req_nopathfire` | Defined | Event | E6.29 p7 | `#req_nopathfire <level>` |
| `#req_nopathglamour` | Defined | Event | E6.29 p8 | `#req_nopathglamour <level>` |
| `#req_nopathholy` | Defined | Event | E6.29 p8 | `#req_nopathholy <level>` |
| `#req_nopathnature` | Defined | Event | E6.29 p8 | `#req_nopathnature <level>` |
| `#req_nopathwater` | Defined | Event | E6.29 p7 | `#req_nopathwater <level>` |
| `#req_norealmnr` | Defined | Event | E6.29 p7 | `#req_norealmnr "name" \| <number>` |
| `#req_noseason` | Defined | Event | E6.29 p3 | `#req_noseason <0 - 4>` |
| `#req_nositenbr` | Defined | Event | E6.29 p5 | `#req_nositenbr <site number>` |
| `#req_notanycode` | Defined | Event | E6.29 p10 | `#req_notanycode <event code>` |
| `#req_notcode` | Defined | Event | E6.29 p10 | `#req_notcode <event code>` |
| `#req_notforally` | Defined | Event | E6.29 p3 | `#req_notforally <nation number>` |
| `#req_notfornation` | Defined | Event | E6.29 p3 | `#req_notfornation <nation number>` |
| `#req_notpoptype` | Defined | Event | E6.29 p4 | `#req_notpoptype <value>` |
| `#req_noworlditem` | Defined | Event | E6.29 p11 | `#req_noworlditem "item name" \| <item number>` |
| `#req_order` | Defined | Event | E6.29 p6 | `#req_order <value>` |
| `#req_owncapital` | Defined | Event | E6.29 p4 | `#req_owncapital < 0 \| 1 >` |
| `#req_path` | Defined | Event | E6.29 p3 | `#req_path <type>` |
| `#req_pathair` | Defined | Event | E6.29 p7 | `#req_pathair <level>` |
| `#req_pathastral` | Defined | Event | E6.29 p7 | `#req_pathastral <level>` |
| `#req_pathblood` | Defined | Event | E6.29 p7 | `#req_pathblood <level>` |
| `#req_pathdeath` | Defined | Event | E6.29 p7 | `#req_pathdeath <level>` |
| `#req_pathearth` | Defined | Event | E6.29 p7 | `#req_pathearth <level>` |
| `#req_pathfire` | Defined | Event | E6.29 p7 | `#req_pathfire <level>` |
| `#req_pathgems` | Defined | Event | E6.29 p3 | `#req_pathgems <amount>` |
| `#req_pathglamour` | Defined | Event | E6.29 p7 | `#req_pathglamour <level>` |
| `#req_pathholy` | Defined | Event | E6.29 p7 | `#req_pathholy <level>` |
| `#req_pathnature` | Defined | Event | E6.29 p7 | `#req_pathnature <level>` |
| `#req_pathwater` | Defined | Event | E6.29 p7 | `#req_pathwater <level>` |
| `#req_permonth` | Defined | Event | E6.29 p10; E6.29 p20 | `#req_permonth <nbr>` |
| `#req_plane` | Defined | Event | E6.29 p4 | `#req_plane < planenr >` |
| `#req_pop0ok` | Defined | Event | E6.29 p4 | `#req_pop0ok` |
| `#req_poptype` | Defined | Event | E6.29 p4 | `#req_poptype <value>` |
| `#req_preach` | Defined | Event | E6.29 p7 | `#req_preach <value>` |
| `#req_pregame` | Defined | Event | E6.29 p3 | `#req_pregame <value>` |
| `#req_pretawake` | Defined | Event | E6.29 p6 | `#req_pretawake <0 - 1>` |
| `#req_pretismnr` | Defined | Event | E6.29 p6 | `#req_pretismnr "name" \| <number>` |
| `#req_prod` | Defined | Event | E6.29 p6 | `#req_prod <value>` |
| `#req_rare` | Defined | Event | E6.29 p2; E6.29 p20 | `#req_rare <percent>` |
| `#req_realmnr` | Defined | Event | E6.29 p7 | `#req_realmnr "name" \| <number>` |
| `#req_researcher` | Defined | Event | E6.29 p7 | `#req_researcher` |
| `#req_school` | Defined | Event | E6.29 p3 | `#req_school <school>` |
| `#req_season` | Defined | Event | E6.29 p3 | `#req_season <0 - 4>` |
| `#req_site` | Defined | Event | E6.29 p5; E6.29 p19 | `#req_site < 0 \| 1 >` |
| `#req_story` | Defined | Event | E6.29 p2 | `#req_story < 0 \| 1 >` |
| `#req_swamp` | Defined | Event | E6.29 p4 | `#req_swamp < 0 \| 1 >` |
| `#req_targaff` | Defined | Event | E6.29 p9 | `#req_targaff <affliction number>` |
| `#req_targally` | Defined | Event | E6.29 p9 | `#req_targally <nation number>` |
| `#req_targanimal` | Defined | Event | E6.29 p9 | `#req_targanimal <0 \| 1>` |
| `#req_targdemon` | Defined | Event | E6.29 p9 | `#req_targdemon <0 \| 1>` |
| `#req_targforeignok` | Defined | Event | E6.29 p9 | `#req_targforeignok` |
| `#req_targgod` | Defined | Event | E6.29 p8 | `#req_targgod < 0 - 2 >` |
| `#req_targhorrormark` | Defined | Event | E6.29 p9 | `#req_targhorrormark <value>` |
| `#req_targhumanoid` | Defined | Event | E6.29 p8; E6.29 p19 | `#req_targhumanoid < 0 \| 1 >` |
| `#req_targimmobile` | Defined | Event | E6.29 p9 | `#req_targimmobile <0 \| 1>` |
| `#req_targinanimate` | Defined | Event | E6.29 p9 | `#req_targinanimate <0 \| 1>` |
| `#req_targinsane` | Defined | Event | E6.29 p9 | `#req_targinsane <0 \| 1>` |
| `#req_targitem` | Defined | Event | E6.29 p9 | `#req_targitem "item name" \| <item number>` |
| `#req_targmagicbeing` | Defined | Event | E6.29 p9 | `#req_targmagicbeing <0 \| 1>` |
| `#req_targmale` | Defined | Event | E6.29 p8 | `#req_targmale < 0 \| 1 >` |
| `#req_targmanygems` | Defined | Event | E6.29 p8 | `#req_targmanygems <path number>` |
| `#req_targmaxkills` | Defined | Event | E6.29 p10 | `#req_targmaxkills <value>` |
| `#req_targmaxmorale` | Defined | Event | E6.29 p9 | `#req_targmaxmorale <morale>` |
| `#req_targmaxsize` | Defined | Event | E6.29 p9 | `#req_targmaxsize <size>` |
| `#req_targmindless` | Defined | Event | E6.29 p9 | `#req_targmindless <0 \| 1>` |
| `#req_targminkills` | Defined | Event | E6.29 p9 | `#req_targminkills <value>` |
| `#req_targminmorale` | Defined | Event | E6.29 p9 | `#req_targminmorale <morale>` |
| `#req_targminsize` | Defined | Event | E6.29 p9 | `#req_targminsize <size>` |
| `#req_targmnr` | Defined | Event | E6.29 p8 | `#req_targmnr "name" \| <number>` |
| `#req_targnoaff` | Defined | Event | E6.29 p9 | `#req_targnoaff <affliction number>` |
| `#req_targnoitem` | Defined | Event | E6.29 p9 | `#req_targnoitem "item name" \| <item number>` |
| `#req_targnomnr` | Defined | Event | E6.29 p8 | `#req_targnomnr "name" \| <number>` |
| `#req_targnoorder` | Defined | Event | E6.29 p9 | `#req_targnoorder <order>` |
| `#req_targnopath1` | Defined | Event | E6.29 p8 | `#req_targnopath1 <path number>` |
| `#req_targnopath2` | Defined | Event | E6.29 p8 | `#req_targnopath2 <path number>` |
| `#req_targnopath3` | Defined | Event | E6.29 p8 | `#req_targnopath3 <path number>` |
| `#req_targnopath4` | Defined | Event | E6.29 p8 | `#req_targnopath4 <path number>` |
| `#req_targnorealmnr` | Defined | Event | E6.29 p8 | `#req_targnorealmnr "name" \| <number>` |
| `#req_targnotally` | Defined | Event | E6.29 p9 | `#req_targnotally <nation number>` |
| `#req_targnotowner` | Defined | Event | E6.29 p9 | `#req_targnotowner <nation number>` |
| `#req_targorder` | Defined | Event | E6.29 p9; E6.29 p19 | `#req_targorder <order number>` |
| `#req_targowner` | Defined | Event | E6.29 p9 | `#req_targowner <nation number>` |
| `#req_targpath1` | Defined | Event | E6.29 p8 | `#req_targpath1 <path number>` |
| `#req_targpath2` | Defined | Event | E6.29 p8; E6.29 p19 | `#req_targpath2 <path number>` |
| `#req_targpath3` | Defined | Event | E6.29 p8; E6.29 p19 | `#req_targpath3 <path number>` |
| `#req_targpath4` | Defined | Event | E6.29 p8 | `#req_targpath4 <path number>` |
| `#req_targprophet` | Defined | Event | E6.29 p8 | `#req_targprophet < 0 \| 1 >` |
| `#req_targrealmnr` | Defined | Event | E6.29 p8 | `#req_targrealmnr "name" \| <number>` |
| `#req_targseductions` | Defined | Event | E6.29 p9 | `#req_targseductions <value>` |
| `#req_targsight` | Defined | Event | E6.29 p8 | `#req_targsight < 0 \| 1 >` |
| `#req_targundead` | Defined | Event | E6.29 p9 | `#req_targundead <0 \| 1>` |
| `#req_temple` | Defined | Event | E6.29 p4 | `#req_temple < 0 \| 1 >` |
| `#req_thronesite` | Defined | Event | E6.29 p5 | `#req_thronesite < 0 \| 1 >` |
| `#req_turn` | Defined | Event | E6.29 p3 | `#req_turn <value>` |
| `#req_turnrare` | Defined | Event | E6.29 p2 | `#req_turnrare <value>` |
| `#req_unclaimedthrone` | Defined | Event | E6.29 p5 | `#req_unclaimedthrone < 0 \| 1 >` |
| `#req_unique` | Defined | Event | E6.29 p2; E6.29 p19 | `#req_unique <value>` |
| `#req_unluck` | Defined | Event | E6.29 p6 | `#req_unluck <value>` |
| `#req_unmagic` | Defined | Event | E6.29 p6 | `#req_unmagic <value>` |
| `#req_varneg` | Defined | Event | E6.29 p10 | `#req_varneg <event var>` |
| `#req_varone` | Defined | Event | E6.29 p10 | `#req_varone <event var>` |
| `#req_varpos` | Defined | Event | E6.29 p10 | `#req_varpos <event var>` |
| `#req_varzero` | Defined | Event | E6.29 p10 | `#req_varzero <event var>` |
| `#req_void` | Defined | Event | E6.29 p5 | `#req_void < 0 \| 1 >` |
| `#req_voidok` | Defined | Event | E6.29 p4; E6.29 p5 | `#req_voidok < 0 \| 1 >` |
| `#req_waste` | Defined | Event | E6.29 p4 | `#req_waste < 0 \| 1 >` |
| `#req_worlditem` | Defined | Event | E6.29 p11 | `#req_worlditem "item name" \| <item number>` |
| `#reqeyes` | Defined | Item | M6.34 p57 | `#reqeyes` |
| `#reqlab` | Defined | Monster | M6.34 p15 | `#reqlab` |
| `#reqnoplant` | Defined | Spell | M6.34 p55 | `#reqnoplant` |
| `#reqnoseduce` | Defined | Spell | M6.34 p55 | `#reqnoseduce` |
| `#reqnospellsinger` | Defined | Spell | M6.34 p55 | `#reqnospellsinger` |
| `#reqnotaskmaster` | Defined | Spell | M6.34 p55 | `#reqnotaskmaster` |
| `#reqplant` | Defined | Spell | M6.34 p55 | `#reqplant` |
| `#reqseduce` | Defined | Spell | M6.34 p55 | `#reqseduce` |
| `#reqspellsinger` | Defined | Spell | M6.34 p55 | `#reqspellsinger` |
| `#reqsun` | Defined | Spell | M6.34 p54 | `#reqsun <0 - 1>` |
| `#reqtaskmaster` | Defined | Spell | M6.34 p55 | `#reqtaskmaster` |
| `#reqtemple` | Defined | Monster | M6.34 p15 | `#reqtemple` |
| `#res` | Defined | Site | M6.34 p38 | `#res <amount>` |
| `#researchaff` | Defined | Event | E6.29 p15 | `#researchaff <affliction bitmask>` |
| `#researchbonus` | Defined | Monster | M6.34 p34; M6.34 p60 | `#researchbonus <value>` |
| `#researchgoal` | Defined | AI | M6.34 p64 | `#researchgoal "spell name" \| "item name"` |
| `#researchlevel` | Defined | Event, Spell | M6.34 p50; E6.29 p20 | `#researchlevel <level>` |
| `#researchscale` | Defined | General | M6.34 p61 | `#researchscale <bonus>` |
| `#resetcode` | Defined | Event | E6.29 p17 | `#resetcode <event code>` |
| `#resetcodedelay` | Defined | Event | E6.29 p18 | `#resetcodedelay <event code>` |
| `#resetcodedelay2` | Defined | Event | E6.29 p18 | `#resetcodedelay2 <event code>` |
| `#resolvearena1` | Defined | Event | E6.29 p18 | `#resolvearena1` |
| `#resolvearena2` | Defined | Event | E6.29 p18 | `#resolvearena2` |
| `#resourcemult` | Defined | General | M6.34 p61 | `#resourcemult <percent>` |
| `#resources` | Defined | Monster | M6.34 p26 | `#resources <value>` |
| `#ressize` | Defined | Monster | M6.34 p16 | `#ressize <size>` |
| `#restricted` | Defined | Item, Spell | M6.34 p53; M6.34 p57 | `#restricted <nation nbr> \| "nation name"` |
| `#restricteditem` | Defined | Item | M6.34 p57 | `#restricteditem <value>` |
| `#revealprov` | Defined | Event | E6.29 p13 | `#revealprov` |
| `#revealsite` | Defined | Event | E6.29 p13; E6.29 p19 | `#revealsite` |
| `#revolt` | Defined | Event | E6.29 p13 | `#revolt` |
| `#riverstart` | Defined | Site | M6.34 p43 | `#riverstart` |
| `#rockcol` | Defined | Map | P6.26 p8 | `#rockcol <red> <green> <blue>` |
| `#rpcost` | Defined | Monster | M6.34 p15 | `#rpcost <recruitment points>` |
| `#run` | Defined | Item | M6.34 p57 | `#run` |

### S

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#sabbathmaster` | Reference | Monster | M6.34 p60 | `#sabbathmaster` |
| `#sabbathslave` | Defined | Monster | M6.34 p35; M6.34 p60 | `#sabbathslave` |
| `#sacredonly` | Defined | Weapon | M6.34 p9 | `#sacredonly` |
| `#sacrificedom` | Defined | Nation | M6.34 p49 | `#sacrificedom` |
| `#saildist` | Defined | Map | P6.26 p4 | `#saildist <1-10>` |
| `#sailing` | Defined | Monster | M6.34 p20 | `#sailing <ship size> <max unit size>` |
| `#sample` | Defined | Sound, Weapon | M6.34 p5; M6.34 p7; M6.34 p52 | `#sample "<filename>"` |
| `#scale` | Defined | AI, Map | P6.26 p9; M6.34 p64 | `#scale chaos <nation nbr> <(-5)-5>` |
| `#scalewalls` | Defined | Monster | M6.34 p20; M6.34 p59 | `#scalewalls` |
| `#school` | Defined | Event, Spell | M6.34 p50; E6.29 p20 | `#school <school nbr>` |
| `#scry` | Defined | Site | M6.34 p39 | `#scry <duration>` |
| `#scryrange` | Defined | Site | M6.34 p39 | `#scryrange <range>` |
| `#seatrace` | Defined | Nation | M6.34 p49 | `#seatrace` |
| `#secondarycolor` | Defined | General, Nation | M6.34 p43; M6.34 p64 | `#secondarycolor <red> <green> <blue>` |
| `#secondaryeffect` | Defined | Weapon | M6.34 p10 | `#secondaryeffect "<weapon name>" \| <weapon nbr>` |
| `#secondaryeffectalways` | Defined | Weapon | M6.34 p10 | `#secondaryeffectalways "<weapon name>" \| <weapon nbr>` |
| `#secondarylevel` | Defined | Item | M6.34 p55 | `#secondarylevel <path>` |
| `#secondarypath` | Defined | Item | M6.34 p55 | `#secondarypath <path>` |
| `#secondshape` | Defined | Monster | M6.34 p27 | `#secondshape "<monster name>" \| <monster nbr>` |
| `#secondtmpshape` | Defined | Monster | M6.34 p28 | `#secondtmpshape "<monster name>" \| <monster nbr>` |
| `#seduce` | Defined | Monster | M6.34 p20; M6.34 p58 | `#seduce <value>` |
| `#selectarmor` | Defined | Armour | M6.34 p12 | `#selectarmor "<armor name>" \| <nbr>` |
| `#selectbless` | Defined | Bless | M6.34 p36 | `#selectbless "<bless name>" \| <nbr>` |
| `#selectevent` | Defined | Event | E6.29 p2 | `#selectevent <event nbr>` |
| `#selectitem` | Defined | Item | M6.34 p55 | `#selectitem "<item name>" \| <item nbr>` |
| `#selectmonster` | Defined | Monster | M6.34 p13 | `#selectmonster "<monster name>" \| <monster nbr>` |
| `#selectnametype` | Defined | Names | M6.34 p36 | `#selectnametype <nametype nbr>` |
| `#selectnation` | Defined | Nation | M6.34 p41 | `#selectnation <nation nbr>` |
| `#selectpoptype` | Defined | Poptype | M6.34 p62 | `#selectpoptype <poptype>` |
| `#selectsite` | Defined | Site | M6.34 p37 | `#selectsite "<site name>" \| <site nbr>` |
| `#selectsound` | Defined | Sound | M6.34 p5 | `#selectsound <nbr>` |
| `#selectspell` | Defined | Spell | M6.34 p50 | `#selectspell "<spell name>" \| <nbr>` |
| `#selectweapon` | Defined | Weapon | M6.34 p6 | `#selectweapon "<weapon name>" \| <weapon nbr>` |
| `#sethome` | Defined | Spell | M6.34 p54 | `#sethome` |
| `#setland` | Defined | Map | P6.26 p6; P6.26 p3 | `#setland <province nbr>` |
| `#setpoptype` | Defined | Event | E6.29 p13 | `#setpoptype <value>` |
| `#setxp` | Defined | Event | E6.29 p16 | `#setxp <experience points>` |
| `#shapechance` | Defined | Monster | M6.34 p28 | `#shapechance <percent>` |
| `#shapechange` | Defined | Monster | M6.34 p27 | `#shapechange "<monster name>" \| <monster nbr>` |
| `#shatteredsoul` | Defined | Monster | M6.34 p27; M6.34 p60 | `#shatteredsoul <percent>` |
| `#shock` | Defined | Weapon | M6.34 p9 | `#shock` |
| `#shockifhit` | Defined | Weapon | M6.34 p12 | `#shockifhit <dmg>` |
| `#shockres` | Defined | Item, Monster | M6.34 p22; M6.34 p56 | `#shockres <prot>` |
| `#shrinkhp` | Defined | Monster | M6.34 p28 | `#shrinkhp <hit points>` |
| `#siegebonus` | Defined | Monster | M6.34 p26; M6.34 p60 | `#siegebonus <value>` |
| `#singlebattle` | Defined | Monster | M6.34 p15; M6.34 p58 | `#singlebattle` |
| `#size` | Defined | Monster | M6.34 p17 | `#size <size>` |
| `#sizecost` | Defined | Spell | M6.34 p54 | `#sizecost <value>` |
| `#sizeresist` | Defined | Weapon | M6.34 p9 | `#sizeresist` |
| `#skilledrider` | Defined | Monster | M6.34 p31 | `#skilledrider <value>` |
| `#skip` | Defined | Weapon | M6.34 p10 | `#skip` |
| `#skip2` | Defined | Weapon | M6.34 p10 | `#skip2` |
| `#skirmisher` | Reference | Monster | M6.34 p36; M6.34 p60 | `#skirmisher` |
| `#skybox` | Defined | Map | P6.26 p8 | `#skybox "<pic.tga>` |
| `#slash` | Defined | Weapon | M6.34 p9 | `#slash` |
| `#slashres` | Defined | Monster | M6.34 p23; M6.34 p59 | `#slashres` |
| `#slave` | Defined | Monster | M6.34 p32 | `#slave` |
| `#slaver` | Defined | Monster | M6.34 p30 | `#slaver "<monster name>" \| <monster nbr>` |
| `#slaverbonus` | Defined | Monster | M6.34 p30 | `#slaverbonus <modifier>` |
| `#sleepaura` | Defined | Monster | M6.34 p24 | `#sleepaura <area>` |
| `#sleepres` | Defined | Monster | M6.34 p26; M6.34 p60 | `#sleepres <bonus>` |
| `#slimer` | Defined | Monster | M6.34 p24; M6.34 p59 | `#slimer <strength>` |
| `#slothincome` | Defined | General | M6.34 p61 | `#slothincome <percent>` |
| `#slothpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#slothpower <bonus>` |
| `#slothresearch` | Defined | Monster | M6.34 p34; M6.34 p60 | `#slothresearch <value>` |
| `#slothresources` | Defined | General | M6.34 p61 | `#slothresources <percent>` |
| `#slothscale` | Defined | Bless | M6.34 p37 | `#slothscale <value>` |
| `#slowrec` | Defined | Monster | M6.34 p14 | `#slowrec` |
| `#smartmount` | Defined | Monster | M6.34 p31 | `#smartmount <smartness>` |
| `#smpmode` | Defined | Sound | M6.34 p5 | `#smpmode <mode>` |
| `#snake` | Defined | Monster | M6.34 p18 | `#snake` |
| `#snaketattoo` | Defined | Monster | M6.34 p26 | `#snaketattoo <value>` |
| `#sneakunit` | Defined | Item | M6.34 p57 | `#sneakunit <value>` |
| `#snow` | Defined | Monster | M6.34 p19 | `#snow` |
| `#sorcerygems` | Defined | Monster | M6.34 p34; M6.34 p60 | `#sorcerygems <gems>` |
| `#sorceryrange` | Defined | Monster, Site | M6.34 p34; M6.34 p39; M6.34 p60 | `#sorceryrange <range>` |
| `#sound` | Defined | Sound, Weapon | M6.34 p7; M6.34 p52 | `#sound <sample nbr>` |
| `#spec` | Defined | Spell | M6.34 p53 | `#spec <spec bitmask>` |
| `#speciallook` | Defined | Monster | M6.34 p13 | `#speciallook <value>` |
| `#specstart` | Defined | Map | P6.26 p6 | `#specstart <nation nbr> <land nbr>` |
| `#speedmult` | Defined | Sound, Weapon | M6.34 p11; M6.34 p52 | `#speedmult <1 - 3>` |
| `#spell` | Defined | Spell | M6.34 p56 | `#spell "<spell name>"` |
| `#spellreqfly` | Defined | Spell | M6.34 p53 | `#spellreqfly <0 - 1>` |
| `#spellsinger` | Defined | Monster | M6.34 p35; M6.34 p60 | `#spellsinger` |
| `#spikes` | Defined | Monster | M6.34 p24; M6.34 p59 | `#spikes <dmg>` |
| `#spiritform` | Defined | Monster | M6.34 p19 | `#spiritform` |
| `#spiritformimmune` | Defined | Weapon | M6.34 p10 | `#spiritformimmune` |
| `#spiritsight` | Defined | Monster | M6.34 p25; M6.34 p59 | `#spiritsight` |
| `#spr` | Defined | Item | M6.34 p55 | `#spr "<filename>"` |
| `#spr1` | Defined | Monster | M6.34 p13 | `#spr1 "<imgfile>"` |
| `#spr2` | Defined | Monster | M6.34 p13 | `#spr2 "<imgfile>"` |
| `#spreaddom` | Defined | Monster | M6.34 p26; M6.34 p60 | `#spreaddom <candles>` |
| `#springimmortal` | Defined | Monster | M6.34 p23 | `#springimmortal` |
| `#springpower` | Defined | Monster | M6.34 p24; M6.34 p59 | `#springpower <percent>` |
| `#springshape` | Defined | Monster | M6.34 p28 | `#springshape "<monster name>" \| <monster nbr>` |
| `#spy` | Defined | Monster | M6.34 p20 | `#spy` |
| `#standard` | Defined | Monster | M6.34 p32; M6.34 p60 | `#standard <bonus>` |
| `#start` | Defined | Map | P6.26 p6 | `#start <province nbr>` |
| `#startaff` | Defined | Monster | M6.34 p22 | `#startaff <percent>` |
| `#startage` | Defined | Monster | M6.34 p21 | `#startage <age>` |
| `#startcom` | Defined | Nation | M6.34 p45 | `#startcom "<monster name>" \| <monster nbr>` |
| `#startdom` | Defined | Monster, Nation | M6.34 p14 | `#startdom <dominion strength>` |
| `#startheroab` | Defined | Monster | M6.34 p22 | `#startheroab <percent>` |
| `#startingaff` | Defined | Monster | M6.34 p22 | `#startingaff <affliction bitmask>` |
| `#startitem` | Defined | Monster | M6.34 p18 | `#startitem "item name" \| <item nbr>` |
| `#startmajoraff` | Defined | Monster | M6.34 p22 | `#startmajoraff <percent>` |
| `#startresearch` | Defined | General | M6.34 p62 | `#startresearch <RP>` |
| `#startscout` | Defined | Nation | M6.34 p45 | `#startscout "<monster name>" \| <monster nbr>` |
| `#startsite` | Defined | Site | M6.34 p43 | `#startsite "<site name>"` |
| `#startunitnbrs1` | Defined | Nation | M6.34 p45 | `#startunitnbrs1 <nbr of units>` |
| `#startunitnbrs2` | Defined | Nation | M6.34 p45 | `#startunitnbrs2 <nbr of units>` |
| `#startunittype1` | Defined | Nation | M6.34 p45 | `#startunittype1 "<monster name>" \| <monster nbr>` |
| `#startunittype2` | Defined | Nation | M6.34 p45 | `#startunittype2 "<monster name>" \| <monster nbr>` |
| `#statbreak` | Defined | Monster | M6.34 p20; M6.34 p58 | `#statbreak <value>` |
| `#statstorm` | Defined | Monster | M6.34 p20; M6.34 p58 | `#statstorm <value>` |
| `#stealthboost` | Defined | Item | M6.34 p57 | `#stealthboost <value>` |
| `#stealthcom` | Defined | Event | E6.29 p14 | `#stealthcom "name" \| <number>` |
| `#stealthy` | Defined | Monster | M6.34 p20 | `#stealthy <value>` |
| `#stonebeing` | Defined | Monster | M6.34 p19; M6.34 p58 | `#stonebeing` |
| `#stoneskin` | Defined | Item | M6.34 p56 | `#stoneskin` |
| `#stormimmune` | Defined | Item, Monster | M6.34 p19; M6.34 p57 | `#stormimmune` |
| `#stormpower` | Defined | Monster | M6.34 p25; M6.34 p59 | `#stormpower <bonus>` |
| `#str` | Defined | Item, Monster | M6.34 p16; M6.34 p56 | `#str <strength>` |
| `#strikesound` | Defined | Sound | M6.34 p52 | `#strikesound <sample nbr>` |
| `#strikeunits` | Defined | Event | E6.29 p15 | `#strikeunits <damage>` |
| `#succubus` | Defined | Monster | M6.34 p20; M6.34 p58 | `#succubus <value>` |
| `#sumhealaffs` | Defined | Spell | M6.34 p54 | `#sumhealaffs <value>` |
| `#summary` | Defined | Nation | M6.34 p42 | `#summary "<nation name>"` |
| `#summerpower` | Defined | Monster | M6.34 p24; M6.34 p59 | `#summerpower <percent>` |
| `#summershape` | Defined | Monster | M6.34 p28 | `#summershape "<monster name>" \| <monster nbr>` |
| `#summon` | Defined | Monster | M6.34 p38 | `#summon "<monster name>" \| <monster nbr>` |
| `#summon1` | Reference | Monster | M6.34 p61 | `#summon1` |
| `#summon1...5` | Defined; template | Monster | M6.34 p29 | `#summon1...5 "<monster name>" \| <monster nbr>` |
| `#summon2` | Reference | Monster | M6.34 p61 | `#summon2` |
| `#summon3` | Reference | Monster | M6.34 p61 | `#summon3` |
| `#summon4` | Reference | Monster | M6.34 p61 | `#summon4` |
| `#summon5` | Reference | Monster | M6.34 p61 | `#summon5` |
| `#summonlvl2` | Defined | Monster | M6.34 p38 | `#summonlvl2 "<monster name>" \| <monster nbr>` |
| `#summonlvl3` | Defined | Monster | M6.34 p38 | `#summonlvl3 "<monster name>" \| <monster nbr>` |
| `#summonlvl4` | Defined | Monster | M6.34 p38 | `#summonlvl4 "<monster name>" \| <monster nbr>` |
| `#sunawe` | Defined | Monster | M6.34 p24; M6.34 p59 | `#sunawe <bonus>` |
| `#supayareanim` | Defined | Nation | M6.34 p50 | `#supayareanim` |
| `#superiorleader` | Defined | Monster | M6.34 p31 | `#superiorleader` |
| `#superiormagicleader` | Defined | Monster | M6.34 p32 | `#superiormagicleader` |
| `#superiorundeadleader` | Defined | Monster | M6.34 p32 | `#superiorundeadleader` |
| `#supply` | Defined | Site | M6.34 p38 | `#supply <value>` |
| `#supplybonus` | Defined | Monster | M6.34 p26; M6.34 p60 | `#supplybonus <value>` |
| `#supplymult` | Defined | General | M6.34 p61 | `#supplymult <percent>` |
| `#swamplabcost` | Defined | Nation | M6.34 p48 | `#swamplabcost <price>` |
| `#swampsurvival` | Defined | Monster | M6.34 p20 | `#swampsurvival` |
| `#swamptemplecost` | Defined | Nation | M6.34 p48 | `#swamptemplecost <price>` |
| `#swift` | Defined | Item | M6.34 p57 | `#swift <percent>` |
| `#swimming` | Defined | Monster | M6.34 p19 | `#swimming` |
| `#syncretism` | Defined | Nation | M6.34 p49 | `#syncretism <0 or 1>` |

### T

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `##targhis##` | Reference; message | Event | E6.29 p11 | `##targhis##` |
| `##targname##` | Reference; message | Event | E6.29 p11 | `##targname##` |
| `#tainted` | Defined | Item, Monster | M6.34 p35; M6.34 p57 | `#tainted <chance>` |
| `#taskmaster` | Defined | Monster | M6.34 p32; M6.34 p60 | `#taskmaster <bonus>` |
| `#taxboost` | Defined | Event | E6.29 p13 | `#taxboost <percent>` |
| `#taxcollector` | Defined | Monster | M6.34 p27; M6.34 p60 | `#taxcollector` |
| `#teamstart` | Defined | Map | P6.26 p6 | `#teamstart <land nbr> <team nbr>` |
| `#teleport` | Defined | Monster | M6.34 p20 | `#teleport` |
| `#temple` | Defined | Event, Map, Site | E6.29 p13; P6.26 p8; M6.34 p40 | `#temple < 0 \| 1 >` |
| `#templecost` | Defined | Nation | M6.34 p48 | `#templecost <price>` |
| `#templegems` | Defined | Nation | M6.34 p48 | `#templegems <type>` |
| `#templeholypoints` | Defined | Nation | M6.34 p49 | `#templeholypoints <value>` |
| `#templepic` | Defined | Nation | M6.34 p48 | `#templepic <pic nbr>` |
| `#templetrainer` | Defined | Monster | M6.34 p29; M6.34 p61 | `#templetrainer "<monster name>" \| <monster nbr>` |
| `#tempscalecap` | Defined | General | M6.34 p61 | `#tempscalecap <value>` |
| `#tempunits` | Defined | Event | E6.29 p14 | `#tempunits < 0 \| 1>` |
| `#terrain` | Defined | Map | P6.26 p4; P6.26 p3 | `#terrain <province nbr> <terrain mask>` |
| `#thaucost` | Defined | Site | M6.34 p39 | `#thaucost <bonus>` |
| `#thirdstr` | Defined | Weapon | M6.34 p9 | `#thirdstr` |
| `#thronekill` | Defined | Monster | M6.34 p27; M6.34 p60 | `#thronekill <chance>` |
| `#tmpairgems` | Defined | Monster | M6.34 p34; M6.34 p60 | `#tmpairgems <gems>` |
| `#tmpastralgems` | Defined | Monster | M6.34 p34; M6.34 p61 | `#tmpastralgems <gems>` |
| `#tmpbloodslaves` | Defined | Monster | M6.34 p34; M6.34 p61 | `#tmpbloodslaves <slaves>` |
| `#tmpdeathgems` | Defined | Monster | M6.34 p34; M6.34 p61 | `#tmpdeathgems <gems>` |
| `#tmpearthgems` | Defined | Monster | M6.34 p34; M6.34 p61 | `#tmpearthgems <gems>` |
| `#tmpfiregems` | Defined | Monster | M6.34 p34; M6.34 p60 | `#tmpfiregems <gems>` |
| `#tmpglamourgems` | Defined | Monster | M6.34 p34; M6.34 p61 | `#tmpglamourgems <gems>` |
| `#tmpnaturegems` | Defined | Monster | M6.34 p34; M6.34 p61 | `#tmpnaturegems <gems>` |
| `#tmpwatergems` | Defined | Monster | M6.34 p34; M6.34 p60 | `#tmpwatergems <gems>` |
| `#togglevar` | Defined | Event | E6.29 p18 | `#togglevar <event var>` |
| `#tolerateund` | Defined | Monster | M6.34 p33 | `#tolerateund` |
| `#tombwyrmreanim` | Defined | Nation | M6.34 p50 | `#tombwyrmreanim` |
| `#tradecoast` | Defined | Nation | M6.34 p49 | `#tradecoast <income boost in percent>` |
| `#trample` | Defined | Monster | M6.34 p25; M6.34 p59 | `#trample` |
| `#trampswallow` | Defined | Monster | M6.34 p25; M6.34 p59 | `#trampswallow` |
| `#transform` | Defined | Event | E6.29 p15 | `#transform "name" \| <number>` |
| `#transformation` | Defined | Monster | M6.34 p28 | `#transformation <value>` |
| `#triple3mon` | Defined | Monster | M6.34 p14 | `#triple3mon` |
| `#triplegod` | Defined | Monster | M6.34 p14 | `#triplegod <type>` |
| `#triplegodmag` | Defined | Monster | M6.34 p14 | `#triplegodmag <penalty>` |
| `#troglodyte` | Defined | Monster | M6.34 p18 | `#troglodyte` |
| `#truesight` | Defined | Monster | M6.34 p25; M6.34 p59 | `#truesight` |
| `#turmoilevents` | Defined | General | M6.34 p61 | `#turmoilevents <percent>` |
| `#turmoilincome` | Defined | General | M6.34 p61 | `#turmoilincome <percent>` |
| `#twiceborn` | Defined | Monster | M6.34 p28 | `#twiceborn "<monster name>" \| <monster nbr>` |
| `#twiceborncost` | Defined | Spell | M6.34 p54 | `#twiceborncost <value>` |
| `#twistfate` | Defined | Monster | M6.34 p23; M6.34 p59 | `#twistfate` |
| `#twohanded` | Defined | Weapon | M6.34 p7 | `#twohanded` |
| `#type` | Defined | Armour, Item | M6.34 p12; M6.34 p55 | `#type <type>` |

### U

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#undcommand` | Defined | Monster | M6.34 p32; M6.34 p60 | `#undcommand <value>` |
| `#undead` | Defined | Monster | M6.34 p19 | `#undead` |
| `#undeadimmune` | Defined | Weapon | M6.34 p9 | `#undeadimmune` |
| `#undeadonly` | Defined | Weapon | M6.34 p9 | `#undeadonly` |
| `#undeadreanim` | Defined | Nation | M6.34 p50 | `#undeadreanim` |
| `#undisciplined` | Defined | Monster | M6.34 p32; M6.34 p60 | `#undisciplined` |
| `#undisleader` | Defined | Monster | M6.34 p33 | `#undisleader <value>` |
| `#undregen` | Defined | Monster | M6.34 p22; M6.34 p59 | `#undregen <percent>` |
| `#unify` | Defined | Monster | M6.34 p14 | `#unify` |
| `#unique` | Defined | Item, Monster | M6.34 p19; M6.34 p57 | `#unique` |
| `#unit` | Defined | Mercenary | M6.34 p63 | `#unit "<monster name>"` |
| `#units` | Defined | Map | P6.26 p8 | `#units <nbr of units> "<type>"` |
| `#unmountedspr1` | Defined | Monster | M6.34 p30 | `#unmountedspr1 "<imgfile>"` |
| `#unmountedspr2` | Defined | Monster | M6.34 p30 | `#unmountedspr2 "<imgfile>"` |
| `#unrepel` | Defined | Weapon | M6.34 p10 | `#unrepel` |
| `#unrest` | Defined | Event, Map | E6.29 p13; P6.26 p8 | `#unrest <value>` |
| `#unresthalfinc` | Defined | General | M6.34 p61 | `#unresthalfinc <unrest level>` |
| `#unresthalfres` | Defined | General | M6.34 p61 | `#unresthalfres <unrest level>` |
| `#unseen` | Defined | Monster | M6.34 p25; M6.34 p59 | `#unseen` |
| `#unsurr` | Reference | Monster | M6.34 p36; M6.34 p59 | `#unsurr` |
| `#unteleportable` | Defined | Monster | M6.34 p20; M6.34 p58 | `#unteleportable` |
| `#userestricteditem` | Defined | Item, Monster | M6.34 p18 | `#userestricteditem <value>` |
| `#uwbug` | Defined | Monster | M6.34 p19 | `#uwbug` |
| `#uwbuild` | Defined | Nation | M6.34 p47 | `#uwbuild <0 or 1>` |
| `#uwcom` | Defined | Nation | M6.34 p45 | `#uwcom "<monster name>" \| <monster nbr>` |
| `#uwdamage` | Defined | Monster | M6.34 p21; M6.34 p59 | `#uwdamage <percent>` |
| `#uwfireshield` | Defined | Monster | M6.34 p24; M6.34 p59 | `#uwfireshield <damage>` |
| `#uwheat` | Defined | Monster | M6.34 p23; M6.34 p59 | `#uwheat <0-100>` |
| `#uwnation` | Defined | Site | M6.34 p43 | `#uwnation` |
| `#uwok` | Defined | Weapon | M6.34 p11 | `#uwok` |
| `#uwrec` | Defined | Nation | M6.34 p45 | `#uwrec "<monster name>" \| <monster nbr>` |
| `#uwregen` | Defined | Monster | M6.34 p23; M6.34 p59 | `#uwregen <percent>` |
| `#uwwallcom` | Defined | Monster, Nation | M6.34 p38; M6.34 p47 | `#uwwallcom "<monster name>" \| <monster nbr>` |
| `#uwwallmult` | Defined | Monster, Nation | M6.34 p38; M6.34 p47 | `#uwwallmult <multiplier>` |
| `#uwwallunit` | Defined | Monster, Nation | M6.34 p38; M6.34 p47 | `#uwwallunit "<monster name>" \| <monster nbr>` |

### V

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#var0units` | Defined | Event | E6.29 p15 | `#var0units "name" \| <number>` |
| `#version` | Defined | General, Metadata | M6.34 p5; M6.34 p64 | `#version x.yy` |
| `#victorycondition` | Defined | Map | P6.26 p6 | `#victorycondition <condition> <attribute>` |
| `#viewallbat` | Defined | Nation | M6.34 p43 | `#viewallbat` |
| `#viewallprov` | Defined | Nation | M6.34 p43 | `#viewallprov` |
| `#visitors` | Defined | Event | E6.29 p13 | `#visitors` |
| `#voidgate` | Defined | Monster | M6.34 p38 | `#voidgate <success chance>` |
| `#voidret` | Defined | Monster | M6.34 p35; M6.34 p60 | `#voidret <chance>` |
| `#voidsanity` | Defined | Item, Monster | M6.34 p17; M6.34 p56 | `#voidsanity <value>` |

### W

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#walkable` | Defined | Spell | M6.34 p52 | `#walkable <0 or 1>` |
| `#wallcom` | Defined | Monster, Nation | M6.34 p38; M6.34 p46 | `#wallcom "<monster name>" \| <monster nbr>` |
| `#wallmult` | Defined | Monster, Nation | M6.34 p38; M6.34 p46 | `#wallmult <multiplier>` |
| `#wallunit` | Defined | Monster, Nation | M6.34 p38; M6.34 p46 | `#wallunit "<monster name>" \| <monster nbr>` |
| `#warning` | Defined | Monster | M6.34 p32; M6.34 p60 | `#warning <bonus>` |
| `#wastelabcost` | Defined | Nation | M6.34 p48 | `#wastelabcost <price>` |
| `#wastesurvival` | Defined | Monster | M6.34 p20 | `#wastesurvival` |
| `#wastetemplecost` | Defined | Nation | M6.34 p48 | `#wastetemplecost <price>` |
| `#waterblessbonus` | Defined | Nation | M6.34 p47 | `#waterblessbonus <0 - 9>` |
| `#waterboost` | Defined | Event | E6.29 p16; E6.29 p19 | `#waterboost "name" \| <number>` |
| `#waterbreathing` | Defined | Item | M6.34 p57 | `#waterbreathing` |
| `#waterelementals` | Defined | Monster | M6.34 p30; M6.34 p61 | `#waterelementals <bonus>` |
| `#waterrange` | Defined | Monster, Site | M6.34 p33; M6.34 p39; M6.34 p60 | `#waterrange <range>` |
| `#watershape` | Defined | Monster | M6.34 p28 | `#watershape "<monster name>" \| <monster nbr>` |
| `#weapon` | Defined | Item, Weapon | M6.34 p17; M6.34 p56 | `#weapon "<weapon name>" \| <nbr>` |
| `#wightreanim` | Defined | Nation | M6.34 p50 | `#wightreanim` |
| `#wild` | Defined | Site | M6.34 p41 | `#wild` |
| `#winterpower` | Defined | Monster | M6.34 p24; M6.34 p59 | `#winterpower <percent>` |
| `#wintershape` | Defined | Monster | M6.34 p28 | `#wintershape "<monster name>" \| <monster nbr>` |
| `#wolftattoo` | Defined | Monster | M6.34 p26 | `#wolftattoo <value>` |
| `#woodenarmor` | Defined | Armour | M6.34 p13 | `#woodenarmor` |
| `#woodenweapon` | Defined | Weapon | M6.34 p10 | `#woodenweapon` |
| `#worldage` | Defined | Event | E6.29 p17 | `#worldage <years>` |
| `#worldcurse` | Defined | Event | E6.29 p17 | `#worldcurse <percent>` |
| `#worlddarkness` | Defined | Event | E6.29 p17 | `#worlddarkness` |
| `#worlddecscale` | Defined | Event | E6.29 p16 | `#worlddecscale <scale>` |
| `#worlddecscale2` | Defined | Event | E6.29 p16 | `#worlddecscale2 <scale>` |
| `#worlddecscale3` | Defined | Event | E6.29 p16 | `#worlddecscale3 <scale>` |
| `#worlddisease` | Defined | Event | E6.29 p17; E6.29 p20 | `#worlddisease <percent>` |
| `#worldheal` | Defined | Event | E6.29 p17 | `#worldheal <percent>` |
| `#worldincdom` | Defined | Event | E6.29 p17 | `#worldincdom <value>` |
| `#worldincscale` | Defined | Event | E6.29 p16 | `#worldincscale <scale>` |
| `#worldincscale2` | Defined | Event | E6.29 p16 | `#worldincscale2 <scale>` |
| `#worldincscale3` | Defined | Event | E6.29 p16 | `#worldincscale3 <scale>` |
| `#worldmark` | Defined | Event | E6.29 p17 | `#worldmark <percent>` |
| `#worldritrebate` | Defined | Event | E6.29 p17 | `#worldritrebate <school>` |
| `#worldshape` | Defined | Monster | M6.34 p28 | `#worldshape "<monster name>" \| <monster nbr>` |
| `#worldunrest` | Defined | Event | E6.29 p17 | `#worldunrest <value>` |
| `#worldvisible` | Defined | Spell | M6.34 p54 | `#worldvisible <0 - 1>` |
| `#woundfend` | Defined | Monster | M6.34 p22; M6.34 p59 | `#woundfend <value>` |

### X

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#xp` | Defined | Event, Map, Mercenary, Site | E6.29 p16; P6.26 p8; M6.34 p40; M6.34 p63 | `#xp <experience points>` |
| `#xpgain` | Defined | Monster | M6.34 p22; M6.34 p59 | `#xpgain <percent>` |
| `#xploss` | Defined | Monster | M6.34 p28; M6.34 p60 | `#xploss <0-100>` |
| `#xpshape` | Defined | Monster | M6.34 p28 | `#xpshape <xp value>` |
| `#xpshapeloss` | Defined | Monster | M6.34 p28 | `#xpshapeloss <0-100>` |
| `#xpshapemon` | Defined | Monster | M6.34 p28 | `#xpshapemon "<monster name>" \| <monster nbr>` |
| `#xspr1` | Defined | Monster | M6.34 p31 | `#xspr1 "<imgfile>"` |
| `#xspr2` | Defined | Monster | M6.34 p31 | `#xspr2 "<imgfile>"` |

### Y

| Token | Status | Domain | Official locator | Strongest syntax |
|---|---|---|---|---|
| `#yearaging` | Defined | Item | M6.34 p58 | `#yearaging <value>` |
| `#yearturn` | Defined | Monster | M6.34 p24; M6.34 p59 | `#yearturn <bonus>` |
<!-- GENERATED:END command-locator -->

## Template and alias locator

The alias table lists concrete search terms generated from official terrain and numeric templates. Each alias points back to one canonical template definition.

<!-- GENERATED:BEGIN template-aliases -->
| Search alias | Official template | Derivation |
|---|---|---|
| `#batstartsum1` | `#batstartsum1...5` | Numeric range |
| `#batstartsum1d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum2` | `#batstartsum1...5` | Numeric range |
| `#batstartsum2d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum3` | `#batstartsum1...5` | Numeric range |
| `#batstartsum3d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum4` | `#batstartsum1...5` | Numeric range |
| `#batstartsum4d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum5` | `#batstartsum1...5` | Numeric range |
| `#batstartsum5d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum6d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum7d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum8d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#batstartsum9d6` | `#batstartsum1d6...9d6` | Numeric range |
| `#battlesum1` | `#battlesum1...5` | Numeric range |
| `#battlesum2` | `#battlesum1...5` | Numeric range |
| `#battlesum3` | `#battlesum1...5` | Numeric range |
| `#battlesum4` | `#battlesum1...5` | Numeric range |
| `#battlesum5` | `#battlesum1...5` | Numeric range |
| `#cavecom` | `#(terrain)com` | Terrain substitution |
| `#cavefortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#cavefortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#caverec` | `#(terrain)rec` | Terrain substitution |
| `#coastcom` | `#(terrain)com` | Terrain substitution |
| `#coastcom1` | `#coastcom1...2` | Numeric range |
| `#coastcom2` | `#coastcom1...2` | Numeric range |
| `#coastfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#coastfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#coastrec` | `#(terrain)rec` | Terrain substitution |
| `#coastunit1` | `#coastunit1...3` | Numeric range |
| `#coastunit2` | `#coastunit1...3` | Numeric range |
| `#coastunit3` | `#coastunit1...3` | Numeric range |
| `#deepcom` | `#(terrain)com` | Terrain substitution |
| `#deeprec` | `#(terrain)rec` | Terrain substitution |
| `#dripcom` | `#(terrain)com` | Terrain substitution |
| `#dripfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#dripfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#driprec` | `#(terrain)rec` | Terrain substitution |
| `#farmcom` | `#(terrain)com` | Terrain substitution |
| `#farmfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#farmfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#farmrec` | `#(terrain)rec` | Terrain substitution |
| `#foreigncom` | `#(terrain)com` | Terrain substitution |
| `#foreignfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#foreignfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#foreignrec` | `#(terrain)rec` | Terrain substitution |
| `#forestcom` | `#(terrain)com` | Terrain substitution |
| `#forestfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#forestfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#forestrec` | `#(terrain)rec` | Terrain substitution |
| `#hero1` | `#hero1...10` | Numeric range |
| `#hero10` | `#hero1...10` | Numeric range |
| `#hero2` | `#hero1...10` | Numeric range |
| `#hero3` | `#hero1...10` | Numeric range |
| `#hero4` | `#hero1...10` | Numeric range |
| `#hero5` | `#hero1...10` | Numeric range |
| `#hero6` | `#hero1...10` | Numeric range |
| `#hero7` | `#hero1...10` | Numeric range |
| `#hero8` | `#hero1...10` | Numeric range |
| `#hero9` | `#hero1...10` | Numeric range |
| `#kelpcom` | `#(terrain)com` | Terrain substitution |
| `#kelprec` | `#(terrain)rec` | Terrain substitution |
| `#makemonsters1` | `#makemonsters1...5` | Numeric range |
| `#makemonsters2` | `#makemonsters1...5` | Numeric range |
| `#makemonsters3` | `#makemonsters1...5` | Numeric range |
| `#makemonsters4` | `#makemonsters1...5` | Numeric range |
| `#makemonsters5` | `#makemonsters1...5` | Numeric range |
| `#mountaincom` | `#(terrain)com` | Terrain substitution |
| `#mountainfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#mountainfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#mountainrec` | `#(terrain)rec` | Terrain substitution |
| `#multihero1` | `#multihero1...7` | Numeric range |
| `#multihero2` | `#multihero1...7` | Numeric range |
| `#multihero3` | `#multihero1...7` | Numeric range |
| `#multihero4` | `#multihero1...7` | Numeric range |
| `#multihero5` | `#multihero1...7` | Numeric range |
| `#multihero6` | `#multihero1...7` | Numeric range |
| `#multihero7` | `#multihero1...7` | Numeric range |
| `#plaincom` | `#(terrain)com` | Terrain substitution |
| `#plainfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#plainfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#plainrec` | `#(terrain)rec` | Terrain substitution |
| `#seacom` | `#(terrain)com` | Terrain substitution |
| `#searec` | `#(terrain)rec` | Terrain substitution |
| `#summon1` | `#summon1...5` | Numeric range |
| `#summon2` | `#summon1...5` | Numeric range |
| `#summon3` | `#summon1...5` | Numeric range |
| `#summon4` | `#summon1...5` | Numeric range |
| `#summon5` | `#summon1...5` | Numeric range |
| `#swampcom` | `#(terrain)com` | Terrain substitution |
| `#swampfortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#swampfortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#swamprec` | `#(terrain)rec` | Terrain substitution |
| `#wastecom` | `#(terrain)com` | Terrain substitution |
| `#wastefortcom` | `#(terrain)fortcom` | Terrain substitution |
| `#wastefortrec` | `#(terrain)fortrec` | Terrain substitution |
| `#wasterec` | `#(terrain)rec` | Terrain substitution |
<!-- GENERATED:END template-aliases -->

## Complete patch-token index

This locator index contains the 221 hash tokens extracted from official 6.01-6.35 announcements. Exact entries link directly to the pinned manual record, while non-exact entries use the controlled reconciliation described in Part VI. The five event commands introduced by 6.36 remain in the patch-only supplement until the complete current-manual locator is rebuilt; 6.37 added no hash tokens.

<!-- GENERATED:BEGIN patch-token-index -->
| Patch token | Present resolution | First version | Patch records |
|---|---|---:|---:|
| `#3castbattlespell` | `#3castbattlespell` | 6.30 | 1 |
| `#addgeo` | `#addgeo` | 6.08 | 1 |
| `#addkills` | `#addkills` | 6.12 | 1 |
| `#addseduction` | `#addseductions` | 6.12 | 1 |
| `#aftercloud` | `#aftercloud` | 6.08 | 1 |
| `#aftercloudarea` | `#aftercloudarea` | 6.08 | 1 |
| `#aiassmod` | `#aiassmod` | 6.18 | 1 |
| `#aibadlvl` | `#aibadlvl` | 6.27 | 1 |
| `#aimusthavemag` | `#aimusthavemag` | 6.04 | 1 |
| `#airshield` | `#airshield` | 6.04 | 1 |
| `#ammo` | `#ammo` | 6.07 | 1 |
| `#animated` | `#animated` | 6.12 | 1 |
| `#assassin` | `#assassin` | 6.09 | 1 |
| `#assencloc` | `#assencloc` | 6.04 | 1 |
| `#assfollower1` | `#assfollower1` | 6.07 | 1 |
| `#assfollower1d3` | `#assfollower1d3` | 6.07 | 1 |
| `#assownerench` | `#assownerench` | 6.19 | 1 |
| `#att` | `#att` | 6.08 | 1 |
| `#battlesum1dx` | `#battlesum1d2`, `#battlesum1d3` | 6.27 | 1 |
| `#battlesumwarm` | `#battlesumwarm` | 6.27 | 1 |
| `#bugshape` | `#bugshape` | 6.24 | 2 |
| `#bugswarmshape` | `#bugswarmshape` | 6.24 | 1 |
| `#bugswarmuwshape` | `#bugswarmuwshape` | 6.24 | 1 |
| `#buguwshape` | `#buguwshape` | 6.24 | 1 |
| `#caveinc` | `#caveinc` | 6.24 | 1 |
| `#cavenation` | `#cavenation` | 6.16 | 1 |
| `#caverecpt` | `#caverecpt` | 6.24 | 1 |
| `#caveres` | `#caveres` | 6.24 | 1 |
| `#chaosrecscale` | `#chaosrecscale` | 6.11 | 1 |
| `#chaosscale` | `#chaosscale` | 6.08 | 1 |
| `#chorusmaster` | `#chorusmaster` | 6.23 | 1 |
| `#chorusslave` | `#chorusslave` | 6.23 | 1 |
| `#clear` | `#clear` | 6.19 | 1 |
| `#clearrec` | `#clearrec` | 6.23 | 1 |
| `#clumsy` | `#clumsy` | 6.08 | 1 |
| `#coastcom1` | `#coastcom1...2` | 6.04 | 1 |
| `#coastfortcom` | `#(terrain)fortcom` | 6.05 | 1 |
| `#coastfortrec` | `#(terrain)fortrec` | 6.05 | 1 |
| `#coastunit1` | `#coastunit1...3` | 6.04 | 1 |
| `#coldifhit` | `#coldifhit` | 6.08 | 1 |
| `#coldscale` | `#coldscale` | 6.16 | 1 |
| `#copysite` | `#copysite` | 6.29 | 1 |
| `#corruptor` | `#corruptor` | 6.09 | 1 |
| `#cure` | `#cure` | 6.13 | 1 |
| `#deathgrab` | `#deathgrab` | 6.04 | 1 |
| `#deathrecscale` | `#deathrecscale` | 6.11 | 1 |
| `#deathshock` | `#deathshock` | 6.04 | 1 |
| `#deathslime` | `#deathslime` | 6.04 | 1 |
| `#dec10var` | `#dec10var` | 6.15 | 1 |
| `#deeprec` | `#(terrain)rec` | 6.04 | 1 |
| `#defroll` | `#defroll` | 6.29 | 1 |
| `#disbless` | `#disbless` | 6.01 | 1 |
| `#dispglobals` | `#dispglobals` | 6.16 | 1 |
| `#dompower` | `#dompower` | 6.23 | 1 |
| `#domwar` | `#domwar` | 6.12 | 1 |
| `#dread` | `#dread` | 6.04 | 1 |
| `#dripfortrec` | `#(terrain)fortrec` | 6.04 | 1 |
| `#driprec` | `#(terrain)rec` | 6.04 | 1 |
| `#elementgems` | `#elementgems` | 6.12 | 1 |
| `#enchantedblood` | `#enchantedblood` | 6.27 | 1 |
| `#extralives` | `#extralives` | 6.04 | 1 |
| `#false` | `#false` | 6.08 | 1 |
| `#falseregen` | `#falseregen` | 6.04 | 1 |
| `#falsesupply` | `#falsesupply` | 6.08 | 1 |
| `#faysummon` | `#faysummon` | 6.30 | 1 |
| `#fearofflood` | `#fearofflood` | 6.08 | 1 |
| `#fireelementals` | `#fireelementals` | 6.04 | 1 |
| `#fireifhit` | `#fireifhit` | 6.08 | 1 |
| `#force` | `#force1d3vis`, `#force1d6vis`, `#force2d4vis`, `#force2d6vis`, `#force3d6vis`, `#force4d6vis` | 6.06 | 1 |
| `#force1d3vis` | `#force1d3vis` | 6.05 | 1 |
| `#forceexactgold` | `#forceexactgold` | 6.05 | 1 |
| `#forcegold` | `#forcegold` | 6.05 | 1 |
| `#forcess` | `#forcess` | 6.32 | 1 |
| `#forestfortcom` | `#(terrain)fortcom` | 6.04 | 1 |
| `#forestfortrec` | `#(terrain)fortrec` | 6.04 | 1 |
| `#fort` | `#fort` | 6.19 | 1 |
| `#fortcoldscaleres` | `#fortcoldscaleres` | 6.23 | 1 |
| `#gemlongevity` | `#gemlongevity` | 6.16 | 1 |
| `#gemlosslarge` | `#gemlosslarge` | 6.07 | 1 |
| `#gemlosssmall` | `#gemlosssmall` | 6.07 | 1 |
| `#glamourmanip` | `#glamourmanip` | 6.08 | 1 |
| `#globallook` | `#globallook` | 6.07 | 1 |
| `#godpathspell` | `#godpathspell` | 6.08 | 1 |
| `#godsite` | `#godsite` | 6.08 | 1 |
| `#grandcom` | `#grandcom` | 6.29 | 1 |
| `#growthpower` | `#growthpower` | 6.29 | 1 |
| `#growthrecscale` | `#growthrecscale` | 6.11 | 1 |
| `#header` | `#header` | 6.12 | 1 |
| `#healaff` | `#healaff` | 6.08 | 1 |
| `#hidedom` | `#hidedom` | 6.11 | 1 |
| `#holyifhit` | `#holyifhit` | 6.08 | 1 |
| `#holyrange` | `#holyrange` | 6.12 | 1 |
| `#homerealm` | `#homerealm` | 6.33 | 1 |
| `#icenatprot` | `#icenatprot` | 6.12 | 1 |
| `#illusionimmune` | `#illusionsimmune` | 6.08 | 1 |
| `#inc10var` | `#inc10var` | 6.15 | 1 |
| `#kelpcom` | `#(terrain)com` | 6.24 | 1 |
| `#kelprec` | `#(terrain)rec` | 6.04 | 2 |
| `#killdemonifhit` | `#killdemonifhit` | 6.08 | 1 |
| `#killmagicifhit` | `#killmagicifhit` | 6.08 | 1 |
| `#localglobal` | `#localglobal` | 6.07 | 1 |
| `#look` | `#look` | 6.08 | 1 |
| `#magiconly` | `#magiconly` | 6.23 | 1 |
| `#makecrater` | `#makecrater` | 6.25 | 1 |
| `#maxage` | `#maxage` | 6.15 | 1 |
| `#maybeaddsite` | `#maybeaddsite` | 6.30 | 1 |
| `#maybehiddensite` | `#maybehiddensite` | 6.30 | 1 |
| `#melee50` | `#melee50` | 6.07 | 1 |
| `#mindcollar` | `#mindcollar` | 6.19 | 1 |
| `#minsizeleader` | `#minsizeleader` | 6.04 | 1 |
| `#mobilearcher` | `#mobilearcher` | 6.12 | 1 |
| `#morroll` | `#morroll` | 6.29 | 1 |
| `#mrhalf` | `#mrhalf` | 6.24 | 1 |
| `#name` | `#name` | 6.05 | 1 |
| `#napbreakrit` | `#napbreakrit` | 6.19 | 1 |
| `#natcom` | `#natcom` | 6.03 | 1 |
| `#natmon` | `#natmon` | 6.03 | 1 |
| `#nightmareaura` | `#nightmareaura` | 6.04 | 1 |
| `#nodeepchoice` | `#nodeepchoice` | 6.01 | 1 |
| `#norange` | `#norange` | 6.08 | 1 |
| `#not` | `#notmounted`, `#notdismounted` | 6.12 | 1 |
| `#notfornation` | `#notfornation` | 6.07 | 1 |
| `#notindoors` | `#notindoors` | 6.25 | 1 |
| `#notmnr` | `#notmnr` | 6.19 | 1 |
| `#notmounted` | `#notmounted` | 6.09 | 1 |
| `#onlyfriendlydst` | `#onlyfriendlydst` | 6.13 | 1 |
| `#onlymnr` | `#onlymnr` | 6.19 | 1 |
| `#onlysitedst` | `#onlysitedst` | 6.19 | 1 |
| `#orderrecscale` | `#orderrecscale` | 6.11 | 1 |
| `#orderscale` | `#orderscale` | 6.08 | 1 |
| `#petrifyifhit` | `#petrifyifhit` | 6.08 | 1 |
| `#plaguedoctor` | `#plaguedoctor` | 6.09 | 1 |
| `#plaincom` | `#(terrain)com` | 6.24 | 1 |
| `#plainfortcom` | `#(terrain)fortcom` | 6.24 | 1 |
| `#plainfortrec` | `#(terrain)fortrec` | 6.24 | 1 |
| `#plainrec` | `#(terrain)rec` | 6.24 | 1 |
| `#poisonifdmg` | `#poisonifdmg` | 6.08 | 1 |
| `#popgrowth` | `#popgrowth` | 6.11 | 1 |
| `#portent` | `#portent` | 6.13 | 1 |
| `#powerofdeath` | `#powerofdeath` | 6.08 | 1 |
| `#praise` | `#praise` | 6.25 | 1 |
| `#protparts` | `#protparts` | 6.21 | 1 |
| `#range0` | `#range0` | 6.07 | 1 |
| `#range050` | `#range050` | 6.07 | 1 |
| `#reclimit` | `#reclimit` | 6.24 | 1 |
| `#reconst` | `#reconst` | 6.04 | 1 |
| `#remgeo` | `#remgeo` | 6.08 | 1 |
| `#remount` | `#remount` | 6.04 | 2 |
| `#removesite` | `#removesite` | 6.35 | 1 |
| `#req_crystal` | `#req_crystal` | 6.15 | 1 |
| `#req_deep` | `#req_deep` | 6.15 | 1 |
| `#req_drip` | `#req_drip` | 6.15 | 1 |
| `#req_enchnearby` | `#req_enchnearby` | 6.11 | 1 |
| `#req_enchtarget` | `#req_enchtarget` | 6.07 | 2 |
| `#req_forestcave` | `#req_forestcave` | 6.15 | 1 |
| `#req_fortid` | `#req_fortid` | 6.19 | 1 |
| `#req_godawake` | `#req_godawake` | 6.12 | 1 |
| `#req_godismnr` | `#req_godismnr` | 6.02 | 1 |
| `#req_gorge` | `#req_gorge` | 6.15 | 1 |
| `#req_kelp` | `#req_kelp` | 6.15 | 1 |
| `#req_maxglobals` | `#req_maxglobals` | 6.16 | 1 |
| `#req_minglobals` | `#req_minglobals` | 6.16 | 1 |
| `#req_minresearch` | `#req_minresearch` | 6.23 | 1 |
| `#req_monsterbs` | `#req_monsterbs` | 6.34 | 1 |
| `#req_month` | `#req_month` | 6.07 | 1 |
| `#req_norealmnr` | `#req_norealmnr` | 6.29 | 1 |
| `#req_notcode` | `#req_notcode` | 6.07 | 1 |
| `#req_notpoptype` | `#req_notpoptype` | 6.12 | 1 |
| `#req_path` | `#req_path` | 6.23 | 1 |
| `#req_pathgems` | `#req_pathgems` | 6.23 | 1 |
| `#req_plane` | `#req_plane` | 6.12 | 2 |
| `#req_pretawake` | `#req_pretawake` | 6.12 | 1 |
| `#req_pretismnr` | `#req_pretismnr` | 6.12 | 1 |
| `#req_realmnr` | `#req_realmnr` | 6.29 | 1 |
| `#req_school` | `#req_school` | 6.23 | 1 |
| `#req_targgod` | `#req_targgod` | 6.12 | 1 |
| `#req_targhorrormark` | `#req_targhorrormark` | 6.19 | 1 |
| `#req_targmanygems` | `#req_targmanygems` | 6.07 | 1 |
| `#req_targmaxkills` | `#req_targmaxkills` | 6.12 | 1 |
| `#req_targminkills` | `#req_targminkills` | 6.12 | 1 |
| `#req_targnorealmnr` | `#req_targnorealmnr` | 6.24 | 1 |
| `#req_targrealmnr` | `#req_targrealmnr` | 6.24 | 1 |
| `#req_targseductions` | `#req_targseductions` | 6.12 | 1 |
| `#req_targsight` | `#req_targsight` | 6.07 | 1 |
| `#req_turnrare` | `#req_turnrare` | 6.19 | 1 |
| `#req_void` | `#req_void` | 6.13 | 1 |
| `#reqnoseduce` | `#reqnoseduce` | 6.04 | 1 |
| `#reqnospellsinger` | `#reqnospellsinger` | 6.04 | 1 |
| `#reqnotaskmaster` | `#reqnotaskmaster` | 6.04 | 1 |
| `#res_mnrbs` | `#req_mnrbs` | 6.34 | 1 |
| `#revealsite` | `#revealsite` | 6.35 | 1 |
| `#sabbathmaster` | `#sabbathmaster` | 6.23 | 1 |
| `#sabbathslave` | `#sabbathslave` | 6.23 | 1 |
| `#searec` | `#(terrain)rec` | 6.04 | 1 |
| `#selectevent` | `#selectevent` | 6.19 | 1 |
| `#shockifhit` | `#shockifhit` | 6.08 | 1 |
| `#sizecost` | `#sizecost` | 6.30 | 1 |
| `#sleepres` | `#sleepres` | 6.23 | 1 |
| `#sorcerygems` | `#sorcerygems` | 6.12 | 1 |
| `#speedmult` | `#speedmult` | 6.07 | 1 |
| `#spikes` | `#spikes` | 6.23 | 1 |
| `#spiritformimmune` | `#spiritformimmune` | 6.08 | 1 |
| `#startitem` | `#startitem` | 6.02 | 1 |
| `#startresearch` | `#startresearch` | 6.04 | 1 |
| `#statbreak` | `#statbreak` | 6.19 | 1 |
| `#statstorm` | `#statstorm` | 6.19 | 1 |
| `#sumhealaffs` | `#sumhealaffs` | 6.21 | 1 |
| `#summon` | `#summon` | 6.27 | 1 |
| `#swimming` | `#swimming` | 6.13 | 1 |
| `#templegems` | `#templegems` | 6.04 | 1 |
| `#templeholypoints` | `#templeholypoints` | 6.19 | 1 |
| `#tolerateund` | `#tolerateund` | 6.30 | 1 |
| `#twiceborncost` | `#twiceborncost` | 6.30 | 1 |
| `#undisleader` | `#undisleader` | 6.04 | 1 |
| `#unseen` | `#unseen` | 6.29 | 1 |
| `#var0units` | `#var0units` | 6.30 | 1 |
| `#varxxx` | message placeholder | 6.16 | 1 |
| `#viewallbat` | `#viewallbat` | 6.07 | 1 |
| `#viewallprov` | `#viewallprov` | 6.07 | 1 |
| `#worldshape` | `#worldshape` | 6.05 | 1 |
| `#worldvisible` | `#worldvisible` | 6.07 | 1 |
<!-- GENERATED:END patch-token-index -->

# Part XI: Source and Publication Register

## Official sources

- [Illwinter's Dominions 6 documentation page](https://illwinter.com/dom6/docs.html)
- [Dominions 6 Modding Manual](https://illwinter.com/dom6/dom6modman.pdf), version 6.34
- [Dominions 6 Event Modding Manual](https://illwinter.com/dom6/dom6eventman.pdf), version 6.29
- [Dominions 6 Map Making Manual](https://illwinter.com/dom6/dom6mapman.pdf), version 6.26
- [Official Dominions 6 announcement archive](https://steamcommunity.com/app/2511500/announcements/)
- Book XIII's 1,096-record official patch chronology

## Publication boundary

The public register retains command and token spellings, syntax locators, pages, versions, section labels, hashes, classifications, aliases, and restrained editorial mappings. It does not reproduce the manuals' long descriptions. Readers requiring full official semantics are directed to the cited page.

Dominions Enhanced 2.16 and Divinitus 1.15.3 DE remain separate rulesets. A token found only in either supplied `.dm` source is not promoted into the vanilla official lexicon. Mod-source usage analysis can reference this register later, but the command's official status and the mod's implementation evidence must remain distinct.

## What this unlocks

The library now has five complementary retrieval layers:

- Book X explains how to operate the game;
- Book XI explains how to read units, abilities, experience, and conditions;
- Book XII indexes base-game objects;
- Book XIII explains when official rules and features changed;
- Book XIV identifies the official modding language used to alter those objects and systems.

This closes the principal shared-foundation gap before broad nation dossiers. Future mod analyses can identify every source token, resolve it to official context, detect documentation gaps, and link implementation choices to parser, object, event, map, AI, compatibility, and patch-history chapters without rebuilding the same glossary inside every faction or mod report.
