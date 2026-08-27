const copyOutput = async (output, status) => {
  const text = output?.textContent.trim();
  if (!text) {
    if (status) status.textContent = "Create the record first.";
    return;
  }
  try {
    await navigator.clipboard.writeText(text);
    if (status) status.textContent = "Copied.";
  } catch {
    if (status) status.textContent = "The browser blocked clipboard access. Select and copy the text instead.";
  }
};

const finiteNumber = (value, fallback = 0) => {
  const number = Number(value);
  return Number.isFinite(number) ? number : fallback;
};

const formNumber = (formData, name, fallback = 0) => finiteNumber(formData.get(name), fallback);

const formatToolNumber = (value, maximumFractionDigits = 2) => finiteNumber(value).toLocaleString("en-AU", {
  maximumFractionDigits,
});

const formatToolPercent = (value) => `${(finiteNumber(value) * 100).toLocaleString("en-AU", {
  minimumFractionDigits: 0,
  maximumFractionDigits: 2,
})}%`;

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

const economyCalculator = document.querySelector("[data-economy-calculator]");

if (economyCalculator) {
  const output = document.querySelector("[data-economy-output]");

  const calculate = () => {
    const form = new FormData(economyCalculator);
    const population = Math.max(0, formNumber(form, "population"));
    const scaleMultiplier = Math.max(0, formNumber(form, "scale", 100)) / 100;
    const administration = Math.max(0, formNumber(form, "administration"));
    const unrest = Math.max(0, formNumber(form, "unrest"));
    const potentialResources = Math.max(0, formNumber(form, "resources"));
    const resourceAccess = Math.max(0, formNumber(form, "resource-access", 0.5));
    const hasTaxTrace = form.get("tax-trace") === "on";

    const baseIncome = population / 100;
    const administrationMultiplier = 1 + administration / 200;
    const modifiedIncome = baseIncome * scaleMultiplier * administrationMultiplier;
    const incomeRetention = 1 / (1 + unrest * 0.02);
    const finalIncomeBeforeTrace = modifiedIncome * incomeRetention;
    const finalIncome = hasTaxTrace ? finalIncomeBeforeTrace : 0;
    const localResourcesBeforeUnrest = potentialResources * resourceAccess;
    const resourceRetention = 1 / (1 + unrest * 0.01);
    const finalResources = localResourcesBeforeUnrest * resourceRetention;
    const recruitmentStatus = unrest >= 100
      ? "Ordinary unit and commander recruitment is shut down at unrest 100 or greater."
      : "Ordinary recruitment is not shut down by unrest.";

    output.textContent = [
      "PROVINCE ECONOMY ESTIMATE",
      `Base income from population: ${formatToolNumber(baseIncome)}`,
      `Scale multiplier: ${formatToolPercent(scaleMultiplier)}`,
      `Administration bonus: +${formatToolNumber(administration / 2)}%`,
      `Income retained after unrest: ${formatToolPercent(incomeRetention)}`,
      `Estimated income before tax trace: ${formatToolNumber(finalIncomeBeforeTrace)}`,
      `Estimated collected income: ${formatToolNumber(finalIncome)}${hasTaxTrace ? "" : " — no valid tax trace"}`,
      "",
      `Local resources before unrest: ${formatToolNumber(localResourcesBeforeUnrest)}`,
      `Resources retained after unrest: ${formatToolPercent(resourceRetention)}`,
      `Estimated local resource pool: ${formatToolNumber(finalResources)}`,
      "",
      recruitmentStatus,
      "Use the value shown in-game when intermediate rounding changes the result.",
    ].join("\n");
  };

  economyCalculator.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  economyCalculator.addEventListener("reset", () => window.setTimeout(calculate, 0));
  calculate();
}

const recruitmentPlanner = document.querySelector("[data-recruitment-planner]");

