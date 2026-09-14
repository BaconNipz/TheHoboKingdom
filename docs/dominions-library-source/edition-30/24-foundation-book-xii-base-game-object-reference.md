# Foundation Book XII: Base-Game Objects and the Searchable Reference Layer

## Ruleset, purpose, and evidence boundary

Book XII contains the unmodded Dominions 6 structured object snapshot pinned to version 6.35. The live rules baseline is 6.36, with its official announcement overlaid in the canonical books and patch ledger. A 6.36 object export has not replaced the auditable Inspector commit used here. Dominions Enhanced 2.16 and Divinitus 1.15.3 DE are kept out of these records. Their exact source inventories remain in Book IX and can later be applied as overlays against the vanilla identities established here.

Book XII fills a different gap from the earlier foundation books. Books II-VI explain economy, religion, armies, magic, and campaign judgement. Book XI explains how to read units and abilities. None of them should become a thousand-page inventory of object cards, so the work is divided clearly:

- Book XII explains how to interpret, compare, verify, and maintain object records;
- `website/base-object-register.json` owns the filterable records;
- `website/base-object-register.schema.json` defines the publication contract;
- the earlier books retain the full rules and strategic consequences;
- nation dossiers will import shared objects by stable identity instead of researching them again.

The baseline data comes from the public Dominions 6 Data Inspector at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, dated 26 May 2026 and labelled by its maintainer as an update to 6.35. The Inspector is an extremely useful community extraction, but it is not an official rules document and its own documentation warns that errors may remain. A field drawn from it is labelled **source-confirmed**, not **official**. Statements from the official manuals receive the higher official label. Derived classifications, such as grouping a spell under remote attack or tagging a site as a Throne from its source rarity code, remain visibly derived even when the underlying values are source-confirmed.

The register does not reproduce the game's long descriptions or artwork. It records names, identities, mechanical fields, relationships, provenance, evidence status, canonical links, and stable hashes. This makes it useful for search and comparison without turning the website into an unattributed mirror of the game text.

## The no-duplication delta

Book V already explains research, casting, rituals, global enchantments, forging, path access, gems, communions, and late-game magic. Book III owns Pretender design, dominion, scales, blessings, and divine continuity. Book VI owns strategic use of Thrones and mercenaries. Book XI owns the interpretation of unit abilities. The present volume does not replace any of those chapters.

Its new contribution is retrieval. It establishes stable object identities, versioned source lineage, cross-object relationships, filter fields, incomplete-data markers, and maintenance rules. A reader looking up *what an object is* should arrive here or at the register. A reader asking *why and when it matters* should follow the canonical link to the earlier foundation book.

## What the first register contains

| Record family | Current records | What is represented |
| --- | ---: | --- |
| Spells | 1,474 | All extracted spell rows, including 1,233 researchable or Divine rows and 241 unresearchable or internal rows |
| Magic items | 529 | Ordinary forgeable items, Construction 9 artifacts, barding, and special or engine-managed items |
| Summon relations | 549 | Spell-to-unit or spell-to-selection-group relationships, including chained effects |
| Pretender forms | 298 | Base forms with national availability, body statistics, paths, discounts, and shape links |
| Thrones | 74 | Thirty-six level-one, twenty-six level-two, and twelve level-three Thrones |
| Other magic sites | 1,179 | Random, capital, national, event, and other non-Throne sites |
| Mercenary companies | 78 | Company, leader, troop, era, starting strength, minimum bid, experience, and recovery fields |
| Independent recruitment | 1 coverage marker | The missing population-type relation is documented without inventing an exhaustive catalogue |
| Special dominions | 14 | Official system families from the manual, linked to every applicable nation and age |

These 4,196 records are not all equally player-facing. Internal spell rows, engine-managed items, and unresolved selection groups are retained because removing them would make version comparisons unreliable. Website defaults should hide such records from a beginner search while keeping them available to researchers and modders.

# Part I: The Object-Reference Method

## 1. An object is an identity, not merely a name

Dominions contains many repeated names. Several forms may share a display name; different items may occupy the same apparent category; a spell may chain into a second hidden spell; a Pretender may transform into another monster record. Names are presentation fields, not primary keys.

Every record begins with three different identities:

- a stable publication ID such as `spell-0200` or `pretender-0109`;
- the engine-facing numeric ID supplied by the extracted data;
- the current display name.

The publication ID supplies durable website links. The engine ID allows comparison with mod commands, inspector entries, debug output, and later patch exports. The name remains essential for readers, but a rename does not have to break links or confuse a changed record with an entirely new one.

For a national guide, this distinction is decisive. A dossier may say that a nation can choose Dagon, but the underlying reference should point to Pretender form 109. If a later patch changes the name or statistics of that form, one object record changes and every dossier importing it receives the corrected fact.

## 2. Ruleset identity belongs inside every record

A record without a ruleset is unsafe. The same visible object can have different requirements, statistics, or secondary effects under vanilla play, Dominions Enhanced, Divinitus, another balance mod, or a different load order.

The first register uses one ruleset label throughout:

```text
vanilla-6.35
```

Modded records will not overwrite that layer. They should later be expressed as additions, replacements, or field-level deltas with their own load-order identity. This preserves a clean answer to three different questions:

1. What does the object do in unmodded 6.35?
2. What does a named mod change?
3. What is the final value after the frozen mod order is applied?

Conflating those questions is one of the fastest ways to make an encyclopedia sound certain while returning the wrong rule.

## 3. Evidence status belongs beside the field

The register currently uses four public evidence states.

| Status | Meaning | Proper use |
| --- | --- | --- |
| Official | Directly supported by current official documentation | Special-dominion rules and manual classifications |
| Source-confirmed | Present in the pinned 6.35 extracted game data | IDs, names, requirements, statistics, site fields, and roster relations |
| Source-confirmed with unresolved selection | The effect is identified but the engine chooses from a group that is not completely resolved | Certain negative-tag or engine-selected summons |
| Test-pending | Available sources cannot support a complete current-version claim | Independent population-type recruitment |

