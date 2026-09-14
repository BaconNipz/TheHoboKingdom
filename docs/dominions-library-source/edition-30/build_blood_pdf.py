#!/usr/bin/env python3
"""Build the standalone Blood Magic research paper PDF."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
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

from build_pdf import GOLD, INK, LINE, MUTED, NAVY, NAVY_2, PAGE_H, PAGE_W, STYLES
from build_pdf import markdown_to_story


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "23-blood-magic-research-paper.md"
OUTPUT = ROOT.parent / "output" / "pdf" / "dominions-6-blood-magic-research-paper.pdf"


class BloodPaperDocTemplate(BaseDocTemplate):
    """Document template with bookmarks and a generated contents page."""

    def __init__(self, filename: str):
        super().__init__(
            filename,
            pagesize=A4,
            rightMargin=18 * mm,
            leftMargin=18 * mm,
            topMargin=20 * mm,
            bottomMargin=20 * mm,
            title="Blood Magic in Dominions 6",
            author="TheHoboKingdom",
            subject=(
                "A systems study of Blood hunting, logistics, research, Sabbaths, "
                "rituals, blessings, sacrifice, globals, counterplay, and the frozen "
                "Dominions Enhanced and Divinitus mod stack"
            ),
            creator="TheHoboKingdom",
        )
        self.heading_counter = 0

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name not in {"ArchiveH1", "ArchiveH2", "ArchiveH3"}:
            return
        level = {"ArchiveH1": 0, "ArchiveH2": 1, "ArchiveH3": 2}[style_name]
        heading = flowable.getPlainText()
        key = getattr(flowable, "_blood_bookmark_key", None)
        if key is None:
            key = f"blood-heading-{self.heading_counter}"
            flowable._blood_bookmark_key = key
            self.heading_counter += 1
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(heading, key, level=level, closed=level > 0)
        if level <= 1:
            self.notify("TOCEntry", (level, heading, self.page, key))


def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#28131B"))
    canvas.rect(0, 0, PAGE_W, 35 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
    canvas.rect(18 * mm, PAGE_H - 59 * mm, 34 * mm, 1.5 * mm, fill=1, stroke=0)
    canvas.setFont("DejaVuSans", 7.5)
    canvas.setFillColor(colors.HexColor("#AEBBC9"))
    canvas.drawString(18 * mm, 17 * mm, "THEHOBOKINGDOM")
    canvas.setFillColor(GOLD)
    canvas.drawRightString(PAGE_W - 18 * mm, 17 * mm, "RESEARCH PAPER · FIRST EDITION")
    canvas.restoreState()


def draw_body(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.75)
    canvas.line(18 * mm, PAGE_H - 13 * mm, PAGE_W - 18 * mm, PAGE_H - 13 * mm)
    canvas.setFont("DejaVuSans-Bold", 7.2)
    canvas.setFillColor(NAVY)
    canvas.drawString(18 * mm, PAGE_H - 10 * mm, "BLOOD MAGIC IN DOMINIONS 6")
    canvas.setFont("DejaVuSans", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 10 * mm, "RULES BASELINE 6.35")
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.45)
    canvas.line(18 * mm, 13 * mm, PAGE_W - 18 * mm, 13 * mm)
    canvas.setFont("DejaVuSans", 7.1)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 8.5 * mm, "TheHoboKingdom | 3 August 2026")
    canvas.drawRightString(PAGE_W - 18 * mm, 8.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def register_fonts():
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


def tune_paper_styles():
    """Use slightly tighter long-form spacing without reducing readability."""
    STYLES["body"].fontSize = 9.2
    STYLES["body"].leading = 13.7
    STYLES["body"].spaceAfter = 6.5
    STYLES["bullet"].fontSize = 9.0
    STYLES["bullet"].leading = 13.2
    STYLES["table_cell"].fontSize = 7.3
    STYLES["table_cell"].leading = 9.4
    STYLES["h2"].spaceBefore = 14


def build():
    register_fonts()
    tune_paper_styles()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BloodPaperDocTemplate(str(OUTPUT))
    cover_frame = Frame(
        18 * mm,
        35 * mm,
        PAGE_W - 36 * mm,
        PAGE_H - 57 * mm,
        id="cover_frame",
        showBoundary=0,
    )
    body_frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="body_frame",
        showBoundary=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="Cover", frames=[cover_frame], onPage=draw_cover),
            PageTemplate(id="Body", frames=[body_frame], onPage=draw_body),
        ]
    )

    story = [
        Spacer(1, 36 * mm),
        Paragraph("DOMINIONS 6 SYSTEMS STUDY", STYLES["cover_kicker"]),
        Paragraph("Blood Magic<br/>in Dominions 6", STYLES["cover_title"]),
        Paragraph(
            "Extraction, logistics, ritual power, and strategic conversion",
            STYLES["cover_subtitle"],
        ),
        Spacer(1, 7 * mm),
        HRFlowable(width=44 * mm, thickness=1.4, color=GOLD, hAlign="LEFT"),
        Spacer(1, 7 * mm),
        Paragraph(
            "<b>First edition</b><br/>3 August 2026<br/><br/>"
            "Vanilla rules baseline: Dominions 6.35<br/>"
            "Optional appendix: Dominions Enhanced 2.16 + Divinitus 1.15.3 DE",
            STYLES["cover_note"],
        ),
        NextPageTemplate("Body"),
        PageBreak(),
        Paragraph("Contents", STYLES["toc_title"]),
        Paragraph(
            "A standalone reference to Blood hunting, the slave economy, hosting "
            "timing, research, battlefield casting, Sabbaths, summons, sacrifice, "
            "blessings, path access, global enchantments, counterplay, operations, "
            "and the frozen mod stack.",
            STYLES["body"],
        ),
        Spacer(1, 5),
    ]

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "BloodTOCLevel1",
            fontName="DejaVuSans-Bold",
            fontSize=10.0,
            leading=14.5,
            leftIndent=0,
            firstLineIndent=0,
            textColor=NAVY,
            spaceBefore=4,
        ),
        ParagraphStyle(
            "BloodTOCLevel2",
            fontName="DejaVuSans",
            fontSize=8.3,
            leading=11.5,
            leftIndent=13,
            firstLineIndent=0,
            textColor=INK,
        ),
    ]
    story.extend([toc, PageBreak()])
    story.extend(markdown_to_story(SOURCE, doc.width))

    doc.multiBuild(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
