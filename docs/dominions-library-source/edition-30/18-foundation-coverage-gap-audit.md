# Foundation Coverage and Gap Audit

## Purpose

This audit determines what Progress Edition 24 already explains, what remains incomplete, and where any future addition must live. Its main purpose is preventative: new work should extend the library rather than restate it under a new title.

The audit compares the reader-facing corpus with:

- the official *Dominions 6 Manual*, revision 2;
- the official Modding Manual identified locally as version 6.34;
- the official Event Modding Manual identified locally as version 6.29;
- the official Map Making Manual identified locally as version 6.26;
- the official File Formats note;
- official update notes through Dominions 6.36, released 17 August 2026 UTC;
- the exact Dominions Enhanced 2.16 and Divinitus 1.15.3 DE source files already frozen by the project.

The official documentation page describes the main manual as the rules reference for new and experienced players and identifies the separate modding, event, map, and file-format manuals. The announcements through 6.36 remain necessary because the revision-2 manual predates later content, interface changes, rule corrections, and mod commands.

## Audit result

Edition 24 contains the foundational explanation of the game's central systems and the five retrieval and maintenance layers added after the first audit: player operations in Book X; units, abilities, experience, heroic traits, and conditions in Book XI; the pinned 6.35 base-game object reference in Book XII; the complete official 6.01-6.36 version spine in Book XIII; and the official command, template, message-token, and patch-reconciliation layer in Book XIV. It does **not** need another general book about those subjects, turns, economy, Pretender design, battles, magic, campaign strategy, modding principles, patch history, command syntax, or the DE/Divinitus ruleset.

The remaining work falls into three different kinds:

1. **Database edge cases** - Book XII and its 4,196-record register cover the reusable 6.35 object layer, while independent population types, 25 selection-based summon relations, several human-readable property labels, and complete realm expansion remain explicit limitations.
2. **Maintenance gaps** - the official patch history and command vocabulary now have complete source-linked registers; 250 lower-confidence patch classifications, 60 reference-only command tokens, nine mention-only command tokens, and five 6.36 patch-only event commands remain in visible review queues.
3. **Coverage expansion** - only Middle Age Arcoscephale has a complete nation dossier. The remaining national library is planned work rather than a missing general rulebook.

Several rules also remain **verification gaps** rather than writing gaps. Those questions already belong to the research register and must not be turned into confident new prose until reliable evidence exists.

## Status key

| Status | Meaning | Editorial response |
| --- | --- | --- |
| Complete | The subject has a clear authoritative home and sufficient foundational treatment. | Cross-reference it; do not create another general explanation. |
| Substantially complete | The reusable foundation and records exist, but explicit edge cases remain. | Maintain the existing layer and resolve only the listed limitations. |
| Distributed | Different books own distinct mechanical, tactical, or strategic layers. | Preserve the division and improve navigation if needed. |
| Underdeveloped | The subject appears, but a major practical or reference layer is absent. | Expand only the assigned home. |
| Structured-data gap | Prose methodology exists, but a complete object catalogue does not. | Build versioned records rather than another essay. |
| Planned dossier work | The reusable method exists, but nation-specific application is incomplete. | Use the Book VII dossier template. |
| Verification pending | The question is stated but reliable evidence remains incomplete. | Keep it in the research register; do not fill the gap by inference. |
| Intentionally excluded | The material has little player value or is better served by the official document. | Link to the source unless a concrete project later requires it. |

## Canonical ownership map

This table is the first check for every proposed section.

