const titleCase = (value) => value
  .split("-")
  .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
  .join(" ");

const searchPanel = document.querySelector("[data-library-search]");

if (searchPanel) {
  const queryInput = searchPanel.querySelector("[data-search-query]");
  const topicSelect = searchPanel.querySelector("[data-search-topic]");
  const status = searchPanel.querySelector("[data-search-status]");
  const resultsRoot = searchPanel.querySelector("[data-search-results]");
  let searchIndex = null;
  let loadingPromise = null;
  let debounceTimer = null;

  const readIndex = async (response, url) => {
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
        if (!fallback.ok) throw new Error("Library search index could not be loaded.");
        return fallback.json();
      }
    }
  };

  const loadIndex = async () => {
    if (searchIndex) return searchIndex;
    if (!loadingPromise) {
      const indexUrl = searchPanel.dataset.indexUrl;
      loadingPromise = fetch(indexUrl)
        .then((response) => {
          if (!response.ok) throw new Error("Library search index could not be loaded.");
          return readIndex(response, indexUrl);
        })
        .then((entries) => {
          searchIndex = entries;
          const topics = [...new Set(entries.flatMap((entry) => entry.topics || []))].sort();
          for (const topic of topics) {
            const option = document.createElement("option");
            option.value = topic;
            option.textContent = titleCase(topic);
            topicSelect.append(option);
          }
          return entries;
        });
    }
    return loadingPromise;
  };

  const score = (entry, words) => {
    const title = entry.title.toLowerCase();
    const book = entry.documentTitle.toLowerCase();
    let total = 0;
    for (const word of words) {
      if (title === word) total += 20;
      if (title.startsWith(word)) total += 10;
      if (title.includes(word)) total += 6;
      if (book.includes(word)) total += 3;
      if ((entry.topics || []).some((topic) => topic.includes(word))) total += 3;
      if (entry.searchText.includes(word)) total += 1;
    }
    return total;
  };

  const addResult = (entry) => {
    const article = document.createElement("article");
    article.className = "library-search-result";

    const meta = document.createElement("div");
    meta.className = "library-search-meta";
    const book = document.createElement("span");
    book.textContent = entry.documentTitle;
    meta.append(book);
    for (const topic of (entry.topics || []).slice(0, 2)) {
      const tag = document.createElement("span");
      tag.textContent = titleCase(topic);
      meta.append(tag);
    }

    const heading = document.createElement("h3");
    const link = document.createElement("a");
    link.href = `/dominions/library/books/${entry.documentSlug}/#${entry.id}`;
    link.textContent = entry.title;
    heading.append(link);
    article.append(meta, heading);

    if (entry.excerpt) {
      const excerpt = document.createElement("p");
      excerpt.textContent = entry.excerpt;
      article.append(excerpt);
    }
    resultsRoot.append(article);
  };

  const runSearch = async () => {
    const query = queryInput.value.toLowerCase().trim();
    const topic = topicSelect.value;
    const words = query.split(/\s+/).filter(Boolean);
    resultsRoot.replaceChildren();

    if (!words.length && topic === "all") {
      status.textContent = "Enter a term or choose a subject.";
      return;
    }

    status.textContent = "Searching the library…";
    try {
      const entries = await loadIndex();
      const results = entries
        .filter((entry) => topic === "all" || (entry.topics || []).includes(topic))
        .map((entry) => ({ entry, rank: words.length ? score(entry, words) : 1 }))
        .filter(({ rank }) => rank > 0)
        .sort((left, right) => right.rank - left.rank || left.entry.level - right.entry.level)
        .slice(0, 24)
        .map(({ entry }) => entry);

      status.textContent = `${results.length}${results.length === 24 ? "+" : ""} matching sections`;
      if (results.length) {
        results.forEach(addResult);
      } else {
        const empty = document.createElement("div");
        empty.className = "library-search-empty";
        const heading = document.createElement("h3");
        heading.textContent = "No sections found";
        const copy = document.createElement("p");
        copy.textContent = "Try a broader term, remove the subject filter, or search for the rule rather than its nickname.";
        empty.append(heading, copy);
        resultsRoot.append(empty);
      }
    } catch {
      status.textContent = "Search is temporarily unavailable. The books can still be opened below.";
    }
  };

  const queueSearch = () => {
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(runSearch, 120);
  };

  queryInput.addEventListener("focus", () => loadIndex().catch(() => {}), { once: true });
  queryInput.addEventListener("input", queueSearch);
  topicSelect.addEventListener("change", runSearch);

  const searchParameters = new URLSearchParams(window.location.search);
  const initialQuery = searchParameters.get("q");
  if (initialQuery) {
    queryInput.value = initialQuery;
    runSearch();
  }
}

const register = document.querySelector("[data-register]");

