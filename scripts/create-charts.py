#!/usr/bin/env python3
"""Generate the chart images used in the deck, one set per language.

Charts are hand-authored SVG so they stay minimal: no axes, no gridlines, no
chart titles, one accent colour per chart. The background is transparent so
each chart sits directly on the dark media card produced by build.cjs.

Output:
    slides/images/charts/en/*.svg
    slides/images/charts/vi/*.svg

    python3 scripts/create-charts.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "slides" / "images" / "charts"

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

STRINGS = {
    "en": {
        "decimal": ".",
        "senior": "Senior",
        "mid": "Mid-level",
        "entry": "Entry-level",
        "posting_callout": "1 in 22 postings is open to someone without experience",
        "src_postings": "INDEED HIRING LAB · Q1 2026 · US",
        "age_young": "Aged 22–25",
        "age_senior": "Aged 35–49",
        "same_occupations": "Same occupations.",
        "opposite_outcomes": "Opposite outcomes.",
        "src_cohort": "STANFORD DIGITAL ECONOMY LAB · ADP PAYROLL DATA",
        "embedded": "Embedded",
        "mobile": "Mobile",
        "backend": "Back-end",
        "fullstack": "Full-stack",
        "per_month": "Million VND per month",
        "src_salary": "TALENTHERO · EMPLOYSOME · 2026",
        "applications": "applications",
        "reach_interview": "reach an interview",
        "gets_offer": "gets the offer",
        "funnel_caption": "4.2% reach an interview · 0.34% reach an offer",
        "src_funnel": "ASHBY 2026 · 109M APPLICATIONS",
        "ai_suspect": "Recruiters suspect deception",
        "ai_candidates": "Candidates seen using AI",
        "ai_inperson": "Roles with an in-person round",
        "ai_allow": "Employers allowing AI in tests",
        "detection_bad": "Detection is unreliable.",
        "detection_good": "The follow-up question is not.",
        "src_ai": "GREENHOUSE 2026 · GARTNER · ROBERT HALF",
        "detector_l1": "of human-written English from non-native",
        "detector_l2": "speakers is flagged as machine-generated",
        "detector_wrong": "wrongly flagged",
        "detector_right": "handled correctly",
        "detector_tool": "The tool is guessing.",
        "detector_you": "Your explanation is not.",
        "src_detector": "STANFORD · SEVEN LEADING AI-TEXT DETECTORS",
        "convert": "convert to full-time",
        "intern_l1": "The internship is the highest-leverage",
        "intern_l2": "move available to a student.",
        "src_intern": "NACE 2026 INTERNSHIP & CO-OP REPORT",
        "major": "Academic major",
        "experience": "Industry experience",
        "internship": "Industry internship",
        "internship_here": "Internship here",
        "still_gpa": "still screen GPA",
        "gpa_drop": "down from 73% in 2019",
        "src_nace": "NACE 2026 · EMPLOYERS WHO SKIP GPA",
        "build": "Build",
        "package": "Package",
        "apply": "Apply",
        "build_detail": "fundamentals + one project",
        "package_detail": "CV per role + GitHub profile",
        "apply_detail": "10 applications a week + 2 mocks",
        "week": "week {}",
        "start": "start",
        "src_sprint": "A PLAN SMALL ENOUGH TO ACTUALLY START",
    },
    "vi": {
        "decimal": ",",
        "senior": "Senior",
        "mid": "Mid-level",
        "entry": "Entry-level",
        "posting_callout": "1 trong 22 tin tuyển dành cho người chưa có kinh nghiệm",
        "src_postings": "INDEED HIRING LAB · QUÝ 1/2026 · MỸ",
        "age_young": "22–25 tuổi",
        "age_senior": "35–49 tuổi",
        "same_occupations": "Cùng một nghề.",
        "opposite_outcomes": "Kết quả trái ngược.",
        "src_cohort": "STANFORD DIGITAL ECONOMY LAB · DỮ LIỆU BẢNG LƯƠNG ADP",
        "embedded": "Nhúng",
        "mobile": "Mobile",
        "backend": "Back-end",
        "fullstack": "Full-stack",
        "per_month": "Triệu VND mỗi tháng",
        "src_salary": "TALENTHERO · EMPLOYSOME · 2026",
        "applications": "hồ sơ",
        "reach_interview": "được gọi phỏng vấn",
        "gets_offer": "được nhận",
        "funnel_caption": "4,2% được gọi phỏng vấn · 0,34% được nhận",
        "src_funnel": "ASHBY 2026 · 109 TRIỆU HỒ SƠ",
        "ai_suspect": "Recruiter nghi ngờ gian dối",
        "ai_candidates": "Ứng viên dùng AI",
        "ai_inperson": "Vị trí có vòng trực tiếp",
        "ai_allow": "Cho phép AI khi thi kỹ thuật",
        "detection_bad": "Phát hiện không đáng tin.",
        "detection_good": "Câu hỏi đào sâu thì có.",
        "src_ai": "GREENHOUSE 2026 · GARTNER · ROBERT HALF",
        "detector_l1": "văn bản tiếng Anh của người không bản ngữ",
        "detector_l2": "bị gắn nhãn là do máy tạo ra",
        "detector_wrong": "gắn nhãn sai",
        "detector_right": "xử lý đúng",
        "detector_tool": "Công cụ đang đoán.",
        "detector_you": "Lời giải thích của bạn thì không.",
        "src_detector": "STANFORD · BẢY CÔNG CỤ PHÁT HIỆN HÀNG ĐẦU",
        "convert": "được chuyển chính thức",
        "intern_l1": "Thực tập là nước đi đòn bẩy",
        "intern_l2": "cao nhất với sinh viên.",
        "src_intern": "NACE 2026 · BÁO CÁO THỰC TẬP",
        "major": "Ngành học",
        "experience": "Kinh nghiệm trong ngành",
        "internship": "Thực tập trong ngành",
        "internship_here": "Thực tập tại đây",
        "still_gpa": "vẫn lọc theo GPA",
        "gpa_drop": "giảm từ 73% năm 2019",
        "src_nace": "NACE 2026 · DOANH NGHIỆP KHÔNG LỌC GPA",
        "build": "Xây",
        "package": "Đóng gói",
        "apply": "Nộp",
        "build_detail": "nền tảng + một dự án",
        "package_detail": "CV theo vị trí + hồ sơ GitHub",
        "apply_detail": "10 hồ sơ mỗi tuần + 2 buổi thử",
        "week": "tuần {}",
        "start": "bắt đầu",
        "src_sprint": "KẾ HOẠCH ĐỦ NHỎ ĐỂ THỰC SỰ BẮT ĐẦU",
    },
}


def esc(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, value, size=12, fill=INK, weight=400, anchor="start", spacing=None):
    extra = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>'
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


def make_num(t):
    sep = t["decimal"]

    def num(value, decimals=1):
        return f"{value:.{decimals}f}".replace(".", sep)

    return num


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


def save(lang, name, body, source=""):
    folder = OUT / lang
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.svg"
    path.write_text(doc(body, source), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def bar_list(rows, max_value, top=196, gap=100):
    body = []
    for i, (label, value, color, display) in enumerate(rows):
        y = top + i * gap
        body.append(text(PAD, y, label, 12.5, MUTED))
        body.append(text(W - PAD, y, display, 19, INK, 700, anchor="end"))
        body.append(rect(PAD, y + 16, INNER, 8, 4, TRACK))
        body.append(rect(PAD, y + 16, INNER * (value / max_value), 8, 4, color))
    return body, top + (len(rows) - 1) * gap + 44


# ── Slide 5: share of postings ────────────────────────────────────────────────


def chart_posting_mix(lang, t, num):
    base, top = 470, 150
    slot = INNER / 3
    bar_w = 92
    rows = [
        (t["senior"], 69.3, FAINT, num(69.3) + "%"),
        (t["mid"], 26.2, FAINT, num(26.2) + "%"),
        (t["entry"], 4.5, AMBER, num(4.5) + "%"),
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

    body.append(text(PAD, 556, t["posting_callout"], 11.5, AMBER, 600))
    save(lang, "05-posting-mix", body, t["src_postings"])


# ── Slide 6: two cohorts, opposite directions ─────────────────────────────────


def chart_cohort_split(lang, t, num):
    cx = W / 2
    scale = 160 / 24.0

    body = [line(cx, 196, cx, 452, TRACK, 1.5)]

    body.append(text(cx, 150, t["age_young"], 12.5, MUTED, 400, anchor="middle"))
    body.append(rect(cx - 19 * scale, 230, 19 * scale, 44, 8, ROSE))
    body.append(text(cx - 19 * scale - 12, 252, "−" + num(19, 0) + "%", 27, ROSE, 700, anchor="end"))

    body.append(text(cx, 348, t["age_senior"], 12.5, MUTED, 400, anchor="middle"))
    body.append(rect(cx, 366, 7.5 * scale, 44, 8, GREEN))
    body.append(text(cx + 7.5 * scale + 12, 388, "+" + num(7.5) + "%", 27, GREEN, 700))

    body.append(text(PAD, 486, t["same_occupations"], 15, INK, 700))
    body.append(text(PAD, 510, t["opposite_outcomes"], 15, ROSE, 700))
    save(lang, "06-cohort-split", body, t["src_cohort"])


# ── Slide 8: fresher salary by track ─────────────────────────────────────────


def chart_vietnam(lang, t, num):
    rows = [
        (t["embedded"], 21.4, AMBER, num(21.4)),
        (t["mobile"], 14.2, AMBER, num(14.2)),
        (t["backend"], 12.4, AMBER, num(12.4)),
        (t["fullstack"], 10.1, AMBER, num(10.1)),
    ]
    body, bottom = bar_list(rows, 24.0, top=176, gap=90)
    body.append(line(PAD, bottom + 2, W - PAD, bottom + 2, TRACK, 1))
    for tick in (0, 10, 20):
        x = PAD + INNER * (tick / 24.0)
        body.append(text(x, bottom + 26, str(tick), 10, SOURCE, 400, anchor="middle"))
    body.append(text(PAD, bottom + 54, t["per_month"], 11, MUTED))
    save(lang, "08-vietnam-market", body, t["src_salary"])


# ── Slide 9: the funnel ───────────────────────────────────────────────────────


def chart_funnel(lang, t, num):
    stages = [
        ("291", t["applications"], 1.0, AMBER),
        ("12", t["reach_interview"], 0.62, VIOLET),
        ("1", t["gets_offer"], 0.30, TEAL),
    ]
    body = []
    for i, (big, label, ratio, color) in enumerate(stages):
        w = INNER * ratio
        x = (W - w) / 2
        y = 154 + i * 126
        body.append(rect(x, y, w, 64, 14, color, 0.92))
        body.append(text(W / 2, y + 31, big, 26, "#0f172a", 700, anchor="middle"))
        body.append(text(W / 2, y + 51, label, 10.5, "#0f172a", 500, anchor="middle"))
    body.append(text(PAD, 556, t["funnel_caption"], 11.5, MUTED))
    save(lang, "09-funnel", body, t["src_funnel"])


# ── Slide 14: AI in the interview loop ───────────────────────────────────────


def chart_ai_interview(lang, t, num):
    rows = [
        (t["ai_suspect"], 91, ROSE, num(91, 0) + "%"),
        (t["ai_candidates"], 35, ROSE, num(35, 0) + "%"),
        (t["ai_inperson"], 30, BLUE, num(30, 0) + "%"),
        (t["ai_allow"], 25, TEAL, num(25, 0) + "%"),
    ]
    body, bottom = bar_list(rows, 100, top=182, gap=88)
    body.append(text(PAD, bottom + 30, t["detection_bad"], 14, INK, 700))
    body.append(text(PAD, bottom + 54, t["detection_good"], 14, TEAL, 700))
    save(lang, "14-ai-interview", body, t["src_ai"])


# ── Slide 15: false positives ────────────────────────────────────────────────


def chart_detector(lang, t, num):
    body = [
        text(PAD, 214, "61%", 64, ROSE, 700, spacing="-0.03em"),
        text(PAD, 250, t["detector_l1"], 12.5, INK),
        text(PAD, 270, t["detector_l2"], 12.5, INK),
    ]
    y = 330
    body.append(rect(PAD, y, INNER, 22, 11, TRACK))
    body.append(rect(PAD, y, INNER * 0.61, 22, 11, ROSE))
    body.append(text(PAD, y + 52, t["detector_wrong"], 10.5, ROSE, 500))
    body.append(text(W - PAD, y + 52, t["detector_right"], 10.5, TEAL, 500, anchor="end"))
    body.append(text(PAD, 456, t["detector_tool"], 13, INK, 600))
    body.append(text(PAD, 478, t["detector_you"], 13, TEAL, 600))
    save(lang, "15-detector-bias", body, t["src_detector"])


# ── Slide 16: internship conversion ──────────────────────────────────────────


def chart_conversion(lang, t, num):
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
        text(cx, cy - 2, num(63.1) + "%", 44, INK, 700, anchor="middle", spacing="-0.02em"),
        text(cx, cy + 30, t["convert"], 11.5, MUTED, 400, anchor="middle"),
        text(PAD, 498, t["intern_l1"], 12.5, INK),
        text(PAD, 520, t["intern_l2"], 12.5, INK),
    ]
    save(lang, "16-intern-conversion", body, t["src_intern"])


# ── Slide 17: what fills the gap when GPA drops ──────────────────────────────


def chart_nace_factors(lang, t, num):
    rows = [
        (t["major"], 94, VIOLET, num(94, 0) + "%"),
        (t["experience"], 81, VIOLET, num(81, 0) + "%"),
        (t["internship"], 79, VIOLET, num(79, 0) + "%"),
        (t["internship_here"], 74, VIOLET, num(74, 0) + "%"),
    ]
    body, bottom = bar_list(rows, 100, top=176, gap=84)
    body.append(line(PAD, bottom + 8, W - PAD, bottom + 8, TRACK, 1))
    body.append(text(PAD, bottom + 54, num(42, 0) + "%", 31, AMBER, 700))
    body.append(text(PAD + 92, bottom + 50, t["still_gpa"], 11.5, MUTED))
    body.append(text(PAD + 92, bottom + 68, t["gpa_drop"], 11.5, MUTED))
    save(lang, "17-nace-factors", body, t["src_nace"])


# ── Slide 20: the 12-week plan ───────────────────────────────────────────────


def chart_sprint(lang, t, num):
    phases = [
        (t["build"], t["week"].format("1–4"), 0.0, AMBER, t["build_detail"]),
        (t["package"], t["week"].format("5–8"), 4 / 12, VIOLET, t["package_detail"]),
        (t["apply"], t["week"].format("9–12"), 8 / 12, TEAL, t["apply_detail"]),
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
        label = t["start"] if w == 0 else t["week"].format(w)
        body.append(text(x, 536, label, 9.5, SOURCE, 400, anchor=anchor))

    save(lang, "20-sprint-plan", body, t["src_sprint"])


BUILDERS = [
    chart_posting_mix,
    chart_cohort_split,
    chart_vietnam,
    chart_funnel,
    chart_ai_interview,
    chart_detector,
    chart_conversion,
    chart_nace_factors,
    chart_sprint,
]


if __name__ == "__main__":
    for lang, strings in STRINGS.items():
        for builder in BUILDERS:
            builder(lang, strings, make_num(strings))