| Domain | Authoritative home | Permitted secondary treatment | Duplication boundary |
| --- | --- | --- | --- |
| Ruleset, version labels, evidence and hosting sequence | Book I | Field reference for abbreviated timing | No second anatomy-of-a-turn chapter. |
| Gold, population, resources, recruitment, upkeep, supply, infrastructure, PD and siege arithmetic | Book II | Field formulas; Book VI campaign consequences | Exact arithmetic remains in Book II. |
| Pretenders, design points, awakening, dominion, scales, blessings and god recovery | Book III | Nation-specific builds in dossiers; exact DE changes in Book IX | General Pretender theory is not rewritten per nation. |
| Unit reading, army construction, battle orders, formations and combat resolution | Book IV | Nation-specific army packages; campaign use in Book VI | Combat formulas and battle scripting stay in Book IV. |
| Research, paths, gems, communions, rituals, globals, forging and late magic | Book V | Battle arithmetic in Book IV; national research branches in dossiers | Magical planning is not duplicated as spell-list prose. |
| Expansion, intelligence, logistics, raiding, war, sieges, diplomacy, Thrones, recovery and turn discipline | Book VI | Mechanical rules in their system books | No new general strategy compendium. |
| Nation-analysis method and nation-specific application | Book VII and later dossiers | Rules cross-referenced from Books I-VI | Dossiers apply rules; they do not re-teach the foundation. |
| Mod construction, events, maps, AI scaffolding, compatibility and testing | Book VIII | Exact DE/Divinitus findings in Book IX | Generic method stays in Book VIII. |
| Frozen DE 2.16 and Divinitus 1.15.3 DE source facts | Book IX | Nation-specific consequences in dossiers | Exact inventories and collisions stay in Book IX. |
| Reader routes, glossary, concordance and retrieval | Reader's Guide | Short definitions only | Navigation never becomes a second rules authority. |
| Interface, game creation, hosting, files, shortcuts and strategic map-order procedure | Book X | Brief links from existing operational checklists | Book X explains operation and links to existing rules and strategy. |
| Unit classes, experience, heroic abilities and the systematic ability reference | Book XI | Combat consequences linked to Book IV | The reference defines abilities; Book IV retains combat derivations. |
| Complete unmodded object catalogues | Book XII and website data layer | Selected strategic examples in Books II-VI | Use versioned records, filters and links rather than long replicated tables. |
| Official release chronology and patch maintenance | Book XIII and website patch ledger | Current-rule corrections in each affected canonical book | Preserve chronology here; do not turn system books into patch diaries. |
| Official command syntax, templates, manual context, message substitutions and patch reconciliation | Book XIV and website command lexicon | Design method in Book VIII; chronology in Book XIII | Locate and reconcile language here without copying the official manuals or repeating design guidance. |

## Main-manual coverage matrix

### Entry, interface, and game operation

| Manual subject | Status | Existing home | Gap or action |
| --- | --- | --- | --- |
| Introduction and series history | Intentionally excluded | Nation lore appears where strategically useful | Preserve the official narrative; add lore only when it supports a nation or mechanic. |
| Starting and creating a game | Complete procedurally | Book X; Book VI retains strategic setting consequences | Maintain the creation workflow and setting explanations in Book X. |
| Choosing an age and participants | Complete procedurally and distributed strategically | Book X procedure; Books I, III, VI and VII consequences | Maintain the procedure in Book X; strategic consequences remain in the existing books. |
| Disciple game setup | Complete procedurally | Book X; Book III explains disciple design | Maintain lobby creation, teams and start procedure without repeating disciple mechanics. |
| Pretender creation interface | Complete procedurally | Book X; Book III fully owns design theory and arithmetic | Maintain controls, saving and loading; all design advice links to Book III. |
| Game settings, Throne settings and Cataclysm | Distributed | Book VI owns strategic consequences | Add a setup table in Book X; do not repeat throne-rush or Cataclysm strategy. |
| Limited artifact forging and legendary research settings | Complete procedurally | Book X; Book V explains artifacts and legendary research | Maintain the toggles and links to Book V. |
| Renaming, cheat prevention and master password | Complete procedurally | Book X | Maintain procedures, security cautions and hosting responsibilities. |
| Game tools and user-data locations | Complete procedurally | Book X; Book VIII covers the mod directory | Ordinary player tools stay in Book X; Book VIII retains mod-project setup. |
| Hotseat, network play and official lobby | Complete procedurally | Book X; Book VI covers multiplayer conduct | Maintain the current hosting and joining guide in Book X. |
| Interface screens, filters, overlays and shortcuts | Complete procedurally | Book X | Maintain the task-based interface and shortcut reference. |
| Save, turn, Pretender and map files | Complete procedurally | Book X; Book VIII covers mod and map project files | Maintain player-facing file, backup, transfer and version safety. |