if (register) {
  const queryInput = register.querySelector("[data-register-query]");
  const statusSelect = register.querySelector("[data-register-status]");
  const prioritySelect = register.querySelector("[data-register-priority]");
  const count = register.querySelector("[data-register-count]");
  const items = [...register.querySelectorAll("[data-register-item]")];

  const filterRegister = () => {
    const query = queryInput.value.toLowerCase().trim();
    let visible = 0;
    for (const item of items) {
      const matchesQuery = !query || item.dataset.search.includes(query);
      const matchesStatus = statusSelect.value === "all" || item.dataset.status === statusSelect.value;
      const matchesPriority = prioritySelect.value === "all" || item.dataset.priority === prioritySelect.value;
      item.hidden = !(matchesQuery && matchesStatus && matchesPriority);
      if (!item.hidden) visible += 1;
    }
    count.textContent = `Showing ${visible} of ${items.length} research questions`;
  };

  queryInput.addEventListener("input", filterRegister);
  statusSelect.addEventListener("change", filterRegister);
  prioritySelect.addEventListener("change", filterRegister);
  filterRegister();
}

const glossary = document.querySelector("[data-glossary]");

if (glossary) {
  const queryInput = glossary.querySelector("[data-glossary-query]");
  const count = glossary.querySelector("[data-glossary-count]");
  const letterButtons = [...glossary.querySelectorAll("[data-glossary-letter]")];
  const items = [...glossary.querySelectorAll("[data-glossary-item]")];
  let activeLetter = "all";

  const filterGlossary = () => {
    const query = queryInput.value.toLowerCase().trim();
    let visible = 0;
    for (const item of items) {
      const matchesQuery = !query || item.dataset.search.includes(query);
      const matchesLetter = activeLetter === "all" || item.dataset.letter === activeLetter;
      item.hidden = !(matchesQuery && matchesLetter);
      if (!item.hidden) visible += 1;
    }
    count.textContent = `Showing ${visible} of ${items.length} terms`;
  };

  for (const button of letterButtons) {
    button.addEventListener("click", () => {
      activeLetter = button.dataset.glossaryLetter;
      letterButtons.forEach((entry) => entry.classList.toggle("is-active", entry === button));
      filterGlossary();
    });
  }

  queryInput.addEventListener("input", filterGlossary);
  filterGlossary();
}

const recentKey = "thk-library-recent";
const bookPath = window.location.pathname.match(/^\/dominions\/library\/books\/[^/]+\/?$/);

const readRecent = () => {
  try {
    const entries = JSON.parse(window.localStorage.getItem(recentKey) || "[]");
    if (!Array.isArray(entries)) return [];
    return entries.filter((entry) => (
      typeof entry?.title === "string"
      && typeof entry?.url === "string"
      && /^\/dominions\/library\/books\/[^/]+\/?$/.test(entry.url)
    ));
  } catch {
    return [];
  }
};

const writeRecent = (items) => {
  try {
    window.localStorage.setItem(recentKey, JSON.stringify(items));
  } catch {
    // Reading history is optional and stays on this device.
  }
};

if (bookPath) {
  const title = document.querySelector(".library-page-hero h1")?.textContent.trim();
  if (title) {
    const nextRecent = [
      { title, url: window.location.pathname },
      ...readRecent().filter((entry) => entry.url !== window.location.pathname),
    ].slice(0, 4);
    writeRecent(nextRecent);
  }

  const prose = document.querySelector(".library-prose");
  if (prose) {
    const progress = document.createElement("div");
    progress.className = "reading-progress";
    progress.setAttribute("aria-hidden", "true");
    document.body.append(progress);
    const updateProgress = () => {
      const start = prose.offsetTop;
      const end = start + prose.offsetHeight - window.innerHeight;
      const percentage = end <= start ? 100 : Math.max(0, Math.min(100, ((window.scrollY - start) / (end - start)) * 100));
      progress.style.width = `${percentage}%`;
    };
    window.addEventListener("scroll", updateProgress, { passive: true });
    window.addEventListener("resize", updateProgress);
    updateProgress();
  }
}

const recentPanel = document.querySelector("[data-recent-library]");
if (recentPanel) {
  const list = recentPanel.querySelector("[data-recent-library-list]");
  const clearButton = recentPanel.querySelector("[data-clear-recent]");
  const renderRecent = () => {
    const entries = readRecent();
    list.replaceChildren();
    recentPanel.hidden = entries.length === 0;
    for (const entry of entries) {
      const article = document.createElement("article");
      article.className = "library-card library-card--recent";
      const heading = document.createElement("h3");
      const link = document.createElement("a");
      link.href = entry.url;
      link.textContent = entry.title;
      heading.append(link);
      const copy = document.createElement("p");
      copy.textContent = "Continue from the book most recently opened on this device.";
      article.append(heading, copy);
      list.append(article);
    }
  };
  clearButton.addEventListener("click", () => {
    writeRecent([]);
    renderRecent();
  });
  renderRecent();
}

const showCopyFeedback = (message) => {
  const oldFeedback = document.querySelector(".copy-link-feedback");
  oldFeedback?.remove();
  const feedback = document.createElement("div");
  feedback.className = "copy-link-feedback";
  feedback.textContent = message;
  feedback.setAttribute("role", "status");
  document.body.append(feedback);
  window.setTimeout(() => feedback.remove(), 1800);
};

for (const link of document.querySelectorAll(".heading-link")) {
  link.addEventListener("click", async (event) => {
    const target = link.getAttribute("href");
    if (!target?.startsWith("#")) return;
    event.preventDefault();
    const url = new URL(window.location.href);
    url.hash = target;
    window.history.replaceState(null, "", url);
    try {
      await navigator.clipboard.writeText(url.href);
      showCopyFeedback("Section link copied.");
    } catch {
      window.location.hash = target;
    }
  });
}
