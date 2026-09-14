#!/usr/bin/env python3
"""Build the four split reader-facing PDFs for Progress Edition 28."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

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


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT.parent / "output" / "pdf"
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
    markdown_to_story,
)


@dataclass(frozen=True)
class ReaderSpec:
    slug: str
    title: str
    cover_title: str
    short_label: str
    subtitle: str
    introduction: str
    subject: str
    sources: tuple[str, ...]


@dataclass
class MemoryMarkdown:
    name: str
    text: str

    def read_text(self, encoding: str = "utf-8") -> str:
        return self.text


READERS = (
    ReaderSpec(
        slug="core-rules-and-strategy",
        title="Core Rules and Strategy",
        cover_title="Core Rules<br/>and Strategy",
        short_label="CORE RULES & STRATEGY",
        subtitle=(
            "Rulesets, turn structure, economy, Pretenders, battle, magic, "
            "and campaign conduct."
        ),
        introduction=(
            "This volume contains the Reader's Guide and Foundation Books I-VI. "
            "The standalone field reference, nation compendium, and technical volume "
            "remain separate downloads. Book and section names stay unchanged so "
            "references remain compatible with the omnibus and website."
        ),
        subject="Dominions 6 core rules, economy, Pretenders, battle, magic, and strategy",
        sources=(
            "16-reader-guide-concordance.md",
            "04-foundation-book-i.md",
            "06-foundation-book-ii-economy-state.md",
            "07-foundation-book-iii-pretenders-dominion-scales-blesses.md",
            "08-foundation-book-iv-armies-and-battle.md",
            "09-foundation-book-v-magic.md",
            "10-foundation-book-vi-strategy.md",
        ),
    ),
    ReaderSpec(
        slug="middle-age-nation-compendium-volume-1",
        title="Middle Age Nation Compendium - Volume I",
        cover_title="Middle Age<br/>Nation Compendium",
        short_label="MIDDLE AGE | VOLUME I",
        subtitle="Volume I: Arcoscephale, Marignon, and Pyrène.",
        introduction=(
            "This first Middle Age volume contains the complete Arcoscephale, "
            "Marignon, and Pyrène dossiers from Book VII. It does not present the "
            "remaining Middle Age nations as finished."
        ),
        subject="Dominions 6 Middle Age nation dossiers and strategy",
        sources=("12-foundation-book-vii-nations-arcoscephale.md",),
    ),
    ReaderSpec(
        slug="technical-and-modding-reference",
        title="Technical and Modding Reference",
        cover_title="Technical and<br/>Modding Reference",
        short_label="TECHNICAL & MODDING",
        subtitle=(
            "Modding, DE and Divinitus, player operations, abilities, objects, "
            "patch history, and command lookup."
        ),
        introduction=(
            "This volume contains Foundation Books VIII-XIV. It keeps the technical, "
            "operational, object, patch-history, and command-reference material in one "
            "place without duplicating the core rules or nation compendium."
        ),
        subject="Dominions 6 technical, operational, object, patch, and modding reference",
        sources=(
            "13-foundation-book-viii-modding-scenarios.md",
            "14-foundation-book-ix-de-divinitus.md",
            "19-foundation-book-x-player-operations.md",
            "21-foundation-book-xi-unit-ability-reference.md",
            "24-foundation-book-xii-base-game-object-reference.md",
            "26-foundation-book-xiii-official-patch-history.md",
            "28-foundation-book-xiv-command-terminology-lexicon.md",
        ),
    ),
    ReaderSpec(
        slug="turn-and-economy-quick-reference",
        title="Turn and Economy Quick Reference",
        cover_title="Turn and Economy<br/>Quick Reference",
        short_label="QUICK REFERENCE",
        subtitle="The compact play-side reference from Progress Edition 28.",
        introduction=(
            "This compact volume contains the Turn and Economy Quick Reference from "
            "Edition 28. Full explanations and evidence remain in the omnibus, core "
            "volume, and searchable website."
        ),
        subject="Dominions 6 turn order, economy, recruitment, forts, and logistics reference",
        sources=("05-turn-and-economy-quick-reference.md",),
    ),
)


class ReaderDocTemplate(BaseDocTemplate):
    def __init__(
        self,
        filename: str,
        spec: ReaderSpec,
        aliases_by_target: dict[str, list[str]],
    ):
        super().__init__(
            filename,
            pagesize=A4,
            rightMargin=18 * mm,
            leftMargin=18 * mm,
            topMargin=20 * mm,
            bottomMargin=20 * mm,
            title=f"Dominions 6 Knowledge Library - {spec.title}",
            author="TheHoboKingdom",
            subject=spec.subject,
            creator="TheHoboKingdom",
        )
        self.aliases_by_target = aliases_by_target
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
        for alias in self.aliases_by_target.get(key, []):
            self.canv.bookmarkPage(alias)
        self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
        if level <= 1:
            self.notify("TOCEntry", (level, text, self.page, key))


def cover_drawer(spec: ReaderSpec):
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
        canvas.drawRightString(PAGE_W - 18 * mm, 17 * mm, spec.short_label)
        canvas.restoreState()

    return draw


def body_drawer(spec: ReaderSpec):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(0.75)
        canvas.line(18 * mm, PAGE_H - 13 * mm, PAGE_W - 18 * mm, PAGE_H - 13 * mm)
        canvas.setFont("DejaVuSans-Bold", 7.2)
        canvas.setFillColor(NAVY)
        canvas.drawString(18 * mm, PAGE_H - 10 * mm, "DOMINIONS 6 KNOWLEDGE LIBRARY")
        canvas.setFont("DejaVuSans", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 10 * mm, spec.short_label)
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.45)
        canvas.line(18 * mm, 13 * mm, PAGE_W - 18 * mm, 13 * mm)
        canvas.setFont("DejaVuSans", 7.1)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 8.5 * mm, "TheHoboKingdom | 30 August 2026")
        canvas.drawRightString(PAGE_W - 18 * mm, 8.5 * mm, f"Page {doc.page}")
        canvas.restoreState()

    return draw


def configure_navigation(source_names: tuple[str, ...]):
    allowed_targets = {
        record.anchor
        for source_name in source_names
        for record in library_pdf.HEADING_CATALOG.get(source_name, [])
    }
    aliases_by_target = {
        target: aliases
        for target, aliases in library_pdf.ALIASES_BY_TARGET.items()
        if target in allowed_targets
    }
    allowed_links = set(allowed_targets)
    for aliases in aliases_by_target.values():
        allowed_links.update(aliases)

    library_pdf.BOOK_TARGETS = {
        key: target
        for key, target in library_pdf.cross_reference_targets(
            library_pdf.HEADING_CATALOG
        )[0].items()
        if target in allowed_targets
    }
    library_pdf.PART_TARGETS = {
        key: target
        for key, target in library_pdf.cross_reference_targets(
            library_pdf.HEADING_CATALOG
        )[1].items()
        if target in allowed_targets
    }
    library_pdf.SECTION_TARGETS = {
        key: target
        for key, target in library_pdf.cross_reference_targets(
            library_pdf.HEADING_CATALOG
        )[2].items()
        if target in allowed_targets
    }
    return allowed_links, aliases_by_target


def strip_missing_internal_links(text: str, allowed_links: set[str]) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        return match.group(0) if target in allowed_links else label

    return re.sub(r"\[([^\]]+)\]\(#([A-Za-z0-9_.:-]+)\)", replace, text)


def build_one(spec: ReaderSpec) -> Path:
    output = OUTPUT_DIR / f"dominions-6-{spec.slug}-edition-28.pdf"
    allowed_links, aliases_by_target = configure_navigation(spec.sources)
    doc = ReaderDocTemplate(str(output), spec, aliases_by_target)
    cover_frame = Frame(18 * mm, 33 * mm, PAGE_W - 36 * mm, PAGE_H - 55 * mm, id="cover")
    body_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates(
        [
            PageTemplate(id="Cover", frames=[cover_frame], onPage=cover_drawer(spec)),
            PageTemplate(id="Body", frames=[body_frame], onPage=body_drawer(spec)),
        ]
    )

    story = [
        Spacer(1, 40 * mm),
        Paragraph("DOMINIONS 6 KNOWLEDGE LIBRARY", STYLES["cover_kicker"]),
        Paragraph(spec.cover_title, STYLES["cover_title"]),
        Paragraph(spec.subtitle, STYLES["cover_subtitle"]),
        Spacer(1, 7 * mm),
        HRFlowable(width=44 * mm, thickness=1.4, color=GOLD, hAlign="LEFT"),
        Spacer(1, 7 * mm),
        Paragraph(
            "<b>Progress Edition 28 companion reader</b><br/>"
            "30 August 2026<br/><br/>"
            "Unmodded 6.36 baseline. DE and Divinitus remain separately labelled.",
            STYLES["cover_note"],
        ),
        NextPageTemplate("Body"),
        PageBreak(),
        Paragraph("Contents", STYLES["toc_title"]),
        Paragraph(spec.introduction, STYLES["body"]),
        Spacer(1, 5),
    ]

    toc = TableOfContents()
    toc.levelStyles = [
        STYLES["h2"].clone(
            f"{spec.slug}TOC1",
            fontSize=9.4,
            leading=13,
            leftIndent=0,
            spaceBefore=2,
            spaceAfter=1,
        ),
        STYLES["body"].clone(
            f"{spec.slug}TOC2",
            fontSize=8.1,
            leading=11,
            leftIndent=14,
            textColor=INK,
        ),
    ]
    story.extend([toc, PageBreak()])

    for index, source_name in enumerate(spec.sources):
        if index:
            story.append(PageBreak())
        story.append(
            Paragraph(
                f"DOCUMENT {index + 1} OF {len(spec.sources)}",
                STYLES["section_label"],
            )
        )
        source = ROOT / source_name
        text = strip_missing_internal_links(
            source.read_text(encoding="utf-8"), allowed_links
        )
        story.extend(markdown_to_story(MemoryMarkdown(source_name, text), doc.width))

    doc.multiBuild(story)
    return output


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(
        TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    )
    pdfmetrics.registerFont(
        TTFont(
            "DejaVuSans-Bold",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        )
    )
    pdfmetrics.registerFont(
        TTFont(
            "DejaVuSansMono",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        )
    )

    for spec in READERS:
        print(build_one(spec))


if __name__ == "__main__":
    main()