Source-confirmed does not mean infallible. It means that the value can be reproduced from a named source revision. A contentious value should still be checked against the 6.36 interface, a later official patch statement, or a second current extraction before it becomes the basis of a precise public claim.

## 4. Record hashes make silent change visible

Each record receives a SHA-256 hash calculated from its normalized fields. The hash is not a gameplay fact. It is an editorial control.

When a future source is imported, unchanged hashes identify stable records. Changed hashes identify objects requiring review. Added and removed IDs identify content changes. This permits a patch audit to concentrate on actual deltas instead of rereading thousands of cards.

A good update report can answer:

- which records changed;
- which fields changed;
- whether the change is official, extracted, or merely a new interpretation;
- which book sections and nation dossiers depend on those records;
- whether a website cache or search index must be rebuilt.

## 5. Raw fields and interpreted fields serve different readers

The register preserves selected source-native fields under names such as `mechanical_properties` and `extra_attributes`. These are valuable to researchers, but they are not always readable or fully decoded. The same record also carries interpreted fields such as `spell_kind`, `role_tags`, `throne_level`, `tier_class`, or a list of named national restrictions.

The two layers must remain separate. A raw field records what the source said. An interpreted field records what the publication concluded. When an interpretation changes, the source record should not be rewritten to match the conclusion.

## 6. A ninety-second lookup routine

A beginner need not read every field. Most practical lookups can follow the same order:

1. Confirm the ruleset and version.
2. Confirm the object type and engine ID.
3. Read its access fields: school, path, Construction level, nation, site, or era.
4. Read its cost and delivery fields.
5. Read the principal effect or relationship.
6. Open the canonical chapter for strategic consequences.
7. Check evidence status before relying on an edge case.

This order prevents two common mistakes: judging an object before confirming that the nation can access it, and treating a concise database field as though it contained the entire game rule.

## 7. The expert audit routine

An expert or editor should add five checks:

1. Inspect the engine ID and any chained or shaped identities.
2. Review source revision and file hash.
3. Distinguish explicit values from derived tags.
4. Compare unresolved attributes against the Modding Manual and current UI.
5. Record any correction as a new claim or revision, never as an undocumented overwrite.

The result is slower than reading a tooltip but much faster than rebuilding the same evidence for every guide.

# Part II: Spells

## 8. Spell rows and player-facing spells are not the same thing

The source contains 1,474 spell rows. Of these, 1,233 belong to a research school or Divine magic and 241 are marked unresearchable or internal. Internal rows can represent helper effects, hidden chains, scenario functions, or other engine work. They should not appear in an ordinary player's search results unless an advanced filter requests them.

The register gives every spell a `public_status`:

- `researchable-or-divine` for schools zero through seven;
- `unresearchable-or-internal` for school minus one.

This is a visibility classification, not a guarantee that every public row is generically available to every nation. National restrictions, realm restrictions, unique casters, and special access still apply.

## 9. School and research level

School numbers are translated into the current names used by the game:

| Source code | School |
| ---: | --- |
| 0 | Conjuration |
| 1 | Alteration |
| 2 | Evocation |
| 3 | Construction |
| 4 | Enchantment |
| 5 | Thaumaturgy |
| 6 | Blood |
| 7 | Divine |
| -1 | Unresearchable |

Research level is preserved separately. A level is not a complete access statement. The real access question combines school level, path requirements, cost, caster availability, national restriction, and sometimes a source or destination condition.

Fifty-nine public rows are flagged at research level nine. The flag supports the game's legendary-spell research option and gives the website a direct filter for the final research tier. Book V remains the canonical home for late-game research planning.

## 10. Path requirements are thresholds

Each spell record contains zero, one, or two path requirements. A requirement such as Fire 3 means that the caster must reach that threshold at the moment of casting. It does not identify how the threshold is reached.

The access chain may include:

- innate paths;
- communion or sabbath levels;
- path boosters;
- temporary gems;
- empowerment;
- a site bonus;
- a national or Pretender-only caster;
- a transformation or shape with different magic.

Those mechanisms belong to Book V. The record supplies the threshold that the access analysis must meet.

## 11. Combat spell, ritual, and delivery context

The spell kind is derived from the attached effect record. A ritual and a combat spell can share superficially similar purposes while competing for entirely different resources and timing windows.

A spell record keeps:

- ritual status;
- fatigue cost as extracted;
- gem or slave cost as extracted;
- precision modifier;
- effect count;
- base and per-level range fields;
- base and per-level area fields;
- battlefield percentage where present;
- duration and modifier masks;
- province range attributes where exposed.

Several of these are source-native values rather than finished player prose. A website card should render the common cases clearly but preserve the raw value in an advanced panel. It should not guess how an unfamiliar mask is displayed.

## 12. Effects, roles, and the danger of one-label summaries

An effect record supplies an effect number and an extracted effect name. The register also adds restrained role tags, including:

- summon;
- damage or disable;
- buff or restoration;
- control;
- dispel;
- remote attack;
- remote assassination;
- strategic movement;
- site search;
- fort construction;
- transformation;
- enchantment;
- province enchantment.

These tags are search aids, not complete tactical judgments. A damaging spell may also create a cloud. A summon may be a battlefield screen, a path break, a raider, or a source of new recruitment. A global enchantment may primarily function as diplomacy rather than raw economy. The canonical chapter should receive the interpretive burden.

## 13. Chained spells

Some visible spells lead to another spell row through `next_spell`. The second row may hold an additional effect, a terrain-specific branch, or a helper operation. Searching only the first row can miss a summon or secondary consequence.

The importer follows each chain until it ends or repeats. Summon relationships are collected across the chain and attached to the visible root. The hidden rows remain independently addressable, making later patch comparisons possible.

A chain should be read as a graph:

```text
visible spell -> effect row -> optional next spell -> optional further effect
```

The graph also explains why name-based scraping is unreliable. The second row may have an internal name that is never shown to a player.

## 14. National and realm restrictions

The extracted spell-attribute table identifies explicit national restrictions. The register resolves those numeric values into nation name and age where possible. A public website should display the restriction near the spell name rather than burying it below the effect.

