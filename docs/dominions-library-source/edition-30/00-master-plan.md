# The Dominions 6 Knowledge Library

## Purpose

The aim is to build a reference library deep enough to support serious play, modding, multiplayer diplomacy, nation analysis, and long-form guides without having to reconstruct the same knowledge from scattered manuals, videos, forum posts, and old conversations.

The finished library will serve two forms at once:

1. **A private research archive** containing citations, disputed claims, test notes, version history, and raw technical detail.
2. **A public TheHoboKingdom edition** written as clear guides, essays, nation dossiers, tables, and tools without exposing private campaign material or filling the prose with research-process commentary.

This is not a one-pass encyclopaedia. Dominions 6 changes through patches, and Dominions Enhanced and Divinitus change the rules again. Every article therefore needs an explicit ruleset and evidence date.

The current public base-game release recorded by Illwinter is Dominions 6.37, released on 9 September 2026 UTC. Foundation Book I uses that public baseline together with the official main manual revision 2. The live Modding Manual still identifies itself as version 6.36; the Event Modding Manual remains a separately versioned source and later patch notes or controlled tests still govern uncovered behaviour. The large structured object register remains pinned separately to its auditable 6.35 Inspector commit. Book XIV's command-locator export remains labelled as its complete 6.34 extraction until every token and page locator is rebuilt against the newer manual.

## Rulesets to keep separate

Never combine these silently:

| Ruleset | Baseline |
| --- | --- |
| Unmodded Dominions 6 | Current game patch, official manual revision, and current extracted game data |
| Dominions Enhanced | Exact DE release and source commit |
| Divinitus | Exact Divinitus file/version |
| DE + Divinitus | Exact load order and both exact versions |
| Historical advice | The version used when the advice was written |
| Experimental mod work | Its own mod version and test scenario |

The active combined ruleset has now been frozen from the exact supplied files:

- `DomEnhanced2_16.dm` - Dominions Enhanced v2.16.
- `Divinitus_1.15.3_DE.dm` - Divinitus v1.15.3 DE edition.
- Intended load order: Dominions Enhanced first, Divinitus DE second.

The public Divinitus sources remain inconsistent, but that no longer prevents analysis of this particular game setup. All combined guides can be tied to the two supplied file hashes rather than a vague claim that the mods were "latest."

## Evidence standard

Each claim receives one of seven labels in the research archive:

| Label | Meaning |
| --- | --- |
| **Official** | Directly stated in an Illwinter manual, official change page, or current in-game data |
| **Source-confirmed** | Directly present in the relevant mod source or changelog |
| **Reproduced** | Confirmed in a documented test with version, setup, and result |
| **Community-tested** | Reported with enough detail to be credible, but not yet reproduced for this library |
| **Derived** | Calculated from confirmed inputs, with the derivation stated |
| **Strategic doctrine** | A reasoned recommendation whose value depends on the position |
| **Test pending** | Important, plausible, incomplete, contradictory, or not yet reproduced |

Strategy recommendations are not facts. They should state their assumptions: map type, player count, independent strength, research speed, diplomacy rules, throne settings, opponents, pretender, and mod list.

## Core source stack

### Official documents already preserved

- Dominions 6 Manual, revision 2 — 449 PDF pages.
- Dominions 6 Modding Manual, game version 6.36 — 65 pages; the Book XIV command-locator snapshot remains the archived 6.34 extraction.
- Dominions 6 Event Modding Manual, game version 6.29 — 20 pages.
- Dominions 6 Map Making Manual, game version 6.26 — 11 pages.
- Dominions 6 File Formats — 1 page.

### Current structured references

- Illwinter’s official Dominions 6 documentation and change pages.
- The current Dominions 6 Mod Inspector, checked against in-game data where discrepancies matter.
- The Dominions 6 section of Illwiki, treated as a community reference rather than final authority.
- Dominions Enhanced source, releases, and Workshop change notes.
- Divinitus source files and changelog.
- Reproducible test games and controlled battle tests.
- Carefully selected guides, videos, tournament commentary, and forum investigations.

## Library structure

### Book I — Foundations

- What Dominions 6 is actually modelling
- Ages, nations, pretenders, dominion, thrones, and victory
- Turn structure and simultaneous resolution
- Information management and the limits of what the game reveals
- Player-facing interface operation, setup, and hosting are owned by completed Book X
- The Dominions random number system
- What the game tells us, what it hides, and how to inspect it

Foundation Book I has now begun as a full reference chapter rather than a planning outline. Its first completed draft establishes:

- version and ruleset labels;
- evidence and citation standards;
- path, school, statistic, time, and spatial notation;
- an essential glossary;
- the complete official 63-step hosting sequence;
- beginner explanations and expert timing consequences;
- diagnostic and operational checklists;
- controlled tests for unresolved edge cases.

The turn-and-economy quick reference has also been completed. It condenses the hosting spine, provincial formulas, recruitment gates, standard fort table, siege arithmetic, Province Defence costs, site-search rules, Blood Hunting checks, and the exact global economy changes in the frozen mod set.

### Book II — Economy and State

- Gold, resources, recruitment points, command points, upkeep, and supplies
- Population, taxation, unrest, pillaging, and blood hunting
- Forts, laboratories, temples, administration, and province defence
- Magic sites, site searching, gem income, and conversion
- Expansion tempo, infrastructure tempo, and opportunity cost

Foundation Book II now has a complete first research edition. It establishes:

- stock, flow, capacity, and position as the core economic model;
- population, terrain, tax trace, income, upkeep, local resources, and every recruitment gate;
- unrest, pillage, patrolling, supplies, starvation, and Blood Hunting;
- forts, temples, laboratories, construction timing, sieges, and Province Defence;
- new-player audits and expert diagnostic ratios;
- exact DE 2.16 global economic overrides under the frozen combined load order;
- an explicit record of official-document conflicts;
- the ordinary Commander Point ladder, multi-month cost model, and AI exclusions;
- versioned Sacred-Slave and mounted-component upkeep evidence;
- explicit Need Not Eat, Appetite, transformation, and commander-priority boundaries;
- a subsystem-by-subsystem rounding map, annual-upkeep observation table, unrest candidate thresholds, and fort-supply documentary interval;
- ten controlled-test suites;
- seven long-form essays on forts, population, static defence, logistics, unrest, conversion, and integer production boundaries.

R-009 is complete at its stated Official plus Community-tested tier. Full rounding order, unrest thresholds, fort-supply distance, shapechanged upkeep, fractional monthly aggregation, and generic commander feeding priority remain open until reliable current evidence becomes available. They do not require work from the player and do not block later publication.

### Book III — Pretenders, Dominion, Scales, and Blesses

- Chassis roles and design budgets
- Awake, dormant, and imprisoned timing
- Expansion pretenders, bless pretenders, scales pretenders, and ritual platforms
- Dominion conflict, preaching, temples, prophets, and special dominions
- Scale economics and extreme-scale effects
- Bless design by sacred roster and strategic purpose
- Pretender recovery, Call God, immortality, and transformation

Foundation Book III now has a complete first research edition. It establishes:

