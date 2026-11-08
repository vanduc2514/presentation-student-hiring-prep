# Student Hiring Preparation in the AI Era

[![vi](https://img.shields.io/badge/lang-vi-yellow.svg)](README.vi-VN.md)

A 90-minute campus talkshow on what Fresher and Intern hiring actually tests — and how to prepare from year 3 to first offer.

Built with [markpress](https://github.com/davidecaminati/markpress) and impress.js.

**Live deck:** <https://vanduc2514.github.io/presentation-student-hiring-prep/> ([Tiếng Việt](https://vanduc2514.github.io/presentation-student-hiring-prep/index.vi.html))

## Background

The IT job market is more competitive and companies are stricter when hiring Freshers and Interns. Knowing how to code and having a clean CV is no longer enough to get an interview.

This talk takes the employer's side of the table: what a hiring panel actually writes down, where candidates are rejected, how AI changed the interview loop, and what a student can do in the next 12 weeks.

**Audience:** IT students in year 3–4, and recent graduates already applying.

**Four sections:**

1. The Fresher/Intern hiring picture in the AI era
2. The hiring process and the criteria candidates are judged on
3. A preparation roadmap for year 3, year 4, and new graduates
4. Live Q&A

## Build

```sh
npm install
npm run build      # → output/index.html and output/index.vi.html
npm run preview    # open the English deck in the browser
```

Requires Node.js 20. If you use [mise](https://mise.jdx.dev/), run `mise install` first.

### Regenerating the charts

Nine slides use a chart on the right-hand card. Each language has its own chart set, so labels and decimal separators match the deck:

| Path | Language |
|---|---|
| `slides/images/charts/en/` | English labels, `69.3%` |
| `slides/images/charts/vi/` | Vietnamese labels, `69,3%` |

They are hand-authored SVG, not screenshots, so they stay sharp at any projection size:

```sh
python3 scripts/create-charts.py
```

The script writes both sets. Edit the chart source and the `STRINGS` table in that file, never the `.svg` files.

### Regenerating the photos

Five slides use a photograph, full-bleed in the right-hand card:

```sh
python3 scripts/prepare-photos.py
```

The script downloads each original, centre-crops it to the card's aspect ratio, and applies a warm muted grade so photos share the palette of the paper cards. All sources are **CC0 1.0** and recorded, with creators and source pages, in [`slides/images/photos/CREDITS.md`](slides/images/photos/CREDITS.md).

| Output | Language |
|---|---|
| `output/index.html` | English |
| `output/index.vi.html` | Vietnamese |
| `output/remote.html` | Phone remote with live speaker notes |

## Contents

| Path | Purpose |
|---|---|
| `slides/presentation.en.md` | English slide source |
| `slides/presentation.vi.md` | Vietnamese slide source |
| `slides/images/` | QR codes and icons |
| `slides/images/charts/` | Generated chart SVGs, one set per language |
| `slides/images/photos/` | Processed photographs plus `CREDITS.md` |
| `scripts/create-charts.py` | Chart generator |
| `scripts/prepare-photos.py` | Photo downloader and grader |
| `research/findings.md` | Sourced statistics behind every claim in the deck |
| `research/idea.md` | Talk concept, thesis, and structure |
| `build.cjs` | Build script and theming |
| `.agents/skills/` | Skills for writing and styling slides |

## Outline

| # | Slide | Section |
|---|---|---|
| 1–3 | Title, the question, agenda | Hook |
| 4 | Three things you have been told | Hook |
| 5–8 | Entry-level share, the narrowing ladder, the new bar, Vietnam | The picture |
| 9–10 | The funnel, CV as a ranking problem | Process |
| 11–13 | The eight boxes, knockout criteria, red flags | Criteria |
| 14–15 | How AI is tested, unreliable detection | Criteria |
| 16–18 | Year 3, year 4, new grad | Roadmap |
| 19–20 | The evidence stack, the next 12 weeks | Roadmap |
| 21 | Q&A | Close |

## Speaker notes

Notes live in HTML comments under each slide. Personal stories are marked `[STORY: ...]` and should be replaced with real cases before delivering the talk.

## Sources

Every number on a slide is traceable to `research/findings.md`, which also lists the widely repeated statistics that were deliberately excluded because they have no verifiable primary source.

## Deploy

The deck is published to GitHub Pages at <https://vanduc2514.github.io/presentation-student-hiring-prep/>. Every push to `main` triggers `.github/workflows/deploy-pages.yml`, which builds both language versions, generates the PDFs, and deploys `output/`. The workflow can also be run manually from the Actions tab.

To preview locally:

```sh
npm run build && npm run preview
```

## Writing slides

Slides are separated by `------` (six dashes). See [`.agents/skills/markpress-content/SKILL.md`](.agents/skills/markpress-content/SKILL.md) for the authoring guide, and [`.agents/skills/markpress-styling/SKILL.md`](.agents/skills/markpress-styling/SKILL.md) for theming.