Realm access is now resolved through the same versioned chain used by the Inspector. The Modding Manual supplies the ten official realm names and states that a realm-restricted spell belongs to nations with the matching home realm. The pinned nation attributes supply those home realms, while the Inspector's spell logic confirms that realm matches are added to explicit national access.

Six spells use realm restrictions in the 6.35 snapshot. Their North, Africa, or India requirements expand into ninety realm-to-nation links. Each record keeps the raw realm number, official realm name, eligible nations, explicit national entries, and their combined allowed list. This is an access relation, not a claim that every nation in a cultural region belongs to the realm; only the extracted `#homerealm` values count.

## 15. Cost fields are not an efficiency verdict

Gem or slave cost is recorded because it is an access fact. It is not enough to rank spells. Efficiency also depends on:

- mage-turn cost;
- research timing;
- caster scarcity;
- battlefield survival;
- expected targets;
- repeatability;
- opportunity cost against forging, empowerment, or another ritual;
- whether the effect creates a reusable asset;
- whether the spell reveals strategic information.

Book V explains those conversions. The database should make them calculable without pretending that one universal score can replace the campaign state.

## 16. Useful spell queries

Beginner searches should ask one concrete question at a time:

- all public spells in a chosen school and level;
- all spells requiring no more than a nation's current path ceiling;
- all battle buffs for a known army problem;
- all rituals that produce a commander;
- all site-search spells by path;
- all spells marked national for the selected nation.

Expert searches can combine access and role:

- remote attacks that meet a precise province range;
- battlefield-wide effects with a gem cost;
- summons that produce commanders with new paths;
- level-nine spells changed since the previous source revision;
- spells whose effect number or modifier mask remains undecoded;
- visible spells whose hidden chain changed while the root row did not.

# Part III: Magic Items, Artifacts, and Barding

## 17. Item identity and slot type

The first register contains 529 item records. Each one has a numeric ID, current name, slot type, Construction level, path requirements, attached weapon or armour ID where applicable, and a sparse set of mechanical properties.

Slot types include one-handed and two-handed weapons, missile weapons, shields, armour, helmets or crowns, boots, miscellaneous items, and barding. The slot is an equipment constraint, not a promise that every unit with an apparent body part can wear the object. Unit item slots, mount rules, minimum size, minimum strength, hand requirements, crown restrictions, and other item properties can still veto use.

Book XI owns the body and equipment-reading method. Book V owns forging and booster planning.

## 18. The Construction ladder and special records

The source uses the visible odd-numbered Construction tiers. The current distribution is:

| Construction level | Records | Register classification |
| ---: | ---: | --- |
| 1, 3, 5, or 7 | 378 | Ordinary forgeable |
| 9 | 118 | Unique artifact |
| 11, 13, or 15 | 33 | Special or engine-managed |

The official manual identifies Construction 9 items as artifacts. Values above the ordinary ladder are retained as source facts but are not presented as ordinary forgeable tiers. They include special prizes and engine-managed objects whose acquisition rules must be learned from the relevant event, spell, or scenario.

## 19. Requirements and actual forge access

An item may list one or two path requirements. Those are necessary thresholds, not a complete forge plan. A nation still needs:

- an eligible commander with appropriate item slots and magic;
- the required Construction research;
- sufficient gems;
- any national or unit restriction to be satisfied;
- freedom from an artifact uniqueness conflict;
- a mage-turn that is worth spending.

The database intentionally does not fabricate forge costs from path levels. Explicit UI or engine-export costs should be added as their own fields when a reliable current source is available.

## 20. Mechanical properties

Item properties are sparse: only non-empty source fields are retained. This prevents hundreds of meaningless zeroes while preserving unusual effects. Common fields include:

- resistances and reinvigoration;
- path boosts and path-range increases;
- temporary gems or gem generation;
- leadership, research, supply, patrol, siege, and forging bonuses;
- flight, sailing, water breathing, stealth, or map movement;
- regeneration, luck, etherealness, quickness, or defensive skins;
- start-of-battle spells, automatic spells, and item rituals;
- bearer restrictions and minimum body requirements;
- transformations, afflictions, curses, or insanity costs;
- national rebates and special acquisition rules.

A raw property name is not automatically safe prose. Edition 25 compares every item and site property used by the register with the pinned Inspector display tables. It supplies readable labels for all 233 item fields and 78 site-or-Throne fields. Of these, 221 item labels and 74 site labels reproduce the source interface wording. The remaining twelve item labels and four site labels are restrained editorial expansions, kept separate with a derived badge. Raw keys remain beside every label, so a readable filter never replaces the source field.

## 21. Boosters as access edges

The most strategically important item searches often concern path access rather than combat equipment. A booster can turn a caster into a node in a larger access graph:

```text
native path -> first booster -> higher booster or summon -> ritual threshold
```

The item record provides the requirement and mechanical boost. A separate access calculator can then join it to national mage probabilities, summoned commanders, sites, and empowerment. That calculator should never assume that owning the gems is equivalent to owning the mage-turns or keeping the bearer alive.

## 22. Artifacts as a world-state race

Artifacts are unique. Their value includes denial, timing, and information. A static item score cannot capture the fact that another nation may forge the object first, that a holder may be killed, or that an artifact may begin yearning under the game's artifact rules.

The register marks artifact identity but leaves artifact-race doctrine in Book V. A future campaign tool can add availability state without modifying the underlying object record:

- uncreated;
- yearning;
- forged by a known nation;
- forged, holder unknown;
- recovered;
- destroyed or otherwise unavailable.

That state belongs to a specific game, not to the base object.

## 23. Comparing equipment packages

Items should rarely be compared in isolation. The relevant unit, opponent, and battlefield create the package.

A reliable comparison asks:

1. Can the intended bearer equip every piece?
2. Which defence is weakest before equipment?
3. Does the package solve fatigue as well as protection?
4. Does it preserve movement and script reliability?
5. Does it answer the expected damage types and control effects?
6. What is lost if the bearer dies?
7. Would the same gems produce more value as research access, summons, or army support?

The database supplies the object fields. Book IV owns the combat derivation.

# Part IV: Summons

## 24. A summon record is a relationship

A summon is not adequately represented by a spell row or a unit row alone. It is the relationship between them.

