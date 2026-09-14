# Progress Edition 15 and Book XII Audit

## Scope

This audit records the checks applied to Foundation Book XII, *Base-Game Objects and the Searchable Reference Layer*, the versioned 6.35 object register, and the linked Progress Edition 15 PDF and website exports. The audit date is 5 August 2026. The unmodded game baseline is Dominions 6.35; Dominions Enhanced 2.16 and Divinitus 1.15.3 DE remain separate rulesets.

## Outcome

Book XII substantially closes G-03 in the foundation coverage register. It supplies the interpretive method, evidence boundary, maintenance workflow, and website publication contract for the reusable base-game object layer. Books II-VI retain economic, religious, magical, and strategic interpretation, preventing the new reference from becoming a second set of system chapters.

The generated register contains 4,196 records:

| Category | Records | Verification note |
| --- | ---: | --- |
| Spell rows | 1,474 | 1,233 researchable or Divine; 241 unresearchable or internal |
| Magic items | 529 | 378 ordinary forgeable; 118 unique artifacts; 33 special or engine-managed |
| Summon relations | 549 | 25 retain an unresolved selection or monster-tag group |
| Pretender forms | 298 | Nation-age availability is represented as relations |
| Thrones | 74 | 36 level one; 26 level two; 12 level three |
| Other sites | 1,179 | Throne records are removed from this collection to avoid double counting |
| Mercenary companies | 78 | Company, leader, troop, bid, strength, experience, and continuity fields are retained where present |
| Independent recruitment | 1 coverage marker | The missing population-type table is disclosed rather than reconstructed from obsolete data |
| Special dominions | 14 | Official manual systems are linked to their applicable nations and ages |

## Source and Evidence Checks

- The primary extracted source is the public Dominions Data Inspector repository at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, dated 26 May 2026 and labelled `Update to 6.35.`
- The source manifest records the repository URL, commit, date, subject, licence note, and SHA-256 hash for every imported table.
- Official special-dominion statements were checked against the *Dominions 6 Manual*, revision 2, especially pages 87-88.
- The official Modding Manual, version 6.34, supplies object-selection and field context but is not treated as proof of every player-facing display value.
- Source-confirmed, official, derived, unresolved-selection, and test-pending claims remain distinguishable.
- Long descriptions and artwork are excluded. The register stores factual fields, relationships, provenance, evidence, canonical links, and hashes rather than mirroring copyrighted game text.

## Import and Data Checks

- `tools/build_base_object_register.py` refuses an unexpected upstream revision unless an explicit refresh flag is supplied.
- Python compilation completed without error.
- Import assertions passed for category counts, stable-ID uniqueness, required fields, source lineage, and 64-character record hashes.
- All twelve website JSON files parse successfully.
- The base-object register validates against `base-object-register.schema.json` with an independent JSON Schema 2020-12 validator.
- Every one of the 4,196 `canonical_section_id` values resolves to a current heading or declared semantic alias.
- Rebuilding from the same pinned source produced deterministic category counts and a stable register hash of `14ed5c2205ca1d65187d4db336b80656ecda2b4f57d9d71430737d67673f657b`.

## Duplication and Ownership Checks

- Book XII contains 9,148 words and 71 numbered sections across eleven parts, followed by a source record.
- No internal block of at least fifteen words is repeated exactly.
- No Book XII prose paragraph of at least 35 words is repeated exactly elsewhere in the reader corpus.
- No such paragraph reached the 0.88 near-duplicate threshold against the earlier reader corpus.
- The book points to Books II-VI for economic, Pretender, magical, and strategic judgment rather than reproducing their formulas, doctrines, and worked explanations.
- Exhaustive object rows remain in JSON instead of being converted into thousands of pages of repetitive prose.
- Direct second-person address and machine-authorship language are absent from Book XII.

## Navigation and Website Checks

- Book XII has a stable website path at `/dominions/library/book-xii/`.
- Ten semantic aliases provide durable entry points for the register, spells, items, summons, Pretenders, Thrones and sites, mercenaries and independents, special dominions, website use, and maintenance.
- All Reader's Guide, glossary, research-register, reading-path, subject-index, ability-register, and alias destinations resolve.
- The content index contains 14 reader documents and 2,229 stable section records.
- The Reader's Guide now contains 205 subject entries, 100 glossary entries, six reading paths, and 55 research items.
- R-031 is marked completed against the current Throne records. R-053 through R-055 preserve the independent-population, unresolved-summon, and human-label work without asking the player to perform bespoke tests.
- The coverage register assigns the object domain to Book XII and the website data layer and marks G-03 substantially complete.

## PDF Checks

- PDF generation completed without an exception.
- The final file contains 655 A4 pages, 2,229 outline items, and 3,922 link annotations.
- Text extraction found no Unicode replacement characters and no page with fewer than 80 extracted characters.
- A full bounding-box scan found no body text below the content frame; the cover footer is the only intentional text in that region.
- The body fonts are embedded. The unembedded Helvetica entry is ReportLab infrastructure rather than manuscript text.
- The PDF metadata identifies Foundation Books I-XII and Progress Edition 15.
- The cover, Book XII contents entry, Reader's Guide opener, object-lookup table and continuation, website object model, research-register ending, Book XII opener, first-register table, section transitions, special-dominion table, limitation page, practical checklists, and final source page were rendered and visually inspected.
- Tables repeat their headers after page breaks, remain within the frame, and show no observed clipping or overflow.
- Running headers, footers, page numbers, bookmarks, internal links, and final-page whitespace remain consistent with the established reader design.

## Known Limits

The first object build does not claim a complete independent population-type catalogue. Twenty-five summon relations preserve unresolved engine selections. Some source-native item and site property names still need authoritative human labels, realm restrictions are not fully expanded to nation lists, and not every source-confirmed value has received an independent current-UI check. Weapons, armour, full unit records, events, and nation records remain separate schemas or future work.

## Remaining Foundation Priority

The next shared foundation is G-04, the complete official patch ledger. It should classify every official update, map each material change to a canonical chapter or object record, and provide the version-diff layer needed for dependable website maintenance. The searchable mod-command lexicon follows. Nation dossiers can then resume against the stable rules, object, and patch foundations.
