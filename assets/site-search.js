const siteSearch = document.querySelector("[data-site-search]");

if (siteSearch) {
  const queryInput = siteSearch.querySelector("[data-site-search-query]");
  const projectSelect = siteSearch.querySelector("[data-site-search-project]");
  const typeSelect = siteSearch.querySelector("[data-site-search-type]");
  const count = siteSearch.querySelector("[data-site-search-count]");
  const siteEntries = [...siteSearch.querySelectorAll("[data-site-entry]")];
  const libraryStatus = siteSearch.querySelector("[data-library-search-status]");
  const libraryResults = siteSearch.querySelector("[data-library-search-results]");
  let libraryIndex = null;
  let libraryPromise = null;
  let requestNumber = 0;
  let debounceTimer = null;

  const sha256 = async (bytes) => [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))]
    .map((value) => value.toString(16).padStart(2, "0"))
    .join("");

  const titleCase = (value) => value
    .split("-")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");

  const readIndex = async (response, url) => {
    if (url.endsWith(".index.json")) {
      const manifest = await response.json();
      if (manifest.kind !== "dominions-library-search-index" || !Array.isArray(manifest.parts)) {
        throw new Error("The library search manifest is invalid.");
      }
      const baseUrl = new URL(url, window.location.href);
      const parts = await Promise.all(manifest.parts.map(async (part) => {
        const partResponse = await fetch(new URL(part.file, baseUrl));
        if (!partResponse.ok) throw new Error("The library index could not be loaded.");
        const bytes = await partResponse.arrayBuffer();
        if (part.sha256 && await sha256(bytes) !== part.sha256) {
          throw new Error("The library index failed its integrity check.");
        }
        const entries = JSON.parse(new TextDecoder().decode(bytes));
        if (!Array.isArray(entries)) throw new Error("The library index part is invalid.");
        return entries;
      }));
      const entries = parts.flat();
      if (entries.length !== manifest.entry_count) throw new Error("The library index is incomplete.");
      return entries;
    }
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
        if (!fallback.ok) throw new Error("The library index could not be loaded.");
        return fallback.json();
      }
    }
  };

  const loadLibrary = async () => {
    if (libraryIndex) return libraryIndex;
    if (!libraryPromise) {
      const url = siteSearch.dataset.libraryIndexUrl;
      libraryPromise = fetch(url)
        .then((response) => {
          if (!response.ok) throw new Error("The library index could not be loaded.");
          return readIndex(response, url);
        })
        .then((entries) => {
          libraryIndex = entries;
          return entries;
        });
    }
    return libraryPromise;
  };

  const score = (entry, words) => {
    const title = entry.title.toLowerCase();
    const book = entry.documentTitle.toLowerCase();
    let rank = 0;
    for (const word of words) {
      if (title === word) rank += 24;
      if (title.startsWith(word)) rank += 12;
      if (title.includes(word)) rank += 7;
      if (book.includes(word)) rank += 4;
      if ((entry.topics || []).some((topic) => topic.includes(word))) rank += 3;
      if (entry.searchText.includes(word)) rank += 1;
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
      libraryStatus.textContent = "Enter at least two characters to search the full library.";
      return;
    }

    libraryStatus.textContent = "Searching the full library…";
    try {
      const entries = await loadLibrary();
      if (currentRequest !== requestNumber) return;
      const words = query.split(/\s+/).filter(Boolean);
      const matches = entries
        .map((entry) => ({ entry, rank: score(entry, words) }))
        .filter(({ rank }) => rank > 0)
        .sort((left, right) => right.rank - left.rank || left.entry.level - right.entry.level)
        .slice(0, 20)
        .map(({ entry }) => entry);
      matches.forEach(addLibraryResult);
      libraryStatus.textContent = matches.length
        ? `${matches.length}${matches.length === 20 ? "+" : ""} matching library sections.`
        : "No Library sections matched. Try a broader term or the rule's proper name.";
    } catch {
      libraryStatus.textContent = "Library search could not be loaded. The books are still available from the Dominions page.";
    }
  };

  const runSearch = () => {
    const query = queryInput.value.toLowerCase().trim();
    const queryWords = query.split(/\s+/).filter(Boolean);
    const project = projectSelect.value;
    const type = typeSelect.value;
    let visible = 0;
    for (const entry of siteEntries) {
      const matchesQuery = queryWords.every((word) => entry.dataset.search.includes(word));
      const matchesProject = project === "all" || entry.dataset.project === project;
      const matchesType = type === "all" || entry.dataset.type === type;
      entry.hidden = !(matchesQuery && matchesProject && matchesType);
      if (!entry.hidden) visible += 1;
    }
    count.textContent = `Showing ${visible} main-site result${visible === 1 ? "" : "s"}.`;
    requestNumber += 1;
    searchLibrary(query, requestNumber);
  };

  const queueSearch = () => {
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(runSearch, 120);
  };

  queryInput.addEventListener("input", queueSearch);
  projectSelect.addEventListener("change", runSearch);
  typeSelect.addEventListener("change", runSearch);

  const initialQuery = new URLSearchParams(window.location.search).get("q") || "";
  queryInput.value = initialQuery;
  runSearch();
}