Each summon relation currently records:

- the root spell ID and name;
- every directly resolved target unit;
- named selection groups for random, unique, or terrain-dependent results;
- unresolved engine selections;
- the extracted effect count;
- evidence status and source revision.

The target units continue to belong to the unit layer. Their abilities should be read through Book XI, and their battle performance through Book IV.

## 25. Direct, unique, terrain, and tag-based summons

The importer recognizes several broad forms.

| Form | Meaning | Record treatment |
| --- | --- | --- |
| Direct unit | Effect points to a positive unit ID | Unit ID and name are resolved |
| Direct commander | Effect identifies a commander summon | Commander ID and name are resolved |
| Unique group | One of a finite named group can answer | Every known candidate is listed |
| Terrain group | Result depends on terrain-specific table | Every known candidate is listed under the terrain group |
| Chained summon | A later spell row supplies an additional summon | Relation is attached to the root and chain retained |
| Negative monster tag | Engine chooses from a tagged group | Raw selector is retained and marked unresolved unless the current table is known |

The first build had twenty-five selection-based relations without a complete explanation. Edition 25 resolves one through the Inspector's fixed Dwarf table and names the monster-tag selector for eighteen more. These include Longdead, Soulless, Random Bug, Random Animal, Ghoul, Lesser Horror, and Horror. The pinned export still does not expose their complete weighted unit membership, so it records the selector without inventing candidate odds. Six relations remain genuinely unresolved: five use raw selector `-26` and one uses `-18`, neither of which appears in the pinned monster-tag or fixed-summon tables.

## 26. Quantity and scaling

The source carries an extracted effect count, but exact quantity can also depend on caster level, special effect rules, random selection, terrain, or a chained effect. The first register preserves the raw count and target relationship without converting every case into a prose formula.

A later verified quantity layer should distinguish:

- fixed base quantity;
- additional units per full path level;
- fractional scaling and rounding;
- commander plus retinue;
- one result selected from a unique pool;
- a variable or random composition;
- temporary battlefield summons;
- permanent strategic summons.

These are separate fields because a single number cannot describe them safely.

## 27. Summoned units as access and logistics

Summon evaluation begins with role, not statistics alone. Common roles include:

- path extension;
- site searching;
- forging access;
- leadership for magic, undead, or animals;
- siege mass;
- patrol strength;
- raiding and remote presence;
- sacred or bless-compatible force generation;
- amphibious or flying logistics;
- battlefield disruption;
- durable line combat;
- expendable screening.

The database can filter the result set by unit properties. The strategic conclusion still depends on a nation's shortages and timetable.

## 28. Unique summons are contested resources

Elemental royalty, Demon Lords, and other unique beings are not ordinary repeatable outputs. Their availability depends on what has already been summoned and, in some cases, what has died or returned.

The base register lists the candidate pool. A live-game overlay should track availability as mutable state. The object record should never be altered merely because one campaign has already consumed the unique target.

## 29. Shape graphs after summoning

A summoned commander may transform on land, underwater, in battle, on death, or through an activated ability. Looking only at the first form can conceal magic paths, item slots, movement permissions, or vulnerabilities.

The proper lookup follows shape links until the graph closes. Book XI explains shape-sensitive ability reading. The current Pretender records expose their major shape links; a later general unit graph should extend the same treatment to every summoned form.

# Part V: Pretender Forms

## 30. Form records and design records

The register contains 298 Pretender forms derived from national availability, home-realm membership, explicit additions, and explicit removals in the pinned data. A form record is not a finished Pretender build. It is the chassis before design choices are applied.

The record includes:

- body statistics;
- starting dominion;
- cost for a new path where extracted;
- innate magic;
- random-magic source fields if present;
- equipment IDs and body properties;
- minimum imprisonment source field where present;
- availability by nation and age;
- nation-specific cheap-god adjustments;
- major shape relationships.

Book III remains the authoritative guide to design points, awakening, scales, blessings, and role construction.

## 31. Availability is a relation, not a chassis property

Dagon is not an abstract underwater Pretender. It is available to a particular set of nations. Another chassis may be supplied by a home realm, removed from one nation, or discounted for a small family.

The database stores availability as a list of nation records. This makes several questions directly searchable:

- every chassis available to a selected nation;
- every nation that can choose a selected chassis;
- chassis shared across all ages of one cultural line;
- chassis that disappear or appear between ages;
- national discounts on an otherwise shared form.

This relation will prevent future dossiers from repeating a complete chassis inventory in prose.

## 32. Starting dominion and path cost are only the opening geometry

Starting dominion affects the design-point curve and the chassis's relationship with dominion strength. New-path cost affects the marginal price of diversification. Neither value determines the best build on its own.

A complete design must still price:

- awakening state;
- desired blessing thresholds;
- scales and national economic interaction;
- expansion reliability;
- research and forging access;
- the risk of chassis death;
- whether the chassis must be mobile, stealthy, amphibious, or present on the battlefield;
- whether special dominion systems reward stronger candles.

The record supplies the immutable chassis facts. Book III supplies the engineering method.

## 33. Innate paths, purchased paths, and shape changes

Innate paths belong to the current form. Purchased paths belong to the designed god. Shape changes can alter the body and may change how paths or equipment are used. The reference keeps innate paths and shape links separate.

When a chassis has multiple forms, the design audit should inspect:

- which form appears on the strategic map;
- which form fights;
- whether items remain equipped;
- whether a form is aquatic or land-capable;
- whether protection, regeneration, or movement changes;
- whether death or transformation is reversible.

No single thumbnail can carry this information safely.

## 34. Cheap-god relations

Some nations receive a twenty- or forty-point adjustment for named chassis. These discounts are stored as nation relations on the chassis record, not baked into a universal chassis cost.

This matters because the same form can be ordinary for one nation and economically distinctive for another. A website Pretender planner should apply the discount only after nation selection and should display its source rather than silently changing the price.

## 35. Useful Pretender queries

Beginner filters:

- all chassis available to the selected nation;
- awake candidates with a desired body type;
- immobile candidates;
- chassis beginning with a required magic path;
- chassis capable of operating underwater.

