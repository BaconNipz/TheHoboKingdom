const menuButton = document.querySelector(".nav-toggle");
const navigation = document.querySelector(".site-nav");
const toolStorageMetadataKey = "thk-tool-data-metadata-v1";

const updateToolStorageMetadata = (key, value) => {
  try {
    const metadata = JSON.parse(window.localStorage.getItem(toolStorageMetadataKey) || "{}");
    if (value) metadata[key] = value;
    else delete metadata[key];
    window.localStorage.setItem(toolStorageMetadataKey, JSON.stringify(metadata));
  } catch {
    // Tool pages still work when browser storage is unavailable or metadata is damaged.
  }
};

window.thkStorageMarkUpdated = (key) => updateToolStorageMetadata(key, new Date().toISOString());
window.thkStorageForget = (key) => updateToolStorageMetadata(key, null);

const annotateToolTable = (table) => {
  const headers = [...table.querySelectorAll("thead th")].map((header, index) => (
    header.textContent.trim() || (index === 0 ? "Row" : "Actions")
  ));
  table.querySelectorAll("tbody tr").forEach((row) => {
    [...row.children].forEach((cell, index) => {
      if (!cell.dataset.label) cell.dataset.label = headers[index] || `Column ${index + 1}`;
    });
  });
  const wrapper = table.closest(".tool-table-wrap");
  if (wrapper && !wrapper.hasAttribute("tabindex")) {
    const legend = table.closest("fieldset")?.querySelector("legend")?.textContent.trim();
    wrapper.tabIndex = 0;
    wrapper.setAttribute("aria-label", `${legend || document.body.dataset.pageTitle || "Tool"} table`);
  }
};

document.querySelectorAll(".tool-table").forEach((table) => {
  annotateToolTable(table);
  const observer = new MutationObserver(() => annotateToolTable(table));
  observer.observe(table, { childList: true, subtree: true });
});

document.querySelectorAll(".tool-status, [data-record-status]").forEach((toolStatus) => {
  if (!toolStatus.hasAttribute("aria-live")) toolStatus.setAttribute("aria-live", "polite");
  const observer = new MutationObserver(() => {
    toolStatus.classList.remove("is-updated");
    window.requestAnimationFrame(() => toolStatus.classList.add("is-updated"));
  });
  observer.observe(toolStatus, { childList: true, characterData: true, subtree: true });
});

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const isOpen = navigation.classList.toggle("is-open");
    menuButton.setAttribute("aria-expanded", String(isOpen));
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      navigation.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
    }
  });
}

const searchLink = document.querySelector(".nav-search");
const searchInput = document.querySelector("[data-site-search-query]");

const focusSiteSearch = () => {
  if (searchInput) {
    searchInput.focus();
    searchInput.select();
    const url = new URL(window.location.href);
    if (url.searchParams.has("focus")) {
      url.searchParams.delete("focus");
      window.history.replaceState({}, "", `${url.pathname}${url.search}${url.hash}`);
    }
    return;
  }
  if (searchLink) window.location.assign(`${searchLink.href}?focus=1`);
};

document.addEventListener("keydown", (event) => {
  const target = event.target;
  const isWriting = target instanceof HTMLElement && (
    target.matches("input, textarea, select") || target.isContentEditable
  );
  const slashShortcut = event.key === "/" && !event.ctrlKey && !event.metaKey && !event.altKey;
  const commandShortcut = event.key.toLowerCase() === "k" && (event.ctrlKey || event.metaKey);
  if ((!slashShortcut && !commandShortcut) || isWriting) return;
  event.preventDefault();
  focusSiteSearch();
});

if (searchInput && new URLSearchParams(window.location.search).get("focus") === "1") {
  window.requestAnimationFrame(focusSiteSearch);
}

const reportLink = document.querySelector("[data-report-link]");

if (reportLink) {
  reportLink.addEventListener("click", () => {
    const reportUrl = new URL(reportLink.href);
    reportUrl.searchParams.set("page", window.location.href);
    reportUrl.searchParams.set("title", document.body.dataset.pageTitle || document.title);
    reportLink.href = reportUrl.toString();
  });
}