- the exact unmodded design-point curves for forms, purchased paths, dominion, scales, and awakening;
- chassis roles, national requirements, design worksheets, and opening-to-late-game job audits;
- official dominion sources, maximum, temple checks, propagation, preaching, Inquisitors, Heretics, blood sacrifice, Thrones, and dominion elimination;
- ordinary and extreme scale effects with unresolved official-document conflicts kept visible;
- a current blessing reference using the 6.35 structured snapshot and official changes through 6.36, including the Heroism correction and current Inspirational Presence placement;
- blessing design by sacred throughput, activation, Incarnate dependency, combat function, and counterplay;
- Divine Magic replacement families determined by Pretender paths;
- Pretender death, path or dominion loss, Call God, immortality, and remote-plane or soul-destruction limits;
- special dominion categories and disciple-team obligations;
- exact DE 2.16 global scale overrides and its major blessing rewrites;
- the Divinitus 1.15.3 DE load-order layer;
- twelve controlled-test and regression suites;
- six essays on national engineering, religious territory, roster contracts, deferred power, religious logistics, and divine risk.

The foundation is ready to support nation-specific Pretender families. Edition 22 resolves the practical Call God model and same-turn Throne claim-loss timing at mixed, explicitly labelled evidence tiers. Edition 23 traces the currently republished awakening formula back to its pre-Dominions 6 source and records why that republication does not yet close the current distribution. Scale conflicts, some blessing edge cases, guaranteed Throne-check behaviour, simultaneous victory ties, and special-dominion inheritance remain deliberately assigned to evidence-ready research.

### Book IV — Armies and Battle

- Unit statistics and abilities
- Weapons, armour, repel, length, attack, defence, protection, and damage
- Formations, density, squad placement, and battlefield terrain
- Morale, routing, mindless troops, leadership, standards, and taskmasters
- Mounts, trampling, size, obstacles, and movement
- Fatigue, critical hits, regeneration, resistances, afflictions, and healing
- Battle scripting, spell selection, timing, and counters
- Siege, storming, retreat routes, pursuit, and army preservation

Foundation Book IV now has a complete first research edition. It establishes:

- battle objectives, result layers, DRN, long-battle limits, and the distinction between field victory and strategic preservation;
- unit-role analysis, effective statistics, command redundancy, special leadership, squad morale, and harmful mixing;
- formation width, depth, density, placement, movement, zones of control, displacement, and staggered contact;
- every ordinary squad and commander order, target-order limitations, five-order scripts, gem policy, and failure branches;
- exact melee, shield, damage, protection, hit-location, weapon-type, underwater, multiweapon, harassment, repel, and resolution-order rules;
- missile deviation, square-hit mechanics, friendly fire, and shield interaction;
- separate rider and mount targeting, morale, recovery, and trample resolution;
- fatigue thresholds, spellcasting cost, morale checks, army-rout weights, fear, retreat intelligence, and fort-defence retreat;
- resistance, fire, cold, poison, bleeding, shock, rust, life drain, paralysis, false damage, clouds, regeneration, and afflictions;
- battle-magic mechanics, siege and storm context, counter construction, and a repeatable battle-replay method;
- the object-level combat scope of DE 2.16 and Divinitus 1.15.3 DE;
- sixteen controlled-test suites;
- seven essays on morale, fatigue, formation, protection, scripting, army preservation, and combined arms.

The foundation is ready to support the magic volume and later faction army packages. Harassment decay, complete cooldown constants, morale survivor bonus, ordinary active-unit fatigue recovery, some obstacle and targeting weights, mounted carrying arithmetic, and several rounding rules remain deliberately assigned to controlled tests.

### Book V — Magic

- Paths, schools, research, gems, and fatigue
- Combat magic by role: damage, control, buffs, debuffs, summons, and battlefield enchantments
- Rituals, globals, dispels, domes, remote attacks, and movement magic
- Communions, Sabbaths, Choruses, and Grand Communions
- Forging, boosters, path access, empowerment, and hidden paths
- Legendary spells and level-nine research choices
- Wish, Nexus, Tartarians, global economies, and late-game escalation

Foundation Book V now has a complete first research edition. It establishes:

- magic as a conversion chain linking research, paths, mage-turns, gems, laboratories, position, and delivery;
- the nine paths, seven schools, three access gates, primary paths, excess skill, empowerment, and indirect path bonuses;
- exact research arithmetic, hosting timing, breakpoint and portfolio planning, mage-turn opportunity cost, and level-nine selection;
- gem production, pooling, battlefield use, spending limits, alchemy, reserves, and Blood logistics;
- spell preparation, interruption, accuracy, Magic Resistance, penetration, fatigue, battlefield enchantments, and scripting;
- functional battlefield roles for all nine paths and cross-path packages;
- exact Communion, Sabbath, Chorus, and Grand Communion rules, including thresholds, participants, fatigue brackets, shared self-buffs, and collapse;
- rituals, local enchantments, domes, remote attacks, magic movement, globals, overcasting, Dispel, and geopolitical consequences;
- forging, item tiers, base costs, national items, artifacts, yearning, generic boosters, and path-access ladders;
- legendary and late-game transitions;
- the magic-relevant source scope of DE 2.16 and Divinitus 1.15.3 DE;
- twenty controlled-test suites;
- seven essays on research, gems, army magic, communions, rituals, globals, and level-nine choices.

The foundation is ready to support the general strategy volume and later nation-specific research and battlefield packages. Combat-gem AI, spell targeting, rounding, layered domes, Wish vocabulary, simultaneous artifact/global edge cases, and resolved combined-mod objects remain deliberately assigned to controlled tests.

### Book VI — Strategy

- Expansion planning and expansion testing
- Scouting, intelligence, threat assessment, and hidden information
- Research planning as a response tree rather than a fixed queue
- Raiding, counter-raiding, border control, and logistics
- Thugs, supercombatants, assassins, remote warfare, and counters
- Timing attacks, power spikes, deterrence, and recovery
- Throne races, coalition politics, and endgame conversion
- Multiplayer etiquette, NAPs, diplomacy, trades, and table balance
- Single-player AI strengths, weaknesses, and difficulty settings

Foundation Book VI now has a complete first research edition. It establishes:

- strategy as the conversion of assets through position, access, deadlines, tempo, initiative, and attention;
- repeatable expansion testing, party roles, target value, acceptable losses, routing, borders, and first-war transition;
- exact scouting channels, patrol and stealth structure, intelligence cycles, information denial, battle probes, and score-graph interpretation;
- map structure, interior lines, border geometry, fort, laboratory, temple, Province Defence, and annotation doctrine;
- research response trees, breakpoint records, portfolio depth, timing attacks, and emergency pivots;
- exact movement costs, barriers, special movement, logistics, supplies, gem delivery, and reserve positioning;
- the current Raid order, pillaging, raider classes, counter-raiding systems, thugs, assassins, and remote force;
- war aims, invasion ledgers, siege clocks, relief, storming, deterrence, recovery, and elastic defence;
- formal and social NAPs, trades, reputation, threat communication, and coalition politics;
- Throne discovery, claiming, Ascension Point arithmetic, rush timing, counterplay, and Cataclysm;
- current AI bonuses, capabilities, and learning uses;
- multiplayer turn discipline and continuity practice;
- exact active-mod separation;
- twenty controlled-test suites;
- nine essays on expansion, information, raiding, sieges, timing, diplomacy, recovery, Thrones, and AI.

The shared strategic foundation is ready to support nation monographs. Interception probabilities, several movement and siege rounding rules, pillage output, assassination distributions, formal-NAP edge cases, current Throne object data, Cataclysm resolution, AI decision weights, and resolved combined-mod strategies remain deliberately assigned to controlled tests.