### Map, province, economy, and state

| Manual subject | Status | Existing home | Gap or action |
| --- | --- | --- | --- |
| Province attributes, terrain, population, income and resources | Complete | Book II | Cross-reference only. |
| Recruitment Points and recruitment restrictions | Complete | Book II | Cross-reference only. |
| Dominion, unrest, supplies, starvation and defence | Distributed | Books II-IV | Preserve the mechanical ownership already assigned. |
| Province corpses and corpse visibility | Underdeveloped | Book II mentions corpses only in provincial role lists | Add one bounded Book II section on visibility, production, persistence where verified, reanimation and spell interaction. |
| National summary and gem inventory | Complete procedurally | Book X; Books II and V explain the underlying systems | Maintain screen-reading procedure without formula repetition. |
| Forts, fort statistics, resource collection and supply | Complete | Book II | Book VI may discuss positioning and campaigns only. |
| Temples and laboratories | Complete | Book II; religious consequences in Book III | Interface construction procedure may be shown once in Book X. |
| Magic sites and site searching | Complete with records | Books II and V; Book XII catalogue | Maintain exact records in the data layer and interpretation in the system books. |
| Province Defence | Complete | Book II; campaign use in Book VI | Cross-reference only. |
| Mercenaries | Complete with records | Book X procedure; Book XII catalogue; timing in Book I | Maintain company records and cross-reference economic evaluation. |
| Scouting, scrying and score graphs | Complete strategically | Book VI | Book X may explain filters and screens; 6.35 victory-reveal behaviour needs a targeted correction in Book VI. |
| AI opponents and difficulty | Complete strategically | Book VI; mod hints in Book VIII | Patch-specific behaviour belongs in the version ledger. |
| Random-event reports and event settings | Complete procedurally | Book X; Book I owns timing; Book III owns Luck and Misfortune; Book VIII owns event modding | Exhaustive event records, if pursued, belong to a separate structured layer. |

### Pretenders, dominion, and religion

| Manual subject | Status | Existing home | Gap or action |
| --- | --- | --- | --- |
| Physical forms, magic, Divine Magic and blessings | Complete with records | Book III; exact form records in Book XII | Maintain design theory and object identity as separate layers. |
| Dominion strength, scales and awakening | Complete | Book III | Verification questions remain in the research register. |
| Pretender death, Call God and immortality | Complete with pending edge cases | Book III | Do not add a second recovery chapter. |
| Dominion spread, preaching, prophets, Inquisitors and Heretics | Complete | Book III | Campaign pressure may be discussed only as application in Book VI. |
| Blood sacrifice | Complete | Book III; Blood production in Book II | Cross-reference the two resource layers. |
| Dominion effects and special dominions | Complete as a foundation and current register | Book III provides categories and method; Book XII records official systems | Add nation-specific applications only where a dossier needs them. |
| Origins and identities of nations | Planned dossier work | Book VII supplies the method and Arcoscephale pilot | Add lore inside each dossier when it explains roster or mechanics. |

### Units, armies, orders, and combat