if (recruitmentPlanner) {
  const rows = [...recruitmentPlanner.querySelectorAll("[data-recruit-row]")];
  const output = document.querySelector("[data-recruitment-output]");
  const status = document.querySelector("[data-recruitment-status]");

  const calculate = () => {
    const totals = { gold: 0, resources: 0, rp: 0, cp: 0, hp: 0, monthly: 0 };
    const entries = [];

    for (const [index, row] of rows.entries()) {
      const quantity = Math.max(0, Math.floor(finiteNumber(row.querySelector('[data-recruit-value="quantity"]').value)));
      if (!quantity) continue;
      const name = row.querySelector("[data-recruit-name]").value.trim() || `Entry ${index + 1}`;
      const values = Object.fromEntries([...row.querySelectorAll("[data-recruit-value]")]
        .map((field) => [field.dataset.recruitValue, Math.max(0, finiteNumber(field.value))]));
      const upkeepSelect = row.querySelector("[data-recruit-upkeep]");
      const divisor = Math.max(0, finiteNumber(upkeepSelect.value));
      const monthly = divisor ? quantity * values.gold / divisor : 0;
      totals.gold += quantity * values.gold;
      totals.resources += quantity * values.resources;
      totals.rp += quantity * values.rp;
      totals.cp += quantity * values.cp;
      totals.hp += quantity * values.hp;
      totals.monthly += monthly;
      entries.push(`${quantity} × ${name}: ${formatToolNumber(quantity * values.gold)} G, ${formatToolNumber(quantity * values.resources)} Res, ${formatToolNumber(quantity * values.rp)} RP, ${formatToolNumber(quantity * values.cp)} CP, ${formatToolNumber(quantity * values.hp)} HP; ≈${formatToolNumber(monthly)} upkeep/month`);
    }

    const capacityLines = ["gold", "resources", "rp", "cp", "hp"].map((key) => {
      const capacity = Math.max(0, finiteNumber(recruitmentPlanner.querySelector(`[data-recruit-capacity="${key}"]`).value));
      const used = totals[key];
      const remaining = capacity - used;
      const label = key === "gold" ? "Gold" : key === "resources" ? "Resources" : key.toUpperCase();
      return `${label}: ${formatToolNumber(used)} / ${formatToolNumber(capacity)}${remaining < 0 ? ` — short ${formatToolNumber(Math.abs(remaining))}` : ` — ${formatToolNumber(remaining)} left`}`;
    });

    output.textContent = [
      "RECRUITMENT QUEUE",
      ...(entries.length ? entries : ["No recruitment entries have a quantity above zero."]),
      "",
      "CAPACITY",
      ...capacityLines,
      "",
      `Estimated monthly upkeep added: ${formatToolNumber(totals.monthly)}`,
      `Estimated annual upkeep added: ${formatToolNumber(totals.monthly * 12)}`,
      "Mounted units and special upkeep exceptions must be checked in the detailed unit interface.",
    ].join("\n");
    const shortfalls = ["gold", "resources", "rp", "cp", "hp"].filter((key) => {
      const capacity = Math.max(0, finiteNumber(recruitmentPlanner.querySelector(`[data-recruit-capacity="${key}"]`).value));
      return totals[key] > capacity;
    });
    status.textContent = shortfalls.length
      ? `Queue exceeds ${shortfalls.map((key) => key === "resources" ? "resources" : key.toUpperCase()).join(", ")}.`
      : "The queue fits the entered capacity.";
  };

  recruitmentPlanner.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  recruitmentPlanner.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  recruitmentPlanner.addEventListener("reset", () => window.setTimeout(calculate, 0));
  calculate();
}

const gemBudget = document.querySelector("[data-gem-budget]");

