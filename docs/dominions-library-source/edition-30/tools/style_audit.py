#!/usr/bin/env python3
"""Audit the reader-facing corpus for recurring editorial patterns.

The report is diagnostic. A hit is a prompt to read the sentence, not proof that
the sentence must be changed.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from navigation import SOURCE_SPECS  # noqa: E402


PATTERNS = {
    "chapter announcement": r"\bthis (?:book|chapter|volume|edition|section|reference)\b",
    "rather than": r"\brather than\b",
    "not merely": r"\bnot merely\b",
    "not simply": r"\bnot simply\b",
    "not just": r"\bnot just\b",
    "therefore": r"\btherefore\b",
    "however": r"\bhowever\b",
    "in practice": r"\bin practice\b",
    "stock emphasis": r"\b(?:crucially|fundamentally|importantly|notably)\b",
    "note announcement": r"\bit is (?:important|useful|worth) to (?:note|remember|understand)\b",
    "takeaway": r"\b(?:the key takeaway|the key point|the key idea)\b",
    "abstract system noun": r"\b(?:framework|architecture|discipline|paradigm|ecosystem)\b",
    "direct second person": r"\b(?:you|your|you're|you'll|you've)\b",
}


def strip_locked_blocks(text: str) -> str:
    """Remove tables, code blocks and link destinations from prose diagnostics."""
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("|"))
    return re.sub(r"\]\([^)]*\)", "]", text)


def main() -> None:
    totals: Counter[str] = Counter()
    for spec in SOURCE_SPECS:
        path = ROOT / spec.filename
        text = strip_locked_blocks(path.read_text(encoding="utf-8"))
        counts = Counter(
            {
                label: len(re.findall(pattern, text, flags=re.IGNORECASE))
                for label, pattern in PATTERNS.items()
            }
        )
        totals.update(counts)
        summary = " ".join(f"{label}={count}" for label, count in counts.items() if count)
        print(f"{spec.code:>5}  {summary or 'clean'}")
    print("TOTAL  " + " ".join(f"{label}={count}" for label, count in totals.items() if count))


if __name__ == "__main__":
    main()
