const referenceRoot = document.querySelector("[data-reference-catalogue]");

if (referenceRoot) {
  const form = referenceRoot.querySelector("[data-reference-filters]");
  const results = referenceRoot.querySelector("[data-reference-results]");
  const heading = referenceRoot.querySelector("[data-reference-heading]");
  const status = referenceRoot.querySelector("[data-reference-status]");
  const total = document.querySelector("[data-reference-total]");
  const more = referenceRoot.querySelector("[data-reference-more]");
  const category = form.querySelector("[data-reference-category]");
  const evidence = form.querySelector("[data-reference-evidence]");
  const levelLabel = form.querySelector("[data-reference-level-label]");
  const batchSize = 60;
  let catalogue = null;
  let filtered = [];
  let visible = batchSize;

  const normalise = (value) => String(value || "").toLocaleLowerCase("en-AU").normalize("NFKD").replace(/[\u0300-\u036f]/g, "");
  const pretty = (value) => String(value || "Not recorded").replace(/[-_]+/g, " ").replace(/\b\w/g, (letter) => letter.toUpperCase());
  const plural = (count, singular, pluralForm = `${singular}s`) => count === 1 ? singular : pluralForm;
  const appendText = (parent, tag, text, className = "") => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = text;
    parent.append(element);
    return element;
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

  const setLevelLabel = () => {
    levelLabel.textContent = ({
      spell: "Research level",
      summon: "Research level",
      item: "Construction level",
      site: "Search level",
      throne: "Throne level",
    })[category.value] || "Recorded level";
  };

  const applyUrlState = () => {
    const url = new URL(window.location.href);
    for (const [key, value] of new FormData(form)) {
      if (value) url.searchParams.set(key, value);
      else url.searchParams.delete(key);
    }
    window.history.replaceState({}, "", `${url.pathname}${url.search}${url.hash}`);
  };

  const makeMeta = (record) => {
    const meta = document.createElement("div");
    meta.className = "reference-record-meta";
    [
      record.categoryLabel,
      record.engineId === null ? "" : `ID ${record.engineId}`,
      record.paths?.length ? record.paths.join(" ") : "",
      record.eras?.length ? record.eras.join(" ") : "",
      record.level === null ? "" : `Level ${record.level}`,
      pretty(record.evidence),
    ].filter(Boolean).forEach((value) => appendText(meta, "span", value));
    return meta;
  };

  const makeRecord = (record) => {
    const card = document.createElement("details");
    card.className = "reference-record";
    const summary = document.createElement("summary");
    const summaryText = document.createElement("div");
    summaryText.className = "reference-record-title";
    appendText(summaryText, "h3", record.name);
    appendText(summaryText, "p", record.summary || "No short summary is recorded for this entry.");
    summary.append(summaryText, makeMeta(record));
    card.append(summary);

    const body = document.createElement("div");
    body.className = "reference-record-body";
    const facts = document.createElement("dl");
    facts.className = "reference-fact-list";
    const rows = [
      ["Record ID", record.id],
      ["Status", pretty(record.status)],
      ...(record.attributes || []),
    ];
    for (const [label, value] of rows) {
      const row = document.createElement("div");
      appendText(row, "dt", label);
      appendText(row, "dd", value || "Not recorded");
      facts.append(row);
    }
    body.append(facts);

    if (record.properties?.length) {
      const propertyBlock = document.createElement("div");
      propertyBlock.className = "reference-properties";
      appendText(propertyBlock, "h4", "Mechanical properties");
      const propertyList = document.createElement("dl");
      for (const [key, value] of record.properties) {
        const row = document.createElement("div");
        appendText(row, "dt", pretty(key));
        appendText(row, "dd", String(value));
        propertyList.append(row);
      }
      propertyBlock.append(propertyList);
      body.append(propertyBlock);
    }

    const boundary = document.createElement("p");
    boundary.className = "reference-evidence-line";
    boundary.textContent = `Evidence: ${pretty(record.evidence)} · Ruleset: ${catalogue.ruleset.game} ${catalogue.ruleset.game_version}, no mods.`;
    const link = document.createElement("a");
    link.className = "text-link";
    link.href = record.libraryUrl;
    link.textContent = "Open the matching Library section →";
    body.append(boundary, link);
    card.append(body);
    return card;
  };

  const render = () => {
    results.replaceChildren();
    const shown = filtered.slice(0, visible);
    shown.forEach((record) => results.append(makeRecord(record)));
    heading.textContent = `${filtered.length.toLocaleString("en-AU")} ${plural(filtered.length, "record")}`;
    status.textContent = filtered.length
      ? `Showing ${shown.length.toLocaleString("en-AU")} of ${filtered.length.toLocaleString("en-AU")} matching ${plural(filtered.length, "record")}. Open a row for the full entry.`
      : "No records match those filters.";
    more.hidden = shown.length >= filtered.length;
    more.textContent = `Show ${Math.min(batchSize, filtered.length - shown.length).toLocaleString("en-AU")} more records`;
  };

  const filter = () => {
    if (!catalogue) return;
    const values = Object.fromEntries(new FormData(form));
    const terms = normalise(values.query).split(/\s+/).filter(Boolean);
    filtered = catalogue.records.filter((record) => (
      (!values.category || record.category === values.category)
      && (!values.path || record.paths.includes(values.path))
      && (!values.era || record.eras.includes(values.era))
      && (!values.level || String(record.level) === values.level)
      && (!values.evidence || record.evidence === values.evidence)
      && terms.every((term) => record.searchText.includes(term))
    ));
    visible = batchSize;
    setLevelLabel();
    applyUrlState();
    render();
  };

  const restoreUrlState = () => {
    const params = new URLSearchParams(window.location.search);
    for (const field of form.elements) {
      if (field.name && params.has(field.name)) field.value = params.get(field.name);
    }
  };

  form.addEventListener("input", filter);
  form.addEventListener("change", filter);
  form.addEventListener("submit", (event) => event.preventDefault());
  form.addEventListener("reset", () => window.setTimeout(filter, 0));
  more.addEventListener("click", () => {
    visible += batchSize;
    render();
  });

  fetch(referenceRoot.dataset.sourceUrl)
    .then((response) => {
      if (!response.ok) throw new Error(`catalogue request returned ${response.status}`);
      return response.arrayBuffer();
    })
    .then((buffer) => {
      const bytes = new Uint8Array(buffer);
      if (bytes[0] !== 0x1f || bytes[1] !== 0x8b) return new Response(buffer).json();
      if (!("DecompressionStream" in window)) throw new Error("this browser cannot open the compressed catalogue");
      const stream = new Blob([buffer]).stream().pipeThrough(new DecompressionStream("gzip"));
      return new Response(stream).json();
    })
    .then((data) => {
      if (!Array.isArray(data.records)) throw new Error("the catalogue does not contain records");
      catalogue = data;
      catalogue.records.forEach((record) => { record.searchText = recordSearchText(record); });
      const evidenceStates = [...new Set(catalogue.records.map((record) => record.evidence).filter(Boolean))].sort();
      evidenceStates.forEach((value) => evidence.add(new Option(pretty(value), value)));
      total.textContent = `${catalogue.totalRecords.toLocaleString("en-AU")} records`;
      restoreUrlState();
      filter();
    })
    .catch((error) => {
      heading.textContent = "Catalogue could not be loaded";
      status.textContent = `The reference file could not be opened: ${error.message}`;
      more.hidden = true;
    });
}
