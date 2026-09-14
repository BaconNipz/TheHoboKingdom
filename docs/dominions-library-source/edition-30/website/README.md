# Dominions 6 Website Export

This directory is the publication bridge between the manuscript and TheHoboKingdom website. It does not replace the Markdown books. It gives a site generator stable destinations, searchable metadata, reading routes, glossary entries, redirects, and a claim-oriented schema.

## Files

- `content.schema.json` defines articles, sections, content blocks, formulas, claims, rulesets, evidence labels, sources, related sections, and revision metadata.
- `article-template.json` is a schema-valid starting record for a new page.
- `content-index.json` lists every heading in the reader corpus with its parent, source line, PDF destination, website URL, aliases, audience, and provisional topic tags.
- `reading-paths.json` exports the six routes from the Reader's Guide.
- `subject-index.json` exports the A-Z concordance.
- `glossary.json` exports the expanded glossary without separating it from its authoritative section links.
- `research-register.json` exports the active foundation queue.
- `ability-register.json` exports the marked Book XI records for unit classes, abilities, experience, heroic traits, and conditions, including category, caveat or counter, evidence layer, and canonical section.
- `perception-matrix.json` publishes the Edition 28 split between strategic concealment, melee Attack penalties, image defenses, and technical creature classes, including the superseded −9 versus current −10 Invisibility record and R-058 boundary.
- `base-object-register.json` is the versioned 6.35 record layer for spells, items, summon relations, Pretender forms, Thrones, other sites, mercenary companies, independent-coverage status, and special dominion systems.
- `base-object-register.schema.json` defines the shared envelope, provenance, and category-specific fields used by those object records.
- `official-patch-ledger.json` records all 32 official public updates and all 1,090 announcement bullets from 6.01 through 6.36 as source-linked, hashed, classified maintenance records without republishing the full announcement text.
- `official-patch-ledger.schema.json` defines the release, source, classification, confidence, domain, command, canonical-link, and hash contract for the patch ledger.
- `command-lexicon.json` locates all 1,609 distinct hash tokens found in the current official Modding, Event Modding, and Map Making manuals, records their syntax contexts and documentation status, generates controlled template aliases, and reconciles all 226 patch-note tokens, including five official 6.36 patch-only event commands awaiting full manual syntax.
- `command-lexicon.schema.json` defines the command, manual locator, evidence, domain, alias, patch-reconciliation, caution, and record-hash contract.
- `coverage-register.json` records canonical topic ownership, genuine gaps, current patch assignments, and the mandatory pre-draft duplication gate.
- `redirects.json` maps durable semantic aliases to the headings used in the current edition.

## Publication rule

The index is suitable for navigation immediately. Claim-level publication requires the prose to be split into content blocks and each factual claim to receive a ruleset, evidence status, and source list. Empty `rulesets`, `evidence_status`, `related_section_ids`, and `last_verified` fields in the heading index are therefore honest work markers rather than missing validation.

Before creating a new page, consult `coverage-register.json`. If a subject already has a canonical owner, the new page must be a correction, a clearly bounded application, a structured reference record, or a genuinely new procedure. A second general explanation should be replaced with a link to the existing owner.

The base-game register intentionally preserves source fields separately from editorial tags. A public object page should display the source commit, game version, record hash, evidence layer, and known limitations. Strategic explanations belong in Books II-VI; object pages link to those chapters instead of copying them.

The patch ledger makes the same separation between official source identity and editorial interpretation. Every source bullet is official; its change class, domains, materiality, named terms, and canonical links are derived. Records marked `mapped-review-recommended` remain valid source locators but should not be used as settled analytic categories until reviewed.

The command lexicon is a locator rather than a republication of the manuals. It preserves official token spellings, syntax lines, pages, versions, and section locations but leaves long explanatory prose in Illwinter's documents. Defined, reference-only, mention-only, template, alias, message-placeholder, and patch-reconciliation states must remain visible in public filters. Its current metadata remains tied to the complete 6.34 extraction; Edition 28's focused perception matrix separately uses the live 6.36 Modding Manual and does not silently remap the older page locators.

## Rebuilding

Run `tools/build_base_object_register.py` against the pinned 6.35 inspector source whenever the object data is refreshed. Run `tools/build_official_patch_ledger.py --source-json tmp/steam-news.json --supplemental-json data/official-update-6.36.json` to reproduce the current patch layer from the archived official feed and the separately preserved 6.36 announcement. Run `tools/build_command_lexicon.py` after any manual or patch-ledger change, then `tools/update_book_xiv_appendices.py` to refresh the printed locators. Finally run `tools/build_website_exports.py` after headings, glossary entries, reading paths, research questions, or semantic aliases change. The builders preserve the evidence boundary and refuse an unpinned object source, unresolved patch token, unresolved internal reference, or alias whose destination no longer exists.