### Book VII — Nations

Each nation receives:

- Identity and historical/lore basis
- Complete roster and recruitment restrictions
- Magic access and path probabilities
- National spells, items, sites, heroes, and mechanics
- Expansion options with test evidence
- Pretender families rather than a single “best” build
- Research branches and breakpoints
- Army packages and scripts
- Match-ups, counters, and diplomatic position
- Early, middle, and late-game plans
- Unmodded, DE, Divinitus, and combined versions kept separate

Book VII has now begun with a complete dossier method and a full pilot monograph for Middle Age Arcoscephale. The first research edition establishes:

- a reproducible nation-dossier standard covering rules, capacity, doctrine, and evidence;
- roster analysis by battlefield job and commander analysis by constrained recruitment turn;
- probability-based mage portfolios, access ladders, research response trees, army packages, matchup classes, and Pretender families;
- the complete unmodded MA Arcoscephale roster from the revision-2 manual;
- exact Mystic and Astrologer random structures with derived threshold probabilities;
- national scrying, healing, troop, commander, expansion, communion, path-access, research, campaign, siege, diplomacy, and Throne doctrine;
- the distinction between owning a national ritual and possessing a legal caster;
- a source-level MA Arcoscephale diff for Dominions Enhanced 2.16;
- the DE recruitment rewrite, paired Heart Companions, new cavalry, revised infantry, hero pools, national items, constellations, and nymph/Titan summon ladders;
- the final Grand Hierophant layer created by loading Divinitus 1.15.3 DE after DE 2.16;
- derived teaching and treasure expectations together with the unresolved teaching-cap ambiguity;
- twenty-five controlled-test suites;
- six essays on dossiers, information, probability, preservation, national transition, and geographic magic access.

The pilot is ready for controlled expansion, communion, mod-inheritance, and Grand Hierophant tests. Precise expansion party sizes, several copied-object final cards, constellation replacement order, Mystic Prophet transformation preservation, teaching caps, and event probability behaviour remain deliberately marked as test pending.

Book VII now also contains compact unmodded dossiers for Middle Age Marignon, Middle Age Pyrène, Middle Age Ulm, and Middle Age Man. Each applies the same rules-capacity-doctrine-evidence split to the official roster, pinned random paths, national assets, research branches, matchup responses, Pretender families, and monthly decisions. The Edition 29 Ulm and Man chapters add separate audits with full recruitment membership, object identifiers, national spell and item records, and reproducible random-path calculations.

The Edition 29 Ulm retrieval unit gives the four dossiers that existed at that checkpoint stable entry aliases and extends the concordance with direct nation, smith, Blacksteel, and Iron Angel routes. The draft website export marks all 32 Ulm sections as Middle Age, unmodded Dominions 6.36 material, and the standalone 12-page Ulm reader carries nation-specific provenance and an explicit unresolved-evidence boundary.

The following Man retrieval unit brings the fifth current dossier into the same system. Stable routes now reach Man's roster, mages, random paths, national spells, item boundary, research, matchups, and open questions; the concordance also supplies direct Avalon, Chorus, Crone, Mother, Logrian Wise Man, and Spellsinger lookups. Its standalone reader and draft index remain unpublished working files.

The next independent dossier unit adds unmodded Middle Age Abysia. Its eight commanders, eight troops, two capital sites, two pinned random schemes, six national spells and rituals, one discounted artifact, three heroes, and 6.01 wall-defender note have been reconciled against the official manual, pinned Inspector data, and official patch ledger. The chapter preserves cave-fort arithmetic, live random displays, wall-defender composition, Inner Furnace behaviour, Infernal Breeding output, and forge-cost stacking as unresolved.

The following retrieval unit gives Abysia stable routes to its roster, mages, random paths, capital sites, national spells, artifact, research, matchups, and open questions. Direct concordance entries cover Abysia, Anathemants, Hellscape, Infernal Breeding, Lava Warriors, O'al Kan's Sceptre, Salamanders, the Smouldercone, and Warlocks, while a standalone reader supplies the same nation-specific evidence boundary outside the omnibus.

The next independent dossier unit adds unmodded Middle Age Pythium. Its eleven commanders, fifteen troops, two capital sites producing eight gems per month, one pinned Arch Theurg random scheme, eight national rituals, two nationally discounted items, and three heroes have been reconciled against the official manual, pinned Inspector data, and official patch ledger. The only Pythium patch-ledger match is explicitly Late Age and was excluded; the live second random, automatic Communicant slave behaviour, hydra cloud and head mechanics, Single Battle timing, displayed rebate costs, and particular communion outcomes remain unresolved.

The following retrieval unit gives Pythium stable routes to its roster, mages, random paths, capital sites, national rituals, items, research, matchups, and open questions. Direct concordance entries cover Pythium, Arch Theurgs, angelic summons, the Cathedral of the Spheres, Contact Lar, Grand Communions, hydras, Serpent Cataphracts, the Swamps of Pythia, Theurgs, and Communicants, while a standalone reader preserves the same evidence boundary outside the omnibus.

The next independent dossier unit adds unmodded Middle Age Eriu. Its eleven commanders and eleven troops have been reconciled across ordinary forts, highland and mountain forts, and two capital sites; four mage-random schemes, five monthly capital gems, two active national spells, two discounted items, four unique heroes, one generic hero, and both relevant 6.01 corrections are recorded. Disabled spell placeholders, the Tuatha's hidden second random, terrain-interface edge cases, displayed rebate costs, Spell Singer outcomes, Glamour detection, rider-and-mount behaviour, and hero timing remain unresolved rather than inferred.

The following retrieval unit gives Eriu stable routes to its roster, mages, random paths, recruitment geography, national magic, items, research, matchups, and open questions. Its standalone reader and nation-aware index remain unpublished working files.

The next independent dossier unit adds unmodded Middle Age Agartha. Ten commanders and eleven troops are reconciled across ordinary forts, caves, the capital, and underwater forts; three capital sites, the Oracle's two random slots, twelve national rituals, three unique heroes, and the 6.04 Oracle-shape note are recorded. Exact Golem Cult scaling and ownership, cave-fort income arithmetic, underwater logistics, variable summon counts, transformation outcomes, and battle performance remain unresolved rather than inferred.

The following retrieval unit gives Agartha stable routes to its roster, mages, random paths, capital sites, national rituals, Golem Cult evidence boundary, heroes, research, matchups, and open questions. Direct concordance entries and a standalone reader preserve the same source-backed distinctions outside the omnibus while leaving every runtime-dependent claim unresolved.

The following independent dossier unit adds unmodded Middle Age Uruk. Seventeen commanders and eleven troops are reconciled across ordinary forts, provinces, the capital, and underwater recruitment; eight mage-random schemes, three capital sites, six national rituals, five national items, and two unique heroes are recorded without promoting gameplay inference to fact.

The following retrieval unit gives Uruk stable routes to its roster, mages, random paths, capital sites, national rituals, national items, heroes, research, matchups, and open questions. Direct concordance entries and a standalone reader preserve the same evidence boundary outside the omnibus while live random displays, summoning scale, rider-and-mount behaviour, underwater operations, and combat outcomes remain unresolved.

The next independent dossier unit adds unmodded Middle Age Ashdod. Eight commanders and nine troops are reconciled across ordinary forts and the capital; two capital sites, eight mage-random records, Strange Fire, eight national rituals, no national-item record, and three unique heroes are documented. Hidden random fields, rare cross-path access, ancestor and angel behaviour, giant logistics, hero timing, and battle performance remain unresolved rather than inferred.

