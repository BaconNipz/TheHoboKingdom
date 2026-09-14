# Edition 29 Working Paper: Middle Age T'ien Ch'i Dossier Audit

**Status:** complete independent research unit  
**Ruleset:** unmodded Dominions 6.36 live baseline  
**Prepared:** 8 September 2026  
**Dossier target:** Book VII, Part XXVI, Middle Age T'ien Ch'i, Imperial Bureaucracy  
**Runtime work:** paused; no battle test, game-state test, or new test asset was used

## Result

Book VII now contains a source-backed MA T'ien Ch'i dossier covering fourteen commanders, sixteen troops, five monthly capital gems, five random-magic schemes, ten national spells, four national-item links, and three heroes. It separates repeatable low-path access from random and capital-only access, so a possible mage result is never treated as an owned caster.

Rules evidence and strategy remain separate. Exact conscription output, live random display, transformation and summon behaviour, forge-rebate stacking, hero timing, and all combat performance remain unresolved. R-047, R-058, and the hands-on testing queue stay parked.

## Source manifest

### Official manual

- Source: *Dominions 6 Manual*, revision 2.
- Official location: <https://www.illwinter.com/dom6/dom6manual.pdf>.
- Local file: `/workspace/scratch/2d4707cca56d/work/dom6manual.pdf`.
- File size: 18,142,052 bytes.
- Page count: 449.
- SHA-256: `65f430fd97c9f27285d63b797b43bc7fe3844241fdf40230b1d25a901ab9f33f`.
- MA T'ien Ch'i nation extraction: PDF pages 338-339.
- Authority: player-facing roster, costs, recruitment locations, visible paths, national rules, sites, spells, rituals, and items.

### Pinned structured snapshot