if (gemBudget) {
  const rows = [...gemBudget.querySelectorAll("[data-gem-row]")];
  const output = document.querySelector("[data-gem-output]");
  const status = document.querySelector("[data-gem-status]");

  const calculate = () => {
    const form = new FormData(gemBudget);
    const turns = Math.max(1, Math.floor(formNumber(form, "turns", 1)));
    const label = String(form.get("label") || "Gem treasury plan").trim() || "Gem treasury plan";
    const reserveGaps = [];
    const lines = rows.map((row) => {
      const values = Object.fromEntries([...row.querySelectorAll("[data-gem-value]")]
        .map((field) => [field.dataset.gemValue, Math.max(0, finiteNumber(field.value))]));
      const projected = values.current + values.income * turns - values.oneoff - values.recurring * turns;
      const aboveReserve = projected - values.reserve;
      if (aboveReserve < 0) reserveGaps.push(`${row.dataset.code} ${formatToolNumber(Math.abs(aboveReserve))}`);
      return `${row.dataset.code} · ${row.dataset.path}: ${formatToolNumber(values.current)} + ${formatToolNumber(values.income)}×${turns} − ${formatToolNumber(values.oneoff)} − ${formatToolNumber(values.recurring)}×${turns} = ${formatToolNumber(projected)}; ${aboveReserve < 0 ? `reserve shortfall ${formatToolNumber(Math.abs(aboveReserve))}` : `${formatToolNumber(aboveReserve)} above reserve`}`;
    });

    output.textContent = [
      label.toUpperCase(),
      `Projection: ${turns} turn${turns === 1 ? "" : "s"}`,
      "",
      ...lines,
      "",
      reserveGaps.length ? `Reserve gaps: ${reserveGaps.join(", ")}` : "Every path remains at or above the entered reserve.",
      "Add alchemy, events, new or lost sites, and interrupted Blood hunting yourself.",
    ].join("\n");
    status.textContent = reserveGaps.length
      ? `${reserveGaps.length} path${reserveGaps.length === 1 ? " is" : "s are"} below reserve.`
      : "The entered plan preserves every reserve.";
  };

  gemBudget.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  gemBudget.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  gemBudget.addEventListener("reset", () => window.setTimeout(calculate, 0));
  calculate();
}

const communionPlanner = document.querySelector("[data-communion-planner]");

if (communionPlanner) {
  const output = document.querySelector("[data-communion-output]");
  const bonusForSlaves = (slaves) => slaves >= 1 ? Math.floor(Math.log2(slaves)) : 0;

  const calculate = () => {
    const form = new FormData(communionPlanner);
    const type = String(form.get("type") || "Communion");
    const slaves = Math.max(0, Math.floor(formNumber(form, "slaves")));
    const losses = Math.max(0, Math.floor(formNumber(form, "losses")));
    const masters = Math.max(1, Math.floor(formNumber(form, "masters", 1)));
    const basePath = Math.max(0, formNumber(form, "base-path"));
    const requirement = Math.max(0, formNumber(form, "requirement"));
    const fatigue = Math.max(0, formNumber(form, "fatigue"));
    const relativeModifier = Math.max(0, formNumber(form, "relative", 1));
    const remainingSlaves = Math.max(0, slaves - losses);
    const valid = slaves >= 1;
    const remainingValid = remainingSlaves >= 1;
    const bonus = bonusForSlaves(slaves);
    const remainingBonus = bonusForSlaves(remainingSlaves);
    const boostedPath = basePath > 0 && valid ? basePath + bonus : basePath;
    const remainingPath = basePath > 0 && remainingValid ? basePath + remainingBonus : basePath;
    const participants = valid ? slaves + 1 : 0;
    const baseShare = participants ? fatigue / participants : 0;
    const slaveShare = baseShare * relativeModifier;
    const totalSlaveLoad = slaveShare * masters;
    const nextThreshold = valid ? 2 ** (bonus + 1) : 1;
    const currentThreshold = valid ? 2 ** bonus : 0;
    const spareSlaves = valid ? slaves - currentThreshold : 0;

    output.textContent = [
      type.toUpperCase(),
      valid ? `Active slaves: ${slaves}; master path bonus: +${bonus}` : "No active slave: the communion is not valid.",
      basePath > 0 ? `Relevant master path: ${formatToolNumber(basePath)} → ${formatToolNumber(boostedPath)}` : "The relevant path is absent; a communion bonus does not create it.",
      `Critical requirement: ${formatToolNumber(requirement)} — ${boostedPath >= requirement ? "currently met" : "not currently met"}`,
      valid ? `Current threshold floor: ${currentThreshold}; spare slaves above it: ${spareSlaves}; next bonus at ${nextThreshold}` : "At least one master effect and one slave effect are required.",
      "",
      `After ${losses} expected loss${losses === 1 ? "" : "es"}: ${remainingSlaves} active slave${remainingSlaves === 1 ? "" : "s"}, +${remainingBonus} bonus, path ${formatToolNumber(remainingPath)}`,
      `Critical requirement after losses: ${remainingPath >= requirement && remainingValid ? "met" : "not met"}`,
      "",
      valid ? `Participants in one master's spell: ${participants}` : "Participants: not applicable",
      valid ? `Base fatigue share: ${formatToolNumber(baseShare)}` : "Base fatigue share: not applicable",
      valid ? `Estimated fatigue per slave for one cast: ${formatToolNumber(slaveShare)}` : "Slave fatigue: not applicable",
      valid ? `Estimated fatigue per slave if all ${masters} masters cast once: ${formatToolNumber(totalSlaveLoad)}` : "Shared load: not applicable",
      "Each master's spell is a separate fatigue event; other masters are not participants in that cast.",
    ].join("\n");
  };

  communionPlanner.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  communionPlanner.addEventListener("reset", () => window.setTimeout(calculate, 0));
  calculate();
}