The following independent dossier unit adds unmodded Middle Age T'ien Ch'i. Fourteen commanders and sixteen troops are reconciled across ordinary and capital recruitment; two capital sites, five random-magic schemes, ten national spells, four nation-linked items, and three heroes are recorded. Exact conscription output, live random displays, summon and transformation behaviour, forge-rebate stacking, hero timing, and combat performance remain unresolved.

Progress Edition 29 was published to TheHoboKingdom on 8 September 2026 as a website-first release. The searchable layer contains sixteen documents, 2,857 sections, and 264,306 words; Book VII now holds twelve complete Middle Age dossiers. Nine Edition 29 standalone nation readers are public, while the 811-page Edition 28 omnibus remains clearly labelled as the latest complete all-in-one PDF. GitHub Pages deployment and the repository's full build, toolkit, and internal-link checks passed after the section-count guardrail was updated to the verified Edition 29 total.

Hands-on runtime testing and preparation of new test assets are paused. Expansion counts, live random displays, forge-cost stacking, targeting behaviour, rider-and-mount outcomes, R-047, R-058, and similar engine-dependent claims remain visible and unresolved while independently verifiable dossier, metadata, editorial, navigation, and retrieval work continues.

The next source-completeness gate accepts unmodded Middle Age Machaka for Part XXVII, and the following independent writing unit completes its 41-section dossier. The official manual and pinned Inspector snapshot reconcile fourteen commanders, eleven troops, two capital sites, four random-mage schemes, three active national rituals, six discounted item records, and five hero slots. The chapter preserves the disabled `xxx` spell row and the structured-only `Herd of Gnus` restriction as metadata discrepancies rather than presenting either as a confirmed live option; all runtime-dependent spider, mount, ritual, rebate, hero, R-047, and R-058 behaviour remains open.

The Machaka retrieval unit adds thirteen stable routes, ten direct concordance lookups, a scoped 2,898-section working index, and a visually verified fourteen-page standalone reader. The index preserves all published non-Book-VII records while replacing Book VII with its current 746-section source range. None of these local working files is published or pushed.

The next source-completeness gate accepts unmodded Middle Age Shinuyama for Part XXVIII. The official manual and pinned Inspector snapshot reconcile ten commanders, twelve troops, three recruitable random-mage schemes, one capital site producing five gems, twenty-one national rituals, no pinned national-item restriction or rebate row, and four hero slots. The 6.08 Shinuyama/Caelum spell-assignment correction is retained as a version boundary without reconstructing its abbreviated source wording; cave income, mountain rebates, summon quantities, retinues, shapes, hero timing, combat behaviour, R-047, and R-058 remain unresolved.

The following independent writing unit completes the source-backed Middle Age Shinuyama dossier. It separates recruited, random, summoned, hero, and Pretender access; maps the twenty-one national rituals into caster and treasury ladders; and adds terrain recruitment, force packages, research branches, matchup responses, and monthly checks. It preserves cave-fort bonuses, mountain rebates, variable summon rolls, retinues, shapes, hero timing, stealth and assassin outcomes, and all other runtime-dependent claims as open.

The Shinuyama retrieval unit adds fifteen stable routes, eight direct concordance lookups, forty-five correctly bounded search entries, and a visually verified fifteen-page standalone reader. The unpublished Progress Edition 30 working index now contains 2,901 sections across sixteen documents; inherited unresolved cross-references remain recorded rather than silently redirected.

The next source-completeness gate accepts unmodded Middle Age C'tis for Part XXIX. The official manual and pinned Inspector snapshot reconcile ten commanders, twelve troops, one recruitable random-mage scheme with two rolls, two capital sites, four national rituals, one restricted artifact, and five hero slots. Exact Miasma income, disease, terrain-conversion and hosting behaviour; cold-blooded fatigue; summon results; hero timing; combat behaviour; R-047; and R-058 remain unresolved.

The following independent writing unit completes the source-backed Middle Age C'tis dossier. Its forty-three sections cover the full roster, capital economy, Marshmaster random probabilities, national rituals, the Jade Mask, research routes, force packages, matchups, and monthly checks while keeping thirteen evidence boundaries explicit. Navigation, search integration, concordance routes, and the standalone reader remain the next retrieval unit; no runtime testing, publication, or repository push was performed.

The C'tis retrieval unit adds fifteen stable routes, seven direct concordance subjects, forty-three correctly bounded search entries, and a visually verified fourteen-page standalone reader. The unpublished Progress Edition 30 index now contains 2,945 sections across sixteen documents; the one inherited Markdown target and five inherited structured-data references remain recorded without invented redirects. No runtime testing, publication, commit, or push was performed.

The next source-completeness gate accepts unmodded Middle Age Pangaea for Part XXX. The official manual and pinned Inspector snapshot reconcile nine commanders, fifteen troops, five recruitable mage schemes, two capital sites, three national battlefield spells, three national rituals, no pinned national-item restriction or rebate row, and three hero assignments. Exact battle-affliction recovery, forest-recruitment interface edge cases, Magical Tune resolution, ritual implementation, hero timing, combat behaviour, R-047, and R-058 remain unresolved.

The following independent writing unit completes the source-backed Middle Age Pangaea dossier. Its forty-eight sections cover the complete roster, forest and capital recruitment, five mage-random schemes, Earth-Nature-Blood access, Magical Tunes, three national rituals, opening priorities, force packages, matchup responses, and thirteen explicit evidence gaps. Navigation, search integration, concordance routes, and a standalone reader remain the next retrieval unit; no runtime testing, publication, repository commit, or push was performed.

The Pangaea retrieval unit adds eighteen stable routes, seven direct concordance subjects, forty-eight correctly bounded search entries, and a visually verified sixteen-page standalone reader. The unpublished Progress Edition 30 index now contains 2,993 sections across sixteen documents; the one inherited Markdown target and five inherited structured-data references remain recorded without invented redirects. No runtime testing, publication, repository commit, or push was performed.

The source-completeness gate, full writing unit, and retrieval integration are complete for unmodded Middle Age Vanheim in Part XXXI. The 49-heading dossier reconciles six commanders, nine troops, two capital sites, two recruitable random-mage schemes, one national battlefield spell, two national rituals, six item-rebate links, and two hero assignments, then converts that evidence into bounded recruitment, research, army, matchup, and monthly-audit guidance. Eighteen stable routes, eight direct concordance subjects, isolated `nation-vanheim` search coverage, and a visually verified sixteen-page reader now complete the working package. The Four Directions ritual's live selection, sailing and trace-income resolution, shape changes, mounted behaviour, random-path display, summon outcomes, hero timing, combat behaviour, R-047, and R-058 remain unresolved.

The next source-completeness gate accepts unmodded Middle Age Caelum for Part XXXII. The official manual and pinned Inspector snapshot reconcile eight commanders, eleven troops, two structured random-mage schemes, two capital sites, one national battlefield spell, ten national rituals, four item-rebate links, and two heroes. The Seraphine's pinned 20% Fire random conflicts with its manual entry and remains explicitly unresolved; flying, storms, ice-armour scaling, Ice Fort protection, Guardian Spirits, Mammoth resolution, summon and Drugvant outcomes, hero timing, R-047, and R-058 also remain open.

