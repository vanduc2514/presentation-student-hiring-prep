# Research Findings — Fresher/Intern Hiring in the AI Era

Collected 2026-11-08. Every number below is tagged with a confidence level:

- **[A]** primary data or named study with methodology
- **[B]** credible vendor or industry survey, sample disclosed
- **[C]** secondary reporting / plausible but unverified — do not put on a slide without hedging

---

## 1. The market: what actually changed

### Entry-level demand collapsed relative to other levels [A]

- **Stanford Digital Economy Lab, "Canaries in the Coal Mine?"** (Brynjolfsson, Chandar, Chen), ADP payroll records covering 3.5–5M US workers monthly:
  - Workers aged 22–25 in the most AI-exposed occupations saw a **16% relative employment decline** vs least-exposed occupations (Nov 2025 version); revised to **19%** using data through June 2026.
  - In absolute terms, employment for this cohort is roughly **20% below its peak**.
  - Workers aged **35–49 in the same occupations grew 6–9%**.
- **Indeed Hiring Lab**:
  - US tech postings **36% below Feb-2020** levels (Jul 2025); software engineers **49% below**.
  - Software-development posting index: **61.1 low (May 2025) → 78.3 (Oct 2026)**, still ~22% below pre-pandemic.
  - **Q1 2026: only 4.5%** of US software-dev postings were entry-level; **senior 69.3%**, mid-level ~26%.
  - **Senior postings +13.5%** since Jan 2025; **entry-level −6.3%**, mid-level −6.7%.
  - **71%** of the May-2025→May-2026 rebound came from senior roles; **37%** of new postings mention AI in the title.
- **Handshake**: by Aug 2025, postings down **>16% YoY** while **applications per job rose 26%**; spring 2026 postings still below 2020 levels.
- **NY Fed**: CS graduate unemployment **6.1%**, computer engineering **7.5%**; overall 22–27 cohort **7.4%** (≈2× national average); recent-grad underemployment **42.5%** in Q4 2025 — highest since 2020.
- **BLS 2025–2035**: software developers projected **+10%** (~174,700 jobs) — still "much faster than average", but revised down from +15% the previous cycle.

### The belief gap [B]

- **SHRM 2024 survey**: **70%** of hiring managers say AI can already do the work of interns; **57%** trust AI output more than the work of interns or recent graduates.
- **Stack Overflow Developer Survey**: 84% of developers use AI tools (2025, +14 pts vs 2023); **73% of AI users use assistants/agents daily** (2026).

### AI capability vs AI reliability [A]

- SWE-bench solved-rate: **4.4% (2023) → 71.7% (2024)**.
- **Veracode 2025**: **45%** of AI-generated code samples introduced an OWASP Top 10 vulnerability.
- **METR 2025 RCT**: experienced developers were **19% slower** with AI assistance while believing they were **20% faster**.
- Independent telemetry: **26.9%** of merged production code is AI-generated; executive claims run 20–30%.

**Slide-worthy implication:** the bottleneck moved from *writing* code to *deciding what to write and verifying it*. That is precisely the skill juniors were previously not required to have.

### AI skill premium [B]

- Lightcast: postings requiring AI skills pay **~28% more** (~$18k/yr).
- PwC 2026: broader estimate of a **62% premium**.
- **NACE 2026**: **13.3%** of entry-level postings now require AI skills.

---

## 2. The funnel and where candidates actually die

### Volume [A/B]

| Metric | Value | Source |
|---|---|---|
| Applications per job posting | **95** (2025) vs 28 (2021) | Greenhouse customer data |
| Applications per hire | **291** vs ~100 in early 2021 | Ashby, 2026, 109M applications |
| Applications → interview | **3.6%–4.7%**, down from 7–8% in 2021 | Ashby, 2026 |
| Job seekers using AI to apply | **74%** | Greenhouse, 2025 (n=1,200) |

### Resume screening [A/B]

- **7.4 seconds** initial skim (TheLadders 2018 eye-tracking; 6s in the 2012 original).
- **30 seconds** to decide whether a resume deserves a closer read (Jobseeker 2025, n=1,013 HR professionals).
- **92% of ATS platforms do not auto-reject** on content — they **rank and sort** (Enhancv 2025, n=25 recruiters). Ranking #150 out of 180 is functionally a rejection.
- **99.7%** of recruiters use filters in their ATS (Jobscan 2025, n=384): missing key skills, mismatched title, missing degree/certification.
- **77%** of hiring managers call typos an instant deal breaker (CareerBuilder/Harris 2018).
- ATS installed at **97.4%** of Fortune 500 (Jobscan 2026, manual count).

### College-hiring benchmarks [A]

- **NACE 2026**: **63.1%** average intern→full-time conversion; **70%** of employers use skills-based hiring (up from 65%); only **42%** plan to screen GPA (down from **73%** in 2019); **85%** look for teamwork on the resume; hiring projected **+5.6%** for the Class of 2026.
- When GPA is dropped, the top factors are: academic major (~94%), industry experience (~81%), industry internships (~79%), internship with the hiring company (~74%).

---

## 3. What panels actually score

Engineering scorecards typically cover: **technical depth, code quality, problem decomposition, communication, collaboration** (Rework 2026 hiring playbooks).

Key mechanics worth teaching:

1. **Knockout competencies.** Teams pre-define a minimum total plus mandatory minimums (e.g. "coachability must be ≥3/5"). A candidate can outscore the threshold and still be a no-hire.
2. **Behavioral-anchored rubrics.** Each level has an observable description — decoys the "gut feeling" problem.
3. **Question-type mapping.** Behavioral → past action (situation/action/result); situational → reasoning and trade-offs; technical → method, accuracy, application.

**Softer signal [C]:** one widely repeated claim is that ~82% of hiring managers say communication eliminates candidates before technical ability does. Treat as directional, not citable.

---

## 4. How AI changed the interview loop

### Detection and fraud [B]

- **Greenhouse 2026**: recruiters observed candidates using AI during interviews in **35%** of cases; **91%** of recruiters/hiring managers have spotted or suspected deception.
  - AI-inflated resume claims: **63%** (most common)
  - Fake references: **48%**
  - Live AI use in interview: **35%**
  - **74%** more worried about fake credentials than a year ago.
- **Gartner**: 6% of 3,000 candidates self-report interview fraud; projects **1 in 4 profiles could be fake by 2028**.
- **Fabric** analysis of 19,368 interviews (Jul 2025–Jan 2026): cheating detected in **38.5%**, concentrated in technical and junior hiring; AI-assisted candidates cleared the approval threshold **61%** of the time.

### Countermeasures [A/B]

- **Gartner**: **72.4%** of recruiting leaders now run at least one in-person interview to combat fraud. In-person requests surged from ~**5% of roles (2024) to ~30% (2025)**; Google, Cisco, McKinsey reinstated onsite rounds.
- **Stanford**: seven leading AI-text detectors misclassified **non-native English writing as machine-generated 61% of the time**. Detection is unreliable — especially for Vietnamese candidates writing in English.
- **Robert Half**: **>25%** of employers now allow AI during technical interviews, expected to approach **50%**. Canva, Rippling, Red Hat, Meta, Shopify openly permit it.
- **Anthropic**: has repeatedly redesigned its take-home because each new model closes the gap; its policy is now stage-dependent rather than a blanket ban.

**Slide-worthy implication:** companies are not trying to catch you using AI. They are trying to find out whether you can work *without* it when it fails. The reliable defence is being able to explain every line you submit.

---

## 5. Vietnam specifics

- **ITviec Vietnam IT Salary & Recruitment Market Report 2025–2026** (n=1,839 across professionals, freelancers, IT students, HR leaders, CxOs):
  - **66.1%** of companies increased IT headcount in 2025; **69.6%** plan to expand in 2026.
  - Average IT salary **43.2M VND/month**, slightly down (−1.1%) from 2024.
  - **73%** of companies have adopted AI, and it is shifting hiring priorities from pure technical skill toward **problem-solving, adaptability, and collaboration**.
- Supply: **~600,000** IT professionals and **~55,000–60,000 new IT graduates per year**.
- Fresher salary bands (TalentHero / Employsome 2026): back-end fresher **~12.4M VND**, full-stack fresher **~10.1M VND**, mobile fresher **~14.2M**, embedded **~21.4M**. Junior (0–2 yrs) **10–20M VND** depending on track.
- Demand concentration: AI/ML, data engineering, and Java/enterprise back-end lead; AI/ML engineers carry the largest premium (18–25M fresher band).

---

## 6. Claims to avoid

These circulate widely and are poorly sourced. Do not put them on a slide:

| Claim | Reality |
|---|---|
| "75% of resumes are rejected by ATS" | Traced to a 2012 vendor quote with no published method. Verified studies show ATS ranks rather than auto-rejects. |
| "Recruiters spend 6 seconds per resume" | The 6s figure is the 2012 TheLadders study; the 2018 follow-up measured 7.4s for the *first skim only*. |
| "250 applicants per job" | Originates from an unsourced 2015 Glassdoor blog post. Use Greenhouse (95) or Ashby (291/hire) instead. |
| "60% of juniors fail the phone screen" / "82% eliminated for communication" | No traceable primary source. Directionally plausible, numerically unreliable. |
| "AI will eliminate X% of junior jobs" | Forecasts, not measurements. Amodei's 50%-in-five-years is a scenario, not data. |

---

## 7. Sources

- Stanford Digital Economy Lab — *Canaries in the Coal Mine?* (Brynjolfsson, Chandar, Chen), Nov 2025 / Jun 2026 update
- Indeed Hiring Lab — software development posting index, 2025–2026
- Handshake — Class of 2026 network data
- NY Fed — College Labor Market data
- BLS — Occupational Outlook Handbook 2025–2035
- NACE — Job Outlook 2026, Internship & Co-op Report 2026
- Greenhouse — 2025 job-seeker survey; 2026 candidate AI research
- Ashby — 2026 application funnel data
- TheLadders — 2018 eye-tracking study
- Enhancv — 2025 recruiter ATS study (n=25)
- Jobscan — 2025 recruiter survey (n=384)
- TheHireHub / Fabric / Gartner / Robert Half / Stanford (AI text detectors)
- Veracode 2025, METR 2025, Lightcast, PwC 2026
- ITviec — Vietnam IT Salary & Recruitment Market Report 2025–2026
- TalentHero / Employsome — Vietnam developer salary guides 2026