const randomMagic = document.querySelector("[data-random-magic]");

if (randomMagic) {
  const output = document.querySelector("[data-random-output]");

  const calculate = () => {
    const form = new FormData(randomMagic);
    const slots = Math.max(1, Math.floor(formNumber(form, "slots", 1)));
    const occurrence = Math.min(100, Math.max(0, formNumber(form, "occurrence", 100))) / 100;
    const possible = Math.max(1, Math.floor(formNumber(form, "possible", 1)));
    const desired = Math.min(possible, Math.max(0, Math.floor(formNumber(form, "desired"))));
    const mages = Math.max(1, Math.floor(formNumber(form, "mages", 1)));
    const label = String(form.get("label") || "Desired random path").trim() || "Desired random path";
    const slotChance = occurrence * desired / possible;
    const mageChance = 1 - (1 - slotChance) ** slots;
    const runChance = 1 - (1 - mageChance) ** mages;
    const expectedMages = mageChance * mages;

    const recruitsForChance = (target) => {
      if (mageChance <= 0) return "never under these assumptions";
      if (mageChance >= 1) return "1 mage";
      const count = Math.ceil(Math.log(1 - target) / Math.log(1 - mageChance));
      return `${count.toLocaleString("en-AU")} mage${count === 1 ? "" : "s"}`;
    };

    output.textContent = [
      label.toUpperCase(),
      `Chance per random slot: ${formatToolPercent(slotChance)}`,
      `Chance one mage has at least one acceptable result: ${formatToolPercent(mageChance)}`,
      `Chance at least one appears among ${mages} mages: ${formatToolPercent(runChance)}`,
      `Expected mages with at least one acceptable result: ${formatToolNumber(expectedMages)}`,
      "",
      `50% chance by: ${recruitsForChance(0.5)}`,
      `75% chance by: ${recruitsForChance(0.75)}`,
      `90% chance by: ${recruitsForChance(0.9)}`,
      `95% chance by: ${recruitsForChance(0.95)}`,
      "",
      "Assumption: independent slots, uniform outcomes, and replacement between rolls.",
    ].join("\n");
  };

  randomMagic.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  randomMagic.addEventListener("reset", () => window.setTimeout(calculate, 0));
  calculate();
}

const siteSearch = document.querySelector("[data-site-search]");

