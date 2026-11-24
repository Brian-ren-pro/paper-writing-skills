---
name: paper-writing-system
description: A rule system for writing and revising Chinese and English economics/finance papers, organized by where you are writing - structure, each section (abstract to conclusion, tables, footnotes), language and AI-tone - with advisor guidance, corpus statistics and past revision cases as tagged sources. Use for annotating, reviewing, revising, drafting, final language checks, de-AI checks or referee-response planning. Entry point: references/protocol.md.
---

# Paper Writing Rule System v3.3（论文写作规则体系）

Use this skill for any task on academic papers, in Chinese or English: annotating, section-by-section review, authorized revision, structure design, drafting from a fact packet, a final language check, an AI-tone check, or referee-response planning.

## Entry point (mandatory)

1. Read `references/protocol.md` (file map, priority, disciplines D1–D9).
2. **Follow `references/workflow.md` stage by stage** for any revising, drafting, review or final-check task:
   0 intake and triage → 1 one batch of questions (`templates/intake.md`) → 2 fact base (`work/facts.csv`, `terms.md`, `claims.md`) → 3 diagnosis and plan → 4 revise section by section (empirics first, front matter last) → 5 language check (`scripts/run_checks.py`) → 6 consistency checks → 7 Word layout (`plugins/word-layout/`) → 8 delivery (revised docx, revision notes, check report, decisions list).
   Each stage has required outputs; log every stage in `work/RUNLOG.md` and do not start a stage before the previous one's outputs exist.
3. Decide the writing mode in `references/structure.md` §0 (E / ZE / ZC) at stage 1.
4. At stage 3, read `references/narrative.md`: fix the main battleground, list the advantages with their evidence, and record the comparisons the paper declines to fight.

## Tools

- `scripts/run_checks.py 稿件.docx --mode ZE|ZC|E [--terms] [--facts] [--out]` — read-only check report (banned constructions, colons, section openings and previews, long sentences, person, terminology, cross-references, numbers, reference list).
- `scripts/docx_tools.py text|replace` — read docx text; minimal string replacement that keeps formatting (original untouched).
- `plugins/word-layout/docx_format.py check|apply --profile cn-workingpaper|cn-journal|en-submission` — Word layout plugin (three-line tables, fonts, spacing, footnotes, references).
- `templates/` — intake questions, facts.csv, RUNLOG, revision notes, decisions list.
Scripts need Python 3; the layout plugin needs python-docx and lxml.

## Layout (all under `references/`)

- `protocol.md` — master protocol.
- `structure.md` — writing modes, principles, framework choice, length budgets, cross-chapter patterns, and how to cross-reference other sections (§5).
- `narrative.md` — which battle the paper fights: advantage inventory, scope of comparison, where unfavourable information goes (body / footnote / omitted), the must-report red list, and the order of compromises when the results are weak.
- `sections/` — one file per part of the paper: abstract, introduction (+ English intro guide card), background-literature, theory-hypotheses, data-variables, identification, results (also number and magnitude rules for the whole paper), robustness, mechanism-heterogeneity, conclusion, tables-figures-footnotes. Each gives length, paragraph map, rules, Chinese and English phrasing, common problems and a checklist.
- `language/` — `zh.md`, `en.md` (rules shared by all sections, including banned constructions) and `ai-tone.md` (detect → graded report → reply → rewrite → re-check).
- `voices/` — five scholar style files; load only when the user asks to write like a given scholar.
- `sources/` — advisor guidance A1–A42 (original items), casebook C-01–C-25, Zotero corpus statistics (178 English, 33 Chinese top-journal papers), 22-paper annotated corpus with verbatim examples, collaboration meta-rules. Evidence, not executed directly.

Rules carry source tags: 【导师 Ax】 advisor, 【语料】 corpus statistics, 【22 篇】 annotated corpus, 【判例 C-xx】 casebook, 【规则】 author ruling.

## Non-negotiables

- **Annotate by default**; rewrite only when the user authorizes it in this conversation. Their rulings close an item permanently.
- **Facts only from the task's sources**; never reconstruct numbers, data procedures or institutional facts from memory. Ask once, in one batch, for anything only the author can supply.
- **Revise his latest draft**: re-read the file from his device before editing; write back with a modification-time guard; remind him to close the file in Word first.
- **Minimal change, information conserved** for language and AI-tone edits; numbers, citations and hedges unchanged.
- **Report before rewriting** for language and AI-tone checks.
- **Check style advice against the corpus** before proposing it; withdraw advice the corpus does not support.
- **Rule files change only with his approval**; log each change. Tensions are reported, not self-adjudicated.

## Non-negotiable: findings become per-item decisions (protocol D10)
Never report a text problem only as a count or a description. For every finding that would change the manuscript, give position, the full original sentence, the problem with its rule source, and a ready-to-paste rewrite (or "keep" with a reason). Then ask the author item by item: agree / reject / write their own fix — with AskUserQuestion when available (≤4 per call, recommended option first, "original → rewrite" in the preview), otherwise as a numbered list. Record answers in `work/decisions.md`; edit only agreed or author-written items.