The following independent writing unit completes the source-backed Middle Age Caelum dossier. Its forty-nine sections cover the full ordinary and capital roster, High Seraph random probabilities, national magic, item rebates, opening priorities, recruitment packages, research branches, battlefield packages, matchups, and monthly checks while preserving fifteen evidence gaps. Navigation, search integration, concordance routes, and a standalone reader remain the next retrieval unit; no runtime testing, publication, repository commit, or push was performed.

The complete Middle Age expansion adds evidence-bounded working dossiers for the nineteen remaining unmodded nations: Phlegra, Asphodel, Ermor, Sceleria, Na'Ba, Ind, Bandar Log, Nazca, Mictlan, Xibalba, Phaeacia, Vanarus, Jotunheim, Nidavangr, Ys, Pelagia, Oceania, Atlantis, and R'lyeh. Book VII now covers all 37 Middle Age nations. Each new dossier separates direct roster memberships from special recruitment, prints fixed paths and raw pinned random fields, inventories sites, restricted spells, items, and heroes, and adds bounded strategy without inventing runtime outcomes.

The working website grows to 3,606 sections and 519 redirects, including 513 correctly isolated new nation sections. Nineteen standalone readers pass structural and representative visual checks. Special recruitment, freespawn, reanimation, random display, Blood returns, transformations, mounts, summons, item stacking, hero timing, movement, habitat transitions, combat outcomes, R-047, and R-058 remain open; nothing was published or pushed.

The Caelum retrieval unit adds eighteen stable routes, eight direct concordance subjects, and fifty correctly bounded search entries to the 3,092-section working index. Its sixteen-page standalone reader is visually verified. The Seraphine source conflict and every runtime-dependent boundary remain open; no publication, repository commit, or push was performed.

### Book VIII — Modding and Scenario Design

- `.dm` structure, identifiers, load order, and compatibility
- Units, weapons, armour, spells, items, sites, nations, pretenders, and AI templates
- AI research goals and favourite rituals/items
- Events, variables, event chains, special orders, and diplomacy simulations
- Map files, planes, terrain, starts, thrones, and scenario design
- What is hard-coded and cannot be rewritten through ordinary modding
- Test harnesses, regression scenarios, balance records, and releases

Book VIII now has a complete first research edition. It establishes:

- the stateful object-and-parser model, including category phase order and cross-mod load-order limits;
- identifier allocation, automatic-object stability, bitmask discipline, and save-compatibility policy;
- a new-mod learning ladder, folder and filename rules, error isolation, and reload procedure;
- practical design and validation methods for weapons, armour, monsters, mounts, shapes, commanders, sites, nations, spells, items, blessings, population types, and mercenaries;
- event rarity, conditional probability, targets, province codes, global variables, event chains, global enchantment events, and performance controls;
- a bounded reaction-layer architecture for warnings, grievances, sanctions, coalitions, and recovery without claiming to rewrite the strategic AI;
- hand-drawn and generated map workflows, terrain masks, starts, Thrones, gates, multiple planes, scenario types, and Workshop packaging;
- nation AI hints, unit recruitment hints, Pretender templates, research goals, favourite rituals and items, and behavioural sampling;
- compatibility engineering through frozen sources, object-overlap matrices, final-object reconstruction, code and variable registries, and explicit repair patches;
- a reusable shared-object reconstruction method, with the Grand Hierophant application retained in Book VII;
- static, load, object, behaviour, regression, balance, versioning, and release-candidate standards;
- ten complete project workflows, seven design essays, and operational checklists.

The volume is tied to Dominions 6.36, the live Modding Manual 6.36, Event Manual 6.29, Map Manual 6.26, and the exact supplied DE 2.16 and Divinitus 1.15.3 DE sources. Book VIII's older command locators remain source-labelled where they came from the 6.34 extraction. Manual-version gaps and unresolved engine behaviours remain visible in the command ledger and open research register.

### Book IX — Dominions Enhanced and Divinitus

- Versioned global changes
- Pretender and bless changes
- Nation-by-nation deltas
- New spells, items, units, sites, and nations
- Known compatibility problems
- Load-order effects
- Inspector data built from the actual mod files
- Guides tied to exact releases

Book IX now has a complete first technical-encyclopaedia edition. It establishes:

- the exact DE 2.16 and Divinitus 1.15.3 DE hashes, source authority, load order, and public load-order wording conflict;
- a deterministic index of 17,348 active object blocks and their complete command streams;
- DE's six global commands, including monthly combat-gem longevity and stronger scale constants;
- all 38 distinct DE blessing revisions with costs, crosspaths, scale requirements, and Incarnate consequences;
- DE's object ecosystem across weapons, armour, monsters, sites, nations, spells, items, Pretenders, underwater play, and information systems;
- Divinitus's four starting-dominion source tiers, 1,514-event architecture, candle probabilities, capital institutions, temple networks, priesthoods, divine orders, seasonal systems, and global state machines;
- support-spell, unforgeable-item, divine-site, weapon, and armour families;
- representative resolved systems for the Golden Pillar, Father of Winters, Kami of Storms, Divine Feathered Serpent, Great Stag, Once and Future King, and Grand Hierophant;
- a corrected cross-mod matrix showing 235 shared fixed new-monster IDs, 357 shared selected monsters, 600 Divinitus fixed identities touched by DE, and no nonzero event-code or event-variable collision;
- the high-risk monster 8616 conflict between DE's bulk-crafting helper and Divinitus's Crystal Priest;
- combined Pretender resolution, strategic doctrine, website schema, verification standards, source lint, checklists, and four mod-specific essays.

The accompanying source index consists of a summary JSON, a searchable TSV catalogue, full JSONL command blocks, and a reproducible extractor. It is explicitly a provenance layer rather than a simulation of the Dominions loader.

Nation-by-nation DE deltas remain the work of later dossiers. Live-only collision outcomes and automatic ID allocation remain pending until exact-version inspector data, a reliable public reproduction, or a local game executable is available.

### Book X — Playing and Hosting Dominions 6

Book X now has a complete first research edition. It closes the procedural gap between knowing a rule and operating it in a live game. The volume establishes:

- ruleset freezing, user-data locations, safe mod installation, backups, and a reproducible pregame record;
- map, age, participant, disciple, Pretender, game-setting, victory, and security setup procedures;
- official-lobby joining, turn submission and revision, stale prevention, extensions, substitutions, rollback limits, and host trust;
- the main interface, strategic filters, planes, province and nation controls, shortcuts, contextual help, and current 6.36 operational additions;
- message triage, the Nation Overview, dependency-first order entry, and a four-pass end-of-turn audit;
- local recruitment queues, Army Setup, squad selection, scripting controls, item and gem logistics, mounts, and Reclaim Mount;
- a full strategic-order reference for movement, stealth, patrol, forts, construction, religion, magic, pillage, raid, Blood Hunt, reanimation, espionage, assassination, and seduction-family orders;
- a guided route from installation and turn one through expansion, the first fort, first contact, first war, first siege, midgame, endgame, and post-game review;
- symptom-based troubleshooting, a host runbook, tournament records, dispute procedure, eleven operational checklists, and three essays;
- explicit cross-references to Books I-VI wherever the underlying mechanic or strategic doctrine already has an authoritative home.

The volume is tied to Dominions 6.36, the official manual and documentation index, and official patch announcements through 17 August 2026 UTC. Version-sensitive private-server commands and external PBEM automation remain outside the frozen reference until a current authoritative command specification is preserved.