if (siteSearch) {
  const storageKey = "thk-dominions-site-search";
  const rows = [...siteSearch.querySelectorAll("[data-site-row]")];
  const output = document.querySelector("[data-site-output]");
  const status = document.querySelector("[data-site-status]");

  const save = () => {
    const form = new FormData(siteSearch);
    const data = {
      province: String(form.get("province") || ""),
      ruleset: String(form.get("ruleset") || ""),
      notes: String(form.get("notes") || ""),
      paths: rows.map((row) => ({
        current: row.querySelector('[data-site-value="current"]').value,
        target: row.querySelector('[data-site-value="target"]').value,
        plan: row.querySelector('[data-site-value="plan"]').value,
      })),
    };
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(data));
    } catch {
      status.textContent = "Browser storage is unavailable. The record can still be copied.";
    }
  };

  const build = () => {
    const form = new FormData(siteSearch);
    const province = String(form.get("province") || "Unlabelled province").trim() || "Unlabelled province";
    const ruleset = String(form.get("ruleset") || "Not recorded").trim() || "Not recorded";
    const notes = String(form.get("notes") || "").trim();
    let complete = 0;
    const lines = rows.map((row) => {
      const current = Math.max(0, Math.floor(finiteNumber(row.querySelector('[data-site-value="current"]').value)));
      const target = Math.max(0, Math.floor(finiteNumber(row.querySelector('[data-site-value="target"]').value)));
      const plan = row.querySelector('[data-site-value="plan"]').value.trim();
      const gap = Math.max(0, target - current);
      if (gap === 0) complete += 1;
      return `${row.dataset.code} · ${row.dataset.path}: searched ${current}, target ${target} — ${gap === 0 ? "complete" : `gap ${gap}${plan ? `; plan: ${plan}` : "; no searcher recorded"}`}`;
    });
    output.textContent = [
      `SITE-SEARCH RECORD — ${province}`,
      `Ruleset: ${ruleset}`,
      "",
      ...lines,
      "",
      `Coverage targets met: ${complete} of ${rows.length}`,
      `Notes: ${notes || "None recorded."}`,
      "The target levels are your choices. The tool cannot know which sites are present or how a mod changes them.",
    ].join("\n");
    status.textContent = `${complete} of ${rows.length} path targets are met. Saved in this browser.`;
  };

  try {
    const saved = JSON.parse(window.localStorage.getItem(storageKey) || "null");
    if (saved) {
      siteSearch.elements.province.value = saved.province || "";
      siteSearch.elements.ruleset.value = saved.ruleset || siteSearch.elements.ruleset.value;
      siteSearch.elements.notes.value = saved.notes || "";
      rows.forEach((row, index) => {
        const path = saved.paths?.[index];
        if (!path) return;
        row.querySelector('[data-site-value="current"]').value = path.current ?? 0;
        row.querySelector('[data-site-value="target"]').value = path.target ?? 2;
        row.querySelector('[data-site-value="plan"]').value = path.plan || "";
      });
    }
  } catch {
    // A malformed local record should not block a new coverage sheet.
  }

  siteSearch.addEventListener("input", () => { save(); build(); });
  siteSearch.addEventListener("submit", (event) => {
    event.preventDefault();
    save();
    build();
  });
  siteSearch.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  siteSearch.addEventListener("reset", () => window.setTimeout(() => {
    window.localStorage.removeItem(storageKey);
    build();
  }, 0));
  build();
}

const battleScript = document.querySelector("[data-battle-script]");

if (battleScript) {
  const storageKey = "thk-dominions-battle-script";
  const fields = [...battleScript.querySelectorAll("[data-script-field]")];
  const output = document.querySelector("[data-script-output]");
  const status = document.querySelector("[data-script-status]");
  const clearButton = battleScript.querySelector("[data-script-clear]");
  const labels = {
    battle: "BATTLE",
    commander: "COMMANDER",
    role: "ROLE",
    paths: "PATHS AND STATISTICS",
    equipment: "ITEMS AND GEMS",
    position: "POSITION AND PROTECTION",
    postscript: "POST-SCRIPT BEHAVIOUR",
    threat: "THREAT",
    screen: "SCREEN AND PREPARATION",
    gems: "GEM POLICY",
    failure: "FAILURE BRANCH",
    retreat: "RETREAT AND RECOVERY",
    test: "TEST RECORD",
  };

  const save = () => {
    const data = Object.fromEntries(fields.map((field) => [field.name, field.value]));
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(data));
      status.textContent = "Saved in this browser.";
    } catch {
      status.textContent = "Browser storage is unavailable. The script can still be copied.";
    }
  };

  const build = () => {
    const value = (name) => battleScript.elements[name]?.value.trim() || "Not recorded.";
    const scriptLines = [1, 2, 3, 4, 5].map((number) => `${number}. ${value(`order${number}`)}`);
    output.textContent = [
      `BATTLE SCRIPT — ${value("battle")}`,
      "",
      ...["commander", "role", "paths", "equipment", "position"].map((name) => `${labels[name]}\n${value(name)}`),
      "",
      "SCRIPT",
      ...scriptLines,
      `${labels.postscript}\n${value("postscript")}`,
      "",
      ...["threat", "screen", "gems", "failure", "retreat", "test"].map((name) => `${labels[name]}\n${value(name)}`),
    ].join("\n\n");
  };

  try {
    const saved = JSON.parse(window.localStorage.getItem(storageKey) || "{}");
    fields.forEach((field) => { if (typeof saved[field.name] === "string") field.value = saved[field.name]; });
  } catch {
    // A malformed local script should not block a new record.
  }
  fields.forEach((field) => field.addEventListener("input", () => { save(); build(); }));
  battleScript.addEventListener("submit", (event) => {
    event.preventDefault();
    save();
    build();
  });
  battleScript.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  clearButton.addEventListener("click", () => {
    if (!window.confirm("Clear the saved battle script on this device?")) return;
    fields.forEach((field) => { field.value = ""; });
    window.localStorage.removeItem(storageKey);
    build();
    status.textContent = "The saved battle script was cleared.";
  });
  build();
}

