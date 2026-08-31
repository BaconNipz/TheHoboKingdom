const siteSearch = document.querySelector("[data-site-search]");

if (siteSearch) {
  const queryInput = siteSearch.querySelector("[data-site-search-query]");
  const projectSelect = siteSearch.querySelector("[data-site-search-project]");
  const typeSelect = siteSearch.querySelector("[data-site-search-type]");
  const count = siteSearch.querySelector("[data-site-search-count]");
  const siteEntries = [...siteSearch.querySelectorAll("[data-site-entry]")];
  const libraryStatus = siteSearch.querySelector("[data-library-search-status]");
  const libraryResults = siteSearch.querySelector("[data-library-search-results]");
  const referenceStatus = siteSearch.querySelector("[data-reference-search-status]");
  const referenceResults = siteSearch.querySelector("[data-reference-search-results]");
  const referenceFilterPanel = siteSearch.querySelector("[data-reference-filter-panel]");
  const referenceFilters = {
    category: siteSearch.querySelector("[data-reference-search-category]"),
    path: siteSearch.querySelector("[data-reference-search-path]"),
    school: siteSearch.querySelector("[data-reference-search-school]"),
    era: siteSearch.querySelector("[data-reference-search-era]"),
    evidence: siteSearch.querySelector("[data-reference-search-evidence]"),
  };
  let libraryIndex = null;
  let libraryPromise = null;
  let referenceCatalogue = null;
  let referencePromise = null;
  let requestNumber = 0;
  let debounceTimer = null;

  const aliases = {
    ap: ["ap", "ascension points"],
    hp: ["hp", "hit points"],
    mr: ["mr", "magic resistance"],
    pd: ["pd", "province defence"],
    rp: ["rp", "research points"],
  };

  const normalise = (value) => String(value || "")
    .toLocaleLowerCase("en-AU")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/\bdefense\b/g, "defence")
    .replace(/\barmor\b/g, "armour");

  const pretty = (value) => String(value || "Not recorded")
    .replace(/[-_]+/g, " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase());

  const queryGroups = (query) => normalise(query)
    .replace(/\bid(?=\s+\d)/g, "")
    .split(/\s+/)
    .filter(Boolean)
    .map((word) => aliases[word] || [word]);

  const matchesGroups = (searchText, groups) => groups.every((group) => (
    group.some((term) => searchText.includes(term))
  ));

  const sha256 = async (bytes) => [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))]
    .map((value) => value.toString(16).padStart(2, "0"))
    .join("");

  const readCompressedJson = async (response, url) => {
    if (!url.endsWith(".gz")) return response.json();
    const bytes = await response.arrayBuffer();
    try {
      const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"));
      return JSON.parse(await new Response(stream).text());
    } catch {
      try {
        return JSON.parse(new TextDecoder().decode(bytes));
      } catch {
        const fallback = await fetch(url.replace(/\.gz$/, ""));
        if (!fallback.ok) throw new Error("The requested search data could not be loaded.");
        return fallback.json();
      }
    }
  };

  const readLibraryIndex = async (response, url) => {
    if (!url.endsWith(".index.json")) return readCompressedJson(response, url);
    const manifest = await response.json();
    if (manifest.kind !== "dominions-library-search-index" || !Array.isArray(manifest.parts)) {
      throw new Error("The Library search manifest is invalid.");
    }
    const baseUrl = new URL(url, window.location.href);
    const parts = await Promise.all(manifest.parts.map(async (part) => {
      const partResponse = await fetch(new URL(part.file, baseUrl));
      if (!partResponse.ok) throw new Error("The Library index could not be loaded.");
      const bytes = await partResponse.arrayBuffer();
      if (part.sha256 && await sha256(bytes) !== part.sha256) {
        throw new Error("The Library index failed its integrity check.");
      }
      const entries = JSON.parse(new TextDecoder().decode(bytes));
      if (!Array.isArray(entries)) throw new Error("A Library index part is invalid.");
      return entries;
    }));
    const entries = parts.flat();
    if (entries.length !== manifest.entry_count) throw new Error("The Library index is incomplete.");
    return entries;
  };

  const loadLibrary = async () => {
    if (libraryIndex) return libraryIndex;
    if (!libraryPromise) {
      const url = siteSearch.dataset.libraryIndexUrl;
      libraryPromise = fetch(url)
        .then((response) => {
          if (!response.ok) throw new Error("The Library index could not be loaded.");
          return readLibraryIndex(response, url);
        })
        .then((entries) => {
          libraryIndex = entries;
          return entries;
        });
    }
    return libraryPromise;
  };

  const recordSchool = (record) => {
    const school = (record.attributes || []).find(([label]) => label === "School")?.[1] || "";
    return String(school).replace(/\s+\d+$/, "");
  };

  const recordSearchText = (record) => normalise([
    record.name,
    record.id,
    record.engineId,
    record.categoryLabel,
    record.summary,
    record.evidence,
    record.status,
    record.paths,
    record.eras,
    record.attributes?.flat(),
    record.properties?.flat(),
  ].flat(Infinity).join(" "));

  const loadReferenceCatalogue = async () => {
    if (referenceCatalogue) return referenceCatalogue;
    if (!referencePromise) {
      const url = siteSearch.dataset.referenceCatalogueUrl;
      referencePromise = fetch(url)
        .then((response) => {
          if (!response.ok) throw new Error("The base-game catalogue could not be loaded.");
          return readCompressedJson(response, url);
        })
        .then((catalogue) => {
          if (!Array.isArray(catalogue.records) || catalogue.records.length !== catalogue.totalRecords) {
            throw new Error("The base-game catalogue is incomplete.");
          }
          catalogue.records.forEach((record) => {
            record.searchText = recordSearchText(record);
            record.school = recordSchool(record);
          });
          referenceCatalogue = catalogue;
          return catalogue;
        });
    }
    return referencePromise;
  };

  const scoreLibraryEntry = (entry, groups) => {
    const title = normalise(entry.title);
    const book = normalise(entry.documentTitle);
    const text = normalise(entry.searchText);
    let rank = 0;
    for (const group of groups) {
      for (const word of group) {
        if (title === word) rank += 24;
        if (title.startsWith(word)) rank += 12;
        if (title.includes(word)) rank += 7;
        if (book.includes(word)) rank += 4;
        if ((entry.topics || []).some((topic) => normalise(topic).includes(word))) rank += 3;
        if (text.includes(word)) rank += 1;
      }
    }
    return rank;
  };

  const addLibraryResult = (entry) => {
    const article = document.createElement("article");
    article.className = "search-result search-result--library";
    const meta = document.createElement("div");
    meta.className = "search-result-meta";
    const book = document.createElement("span");
    book.textContent = entry.documentTitle;
    const type = document.createElement("span");
    type.textContent = "Library section";
    meta.append(book, type);
    const heading = document.createElement("h3");
    const link = document.createElement("a");
    link.href = `/dominions/library/books/${entry.documentSlug}/#${entry.id}`;
    link.textContent = entry.title;
    heading.append(link);
    article.append(meta, heading);
    if (entry.excerpt) {
      const copy = document.createElement("p");
      copy.textContent = entry.excerpt;
      article.append(copy);
    }
    libraryResults.append(article);
  };

  const searchLibrary = async (query, currentRequest) => {
    libraryResults.replaceChildren();
    const projectAllowsLibrary = projectSelect.value === "all" || projectSelect.value === "Dominions 6";
    const typeAllowsLibrary = typeSelect.value === "all" || typeSelect.value === "Library";
    if (!projectAllowsLibrary || !typeAllowsLibrary) {
      libraryStatus.textContent = "Those filters leave out the Dominions 6 Library.";
      return;
    }
    if (query.length < 2) {
      libraryStatus.textContent = "Enter at least two characters to search the full Library.";
      return;
    }

    libraryStatus.textContent = "Searching the full Library…";
    try {
      const entries = await loadLibrary();
      if (currentRequest !== requestNumber) return;
      const groups = queryGroups(query);
      const matches = entries
        .map((entry) => ({ entry, rank: scoreLibraryEntry(entry, groups), searchText: normalise(entry.searchText) }))
        .filter(({ rank, searchText }) => rank > 0 && matchesGroups(searchText, groups))
        .sort((left, right) => right.rank - left.rank || left.entry.level - right.entry.level)
        .slice(0, 20)
        .map(({ entry }) => entry);
      matches.forEach(addLibraryResult);
      libraryStatus.textContent = matches.length
        ? `${matches.length}${matches.length === 20 ? "+" : ""} matching Library sections.`
        : "No Library sections matched. Try a broader term or the rule's proper name.";
    } catch {
      libraryStatus.textContent = "Library search could not be loaded. The books are still available from the Dominions page.";
    }
  };

  const scoreReferenceRecord = (record, groups) => {
    if (!groups.length) return 1;
    const title = normalise(record.name);
    const id = normalise(record.id);
    const engineId = String(record.engineId ?? "");
    let rank = 0;
    for (const group of groups) {
      for (const word of group) {
        if (title === word) rank += 40;
        if (id === word || engineId === word.replace(/^id\s*/, "")) rank += 36;
        if (title.startsWith(word)) rank += 18;
        if (title.includes(word)) rank += 10;
        if (normalise(record.summary).includes(word)) rank += 4;
        if (record.searchText.includes(word)) rank += 1;
      }
    }
    return rank;
  };

  const addReferenceResult = (record, ruleset) => {
    const article = document.createElement("article");
    article.className = "search-result search-result--reference";
    const meta = document.createElement("div");
    meta.className = "search-result-meta";
    [
      record.categoryLabel,
      record.engineId === null ? "" : `ID ${record.engineId}`,
      record.paths?.length ? record.paths.join(" ") : "",
      record.eras?.length ? record.eras.join(" ") : "",
      record.school,
      pretty(record.evidence),
    ].filter(Boolean).forEach((value) => {
      const chip = document.createElement("span");
      chip.textContent = value;
      meta.append(chip);
    });
    const heading = document.createElement("h3");
    const link = document.createElement("a");
    const target = new URL("/dominions/tools/reference/", window.location.origin);
    target.searchParams.set("query", record.id);
    target.searchParams.set("category", record.category);
    link.href = `${target.pathname}${target.search}`;
    link.textContent = record.name;
    heading.append(link);
    const copy = document.createElement("p");
    copy.textContent = record.summary || "No short summary is recorded for this entry.";
    const boundary = document.createElement("small");
    boundary.className = "search-result-boundary";
    boundary.textContent = `${ruleset.game} ${ruleset.game_version} · Vanilla catalogue · Open the result for the full record`;
    article.append(meta, heading, copy, boundary);
    referenceResults.append(article);
  };

  const referenceValues = () => Object.fromEntries(
    Object.entries(referenceFilters).map(([key, field]) => [key, field.value]),
  );

  const searchReference = async (query, currentRequest) => {
    referenceResults.replaceChildren();
    const projectAllowsReference = projectSelect.value === "all" || projectSelect.value === "Dominions 6";
    const typeAllowsReference = typeSelect.value === "all" || typeSelect.value === "Reference record";
    if (!projectAllowsReference || !typeAllowsReference) {
      referenceStatus.textContent = "Those filters leave out the Dominions 6 base-game records.";
      return;
    }
    const values = referenceValues();
    const hasRecordFilter = Object.values(values).some(Boolean);
    if (query.length < 2 && !hasRecordFilter) {
      referenceStatus.textContent = "Enter at least two characters or choose a record filter.";
      return;
    }

    referenceStatus.textContent = "Searching all 5,340 base-game records…";
    try {
      const catalogue = await loadReferenceCatalogue();
      if (currentRequest !== requestNumber) return;
      const groups = queryGroups(query);
      const matches = catalogue.records
        .filter((record) => (
          (!values.category || record.category === values.category)
          && (!values.path || record.paths.includes(values.path))
          && (!values.school || record.school === values.school)
          && (!values.era || record.eras.includes(values.era))
          && (!values.evidence || record.evidence === values.evidence)
          && matchesGroups(record.searchText, groups)
        ))
        .map((record) => ({ record, rank: scoreReferenceRecord(record, groups) }))
        .sort((left, right) => right.rank - left.rank || left.record.name.localeCompare(right.record.name, "en-AU"));
      matches.slice(0, 30).forEach(({ record }) => addReferenceResult(record, catalogue.ruleset));
      referenceStatus.textContent = matches.length
        ? `Showing ${Math.min(matches.length, 30).toLocaleString("en-AU")} of ${matches.length.toLocaleString("en-AU")} matching base-game records.`
        : "No base-game records matched. Try the exact name, numeric ID, or a broader filter.";
    } catch {
      referenceStatus.textContent = "The base-game catalogue could not be loaded. Its separate reference page is still available from Dominions tools.";
    }
  };

  const applyUrlState = () => {
    const params = new URLSearchParams();
    const query = queryInput.value.trim();
    if (query) params.set("q", query);
    if (projectSelect.value !== "all") params.set("project", projectSelect.value);
    if (typeSelect.value !== "all") params.set("type", typeSelect.value);
    for (const [key, field] of Object.entries(referenceFilters)) {
      if (field.value) params.set(key, field.value);
    }
    const search = params.toString();
    window.history.replaceState({}, "", `${window.location.pathname}${search ? `?${search}` : ""}${window.location.hash}`);
  };

  const restoreUrlState = () => {
    const params = new URLSearchParams(window.location.search);
    queryInput.value = params.get("q") || "";
    if ([...projectSelect.options].some((option) => option.value === params.get("project"))) {
      projectSelect.value = params.get("project");
    }
    if ([...typeSelect.options].some((option) => option.value === params.get("type"))) {
      typeSelect.value = params.get("type");
    }
    for (const [key, field] of Object.entries(referenceFilters)) {
      if ([...field.options].some((option) => option.value === params.get(key))) field.value = params.get(key);
    }
    if (Object.values(referenceFilters).some((field) => field.value)) referenceFilterPanel.open = true;
  };

  const runSearch = () => {
    const query = normalise(queryInput.value.trim());
    const groups = queryGroups(query);
    const project = projectSelect.value;
    const type = typeSelect.value;
    let visible = 0;
    for (const entry of siteEntries) {
      const matchesQuery = matchesGroups(normalise(entry.dataset.search), groups);
      const matchesProject = project === "all" || entry.dataset.project === project;
      const matchesType = type === "all" || entry.dataset.type === type;
      entry.hidden = !(matchesQuery && matchesProject && matchesType);
      if (!entry.hidden) visible += 1;
    }
    count.textContent = `Showing ${visible} main-site result${visible === 1 ? "" : "s"}.`;
    applyUrlState();
    requestNumber += 1;
    searchReference(query, requestNumber);
    searchLibrary(query, requestNumber);
  };

  const queueSearch = () => {
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(runSearch, 120);
  };

  queryInput.addEventListener("input", queueSearch);
  projectSelect.addEventListener("change", runSearch);
  typeSelect.addEventListener("change", runSearch);
  Object.values(referenceFilters).forEach((field) => field.addEventListener("change", runSearch));

  restoreUrlState();
  runSearch();
}