### Book XI — Units, Abilities, Experience, and Conditions

Book XI now has a complete first research edition. It closes the lookup gap between seeing an unfamiliar unit icon and understanding the systems that icon changes. The volume establishes:

- a six-layer reading method covering class, command, movement, abilities, development, and conditions;
- overlapping unit classes and their leadership, targeting, supply, healing, morale, and movement consequences;
- water, flight, terrain, sailing, teleport, stealth, perception, command support, defence, recovery, auras, contact effects, conditional powers, economic support, and summoning families;
- official experience gain and thresholds, veteran-preservation doctrine, and a visible official/community conflict over cumulative five-star Hit Points;
- the official Hall-of-Fame boundary, a cautiously labelled community-derived heroic taxonomy, and no false promotion of old reverse-engineered formulas into current rules;
- persistent and temporary condition families, including afflictions, disease, old age, curses, horror marks, insanity, poison, control loss, and body-specific recovery;
- a 93-record marked ability and condition table that generates `website/ability-register.json`;
- an army-compatibility audit, counter-construction matrix, battle-review method, seven verification questions, and five essays;
- current ability-facing corrections through Dominions 6.36 and explicit links to Book IV whenever combat resolution would otherwise be repeated.

The book is an interpretive reference rather than an exhaustive export of every unit-card ability value. Current object-specific wording remains a UI or data-record responsibility, while exact unresolved stacking, heroic, experience, perception, and condition relationships remain in the research queue.

### Book XII — Base-Game Objects and the Searchable Reference Layer

Book XII now has a complete first research edition. It supplies the method and publication contract for the reusable unmodded object layer while leaving strategic interpretation in Books II-VI. The accompanying 6.35 register contains:

- 1,474 spell rows, including 1,233 public researchable or Divine entries and 241 internal or unresearchable rows;
- 529 magic items, divided into 378 ordinary Construction entries, 118 Construction 9 artifacts, and 33 special records above the ordinary scale;
- 549 summon relations, of which 25 retain an explicit unresolved engine selection;
- 298 Pretender forms with nation-age availability relations;
- 74 Thrones and 1,179 other magic sites;
- 78 mercenary companies;
- one independent-coverage marker preserving the absence of a current population-type table rather than inventing a catalogue;
- 14 official special-dominion systems, with nation-age relations stored inside the records.

The importer pins its source to the Dominions Data Inspector commit labelled for 6.35, hashes every imported table and record, separates source fields from editorial tags, and refuses an unexpected source revision without an explicit refresh flag. Book XII explains object identity, evidence, spells, items, summons, Pretenders, sites, mercenaries, independent limitations, special dominions, website filtering, and maintenance. It does not reproduce the object rows as thousands of pages of prose.

### Book XIII - Version History and the Official Patch Ledger

Book XIII now has a complete first research edition. It supplies the official version spine that the earlier system and reference books depend upon. The accompanying ledger contains:

- all 33 official public update announcements from 6.01 through 6.37;
- all 1,096 individual change bullets, each with release, official section, source locator, source and record hashes, editorial class, confidence, domains, named terms, commands, and canonical destinations;
- a complete dated release timeline, with 774 changes in 2024, 222 in 2025, and 100 through the 6.37 release in 2026;
- an explicit record that no matching public announcements were present for 6.10, 6.20, 6.22, or 6.26, without inventing a reason or undocumented build history;
- 226 distinct named `#commands` linked to the command lexicon;
- a stale-guide repair method, dependency-driven maintenance process, website publication model, and three essays on versioned rules, bug-fix history, and authorship as maintenance.

The public ledger does not reproduce the full official announcement text. It preserves source identities, URLs, locators, word counts, and hashes, then adds restrained project metadata. All source bullets are official; 250 lower-confidence fine-grained classifications remain openly marked for editorial review. Book XIII owns chronology and maintenance, while each earlier book retains the readable explanation of the current rule.

### Book XIV - The Command and Terminology Lexicon

Book XIV now has a complete first research edition. It supplies the official-language retrieval layer that Books VIII and XIII deliberately left separate. The accompanying register contains:

- 1,609 distinct hash tokens located across the archived official Modding 6.34, Event Modding 6.29, and Map Making 6.26 extraction used for the current command-locator snapshot;
- 1,540 tokens with official definition or syntax lines, 60 reference-only entries, and nine prose-only mentions;
- 1,567 literal commands, thirteen official templates, and 29 case-preserved double-hash message substitutions;
- 97 controlled terrain and numeric aliases that point back to official templates rather than masquerading as separate definitions;
- complete reconciliation of all 226 patch-note tokens: 196 exact definitions, two exact reference entries, sixteen template aliases, three spelling discrepancies, three family expressions, one message placeholder, and five official 6.36 patch-only event commands awaiting full manual syntax;
- manual versions, pages, sections, syntax locators, domains, patch records, cautions, canonical destinations, stable hashes, and a validated website schema;
- a safe lookup method, context-collision model, evidence ladder, version-drift analysis, maintenance workflow, five expert essays, a complete A-Z manual locator, template-alias table, and patch-token index.

The public register does not reproduce the manuals' explanatory prose. Book XIV locates and reconciles syntax; Book VIII retains design and validation method; Book XIII retains chronology. Vanilla 6.37, the pinned vanilla 6.35 object snapshot, DE 2.16, and Divinitus 1.15.3 DE remain separate evidence or ruleset layers.

### Editorial consolidation — Progress Edition 11

The reader-facing library has completed its first cross-book editorial pass:

- internal research-control documents remain in the project archive but no longer appear before Book I in the public PDF;
- Book I now defines one authoritative subject map for the whole library;
- repeated baseline, evidence-key, reading-route, and completion boilerplate has been removed from later books;
- DE scale, blessing, object, event, and collision inventories live in Book IX;
- battle-spell arithmetic lives in Book IV, while Book V owns magical planning;
- siege arithmetic lives in Book II and the field reference, while Books IV and VI keep only battle and campaign consequences;
- the Grand Hierophant application lives in Book VII, while Book VIII keeps the reusable reconstruction method;
- duplicate essays and appendices have been removed or replaced with cross-references;
- the only exact cross-book paragraph retained is the modified-income formula in Book II and the deliberately duplicative field reference.

The detailed audit is preserved in `15-editorial-consolidation-audit.md`. Progress Edition 11 is the consolidated reader's edition of Foundation Books I-IX.

### Retrieval and publication layer — Progress Edition 12

The consolidated books now have a shared navigation and website-export layer:

- `16-reader-guide-concordance.md` supplies six reading routes, problem-based navigation, a 192-entry A-Z subject concordance, a 92-term expanded glossary, and a 45-item foundation research register;
- every one of the reader corpus's 1,846 headings has a stable PDF and website destination;
- 151 semantic aliases preserve readable links when an editorial heading uses different wording;
- the PDF builder turns ordinary Book-and-Part references into internal links and uses the stable destinations for bookmarks and the linked contents;
- `website/content-index.json` records the complete hierarchy, source lines, URLs, aliases, audience hints, topic hints, and word counts;
- `website/content.schema.json` defines versioned rulesets, sources, evidence-labelled claims, formulas, content blocks, related sections, and revision metadata;
- separate JSON exports carry the reading paths, subject index, glossary, research register, redirects, and a schema-valid article template;
- active research excludes questions that would require the player to run bespoke tests. Engine-dependent questions remain visible but blocked until reliable published evidence or an exact engine export exists.

