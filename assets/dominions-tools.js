const copyOutput = async (output, status) => {
  const text = output?.textContent.trim();
  if (!text) {
    if (status) status.textContent = "Build the record before copying it.";
    return;
  }
  try {
    await navigator.clipboard.writeText(text);
    if (status) status.textContent = "Copied to the clipboard.";
  } catch {
    if (status) status.textContent = "Copying was blocked by the browser. Select the text manually.";
  }
};

const nationFinder = document.querySelector("[data-nation-finder]");

if (nationFinder) {
  const queryInput = nationFinder.querySelector("[data-nation-query]");
  const ageSelect = nationFinder.querySelector("[data-nation-age]");
  const count = nationFinder.querySelector("[data-nation-count]");
  const cards = [...nationFinder.querySelectorAll("[data-nation-card]")];
  const comparePanel = nationFinder.querySelector("[data-nation-compare]");
  const compareGrid = nationFinder.querySelector("[data-nation-compare-grid]");
  const compareStatus = nationFinder.querySelector("[data-nation-compare-status]");
  const clearButton = nationFinder.querySelector("[data-nation-clear]");

  const selectedCards = () => cards.filter((card) => card.querySelector("[data-nation-select]").checked);

  const renderComparison = (message = "") => {
    const selected = selectedCards();
    compareGrid.replaceChildren();
    comparePanel.hidden = selected.length === 0;
    compareStatus.textContent = message || `${selected.length} of 3 comparison places used.`;
    for (const card of selected) {
      const article = document.createElement("article");
      article.className = "nation-compare-card";
      const age = document.createElement("span");
      age.className = "content-badge content-badge--official";
      age.textContent = card.dataset.age === "early" ? "Early Age" : card.dataset.age === "middle" ? "Middle Age" : "Late Age";
      const heading = document.createElement("h3");
      heading.textContent = card.dataset.name;
      const summary = document.createElement("p");
      summary.textContent = card.dataset.summary;
      const source = document.createElement("small");
      source.textContent = `Official manual, page ${card.dataset.page}`;
      article.append(age, heading, summary, source);
      compareGrid.append(article);
    }
  };

  const filterNations = () => {
    const words = queryInput.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const age = ageSelect.value;
    let visible = 0;
    for (const card of cards) {
      const matchesWords = words.every((word) => card.dataset.search.includes(word));
      const matchesAge = age === "all" || card.dataset.age === age;
      card.hidden = !(matchesWords && matchesAge);
      if (!card.hidden) visible += 1;
    }
    count.textContent = `Showing ${visible} of ${cards.length} nations.`;
  };

  for (const card of cards) {
    const checkbox = card.querySelector("[data-nation-select]");
    checkbox.addEventListener("change", () => {
      if (checkbox.checked && selectedCards().length > 3) {
        checkbox.checked = false;
        renderComparison("Three nations are already selected. Remove one before adding another.");
        return;
      }
      card.classList.toggle("is-selected", checkbox.checked);
      renderComparison();
    });
  }

  clearButton.addEventListener("click", () => {
    for (const card of cards) {
      card.querySelector("[data-nation-select]").checked = false;
      card.classList.remove("is-selected");
    }
    renderComparison();
  });
  queryInput.addEventListener("input", filterNations);
  ageSelect.addEventListener("change", filterNations);
  filterNations();
}

const researchPlanner = document.querySelector("[data-research-planner]");

if (researchPlanner) {
  const output = document.querySelector("[data-research-output]");
  const calculate = () => {
    const form = new FormData(researchPlanner);
    const target = String(form.get("target") || "Next breakpoint").trim() || "Next breakpoint";
    const currentTurn = Math.max(1, Number(form.get("turn")) || 1);
    let remaining = Math.max(1, Number(form.get("remaining")) || 1);
    const normal = Math.max(1, Number(form.get("monthly")) || 1);
    const statedLoss = Math.max(0, Number(form.get("lost")) || 0);
    const disruptedMonths = Math.max(0, Math.floor(Number(form.get("disrupted")) || 0));
    const disruptedOutput = Math.max(0, normal - statedLoss);
    let disruptionUsed = 0;
    if (disruptedOutput === 0) {
      disruptionUsed = disruptedMonths;
    } else {
      disruptionUsed = Math.min(disruptedMonths, Math.ceil(remaining / disruptedOutput));
      remaining -= disruptedOutput * disruptionUsed;
    }
    let hostingCycles = disruptionUsed;
    if (remaining > 0) {
      hostingCycles += Math.ceil(remaining / normal);
    }

    const finishTurn = currentTurn + hostingCycles;
    const effectiveLoss = Math.min(normal, statedLoss) * disruptionUsed;
    output.textContent = [
      target,
      `Normal output: ${normal.toLocaleString("en-AU")} RP per month`,
      `Output during disruption: ${disruptedOutput.toLocaleString("en-AU")} RP per month for ${disruptionUsed} hosting cycle${disruptionUsed === 1 ? "" : "s"}`,
      `Nominal research diverted before completion: ${effectiveLoss.toLocaleString("en-AU")} RP`,
      `Estimated completion: after ${hostingCycles} hosting cycle${hostingCycles === 1 ? "" : "s"}, on turn ${finishTurn}`,
      "Recalculate if the displayed monthly research total changes.",
    ].join("\n");
  };
  researchPlanner.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  researchPlanner.addEventListener("reset", () => window.setTimeout(() => { output.textContent = ""; }, 0));
  calculate();
}

