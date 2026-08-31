const reportPage = document.querySelector("[data-report-page]");

if (reportPage) {
  const params = new URLSearchParams(window.location.search);
  const suppliedPage = params.get("page");
  const fallbackPage = document.referrer && new URL(document.referrer).origin === window.location.origin
    ? document.referrer
    : window.location.href;
  const sourcePage = suppliedPage || fallbackPage;
  const sourceTitle = params.get("title") || "Page title not supplied";
  const context = reportPage.querySelector("[data-report-context]");
  const repository = reportPage.dataset.reportRepository;
  const reports = {
    correction: {
      prefix: "Correction",
      labels: "correction,evidence",
      template: "factual-correction.md",
      prompt: [
        "## What appears to be wrong?",
        "",
        "Describe the claim, value, record, label, or version statement that needs checking.",
        "",
        "## What should it say instead?",
        "",
        "Give the corrected wording or value if known.",
        "",
        "## Evidence",
        "",
        "Name the manual page, game version, controlled test, source file, or other evidence used.",
      ],
    },
    tool: {
      prefix: "Tool fault",
      labels: "bug,tools",
      template: "tool-fault.md",
      prompt: [
        "## What were you trying to do?",
        "",
        "Describe the tool and the result you were trying to produce.",
        "",
        "## What happened?",
        "",
        "Include the values entered, the result shown, and what you expected instead.",
        "",
        "## Device and browser",
        "",
        "Add the device and browser if the fault may depend on screen size or browser storage.",
      ],
    },
    broken: {
      prefix: "Site problem",
      labels: "bug,site",
      template: "broken-page-or-link.md",
      prompt: [
        "## What is broken?",
        "",
        "Describe the missing page, dead link, wrong download, layout fault, or navigation problem.",
        "",
        "## Where did it lead or fail?",
        "",
        "Add the destination address or visible error if one was shown.",
      ],
    },
    feature: {
      prefix: "Improvement",
      labels: "enhancement",
      template: "focused-improvement.md",
      prompt: [
        "## What should be added or changed?",
        "",
        "Describe the specific addition and where it belongs.",
        "",
        "## What would it help with?",
        "",
        "Explain the practical problem it would solve for the project, guide, or tool.",
      ],
    },
  };

  const displayedPage = (() => {
    try {
      const url = new URL(sourcePage);
      return `${url.pathname}${url.hash}`;
    } catch {
      return sourcePage;
    }
  })();
  context.textContent = sourceTitle === "Page title not supplied"
    ? displayedPage
    : `${sourceTitle} — ${displayedPage}`;

  reportPage.querySelectorAll("[data-report-kind]").forEach((link) => {
    const report = reports[link.dataset.reportKind];
    if (!report) return;
    const issue = new URL(`${repository}/issues/new`);
    issue.searchParams.set("template", report.template);
    issue.searchParams.set("title", `[${report.prefix}] ${sourceTitle}`);
    issue.searchParams.set("labels", report.labels);
    issue.searchParams.set("body", [
      ...report.prompt,
      "",
      "## Page and release context",
      "",
      `- Page: ${sourcePage}`,
      `- Page title: ${sourceTitle}`,
      "- Dominions edition or game version, if relevant:",
      "- Date checked:",
    ].join("\n"));
    link.href = issue.toString();
  });
}
