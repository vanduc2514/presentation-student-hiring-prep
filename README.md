# Student Hiring Preparation in the AI Era

[![vi](https://img.shields.io/badge/lang-vi-yellow.svg)](README.vi-VN.md)

A 90-minute campus talkshow on what Fresher and Intern hiring actually tests — and how to prepare from year 3 to first offer.

Built with [markpress](https://github.com/davidecaminati/markpress) and impress.js.

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

The included workflow (`deploy-pages.yml`) builds and deploys on every push to `main`.

Enable GitHub Pages: **Settings** → **Pages** → **Source**: `GitHub Actions`.

## Writing slides

Slides are separated by `------` (six dashes). See [`.agents/skills/markpress-content/SKILL.md`](.agents/skills/markpress-content/SKILL.md) for the authoring guide, and [`.agents/skills/markpress-styling/SKILL.md`](.agents/skills/markpress-styling/SKILL.md) for theming.
