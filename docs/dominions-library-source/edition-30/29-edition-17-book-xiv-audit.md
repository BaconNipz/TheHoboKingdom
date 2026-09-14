# Progress Edition 17 and Foundation Book XIV Audit

## Publication result

Progress Edition 17 adds Foundation Book XIV, *The Command and Terminology Lexicon*, to the linked reader's edition. Book XIV is the canonical retrieval and reconciliation layer for official hash-token syntax. Book VIII remains the canonical home of parser, object-design, event, map, AI, compatibility, and testing instruction. Book XIII remains the canonical release chronology.

The compiled PDF contains 767 A4 pages and all sixteen reader-facing documents. Its final SHA-256 fingerprint is:

`7b8feb249f7a86bffbeca151f35f2b3d29e5607ce28f547de6f1987084411dc1`

## Ruleset and source boundary

The executable baseline is unmodded Dominions 6.35. The command register was extracted from the currently published official command-bearing manuals:

| Source | Internal version | Pages | SHA-256 |
|---|---:|---:|---|
| Dominions 6 Modding Manual | 6.34 | 65 | `5ac40698e05703f5628db123548c4e6a57fe0ed9bbcb65fb8f72fc589ab309ab` |
| Dominions 6 Event Modding Manual | 6.29 | 20 | `c494f8b660a22e1cbf6998d2570353dd46665e79ba8fe94b708b772ae1796ae5` |
| Dominions 6 Map Making Manual | 6.26 | 11 | `6441d5ffac56a33f8444ea3cd02cecfbefa36c0a45b8e4af7985cb3c45e1e729` |

The official file-format sheet was also checked. It contains data-layout notation but no hash command or double-hash message token, so it contributes no command records. The official 6.01-6.35 patch ledger contributes historical command expressions and provenance, not present syntax definitions. Its SHA-256 fingerprint is `784a0c6bda6a6b35305a73f281182f8719c008972e354a06330f61a03b1d43ff`.

## Extraction and reconciliation results

The register contains:

- 1,609 distinct official-manual hash tokens from 2,304 examined occurrences;
- 1,540 defined tokens, 60 reference-only tokens, and nine mention-only tokens;
- 1,567 literal tokens, thirteen official templates, and 29 double-hash message substitutions;
- 97 controlled search aliases derived from official terrain and numeric templates;
- 221 patch-note tokens reconciled with no unresolved entry.

The patch reconciliation consists of 196 exact defined matches, two exact reference-only matches, sixteen template aliases, three controlled spelling discrepancies, three family expressions, and one message placeholder. The three official spelling discrepancies are preserved rather than silently normalized:

- patch `#addseduction`; current Event Modding Manual `#addseductions`;
- patch `#illusionimmune`; current Modding Manual `#illusionsimmune`;
- patch `#res_mnrbs`; current Event Modding Manual `#req_mnrbs`.

The patch expressions `#not(dis)mounted`, `#force...vis`, `#battlesum1dX`, and `##varXXX##` are recorded as shorthand, families, or message grammar instead of being misrepresented as ordinary literal commands.

## Data and website validation

The website export contains sixteen documents, 2,432 searchable sections, 106 glossary entries, six reading paths, 57 research items, 212 subject entries, 93 ability records, and 213 maintained redirects.

The command dataset and schema passed the following checks:

- Draft 2020-12 JSON Schema validation;
- 1,609 unique record identifiers and command spellings;
- valid SHA-256 record hashes;
- every alias resolves to an existing official template record;
- every concrete patch target resolves to an existing command record;
- every manual page locator falls within its source document;
- summary totals equal the underlying collections;
- no unresolved patch reconciliation remains.

The schema pattern explicitly accepts both ordinary command records and the 29 message-placeholder records. This was corrected during audit after the first schema draft admitted only command-prefixed identifiers.

## Editorial validation

Book XIV contains no exact duplicated prose block of 35 words or more from the preceding books. Shared subjects are handled through ownership statements and cross-references. The authored chapters contain no direct second-person address and no first-person editorial narration. Generated appendices are bounded by explicit markers and can be regenerated without overwriting authored analysis.

Command descriptions are not copied wholesale from the official manuals. The public register retains spellings, syntax lines, versions, pages, section labels, evidence classes, and patch provenance; readers return to the cited manual for the official explanatory text.

## PDF validation

The final PDF passed structural and visual checks:

- 767 pages reported consistently by Poppler and `pypdf`;
- no blank page, replacement glyph, or leaked Markdown table escape;
- 2,432 valid outline destinations and no invalid outline destination;
- 4,329 link annotations: 4,256 internal links and 73 external source links;
- correct title, author, subject, edition label, date, and Books I-XIV running furniture;
- embedded DejaVu Sans, DejaVu Sans Bold, and DejaVu Sans Mono subsets;
- inspected cover, contents, Book XIV opening, source table, exception matrix, complete locator, template-alias register, patch-token index, and closing page;
- repeated table headers, alternating row treatment, code typography, margins, and footer legibility retained across the long generated appendices.

## Remaining evidence boundary

A current-manual locator proves that a spelling or template appears in the cited official document. It does not by itself prove every legal value, every interacting selector, combined-mod compatibility, or runtime effect. The 60 reference-only and nine mention-only entries remain visibly incomplete. Stronger claims should be added only as separately labelled official clarification, reproducible community implementation, parser acceptance, or observed runtime evidence tied to a game version and test conditions.

