# Foundation Book XIII: Version History and the Official Patch Ledger

## Ruleset, purpose, and evidence boundary

This volume belongs to the unmodded Dominions 6.37 ruleset. Its historical range begins with the public 6.01 update of 19 January 2024 and ends with 6.37, released on 9 September 2026. Dominions Enhanced 2.16 and Divinitus 1.15.3 DE remain separate rulesets. Their changes are not folded into the official chronology, even where a mod later adopted or anticipated a similar rule.

The official announcements contain 1,096 individual change bullets across 33 named updates. Book XIII turns that material into two complementary resources:

- a readable account of how the live ruleset developed;
- `website/official-patch-ledger.json`, a machine-readable record of every official bullet, its release, source locator, source hash, editorial classification, affected domains, and canonical library destinations.

The ledger does not reproduce the full wording of the announcements. Each record identifies its official source and preserves a hash of the normalized source bullet. The public layer adds only a restrained summary and editorial metadata. This keeps the history verifiable without making the project a mirror of Illwinter's publication.

The source of record is the complete official Dominions 6 announcement feed exposed through Steam, checked against the [official announcement archive](https://steamcommunity.com/app/2511500/announcements/) and the [Illwinter Dominions 6 site](https://illwinter.com/). The [official documentation page](https://illwinter.com/dom6/docs.html) remains the authority for the main manual and the separate modding, event, map-making, and file-format manuals.

## The no-duplication delta

Earlier books own the rules themselves. Book I owns ruleset labels and hosting order. Books II through VI own economy, religion, combat, magic, and campaign conduct. Book VIII owns mod construction. Book X owns operation and hosting. Books XI and XII own ability and object lookup. Repeating those explanations release by release would make the library harder to maintain.

Book XIII owns a different question: **when did the current rule become current, what older statement did it displace, and which part of the library must be reviewed when it changes?**

This produces a firm editorial boundary:

- use Book XIII to establish chronology, provenance, and change impact;
- use the linked foundation book to understand the current mechanic;
- use the official announcement when exact source wording is necessary;
- use a historical executable or preserved save only when a past-version interaction itself is under study.

The patch ledger is therefore not a second combat guide, spell guide, or modding manual. It is the maintenance spine that tells every other guide when it may have become stale.

## What the ledger contains

| Measure | Current result | Meaning |
| --- | ---: | --- |
| Official update announcements | 33 | Every public announcement titled Dominions 6.01 through Dominions 6.37 in the official feed |
| Individual change records | 1,096 | One record for every bullet under General, Modding, Map Making, or a named national section |
| First dated release | 6.01, 19 January 2024 | The first public post-launch update in the feed |
| Current baseline | 6.37, 9 September 2026 | The version used by this edition |
| Public version numbers without a matching announcement | 4 | 6.10, 6.20, 6.22, and 6.26 |
| Distinct `#commands` named in update bullets | 221 | A chronology seed for the complete command lexicon planned after this book |
| 6.35 classification snapshot | 783 high, 26 medium, 255 review | Historical classifier totals retained until the complete 6.37 ledger is regenerated |

The four absent numbers are described only as **numbers without matching public announcements**. They are not called missing releases. A private build, skipped label, withdrawn build, or unannounced numbering decision cannot be distinguished from the public feed alone.

# Part I: Reading Versioned Rules

## 1. The current rule and its history are different facts

A current rules reference should normally state the rule that applies now. A version history should state how that rule arrived. Mixing the two produces avoidable ambiguity.

Consider regeneration. A current ability entry should explain how regeneration behaves in 6.37. The historical note that version 6.31 changed percentage regeneration from bracketed results to a more exact percentage calculation matters when evaluating an older guide, battle report, or saved test. It does not need to interrupt every ordinary explanation of regeneration.

The same separation applies throughout the library:

| Question | Proper home |
| --- | --- |
| What does this mechanic do in 6.37? | Its canonical foundation book |
| Which update changed it? | Book XIII and the patch ledger |
| What did the official announcement say? | The linked official update |
| How did it behave in a preserved older executable? | A version-labelled historical test |
| Does DE or Divinitus change it again? | Book IX or the later mod overlay |

This division keeps ordinary reading smooth while preserving enough history to repair old claims.

## 2. A version label has five parts

The phrase "current Dominions" is too weak for durable research. A useful version label contains:

1. **Game version.** Here the baseline is Dominions 6.37.
2. **Ruleset.** Vanilla, DE, Divinitus, or a named combined load order must be explicit.
3. **Manual revision.** The main manual and auxiliary manuals do not necessarily advance together.
4. **Data revision.** Extracted object data needs its own commit, date, or hash.
5. **Publication date.** The date distinguishes a genuinely current statement from an undated page that merely uses present tense.

A concise public label can read:

```text
Dominions 6.37, unmodded; official updates through 9 September 2026;
object data pinned separately; page reviewed 5 August 2026.
```

The full evidence record can then hold source hashes and tool versions without burdening the reader-facing sentence.

## 3. Patch notes are deltas, not replacement manuals

An update bullet usually assumes knowledge of the prior state. It may say that an effect now works during a siege, that a restriction was removed, or that a statistic was corrected. It rarely restates all eligibility rules, timing, exceptions, and downstream interactions.

Three consequences follow.

First, a patch bullet cannot safely be expanded beyond what it says. "Can now" proves a newly permitted case; it does not prove that every adjacent case works the same way. Second, a corrected bug can become part of ordinary current rules even when the old behaviour was never documented. Third, several bullets may jointly define the current state of one mechanic.

The editorial task is therefore a merge:

```text
current rule = surviving manual rule
             + later official deltas
             + current object data where appropriate
             - superseded or corrected statements
```

The terms in that expression do not have equal authority. The manual and official updates are direct official evidence. Extracted data is version-pinned supporting evidence. A community test can resolve behaviour the documents do not expose, but its version and method must remain attached.

## 4. Four common patch-reading errors

### 4.1 Treating a bug as a permanent rule

An old battle report may accurately show what an earlier executable did. If the behaviour was later fixed, the report remains historical evidence but ceases to be a current rule source. The distinction is especially important for communions, mounted units, shape changes, retreat, remote rituals, and blessings, all of which received repeated corrections.

### 4.2 Treating a wording change as a mechanical change

Presentation, tooltip, message, and statistics-display corrections may reveal the rule more clearly without changing resolution. A revised icon is not automatically a revised ability. Conversely, a display correction may expose a mechanical value that had always been active. The ledger therefore separates presentation, interface, data correction, rule change, balance change, and bug fix.

### 4.3 Treating an added command as a fully documented command

An announcement can establish that a mod command exists. It does not necessarily provide its complete syntax, selection context, legal values, copying behaviour, clearing behaviour, or error handling. Those belong in the current Modding Manual and the future command lexicon.

### 4.4 Treating a missing number as a missing source

The public sequence skips 6.10, 6.20, 6.22, and 6.26. Nothing in the feed establishes why. The correct statement is narrow: no official announcement with any of those four titles appears in the complete app-news response used for this edition.

## 5. Which old claims deserve immediate review

A patch does not make every old guide equally unsafe. The highest review priority belongs to claims that determine legality, access, irreversible resource spending, survival, or multiplayer administration.

| Review priority | Claim type | Typical consequence of being stale |
| --- | --- | --- |
| Critical | Order legality, host validation, save integrity, exploit prevention | Failed turn, rejected order, corrupted workflow, unfair game state |
| High | Spell access, ritual targeting, communion behaviour, retreat, transformation, siege permissions | Lost mage, wasted gems, failed operation, destroyed army |
| High | Bless cost or activation, Pretender status, recruitment restriction | Invalid design or roster plan |
| Medium | Unit cost, item effect, Throne effect, site output | Mispriced strategy or inaccurate comparison |
| Medium | Interface shortcut, message, filter, overview | Avoidable operational friction |
| Low | Sprite, sound, typo, graphical effect | Little or no strategic error unless identity is obscured |

This priority order controls the maintenance queue. It does not claim that a low-priority correction is unimportant to the quality of the game; it means the correction is less likely to invalidate strategic advice.

# Part II: The Complete Official Release Spine

## 6. Release density and what it reveals

The update history is front-loaded. Twenty-one announcements and 774 of the 1,096 recorded changes appeared in 2024. Eight announcements and 222 changes appeared in 2025. Four updates in 2026 contribute the remaining 100 changes through the present baseline.

| Calendar year | Announcements | Change records | Share of all records |
| ---: | ---: | ---: | ---: |
| 2024 | 21 | 774 | 70.6% |
| 2025 | 8 | 222 | 20.3% |
| 2026 through 9 September | 4 | 100 | 9.1% |

This is not a measure of importance. A short later update can change a central rule. It does show why undated launch-era guides require careful repair: most of the public delta history accumulated during the first year.

## 7. The 2024 release sequence

| Version | Date | Records | Historical profile |
| --- | --- | ---: | --- |
| 6.01 | 19 Jan | 33 | First balance and correctness pass; global-enchantment attacks were detached from NAP restrictions, and several roster and transformation problems were corrected. |
| 6.02 | 24 Jan | 29 | Research and object corrections, hosting work, and the rule that dormant gods do not age while dormant. |
| 6.03 | 25 Jan | 17 | Siege and NAP interaction, AI diplomacy, lobby research, and repeatable `#natcom` and `#natmon` use. |
| 6.04 | 2 Feb | 60 | Broad bug-fix release with blessing, event, AI, hidden-map, national recruitment, and mod-command additions. |
| 6.05 | 9 Feb | 41 | Combat-fatigue and lasting-HP corrections, recruitment fixes, resource-information privacy, prophet recovery, and hosting stability. |
| 6.06 | 11 Feb | 6 | Small hotfix led by coastal-fort recruitment and network correction. |
| 6.07 | 16 Feb | 35 | Lobby reversion to setup, siege-cast remote ritual repair, broader scale modding, and ammunition-fatigue mod support. |
| 6.08 | 6 Mar | 102 | Largest announcement in the ledger: major Asphodel revision, extensive rules and UI repair, many commands, and important changes to Twiceborn, passive blessings, Fear and Dread, empowerment, and site searching. |
| 6.09 | 12 Mar | 18 | Focused fixes to movement abilities, summons, items, networking, and mod commands. |
| 6.11 | 20 Mar | 24 | Manikin and object work, roster corrections, and additions including `#hidedom`. |
| 6.12 | 29 Apr | 89 | LA Pyrene, a large rules pass over disciples, communions, remote rituals, map targets, transformations, events, and modding. |
| 6.13 | 15 May | 52 | Besieged-fort teleport targets, random preaching order, NAP siege movement, major experience changes, interface work, and new event/global commands. |
| 6.14 | 16 May | 5 | Immediate correction release, including experience-related hit-point statistics. |
| 6.15 | 29 May | 33 | Grand Communion, victory-graph handling, illusion and false-damage rules, communion gem correction, and event-variable expansion. |
| 6.16 | 18 Jun | 29 | Fort-ritual repair, mercenary-screen operation, settlement and transformation work, plus map and event modding fixes. |
| 6.17 | 20 Jun | 3 | Settings compatibility, vanilla gem-longevity default correction, and lobby connection tracking. |
| 6.18 | 9 Jul | 24 | Undying healing, starvation removal after non-eating transformation, underwater and multiplane-map work, and defensive file handling. |
| 6.19 | 26 Aug | 38 | Afflicted-mount reclaiming, blessing and item fixes, underwater cases, and notable event, fort, ritual, and nation commands. |
| 6.21 | 10 Oct | 26 | Income-overview improvements, siege and mount fixes, lobby retention policy, rebirth behaviour, cave growth, and map-editor repair. |
| 6.23 | 3 Dec | 53 | A substantial balance and rules pass touching Fear, Dread, Asphodel, mounts, communions, events, research requirements, and terrain-linked recruitment. |
| 6.24 | 17 Dec | 57 | Ind, new Thrones and a spell, combat and ritual restrictions, order copying, large-file networking, terrain recruitment, and a broad mod-command set. |

## 8. The 2025 release sequence

| Version | Date | Records | Historical profile |
| --- | --- | ---: | --- |
| 6.25 | 15 Jan | 29 | Praise, Pillar of Truths, battle-version display, indoor battlefield-wide spell restrictions, temperature display, and mount and bless corrections. |
| 6.27 | 7 Mar | 42 | Seven new Thrones, treasury autosort, disease-spell resistance, Haunted Forest and Utterdark revision, ritual target validation, AI work, and new battle-summon commands. |
| 6.28 | 8 Mar | 4 | Hotfix for Call God, event-producing rituals, map item spells, and scripted AI priority. |
| 6.29 | 22 Apr | 47 | Planar ritual boundaries, order copying with `0`, allied-territory waiting, large-battle performance, communion backlash, AI ritual improvements, and many mod commands. |
| 6.30 | 6 Oct | 53 | LA Zemaitia, Fay additions, lab-to-commander gem shortcuts, new Pretenders, many combat and movement corrections, larger network turns, and ritual-loop detection. |
| 6.31 | 20 Oct | 19 | Exact percentage regeneration, longer wall enchantments, higher bless-effect limit, faster hosting, underwater Creeping Doom, and mounted/event fixes. |
| 6.32 | 13 Nov | 10 | Mounted gateway crash fix, secondary-shape Soul Slay, remote Blood Vengeance loot restriction, Farstrike targeting, and `#forcess`. |
| 6.33 | 16 Dec | 18 | Faster map rendering, cheat detection, barding and yearning fixes, AoE explanations, several unit corrections, and `#homerealm`. |

## 9. The 2026 release sequence

| Version | Date | Records | Historical profile |
| --- | --- | ---: | --- |
| 6.34 | 27 Feb | 44 | Fay summons and Pretenders, ritual-message and ability-icon work, AI corrections, automatic summons during siege, rebirth healing, security repair, and performance improvements. |
| 6.35 | 18 May | 24 | Gnu content and the Throne of Violence, script resumption for innate casters, victory reveal behaviour, teleport movement from besieged forts, interface additions, mount recovery, and integrity fixes. |
| 6.36 | 17 Aug | 26 | Movement, Rust, Blood Sacrifice ordering, mounts, interface and replay corrections, plus five event-modding command additions. |
| 6.37 | 9 Sep | 6 | Level-nine research access, drowning for non-commanders, Drake breath timing, game-switch memory use, anti-cheat work, and unspecified stat and typo corrections. |

### 9.1 Dominions 6.37 maintenance impact

The [official Dominions 6.37 announcement](https://store.steampowered.com/news/app/2511500/view/717915822014595135) describes six General changes. Three have direct rules-facing consequences: some level-nine spells had been impossible to research, drowning did not always affect non-commanders, and Drakes recovered too quickly after using a breath weapon in melee. The announcement also records a memory-leak fix when switching games, anti-cheat improvements, and unspecified statistic and typo corrections.

The patch establishes the corrected categories but does not name the affected level-nine spells, define every drowning trigger, quantify the corrected Drake delay, or identify the objects covered by the generic statistic note. Those details remain unresolved rather than being inferred. The release names no mod commands, so the 226-token command reconciliation remains unchanged; the executable baseline advances to 6.37 while the live Modding Manual remains version 6.36 and the structured object snapshot remains pinned to 6.35.

## 10. The absent public numbers

No matching official announcement was present for 6.10, 6.20, 6.22, or 6.26. The ledger preserves that fact in `scope.unannounced_version_numbers`. These labels are intentionally excluded from the release table and from any inferred chronology.

A future source may explain one or more gaps. If that happens, the correction should add the source and revise the scope note. It should not silently manufacture release dates or change bullets from forum recollection.

# Part III: The Classification and Evidence Model

## 11. One official bullet becomes one patch record

Every source bullet receives a stable record ID. `patch-6-35-015`, for example, identifies the fifteenth bullet in the normalized 6.35 announcement sequence. A record contains:

- version and publication date;
- official section and bullet index;
- source announcement identity and URL;
- SHA-256 of the source bullet and of the normalized record;
- editorial change class and confidence;
- affected domains;
- direction and materiality;
- named `#commands`, terms, and object mentions where detected;
- canonical destinations elsewhere in the library;
- a concise impact summary that does not reproduce the source text.

The ID is a publication key, not an official Illwinter identifier. The official source identity remains separate.

## 12. The fourteen change classes

| Class | Records | Share | Editorial meaning |
| --- | ---: | ---: | --- |
| Bug fix | 234 | 22.0% | A stated malfunction or inconsistency was corrected. |
| Rule or permission change | 193 | 18.1% | Legality, timing, targeting, immunity, or behaviour changed. |
| Balance adjustment | 177 | 16.6% | Cost, strength, chance, quantity, or comparative value changed. |
| Modding behaviour change | 113 | 10.6% | Existing mod or parser behaviour changed or was repaired. |
| Mod-command addition | 81 | 7.6% | One or more new `#commands` were announced. |
| Interface or quality of life | 68 | 6.4% | A screen, shortcut, display, filter, or workflow changed. |
| Performance or stability | 43 | 4.0% | Speed, memory, crash resistance, or hosting stability improved. |
| Artificial intelligence | 40 | 3.8% | Strategic or spellcasting AI behaviour changed. |
| Network or hosting | 36 | 3.4% | Lobby, server, connection, transfer, or turn-file behaviour changed. |
| Data correction | 30 | 2.8% | Statistics, text-linked data, or object records were corrected. |
| Content addition | 21 | 2.0% | A named nation, unit, spell, item, Throne, Pretender, or similar object was added. |
| Presentation | 18 | 1.7% | Graphics, sound, animation, text rendering, or appearance changed. |
| Security or integrity | 8 | 0.8% | Cheat detection, exploit handling, validation, or corrupted-data handling changed. |
| Map-making change | 2 | 0.2% | A map-making-only change was identified outside broader modding treatment. |

These are navigation classes, not official headings. A single bullet can reasonably touch several ideas. The record stores one primary class to keep filters usable, then adds multiple affected domains.

## 13. Domain tags are many-to-many

A remote ritual that crosses planes, targets a besieged fort, spends gems, and moves an army may touch magic, movement, maps, hosting order, and interface messaging at once. Forcing it into one subject would hide the cross-system risk.

The most frequently tagged domains are:

| Domain | Records carrying the tag | Canonical interpretation home |
| --- | ---: | --- |
| Modding | 195 | Book VIII |
| Magic and spells | 171 | Book V and Book XII records |
| Maps and scenarios | 158 | Book VIII |
| General game objects | 156 | Book XII |
| Combat | 146 | Book IV |
| Summons and transformations | 115 | Books V, XI, and XII |
| Operations and interface | 89 | Book X |
| Presentation | 69 | Book XIII maintenance layer |
| Hosting and network | 67 | Book X |
| Items and artifacts | 67 | Books V and XII |
| Events | 66 | Book VIII |
| Nations and rosters | 57 | Book VII dossier system |
| Movement and logistics | 53 | Book VI |
| Units, abilities, and conditions | 53 | Book XI |
| Dominion and blessings | 49 | Book III |

Domain totals exceed 1,096 because one record can affect several domains. That overlap is a feature: it identifies which books and website records must be reviewed together.

## 14. Classification confidence is not source confidence

All 1,096 source bullets are official. The uncertainty concerns only the project's derived labels.

| Label | Records | Meaning |
| --- | ---: | --- |
| High | 783 | Wording contains a strong signal such as "fixed," "new," "now," a command, an AI reference, or an explicit interface term. |
| Medium | 26 | The broad family is probable, but wording is less diagnostic. |
| Editorial review | 255 | Source identity is settled; the fine-grained class should be checked before relying on it as an analytic statistic. |

The review queue does not make the ledger incomplete. Every official bullet has an identity, source, hash, release, domain route, and public locator. The queue limits how confidently the automatically assigned category may be used.

An editorial correction changes the classification and record hash. It does not alter the source hash. This makes interpretation changes visible without pretending that the official announcement changed.

## 15. Materiality is contextual

The automated materiality field uses three coarse levels: major, notable, and maintenance. It is only a triage aid.

A one-line change to retreat legality can decide a multiplayer game. A new nation is obviously major content but may have no effect on a match where that nation is absent. A crash fix is critical to hosts running the affected setup and irrelevant to everyone else. Consequently, publication pages should combine materiality with domain, object identity, and reader task.

The strongest practical filter is often:

```text
version range + domain + current canonical page + player-facing status
```

This finds changes that can invalidate a specific page without claiming a universal rank.

# Part IV: Player-Facing Changes That Commonly Make Guides Stale

## 16. Economy, recruitment, and provincial state

Most economic formulas were stable enough to remain in Book II, but several surrounding permissions and displays changed.

### 16.1 Information and privacy

Version 6.05 stopped players from seeing resources already used inside another player's fort. This is an information rule, not an income formula. Old advice that assumes direct inspection of an enemy production queue is therefore unsafe.

Version 6.21 made the income overview easier to audit, including colour coding and the display of zero-upkeep units. Version 6.18 corrected the omission of national income bonuses from Thrones in that overview. These changes affect diagnosis: a modern screen can reveal costs or bonuses that an older screenshot does not show.

### 16.2 Recruitment geography

Coastal-fort recruitment received corrections in 6.05 and 6.06. Later releases adjusted foreign recruitment in caves, reef-warrior availability, cave Province Defence, terrain-linked national recruitment, and underwater fort defence. A roster claim must therefore state both nation and terrain context.

### 16.3 Borders and traced income

Version 6.30 stopped income from being traced through impassable borders. This is strategically important on unusual maps and multiple-plane layouts. Book II owns the current economic interpretation; Book XIII establishes when older connectivity assumptions became stale.

### 16.4 Population and events

Version 6.24 corrected a possible population overflow and made Conscription depend on the Order scale. Version 6.30 stopped Bringer of Fortune from producing events while under siege. These are narrow changes with wide planning consequences: scale value, siege economy, and event engines cannot be evaluated from launch-era behaviour alone.

## 17. Pretenders, dominion, disciples, and blessings

### 17.1 Dormancy and divine continuity

Version 6.02 established that gods do not age while dormant. Version 6.28 repaired Call God when invoked without the shortcut. Several releases corrected Pretender age, prophet replacement, resurrection, Twiceborn, Life after Death, and shape-related divine status.

The lesson is not that divine recovery is unreliable. It is that old demonstrations need their version attached, particularly where immortality, shape changes, mercenary status, or underwater laboratories are involved.

### 17.2 Passive and incarnate blessings

Version 6.04 changed Reconstruction from passive behaviour. Version 6.08 corrected the treatment of passive blessings outside friendly dominion: Pretenders no longer lost those passive effects merely by leaving dominion. Several releases repaired the displayed incarnate status or omitted bless effects.

A blessing page needs three independent checks:

1. design legality and cost;
2. activation rule in the current version;
3. whether the interface correctly displays the active effect.

An interface omission is not proof that the effect is absent, and a displayed icon is not proof that every edge case resolves correctly.

### 17.3 Fear, Dread, and overlapping effects

Version 6.08 stopped Fear and Dread from stacking with each other. Version 6.23 revised their bless costs and capped the morale reduction attributable to Fear by the effect's value, with an upper limit stated in the announcement. This is a classic stale-guide trap: cost, stacking, and combat outcome changed at different times.

### 17.4 Experience and heroic value

Version 6.08 reduced the experience gain from the Heroism blessing. Version 6.13 added rare heroic abilities, limited battle-participation experience to once per month, granted Magic Resistance at five stars, and granted additional hit points at three stars and beyond. Version 6.14 immediately corrected related hit-point statistics.

Book XI owns the current experience and heroic reference. The patch history explains why older tables may disagree.

### 17.5 Disciples and religious state

Version 6.12 allowed diplomacy to continue through the first disciple when the Pretender was dead. Version 6.13 preserved dominion and ascension graphs while disciples remained alive. Version 6.24 allowed Pretender Throne sensing to reveal the site for disciples. Version 6.34 increased the maximum number of teams in disciple games.

These are multiplayer-state rules, not merely UI conveniences. Disciple guides should be reviewed whenever team, death, diplomacy, graph, or Throne rules change.

## 18. Combat, fatigue, morale, and retreat

### 18.1 Fatigue delivery

Version 6.05 stopped a ranged weapon with a fatigue cost from adding the user's encumbrance to that cost. Version 6.15 corrected cases where communions consumed too many gems to reduce fatigue. Later releases corrected fatigue from flight, trampling, Earthquake, and scripted communion casting.

The practical danger is false arithmetic. An old calculator can be internally consistent and still model a superseded rule.

### 18.2 Lasting hit-point loss and equipment

Version 6.05 stopped never-healing wounds and similar maximum-hit-point reductions from reducing hit points supplied by armour. Version 6.16 repaired Undying interactions with the Shroud of the Battle Saint. Version 6.34 corrected shields against certain weapon blessings. These changes sit at the boundary between unit body, equipment, blessing, and damage resolution; all relevant layers must be checked together.

### 18.3 Illusions, false damage, and spirit forms

Version 6.15 allowed false damage to cause an HP rout and prohibited illusions from casting Phoenix Pyre. Version 6.30 repaired illusions harming one another, changed how spirit-form states interact with bleed, frozen, and burning effects, and corrected illusions disappearing at battle start. Older shorthand such as "false damage is harmless" or "ethereal is the relevant tag" is too crude for current play.

### 18.4 Morale and Fear

Fear's current cap arrived in 6.23. Version 6.27 stopped mindless units from receiving false damage when repelled. Version 6.30 made gods and prophets unable to fail the retreat morale roll. These are different layers: resistance to morale effects, repel consequences, and the retreat check should not be collapsed into one immunity claim.

### 18.5 Indoor and terrain restrictions

Version 6.25 prohibited battlefield-wide spells indoors, except Holy spells. Version 6.31 allowed Creeping Doom underwater. Every spell package that depends on cave, indoor, underwater, or planar context should therefore include terrain legality in addition to research and path access.

## 19. Magic, communions, rituals, and global enchantments

### 19.1 Communions changed repeatedly

Communion-related deltas appear throughout the history:

- version 6.12 removed the communion-slave effect when a unit was thrown out of a communion;
- version 6.15 introduced Grand Communion and corrected excessive gem use in some fatigue-reduction cases;
- version 6.16 repaired missing Grand Communion ability entries on certain heroes;
- version 6.23 improved AI handling of multiple communion types;
- version 6.27 made `#aibadlvl` communion-aware;
- version 6.29 repaired communion backlash;
- version 6.30 corrected conservative-gem communion masters failing to attempt higher-level spells.

A communion guide without a version is therefore hazardous even when its basic path-boosting explanation remains sound.

### 19.2 Remote rituals and targets

Version 6.07 repaired several remote attacks cast from a besieged fort. Version 6.12 stopped gem expenditure when a commander was the target of a remote attack ritual. Version 6.13 allowed teleport items and gems to target besieged forts. Version 6.27 added ritual host-target validation. Version 6.29 blocked most rituals from tracing across void and non-void planar boundaries. Version 6.32 changed Farstrike-style targeting toward the largest enemy army in a province.

Each change affects a different part of a remote operation:

| Layer | Question |
| --- | --- |
| Origin legality | Can the caster act from the current province or siege state? |
| Path and cost | Can the caster meet the requirements and pay? |
| Route | Can the effect cross the relevant plane or boundary? |
| Destination legality | Is the target province valid? |
| Target selection | Which army, unit, or object is selected inside it? |
| Host validation | Will the order survive final processing? |
| Message and evidence | What report proves success, interception, or failure? |

This checklist is more durable than memorising one patch sentence.

### 19.3 Global enchantments and layered counters

Version 6.01 separated global-enchantment attacks from NAP restrictions. Version 6.27 revised Utterdark and Haunted Forest. Version 6.30 allowed Arcane Decree to block Astral Disruption completely and allowed Sea of Ice to coexist with nexus-gate use. Version 6.34 stated that domes may protect against Astral Disruption and corrected Eternal Twilight's effect on resources.

Global strategy is consequently both political and versioned. A guide must distinguish the enchantment's current rule, the counters available in the same version, and the diplomacy settings of the match.

### 19.4 Rebirth and secondary forms

Version 6.12 stopped Life after Death commanders from becoming feebleminded in the corrected case. Version 6.24 prohibited Ritual of Rebirth on spirit-form beings. Version 6.27 made Lichcraft remove an existing Twiceborn enchantment. Version 6.32 made Soul Slay kill units with secondary shapes properly. Version 6.34 made Ritual of Rebirth remove most afflictions.

The current state cannot be derived from one of those bullets alone. Book V explains the access and strategic uses, Book XI explains the relevant conditions and forms, Book XII identifies the objects, and Book XIII supplies the chronological merge.

## 20. Movement, mounts, sieges, and planes

Mounted systems were among the most frequently corrected cross-object mechanics. The history includes sacred mounts, rider-bless interaction, floating mounts, afflicted mount recovery, siege retreat, unique event mounts, barding slots, gateway crashes, remount orders, and automatic recovery.

### 20.1 Siege exits and entries

Version 6.13 allowed certain teleport targets inside besieged forts and made it legal to move an army into NAP-protected forces besieging the mover's fort. Version 6.35 allowed commanders with teleport movement to leave a besieged fort. These statements are not interchangeable. Targeting a fort, entering a siege, and moving out of one are separate permissions.

### 20.2 Planar boundaries

Version 6.08 prevented return from the Void from placing a unit inside a cave wall. Version 6.12 stopped province-granting wishes from selecting empty cave-wall provinces. Version 6.29 restricted ritual tracing across void and non-void boundaries. Version 6.30 corrected global attacks against cave-wall provinces.

Multiple-plane maps turn topology into a rule layer. An apparent adjacency or province identity does not guarantee a legal magical route.

### 20.3 Mount recovery

Version 6.19 allowed commanders to reclaim afflicted mounts. Version 6.21 repaired mounts retreating after fort defence. Version 6.30 corrected a reclaim order that could cause fall damage. Version 6.35 made mount return automatic at the end of the turn in the applicable case. Book I owns the end-of-turn timing; Book XI owns mounted identities; Book XIII shows why older manual procedures may now be unnecessary or wrong.

## 21. Interface and operating changes

Interface changes are strategically important when they reduce error rates.

Notable additions include:

- lobby reversion to setup in 6.07;
- colour-coded income review and zero-upkeep visibility in 6.21;
- copying and pasting army-position orders in 6.24;
- treasury autosort in 6.27;
- universal order copy/paste with the `0` key in 6.29;
- direct laboratory-to-commander gem transfers and repeated bless selection in 6.30;
- area-of-effect explanations in 6.33;
- the F1 pillage filter and related operational improvements in 6.35.

These belong in Book X as current procedure. Their history remains here so an older screenshot or tutorial can be interpreted correctly.

## 22. Hosting, networking, security, and integrity

The official history records repeated work on lobby connections, game retention, map upload and download, large turn files, large-game hosting speed, corrupt files, illegal orders, exploit prevention, and cheat detection.

A fair hosting standard should therefore require:

1. an agreed executable version;
2. exact mod versions and load order;
3. a preserved setup sheet;
4. turn and save backups appropriate to the hosting method;
5. a documented response to version changes during a running game;
6. use of current validation rather than a claim that an old exploit is still possible;
7. a distinction between a client display problem and a host-resolution problem.

Version 6.24 repaired handling for turn files above an earlier network threshold. Version 6.30 further improved larger turn-file handling. Versions 6.33 and 6.34 added integrity and exploit corrections. A host diagnosing an old report should begin with version and file size before treating it as a current rules dispute.

## 23. Artificial intelligence changes

Forty records were classified primarily as AI changes, with additional AI-relevant records under modding and other domains. They address siege behaviour, blood hunting, bless selection, gem preparation, research, preaching, ritual laboratories, dispels, Arcane Analysis, communion types, range buffs, target selection, and many spell preferences.

The correct conclusion is limited. The AI is not a static opponent, and old difficulty reviews may describe obsolete priorities. The patch notes do not establish that the AI now plans like an expert human. They establish particular improvements or corrections.

AI claims should use one of three forms:

| Claim form | Evidence needed |
| --- | --- |
| Capability | Official bullet or current repeatable observation that the AI can perform the action |
| Preference | Versioned behavioural sample large enough to distinguish a tendency |
| Competence | A clearly defined task and comparative benchmark, not an impression from one game |

This keeps official improvements from being inflated into unsupported strategic promises.

# Part V: Modding and Command Chronology

## 24. Why patch history is indispensable to modders

The auxiliary manuals are versioned documents. The update stream can add a command, repair its parser, extend legal arguments, change an object limit, or alter runtime behaviour before the next manual revision is available.

Across the 31 announcements, 221 distinct `#commands` are named. Some bullets announce several commands at once; some commands appear again because their behaviour was later extended or fixed. The chronology answers three questions that a static manual cannot answer alone:

1. When did this command enter the public ruleset?
2. Was it later repaired or extended?
3. Which manual baseline is old enough that the command may be absent?

It does not answer the complete syntax question. That is the purpose of the next structured foundation, the command lexicon.

## 25. Command families visible in the update stream

The official bullets span most major modding surfaces.

| Family | Representative chronology |
| --- | --- |
| National recruitment and terrain | Forest, coast, sea, deep, kelp, plain, cave, scale-linked fort, and non-capital fort recruitment commands accumulated across multiple releases. |
| Monsters, mounts, and shapes | Bug shapes, battle summons, barding and rider behaviour, forced secondary shapes, realms, tolerance, Fay summoning, and reclaim-related systems expanded over time. |
| Spells and rituals | AI modifiers, indoor restrictions, home realms, size and Twiceborn costs, mass teleport effects, new target controls, and ritual safety checks were added or changed. |
| Events | Research and path requirements, realm requirements, fort identities, nation-number variables, optional sites, unit variables, and repeated variable operations expanded the event language. |
| Items and weapons | Defence and morale rolls, Fay summoning, Praise, unseen status, ammunition-fatigue behaviour, protection parts, and new effect controls appeared in the chronology. |
| Maps and sites | Site copying, multiplane repair, terrain validation, gates, province insertion, and source-target realm controls developed alongside the map editor. |
| AI templates | Bless compatibility, research goals, communion-aware bad-spell ratings, and spell-assessment controls received explicit attention. |

These descriptions are deliberately family-level. Exact command names, selectors, arguments, defaults, clearing semantics, version introduced, version changed, and minimal examples belong in the future lexicon.

## 26. The command-lexicon record required next

Each command should eventually receive a record containing:

| Field | Purpose |
| --- | --- |
| Command | Exact `#name` |
| Current manual | Manual and revision in which it is documented |
| Selection context | Nation, monster, weapon, armour, spell, item, site, event, map, or general scope |
| Arguments | Count, types, ranges, sentinel values, and defaults |
| Repeatability | Whether repeated use appends, replaces, toggles, or errors |
| Copy and clear behaviour | Interaction with `#copy`, inherited values, and clear commands |
| Introduced | Earliest official update or manual in the evidence set |
| Changed | Later updates that repaired or extended it |
| Example | Minimal valid source block |
| Failure mode | Common parser or runtime mistake |
| Evidence | Official manual page, update source, and any bounded reproduction |

The patch ledger already supplies introduced-or-mentioned candidates and official URLs. The lexicon must add manual parsing and context, not duplicate the whole patch history.

## 27. Safe treatment of post-manual commands

When an update introduces a command that is absent from the locally pinned manual, the public entry should state:

- that existence is official from the update;
- that syntax is documented only to the extent supported by current official material;
- that any additional example is derived from inspected source or a controlled test;
- that older game versions may reject the command;
- that a mod using it should declare a minimum Dominions version.

This avoids a common failure in mod guides: copying a working example and presenting every inferred argument as official syntax.

# Part VI: Repairing Stale Guides and Maintaining the Library

## 28. The stale-guide repair workflow

The repair process begins with a claim, not with a whole document.

1. **Extract the claim.** Reduce the sentence to its subject, rule, value, and conditions.
2. **Pin the guide's date or version.** If neither is available, mark the claim undated.
3. **Search the ledger forward.** Filter from the guide's probable version through 6.37 by domain, named term, command, and canonical page.
4. **Open every plausible official source.** A classification hit is a lead, not proof that the claim changed.
5. **Merge the deltas in order.** Later official changes supersede earlier ones where they address the same state.
6. **Check the current canonical book.** Confirm that the library's ordinary explanation matches the resulting rule.
7. **Check current object data.** Use Book XII when the claim includes an ID, cost, path, statistic, or roster relation.
8. **Preserve uncertainty.** If the surviving rule is still incomplete, add or update a research-register item.
9. **Record the repair.** Store old claim, new claim, source release, affected pages, and review date.

This is slower than changing every sentence containing a keyword. It is much faster than allowing contradictory rules to accumulate.

## 29. A worked repair pattern: regeneration

Suppose an older guide describes regeneration through hit-point brackets and claims that a one-hit-point boundary can sharply increase the amount restored.

The repair trace is:

1. subject: regeneration calculation;
2. old source: guide predating October 2025;
3. ledger hit: version 6.31;
4. official delta: regeneration became accurate to the percentage value rather than the older bracket behaviour;
5. canonical home: Book XI's ability reference, with combat consequences in Book IV;
6. update: replace the bracket claim in current prose, retain a short version note where an older test is discussed;
7. dependent records: unit and item comparisons relying on boundary exploitation require recalculation.

The patch note supplies the transition. It does not by itself supply every rounding detail. If exact rounding remains unverified, that question stays explicit.

## 30. A worked repair pattern: besieged-fort teleportation

An old guide might state broadly that teleportation cannot interact with a besieged fort.

The chronological repair finds at least two distinct deltas:

- version 6.13 allowed teleport items and gems to target besieged forts;
- version 6.35 allowed commanders with teleport movement to move out of besieged forts.

The old sentence is too broad. The current replacement must distinguish targeting into the fort from teleport movement out of it. Book VI receives the operational rule; Book I supplies hosting context; Book XIII preserves both dates.

## 31. A worked repair pattern: communions

A communion guide written at launch may remain correct about path boosting but wrong about slave removal, gem conservation, Grand Communions, backlash, AI casting, or item support.

The correct repair is modular:

| Subclaim | Relevant releases |
| --- | --- |
| Removal from communion | 6.12 |
| Grand Communion existence | 6.15 |
| Excessive gem spending correction | 6.15 |
| Missing hero ability | 6.16 |
| AI confusion between communion types | 6.23 |
| Communion-aware `#aibadlvl` | 6.27 |
| Backlash correction | 6.29 |
| Conservative-gem master casting | 6.30 |

Each subclaim is updated in its own canonical paragraph. The guide does not need an eight-entry patch diary in the middle of the teaching sequence.

## 32. Dependency-driven maintenance

Every patch record carries canonical section IDs. These create a reverse index from change to affected publication area.

```text
official update
    -> patch records
        -> domains and object mentions
            -> canonical book sections
                -> website pages and dossier imports
```

When a new update arrives, the maintenance process should produce:

- added, changed, and removed patch records;
- affected domains;
- affected object IDs where resolvable;
- canonical pages requiring review;
- unresolved classifications;
- newly named commands for the lexicon;
- a publication note describing what was actually revised.

This is the central reason to preserve hashes. A future import can prove which records are unchanged and direct human attention to the real delta.

## 33. Updating the official feed safely

The importer at `tools/build_official_patch_ledger.py` can rebuild the data layer from a saved official Steam news response or the current endpoint. A safe update follows this sequence:

1. preserve the previous JSON and its hash;
2. retrieve the complete official feed;
3. identify official update announcements by exact title pattern;
4. parse sectioned list bullets without importing comments or marketing articles;
5. compare announcement identities, dates, source hashes, and record counts;
6. fail closed if an older source unexpectedly disappears or changes;
7. classify new records and place uncertain labels in review;
8. validate the JSON against its schema;
9. review canonical links and command mentions;
10. publish the new ledger only with a matching game-baseline update.

The importer must assert the known 6.37 completeness totals. Those assertions must be intentionally revised for a later baseline; bypassing them would remove the main guard against a partial feed.

## 34. Website uses

The public website can expose the ledger through several views without reproducing patch prose.

### 34.1 Release page

Show date, record count, class distribution, leading domains, and a link to the official announcement. Records can be grouped by source section and linked to canonical current pages.

### 34.2 Topic history

For a subject such as communions, retreat, mounts, or Thrones, show a chronological list of matching records with concise summaries and official locators. The current-rule page remains visually primary.

### 34.3 Stale-page warning

If a library page has not been reviewed after a later matching patch record, display a maintenance flag. The warning should say that review is due, not that the page is necessarily wrong.

### 34.4 Version comparison

Given two public versions, list intervening records by domain and class. This is a delta list, not a simulation of the older executable.

### 34.5 Command chronology

Expose commands named by each release and link them to the future lexicon. The patch record proves mention; the lexicon supplies syntax.

## 35. Publication cautions

The website should not:

- present editorial classifications as official categories;
- claim that absent public numbers are missing releases;
- display a hash as though it proves mechanical correctness;
- turn a one-line official delta into an invented complete rule;
- silently merge vanilla and modded histories;
- mark an old page wrong merely because a related record exists;
- reproduce the complete patch-note wording;
- hide review-recommended classifications from maintainers.

# Part VII: Essays on Versioned Knowledge

## Essay I: A Rule Without a Version Is Not a Complete Rule

Dominions invites timeless language. Armour reduces damage. Communions raise paths. A besieged fort restricts movement. Regeneration restores hit points. Such statements sound like permanent laws because they describe systems rather than content.

In a living strategy game, however, even a durable system has a date. The underlying idea may survive while its boundary cases move. Regeneration can keep its name and strategic purpose while its calculation changes. Communions can remain communions while the removal of a slave, gem use, backlash, and AI handling are corrected over several releases. Teleportation can remain teleportation while its permissions around besieged forts expand in separate directions.

Versioning is not a scholarly ornament attached after the real work. It is part of the rule's conditions. A statement about Fire 3 already contains a threshold. A statement about a cave already contains terrain. A statement about 6.37 contains time.

This does not mean that every sentence needs a parenthetical patch number. Good writing keeps the current rule readable and places chronology where it resolves a real ambiguity. The version belongs in the page baseline, the evidence record, and any sentence that would otherwise conflict with a still-circulating older claim.

The most dangerous unversioned statements are not always obscure formulas. They are confident operational rules: an order is impossible, a ritual always spends a gem, a unit cannot retreat, a blessing remains passive, a target cannot be reached. Players build turns around categorical claims. When a patch changes one, the old sentence becomes more harmful than a missing statistic.

A versioned library therefore behaves differently from a conventional guide. It preserves stable current teaching, but every claim has a route back to evidence and forward to maintenance. It treats an official change as a dependency event. It distinguishes the history of a rule from the rule now in force. It can say both "this is how 6.37 works" and "this older report was accurate when written" without forcing one to erase the other.

That is the deeper value of a patch ledger. It is not a museum of old notes. It is the mechanism that lets knowledge remain current without losing its memory.

## Essay II: Bug Fixes Are Strategic History

Balance changes attract attention because their intent is visible. A unit becomes cheaper. A blessing becomes more expensive. A new Throne appears. Strategy writers naturally discuss the altered comparison.

Bug fixes are easier to dismiss as housekeeping. That is a mistake. A bug can define the apparent rule for every player who encountered it. If a communion failed to apply backlash, an item effect survived removal, a remote ritual selected the wrong target, or a mount behaved incorrectly during retreat, players adapted to the behaviour whether or not it was intended.

Once fixed, the behaviour acquires two identities. Historically, it was an observable property of the earlier version. Currently, it is a rejected state. Both facts matter. The first explains old reports and established habits. The second governs new play.

This makes bug fixes strategically significant in three ways.

First, they invalidate empirical knowledge. A careful test can become obsolete without ever having been poorly designed. Version must therefore travel with the result.

Second, they change risk. An interaction that once failed intermittently may become dependable; an exploit that once offered an advantage may become illegal or detectable; a crash-prone operation may become safe enough for ordinary use.

Third, they reveal system boundaries. Repeated fixes around mounts, shapes, communions, besieged forts, and planes show where several object models meet. Those areas deserve stronger test matrices and more cautious prose, not because the engine is unknowable, but because a one-object explanation is insufficient.

The correct editorial response is not to preserve every bug in the current chapter. It is to keep the ordinary rule clean, link consequential history, and retain the old behaviour only when it explains a source conflict or a still-common misconception.

Bug fixes are therefore strategic history: records of what players could rely on, what they learned to fear, and what later ceased to be true.

## Essay III: Maintenance Is Part of Authorship

A large strategy library can fail while every individual essay remains elegant. The failure occurs when pages stop sharing a baseline. A combat article uses launch behaviour, a nation dossier imports a current unit cost, a modding example requires a later command, and a hosting guide assumes an earlier file limit. Each page may sound reasonable. Together they describe no game that ever existed.

Maintenance solves this by treating the library as a dependency system. Canonical books own explanations. Structured registers own identities and deltas. Dossiers apply the common rules. A patch does not trigger a general rewrite; it triggers a bounded review of affected dependencies.

This approach also improves prose. A chapter no longer needs defensive repetitions of every exception. It can rely on stable cross-references and a visible baseline. Historical detail moves to the patch layer. Exact object fields move to the object register. The main argument becomes easier to read because maintenance architecture carries the bookkeeping.

Authorship in such a system includes deciding what not to repeat, recording uncertainty, and making future correction inexpensive. A finished paragraph is not the endpoint. The endpoint is a paragraph that can be found, tested, revised, and propagated when its evidence changes.

# Part VIII: Practical Reference

## 36. Reader's patch-check routine

When an old guide or discussion appears to conflict with the current library:

1. record the guide's date, stated version, ruleset, and mods;
2. isolate the disputed claim;
3. search the patch ledger from that version onward;
4. read the linked official announcements;
5. check the current canonical book;
6. check current object data where the claim is numerical;
7. treat unresolved behaviour as a research question rather than a vote between authors.

## 37. Author's pre-publication version audit

- Is the game version visible?
- Are mods and load order visible?
- Is the manual revision appropriate to the claim?
- Have later official updates been searched?
- Is an old empirical test tied to its executable version?
- Are object values tied to a pinned data revision?
- Does each rule have one canonical explanatory home?
- Are historical deltas kept out of ordinary prose unless they resolve confusion?
- Are editorial classifications described as editorial?
- Are unresolved cases linked to the research register?

## 38. Host's mid-game update decision

Before changing executable version during a multiplayer game, record:

| Question | Why it matters |
| --- | --- |
| Does the update change order legality or hosting? | Existing turns or procedures may resolve differently. |
| Does it change a nation, spell, item, bless, or Throne present in the game? | Competitive value may shift unevenly. |
| Does it repair an exploit or integrity problem? | Remaining on the old version may be riskier than updating. |
| Does it alter mods or command support? | The active mod set may fail or behave differently. |
| Are all players able to update and verify the same files? | Mixed clients undermine reproducibility. |
| Is a rollback path preserved? | A failed migration should not destroy the campaign. |

The decision belongs to the game's agreed administration. The patch ledger supplies the relevant delta; it does not impose a social rule on the group.

## 39. Maintainer's new-release checklist

1. Archive the new official announcement and retrieval metadata.
2. Rebuild the ledger and confirm the prior 1,096 records remain stable unless an official source changed.
3. Validate every new record and release against the schema.
4. Review all new `#commands` against current manuals.
5. Resolve named objects against the base object register.
6. Review canonical pages reached by the new domain tags.
7. Run duplicate and voice checks on revised prose.
8. Rebuild website indexes, redirects, coverage, and research registers.
9. Rebuild and visually inspect the PDF.
10. Publish a bounded change note: what changed, what was reviewed, and what remains open.

## 40. Source and verification record

| Source | Role in this volume | Evidence status |
| --- | --- | --- |
| [Official Steam announcement archive](https://steamcommunity.com/app/2511500/announcements/) | Public release chronology and official change bullets | Official |
| [Illwinter Dominions 6 site](https://illwinter.com/) | Current game-update confirmation and publisher identity | Official |
| [Official Dominions 6 documentation](https://illwinter.com/dom6/docs.html) | Main and auxiliary manual baselines | Official |
| Steam app-news response archived for this edition | Complete machine-readable announcement feed and source hashes | Official feed, locally preserved |
| `website/official-patch-ledger.json` | Derived record identities, classifications, domains, commands, and links | Official source with editorial derivation |
| `website/official-patch-ledger.schema.json` | Publication and validation contract | Project schema |
| `tools/build_official_patch_ledger.py` | Reproducible import and completeness assertions | Project method |

## 41. Explicit limitations

The current release closes the official-feed collection gap, but it does not claim more than the sources permit.

- The ledger records public announcements, not undocumented internal builds.
- The four absent public numbers are not assigned invented dates or content.
- The full official bullet text is not republished in the public JSON.
- Two hundred fifty-five fine-grained classifications remain marked for editorial review; source identity and completeness are unaffected.
- Command mention does not equal complete command documentation.
- Patch notes do not replace controlled tests for mechanics they leave unspecified.
- Historical behaviour is not reconstructed without the matching executable or a preserved reproduction.
- Vanilla history is not silently merged with DE, Divinitus, or any other mod.

## What this unlocks

Book XIII completes the first full official version spine for the library. Every public update announcement through 6.37 is represented, every official bullet has a stable record and source locator, every record routes toward a canonical foundation, and the current ruleset can now be checked against the history that produced it.

The next foundation should be the command lexicon. The patch ledger already identifies 221 distinct named commands and the releases that introduced, changed, or repaired them. The Modding Manual supplies syntax and context. The two sources can now be reconciled command by command without repeating Book VIII's design guidance or Book XIII's chronology.
