# Progress Edition 13 - Book X Integration Audit

Audit date: 1 August 2026  
Game baseline: Dominions 6.35  
Reader corpus: Reader's Guide, field reference, and Foundation Books I-X

## Outcome

Foundation Book X closes coverage gap G-01 from the Edition 12 foundation audit. It supplies the operating layer that was previously underdeveloped: local files, game creation, joining and hosting, the main interface, current shortcuts, turn preparation, recruitment and army manipulation, strategic orders, a guided first campaign, troubleshooting, and host administration.

The book does not create a second rules encyclopaedia. Turn resolution remains in Book I; economy and recruitment mechanics in Book II; Pretenders and religion in Book III; battle in Book IV; magic in Book V; and campaign doctrine in Book VI. Book X links to those owners and explains how their rules are entered, inspected, submitted, and diagnosed in the interface.

## Deliverable Record

| Artifact | Result |
| --- | --- |
| Book X manuscript | 14,104 words; 96 numbered sections; 13 Parts including sources and research boundaries |
| Edition 13 PDF | 584 A4 pages; 2,657,646 bytes |
| PDF title | *The Dominions 6 Knowledge Library - Foundation Books I-X* |
| Website corpus | 12 reader documents; 2,025 stable sections |
| Reader paths | 6 |
| A-Z subject entries | 197 |
| Glossary entries | 92 |
| Research questions | 45 |
| Semantic redirects | 172 |

File fingerprints at audit time:

- Book X Markdown SHA-256: `046d7ba7a30b0fe01184434d2fca7c816530c2279e0b982d0c4761391bdc9889`
- Edition 13 PDF SHA-256: `bfb625c3a60e2db87e981232ac848e43083300abb7a4d33f304a37aa2bdd0c1b`

## Source Verification

The procedural claims were checked against:

1. the official *Dominions 6 Manual*, revision 2;
2. Illwinter's official Dominions 6 documentation index;
3. official announcements through Dominions 6.35;
4. official modding and file-format manuals for the local-data boundary;
5. the existing canonical foundation chapters for underlying mechanics.

The 6.35 pass specifically incorporated and checked:

- the F1 pillage filter;
- teleport movement out of a besieged fort;
- end-of-turn automatic mount recovery where applicable;
- victory revelation of the hidden map and scoregraphs for players remaining to the end;
- current spell-script display and AI corrections relevant to operations.

The accumulated interface pass also checked the official 6.25-6.30 additions used in Book X: battle version display, treasury autosort, lobby mod safety, broad order copy/paste, gem-transfer shortcuts, bless-entry shortcuts, improved ritual and destination messages, and larger network-turn handling.

Version-sensitive private-server command lines and external PBEM automation were deliberately excluded. The current official material does not provide a sufficiently frozen modern command specification for this edition, and copying older executable commands would violate the project's evidence standard.

## Duplication Audit

The complete reader corpus was scanned for normalized exact paragraph repetition of at least 25 words. No cross-document exact duplicate paragraph was found.

Book X was also compared with the other project Markdown using a near-duplicate pass on prose paragraphs of at least 45 words. The candidate threshold required both high vocabulary overlap and high sequence similarity. No near-duplicate paragraph passed the threshold.

The scope boundary was inspected manually in the sections most likely to repeat earlier work:

| Book X subject | Canonical mechanics owner | Book X treatment |
| --- | --- | --- |
| Hosting | Book I | Submission, lobby, administration, and diagnosis only |
| Recruitment | Book II | Queue and Army Setup operation only |
| Pretenders and prophets | Book III | Save/load, setup, and order procedure only |
| Battle orders and scripts | Book IV | Screen manipulation and audit only |
| Gems, rituals, and forging | Book V | Transfer and dependency checks only |
| Movement, war, diplomacy, Thrones | Book VI | Order entry and first-campaign workflow only |

## Navigation and Website Checks

- All 2,025 generated heading destinations are unique within their document scope.
- Every internal Markdown link in the reader corpus resolves to a current destination or a declared semantic alias.
- The website exporter completed without an unresolved reference or missing alias target.
- Book X has a stable website path at `/dominions/library/book-x/`.
- The coverage register assigns player operations to Book X and marks G-01 complete.
- The master plan now treats Books I-X as the completed general foundation and does not propose player operations again.

## PDF Checks

- PDF generation completed without an exception.
- Text extraction produced 224,000-plus words and no Unicode replacement characters.
- The PDF contains 319 outline items and more than 3,300 link annotations.
- No page contained fewer than 80 extracted characters; no accidental blank page was detected.
- Fonts used by the manuscript are embedded where expected.
- The cover, contents transition, Book X opener, settings table, turn audit, strategic-order table, first-campaign transition, hosting runbook, and closing page were rendered to PNG and visually inspected.
- The first render exposed a stale Edition 12 cover footer and a cramped baseline line. Both were corrected, the PDF rebuilt, and the affected pages reinspected.
- The final cover, running headers, contents, tables, lists, cross-references, and final page are legible and free of observed clipping or overflow.

## Editorial Voice Check

Book X uses direct procedural prose, concrete examples, varied paragraph construction, and bounded essays. It avoids claims about being generated, self-congratulatory process narration, fictitious quotations, and generic concluding boilerplate. Direct second-person address is avoided in the manuscript; imperatives are confined to procedures and checklists where they improve usability.

## Remaining Foundation Priority

With G-01 complete, the next shared reference priority is the systematic unit-class and special-ability reference. It should define and index abilities, experience, heroic abilities, and conditions, while linking combat consequences back to Book IV. Structured base-game object records, the complete official patch ledger, and the mod-command lexicon remain separate data projects.
