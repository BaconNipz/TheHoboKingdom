# Progress Edition 22 - Divine Timing Audit

**Release date:** 25 August 2026  
**Live game baseline:** Dominions 6.36  
**Structured object snapshot:** Dominions 6.35 Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`  
**Scope:** Book III, Book I timing cross-references, Book VI Throne operations, Evidence Ledger, Reader's Guide, website exports, and the linked reader's PDF

## Purpose

Edition 22 is an evidence and maintenance release rather than Foundation Book XV. It returns to the unresolved Book III timing questions R-014, R-017, and R-018, adds only what survives source reconciliation, and preserves the difference between official rules, published controlled research, current community reference, historical reverse engineering, and direct current-version testing.

## Canonical placement

Awakening, Call God, and the mechanical Throne claim-loss state live in Book III. Book I retains the common hosting order and links to Book III for the resolved ownership result. Book VI retains campaign arithmetic, rushes, and counterplay. No second Pretender, recovery, or Throne book has been created.

## Research decisions

| Item | Edition 22 decision | Evidence boundary |
| --- | --- | --- |
| R-014 - awakening distribution | Remains queued | The manual establishes approximately turns 10-13 and 28-42 and roughly half-time Disciples. An older Dominions 5 exploding-die model is only a test hypothesis until reproduced under 6.36. |
| R-017 - Call God | Completed | Official Holy, Disciple-game, Elegist, Recall God, Trinity, home-province, and hosting rules are reconciled with published controlled research establishing a fixed 50-point base and effective-rating `-1/0/+1` monthly contributions. Detailed routing and capital or fort placement remain Current Community Reference. |
| R-018 - same-turn Throne ownership | Completed | Official hosting and ownership rules, the current conquest rule, and a published same-turn report establish claimant-death, unfortified-conquest, siege, and fort-storm outcomes. Exact simultaneous winning-total ties remain separate. |

## Awakening result

The official ranges remain the publication baseline. The new section explains how to plan against the late end of each range, why a midpoint is not an expected value, and why an Incarnate design must be evaluated in pre- and post-awakening states. The controlled-test programme now requires independent seeds, raw outcomes, confidence intervals, and explicit comparison against the old candidate formulas instead of a small convenience sample.

## Call God result

For an ordinary positive effective recall rating, published testing supports a monthly contribution of rating minus one, rating, or rating plus one. The effective rating begins with Holy level, adds Elegist, and receives any applicable official Recall God modifier. The ordinary pool is fixed at 50. Combining that tested base with the manual's 50% Disciple-game increase gives 75 for the main Pretender in a Disciple game.

The chapter supplies caller ranges and planning times for H1, H2, H3, groups, and an Elegist example. It separately labels cross-team Disciple routing and return placement because those details come from current community documentation rather than the revision-2 manual. The official step-16 order also establishes the interruption boundary: an earlier removal can prevent contribution, while a later assassination or battle cannot undo points already added that month.

## Throne timing result

A step-8 claim is not an immediate victory. It survives later claimant death if the nation retains the Throne. Conquest of an unfortified Throne, or successful storming of the fort containing one, unclaims it before the step-57 victory check. A siege without fort conquest does not. Book III carries the full state matrix, Book I carries the turn order, and Book VI applies the result to endgame operations.

## Editorial safeguards

- Older Dominions 5 reverse engineering is never presented as a current Dominions 6 law.
- Community-tested formulas remain distinct from official text.
- Current community routing and placement details remain distinct from controlled research.
- Historical Edition 19 through Edition 21 audit files remain unchanged as release records.
- Exact simultaneous victory ties remain open rather than being folded into R-018.
- The same-turn matrix is stated once in full and cross-referenced from the timing and strategy books.

## Sources added or rechecked

- Dominions 6 Manual, revision 2;
- Dominions 6 Modding Manual 6.34;
- official Dominions 6 release record and change history through 6.36, rechecked 25 August 2026;
- current Dominions 6 Pretender, Elegist, and Throne references;
- Loggy's published Call God research notes;
- published same-turn Throne claim report;
- legacy Pretender mechanics page, used only as a historical awakening and Trinity test lead.

## Build verification

The rebuilt website export contains 16 reader documents, 2,466 indexed sections, 106 glossary entries, 213 subject entries, 57 research items, 93 ability records, and 213 redirects. R-014 remains queued; R-017 and R-018 are completed and resolve to their canonical Book III headings. All 16 JSON outputs parse, every generated section reference resolves, the official patch builder retains 32 announcements and 1,090 records, and the command builder reconciles 226 patch tokens with no unresolved token.

The reader corpus contains zero exact cross-document prose duplicate groups at the audited paragraph threshold. No reader document contains a repeated level-one or level-two heading. The controlled assistant-chatter search returns no substantive matches, and every fenced code block is balanced.

The linked reader's PDF contains 787 A4 pages and 225,456 source words. Text extraction found no blank pages and no replacement glyphs. The file contains 4,372 link annotations: 4,287 internal links and 85 external links. Its outline contains 421 top-level entries and 2,466 total destinations.

Visual inspection covered the cover; the awakening range and planning table; the transition into the opening chapter; the same-turn Throne sequence and state matrix; all Call God formula, capacity, Disciple-routing, return, and evidence-decision pages; the revised awakening regression test; the Book III source record; and the closing page. Tables remain within the text frame, continuation pages are clean, edition labels and footer dates are current, and no clipping or overlap was observed.

**PDF SHA-256:** `d1d6d87ca9a00035f6d6185ff9e1c916ab7a16ed9fae773e214398695189677c`  
**PDF size:** 3,594,553 bytes