const buildSheet = document.querySelector("[data-build-sheet]");

if (buildSheet) {
  const storageKey = "thk-dominions-build-sheet";
  const fields = [...buildSheet.querySelectorAll("[data-build-field]")];
  const output = document.querySelector("[data-build-output]");
  const status = document.querySelector("[data-build-status]");
  const clearButton = buildSheet.querySelector("[data-build-clear]");
  const labels = {
    ruleset: "RULESET",
    nation: "NATION AND MAGE POOL",
    problem: "IMMEDIATE PROBLEM",
    route: "RESEARCH ROUTE",
    delivery: "DELIVERY PACKAGE",
    timing: "TIMING",
    branch: "BRANCH CONDITION",
    endstate: "INTENDED END STATE",
  };

  const save = () => {
    const data = Object.fromEntries(fields.map((field) => [field.name, field.value]));
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(data));
      status.textContent = "Saved in this browser.";
    } catch {
      status.textContent = "Browser storage is unavailable. The sheet can still be copied.";
    }
  };

  const build = () => {
    output.textContent = fields
      .map((field) => `${labels[field.name]}\n${field.value.trim() || "Not recorded."}`)
      .join("\n\n");
  };

  try {
    const saved = JSON.parse(window.localStorage.getItem(storageKey) || "{}");
    fields.forEach((field) => { if (typeof saved[field.name] === "string") field.value = saved[field.name]; });
  } catch {
    // A malformed local record should not block a new sheet.
  }
  fields.forEach((field) => field.addEventListener("input", save));
  buildSheet.addEventListener("submit", (event) => { event.preventDefault(); save(); build(); });
  buildSheet.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  clearButton.addEventListener("click", () => {
    if (!window.confirm("Clear the saved build sheet on this device?")) return;
    fields.forEach((field) => { field.value = ""; });
    window.localStorage.removeItem(storageKey);
    output.textContent = "";
    status.textContent = "The saved sheet was cleared.";
  });
  if (fields.some((field) => field.value.trim())) build();
}

const settingsForm = document.querySelector("[data-game-settings]");

if (settingsForm) {
  const storageKey = "thk-dominions-game-settings";
  const fields = [...settingsForm.querySelectorAll("[data-settings-field]")];
  const output = document.querySelector("[data-settings-output]");
  const status = document.querySelector("[data-settings-status]");
  const clearButton = settingsForm.querySelector("[data-settings-clear]");
  const labels = {
    name: "GAME",
    version: "DOMINIONS VERSION",
    age: "AGE",
    players: "HUMAN PLAYERS",
    provinces: "TARGET PROVINCES PER PLAYER",
    map: "MAP OR GENERATOR",
    research: "RESEARCH",
    independents: "INDEPENDENT STRENGTH",
    sites: "MAGIC-SITE FREQUENCY",
    thrones: "THRONES AND ASCENSION POINTS",
    cataclysm: "CATACLYSM",
    graphs: "SCORE GRAPHS",
    mods: "MODS IN LOAD ORDER",
    hosting: "HOSTING AND EXTENSIONS",
    diplomacy: "DIPLOMACY AND TABLE RULES",
    security: "SECURITY AND ADMINISTRATION",
  };

  const save = () => {
    const data = Object.fromEntries(fields.map((field) => [field.name, field.value]));
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(data));
      status.textContent = "Saved in this browser.";
    } catch {
      status.textContent = "Browser storage is unavailable. The record can still be copied.";
    }
  };

  const build = () => {
    const values = Object.fromEntries(fields.map((field) => [field.name, field.value.trim()]));
    const players = Math.max(0, Number(values.players) || 0);
    const provinces = Math.max(0, Number(values.provinces) || 0);
    const mapTarget = players && provinces ? `\nTARGET LAND PROVINCES\nAbout ${(players * provinces).toLocaleString("en-AU")} before water and special map requirements` : "";
    output.textContent = fields
      .map((field) => `${labels[field.name]}\n${field.value.trim() || "Not recorded."}`)
      .join("\n\n") + mapTarget;
  };

  try {
    const saved = JSON.parse(window.localStorage.getItem(storageKey) || "{}");
    fields.forEach((field) => { if (typeof saved[field.name] === "string") field.value = saved[field.name]; });
  } catch {
    // A malformed local record should not block a new settings sheet.
  }
  fields.forEach((field) => field.addEventListener("input", save));
  settingsForm.addEventListener("submit", (event) => { event.preventDefault(); save(); build(); });
  settingsForm.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  clearButton.addEventListener("click", () => {
    if (!window.confirm("Clear the saved multiplayer settings on this device?")) return;
    settingsForm.reset();
    window.localStorage.removeItem(storageKey);
    output.textContent = "";
    status.textContent = "The saved settings record was cleared.";
  });
  if (fields.some((field) => field.value.trim())) build();
}