| Manual subject | Status | Existing home | Gap or action |
| --- | --- | --- | --- |
| Basic unit attributes | Complete | Book IV | Cross-reference only. |
| Unit classes and approximately 500 special abilities | Complete as an interpretive reference | Book XI; Book IV explains battle resolution | Maintain the versioned reference without forcing every definition into Book IV prose. |
| Experience and heroic abilities | Complete with explicit verification limits | Book XI | Maintain systematic reference tables and keep unresolved formulas in the research register. |
| Afflictions and healing | Complete mechanically | Book IV; Pretender and nation consequences elsewhere | Cross-reference only. |
| Recruiting units and costs | Complete | Book II | The click-by-click procedure belongs in Book X. |
| Army setup, squads, battle position, formations and battle orders | Complete | Book IV | Book X may explain interface manipulation without re-teaching tactics. |
| Unit inventories and equipment | Complete with records | Book V; Book XII item catalogue | Book V owns use and access; Book XII owns object records. |
| Strategic movement | Complete procedurally and distributed mechanically | Book X owns order entry; Book I timing; Book VI operational use | Preserve the division between procedure, timing, and strategy. |
| Ordinary strategic orders | Complete procedurally and distributed mechanically | Book X procedure; Books I, II, III and VI consequences | Maintain one procedural order reference linked to authoritative mechanics. |
| Seduction, dream seduction, corruption and similar special actions | Complete procedurally | Book X; strategic context in Book VI | Maintain eligibility, outcomes and failure handling in the strategic-order reference. |
| Reanimation, Contact Allies, Capture Slaves and special labour orders | Complete procedurally | Book X; timing in Book I | Maintain the command reference without duplicating hosting. |
| Infiltration, Instill Uprising, Hide and special stealth orders | Complete procedurally | Book X; Book VI covers intelligence and unrest strategically | Maintain exact operational entries with links to Book VI. |
| Battle sequence and battlefield view | Complete | Book IV | Interface controls may be summarised in Book X. |
| Battlefield movement, melee, missile combat, mounts and damage families | Complete | Book IV | No new general battle book. |
| Morale, rout, retreat and long battles | Complete | Book IV | Campaign recovery remains in Book VI. |
| Sieges, storming and supply | Distributed | Book II arithmetic; Book IV battle; Book VI campaign | Preserve the three-layer division. |
| Weather | Complete as a compact reference | Book XI; battle consequences in Book IV | Maintain the lookup and link resolution back to Book IV. |

### Magic and objects

| Manual subject | Status | Existing home | Gap or action |
| --- | --- | --- | --- |
| Paths, schools, access, empowerment and indirect magic | Complete | Book V | Cross-reference only. |
| Battle magic mechanics | Complete | Book IV | Book V retains package selection and path doctrine. |
| Rituals, global enchantments, Dispel and protection | Complete as systems | Book V | Exact spell records belong to the database. |
| Communions and related systems | Complete | Book V | No second communion guide. |
| Gems, research, alchemy and forging | Complete | Book V | Interface steps may appear in Book X. |
| Magic items and path boosters | Complete method and catalogue | Book V; Book XII item records | Preserve the booster reference; maintain exact current records as data. |
| Battlefield spells | Complete method and catalogue | Books IV and V; Book XII spell records | Filter records by path, school, delivery, role and evidence without duplicating tactical explanation. |
| Summoning rituals | Complete method; substantially complete relations | Book V; Book XII summon records | Resolve the 25 selection-based relations when exact engine evidence becomes available. |
| Global enchantments and other rituals | Complete method and catalogue | Book V; Book XII spell records | Maintain full records without converting tables into repetitive prose. |
| Legendary spells, Wish and late-game magic | Complete strategically | Book V | Exact Wish vocabulary and edge cases remain verification work. |

### Nations and large catalogues

| Manual subject | Status | Existing home | Gap or action |
| --- | --- | --- | --- |
| Nation index and full national rosters | Planned dossier work | Book VII method; MA Arcoscephale complete | Continue nation dossiers only after the remaining foundation gaps are addressed. |
| Full spell, item and summon tables | Substantially complete structured layer | Book XII and website register; Book V supplies evaluation methods | Maintain searchable, versioned records and resolve listed summon selectors. |
| Complete Pretender, Throne, site, mercenary and independent catalogues | Substantially complete structured layer | Book XII; systems across Books II, III, V and VI | Pretenders, Thrones, sites and mercenaries are recorded; population-type membership remains an explicit gap. |