const turnPlanner = document.querySelector("[data-turn-planner]");

if (turnPlanner) {
  const storageKey = "thk-dominions-turn-planner";
  const fields = [...turnPlanner.querySelectorAll("[data-turn-field]")];
  const items = [...turnPlanner.querySelectorAll("[data-turn-item]")];
  const progress = turnPlanner.querySelector("[data-turn-progress]");
  const progressLabel = turnPlanner.querySelector("[data-turn-progress-label]");
  const output = document.querySelector("[data-turn-output]");
  const status = document.querySelector("[data-turn-status]");

  const save = () => {
    const data = {
      fields: Object.fromEntries(fields.map((field) => [field.name, field.value])),
      checked: items.filter((item) => item.checked).map((item) => item.value),
    };
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(data));
      status.textContent = "Checklist state saved in this browser.";
    } catch {
      status.textContent = "Browser storage is unavailable. The audit can still be copied.";
    }
  };

  const update = () => {
    const completed = items.filter((item) => item.checked);
    const outstanding = items.filter((item) => !item.checked);
    const percentage = items.length ? completed.length / items.length * 100 : 0;
    const game = turnPlanner.elements.game.value.trim() || "Unlabelled game and nation";
    const turn = Math.max(1, Math.floor(finiteNumber(turnPlanner.elements.turn.value, 1)));
    const notes = turnPlanner.elements.notes.value.trim();
    progress.value = percentage;
    progressLabel.textContent = `${completed.length} of ${items.length} checks complete`;
    output.textContent = [
      `TURN ${turn} AUDIT — ${game}`,
      `Completed: ${completed.length} of ${items.length}`,
      "",
      "OUTSTANDING",
      ...(outstanding.length ? outstanding.map((item) => `- ${item.value}`) : ["- No checklist items remain."]),
      "",
      "TURN NOTES",
      notes || "None recorded.",
    ].join("\n");
  };

  try {
    const saved = JSON.parse(window.localStorage.getItem(storageKey) || "null");
    if (saved) {
      fields.forEach((field) => { if (typeof saved.fields?.[field.name] === "string") field.value = saved.fields[field.name]; });
      const checked = new Set(saved.checked || []);
      items.forEach((item) => { item.checked = checked.has(item.value); });
    }
  } catch {
    // A malformed local checklist should not block a new turn.
  }

  turnPlanner.addEventListener("input", () => { save(); update(); });
  turnPlanner.querySelector("[data-turn-copy]").addEventListener("click", () => copyOutput(output, status));
  turnPlanner.querySelector("[data-turn-complete]").addEventListener("click", () => {
    items.forEach((item) => { item.checked = true; });
    save();
    update();
  });
  turnPlanner.querySelector("[data-turn-reset]").addEventListener("click", () => {
    if (!window.confirm("Clear completed checks and move this planner to the next turn?")) return;
    items.forEach((item) => { item.checked = false; });
    turnPlanner.elements.turn.value = Math.max(1, Math.floor(finiteNumber(turnPlanner.elements.turn.value, 1))) + 1;
    turnPlanner.elements.notes.value = "";
    save();
    update();
    status.textContent = "A fresh turn checklist is ready.";
  });
  update();
}

