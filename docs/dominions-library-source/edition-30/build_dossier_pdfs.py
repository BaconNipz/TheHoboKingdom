#!/usr/bin/env python3
"""Build standalone PDFs for the compact Middle Age nation dossiers."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build_pdf as library_pdf  # noqa: E402
from build_pdf import (  # noqa: E402
    GOLD,
    INK,
    LINE,
    MUTED,
    NAVY,
    NAVY_2,
    PAGE_H,
    PAGE_W,
    STYLES,
    WHITE,
    markdown_to_story,
)

SOURCE = ROOT / "12-foundation-book-vii-nations-arcoscephale.md"
OUTPUT_DIR = ROOT.parent / "output" / "pdf"


@dataclass
class MemoryMarkdown:
    name: str
    text: str

    def read_text(self, encoding: str = "utf-8") -> str:
        return self.text


class DossierDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, title: str):
        super().__init__(
            filename,
            pagesize=A4,
            rightMargin=18 * mm,
            leftMargin=18 * mm,
            topMargin=20 * mm,
            bottomMargin=20 * mm,
            title=f"Dominions 6 Nation Dossier - {title}",
            author="TheHoboKingdom",
            subject="Dominions 6 unmodded nation strategy, roster, research, magic, and verification",
            creator="TheHoboKingdom",
        )
        self.heading_counter = 0

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        levels = {"ArchiveH1": 0, "ArchiveH2": 1, "ArchiveH3": 2}
        if flowable.style.name not in levels:
            return
        level = levels[flowable.style.name]
        text = flowable.getPlainText()
        key = getattr(flowable, "_archive_bookmark_key", None)
        if key is None:
            key = f"heading-{self.heading_counter}"
            flowable._archive_bookmark_key = key
            self.heading_counter += 1
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
        if level <= 1:
            self.notify("TOCEntry", (level, text, self.page, key))


def cover_drawer(label: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        canvas.setFillColor(NAVY_2)
        canvas.rect(0, 0, PAGE_W, 33 * mm, fill=1, stroke=0)
        canvas.setFillColor(GOLD)
        canvas.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
        canvas.rect(18 * mm, PAGE_H - 59 * mm, 34 * mm, 1.5 * mm, fill=1, stroke=0)
        canvas.setFont("DejaVuSans", 7.5)
        canvas.setFillColor(colors.HexColor("#AEBBC9"))
        canvas.drawString(18 * mm, 17 * mm, "THEHOBOKINGDOM")
        canvas.setFillColor(GOLD)
        canvas.drawRightString(PAGE_W - 18 * mm, 17 * mm, label.upper())
        canvas.restoreState()

    return draw


def body_drawer(label: str, published_label: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(0.75)
        canvas.line(18 * mm, PAGE_H - 13 * mm, PAGE_W - 18 * mm, PAGE_H - 13 * mm)
        canvas.setFont("DejaVuSans-Bold", 7.2)
        canvas.setFillColor(NAVY)
        canvas.drawString(18 * mm, PAGE_H - 10 * mm, "DOMINIONS 6 NATION DOSSIER")
        canvas.setFont("DejaVuSans", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 10 * mm, label.upper())
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.45)
        canvas.line(18 * mm, 13 * mm, PAGE_W - 18 * mm, 13 * mm)
        canvas.setFont("DejaVuSans", 7.1)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 8.5 * mm, f"TheHoboKingdom | {published_label}")
        canvas.drawRightString(PAGE_W - 18 * mm, 8.5 * mm, f"Page {doc.page}")
        canvas.restoreState()

    return draw


def section(text: str, start: str, end: str | None) -> str:
    begin = text.index(start)
    finish = text.index(end, begin) if end else len(text)
    return text[begin:finish].strip() + "\n"


def standalone_source_register(source_register: str, slug: str) -> str:
    """Keep the shared provenance block focused on the extracted nation."""
    if slug == "ulm":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Ulm nation pages; national spells and rituals; research; mounts; forging; "
                "and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36. No MA Ulm rule change from the "
                "patch ledger was silently applied to the older structured snapshot.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, random-result timing, displayed forge-cost stacking, spell "
                "targeting, and combat outcomes remain observation questions until a versioned "
                "raw set is published.",
            )
        )

    if slug == "man":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Man nation pages; national spells and rituals; research; communions and "
                "Chorus; mounts; forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36, including the 6.13 Forest of "
                "Avalon Magic correction. No later MA Man change was inferred where the official "
                "record does not name the nation or object.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live random displays, Chorus and Geas targeting, "
                "rider-and-mount outcomes, and other combat results remain observation questions "
                "until a versioned raw set is published.",
            )
        )

    if slug == "abysia":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Abysia nation pages; national spells and rituals; Blood and crossbreeding; "
                "forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36, including the 6.01 Abysia "
                "wall-defender note. No numerical defender change was inferred where the "
                "announcement supplied none.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live random displays, cave-fort arithmetic, wall-defender "
                "composition, crossbreeding outputs, displayed forge-cost stacking, spell "
                "behaviour, and combat outcomes remain observation questions until a versioned "
                "raw set is published.",
            )
        )

    if slug == "pythium":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Pythium nation pages; national spells and rituals; research; communions and "
                "Grand Communion; mounts; forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36. The only Pythium name match is "
                "the 6.07 Epoteia correction for Late Age Pythium, so it is not applied here.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live random displays, displayed forge-cost stacking, "
                "communion and Grand Communion outcomes, hydra behaviour, Single Battle timing, "
                "rider-and-mount outcomes, and other combat results remain observation questions "
                "until a versioned raw set is published.",
            )
        )

    if slug == "eriu":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Eriu nation pages; national spells and rituals; research; Chorus; mounts; "
                "forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36, including Eriu's 6.01 "
                "terrain-recruit and Bean Sidhe corrections. No later Eriu change was inferred "
                "where the official record does not name the nation or object.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live random displays, terrain-interface edge cases, displayed "
                "forge-cost stacking, Spell Singer outcomes, Glamour detection, rider-and-mount "
                "outcomes, and other combat results remain observation questions until a "
                "versioned raw set is published.",
            )
        )

    if slug == "agartha":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Agartha nation pages; national spells and rituals; research; dominion; "
                "amphibious movement; forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36, including Agartha's 6.04 "
                "Oracle-shape note. No transformation mechanics were inferred from the short "
                "announcement.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live random displays, cave-fort arithmetic, Golem Cult "
                "scaling and affected ownership, underwater operations, variable summon counts, "
                "transformation outcomes, and other combat results remain observation questions "
                "until a versioned raw set is published.",
            )
        )

    if slug == "uruk":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Uruk nation pages; national spells and rituals; national items; research; "
                "mounts; amphibious movement; forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36. No direct Uruk, Enkidu, "
                "Mushussu, or named Uruk national-ritual match was found; no change was inferred "
                "from a negative ledger result.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live Entu and Mashmashu secondary random displays, Call God "
                "arithmetic, Spell Singer outcomes, Mushussu rider-and-mount behaviour, "
                "underwater operations, variable summon scaling, displayed national-item "
                "costs, hero timing, and other combat results remain observation questions "
                "until a versioned raw set is published.",
            )
        )

    if slug == "ashdod":
        return (
            source_register.replace(
                "MA Marignon, MA Pyrène, MA Ulm, MA Man, MA Abysia, MA Pythium, MA Eriu, MA Agartha, MA Uruk, and MA Ashdod nation pages; national spells and "
                "rituals; research; communions, Chorus, and Grand Communion; Blood and crossbreeding; Inquisition; mounts; forging; "
                "and fort construction.",
                "MA Ashdod nation pages; national spells and rituals; research; sacreds; "
                "forging; and fort construction.",
            )
            .replace(
                "Illwinter official patch history through 6.36, including the current Send "
                "Aatxe restriction, communion corrections, the 6.13 Forest of Avalon Magic "
                "correction, the 6.01 Abysia wall-defender note, Eriu's 6.01 terrain-recruit and Bean Sidhe corrections, and Agartha's 6.04 Oracle-shape note. The only Pythium name match applies explicitly to Late Age Pythium. Nation-specific changes are attached only where the record names "
                "the affected object.",
                "Illwinter official patch history through 6.36. No direct Ashdod, Anakite, "
                "Rephaite, Zamzummite, or named Ashdod national-spell match was found; no "
                "change was inferred from a negative ledger result.",
            )
            .replace(
                "Expansion counts, random-result timing, Blood returns, crossbreeding outputs, "
                "displayed forge-cost stacking, communion and Grand Communion outcomes, hydra-field behaviour, Spell Singer outcomes, Glamour detection, special-dominion scaling and targeting, spell targeting, and combat outcomes remain "
                "observation questions until a versioned raw set is published.",
                "Expansion counts, live Kohen and Talmai secondary random displays, Strange "
                "Fire targeting and results, angel and ancestor retinue and shape behaviour, "
                "giant logistics, hero timing, and other combat results remain observation "
                "questions until a versioned raw set is published.",
            )
        )

    return source_register


def build_one(
    slug: str,
    title: str,
    epithet: str,
    body: str,
    edition: int,
    published_label: str,
) -> Path:
    output = OUTPUT_DIR / f"dominions-6-ma-{slug}-nation-dossier-edition-{edition}.pdf"
    doc = DossierDocTemplate(str(output), title)
    cover_frame = Frame(18 * mm, 33 * mm, PAGE_W - 36 * mm, PAGE_H - 55 * mm, id="cover")
    body_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    label = f"{title} | Edition {edition}"
    doc.addPageTemplates(
        [
            PageTemplate(
                id="Cover",
                frames=[cover_frame],
                onPage=cover_drawer(label),
                autoNextPageTemplate="Body",
            ),
            PageTemplate(
                id="Body",
                frames=[body_frame],
                onPage=body_drawer(label, published_label),
                autoNextPageTemplate="Body",
            ),
        ]
    )

    story = [
        Spacer(1, 42 * mm),
        Paragraph("DOMINIONS 6 NATION DOSSIER", STYLES["cover_kicker"]),
        Paragraph(f"Middle Age<br/>{title}", STYLES["cover_title"]),
        Paragraph(epithet, STYLES["cover_subtitle"]),
        Spacer(1, 8 * mm),
        HRFlowable(width=44 * mm, thickness=1.4, color=GOLD, hAlign="LEFT"),
        Spacer(1, 8 * mm),
        Paragraph(
            f"<b>Progress Edition {edition}</b><br/>{published_label}<br/><br/>"
            "Unmodded 6.36 doctrine with source-labelled rules, strategy, and open verification work.",
            STYLES["cover_note"],
        ),
        NextPageTemplate("Body"),
        PageBreak(),
        Paragraph("Contents", STYLES["toc_title"]),
    ]

    toc = TableOfContents()
    toc.levelStyles = [
        STYLES["h2"].clone("DossierTOC1", fontSize=9.4, leading=13, leftIndent=0, spaceBefore=2, spaceAfter=1),
        STYLES["body"].clone("DossierTOC2", fontSize=8.1, leading=11, leftIndent=14, textColor=INK),
    ]
    story.extend([toc, PageBreak()])
    # Cross-book anchors remain live in the complete library. Standalone
    # dossiers retain their readable labels without unresolved PDF targets.
    body = re.sub(r"\[([^\]]+)\]\(#[^)]+\)", r"\1", body)
    memory = MemoryMarkdown(f"{slug}-dossier.md", body)
    story.extend(markdown_to_story(memory, doc.width))
    doc.multiBuild(story)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--nation",
        choices=["all", "marignon", "pyrene", "ulm", "man", "abysia", "pythium", "eriu", "agartha", "uruk", "ashdod", "tien-chi"],
        default="all",
        help="Build one dossier or every compact dossier (default: all).",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVuSansMono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))

    # The complete library turns prose such as "Book V" into live internal
    # links. Those destinations are intentionally absent from a nation-only
    # extract, so keep the labels but disable that automatic link layer here.
    library_pdf.BOOK_TARGETS = {}
    library_pdf.PART_TARGETS = {}
    library_pdf.SECTION_TARGETS = {}

    text = SOURCE.read_text(encoding="utf-8")
    source_register = section(text, "## Dossier source register", None)
    marignon = section(
        text,
        "# Part XVI: Middle Age Marignon, Fiery Justice",
        "# Part XVII: Middle Age Pyrène, Time of the Akelarre",
    ).replace("# Part XVI: Middle Age Marignon, Fiery Justice", "# Middle Age Marignon: Fiery Justice", 1)
    pyrene = section(
        text,
        "# Part XVII: Middle Age Pyrène, Time of the Akelarre",
        "# Part XVIII: Middle Age Ulm, Forges of Ulm",
    ).replace("# Part XVII: Middle Age Pyrène, Time of the Akelarre", "# Middle Age Pyrène: Time of the Akelarre", 1)
    ulm = section(
        text,
        "# Part XVIII: Middle Age Ulm, Forges of Ulm",
        "# Part XIX: Middle Age Man, Tower of Avalon",
    ).replace("# Part XVIII: Middle Age Ulm, Forges of Ulm", "# Middle Age Ulm: Forges of Ulm", 1)
    man = section(
        text,
        "# Part XIX: Middle Age Man, Tower of Avalon",
        "# Part XX: Middle Age Abysia, Blood and Fire",
    ).replace("# Part XIX: Middle Age Man, Tower of Avalon", "# Middle Age Man: Tower of Avalon", 1)
    abysia = section(
        text,
        "# Part XX: Middle Age Abysia, Blood and Fire",
        "# Part XXI: Middle Age Pythium, Emerald Empire",
    ).replace("# Part XX: Middle Age Abysia, Blood and Fire", "# Middle Age Abysia: Blood and Fire", 1)
    pythium = section(
        text,
        "# Part XXI: Middle Age Pythium, Emerald Empire",
        "# Part XXII: Middle Age Eriu, Last of the Tuatha",
    ).replace("# Part XXI: Middle Age Pythium, Emerald Empire", "# Middle Age Pythium: Emerald Empire", 1)
    eriu = section(
        text,
        "# Part XXII: Middle Age Eriu, Last of the Tuatha",
        "# Part XXIII: Middle Age Agartha, Golem Cult",
    ).replace("# Part XXII: Middle Age Eriu, Last of the Tuatha", "# Middle Age Eriu: Last of the Tuatha", 1)
    agartha = section(
        text,
        "# Part XXIII: Middle Age Agartha, Golem Cult",
        "# Part XXIV: Middle Age Uruk, City States",
    ).replace("# Part XXIII: Middle Age Agartha, Golem Cult", "# Middle Age Agartha: Golem Cult", 1)
    uruk = section(
        text,
        "# Part XXIV: Middle Age Uruk, City States",
        "# Part XXV: Middle Age Ashdod, Reign of the Anakim",
    ).replace("# Part XXIV: Middle Age Uruk, City States", "# Middle Age Uruk: City States", 1)
    ashdod = section(
        text,
        "# Part XXV: Middle Age Ashdod, Reign of the Anakim",
        "# Part XXVI: Middle Age T'ien Ch'i, Imperial Bureaucracy",
    ).replace("# Part XXV: Middle Age Ashdod, Reign of the Anakim", "# Middle Age Ashdod: Reign of the Anakim", 1)
    tien_chi = section(
        text,
        "# Part XXVI: Middle Age T'ien Ch'i, Imperial Bureaucracy",
        "## Dossier source register",
    ).replace("# Part XXVI: Middle Age T'ien Ch'i, Imperial Bureaucracy", "# Middle Age T'ien Ch'i: Imperial Bureaucracy", 1)

    dossiers = [
        ("marignon", "Marignon", "Fiery Justice", marignon, 27, "28 August 2026"),
        ("pyrene", "Pyrène", "Time of the Akelarre", pyrene, 27, "28 August 2026"),
        ("ulm", "Ulm", "Forges of Ulm", ulm, 29, "2 September 2026"),
        ("man", "Man", "Tower of Avalon", man, 29, "2 September 2026"),
        ("abysia", "Abysia", "Blood and Fire", abysia, 29, "2 September 2026"),
        ("pythium", "Pythium", "Emerald Empire", pythium, 29, "3 September 2026"),
        ("eriu", "Eriu", "Last of the Tuatha", eriu, 29, "3 September 2026"),
        ("agartha", "Agartha", "Golem Cult", agartha, 29, "4 September 2026"),
        ("uruk", "Uruk", "City States", uruk, 29, "4 September 2026"),
        ("ashdod", "Ashdod", "Reign of the Anakim", ashdod, 29, "7 September 2026"),
        ("tien-chi", "T'ien Ch'i", "Imperial Bureaucracy", tien_chi, 29, "8 September 2026"),
    ]
    outputs = [
        build_one(
            slug,
            title,
            epithet,
            body + "\n" + standalone_source_register(source_register, slug),
            edition,
            published_label,
        )
        for slug, title, epithet, body, edition, published_label in dossiers
        if args.nation in {"all", slug}
    ]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