## Auxiliary-manual coverage

| Official document | Present coverage | Remaining gap | Priority |
| --- | --- | --- | --- |
| Modding Manual | Book VIII explains the parser model, major object families, safe workflows, compatibility and testing; Book XIV indexes every located token, context, template, syntax line and patch relation. | Reference-only and mention-only commands require stronger evidence before full semantic summaries. | Maintenance through Book XIV and R-057. |
| Event Modding Manual | Book VIII explains events as state machines, requirements, variables, chains, delays and validation; Book XIV indexes event commands and message substitutions. | Reference-only behaviour and post-6.29 documentation changes remain evidence tasks rather than missing index work. | Maintenance through Book XIV and R-057. |
| Map Making Manual | Book VIII covers topology, terrain, starts, Thrones, planes, gates, scenarios and packaging. | No task-based interface walkthrough for the current map editor. | Low to medium; add only when map work resumes. |
| File Formats | Deliberately not expanded. | Binary format detail has little current value for ordinary play or `.dm` authoring. | Low; retain the official one-page reference. |

## Current-version delta audit

The public baseline is Dominions 6.36. The structured object register remains pinned to 6.35. Edition 21 retains the important 6.35 corrections and the 6.36 official overlay.

- innate spellcasters resume their scripts after recovering from unconsciousness;
- automatic mount recovery occurs at the end of the turn;
- `#revealsite` and `#removesite` handle several sites with the same name.

The 6.36 material has been assigned rather than scattered:

| Delta | Correct home | Treatment |
| --- | --- | --- |
| Bless-load cancellation and activation edges | Book III | Setup-state correction integrated; R-016 completed without absorbing transformation or cross-source stacking. |
| Rust on zero-damage attacks | Book IV | Current secondary-effect boundary integrated. |
| Lost Land, Perpetual Storm, and river crossing | Books VI and XI | Route, environment, and mount-specific permissions integrated. |
| Blood-sacrificer item changes | Independent Blood paper | Order-preservation correction integrated without restating the sacrifice formula elsewhere. |
| Touchscreen and interface shortcuts | Book X | Current controls integrated in the operating reference. |
| Replay, release chronology, and all remaining deltas | Book XIII | Complete source-linked chronology retained. |
| Five new event commands and spell `spec2` support | Books VIII and XIV | Existence and provenance recorded; full syntax withheld until official documentation supplies it. |

Book XIII closes the broader maintenance gap. The project has a single machine-readable ledger covering all 32 official public updates and all 1,090 announcement bullets through 6.36. It classifies changes, records official source locators and hashes, identifies affected domains and commands, and routes each record toward canonical pages. Fine-grained classifications remain explicitly editorial, with 250 entries marked for review rather than treated as settled official categories.

## Genuine gaps and recommended order

### G-01 - Player operations, interface, setup, and hosting

**Priority:** P0

**Status:** Complete in Book X

**Proposed home:** Foundation Book X

**Working title:** *Playing and Hosting Dominions 6: Interface, Game Setup, Orders, and the First Campaign*

This is the largest genuine new-player gap. It should cover:

- installation and version confirmation;
- creating single-player, disciple, hotseat, network, and lobby games;
- age, map, AI, diplomacy, research, event, Throne and Cataclysm settings;
- Pretender, turn, map, mod and save-file handling;
- the main strategic screens, overlays, filters, messages and shortcuts;
- recruitment, army organisation, forging, research, ritual and order-entry workflows;
- every strategic map order, especially rare special orders;
- joining, hosting, extensions, stale prevention, substitution and master-password safety;
- a guided first-game sequence that points outward to the existing foundation books.

**Exclusions:** no 63-step hosting rewrite, no new economy chapter, no repeated Pretender-design theory, no duplicate battle scripting, and no second multiplayer-strategy essay.

