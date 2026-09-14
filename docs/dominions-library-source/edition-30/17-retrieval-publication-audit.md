# Retrieval and Publication Audit

## Scope

This audit covers the Reader's Guide, stable PDF navigation, machine-readable website exports, and research triage added on 1 August 2026.

## Reader layer

The Reader's Guide contains:

- six purpose-built reading paths;
- five groups of problem-based navigation tables;
- 192 alphabetical subject entries;
- 92 expanded glossary definitions;
- 45 active foundational research questions;
- a blocked-engine register that explicitly avoids transferring test work to the player;
- maintenance rules for adding, moving, replacing, and cross-linking sections.

The guide is an orientation layer. It does not become a second authority for formulas, exact object definitions, or full rules explanations.

## Stable navigation

The reader corpus contains 11 documents and 1,846 headings. Each heading receives a deterministic destination derived from its document and title. Duplicate headings within one file receive stable numeric suffixes. The current edition also defines 151 semantic aliases for readable, durable references.

PDF navigation now includes:

- linked table-of-contents entries;
- stable bookmarks for every heading;
- internal links in the Reader's Guide and concordance;
- automatic links for ordinary `Book N`, `Book N Part N`, and Book IX section references;
- semantic redirect destinations that remain valid when a link uses a clearer subject name than the printed heading.

## Website exports

The `website` directory contains:

- a Draft 2020-12 JSON Schema;
- a schema-valid article template;
- the complete heading and hierarchy index;
- reading-path, subject-index, glossary, research-register, and redirect exports;
- publication notes explaining which fields still require claim-level review.

The schema supports versioned rulesets, mod load order, hashes, sources, evidence-labelled claims, formulas, content blocks, related sections, unresolved research, verification dates, and supersession.

## Research triage

The active register is ordered as follows:

1. P0 ruleset and source integrity;
2. P1 high-frequency economy, Pretender, combat, magic, movement, diplomacy, and victory rules;
3. P2 advanced magic, assassination, Cataclysm, parser, and transformation behaviour;
4. P3 specialist event, performance, AI, save, and network questions.

All active items identify a reliable resolution route. Engine-only questions without a published reproduction remain blocked and are not requests for player testing.

## Validation standard

Edition 12 is not complete until:

- every Markdown destination resolves to a heading or declared alias;
- every alias resolves to an existing heading;
- every generated JSON file parses;
- the schema and article template validate;
- the PDF contains no empty pages;
- bookmark and link annotations are present;
- representative pages render without clipping, overlap, missing glyphs, or broken tables.

## Final result

The completed Progress Edition 12 passed the standard above:

- 541 A4 pages;
- 1,846 PDF outline entries;
- 3,011 link annotations across 89 pages;
- no empty pages;
- no unresolved authored links;
- no aliases pointing to missing headings;
- no visible generator markers;
- no exact substantial paragraphs repeated across reader documents;
- no cross-document semantic matches at a cosine-similarity threshold of 0.82;
- eight generated JSON files, all parseable;
- Draft 2020-12 schema accepted and the article template validated against it;
- cover, guide opening, learning paths, concordance, glossary, website model, research register, maintenance rules, book transitions, Book IX, and the final page visually inspected.