Expert filters:

- national discounts combined with path-cost breakpoints;
- chassis whose shape graph changes equipment access;
- chassis shared by likely opponents;
- forms with a special dominion interaction;
- version deltas in availability or innate paths;
- designs whose required path thresholds can be met by fewer purchased levels.

# Part VI: Thrones and Magic Sites

## 36. Thrones are sites with victory meaning

The extracted site table marks Thrones with rarity codes eleven, twelve, and thirteen. The register interprets these as Throne levels one, two, and three. The first build contains:

- 36 level-one Thrones;
- 26 level-two Thrones;
- 12 level-three Thrones.

They are removed from the ordinary site array and placed in their own Throne collection, so a website search does not double-count them. Their site identity remains intact.

Book VI owns Throne strategy, claiming, endgame conversion, and Cataclysm. The register owns the exact Throne objects and their effects.

## 37. Claimed and unclaimed fields

Site data can distinguish ordinary gem income from income granted after a Throne is claimed. It can also contain recruitment, scales, dominion effects, ritual modifiers, strength or resistance effects, unrest, population, supply, and other province changes.

A Throne card should visually separate:

- presence before claiming;
- effect after claiming;
- units or commanders available at the site;
- province or dominion changes;
- strategic risks created by the effect.

The database preserves the source fields but does not infer ownership timing for every unusual attribute. Where the manual or UI is required, the card should carry a verification note.

## 38. Site classes

The non-Throne collection contains 1,179 sites. The first classification uses the source rarity code:

- codes zero, one, or two: random discoverable sites;
- code five: special, capital, national, or event-managed sites;
- any other non-Throne code: retained as other until verified.

This classification helps search but should not be mistaken for a complete generation formula. Map terrain, site frequency, age, national starts, events, and scenario design can all shape actual presence.

## 39. Search level and path

Random sites commonly expose a path and search difficulty. Those fields answer two separate questions:

- which path can find the site;
- what search strength is required.

Site-search spells, remote search, and manual searching interact with those facts through rules explained in Book V. A site record should never imply that a nation can exploit it merely because the site exists. Access may still require a laboratory, a fort, a priest, a commander with suitable leadership, or control of the province.

## 40. Location masks

The register decodes known location bits into readable terrain labels:

- plain;
- forest;
- mountain;
- waste;
- farm;
- sea;
- coast;
- swamp;
- deep sea;
- cave;
- underwater mountain;
- underwater forest;
- underwater coastal;
- unique.

The raw mask is retained beside the decoded list. If a later source adds a bit that is not yet understood, the raw value survives the import and the decoder can be extended without losing evidence.

## 41. Site income is not the whole site value

Gem income is the easiest site effect to compare, but it is often not the most important. Sites can provide:

- commanders or troops;
- path access;
- laboratories or forts;
- research or ritual modifiers;
- supply, resources, gold, or recruitment points;
- unrest, disease, horror, or population effects;
- province defence;
- dominion or scale changes;
- unique summons or adventures.

The value of a site depends on who owns it and whether the nation can exploit the granted access. The database makes the fields visible; Book II and Book V explain the economic and magical conversions.

## 42. Duplicate names and site identity

Several sites share a display name. An Academy of Magic in one path or terrain is not safely identified by name alone. Engine ID, path, location mask, and mechanical properties distinguish the records.

Website URLs should use stable IDs. Search results may group matching names for readability, but opening the card must reveal the numeric identity and distinguishing fields.

## 43. Throne comparison queries

Useful Throne searches include:

- all Thrones at the selected game level;
- claimed gem income by path;
- effects that change scales, unrest, population, or dominion;
- Thrones granting recruitable commanders;
- effects that alter ritual levels or Call God;
- Thrones whose effect can harm the owner as well as rivals;
- Throne records changed by a patch.

The query result is an intelligence aid, not a prediction of which Thrones the map generator selected.

# Part VII: Mercenaries and Independent Recruitment

## 44. Mercenary company records

The register contains 78 mercenary companies. Each record joins the company to current unit identities and retains:

- company and commander name;
- commander unit;
- troop unit;
- starting troop count;
- minimum surviving strength;
- minimum bid;
- starting experience;
- random and fixed equipment fields;
- recruitment recovery rate;
- era mask resolved to Early, Middle, and Late Age availability.

The minimum bid is not the expected winning bid. The strategic value depends on competition, timing, map position, morale, equipment, and the opportunity cost of gold. Book II owns the economic comparison and Book VI owns the tempo decision.

## 45. Mercenary attrition and continuity

A company is not equivalent to buying a permanent national production line. Losses, recovery rate, contract timing, and rebidding shape its value. The record preserves the source fields needed for that analysis.

A practical mercenary card should answer:

1. What does the company add immediately?
2. Which roles does the national roster lack?
3. How many casualties can the company sustain before it becomes strategically irrelevant?
4. Does the commander add a useful path, leadership type, or item?
5. Is the bid buying expansion tempo, emergency defence, siege mass, or denial?

## 46. Why independent recruitment remains a marked gap

Independent province recruitment is strategically important, but the pinned 6.35 Inspector extract does not expose a population-type membership table. It contains current unit records but cannot prove which units and commanders each independent population type makes recruitable.

Older community catalogues describe generic humans, tribes, Amazons, cave peoples, mages, and other independent families. Carrying those tables forward as though they were a complete 6.35 export would violate the project's evidence standard. The first register contains one coverage marker instead of a fabricated list.

The marker records:

- what is missing;
- why the available source cannot prove it;
- what reliable evidence would close the gap;
- where current unit statistics can be joined once membership is known.

This is unfinished work, but it is controlled unfinished work.

## 47. The acceptable route to a current independent catalogue

The gap can be closed by either:

- a version-matched engine export of population types and recruit lists; or
- a published 6.35 reproduction giving population type, terrain and age conditions, unit IDs, commander IDs, and a repeatable method.

Once available, the data should be stored as relationships:

```text
population type -> terrain and age conditions -> recruitable units and commanders
```

The units themselves should remain in the shared unit layer. Independent records should not copy their full statistics.

## 48. Evaluating independent access without a complete catalogue