### G-02 - Unit classes, abilities, experience, and condition reference

**Priority:** P1

**Status:** Complete in Book XI and `website/ability-register.json`

**Canonical home:** Foundation Book XI, with structured records generated for the website

The official manual states that the game contains roughly 500 special abilities and explains only a selection. Book IV correctly focuses on the abilities needed to derive battles. Book XI now supplies the dependable interpretive and lookup layer for unfamiliar icons, unit classes, experience, heroic abilities, and conditions.

Each record should contain:

- current name and version;
- unit-card wording and numeric value;
- mechanical category;
- battlefield, strategic, economic or religious effects;
- stacking and incompatibility rules where verified;
- counters and common misreadings;
- source and evidence status;
- links to Book IV rather than copied combat formulas.

### G-03 - Base-game object database

**Priority:** P1

**Status:** Substantially complete in Book XII and `website/base-object-register.json`

**Canonical home:** Foundation Book XII and TheHoboKingdom structured website layer

The first 6.35 build contains 4,196 versioned records: 1,474 spell rows, 529 items, 549 summon relations, 298 Pretender forms, 74 Thrones, 1,179 other sites, 78 mercenary companies, one explicit independent-coverage marker, and 14 special-dominion systems. The source manifest pins the extracted data to commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, records file hashes, and keeps source fields separate from editorial tags.

Remaining limits are explicit: independent population-type membership is not available in the pinned extract; 25 summon relations retain unresolved engine selections; several item and site property fields need authoritative human labels; and realm-based spell restrictions are not all expanded into nation lists. These are maintenance targets, not reasons to recreate the database in prose. Books II-VI retain strategic explanations and selected examples.

### G-04 - Complete official patch ledger

**Priority:** P1

**Status:** Substantially complete in Book XIII and `website/official-patch-ledger.json`

**Canonical home:** Foundation Book XIII and TheHoboKingdom structured website layer

The current complete build contains 32 official announcements and 1,090 records from 6.01 through 6.36. Every record has an official source identity, locator, source hash, editorial class, confidence, domains, terms, commands, record hash, and canonical destinations. The public ledger omits the full announcement text. Remaining work is bounded: review 250 lower-confidence derived classifications, resolve named objects more precisely as the object layer improves, and ingest future official updates without weakening completeness assertions.

### G-05 - Remaining nation dossiers

**Priority:** P2 after G-01 and the data foundation

**Proposed home:** Book VII series

The nation method is complete and MA Arcoscephale is the pilot. Each future dossier should import shared rules by link, then add only national roster facts, probability portfolios, research branches, army packages, Pretender families, matchups, mod deltas and tests.

### G-06 - Searchable mod-command lexicon

**Priority:** P2

**Status:** Substantially complete in Book XIV and `website/command-lexicon.json`

**Canonical home:** Foundation Book XIV and website developer reference

The current complete build contains 1,609 official-manual hash tokens, 97 controlled template aliases, and reconciliation records for all 226 patch-note tokens. Book VIII remains the design and validation manual; Book XIII remains the chronology. Remaining work is bounded to 60 reference-only entries, nine mention-only entries, five 6.36 patch-only commands awaiting full official syntax, future manual and patch ingestion, and any reliable runtime evidence needed to distinguish accepted syntax from observed behaviour.

## Targeted additions to existing canonical homes

These do not justify new books:

| Addition | Canonical home | Boundary |
| --- | --- | --- |
| Province corpses, visibility and corpse-dependent actions | Book II | Keep special orders procedural in Book X and spell records in the database. |
| Victory-time score-graph reveal in 6.35 | Book VI | One version-labelled correction. |
| Teleport movement out of besieged forts in 6.35 | Book VI | Add the exception without duplicating hosting timing. |
| AI preservation of important mages in 6.35 | Book VI | Record as a limited improvement, not a general competence claim. |
| Weather, age, unit-class and condition lookups | Unit and Ability Reference | Link combat consequences back to Book IV. |

