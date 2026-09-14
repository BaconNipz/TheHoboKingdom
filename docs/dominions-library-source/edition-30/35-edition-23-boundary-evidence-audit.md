# Progress Edition 23 - Boundary Evidence Audit

**Release date:** 25 August 2026  
**Live game baseline:** Dominions 6.36  
**Structured object snapshot:** Dominions 6.35 Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`  
**Scope:** Book II, Book III awakening evidence, the Turn and Economy Quick Reference, Evidence Ledger, Reader's Guide, website exports, and the linked reader's PDF

## Purpose

Edition 23 is an evidence-readiness release rather than Foundation Book XV. It returns to R-008 and R-010 through R-014, but does not equate a plausible formula with a verified engine rule. The revision makes each unresolved claim smaller, identifies the exact observation that would settle it, and gives players a safe value to use in the meantime.

## Canonical placement

Economic arithmetic remains in Book II. Awakening remains in Book III. The field reference carries only the decisions needed while issuing orders, while the Evidence Ledger records source strength and the Reader's Guide routes the open questions. No second economy, logistics, or Pretender chapter has been created.

## Research decisions

| Item | Edition 23 decision | Evidence boundary |
| --- | --- | --- |
| R-008 - rounding | Remains queued | Six separate rounding subsystems are now distinguished. One official resource contribution is floored, but the printed aggregate remains inconsistent and cannot define the other chains. |
| R-010 - upkeep | Remains in progress | Published annual entries exclude a simple final floor for the observed 7- and 16-gold units. They do not distinguish ceiling from nearest-integer display or settle monthly treasury fractions and shape bases. |
| R-011 - unrest and recruitment capacity | Remains queued | The current community wording yields explicit loss-floor candidate thresholds for one-, two-, and three-point Commander Point pools. It still lacks a version-labelled boundary reproduction and does not state which intermediate is rounded. |
| R-012 - fort supply | Remains queued | Maximum range, distance limit, and highest-fort selection are secure. The official `x6` formula and `x4` table remain incompatible, so both printed candidates are exposed instead of averaged. |
| R-013 - starvation | Remains in progress | Need Not Eat and transformation immunity remain established. Update 6.35 makes Supply Usage after item changes an official display-state boundary, while generic feeding priority remains unproven as immunity. |
| R-014 - awakening distribution | Remains queued | A June 2026 Dominions 6 page republishes Loggy's exact model, but the formula is traceable to pre-Dominions 6 notes, has no published 6.x raw sample, and carries a displayed-turn discrepancy with the manual. |

## Rounding result

The new Book II map separates provincial income, resources, Recruitment Points, Commander Points, upkeep, and fort supply. Each row identifies the written rule, the unknown conversion, and the current interface value that should govern an order. This prevents an observed floor in one subsystem from being silently reused in another.

The upkeep observations provide one narrow result. Ordinary gold bases of 7 and 16 produce exact annual equivalents of 5.6 and 12.8 but display 6 and 13. A final floor is therefore incompatible with those cases. Ceiling, nearest-integer display, earlier fixed-point arithmetic, and the monthly treasury treatment are not distinguished by the sample.

## Unrest and fort-supply result

The current community unrest page says that each unrest point removes one percent of Recruitment Points and similarly affects Commander Points, with the effect rounded down. For a small pool, rounding the loss and rounding the remainder are different operations. Book II now gives the thresholds predicted by the loss-floor reading and labels them as candidate observations rather than a current rule.

The fort-supply revision separates agreement from conflict. The manual consistently limits projection to four provinces and uses only the largest nearby fort contribution. Its explicit formula uses six times Administration, while its percentage table and one worked example use four. The two systems now form a documentary interval for risk review; that interval is not asserted to contain the executable result.

## Starvation and interface-state result

The priority claim has been narrowed. "Commanders are fed first" does not mean "commanders cannot starve," because no current source shows what happens once lower-priority eligible consumption is exhausted. The same warning applies to animals being fed last.

Official update 6.35 fixed Supply Usage failing to update after magic-item changes. Evidence gathered before that correction can therefore be stale when equipment changes size, appetite, supply production, mounts, or forms. Under the 6.36 baseline, the refreshed display is the intended operational total, although it does not expose the later starvation-selection order.

## Awakening source trace

The current Dominions 6 Pretender-design page was revised on 16 June 2026 and now attributes four exact exploding-die formulas to Loggy. Searching the formula text reaches Loggy's older miscellaneous reverse-engineering notes and copies published before Dominions 6. The current page does not publish raw 6.x outcomes, a save, a test protocol, or an engine trace. It also describes ordinary displayed ranges of turns 11-14 and 29-42, while the revision-2 manual says approximately 10-13 and 28-42.

The formula is therefore a well-specified current community hypothesis with historical provenance. It is not yet a current-version distribution. Opening plans continue to use the official ranges and survive their late endpoints.

## Editorial safeguards

- No open research item is marked complete merely because its candidate formula is precise.
- An official interface correction is not presented as a formula correction.
- Candidate thresholds are labelled where they appear, not hidden in a distant source note.
- The field reference repeats only order-writing consequences; Book II owns the full evidence discussion.
- Historical Edition 21 and Edition 22 audit files remain unchanged as release records.
- The frozen DE 2.16 then Divinitus 1.15.3 DE load order remains separate from unmodded formulas.

## Sources added or rechecked

- Dominions 6 Manual, revision 2;
- Dominions 6 Modding Manual 6.34;
- official Dominions 6 announcements through 6.36, including the 6.35 Supply Usage correction;
- current Dominions 6 unrest, supplies, starvation, population, and Pretender-design references;
- December 2025 in-game upkeep observations under Dominions 6.33;
- Loggy's miscellaneous reverse-engineering notes and older public copies of the awakening formula;
- pinned Dominions 6 Inspector object snapshot at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

## Build verification

The rebuilt website export contains 16 reader documents and 2,466 anchored sections, supported by 106 glossary entries, 213 subject records, 57 research records, 93 ability records, and 213 redirect records. All 16 JSON exports parse successfully. The official patch ledger contains 1,090 records from 32 announcements, while the command lexicon contains 1,609 tokens, including 226 patch-derived tokens, with no unresolved command references.

The reader corpus has no exact cross-document paragraph duplicate groups at the forty-word threshold, no repeated level-one or level-two headings, no unbalanced code fences, no invalid alias targets, and no conversational drafting residue. Research statuses remain deliberately open: R-008, R-011, R-012, and R-014 are queued; R-010 and R-013 remain in progress.

The publication PDF contains 790 A4 pages, 2,466 outline destinations, and 4,374 links: 4,287 internal and 87 external. It contains no blank pages or replacement glyphs. The cover, rounding map, upkeep observation table, unrest candidates, fort-supply conflict, starvation display correction, awakening source trace, section transitions, and closing pages were rendered and inspected without clipping, overlap, or broken layout.

**PDF:** `dominions-6-knowledge-library-progress-edition-23.pdf`  
**Size:** 3,601,851 bytes  
**SHA-256:** `e84ab52510ae4e86af64cf7a38060eeffb290c11ace1f76531a486567c7907e0`