Until the table is verified, campaign analysis can still evaluate a discovered province from the in-game recruitment panel. The useful questions are:

- Does the province repair a national weapon, armour, missile, leadership, or priest gap?
- Is the unit gold-, resource-, or recruitment-point efficient for that role?
- Does the province need a fort, temple, or laboratory before the key unit appears?
- Can production continue under likely unrest or siege pressure?
- Is the province strategically defensible enough to justify infrastructure?

The observation belongs to the current game. It should not be generalized into a universal population-type record without evidence.

# Part VIII: Special Dominion Systems

## 49. Why special dominions are database objects

Special dominions combine national identity with religious territory. They are neither ordinary unit abilities nor ordinary scale effects. The official manual gives them a dedicated section because they change what candles mean.

The register stores fourteen system families. Each record contains:

- a stable system identity;
- every applicable nation and age;
- a concise mechanical list paraphrased from the manual;
- the disciple inheritance rule;
- the official source locator;
- a canonical link to this volume and Book III.

Exact national strategy remains dossier work. The shared system should be written once.

## 50. Official system register

| System | Nations or ages | Core effect | Disciple boundary |
| --- | --- | --- | --- |
| Dominion scrying | Arcoscephale, all ages | Accurate reports inside dominion, including Glamour detection | Information is shared with disciples |
| Dying dominion | EA and LA Mictlan | Ordinary passive spread fails; blood sacrifice becomes central | Dying dominion does not transfer |
| Temple Oni | EA Yomi | Temples generate Oni according to Turmoil, terrain, and temperature | Does not transfer |
| Dreamlands | LA R'lyeh | Insanity, madmen, and Void Dreamer development | Extends into disciple lands with only partial protection |
| Ashen Empire | MA Ermor | Population death, undead arising, and corpse awareness | Applies to disciples |
| Carrion Woods | MA Asphodel | Population death and Carrion animation | Applies to disciples |
| Miasma | MA C'tis | Rain, disease, terrain change, and asymmetric income pressure | Disciples are treated mostly as enemies; sacreds are immune |
| Golem Cult | MA Agartha | Constructs gain Hit Points | Helps allied and enemy constructs inside the dominion |
| Additional blood sacrifice | Seventeen named nation-age entries | Blood sacrifice supplements ordinary dominion spread | Does not transfer, but an innately capable disciple keeps the order |
| Dark Ships | MA Phaeacia | Commanders sail when origin and destination have friendly dominion | Does not transfer; disciple-led Phaeacia still uses it |
| Spectral dominion | EA Therodos | Population decline and fort-generated ghosts | Applies in disciple games |
| Dominion conflict | EA Mekone | Maximum dominion counts one higher when suppressing enemy faith | No transferred rule stated in the manual |
| Dominion unrest | MA and LA Phlegra | Covered provinces gain unrest, increasing with local strength | Operates through disciples only when Phlegra is the Pretender nation |
| Concealed provinces | Ubar, Na'Ba, Ind, and Feminie | Hides ownership and name behind a false independent appearance | Disciples benefit |

## 51. Local strength, presence, and maximum dominion

Special systems depend on different religious variables. They must not be described with the vague phrase “stronger dominion helps” unless the source actually says so.

- Yomi needs the presence of at least one candle for temple generation, but the number of candles does not increase that generation; Turmoil does.
- Phlegra's unrest rises more with higher local dominion strength.
- Mekone modifies effective maximum dominion in a conflict calculation.
- Dark Ships tests whether origin and destination lie in friendly dominion.
- Miasma acts on covered provinces but treats ownership, sacred status, terrain, and underwater location differently.

The controlling variable must be an explicit record field in the next schema revision. Until then, it remains in the verified mechanic list.

## 52. Beneficiaries and victims

Special dominions often affect more than the owning nation. The manual explicitly describes cases involving disciples, enemies, allies, or every suitable object in the province.

The Golem Cult illustrates the danger. Constructs gain Hit Points in the dominion even when they belong to an enemy. A rule that sounds like a national bonus is actually a territorial modifier. The difference changes invasion planning and counter-selection.

Every future special-dominion record should expose four separate audiences:

- owner;
- disciple or ally;
- enemy;
- neutral or universal objects.

## 53. Permanent and reversible effects

Some systems change a province while it is covered. Others consume population, alter terrain, generate units, or accumulate insanity and unrest. Their consequences can outlast the candles that caused them.

A national dossier should distinguish:

- immediate reversible modifiers;
- accumulating but recoverable pressure;
- permanent terrain change;
- population conversion or destruction;
- generated units that persist after dominion changes;
- information effects that end when concealment ends.

This distinction belongs to the national application, not the shared one-line system record.

## 54. Disciples are an explicit field, not an afterthought

The official manual repeatedly states whether a special dominion transfers, partially transfers, or affects disciple lands without becoming the disciple nation's own ability. The register preserves that statement separately.

Team advice that ignores this field can recommend a pairing whose economy or armies are damaged by the master. MA Ermor, Asphodel, C'tis, R'lyeh, and Phlegra all require more than a generic “special dominion” warning.

# Part IX: Website and Research Use

## 55. The publication contract

`base-object-register.schema.json` defines the top-level contract. Every build must contain:

- schema version;
- edition and generation date;
- vanilla 6.35 structured-snapshot declaration with a visible 6.36 live-baseline overlay;
- evidence key;
- scope and deliberate exclusions;
- source manifest;
- per-category counts;
- the nine record collections.

Core record fields include stable ID, object type, name where applicable, ruleset, evidence status, source IDs, canonical section, verification date, and record hash.

The schema is intentionally strict at the collection level and permissive inside the specialist records. The source contains hundreds of rare fields. Prematurely forbidding an unfamiliar property would encourage data loss. Later schema revisions can tighten well-understood object families while retaining an escape hatch for raw source fields.

## 56. Default search views

A public site should provide at least three views.

### Guide view

Guide view hides internal spell rows, raw masks, unknown attributes, hashes, and source-file detail. It shows access, cost, principal effect, evidence badge, and a link to the canonical chapter.

### Advanced view