Progress Edition 18 completes the bounded Book II corpse section and the three assigned Book VI 6.35 corrections. Book X now names the **L** pillage filter explicitly, while its existing score-reveal and teleport procedures remain procedural rather than duplicating Book VI strategy. The independent DE-Divinitus integrity publication closes R-002 through R-005 outside the encyclopedia and is represented here only by a Book IX cross-reference.

Progress Edition 19 completed the official-documentation pass for R-006, R-007, and R-015. Progress Edition 20 completes R-016: Book III now owns the blessing activation state model, automatic-blessing boundaries, repeatability and overlap rules, weapon-trigger families, item blessing, and rider/mount separation. Transformation lifetime and cross-source stacking remain in their separate research items rather than becoming duplicate chapters.

Progress Edition 21 returns to the Book II research cluster without creating another economy volume. R-009 is complete at its stated Official plus Community-tested tier: the ordinary pool is one base Commander Point plus the current fort bonus, multi-point costs accumulate, `#slowrec` changes cost rather than pool, and AI difficulty does not increase Commander Points or Holy Points. R-010 and R-013 advance to in-progress. Sacred-Slave stacking, mounted component upkeep, Need Not Eat, and the 6.18 non-eating transformation correction now have precise evidence boundaries; shapechanged upkeep, fractional aggregation, and generic commander feeding priority remain open. R-008, R-011, and R-012 remain queued because their available sources do not resolve the relevant integer or distance boundaries.

Progress Edition 22 returns to the Book III research cluster without creating another Pretender, dominion, or victory volume. R-017 is complete at a mixed evidence tier: official Holy, Disciple-game, Elegist, Recall God, Trinity, and timing rules now sit beside the published fixed 50-point base and effective-rating `-1/0/+1` contribution model, while detailed routing and return placement remain labelled Current Community Reference. R-018 is complete at Official plus Community-tested tier: later claimant death preserves a completed claim, unfortified conquest or a successful fort storm removes it before victory, and siege without fort conquest does not. R-014 remains queued because its older exploding-die model has not been reproduced under 6.36.

Progress Edition 23 makes the unresolved boundary group more usable without lowering the evidence bar. Book II now distinguishes every major rounding subsystem, records what the annual-upkeep samples exclude, supplies explicit candidate thresholds for the ambiguous unrest wording, separates agreed fort-supply rules from the disputed multiplier, and incorporates the 6.35 equipment-refresh correction. Book III traces the June 2026 republication of the awakening formula to pre-Dominions 6 notes and records the unresolved one-turn range discrepancy. R-008, R-011, R-012, and R-014 remain queued; R-010 and R-013 remain in progress.

Progress Edition 24 completes a full-corpus editorial pass across the Reader's Guide, field reference, and Books I-XIV. It changes the voice and sentence structure without changing the evidence. The exact headings, table rows, code blocks, links, inline code, and numeric tokens are checked against Edition 23. This makes future publication work a layout and retrieval task rather than another prose consolidation.

## Subjects that must not become new books

The following are already sufficiently owned:

- the anatomy of a turn;
- economy and the machinery of state;
- Pretender design, dominion, scales and blessings;
- armies, formations, scripting and battle resolution;
- research, communions, rituals, forging and late-game magic;
- exhaustive spell, item, summon, Pretender, Throne, site, mercenary, and special-dominion explanation in prose;
- general expansion, intelligence, logistics, war, sieges, diplomacy, Thrones and recovery;
- generic modding, event, map, AI and compatibility methods;
- the frozen DE 2.16 and Divinitus 1.15.3 DE technical layer.

New material on one of these subjects must either:

1. correct the existing canonical chapter;
2. provide a nation-, map-, object-, or ruleset-specific application;
3. add verified evidence to an unresolved research item; or
4. improve navigation without restating the explanation.

