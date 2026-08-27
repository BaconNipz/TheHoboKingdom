import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const publicationMetadata = Object.fromEntries(
  fs.readFileSync(path.join(repositoryRoot, "_data", "dominions_library.yml"), "utf8")
    .split(/\r?\n/)
    .map((line) => line.match(/^([a-z0-9_]+):\s*["']?(.*?)["']?\s*$/))
    .filter(Boolean)
    .map((match) => [match[1], match[2]]),
);
// Edition 26 updated the complete PDF. The website reference layer is still
// generated from the last complete structured corpus, retained under edition-25.
const sourceRoot = path.join(repositoryRoot, "docs", "dominions-library-source", "edition-25", "generated");
const libraryRoot = path.join(repositoryRoot, "dominions", "library");
const bookRoot = path.join(libraryRoot, "books");
const dataRoot = path.join(libraryRoot, "data");

const readJson = (file) => JSON.parse(fs.readFileSync(path.join(sourceRoot, file), "utf8"));
const manifest = readJson("manifest.json");
const readingPaths = readJson("reading-paths.json");
const research = readJson("research-register.json");
const glossary = readJson("glossary.json");
const linkMap = readJson("link-map.json");
const editionLabel = publicationMetadata.edition_label;
const editionNumber = publicationMetadata.edition;
const pdfDownload = publicationMetadata.download_url;
const ogImage = publicationMetadata.cover_image;
const pdfPageCount = publicationMetadata.pdf_page_count;
const gameVersion = publicationMetadata.game_version;

const escapeHtml = (value = "") => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

const libraryHref = (href) => href
  .replace(/^\/library\//, "/dominions/library/books/")
  .replace(/^(\/dominions\/library\/books\/[^/#]+)#/, "$1/#");
const sectionHref = (sectionId) => libraryHref(linkMap[sectionId] ?? "/dominions/library/");
const formatNumber = (value) => new Intl.NumberFormat("en-AU").format(value);

const frontMatter = (title, description, extra = "") => `---
title: ${JSON.stringify(title)}
description: ${JSON.stringify(description)}
nav_section: guides
extra_css: /assets/dominions-library.css
extra_js: /assets/dominions-library.js
og_image: ${ogImage}
${extra}---
`;

const blurbs = {
  guide: "How the collection is organised, where each subject lives, and the quickest route to a dependable answer.",
  b1: "Rulesets, terminology, hosting order, and the exact anatomy of a Dominions turn.",
  field: "A compact table-side reference for turn order, income, recruitment, upkeep, forts, and logistics.",
  b2: "Income, resources, recruitment, unrest, supply, forts, administration, and the machinery that keeps a nation functioning.",
  b3: "Pretender design, dominion, scales, blessings, awakening, death, and the consequences of religious pressure.",
  b4: "Army organisation, formations, attacks, protection, morale, fatigue, magic, afflictions, and battle analysis.",
  b5: "Research planning, paths, gems, rituals, forging, communions, blood magic, globals, and magical logistics.",
  b6: "Expansion, tempo, intelligence, movement, raiding, sieges, diplomacy, Thrones, and campaign decision-making.",
  b7: "A framework for understanding nations without reducing them to a single build or opening script.",
  b8: "The mod parser, object identity, commands, events, compatibility, validation, and release engineering.",
  b9: "A separate rules and compatibility reference for Dominions Enhanced 2.16 and Divinitus 1.15.3 DE.",
  b10: "Installation, game creation, interface use, turn submission, multiplayer hosting, recovery, and administration.",
  b11: "Unit classes, special abilities, experience, heroic abilities, conditions, counters, and stacking behaviour.",
  b12: "A structured reference layer for spells, items, summons, sites, Thrones, mercenaries, Pretenders, and other base objects.",
  b13: "The official patch history, organised as a versioned ledger rather than a loose list of remembered changes.",
  b14: "A command and terminology lexicon for locating syntax, documentation status, evidence, and version changes.",
};

const pathDescriptions = {
  "path-a": "Enough structure to play a complete game without first mastering every spell, ability, or edge case.",
  "path-b": "The rules and habits needed when negotiation, hidden intentions, borders, and reputation enter the game.",
  "path-c": "A brisk return through the current version, turn structure, economy, Pretender design, battle, and magic.",
  "path-d": "A fast route from an exact rules question to its canonical chapter, evidence record, and connected exceptions.",
  "path-e": "Trace a failed turn in resolution order so the original cause is found before the most visible consequence.",
  "path-f": "For inspecting objects and commands, planning compatible mods, validating releases, or maintaining the website edition.",
};

fs.mkdirSync(bookRoot, { recursive: true });
fs.mkdirSync(dataRoot, { recursive: true });

const documents = manifest.documents.map((entry) => readJson(`documents/${entry.id}.json`));
const totalWords = documents.reduce((sum, document) => sum + document.wordCount, 0);
const totalSections = documents.reduce((sum, document) => sum + document.sectionCount, 0);

for (const [index, document] of documents.entries()) {
  const directory = path.join(bookRoot, document.slug);
  fs.mkdirSync(directory, { recursive: true });
  const previous = documents[index - 1];
  const next = documents[index + 1];
  const toc = document.toc.filter((entry) => entry.level === 2);
  const renderedHtml = document.html
    .replaceAll('href="/library/', 'href="/dominions/library/books/')
    .replace(/href="(\/dominions\/library\/books\/[^"#]+)#/g, 'href="$1/#');
  const description = blurbs[document.id] ?? `${document.sectionCount} indexed Dominions 6 reference sections.`;

  const page = `${frontMatter(document.title, description)}
<section class="page-hero library-page-hero">
  <div class="shell">
    <div class="breadcrumbs">
      <a href="/dominions/">Dominions 6</a><span aria-hidden="true">/</span>
      <a href="/dominions/library/">Knowledge Library</a><span aria-hidden="true">/</span>
      <span>${escapeHtml(document.shortTitle)}</span>
    </div>
    <p class="eyebrow">${editionLabel}</p>
    <h1>${escapeHtml(document.title)}</h1>
    <p class="lead">${escapeHtml(description)}</p>
    <div class="meta-row">
      <span class="status status--stable">Published reference</span>
      <span class="meta-chip">Dominions ${gameVersion}</span>
      <span class="meta-chip">${formatNumber(document.wordCount)} words</span>
      <span class="meta-chip">${formatNumber(document.sectionCount)} sections</span>
    </div>
  </div>
</section>

<section class="section shell library-section">
  <details class="library-mobile-toc">
    <summary>Table of contents</summary>
    <nav>${toc.map((entry) => `<a href="#${escapeHtml(entry.id)}">${escapeHtml(entry.title)}</a>`).join("\n")}</nav>
  </details>
  <div class="library-reader-grid">
    <article class="content library-prose">
{% raw %}
${renderedHtml}
{% endraw %}
    </article>
    <aside class="sidebar library-toc">
      <h2>In this book</h2>
      <nav>${toc.map((entry) => `<a href="#${escapeHtml(entry.id)}">${escapeHtml(entry.title)}</a>`).join("\n")}</nav>
      <nav class="library-side-links">
        <a href="/dominions/library/">Complete library</a>
        <a href="/dominions/library/glossary/">Glossary</a>
        <a href="/dominions/library/research/">Research register</a>
        <a href="${pdfDownload}">Edition ${editionNumber} PDF</a>
      </nav>
    </aside>
  </div>
  <nav class="library-pagination" aria-label="Adjacent books">
    ${previous ? `<a href="/dominions/library/books/${previous.slug}/"><small>Previous</small>${escapeHtml(previous.shortTitle)}</a>` : "<span></span>"}
    ${next ? `<a class="library-next" href="/dominions/library/books/${next.slug}/"><small>Next</small>${escapeHtml(next.shortTitle)}</a>` : "<span></span>"}
  </nav>
</section>
`;
  fs.writeFileSync(path.join(directory, "index.html"), page);
}

const pathCards = readingPaths.paths.map((readingPath) => {
  const first = readingPath.steps[0];
  return `<article class="library-card">
    <h3>${escapeHtml(readingPath.title.replace(/^Path [A-F]: /, ""))}</h3>
    <p>${escapeHtml(pathDescriptions[readingPath.id] ?? readingPath.summary)}</p>
    <small>${readingPath.steps.length} selected sections</small>
    <a class="text-link" href="${sectionHref(first?.section_id)}">Begin this path →</a>
  </article>`;
}).join("\n");

const bookCards = documents.map((document, index) => `<article class="library-book-row">
  <span class="library-book-number">${String(index + 1).padStart(2, "0")}</span>
  <div>
    <h3><a href="/dominions/library/books/${document.slug}/">${escapeHtml(document.title)}</a></h3>
    <p>${escapeHtml(blurbs[document.id] ?? "Dominions 6 reference book.")}</p>
    <small>${formatNumber(document.wordCount)} words · ${formatNumber(document.sectionCount)} indexed sections</small>
  </div>
  <a class="library-open" href="/dominions/library/books/${document.slug}/">Open →</a>
</article>`).join("\n");

const landing = `${frontMatter("Dominions 6 Knowledge Library", "A versioned, searchable reference to Dominions 6 rules, strategy, modding, and research.")}
<section class="page-hero library-page-hero library-landing-hero">
  <div class="shell">
    <div class="breadcrumbs"><a href="/dominions/">Dominions 6</a><span aria-hidden="true">/</span><span>Knowledge Library</span></div>
    <p class="eyebrow">${editionLabel} · Dominions ${gameVersion}</p>
    <h1>The Dominions 6 Knowledge Library</h1>
    <p class="lead">A working reference for learning the game, checking an exact rule, planning a campaign, or tracing the evidence behind a difficult claim.</p>
    <div class="meta-row">
      <span class="status status--stable">Current edition</span>
      <span class="meta-chip">16 books and guides</span>
      <span class="meta-chip">${formatNumber(totalSections)} indexed sections</span>
      <span class="meta-chip">${formatNumber(totalWords)} words</span>
    </div>
  </div>
</section>

<section class="section shell library-section">
  <div class="library-search-panel" data-library-search data-index-url="/dominions/library/data/search-index.json.gz">
    <div>
      <p class="eyebrow">Search the full collection</p>
      <h2>Start with the question.</h2>
      <p>Results lead directly to the permanent section that owns the explanation. Search by rule, mechanic, command, object, or common term.</p>
    </div>
    <div class="library-search-controls">
      <label><span>Search all ${formatNumber(totalSections)} sections</span><input type="search" data-search-query placeholder="Try fatigue, blood hunting, siege, #newmonster…" autocomplete="off"></label>
      <label><span>Subject</span><select data-search-topic><option value="all">All subjects</option></select></label>
    </div>
    <p class="library-search-status" data-search-status aria-live="polite">Enter a term or choose a subject.</p>
    <div class="library-search-results" data-search-results></div>
  </div>

  <section class="library-recent" data-recent-library hidden>
    <div class="library-heading"><div><p class="eyebrow">Continue reading</p><h2>Recently opened books</h2></div><button class="button button--quiet" type="button" data-clear-recent>Clear</button></div>
    <div class="library-card-grid" data-recent-library-list></div>
  </section>

  <div class="library-heading" id="reading-paths">
    <div><p class="eyebrow">Guided routes</p><h2>Choose a reading path</h2></div>
    <div class="library-heading-action"><p>The collection is meant to be consulted, not endured in order. These routes gather the sections needed for a particular job.</p><a class="button button--quiet" href="/dominions/tools/library-reading/">Track personal progress</a></div>
  </div>
  <div class="library-card-grid">${pathCards}</div>

  <div class="library-heading" id="reference-tools">
    <div><p class="eyebrow">Reference tools</p><h2>Look up a term or inspect the evidence</h2></div>
    <p>The glossary supplies quick definitions. The research register keeps completed work, open questions, and testing requirements distinct.</p>
  </div>
  <div class="library-tool-grid">
    <article class="library-tool-card"><h3>Glossary</h3><p>106 rules, interface terms, abbreviations, and pieces of community language, each linked to its full explanation.</p><a class="button button--quiet" href="/dominions/library/glossary/">Open the glossary</a></article>
    <article class="library-tool-card"><h3>Research register</h3><p>57 verification questions with priorities, status, importance, and the most reliable route to an answer.</p><a class="button button--quiet" href="/dominions/library/research/">Open the register</a></article>
    <article class="library-tool-card"><h3>Field toolkit</h3><p>Sixteen tools cover nations, Pretenders, economy, recruitment, magic, battles, turns, diplomacy, research, reading progress, multiplayer records, and Throne victories.</p><a class="button button--quiet" href="/dominions/tools/">Open the tools</a></article>
    <article class="library-tool-card"><h3>Edition ${editionNumber} PDF</h3><p>The complete ${pdfPageCount}-page library for offline reading, archiving, printing, or sharing outside the website.</p><a class="button button--quiet" href="${pdfDownload}">Download the PDF</a></article>
  </div>

  <div class="library-heading" id="complete-shelf">
    <div><p class="eyebrow">The complete shelf</p><h2>Books and field references</h2></div>
    <p>Each subject has one main home. Related books link back to that home instead of repeating the same explanation.</p>
  </div>
  <div class="library-book-list">${bookCards}</div>
</section>
`;
fs.writeFileSync(path.join(libraryRoot, "index.html"), landing);

const statusLabels = { completed: "Completed", queued: "Queued", "in-progress": "In progress" };
const researchItems = research.items.map((item) => `<article class="library-register-item" data-register-item data-status="${escapeHtml(item.status)}" data-priority="${escapeHtml(item.priority)}" data-search="${escapeHtml(`${item.id} ${item.domain} ${item.question} ${item.why_it_matters} ${item.reliable_resolution_route}`.toLowerCase())}">
  <div class="library-register-meta"><span class="library-status library-status--${escapeHtml(item.status)}">${escapeHtml(statusLabels[item.status] ?? item.status)}</span><span>${escapeHtml(item.priority)}</span><span>${escapeHtml(item.id)}</span><span>${escapeHtml(item.domain)}</span>${item.requires_player_testing ? "<span>Player test needed</span>" : ""}</div>
  <h2>${escapeHtml(item.question)}</h2>
  <div class="library-register-details"><div><h3>Why it matters</h3><p>${escapeHtml(item.why_it_matters)}</p></div><div><h3>Resolution route</h3><p>${escapeHtml(item.reliable_resolution_route)}</p></div></div>
  <a class="text-link" href="${sectionHref(item.primary_section_id)}">Read the canonical section →</a>
</article>`).join("\n");

const researchPage = `${frontMatter("Dominions 6 Research Register", "The completed, open, and in-progress verification work behind the Dominions 6 Knowledge Library.")}
<section class="page-hero library-page-hero"><div class="shell"><div class="breadcrumbs"><a href="/dominions/">Dominions 6</a><span>/</span><a href="/dominions/library/">Knowledge Library</a><span>/</span><span>Research Register</span></div><p class="eyebrow">Evidence and verification</p><h1>Research Register</h1><p class="lead">Every difficult claim deserves a clear status. The register records what has been settled, what remains open, and the evidence needed to close each question properly.</p><div class="meta-row"><span class="meta-chip">${research.items.length} questions</span><span class="meta-chip">${research.items.filter((item) => item.status === "completed").length} completed</span><span class="meta-chip">Dominions ${gameVersion} baseline</span></div></div></section>
<section class="section shell library-section" data-register>
  <div class="library-filter-row"><label><span>Search questions and domains</span><input type="search" data-register-query placeholder="Try communions, rounding, parser…"></label><label><span>Status</span><select data-register-status><option value="all">All statuses</option><option value="completed">Completed</option><option value="in-progress">In progress</option><option value="queued">Queued</option></select></label><label><span>Priority</span><select data-register-priority><option value="all">All priorities</option><option value="P0">P0 — foundation</option><option value="P1">P1 — high</option><option value="P2">P2 — medium</option><option value="P3">P3 — later</option></select></label></div>
  <p class="library-filter-count" data-register-count aria-live="polite"></p>
  <div class="library-register-list">${researchItems}</div>
</section>`;
fs.mkdirSync(path.join(libraryRoot, "research"), { recursive: true });
fs.writeFileSync(path.join(libraryRoot, "research", "index.html"), researchPage);

const glossaryEntries = glossary.entries.map((entry) => `<div class="library-glossary-entry" data-glossary-item data-letter="${escapeHtml(entry.term.charAt(0).toUpperCase())}" data-search="${escapeHtml(`${entry.term} ${entry.definition} ${(entry.aliases ?? []).join(" ")}`.toLowerCase())}"><dt>${escapeHtml(entry.term)}</dt><dd><p>${escapeHtml(entry.definition)}</p>${entry.aliases?.length ? `<p class="library-aliases">Also known as: ${escapeHtml(entry.aliases.join(", "))}</p>` : ""}<a class="text-link" href="${sectionHref(entry.primary_section_id)}">Open the main explanation →</a></dd></div>`).join("\n");
const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").map((letter) => `<button type="button" data-glossary-letter="${letter}">${letter}</button>`).join("");
const glossaryPage = `${frontMatter("Dominions 6 Glossary", "A searchable glossary of Dominions 6 rules, interface terms, abbreviations, and strategic language.")}
<section class="page-hero library-page-hero"><div class="shell"><div class="breadcrumbs"><a href="/dominions/">Dominions 6</a><span>/</span><a href="/dominions/library/">Knowledge Library</a><span>/</span><span>Glossary</span></div><p class="eyebrow">Plain language, exact destination</p><h1>Dominions 6 Glossary</h1><p class="lead">Short definitions for the game's rules, abbreviations, and community language, with a direct route to the full explanation whenever more detail is needed.</p><div class="meta-row"><span class="meta-chip">${glossary.entries.length} terms</span><span class="meta-chip">Dominions ${gameVersion} baseline</span></div></div></section>
<section class="section shell library-section" data-glossary>
  <label class="library-glossary-search"><span>Search terms, definitions, and aliases</span><input type="search" data-glossary-query placeholder="Try glamour, MR, upkeep…"></label>
  <div class="library-alphabet"><button class="is-active" type="button" data-glossary-letter="all">All</button>${alphabet}</div>
  <p class="library-filter-count" data-glossary-count aria-live="polite"></p>
  <dl class="library-glossary-list">${glossaryEntries}</dl>
</section>`;
fs.mkdirSync(path.join(libraryRoot, "glossary"), { recursive: true });
fs.writeFileSync(path.join(libraryRoot, "glossary", "index.html"), glossaryPage);

for (const file of fs.readdirSync(sourceRoot).filter((entry) => (entry.endsWith(".json") || entry.endsWith(".json.gz")) && entry !== "manifest.json")) {
  fs.copyFileSync(path.join(sourceRoot, file), path.join(dataRoot, file));
}
fs.writeFileSync(
  path.join(dataRoot, "manifest.json"),
  `${JSON.stringify({ ...manifest, edition: editionLabel }, null, 2)}\n`,
);

console.log(JSON.stringify({ edition: editionLabel, books: documents.length, sections: totalSections, research: research.items.length, glossary: glossary.entries.length, libraryRoot }));