const throneTracker = document.querySelector("[data-throne-tracker]");

if (throneTracker) {
  const rows = [...throneTracker.querySelectorAll("[data-throne-row]")];
  const output = document.querySelector("[data-throne-output]");
  const status = document.querySelector("[data-throne-status]");

  const calculate = () => {
    const form = new FormData(throneTracker);
    const label = String(form.get("label") || "Unlabelled game and nation").trim() || "Unlabelled game and nation";
    const turn = Math.max(1, Math.floor(formNumber(form, "turn", 1)));
    const required = Math.max(1, Math.floor(formNumber(form, "required", 1)));
    const claimed = Math.max(0, Math.floor(formNumber(form, "claimed")));
    const notes = String(form.get("notes") || "").trim();
    let controlledPoints = 0;
    let targetPoints = 0;
    let controlledCount = 0;
    let targetCount = 0;
    let readyCount = 0;
    let pointsReadyThisTurn = 0;

    for (const row of rows) {
      const level = Math.max(1, Math.floor(finiteNumber(row.dataset.level, 1)));
      const controlled = Math.max(0, Math.floor(finiteNumber(row.querySelector('[data-throne-value="controlled"]').value)));
      const requestedReady = Math.max(0, Math.floor(finiteNumber(row.querySelector('[data-throne-value="ready"]').value)));
      const ready = Math.min(controlled, requestedReady);
      const targets = Math.max(0, Math.floor(finiteNumber(row.querySelector('[data-throne-value="targets"]').value)));
      controlledPoints += controlled * level;
      pointsReadyThisTurn += ready * level;
      targetPoints += targets * level;
      controlledCount += controlled;
      readyCount += ready;
      targetCount += targets;
    }

    const afterReadyClaims = claimed + pointsReadyThisTurn;
    const allControlledPotential = claimed + controlledPoints;
    const namedTargetPotential = allControlledPotential + targetPoints;
    const remainingNow = Math.max(0, required - claimed);
    const remainingAfterReady = Math.max(0, required - afterReadyClaims);
    const currentState = claimed >= required
      ? "The entered claimed total already meets the Ascension requirement."
      : afterReadyClaims >= required
        ? "Ready claim orders can reach the requirement this hosting cycle if the Thrones remain claimable."
        : allControlledPotential >= required
          ? "Controlled Thrones contain enough points, but more claim orders or hosting cycles are required."
          : namedTargetPotential >= required
            ? "Controlled Thrones are insufficient; the named target pool can reach the requirement."
            : "The entered controlled and target pools do not yet contain enough points.";

    output.textContent = [
      `THRONE POSITION — TURN ${turn} — ${label}`,
      `Victory requirement: ${required} AP`,
      `Already claimed: ${claimed} AP; ${remainingNow} AP remaining`,
      "",
      `Controlled but unclaimed: ${controlledCount} Throne${controlledCount === 1 ? "" : "s"}, ${controlledPoints} AP`,
      `Eligible claim orders ready: ${readyCount}`,
      `AP from ready orders this turn: ${pointsReadyThisTurn}`,
      `Projected claimed total after ready orders: ${afterReadyClaims} AP; ${remainingAfterReady} AP remaining`,
      `Potential after every controlled Throne is claimed: ${allControlledPotential} AP`,
      "",
      `Named targets: ${targetCount} Throne${targetCount === 1 ? "" : "s"}, ${targetPoints} AP`,
      `Potential including all named targets: ${namedTargetPotential} AP`,
      "",
      currentState,
      `Notes: ${notes || "None recorded."}`,
      "The points only count if a legal claimer can reach the Throne, issue the order, and survive hosting.",
    ].join("\n");
    status.textContent = currentState;
  };

  throneTracker.addEventListener("submit", (event) => {
    event.preventDefault();
    calculate();
  });
  throneTracker.querySelector("[data-tool-copy]").addEventListener("click", () => copyOutput(output, status));
  throneTracker.addEventListener("reset", () => window.setTimeout(calculate, 0));
  calculate();
}