## Mandatory no-duplication gate

Before any future essay, chapter, dossier, or website page is drafted:

1. Search the Reader's Guide, subject index and content index for the proposed subject and its synonyms.
2. Identify the canonical owner from this audit.
3. Decide whether the proposed work is a correction, application, reference record, new procedure, or genuinely new system.
4. Write a one-paragraph delta statement describing what the new work adds that the owner does not already contain.
5. If no meaningful delta can be stated, create a cross-reference instead of new prose.
6. After drafting, run exact and semantic cross-document duplicate checks.
7. Update the coverage register, redirects and relevant research items before publication.

## Recommended next action

The broad shared foundations are in place. R-002 through R-009, R-015 through R-018, and R-031 are resolved at their stated evidence tiers. R-008 and R-010 through R-014 now have precise evidence gates and operational fallbacks; later corrections still belong in Books II or III rather than in another general volume. Questions lacking official or reproducible published evidence remain visible and do not block work elsewhere.

The next active phase is the website publication pass: searchable articles and indexes, reading routes, evidence and ruleset labels, stable links, and a source-to-export regeneration workflow. Object-layer and command-documentation edge cases follow where exact data exists. Nation dossiers remain planned work, not an active foundation gap.

## Source record

### Official sources

- [Illwinter's Dominions 6 documentation page](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Modding Manual](https://www.illwinter.com/dom6/dom6modman.pdf)
- [Dominions 6 Event Modding Manual](https://www.illwinter.com/dom6/dom6eventman.pdf)
- [Dominions 6 Map Making Manual](https://www.illwinter.com/dom6/dom6mapman.pdf)
- [Dominions 6 File Formats](https://www.illwinter.com/dom6/dom6fileformats.pdf)
- [Official Dominions 6 update announcements](https://steamcommunity.com/app/2511500/announcements/)

### Published community evidence used in Editions 22 and 23

- [Call God research notes](https://illwiki.com/dom5/user/loggy/callgod)
- [Current Dominions 6 Pretender reference](https://illwiki.com/dom5/dom6/pretender-god)
- [Current Dominions 6 Elegist reference](https://illwiki.com/dom5/dom6/elegist)
- [Current Dominions 6 Throne reference](https://illwiki.com/dom5/dom6/thrones)
- [Published same-turn Throne claim report](https://www.reddit.com/r/Dominions5/comments/pu0l7c/noob_questions_on_claiming_thrones/)
- [Legacy Pretender mechanics page](https://illwiki.com/dom5/pretenders), used only as a historical awakening test hypothesis
- [Current Dominions 6 Pretender-design page](https://illwiki.com/dom5/dom6/pretenders), used to audit the June 2026 republication of the awakening model
- [Loggy's miscellaneous reverse-engineering notes](https://illwiki.com/dom5/user/loggy/misc), used to trace that model's pre-Dominions 6 provenance
- [December 2025 upkeep observations](https://steamcommunity.com/app/2511500/discussions/0/691996377956257521/), used for annual-display and mounted-component boundaries
- [Current Dominions 6 unrest reference](https://illwiki.com/dom5/dom6/unrest), retained as a candidate formula without a 6.36 boundary reproduction
- [Current Dominions 6 supplies reference](https://illwiki.com/dom5/dom6/supplies), retained for feeding-priority terminology below an immunity claim

### Internal sources

- Progress Edition 24 reader corpus, Books I-XIV, field reference and Reader's Guide;
- `02-evidence-ledger.md`;
- `15-editorial-consolidation-audit.md`;
- `17-retrieval-publication-audit.md`;
- `website/research-register.json`;
- `website/base-object-register.json` and its schema;
- `website/official-patch-ledger.json` and its schema;
- `website/command-lexicon.json` and its schema;
- pinned 6.35 Dominions Data Inspector tables at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`;
- exact supplied DE 2.16 and Divinitus 1.15.3 DE source files.