Advanced view exposes engine IDs, effect numbers, chained records, raw selectors, unusual item properties, site masks, and record hashes. It is intended for expert play, modding, and research.

### Change view

Change view compares two source revisions and lists added, removed, and changed records by field. It should also show which nation dossiers or canonical sections depend on the changed object.

## 57. Filters that should exist at launch

| Family | Essential filters |
| --- | --- |
| Spells | Public status, school, level, paths, kind, role, cost, national restriction, legendary flag |
| Items | Slot, Construction level, artifact class, paths, path boost, movement, economy, restriction |
| Summons | Spell school, spell level, target type, unique group, resolved status, unit abilities |
| Pretenders | Nation, age, starting dominion, path cost, innate paths, discount, movement class, shape links |
| Thrones | Level, path income, claimed effect, recruitment, scales, dominion, population, unrest |
| Sites | Path, search level, terrain, rarity class, gem income, recruitment, ritual or research effect |
| Mercenaries | Age, troop type, commander, starting strength, minimum bid, experience |
| Special dominions | Nation, age, controlling variable, beneficiary, disciple transfer, permanent effect |

## 58. Related-object links

The website should make object relationships visible without copying pages.

- A summon spell links to every possible unit.
- A summoned unit links back to every producing spell.
- A Pretender links to its available nations and shape forms.
- A site links to recruitable units and commanders.
- A mercenary links to its leader, troop, and fixed items.
- A special dominion links to each applicable nation dossier.
- A national spell links to the nation and its research branch.

These links turn the library into a graph rather than a stack of articles.

## 59. Example website questions

The object layer can answer questions that are awkward in prose:

- Which Nature rituals create commanders rather than troops?
- Which Construction 5 items increase path access?
- Which level-two Thrones grant commanders or research effects?
- Which Pretender chassis are shared by two selected nations?
- Which mercenary companies exist in the Middle Age and begin with experienced troops?
- Which sites can appear underwater and grant recruitable commanders?
- Which special dominions harm disciples or enemies as well as helping the owner?
- Which summon relations remain unresolved in the current evidence set?

The answer can then link to strategy rather than embedding a generic recommendation in every object card.

## 60. Nation dossier integration

A dossier should not print a complete copy of every national spell, Pretender, summon, and site. It should select the records that matter to the nation's plans and add only national analysis.

A clean dossier entry can contain:

- object ID and short name;
- why the nation can access it;
- the timing branch it enables;
- the national role it fills;
- likely counters or failure modes;
- links to the base record and canonical rule chapter;
- modded delta where relevant.

This is the foundation that allows nation work to resume without creating hundreds of duplicate fact paragraphs.

# Part X: Verification and Maintenance

## 61. Import controls

The importer refuses an unexpected upstream commit unless an explicit refresh flag is supplied. This protects the frozen 6.35 baseline from a silent pull of later data.

The source manifest records:

- repository URL;
- commit and date;
- commit subject;
- source licence note;
- SHA-256 hashes for every imported table;
- official manual identity and hash.

The build also confirms category counts, stable ID uniqueness, required fields, record-hash length, and internal JSON validity.

## 62. Cross-source verification

The source hierarchy for object work is:

1. current official manual or patch statement;
2. current in-game UI or exact engine export;
3. pinned 6.35 extracted data;
4. a published reproduction with method and version;
5. community summary or strategic commentary.

Lower layers can discover a question. They do not silently overrule a higher layer. When the manual and extraction disagree, both values should be recorded and the public field marked unresolved until the current UI or patch history settles it.

## 63. Known limitations of the current build

The current build is deliberately incomplete in several places.

- Independent population-type membership is absent.
- Eighteen named monster-tag selectors still lack complete weighted candidate membership.
- Six summon relations use selectors absent from the pinned tag and fixed-summon tables.
- Sixteen readable property labels remain derived rather than source-confirmed.
- Unit descriptions, spell descriptions, item descriptions, and artwork are excluded.
- The register does not yet contain every weapon, armour, unit, event, or nation record because those have separate ownership or future schemas.
- Source-confirmed values have not all received an independent UI check.

These limitations are part of the publication, not hidden production notes.

## 64. Correction workflow

When an error is found:

1. Record the object ID, field, current value, proposed value, and ruleset.
2. Attach the strongest available source and exact locator.
3. Decide whether the source extraction, importer, interpretation, or prose is wrong.
4. Correct the narrowest authoritative layer.
5. Regenerate hashes, search indexes, and dependent pages.
6. Add a revision note when the public meaning changed.
7. Preserve the earlier version for patch comparison.

This workflow avoids the common failure in which a number is corrected in one article while copies remain wrong elsewhere.

## 65. Patch refresh workflow

A later official patch should be processed as a controlled migration:

1. archive the current manifest and register;
2. import the new exact-version data into a separate build;
3. compare record hashes;
4. classify each delta as addition, removal, rename, mechanical change, or extraction change;
5. compare the official patch note with the observed delta;
6. update canonical prose only where the general rule changed;
7. update nation dossiers only where national conclusions changed;
8. publish a version digest and redirects for renamed objects.

The full official patch ledger remains the next separate structured-data project after this object layer.

## 66. Mod overlay workflow

Dominions Enhanced and Divinitus should be applied as versioned overlays, not folded into the vanilla records.

An overlay record should identify:

- base object ID, if an existing object is selected;
- mod source file and line;
- load-order position;
- field additions, replacements, and clears;
- newly allocated ID where known;
- unresolved automatic allocation where not known;
- final combined value after every earlier mod is applied.

Book IX already establishes the frozen mod order and collision discipline. The base object register now supplies the vanilla side of that comparison.

# Essay I: Object Literacy Is Strategic Literacy

Dominions is often described as a game of hidden knowledge. The phrase is only partly true. Much of the knowledge is visible, but it is distributed across cards, paths, schools, shapes, national rosters, sites, rituals, and turn timing. The difficulty lies less in secrecy than in joining the pieces quickly enough to make a decision.

An object database does not remove judgment. It removes avoidable retrieval cost. A player who can immediately find every ritual that produces a Death commander can spend time comparing risk, timing, and price. A player who cannot find the candidates must rely on memory, and memory tends to preserve famous options while losing narrow or recently changed ones.

