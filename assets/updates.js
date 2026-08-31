const updateArchive = document.querySelector("[data-update-archive]");

if (updateArchive) {
  const query = updateArchive.querySelector("[data-update-query]");
  const project = updateArchive.querySelector("[data-update-project]");
  const type = updateArchive.querySelector("[data-update-type]");
  const count = updateArchive.querySelector("[data-update-count]");
  const entries = [...updateArchive.querySelectorAll("[data-update-entry]")];

  const normalise = (value) => String(value || "")
    .toLocaleLowerCase("en-AU")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "");

  const applyUrl = () => {
    const params = new URLSearchParams();
    if (query.value.trim()) params.set("q", query.value.trim());
    if (project.value !== "all") params.set("project", project.value);
    if (type.value !== "all") params.set("type", type.value);
    const search = params.toString();
    window.history.replaceState({}, "", `${window.location.pathname}${search ? `?${search}` : ""}`);
  };

  const filter = () => {
    const words = normalise(query.value).split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const entry of entries) {
      const matchesQuery = words.every((word) => normalise(entry.dataset.search).includes(word));
      const matchesProject = project.value === "all" || entry.dataset.project === project.value;
      const matchesType = type.value === "all" || entry.dataset.type === type.value;
      entry.hidden = !(matchesQuery && matchesProject && matchesType);
      if (!entry.hidden) visible += 1;
    }
    count.textContent = `Showing ${visible} of ${entries.length} recorded update${entries.length === 1 ? "" : "s"}.`;
    applyUrl();
  };

  const params = new URLSearchParams(window.location.search);
  query.value = params.get("q") || "";
  if ([...project.options].some((option) => option.value === params.get("project"))) project.value = params.get("project");
  if ([...type.options].some((option) => option.value === params.get("type"))) type.value = params.get("type");
  query.addEventListener("input", filter);
  project.addEventListener("change", filter);
  type.addEventListener("change", filter);
  filter();
}