- Source: Dominions 6 Data Inspector.
- Exact tree: <https://github.com/larzm42/dom6inspector/tree/cfac4311bc0b58053b8dead7bffbc036ba9bd5dc>.
- Commit: `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.
- Declared dataset baseline: 6.35.
- Files used: `BaseU.csv`, `BaseI.csv`, `MagicSites.csv`, `spells.csv`, `attributes_by_nation.csv`, `attributes_by_spell.csv`, recruitment records, and path definitions.
- Authority: object identifiers, membership sets, random masks, site fields, hero types, nation restrictions, and item rebate fields.

The Inspector is a pinned cross-check. It does not override the current manual or a later official patch.

### Current version and patch boundary

Illwinter's official site records Dominions 6.36 on 17 August 2026 and links the official announcement. The local complete ledger ends at 6.35, so it was searched to that endpoint and the separate 6.36 announcement was checked. No direct MA T'ien Ch'i or named-roster correction was attached from those sources.

That is a bounded negative result, not proof against undocumented or indirect engine changes.

## Nation and site identity

| Field | Verified result |
| --- | --- |
| Nation ID | 69 |
| Name | T'ien Ch'i, Imperial Bureaucracy |
| Era | Middle Age |
| Scale limits | Order +1; Misfortune +1 |
| Fort family | Fortified Cities |
| Heavenly Gate | A1 S2; Celestial Master recruitment |
| Celestial City | W1 E1; Red Guard, Prince General, and Imperial Alchemist recruitment |

The capital produces A1 W1 E1 S2, five gems per month. It produces no Nature gems despite the national Nature ritual suite.

## Recruitment reconciliation

| Class | Count | Records |
| --- | ---: | --- |
| Ordinary commanders | 11 | Scout, Imperial Consort, Eunuch, General, Ceremonial Master, Minister of Rituals, Apothecary, Imperial Geomancer, Minister of Magic, Alchemist of the Five Elements, Master of the Way |
| Capital commanders | 3 | Prince General, Imperial Alchemist, Celestial Master |
| Ordinary troops | 15 | Four basic foot/missile records, three Ministry records, five Imperial foot/missile records, and three cavalry records |
| Capital troops | 1 | Red Guard |

Master of the Way is also marked recruitable outside forts. Capital home-site records remain distinct from the ordinary roster.

## Mage path verification

| Mage | Fixed paths | Pinned random scheme |
| --- | --- | --- |
| Apothecary | N1 | None |
| Imperial Geomancer | E1 S1 | None |
| Minister of Magic | None | One guaranteed A/W/E/S; independent 10% A/W/E/S |
| Alchemist of the Five Elements | N1 | One guaranteed F/A/W/E; independent 10% F/A/W/E/N |
| Master of the Way | W1 H1 | One guaranteed A/W/S/N/G |
| Imperial Alchemist | F1 A1 W1 E1 N2 | One guaranteed F/A/W/E; independent 10% F/A/W/E/N |
| Celestial Master | A1 W2 E1 S1 G1 H2 | One guaranteed A/W/S/N/G; independent 10% A/W/S/N/G |

The Master of the Way's guaranteed branches are 20% each. A specific Minister of Magic path appears across its two rolls with probability 26.875%; 2.5% of all Ministers double their first path, and 7.5% receive two distinct paths. Each elemental path appears on an ordinary or Imperial Alchemist with probability 26.5%, while the secondary Nature result occurs in 2% of recruits. A Celestial Master receives at least one Air increase 21.6% of the time.

These are portfolio probabilities from pinned masks. They are not live-display claims or guarantees for the next recruit.

## National spell reconciliation

| Name | School | Requirement | Cost or type |
| --- | --- | --- | --- |
| Celestial Chastisement | Evocation 5 | S3 | Battle spell, 20 fatigue |
| Celestial Servant | Conjuration 1 | E1 S1 | 1 Earth gem |
| Ambush of Tigers | Conjuration 3 | N2 | 9 Nature gems |
| Herd of Buffaloes | Conjuration 3 | N2 | 8 Nature gems |
| Celestial Hounds | Conjuration 4 | A1 S1 | 2 Air gems |
| Thousand Year Ginseng | Construction 4 | N1 | 4 Nature gems |
| Internal Alchemy | Alteration 5 | W2 S1 | 5 Water gems |
| Living Mercury | Enchantment 5 | W1 E1 | 6 Water gems |
| Contact Huli Jing | Conjuration 6 | N2 | 30 Nature gems |
| Call Celestial Soldiers | Conjuration 6 | A2 S1 | 15 Air gems |

The official tables and pinned nation restrictions agree on the ten names and thresholds. Exact variable summon outputs and runtime behaviour are not inferred.

## National item reconciliation

| Item | Relation | Requirement |
| --- | --- | --- |
| Sword of the Five Elements | Restricted | Construction 3, F1 W1 |
| Armor of the Five Elements | Restricted | Construction 3, E1 A1 |
| Chi Shoes | Nation rebate | Construction 3, A1 |
| Jade Armor | Nation rebate | Construction 7, W2 E1 |

The manual prints two Fire plus two Water gems for the Sword and two Earth plus two Air gems for the Armor. Exact displayed live costs for the rebated items and interaction with other forge modifiers remain open.

## Hero reconciliation

| Hero | Verified paths | Boundary |
| --- | --- | --- |
| Ho Hsien-Ku | A1 N2 | Sacred structured record; timing unresolved |
| Lu Tung-Pin | F1 A1 W2 S3 H2 | Sacred structured record; timing unresolved |
| Li T'ieh-Kuai | A2 S2 D2 | Hero-only Death does not create repeatable national access |

No hero is used as a scheduled path bridge.

## Editorial integration

- Expanded the Book VII title and introductory nation list.
- Added Part XXVI with 43 tagged sections.
- Added the T'ien Ch'i range to the website-export metadata and ended Ashdod's range at the new chapter.
- Preserved strategy as conditional planning and rules as attributed facts.
- Deferred navigation aliases, concordance entries, and a standalone reader to the next retrieval unit.
- Created no test scenario, replay template, observation workbook, or runtime asset.

## Unresolved claim register

| Claim area | Status | Reason |
| --- | --- | --- |
| Conscription output | Unresolved | Manual confirms the rule but not exact composition or scaling |
| Random display | Pinned 6.35 masks | Current live presentation and timing were not observed |
| Summons and transformation | Printed spell records | Variable output, shapes, scripting, and battle behaviour remain engine questions |
| Forge rebates | Pinned nation fields | Final displayed cost stacking was not observed |
| Expansion and matchups | Strategy only | Map, scales, formations, opposition, and rolls change results |
| Hero timing | Hero records only | Arrival conditions and timing are not established here |
| R-047 and R-058 | Parked | Runtime testing is paused |

## Acceptance checklist

- [x] Unmodded MA T'ien Ch'i only; no mod inheritance.
- [x] Fourteen commanders reconciled across ordinary and capital recruitment.
- [x] Sixteen troops reconciled across ordinary and capital recruitment.
- [x] Five random-magic schemes decoded without treating them as live observations.
- [x] Two capital sites and five monthly gems checked.
- [x] Ten national spells matched to source requirements.
- [x] Four nation-linked items separated into restrictions and rebates.
- [x] Three heroes reconciled without scheduling their arrival.
- [x] Patch boundary stated accurately across the 6.35 ledger and separate 6.36 announcement.
- [x] Runtime-dependent claims remain unresolved.
- [x] No external publication or repository push performed.

## Validation record

Scoped validation passed after generated-index integration:

- 3,849 words and 43 headings in the T'ien Ch'i dossier;
- 2,857 entries in the preserved working content index;
- 705 Book VII entries, including 43 correctly isolated T'ien Ch'i entries;
- all nine working website JSON files parse;
- fourteen commander records, five random schemes, ten spells, four items, and two sites rechecked against pinned structured rows;
- Book VII contains no broken internal links.

The full export command still reports six pre-existing unresolved references outside Book VII because the recovered local foundation sources and the newer preserved index are not the same checkpoint. This unit did not delete newer index records or guess replacement targets. The source chapter, export metadata, content-index integration, and audit are the only authored changes in this unit.