The same principle applies to counterplay. An unfamiliar item need not remain a mystery if its slot, resistances, automatic spells, movement changes, and bearer restrictions can be read in one place. The strategic question then becomes concrete: which part of the package creates the threat, and which part can be denied?

Object literacy also improves restraint. Easy access to a catalogue makes it tempting to select the most impressive card. A well-designed reference pushes in the opposite direction by showing access costs and relationships. The object exists inside a conversion chain. Research, gems, mage-turns, infrastructure, position, and risk all stand between possibility and effect.

The strongest use of the database is not encyclopaedic display. It is careful exclusion. Filters can remove options the nation cannot reach, afford, deliver, or exploit in time. The remaining set is small enough for genuine strategic reasoning.

# Essay II: Versioned Facts and Reproducible Judgment

A strategy library becomes unreliable when it treats facts as timeless. Dominions patches can change a requirement, cost, unit, site, or exception. Mods can replace the same object again. A remembered truth may remain broadly sensible while its numerical premise has expired.

Versioned records solve only half of that problem. They can show what changed, but not whether the old recommendation still works. That requires reproducible judgment.

A good recommendation names its premises. It identifies the ruleset, object IDs, national access, research timing, costs, expected opponent, and intended role. When a patch changes one premise, the conclusion can be retested without reconstructing the original argument from memory.

This also improves disagreement. Two players may recommend different summons because they assume different map sizes, gem incomes, research rates, or enemy compositions. With explicit records and assumptions, the disagreement becomes informative rather than rhetorical.

The library's long-term value will not come from claiming finality. It will come from making correction cheap, visible, and local. Stable identities, source manifests, evidence labels, and record hashes turn a correction from an editorial crisis into routine maintenance.

# Part XI: Practical Reference Sheets

## 67. Object-card minimum fields

| Object | Minimum public card |
| --- | --- |
| Spell | Name, ID, school, level, paths, combat or ritual, cost, role, restriction, evidence |
| Item | Name, ID, slot, Construction level, paths, principal properties, restrictions, artifact state, evidence |
| Summon | Producing spell, possible units, selection rule, quantity status, permanence, evidence |
| Pretender | Name, ID, nations, starting dominion, path cost, innate paths, body, forms, discounts, evidence |
| Throne | Name, ID, level, claimed effects, income, recruitment, risks, evidence |
| Site | Name, ID, path, search level, terrain, income, recruitment, other effects, evidence |
| Mercenary | Company, leader, troop, age, strength, minimum bid, experience, recovery, evidence |
| Special dominion | System, nations, controlling variable, beneficiaries, victims, disciple rule, evidence |

## 68. Beginner lookup checklist

- Confirm vanilla or modded ruleset.
- Search by name, then confirm engine ID.
- Check access before effect.
- Check cost and timing before enthusiasm.
- Open linked rules when a field is unfamiliar.
- Treat source-confirmed and unresolved badges differently.
- Use the current game interface when a campaign decision turns on an edge case.

## 69. Expert comparison checklist

- Compare stable IDs and record hashes between versions.
- Inspect chained spells and shape graphs.
- Separate raw fields from publication-derived tags.
- Resolve national and realm restrictions.
- Join summons to current unit records.
- Join sites to terrain and ownership conditions.
- Model mutable campaign state outside the base record.
- Record uncertainty instead of normalizing it away.

## 70. Editorial no-duplication checklist

- Search the Reader's Guide and object register before drafting.
- Link to Book II for economy, Book III for Pretenders and dominion, Book IV for combat, Book V for magic, Book VI for strategy, and Book XI for abilities.
- Add a new paragraph only when it explains an object-specific exception, application, correction, or evidence result.
- Keep complete inventories in data, not prose.
- Use one stable object ID across every dossier and essay.
- Update the source record once, then regenerate dependants.

## 71. What this unlocks

The base-game object layer is now substantial enough to support the next phases without returning to repeated manual research.

It unlocks:

- object-aware nation dossiers;
- vanilla-versus-DE-versus-Divinitus comparison pages;
- spell, item, summon, Pretender, Throne, site, and mercenary filters;
- cross-object search and access graphs;
- patch-by-patch record comparison;
- automatic detection of changed national recommendations;
- a reliable boundary between verified facts and unresolved engine behaviour.

The remaining G-03 work is narrow and explicit: resolve independent population types, enumerate the weighted candidates behind eighteen named monster tags, identify the six remaining raw selectors, and replace sixteen derived property labels when stronger source wording becomes available. Realm-restricted spell access is complete for the pinned snapshot. None of the open items prevents the register from serving as the reusable foundation for the website and later dossiers.

# Source Record

## Official sources

- Illwinter Game Design, *Dominions 6 Manual*, revision 2, especially Magic Sites, Mercenaries, Pretenders, artifacts, and Special Dominions, pp. 28-36, 79-88, and 100-116.
- Illwinter Game Design, *Dominions 6 Modding Manual*, version 6.34, for object selection, IDs, properties, sites, population types, spells, items, and national relations.
- [Illwinter Dominions 6 documentation](https://www.illwinter.com/dom6/docs.html).

## Version-matched extracted source

- [Dominions 6 Data Inspector repository](https://github.com/larzm42/dom6inspector), commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, “Update to 6.35,” 26 May 2026.
- [Dominions 6 Data Inspector](https://larzm42.github.io/dom6inspector/), used as a public cross-check for the extracted object families.

## Project artefacts

- `website/base-object-register.json` - 4,196 versioned records plus realm expansion, selector records, and property-label provenance.
- `website/base-object-register.schema.json` - publication contract.
- `tools/build_base_object_register.py` - pinned, reproducible importer.
- `18-foundation-coverage-gap-audit.md` - ownership and G-03 definition.
- `37-edition-25-object-layer-maintenance.md` - Edition 25 evidence and validation record.
- Book III - canonical Pretender and special-dominion rules.
- Book V - canonical magic, research, ritual, and forging method.
- Book VI - canonical Throne, mercenary, and campaign strategy.
- Book XI - canonical unit and ability interpretation.
