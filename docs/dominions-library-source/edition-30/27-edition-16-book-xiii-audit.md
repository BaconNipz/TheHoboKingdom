# Progress Edition 16 and Book XIII Audit

## Scope

This audit records the construction and verification of Foundation Book XIII, the official patch ledger, the Edition 16 website exports, and the compiled reader PDF. It is an internal publication record rather than a chapter of the reader-facing book.

The public baseline is unmodded Dominions 6.35. Dominions Enhanced 2.16 and Divinitus 1.15.3 DE remain separate frozen rulesets.

## Official-source completeness

The archived Steam app-news response has SHA-256:

```text
92ef3a1810af9383f461004d1a099db30e7923d025ee48ad039b04276542e65a
```

The importer identified 31 official `Dominions 6.xx` announcements and excluded the two non-announcement news items in the response. It parsed 1,064 non-empty list bullets. Completeness assertions confirm:

- first announcement: 6.01, 19 January 2024;
- last announcement: 6.35, 18 May 2026;
- announcements: 31;
- change records: 1,064;
- sum of release record counts: 1,064;
- unique record IDs: 1,064;
- public numbers without a matching announcement: 6.10, 6.20, 6.22, and 6.26;
- distinct `#commands` detected in source bullets: 221.

No content or date was invented for the four unannounced numbers. They are not described as missing releases.

## Evidence and copyright boundary

Every patch record contains an official announcement identity, URL, section, bullet index, source sequence, source-text hash, and source word count. The source bullet is official. Classification, confidence, domains, materiality, direction, named terms, object mentions, impact summary, and canonical destinations are project derivations.

The public JSON does not contain the full official bullet text. The locally archived source response remains excluded from the publication files and project archive. This preserves reproducibility and source verification without republishing the announcement corpus.

## Classification result

All 1,064 records have a primary change class and at least one affected domain. The class totals sum exactly to 1,064.

| Confidence | Records | Publication treatment |
| --- | ---: | --- |
| High | 783 | Mapped and suitable for ordinary filtering |
| Medium | 26 | Mapped with restrained analytic use |
| Editorial review | 255 | Source-complete and searchable; fine-grained class remains review-recommended |

No record is omitted from the ledger because its derived category remains uncertain. Editorial revisions will change record hashes while leaving the official source hashes untouched.

## Book XIII editorial result

Book XIII contains 8,582 indexed words and 87 stable headings. Its new contribution is restricted to:

- official chronology and source method;
- a complete release spine;
- change classification and evidence boundaries;
- player-facing stale-rule analysis by system;
- command chronology;
- stale-guide repair and dependency-driven maintenance;
- website and update workflows;
- essays on versioned rules, bug-fix history, and maintenance as authorship;
- practical reader, author, host, and maintainer checklists.

The volume does not reproduce the current-rule explanations owned by Books I-XII. It routes readers to those owners. An exact long-paragraph comparison across all 15 reader documents found zero duplicate groups of 180 or more normalized characters. The new manuscript contains no direct second-person pronouns and no first-person editorial voice; Roman numerals account for the isolated token `I`.

## Navigation and website integration

Edition 16 exports contain:

- 15 reader documents: the Reader's Guide, field reference, and Books I-XIII;
- 2,318 stable sections;
- 201 semantic redirects;
- 206 subject-concordance entries;
- 102 glossary entries;
- 56 active research records;
- 93 ability records;
- the existing 4,196-record base-object register;
- the new 1,064-record official patch ledger.

Book XIII adds twelve semantic aliases for the official ledger, release timeline, classification model, domain map, editorial-review queue, player-facing changes, command chronology, stale-guide repair, performance and stability, presentation maintenance, website use, and feed maintenance.

Research item R-001 is now in progress: the complete official patch side is present, while the command-by-command current-manual comparison belongs to the next lexicon. R-056 records the bounded classification-review queue.

## Machine validation

The following JSON pairs validate under JSON Schema draft 2020-12 with Ajv 8 and format validation:

- `official-patch-ledger.json` against `official-patch-ledger.schema.json`;
- `base-object-register.json` against `base-object-register.schema.json`;
- `article-template.json` against `content.schema.json`.

The website builder completed with every semantic alias resolved and every generated JSON file parseable.

## PDF verification

The final reader PDF contains 683 A4 pages. Foundation Book XIII begins on page 660 and ends on page 683. The PDF metadata title is *The Dominions 6 Knowledge Library - Foundation Books I-XIII*.

Visual checks covered:

- cover and edition label;
- contents overview and linked entries;
- Reader's Guide patch-history navigation table;
- Book XIII opener and source links;
- transition into the complete release spine;
- 2024-2026 chronology tables;
- classification tables and list layout;
- command-chronology transition;
- essay transition;
- final page, footer, and page number.

The first pass exposed insufficient clearance at one major section transition. The global major-heading spacing was increased, the PDF rebuilt, and the affected pages re-rendered. Final Poppler rendering and text-coordinate checks show clean margins, headers, footers, tables, lists, links, and section transitions.

Final PDF SHA-256:

```text
221787758744d98e7504e7ea519adc75095712de74a73238f0954aa50affe314
```

## File hashes

| File | SHA-256 |
| --- | --- |
| `26-foundation-book-xiii-official-patch-history.md` | `dc3dd9632ca132a7f404bd3d2fedcb4ea7f5b3d3c6f53c57e9fc9067804a3cf2` |
| `website/official-patch-ledger.json` | `784a0c6bda6a6b35305a73f281182f8719c008972e354a06330f61a03b1d43ff` |
| `website/official-patch-ledger.schema.json` | `1e88cdea606ecbfdb3b79146a17b8c3df3cffa9e6b30f289b12ecb778c101844` |
| `dominions-6-knowledge-library-progress-edition-16.pdf` | `221787758744d98e7504e7ea519adc75095712de74a73238f0954aa50affe314` |

## Explicit limitations and next work

- Fine-grained classification review remains for 255 records; source collection is complete.
- The patch ledger proves command mention and chronology, not complete command syntax.
- Public version numbers without matching announcements remain unexplained.
- The object register's independent-population and selection-based-summon limitations remain unchanged.
- The next shared foundation is the command lexicon, after which nation dossiers can resume against stable rule, object, version, and syntax layers.
