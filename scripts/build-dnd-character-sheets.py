#!/usr/bin/env python3
"""Build the original TheHoboKingdom D&D character record PDFs."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


OUTPUT = Path("output/pdf")
PAGE_W, PAGE_H = A4
MARGIN = 34
INK = colors.HexColor("#171A1D")
MUTED = colors.HexColor("#5A6066")
GOLD = colors.HexColor("#B18434")
PALE = colors.HexColor("#F4F1E9")
LINE = colors.HexColor("#9EA3A8")


def line(c, x1, y1, x2, y2, width=0.55, colour=LINE):
    c.setStrokeColor(colour)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)


def label(c, text, x, y, size=6.5, colour=MUTED):
    c.setFillColor(colour)
    c.setFont("Helvetica-Bold", size)
    c.drawString(x, y, text.upper())


def value_line(c, text, x, y, width, height=29):
    c.setStrokeColor(LINE)
    c.setFillColor(colors.white)
    c.roundRect(x, y, width, height, 4, fill=1, stroke=1)
    label(c, text, x + 7, y + height - 10)


def section(c, title, x, y_top, width, height, lines=0):
    c.setStrokeColor(INK)
    c.setFillColor(colors.white)
    c.roundRect(x, y_top - height, width, height, 5, fill=1, stroke=1)
    c.setFillColor(INK)
    c.rect(x, y_top - 22, width, 22, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x + 8, y_top - 15, title.upper())
    if lines:
        available = height - 30
        spacing = available / lines
        for index in range(1, lines + 1):
            y = y_top - 24 - index * spacing
            line(c, x + 7, y, x + width - 7, y, 0.35, colors.HexColor("#C9CDD0"))


def page_header(c, title, subtitle, page_number):
    c.setFillColor(INK)
    c.rect(0, PAGE_H - 58, PAGE_W, 58, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(MARGIN, PAGE_H - 20, "THEHOBOKINGDOM TABLE RECORD")
    c.setFillColor(colors.white)
    c.setFont("Times-Bold", 19)
    c.drawString(MARGIN, PAGE_H - 42, title)
    c.setFont("Helvetica", 7.5)
    subtitle_width = stringWidth(subtitle, "Helvetica", 7.5)
    c.drawString(PAGE_W - MARGIN - subtitle_width, PAGE_H - 40, subtitle)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.5)
    c.drawRightString(PAGE_W - MARGIN, 18, f"Original 5e-compatible play aid | Page {page_number}")


def ability_box(c, name, x, y, width=82, height=62):
    c.setStrokeColor(INK)
    c.roundRect(x, y, width, height, 5, fill=0, stroke=1)
    label(c, name, x + 7, y + height - 11, 6.5, INK)
    label(c, "Score", x + 7, y + 8, 5.5)
    label(c, "Modifier", x + 37, y + 8, 5.5)
    line(c, x + 31, y + 5, x + 31, y + height - 18, 0.45)
    line(c, x + 7, y + 19, x + width - 7, y + 19, 0.45)


def build_full(path):
    c = canvas.Canvas(str(path), pagesize=A4, pageCompression=1)
    c.setTitle("TheHoboKingdom 5e-Compatible Character Record")
    c.setAuthor("TheHoboKingdom")

    page_header(c, "Character Record", "Core character and combat", 1)
    top = PAGE_H - 76
    value_line(c, "Character name", MARGIN, top - 32, 220, 32)
    value_line(c, "Player", MARGIN + 228, top - 32, 126, 32)
    value_line(c, "Campaign", MARGIN + 362, top - 32, 165, 32)
    top -= 40
    widths = [166, 55, 98, 102, 74]
    labels = ["Class and subclass", "Level", "Species or ancestry", "Background", "Experience"]
    x = MARGIN
    for item, width in zip(labels, widths):
        value_line(c, item, x, top - 30, width, 30)
        x += width + 8

    top -= 45
    for index, name in enumerate(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]):
        ability_box(c, name, MARGIN + index * 88, top - 62)

    top -= 77
    stat_w = (PAGE_W - 2 * MARGIN - 5 * 7) / 6
    for index, item in enumerate(["Proficiency", "Armour Class", "Initiative", "Speed", "Maximum HP", "Current / Temp HP"]):
        value_line(c, item, MARGIN + index * (stat_w + 7), top - 38, stat_w, 38)

    top -= 50
    left_w = 164
    middle_w = 184
    right_w = PAGE_W - 2 * MARGIN - left_w - middle_w - 16
    section(c, "Saving throws", MARGIN, top, left_w, 174, 6)
    save_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for idx, name in enumerate(save_names):
        y = top - 40 - idx * 22.7
        c.circle(MARGIN + 13, y + 2, 3.2, fill=0, stroke=1)
        label(c, name, MARGIN + 22, y, 6.2, INK)
    section(c, "Skills", MARGIN + left_w + 8, top, middle_w, 300, 18)
    skills = ["Acrobatics (DEX)", "Animal Handling (WIS)", "Arcana (INT)", "Athletics (STR)", "Deception (CHA)", "History (INT)", "Insight (WIS)", "Intimidation (CHA)", "Investigation (INT)", "Medicine (WIS)", "Nature (INT)", "Perception (WIS)", "Performance (CHA)", "Persuasion (CHA)", "Religion (INT)", "Sleight of Hand (DEX)", "Stealth (DEX)", "Survival (WIS)"]
    for idx, name in enumerate(skills):
        y = top - 37 - idx * 14.55
        c.circle(MARGIN + left_w + 20, y + 1, 2.7, fill=0, stroke=1)
        label(c, name, MARGIN + left_w + 28, y - 1, 5.4, INK)
    section(c, "Attacks, actions, and damage", MARGIN + left_w + middle_w + 16, top, right_w, 174, 6)
    section(c, "Conditions and current effects", MARGIN, top - 182, left_w, 118, 4)
    section(c, "Combat notes and reactions", MARGIN + left_w + middle_w + 16, top - 182, right_w, 118, 4)
    section(c, "Short rest, long rest, and resource tracking", MARGIN, top - 308, PAGE_W - 2 * MARGIN, 88, 3)
    c.showPage()

    page_header(c, "Character Record", "Features, equipment, and story", 2)
    top = PAGE_H - 76
    col_gap = 10
    col_w = (PAGE_W - 2 * MARGIN - col_gap) / 2
    section(c, "Features, traits, feats, and boons", MARGIN, top, col_w, 260, 11)
    section(c, "Equipment and treasure", MARGIN + col_w + col_gap, top, col_w, 260, 11)
    top -= 270
    section(c, "Proficiencies and languages", MARGIN, top, col_w, 126, 5)
    section(c, "Appearance, personality, ideals, bonds, and flaws", MARGIN + col_w + col_gap, top, col_w, 126, 5)
    top -= 136
    section(c, "Allies, organisations, and contacts", MARGIN, top, col_w, 126, 5)
    section(c, "Backstory and campaign notes", MARGIN + col_w + col_gap, top, col_w, 126, 5)
    top -= 136
    section(c, "Campaign changes, scars, titles, and unfinished business", MARGIN, top, PAGE_W - 2 * MARGIN, 126, 5)
    c.showPage()

    page_header(c, "Spellcasting Record", "Prepared spells and magical resources", 3)
    top = PAGE_H - 76
    widths = [145, 110, 75, 75, 90]
    labels = ["Spellcasting class", "Spellcasting ability", "Save DC", "Attack bonus", "Focus or source"]
    x = MARGIN
    for item, width in zip(labels, widths):
        value_line(c, item, x, top - 34, width, 34)
        x += width + 7
    top -= 46
    section(c, "Cantrips", MARGIN, top, PAGE_W - 2 * MARGIN, 94, 4)
    top -= 104
    col_gap = 10
    col_w = (PAGE_W - 2 * MARGIN - col_gap) / 2
    for idx, level in enumerate(range(1, 9)):
        x = MARGIN if idx % 2 == 0 else MARGIN + col_w + col_gap
        row = idx // 2
        y = top - row * 116
        title = f"Level {level} spells | Slots: ______  Used: ______"
        section(c, title, x, y, col_w, 106, 5)
    final_top = top - 4 * 116
    section(c, "Level 9 spells | Slots: ______  Used: ______", MARGIN, final_top, col_w, 106, 5)
    section(c, "Spell notes and resources", MARGIN + col_w + col_gap, final_top, col_w, 106, 5)
    c.save()


def build_quick(path):
    c = canvas.Canvas(str(path), pagesize=A4, pageCompression=1)
    c.setTitle("TheHoboKingdom 5e-Compatible Quick Character Sheet")
    c.setAuthor("TheHoboKingdom")
    page_header(c, "Quick Character Sheet", "One-shots, companions, and simple builds", 1)
    top = PAGE_H - 76
    value_line(c, "Character name", MARGIN, top - 34, 224, 34)
    value_line(c, "Class / role and level", MARGIN + 232, top - 34, 185, 34)
    value_line(c, "Player", MARGIN + 425, top - 34, 102, 34)
    top -= 48
    for index, name in enumerate(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]):
        ability_box(c, name, MARGIN + index * 88, top - 62)
    top -= 76
    stat_w = (PAGE_W - 2 * MARGIN - 6 * 6) / 7
    for index, item in enumerate(["Prof.", "AC", "Initiative", "Speed", "Max HP", "Current HP", "Hit dice"]):
        value_line(c, item, MARGIN + index * (stat_w + 6), top - 37, stat_w, 37)
    top -= 49
    col_gap = 10
    left_w = 180
    right_w = PAGE_W - 2 * MARGIN - left_w - col_gap
    section(c, "Saving throws and important skills", MARGIN, top, left_w, 190, 8)
    section(c, "Attacks, actions, reactions, and spells", MARGIN + left_w + col_gap, top, right_w, 190, 8)
    top -= 200
    section(c, "Features, traits, and special resources", MARGIN, top, PAGE_W - 2 * MARGIN, 120, 5)
    top -= 130
    section(c, "Equipment, treasure, and consumables", MARGIN, top, left_w + 55, 130, 6)
    section(c, "Conditions, notes, and current objective", MARGIN + left_w + 65, top, right_w - 55, 130, 6)
    top -= 140
    section(c, "Personality, background, allies, and campaign reminders", MARGIN, top, PAGE_W - 2 * MARGIN, 86, 3)
    c.save()


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    build_full(OUTPUT / "dnd-5e-character-record-sheet.pdf")
    build_quick(OUTPUT / "dnd-5e-quick-character-sheet.pdf")
    print("Built two original D&D character-sheet PDFs.")


if __name__ == "__main__":
    main()
