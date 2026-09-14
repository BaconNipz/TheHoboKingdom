# Progress Edition 20 - Blessing and Dominions 6.36 Audit

**Release date:** 20 August 2026  
**Live game baseline:** Dominions 6.36  
**Structured object snapshot:** Dominions 6.35 Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`  
**Scope:** Foundation Books I-XIV, website exports, official patch ledger, command lexicon, and the linked reader's PDF

## Purpose

Edition 20 is a maintenance and evidence release, not a new Foundation Book. It completes the active blessing question R-016, advances the live unmodded baseline to 6.36, and preserves the separately versioned 6.35 object snapshot instead of presenting an unaudited data refresh as current fact.

## R-016 closure

Book III now separates the blessing system into independently testable gates:

- battlefield blessing for ordinary effects;
- no battlefield gate for innate effects;
- active-and-alive Pretender state for Incarnate effects;
- friendly-dominion limits for automatic personal and troop blessing;
- repeatable blessings versus explicit overlap exceptions;
- on-hit, on-damaging-hit, weapon-property, attack-field, and special weapon-trigger families;
- item-granted and sacred-only automatic blessing routes;
- rider and mount records with independent Sacred state;
- display evidence versus engine-state evidence.

The chapter does not use R-016 to absorb adjacent problems. Cross-source stacking remains R-049. Shape and effect lifetime remain R-040 and R-052. The official 6.34 Life after Death item-blessing case is recorded as a bounded exception rather than a universal transformation rule.

## Corrected prior claim

Frost Mist Weapons requires Water 7 and Cold 1. The revision-2 manual and current community reference agree. Progress Edition 19 had removed the Cold requirement on the strength of an unsupported transcription; Book III and the Evidence Ledger now correct that error, and the historical Edition 19 audit carries a supersession note.

## Dominions 6.36 ingestion

The official 6.36 announcement contributes 26 source bullets. The rebuilt patch layer now contains:

| Measure | Edition 20 result |
| --- | ---: |
| Official announcements | 32 |
| Official change records | 1,090 |
| High-confidence classifications | 820 |
| Medium-confidence classifications | 20 |
| Editorial-review classifications | 250 |
| Distinct named hash commands | 226 |

The release-specific source capture is preserved as `data/official-update-6.36.json`. The importer retains the established gaps at 6.10, 6.20, 6.22, and 6.26 without inventing releases or dates.

## Command-lexicon reconciliation

The three current command-bearing manuals still yield 1,609 distinct tokens and 97 controlled aliases. Five commands named by 6.36 are newer than the current Event Modding Manual: `#gainaffmount`, `#healaffmount`, `#newnbor`, `#remnbor`, and `#req_provnbr`.

These records are classified as **official patch-only**. Their spelling, release, source locator, and canonical domain are published; arguments and full parser semantics are not invented. The lexicon now reconciles all 226 patch tokens with zero unresolved records.

## Canonical routing

The 6.36 material was placed in existing owners:

| Change family | Canonical home |
| --- | --- |
| Bless-load cancellation and blessing interaction audit | Book III |
| Rust on a zero-damage attack | Book IV |
| Lost Land, Perpetual Storm, and route consequences | Book VI |
| Touchscreen mode and interface shortcuts | Book X |
| Swimming mounts, charm allegiance, and mounted recruitment state | Book XI |
| Complete release chronology and replay correction | Book XIII |
| New command provenance and documentation gaps | Books VIII and XIV |
| Blood-sacrificer item-order correction | Independent Blood Magic paper |

This routing preserves the single-canonical-content model. Book XIII explains when a rule changed; the owning system book explains how the current rule is used.

## Text and structure checks

- Website export completed with 16 documents, 2,450 sections, 106 glossary entries, 213 subject entries, 57 research items, and 213 redirects.
- R-016 exports as `completed` and points to `b3-the-activation-state-machine`.
- The reader corpus contains zero exact cross-document prose duplicate groups at the audited paragraph threshold.
- No duplicate level-one or level-two headings remain in the reader corpus.
- Python sources compile, JSON outputs parse, and all website section references resolve.
- The official patch ledger asserts 32 announcements and 1,090 records.
- The command lexicon asserts 1,609 manual tokens, 226 patch tokens, five official patch-only entries, and zero unresolved patch tokens.

## PDF verification

The linked reader's PDF contains 778 A4 pages. Text extraction found no blank pages and no replacement glyphs. The document contains 4,359 link annotations: 4,282 internal links and 77 external links. The outline contains 421 top-level entries.

Visual inspection covered the cover, activation state table, weapon-trigger table, item and mount sections, R-016 decision, touchscreen section, mount section, 2026 release table, 6.36 patch-only command discussion, and closing page. Tables remain within the text frame, headings and footers are consistent, and no clipping or overlap was observed.

**PDF SHA-256:** `bcb1f2233938555799413f6c187f801c25171e331f4d398a77c75d5765b9a496`  
**PDF size:** 3,554,164 bytes

## Remaining boundaries

Edition 20 does not claim a 6.36 structured object export. Book XII remains a 6.35 snapshot. The five new event commands lack complete official syntax. Runtime-only questions still require reliable published evidence or a version-matched export. The next high-priority shared questions are R-008 through R-014, R-017, and R-018; nation dossiers remain deferred until a concrete faction task is selected.