Progress Edition 12 is therefore the first edition designed as both a book and a publication source. The Markdown remains authoritative prose; the generated website files are navigation and data contracts for TheHoboKingdom.

### Player-operations foundation — Progress Edition 13

Progress Edition 13 adds Foundation Book X to the reader corpus and integrates its stable destinations into the PDF, concordance, website exports, and coverage register. The edition is now both a systems encyclopaedia and an operating manual: a reader can move from installation and game creation through a complete campaign without needing the interface procedure to be inferred from mechanics chapters.

### Unit and ability foundation — Progress Edition 14

Progress Edition 14 adds Foundation Book XI and the first structured ability register. The reader corpus now has a canonical lookup route for unit classes, command requirements, movement permissions, defensive and offensive abilities, experience, heroic traits, and conditions. Book XI interprets these records while Book IV retains combat arithmetic and battle consequences, preventing the new retrieval layer from duplicating the battle volume.

### Base-game object foundation — Progress Edition 15

Progress Edition 15 adds Foundation Book XII and the first versioned base-game object register. The reader corpus now supports exact category and ID lookup for spells, items, summon relations, Pretender forms, Thrones, other sites, mercenary companies, independent-coverage status, and special dominion systems. The Book XII prose explains how to read and verify those records while existing system books retain strategy, formulas, and worked applications.

### Official version-history foundation - Progress Edition 16

Progress Edition 16 adds Foundation Book XIII and the official patch ledger. The reader corpus now has a complete public release chronology through Dominions 6.35, while the website layer can filter every official change by version, class, domain, source locator, command, and canonical page. Current-rule explanations remain in their existing books, preventing the version history from becoming a second systems encyclopaedia.

### Official command-language foundation - Progress Edition 17

Progress Edition 17 adds Foundation Book XIV and the official command lexicon. The reader corpus now supports exact command, template, alias, context, manual-page, documentation-status, patch-version, and message-substitution lookup. Patch wording remains historically exact in Book XIII, while Book XIV makes every non-exact token relationship explicit. The syntax layer therefore complements Book VIII without duplicating its object-design, event, map, AI, compatibility, or testing guidance.

### Foundation coverage audit - 11 August 2026

The official manual and auxiliary-manual comparison is recorded in `18-foundation-coverage-gap-audit.md`, with machine-readable ownership rules in `website/coverage-register.json`.

The audit confirms that Books I-XIV own the general treatment of turn timing, economy, Pretenders and religion, battle, magic, campaign strategy, nation-analysis method, generic modding, the frozen DE/Divinitus ruleset, player operations, the interpretation of unit classes and conditions, the base-game object layer, official version history, and official command-language retrieval. These subjects must not be proposed again as new general volumes. Later work may correct their canonical chapters, apply them to a nation or object, add verified evidence, or improve retrieval.

The player-operations gap is closed by Book X, the unit-and-ability reference gap by Book XI, the reusable base-game object layer is substantially complete in Book XII, the official patch ledger is substantially complete in Book XIII, and the official command-language layer is substantially complete in Book XIV. The remaining shared maintenance work is:

1. work through the remaining economy, turn, and Pretender questions R-008 and R-010 through R-014 when reliable evidence becomes available;
2. editorial review of 250 lower-confidence patch classifications;
3. bounded object-layer edge cases: independent population types, 25 selection-based summon relations, source-property labels, and realm expansion;
4. documentation research for 60 reference-only and nine mention-only manual tokens when reliable evidence becomes available.

No further broad general reference is presently justified. R-002 through R-005 were resolved in a separate DE-Divinitus integrity publication and are cross-linked from Book IX without incorporating that publication as another foundation book. The main library now advances through corrections, evidence upgrades, structured-data maintenance, and later nation applications rather than rebuilding shared foundations.

### Maintenance checkpoint - Progress Edition 18

Progress Edition 18 is a consolidation release, not Foundation Book XV. It adds the missing province-corpse economy section to Book II, places the remaining official 6.35 score-graph, siege-teleport, and mage-preservation corrections in Book VI, names the 6.35 F1 pillage filter precisely in Book X, and closes R-002 through R-005 through a bounded Book IX link to the independent integrity publication. The repaired Divinitus edition and its technical release remain outside the encyclopedia.

### Evidence checkpoint - Progress Edition 19

Progress Edition 19 resolves R-006, R-007, and R-015 inside their existing canonical homes. The unmodded 6.35 economy now uses 2% Growth/Death income and 2% Order/Turmoil resources per step, with old conflicting tables preserved only as version-history warnings. Book III now distinguishes direct preaching, heretic preaching, Throne claims, ordinary dominion spread, dominion effects, elimination, and victory in hosting order, while preserving narrower uncertainty about passive-source iteration and same-turn Throne ownership. Awakening distribution, blessing edge cases, exact Call God thresholds, rounding, supply, upkeep, unrest, and starvation remain open rather than being inferred.

### Blessing and live-baseline checkpoint - Progress Edition 20

Progress Edition 20 advances the live unmodded baseline to Dominions 6.36 while retaining the auditable 6.35 Inspector object snapshot as a separately labelled data layer. It resolves R-016 in Book III through an activation state model, automatic-blessing boundaries, repeatable and overlapping effects, weapon-trigger families, item-granted blessing, and the independent status of riders and mounts. Adjacent cross-source stacking and transformation lifetime questions remain assigned to R-040, R-049, and R-052.

The edition also ingests the full 6.36 official announcement. Book XIII now contains 32 announcements and 1,090 stable change records; Book XIV reconciles 226 patch tokens and marks the five new event commands as official patch-only until an updated manual supplies their complete syntax. The 6.36 movement, Rust, Blood Sacrifice order, mount, interface, replay, and modding changes are routed to their existing canonical books rather than repeated as a new volume.

### Economic-boundary checkpoint - Progress Edition 21

Progress Edition 21 returns to the unresolved Book II cluster without creating another economy book. It completes R-009 at an Official plus Community-tested tier: ordinary Commander Points are one base point plus the current fort bonus, multi-point costs accumulate over months, `#slowrec` changes commander cost rather than the province pool, and AI difficulty does not multiply Commander Points or Holy Points.

The same audit advances R-010 and R-013. Sacred and Slave upkeep reductions stack under the published 6.33 observation, mounted upkeep is decomposed into separately tagged rider and mount bases, Need Not Eat is established as the explicit starvation-immunity tag, and the 6.18 transformation correction supplies an official state-change boundary. Shapechanged upkeep, fractional monthly aggregation, and generic commander feeding priority remain open. R-008, R-011, and R-012 remain queued because the available documents do not resolve their precise rounding, unrest, or fort-distance boundaries.

### Divine-timing checkpoint - Progress Edition 22

Progress Edition 22 returns to Book III rather than creating another Pretender or victory volume. R-017 is complete at a mixed evidence tier. The official Holy, Disciple-game, Elegist, Recall God, Trinity, return, and hosting rules are reconciled with published controlled research establishing a fixed 50-point ordinary pool and per-priest effective-rating `-1/0/+1` monthly variation. Detailed Disciple routing and capital or fort placement remain explicitly labelled Current Community Reference.

