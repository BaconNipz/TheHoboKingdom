# Progress Edition 14 and Book XI Audit

## Scope

This audit records the checks applied to Foundation Book XI, *Units, Abilities, Experience, and Conditions*, and to the linked Progress Edition 14 PDF and website exports. The audit date is 3 August 2026. The game baseline is Dominions 6.35.

## Outcome

Book XI closes G-02 in the foundation coverage register. It supplies a general unit-reading method, a taxonomy of major ability families, official experience thresholds, a bounded Hall-of-Fame and heroic-ability reference, condition and recovery guidance, a counter matrix, and a structured website register. Book IV remains the canonical owner of combat resolution and is linked wherever a complete formula or battle procedure would otherwise be duplicated.

## Source and Evidence Checks

The volume was checked against:

- the official *Dominions 6 Manual*, revision 2;
- the official Modding Manual, version 6.34;
- official patch announcements through Dominions 6.35;
- current community reference pages for Dom6 unit abilities and experience;
- older community reverse engineering for the Hall of Fame and heroic abilities.

Official, patch, current-UI, community-tested, derived, and test-pending layers are identified separately. Older heroic formulas are not presented as current official rules. The apparent conflict between the official incremental experience table and the current community cumulative Hit Point total remains visible, and the public calculator is explicitly blocked until a current 6.35 unit or engine export resolves it.

## Duplication and Ownership Checks

- Book XI contains 14,292 words and 76 numbered or named sections across fifteen parts.
- No long paragraph is repeated exactly within Book XI.
- No Book XI paragraph of at least 35 words reached the 0.88 near-duplicate threshold against the rest of the reader corpus.
- The book does not reproduce Book IV's melee, damage, fatigue, morale, affliction-location, battle-magic, or trample procedures beyond the minimum definition needed for retrieval.
- Economic, strategic, magical, religious, and operational consequences link to Books II, III, V, VI, and X instead of creating replacement chapters.
- Direct second-person address and machine-authorship language are absent from the manuscript.

## Navigation and Website Checks

- All internal Markdown links in the reader corpus resolve to a current destination or declared semantic alias.
- Book XI has a stable website path at `/dominions/library/book-xi/`.
- Seven semantic aliases provide durable entry points for unit reading, classes, abilities, experience, heroic abilities, conditions, and counters.
- The content index now contains 13 reader documents and 2,132 stable section records.
- The Reader's Guide now contains 204 subject entries, 98 glossary entries, six reading paths, and 52 active research items.
- `website/ability-register.json` contains 93 records generated from the marked Book XI table. Every record includes category, core function, principal caveat or counter, evidence layer, game baseline, and canonical section.
- The coverage register assigns G-02 and the unit-and-ability domain to Book XI and marks the gap complete.
- Python compilation and JSON parsing completed without error.

## PDF Checks

- PDF generation completed without an exception.
- The final file contains 623 A4 pages, 351 outline items, and 3,640 link annotations.
- Text extraction found no Unicode replacement characters and no page with fewer than 80 extracted characters.
- The manuscript fonts are embedded; the unembedded Helvetica entry is ReportLab infrastructure rather than body copy.
- The PDF metadata identifies Foundation Books I-XI and Progress Edition 14.
- The cover, contents, Book XI contents entry, Book XI opener, evidence table, experience table continuation, condition-to-register transition, register continuation, audit tools, patch table, verification queue, source record, and final page were rendered and visually inspected.
- Tables repeat their headers across page breaks, remain inside the frame, and show no observed clipping or overflow.
- Running headers, footers, page numbers, bookmarks, internal links, and final-page whitespace are consistent with the established reader design.

## Editorial Voice Check

The book uses compact definitions, consequence-led explanations, operational audits, and bounded essays. It avoids generic motivational filler, fictitious quotations, process narration, and claims of exhaustive certainty. Community findings are described in ordinary editorial language and receive an evidence warning where current verification is incomplete.

## Remaining Foundation Priority

With G-01 and G-02 complete, the next shared foundation is the structured base-game object database: spells, items, summons, Pretender forms, Thrones, sites, mercenaries, independents, and special dominions. A complete patch ledger and searchable mod-command lexicon remain separate structured-data projects. Nation dossiers remain deferred until these reusable records can prevent repeated object research.
