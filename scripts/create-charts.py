#!/usr/bin/env python3
"""Generate the chart images used in the deck.

Charts are hand-authored SVG so they stay minimal: no axes, no gridlines, no
chart titles, one accent colour per chart. The background is transparent so
each chart sits directly on the dark media card produced by build.cjs.

    python3 scripts/create-charts.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "slides" / "images" / "charts"

W, H = 520, 620
PAD = 28
INNER = W - PAD * 2

INK = "#e9eef7"
MUTED = "#8ea2ba"
FAINT = "#33465e"
TRACK = "#28394f"
SOURCE = "#5b6e88"

AMBER = "#f5a524"
ROSE = "#f7718a"
TEAL = "#2dd4bf"
BLUE = "#5aa9f8"
VIOLET = "#a78bfa"
GREEN = "#34d399"

FONT = "Avenir Next, Inter, Segoe UI, Helvetica, Arial, sans-serif"


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, value, size=12, fill=INK, weight=400, anchor="start", spacing=None, opacity=None):
    extra = f' letter-spacing="{spacing}"' if spacing else ""
    op = f' opacity="{opacity}"' if opacity else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}{op}>'
        f"{esc(value)}</text>"
    )


def rect(x, y, w, h, r, fill, opacity=None):
    if w <= 0:
        return ""
    op = f' opacity="{opacity}"' if opacity else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{r}" fill="{fill}"{op}/>'
    )


def line(x1, y1, x2, y2, stroke=TRACK, width=1):
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{width}"/>'
    )


def doc(body, source):
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
    ]
    parts.extend(body)
    if source:
        parts.append(text(PAD, H - 22, source, 9, SOURCE, 600, spacing="0.09em"))
    parts.append("</svg>")
    return "\n".join(parts)


def save(name, body, source=""):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.svg"
    path.write_text(doc(body, source), encoding="utf-8")
    print(f"wrote {path.name}")


def bar_list(rows, max_value, top=196, gap=100):
    """Label and value on one line, a single rounded track underneath."""
    body = []
    for i, (label, value, color, display) in enumerate(rows):
        y = top + i * gap
        body.append(text(PAD, y, label, 12.5, MUTED))
        body.append(text(W - PAD, y, display, 19, INK, 700, anchor="end"))
        body.append(rect(PAD, y + 16, INNER, 8, 4, TRACK))
        body.append(rect(PAD, y + 16, INNER * (value / max_value), 8, 4, color))
    return body, top + (len(rows) - 1) * gap + 44


# ── Slide 5: share of postings ────────────────────────────────────────────────


def chart_posting_mix():
    base = 470
    top = 150
    slot = INNER / 3
    bar_w = 92

    rows = [
        ("Senior", 69.3, FAINT, "69.3%"),
        ("Mid-level", 26.2, FAINT, "26.2%"),
        ("Entry-level", 4.5, AMBER, "4.5%"),
    ]
    scale = (base - top) / 70.0

    body = [line(PAD, base, W - PAD, base, TRACK, 1.5)]
    for i, (label, value, color, display) in enumerate(rows):
        h = max(value * scale, 7)
        x = PAD + slot * i + (slot - bar_w) / 2
        body.append(rect(x, base - h, bar_w, h, 6, color))
        body.append(
            text(
                x + bar_w / 2,
                base - h - 14,
                display,
                21 if i == 2 else 16,
                AMBER if i == 2 else INK,
                700,
                anchor="middle",
            )
        )
        body.append(text(x + bar_w / 2, base + 26, label, 12, MUTED, 400, anchor="middle"))

    body.append(
        text(PAD, 560, "1 in 22 postings is open to someone without experience", 11.5, AMBER, 600)
    )
    save("05-posting-mix", body, "INDEED HIRING LAB · Q1 2026 · US")


# ── Slide 6: two cohorts, opposite directions ─────────────────────────────────


def chart_cohort_split():
    cx = W / 2
    scale = 205 / 24.0

    body = [line(cx, 196, cx, 452, TRACK, 1.5)]

    body.append(text(cx, 150, "Aged 22–25", 12.5, MUTED, 400, anchor="middle"))
    body.append(text(PAD, 210, "−19%", 27, ROSE, 700))
    body.append(rect(cx - 19 * scale, 230, 19 * scale, 44, 8, ROSE))

    body.append(text(cx, 348, "Aged 35–49", 12.5, MUTED, 400, anchor="middle"))
    body.append(rect(cx, 366, 7.5 * scale, 44, 8, GREEN))
    body.append(text(cx + 7.5 * scale + 14, 398, "+7.5%", 27, GREEN, 700))

    body.append(text(PAD, 486, "Same occupations.", 15, INK, 700))
    body.append(text(PAD, 510, "Opposite outcomes.", 15, ROSE, 700))
    save("06-cohort-split", body, "STANFORD DIGITAL ECONOMY LAB · ADP PAYROLL DATA")


# ── Slide 8: fresher salary by track ─────────────────────────────────────────


def chart_vietnam():
    rows = [
        ("Embedded", 21.4, AMBER, "21.4"),
        ("Mobile", 14.2, AMBER, "14.2"),
        ("Back-end", 12.4, AMBER, "12.4"),
        ("Full-stack", 10.1, AMBER, "10.1"),
    ]
    body, bottom = bar_list(rows, 24.0, top=176, gap=90)
    body.append(line(PAD, bottom + 2, W - PAD, bottom + 2, TRACK, 1))
    for tick in (0, 10, 20):
        x = PAD + INNER * (tick / 24.0)
        body.append(text(x, bottom + 26, str(tick), 10, SOURCE, 400, anchor="middle"))
    body.append(text(PAD, bottom + 54, "Million VND per month", 11, MUTED))
    save("08-vietnam-market", body, "TALENTHERO · EMPLOYSOME · 2026")


# ── Slide 9: the funnel ───────────────────────────────────────────────────────


def chart_funnel():
    stages = [
        ("291", "applications", 1.0, AMBER),
        ("12", "reach an interview", 0.62, VIOLET),
        ("1", "gets the offer", 0.30, TEAL),
    ]
    body = []
    for i, (big, label, ratio, color) in enumerate(stages):
        w = INNER * ratio
        x = (W - w) / 2
        y = 154 + i * 126
        body.append(rect(x, y, w, 64, 14, color, 0.92))
        body.append(text(W / 2, y + 31, big, 26, "#0f172a", 700, anchor="middle"))
        body.append(text(W / 2, y + 51, label, 10.5, "#0f172a", 500, anchor="middle"))
    body.append(text(PAD, 556, "4.2% reach an interview · 0.34% reach an offer", 11.5, MUTED))
    save("09-funnel", body, "ASHBY 2026 · 109M APPLICATIONS")


# ── Slide 14: AI in the interview loop ───────────────────────────────────────


def chart_ai_interview():
    rows = [
        ("Recruiters suspect deception", 91, ROSE, "91%"),
        ("Candidates seen using AI", 35, ROSE, "35%"),
        ("Roles with an in-person round", 30, BLUE, "30%"),
        ("Employers allowing AI in tests", 25, TEAL, "25%"),
    ]
    body, bottom = bar_list(rows, 100, top=182, gap=88)
    body.append(text(PAD, bottom + 30, "Detection is unreliable.", 14, INK, 700))
    body.append(text(PAD, bottom + 54, "The follow-up question is not.", 14, TEAL, 700))
    save("14-ai-interview", body, "GREENHOUSE 2026 · GARTNER · ROBERT HALF")


# ── Slide 15: false positives ────────────────────────────────────────────────


def chart_detector():
    body = []
    body.append(text(PAD, 214, "61%", 64, ROSE, 700, spacing="-0.03em"))
    body.append(text(PAD, 250, "of human-written English from non-native", 12.5, INK))
    body.append(text(PAD, 270, "speakers is flagged as machine-generated", 12.5, INK))

    y = 330
    body.append(rect(PAD, y, INNER, 22, 11, TRACK))
    body.append(rect(PAD, y, INNER * 0.61, 22, 11, ROSE))
    body.append(text(PAD, y + 52, "wrongly flagged", 10.5, ROSE, 500))
    body.append(text(W - PAD, y + 52, "handled correctly", 10.5, TEAL, 500, anchor="end"))

    body.append(text(PAD, 456, "The tool is guessing.", 13, INK, 600))
    body.append(text(PAD, 478, "Your explanation is not.", 13, TEAL, 600))
    save("15-detector-bias", body, "STANFORD · SEVEN LEADING AI-TEXT DETECTORS")


# ── Slide 16: internship conversion ──────────────────────────────────────────


def chart_conversion():
    cx, cy, r = W / 2, 292, 104
    stroke = 20
    circumference = 2 * 3.14159265 * r
    dash = circumference * 0.631

    body = [
        f'<circle cx="{cx:.1f}" cy="{cy}" r="{r}" fill="none" stroke="{TRACK}" stroke-width="{stroke}"/>',
        (
            f'<circle cx="{cx:.1f}" cy="{cy}" r="{r}" fill="none" stroke="{TEAL}" '
            f'stroke-width="{stroke}" stroke-linecap="round" '
            f'stroke-dasharray="{dash:.1f} {circumference:.1f}" '
            f'transform="rotate(-90 {cx:.1f} {cy})"/>'
        ),
        text(cx, cy - 2, "63.1%", 44, INK, 700, anchor="middle", spacing="-0.02em"),
        text(cx, cy + 30, "convert to full-time", 11.5, MUTED, 400, anchor="middle"),
        text(PAD, 498, "The internship is the highest-leverage", 12.5, INK),
        text(PAD, 520, "move available to a student.", 12.5, INK),
    ]
    save("16-intern-conversion", body, "NACE 2026 INTERNSHIP & CO-OP REPORT")


# ── Slide 17: what fills the gap when GPA drops ──────────────────────────────


def chart_nace_factors():
    rows = [
        ("Academic major", 94, VIOLET, "94%"),
        ("Industry experience", 81, VIOLET, "81%"),
        ("Industry internship", 79, VIOLET, "79%"),
        ("Internship here", 74, VIOLET, "74%"),
    ]
    body, bottom = bar_list(rows, 100, top=176, gap=84)
    body.append(line(PAD, bottom + 8, W - PAD, bottom + 8, TRACK, 1))
    body.append(text(PAD, bottom + 54, "42%", 31, AMBER, 700))
    body.append(text(PAD + 92, bottom + 50, "still screen GPA", 11.5, MUTED))
    body.append(text(PAD + 92, bottom + 68, "down from 73% in 2019", 11.5, MUTED))
    save("17-nace-factors", body, "NACE 2026 · EMPLOYERS WHO SKIP GPA")


# ── Slide 20: the 12-week plan ───────────────────────────────────────────────


def chart_sprint():
    phases = [
        ("Build", "W1–4", 0.0, AMBER, "fundamentals + one project"),
        ("Package", "W5–8", 4 / 12, VIOLET, "CV per role + GitHub profile"),
        ("Apply", "W9–12", 8 / 12, TEAL, "10 applications a week + 2 mocks"),
    ]
    body = []
    rows = [176, 306, 436]
    bar_h = 12

    for (name, weeks, start, color, detail), y in zip(phases, rows):
        body.append(text(PAD, y - 18, name, 14, INK, 700))
        body.append(text(W - PAD, y - 18, weeks, 11, MUTED, 500, anchor="end"))
        body.append(rect(PAD, y, INNER, bar_h, 6, TRACK))
        body.append(rect(PAD + INNER * start, y, INNER / 3 - 5, bar_h, 6, color))
        body.append(text(PAD, y + 36, detail, 11, MUTED))

    body.append(line(PAD, 512, W - PAD, 512, TRACK, 1))
    for w in (0, 4, 8, 12):
        x = PAD + INNER * (w / 12)
        anchor = "start" if w == 0 else ("end" if w == 12 else "middle")
        body.append(text(x, 536, f"week {w}" if w else "start", 9.5, SOURCE, 400, anchor=anchor))

    save("20-sprint-plan", body, "A PLAN SMALL ENOUGH TO ACTUALLY START")


if __name__ == "__main__":
    chart_posting_mix()
    chart_cohort_split()
    chart_vietnam()
    chart_funnel()
    chart_ai_interview()
    chart_detector()
    chart_conversion()
    chart_nace_factors()
    chart_sprint()