R-018 is also complete at Official plus Community-tested tier. A claimant killed after the step-8 claim does not undo it; unfortified conquest or successful storming makes the Throne unclaimed before the step-57 victory check; siege without fort conquest does not. Exact simultaneous winning-total ties remain a separate test boundary.

R-014 remains queued. The official 10-13 and 28-42 ranges govern planning. An older Dominions 5 exploding-die model is retained only as a test hypothesis because no current 6.36 sample, engine trace, or developer confirmation proves that distribution for Dominions 6.

### Boundary-evidence checkpoint - Progress Edition 23

Progress Edition 23 returns to the unresolved R-008 and R-010 through R-014 group without pretending that a recent page title is a recent test. Book II now separates the rounding questions for income, resources, Recruitment Points, Commander Points, upkeep, and fort supply; demonstrates what the published annual-upkeep values exclude; converts the ambiguous community unrest wording into explicit candidate thresholds; and distinguishes the agreed fort range and highest-fort rule from the disputed multiplier. The 6.35 Supply Usage refresh correction is incorporated into the equipment-change workflow.

Book III now records that the Dominions 6 community Pretender page revised in June 2026 republishes Loggy's exploding-die awakening model. The formula is traceable to pre-Dominions 6 reverse-engineering notes, has no published 6.x raw sample, and uses displayed ranges that do not exactly match the revision-2 manual. It therefore remains a source-traced hypothesis rather than a 6.36 law.

No research item is closed merely by this release. Its purpose is to make every remaining claim small enough to verify, every operational fallback explicit, and every future correction local to its canonical section.

### Full-corpus editorial checkpoint - Progress Edition 24

Progress Edition 24 applies one house style to all sixteen reader-facing sources used by the combined PDF and website export. The voice is direct, practical, and written for players. It uses ordinary game terms, limits stock transitions and repeated contrast formulas, and avoids constantly addressing the reader in the second person.

The editorial pass does not alter the underlying evidence. Headings and stable destinations, table rows, code blocks, link targets, inline code, numeric tokens, ruleset labels, research statuses, and source qualifications are checked against Edition 23. Generated registers keep their exact source-derived entries; only their surrounding explanations are rewritten.

### Perception and ability-evidence checkpoint - Progress Edition 28

Progress Edition 28 returns to Book XI's R-047 through R-049 cluster. It completes the category-level perception question by separating strategic concealment, melee Attack penalties, image selection, temporary states, and technical creature classes. The live Modding Manual's −10 Invisibility penalty supersedes the revision-2 manual's −9 for the 6.36 baseline, while the older value remains visible as version history.

The release also advances the stacking question with verified best-only, cumulative, replacement, and separate-layer examples. It does not invent a universal source hierarchy. Hall-of-Fame formulas remain open, but Edition 28 supplies a raw-observation schema and a three-stage controlled test sequence; R-058 now owns the two narrow perception interactions that current documents do not settle.

### Dominions 6.37 baseline checkpoint — Progress Edition 30

The working library advances its current unmodded executable baseline to Dominions 6.37, released on 9 September 2026. Book XIII now records 33 official announcements and 1,096 change bullets through 6.37; the new release fixes level-nine research access, drowning for non-commanders, Drake breath recovery timing, a game-switch memory leak, anti-cheat behaviour, and unspecified statistics or typos.

The update does not promote unspecified patch details into object or combat claims. The live Modding Manual remains labelled 6.36, the complete command-locator extraction remains pinned to 6.34, the structured object register remains pinned to Inspector 6.35, and the patch-token total remains 226 because 6.37 names no mod commands. Runtime work, R-047, R-058, and all other engine-dependent questions stay open.

## Foundational essay coverage

This register prevents completed subjects from being proposed again under new titles.

| Topic | Status and canonical home |
| --- | --- |
| Dominions as a Game of Conversion | Complete in Books II and VI. |
| The Anatomy of a Turn | Complete in Book I, with operational layers in Book VI and the field reference. |
| The Expansion Problem | Complete in Book VI, Essay I. |
| Research Is a Response Tree | Complete in Book V, Essay I, and applied in Book VI. |
| Fatigue: The Hidden Battle Economy | Complete in Book IV, Essay II. |
| Morale and the Shape of Defeat | Complete in Book IV, Essay I. |
| Communions Without Myths | Complete in Book V, Essay IV. |
| From Mage to Army | Complete in Book V, Essay III. |
| Pretender Design as National Engineering | Complete in Book III, Essay I. |
| Dominion Is Territory by Other Means | Complete in Book III, Essay II. |
| The Economics of Forts and Mages | Complete in Book II, Essay I. |
| Raiding and Counter-Raiding | Complete in Book VI, Essay III. |
| Siege as a Strategic Clock | Complete in Book VI, Essay IV, with arithmetic in Book II. |
| Thugs and Supercombatants | Covered in Book VI, Part IX; a later worked-example article is permissible only if it adds tested packages rather than repeating the chapter. |
| The Diplomacy of Threat | Complete in Book VI, Essay VI. |
| The Level-Nine Decision | Complete in Book V, Essay VII. |
| Wish, Nexus, and the Late-Game Economy | Covered in Book V, Part XIII; unresolved exact effects remain research items rather than essay gaps. |
| Why the AI Behaves as It Does | Complete in Book VI, Essay IX, with modding limits in Book VIII, Essay III. |
| Designing Fair Mixed-Experience Games | Not yet complete; assign game-creation procedure and setting consequences to Book X, with any house-rule essay clearly marked as doctrine. |
| Mod Compatibility Is Part of Strategy | Complete in Books VIII and IX. |

Nation monographs sit alongside these essays rather than replacing them.

## Work phases

### Phase 1 — Recover and audit earlier work

- Collect every applicable prior Dominions conversation.
- Recover the current TheHoboKingdom Dominions pages.
- Record all known corrections, conflicts, and unfinished projects.
- Do not present old advice as verified merely because it was previously stated.

### Phase 2 — Build the official rules corpus

- Index every section and table in all five official manuals.
- Convert the rules into linked topic notes.
- Cross-check current game data and official change notes.
- Create a versioned glossary and calculation reference.

### Phase 3 — Build the community and testing corpus

- Catalogue high-quality guides, discussions, videos, and investigations.
- Preserve claims with direct links, authors, dates, versions, and scope.
- Reproduce mechanics that are absent or ambiguous in the manual.
- Maintain a test register with controlled inputs and saved results.

### Phase 4 — Unmodded strategy library

- Write the foundational essays.
- Build expansion, research, combat, magic, and diplomacy guides.
- Produce every nation dossier for all three ages.

### Phase 5 — Modded libraries

- Freeze exact Dominions Enhanced and Divinitus source snapshots.
- Generate mod-aware unit, spell, item, site, and pretender references.
- Write separate DE and Divinitus strategy layers.
- Test combined load-order behaviour before publishing combined guides.

### Phase 6 — Website edition

- Convert the private archive into concise public guides and deeper reference pages.
- Add visible version badges and “last verified” dates.
- Add topic, nation, age, path, school, and mod filters.
- Link public claims to a compact source note without turning every paragraph into academic prose.
- Keep raw test logs, private campaign details, and disputed claims out of the public copy.

## Completion standard

A topic is “library complete” only when:

- its scope and ruleset are explicit;
- official statements have been checked;
- important omissions have either been tested or clearly marked;
- strategy claims explain their assumptions;
- contradictory sources are resolved or displayed;
- the article has a revision date and change history;
- the public version can be read without knowing how the research was assembled.
