# Introduction blueprint: corpus analysis (English top-journal intros)

Date: 2026-10-20. Corpus: the cleaned 267-paper English external set defined by `writing_spec/scripts/common_ws.py::load_en()`. That set drops title/text mismatches, papers with no intro or no conclusion, and intros under 500 or over 5,000 words. Journals: JF, JFE, RFS, JFQA, MS (finance) and JAR, TAR, CAR (accounting).
No corpus text is stored here. Every quoted pattern is a placeholder template I abstracted from a paper's first sentence.

## TL;DR (headline numbers)

- **Paragraph breaks in `corpus/segments` are unusable.** Intros there have a median of 4 "paragraphs", 71% of intro words sit in blocks over 400 words, and 21% of blocks end mid-sentence. I rebuilt the breaks from PDF line geometry (indent, vertical gap, font height) and trusted **117/267 papers** (77 finance, 40 accounting).
- **Typical top-journal intro:** about **1,850 words** [IQR 1,450–2,230], **14 paragraphs** [11–17], **73 sentences** [55–90]. Paragraphs run **5 sentences** [4–6] and about **125 words**, with **25 words per sentence** [22–30]. Paragraph length barely changes from the first fifth to the last. The roadmap is the one short paragraph (about 55 words). 91% of intros have footnote markers (median 6). 44% end with a roadmap paragraph (finance 52%, accounting 30%).
- **What a 14-paragraph intro spends its paragraphs on** (40 hand-labelled intros, 565 paragraphs): about 3 contribution paragraphs (90% of intros have them), 1–2 theory/hypothesis paragraphs (75%), 1–2 main-finding paragraphs (88%), 1–2 heterogeneity/additional-result paragraphs (80%), 1 robustness paragraph (60%) and 1–2 mechanism paragraphs (55%). Hook (55%), data/setting (55%), design (45%), identification challenge (40%), implications (38%), roadmap (40%) and a stand-alone magnitude paragraph (20%) each take at most one.
- **Order:** the research-question/"this paper" statement comes in paragraph 1 or 2 in 27/40 intros. The first result arrives at about 37% of the way through. The contribution block sits at the end (it starts at relative position 0.71, and 31/36 intros have a contribution paragraph among the last three). Archetypes: linear 15, interleaved setup↔results 11, early literature positioning 11, theory-led 3.
- **Contribution paragraphs** name a median of 4 papers each (IQR 2–6). 89% of intros with such paragraphs state explicitly how this paper differs. About 2–3 strands get one paragraph each. Accounting announces the count ("makes three contributions") far more often: 73% vs 29% in finance.
- **Quantification:** 29/40 intros give at least one magnitude: percentage change 60%, absolute units (bp, $, cents) 35%, versus a benchmark or mean 22%, standard-deviation scaling 12%. The number usually sits inside the main-finding paragraph. Only 8/40 have a separate "economically significant" paragraph.

## 1. Method

### Step 1. Paragraph-break reliability

1. **I checked the existing segments first.** `corpus/segments/*.json` intro paragraphs for the 267 papers: 1,343 blocks, median 4 per intro. 42% of blocks are over 400 words, and they hold 71% of intro words. 235/267 intros have more than 25% of their words in 400+ word blocks. 21% of blocks end without terminal punctuation. Segment text also contains footnote text inline. **Verdict: the breaks are unusable.**
2. **I rebuilt the breaks from the PDFs** (`rebuild_paras.py`). All 267 PDFs exist locally (Zotero storage or `corpus/external`). `pdftotext -bbox-layout` over pages 1–14 gives every line's x/y box and word heights. Per paper:
   - Body font height = modal line height. Running heads (lines repeated on 3 or more pages), page numbers, margin watermarks and download stamps are dropped.
   - **Footnotes are removed by font size:** from the first small-font line in the lower page, plus its numbered lead-in, to the page end. Superscript footnote markers are counted, then stripped.
   - **The intro starts** after an "Introduction" heading, or at the segment's first words. **It ends** at the next top-level section heading (taken from the segment file), with a word cap as a fallback.
   - **A new paragraph starts** on (a) a first-line indent of 2.5–30 pt, (b) a vertical gap over 1.45× normal line spacing, or (c) a line ending in terminal punctuation well short of the right margin followed by a capital letter. Hyphenated line ends are re-joined.
3. **Trust filter** (per paper):
   - at least 4 paragraphs and at least 450 words;
   - no more than 25% of words in 400+ word paragraphs;
   - no more than 15% of paragraphs under 20 words;
   - no more than 15% of paragraphs ending mid-sentence;
   - rebuilt length 0.7–1.2× the segment's intro word count;
   - the intro end was actually found.

| Journal | cleaned set | rebuilt from PDF | trusted |
|---|---:|---:|---:|
| JF | 54 | 50 | 21 |
| JFE | 49 | 47 | 17 |
| RFS | 34 | 32 | 16 |
| JFQA | 27 | 25 | 13 |
| MS | 25 | 21 | 10 |
| JAR | 45 | 44 | 27 |
| TAR | 22 | 22 | 7 |
| CAR | 11 | 9 | 6 |
| **All** | 267 | 250 | **117** |

Reasons for distrust among the 133 rebuilt-but-untrusted papers (a paper can fail several):

| Reason | Papers |
|---|---:|
| length ratio outside 0.7–1.2 (usually the intro end was mis-detected) | 79 |
| merged blocks (over 25% of words in 400+ word blocks) | 63 |
| fewer than 4 paragraphs | 61 |
| over 15% of paragraphs end mid-sentence | 43 |
| intro end not found | 31 |
| over 15% of paragraphs under 20 words | 11 |
| fewer than 450 words | 6 |

17 PDFs gave no usable bbox output.

In the trusted set, 0.0% of paragraphs exceed 400 words and 0.3% are under 20 words. **Method used: PDF-geometry paragraph reconstruction. I did not fall back to sentence windows.**

### Step 3. Hand labelling

**Sample.** A stratified random sample of 5 trusted intros per journal (40 intros, 572 paragraphs; seed 20261020). I read every paragraph in full and assigned one function per paragraph.

**Functions.** The suggested closed set plus three additions:
- *theory/hypothesis development*: predictions, model set-up and model results in theory papers;
- *caveat/scope*;
- *extraction artifact*: 7 paragraphs, excluded from all aggregates.

**Per-paragraph record.** Sentence and word counts come from the rebuilt text. `cites_auto` is an automatic count of distinct author-year citations. The rest I wrote by hand:
- **slots:** the information the paragraph carries, from a fixed vocabulary (below);
- **opening pattern:** the first sentence abstracted with [placeholders].

**Slot vocabulary.** I used the slot names below, grouped here by what they cover:
- *Motivation and question:* `fact_number`, `trend`, `policy_context`, `anecdote`, `analogy`, `puzzle`, `two_views`, `importance_claim`, `prior_lit_general`, `named_papers`, `gap_explicit`, `rq_explicit`, `this_paper_statement`, `contribution_overview`.
- *Theory:* `theory_argument`, `competing_predictions`, `hypothesis_stated`, `model_setup`, `model_result`.
- *Setting, data and design:* `identification_threat_named`, `shock_named`, `setting_named`, `setting_justification`, `data_source_named`, `sample_period`, `N_obs`, `unit_named`, `measure_construction`, `design_named`, `comparison_group`, `fixed_effects`.
- *Results:* `main_result_direction`, `enumerated_findings`, `magnitude_pct`, `magnitude_sd`, `magnitude_abs`, `magnitude_relative_benchmark`, `stat_significance`, `heterogeneity_dim`, `mechanism_channel`, `interpretation`, `figure_reference`, `extension`, `validation_test`.
- *Robustness and identification checks:* `alt_explanation_ruled_out`, `robustness_list`, `placebo_pretrend`.
- *Positioning and implications:* `contribution_strand_named`, `difference_stated`, `first_claim`, `policy_implication`, `implication_for_theory`, `implication_for_practice`, `future_research`, `scope_limit`, `section_list`.

Output: `para_labels.jsonl`, one row per paragraph with fields `key`, `journal`, `position`, `n_paras`, `rel_position`, `function`, `sentences`, `words`, `cites_auto`, `slots` and `opening_pattern`. It holds no paragraph text.

## 2. Step 2 statistics (117 trusted intros; median [p25–p75])

### 2a. Whole introduction

| Group | n | words | paragraphs | sentences | sent/para | words/sent | roadmap para | footnote markers | has subheads |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **All** | 117 | 1848 [1446–2225] | 14 [11–17] | 73 [55–90] | 5 [4–6] | 25.5 [21.6–29.8] | 44% | 6 [3–8] (≥1: 91%) | 11% |
| Finance | 77 | 1832 [1446–2293] | 14 [11–18] | 74 [59–92] | 5 [4–6] | 24.8 [21.0–29.0] | 52% | 6 [3–8] (≥1: 92%) | 13% |
| Accounting | 40 | 1876 [1458–2195] | 13 [12–16] | 69 [54–82] | 5 [4–6] | 26.9 [23.0–31.7] | 30% | 5 [2–7] (≥1: 90%) | 8% |
| JF | 21 | 1710 [1458–2225] | 14 [11–18] | 68 [59–95] | 5 [4–6] | 24.8 [20.5–29.0] | 57% | 6 [4–9] | 33% |
| JFE | 17 | 1900 [1247–2335] | 14 [10–17] | 73 [50–89] | 5 [4–6] | 24.5 [21.2–28.8] | 71% | 4 [3–8] | 0% |
| RFS | 16 | 1930 [1406–2228] | 14 [12–18] | 80 [64–95] | 5 [4–7] | 24.1 [20.4–28.3] | 38% | 8 [3–10] | 12% |
| JFQA | 13 | 1916 [1607–2071] | 15 [11–19] | 80 [65–91] | 5 [4–7] | 24.0 [21.0–26.8] | 46% | 7 [3–7] | 8% |
| MS | 10 | 1962 [1722–2255] | 14 [13–17] | 70 [53–86] | 5 [4–7] | 27.9 [22.8–33.1] | 40% | 3 [2–6] | 0% |
| JAR | 27 | 2087 [1622–2246] | 14 [13–16] | 77 [60–88] | 5 [4–6] | 26.5 [23.0–31.0] | 22% | 6 [3–8] | 4% |
| TAR | 7 | 1838 [1502–1983] | 14 [12–15] | 66 [59–75] | 5 [4–7] | 26.2 [22.7–31.8] | 43% | 3 [1–4] | 0% |
| CAR | 6 | 1652 [1281–1856] | 10 [9–12] | 56 [52–62] | 5 [4–7] | 30.4 [23.4–36.2] | 50% | 4 [2–5] | 33% |

The sent/para and words/sent columns pool all paragraphs in the group. **Ignore the "has subheads" column.** On inspection, almost every detected heading is the *next* section's title ("I. Data", "I. Methodology"), which the detector catches at the intro boundary when the heading wraps onto two lines. It is not a real intro subheading. Real "Related literature" run-in subheads do occur (e.g., a JFE intro and a JF intro in the labelled sample), but they are not measured reliably here.

### 2b. By paragraph position (all trusted)

| Position | n paras | words | sentences | words/sent |
|---|---:|---:|---:|---:|
| First paragraph | 117 | 123 [92–158] | 5 [4–6] | 25.0 [21.5–29.2] |
| Last paragraph | 117 | 84 [52–122] | 5 [4–6] | 19.2 [10.8–26.0] |
| Last non-roadmap paragraph | 117 | 122 [76–166] | 5 [3–7] | 25.0 [21.9–29.0] |
| Body, fifth 1 (0–20%) | 236 | 130 [103–168] | 5 [4–7] | 25.8 [22.0–29.6] |
| Body, fifth 2 (20–40%) | 310 | 123 [97–159] | 5 [4–6] | 25.3 [21.5–30.0] |
| Body, fifth 3 (40–60%) | 304 | 129 [107–161] | 5 [4–6] | 25.9 [22.4–30.0] |
| Body, fifth 4 (60–80%) | 310 | 127 [93–171] | 5 [4–7] | 26.0 [22.2–29.7] |
| Body, fifth 5 (80–100%) | 256 | 134 [99–171] | 5 [4–6] | 26.0 [22.5–30.2] |

The body fifths exclude the first and last paragraph. Finance and accounting splits are in `stats_tables.md`. Accounting body paragraphs are slightly longer (fifth 1: 151 vs 124 words) and run about 2 words more per sentence.

**Roadmap.** 52/117 intros have one, and in 49 of them it is the final paragraph. It runs 55 [43–87] words and 5 [5–6] short sentences, roughly one sentence per section.

## 3. Paragraph functions (40 labelled intros)

### 3a. Function profiles

| Function | % intros | paras per intro (if present) | median rel. position | sentences/para | words/para | citations/para |
|---|---:|---:|---:|---:|---:|---:|
| hook/phenomenon | 55% | 1 [1–2] | 0.00 | 6 [4–6] | 126 [85–169] | 2 [1–4] |
| research question/gap | 85% | 1 [1–1] | 0.07 | 5 [4–7] | 138 [92–159] | 1 [0–3] |
| theory/hypothesis development | 75% | 2 [1–3] | 0.23 | 6 [4–7] | 128 [102–167] | 1 [0–3] |
| data & setting | 55% | 1 [1–2] | 0.21 | 5 [4–6] | 131 [110–163] | 1 [0–3] |
| empirical design | 45% | 1 [1–1] | 0.35 | 4 [4–6] | 121 [107–177] | 0 [0–2] |
| why hard/identification challenge | 40% | 1 [1–1] | 0.46 | 5 [4–7] | 132 [96–173] | 0 [0–2] |
| main finding | 88% | 1 [1–2] | 0.46 | 5 [4–6] | 119 [91–153] | 0 [0–1] |
| magnitude/economic significance | 20% | 1 | 0.41 | 5 [4–6] | 102 [87–209] | 0 |
| additional results/heterogeneity | 80% | 1 [1–2] | 0.61 | 5 [4–6] | 132 [101–157] | 0 [0–1] |
| mechanism | 55% | 2 [1–3] | 0.55 | 5 [4–7] | 133 [107–163] | 1 [0–2] |
| robustness/alternative explanations | 60% | 1 [1–2] | 0.61 | 4 [3–6] | 116 [81–157] | 0 [0–1] |
| contribution to literature strand | 90% | 3 [2–3] | 0.85 | 5 [4–6] | 131 [96–171] | **4 [2–6]** |
| policy/implication | 38% | 1 | 0.82 | 5 [3–6] | 117 [96–145] | 0 [0–1] |
| caveat/scope | 12% | 1 | 0.81 | 5 [4–7] | 129 [99–146] | 0 |
| roadmap | 40% | 1 | 1.00 | 6 [5–6] | 54 [47–61] | 0 |

Relative position runs from 0 (first paragraph) to 1 (last). The citation counts are automatic and approximate.

### 3b. Typical sequences

Each intro was classified into one archetype from its labels:

| Archetype | n/40 | Skeleton (collapsed) |
|---|---:|---|
| **Linear** | 15 | Hook → Question/"this paper" → (Theory/Hypotheses) → Data & setting → Design → Main finding → Heterogeneity/Mechanism → Robustness → Contributions ×2–3 → (Implications) → (Roadmap) |
| **Interleaved** | 11 | Hook → Question → Data/Design₁ → Finding₁ → Design₂/"Next we exploit…" → Finding₂ → … → Contributions → Roadmap. Each test is introduced with its own design sentence before its result. |
| **Early positioning** | 11 | Hook → Prior literature and its gap (named papers, 1–3 paragraphs) → "In this paper…" → Setting → Findings → (shorter) Contributions |
| **Theory-led** | 3 | Puzzle/Question → Model set-up → Model results ×3–5 → Estimation/Calibration → Findings → Literature |

Most frequent paragraph-to-paragraph transitions, with repeats collapsed:

| Transition | Count |
|---|---:|
| question → theory/hypothesis | 17 |
| hook → question | 14 |
| design → main finding | 12 |
| theory → data/setting | 11 |
| robustness → additional results | 11 |
| main finding → additional results | 10 |
| theory → main finding | 10 |
| additional results → contributions | 9 |
| contributions → roadmap | 9 |

**Anchors that hold across archetypes:**
- the "this paper" statement is in paragraph 1 or 2 in 27/40 intros;
- the first finding is about 37% of the way in (finance 0.38, accounting 0.36);
- a contribution paragraph is among the last three in 31/36 intros;
- a roadmap, when present, is last.

### 3c. Function blueprints

**Slots at the block level.** For each intro I took the union of slots across all its paragraphs of a function. "Almost always" means at least 70% of intros that have the function; "often" means 30–69%.

**Opening patterns.** These are curated from my 40 readings. Automatic family shares are in `label_tables.md`.

**Hook / phenomenon** (55%; paragraph 1; 1–2 paragraphs; 6 sentences)
- Often present: named papers (68%), explicit gap (45%), trend (32%), striking number (32%).
- Openers:
  - "[Market/practice] has grown to [N] / Recent decades have seen [trend]."
  - "In [year], [concrete event with a number]." (anecdote)
  - "[Institution X] is designed to [goal], yet [tension]."
  - "Standard [theory] assumes/predicts [X]." (a puzzle follows)
  - "A neglected topic in [field] is [X]."
- Usually ends by flipping to the gap or the question in its last sentence.

**Research question / gap / "this paper"** (85%; paragraph 1–2; 1 paragraph; 5 sentences)
- Almost always: a this-paper statement (94%).
- Often: named papers (62%), explicit gap (41%).
- Openers:
  - "In this paper, we study/examine whether [X] affects [Y]."
  - "This paper investigates [X]'s role in [event/setting]."
  - "Prior research establishes [X]. What is less well known is [Y]."
  - "Despite [importance], there is limited evidence on [X]. We [verb] …"
  - "Although prior literature on [X] examines [A], we study [B]."
- In accounting, the question paragraph is often paragraph 1 itself (accounting median first-Q position 0.0, finance 0.10).

**Theory / hypothesis development** (75%; positions about 0.15–0.30; 2 [1–3] paragraphs; 6 sentences)
- Almost always: named papers (73%).
- Often: theory argument (67%), explicit hypothesis (47%), competing two-sided predictions (43%).
- Openers:
  - "Our central hypothesis is that [X] provides [agents] with [Y]."
  - "On the one hand, [prediction A]." / "On the other hand, [B]." (a paragraph each)
  - "There are at least two reasons why [X] may have little effect on [Y]."
  - "To motivate the empirical analysis, we draw on [theory/Paper]."
  - "Based on this framework, we make the following predictions."

**Data & setting** (55%; position about 0.2; 1–2 paragraphs; 5 sentences)
- Often: why the setting is good (68%), named papers (64%), named data source (55%), N obs (50%), measure construction (50%), sample period (36%).
- Openers:
  - "To test [predictions], we use a unique [dataset] collected by [source]."
  - "We test these predictions in the setting of [market], where [variation] and [granular data] are available."
  - "[Setting] is an ideal laboratory to study [X] because [reason]."
  - "We exploit [shock/event] to …"
  - "Our sample comprises [N units] over [period]."

**Empirical design** (45%; position about 0.35; 1 paragraph; 4 sentences)
- Often: measure construction (67%), named design such as DiD/IV/event study/RD (44%), named papers (44%), treatment vs control (39%).
- Openers:
  - "Our main empirical strategy employs a difference-in-differences framework."
  - "We implement a DiD design where the treatment group is [A] and the control group is [B]."
  - "In our main specification, we regress [Y] on [X] with [fixed effects]."
  - "We measure [construct] using [data/method]."

**Why hard / identification challenge** (40%; position about 0.45; 1 paragraph; 5 sentences)
- Almost always: the threat is named (88%).
- Often: named papers (50%).
- Openers:
  - "One concern / A possible threat to identification is that [confound]."
  - "The key empirical challenge in testing this hypothesis is (1) [X] and (2) [Y]."
  - "There are [three] potential concerns for identification, which we address as follows."
  - "Given that [X] is unobservable, it is challenging to [Y]."
- In the sample this paragraph usually comes **after** the main result (rebutting threats), not before the design.

**Main finding** (88%; first at about 0.38; 1–2 paragraphs; 5 sentences)
- Almost always: direction and sign of the main result (91%).
- Often: % magnitude (51%), named papers for comparison (40%).
- Openers:
  - "We find that [X] increases [Y] by [k%/bp] after [event]."
  - "Our key finding is that [X]."
  - "The article reports three main findings. First, …"
  - "Consistent with our first hypothesis, we find [X]."
  - "Using [design], we find [X]."

**Magnitude / economic significance** (20% as its own paragraph; otherwise folded into the finding)
- Often: % (62%), absolute units (50%), comparison to a benchmark or mean (50%).
- Openers:
  - "This effect is also economically significant: [X] corresponds to [k%] of the sample mean/SD."
  - "Relative to [benchmark/prior estimate], this is [larger/comparable]."

**Additional results / heterogeneity** (80%; position about 0.6; 1–2 paragraphs; 5 sentences)
- Almost always: the heterogeneity dimension is named (78%).
- Often: named papers (47%), direction (38%).
- Openers:
  - "We next examine whether the effect varies with [dimension]."
  - "Second/Third, we find that [subgroup] [stronger/weaker]."
  - "To understand [X], we examine three sources of heterogeneity."
  - "Consistent with our theory, the effect is stronger when [condition]."

**Mechanism** (55%; position about 0.55; 2 [1–3] paragraphs; 5 sentences)
- Almost always: the channel is named (91%), with named papers (73%).
- Openers:
  - "As a deeper test of the mechanism, we examine [X]."
  - "To test whether [channel] drives the result, we focus on [agents/sub-sample]."
  - "We consider and test [four] possible mechanisms."
  - "The first/second class of explanations is that [X]." (one paragraph per channel, each ending with a verdict)

**Robustness / alternative explanations** (60%; position about 0.6; 1–2 paragraphs; 4 sentences; the shortest)
- Often: alternative explanations ruled out (67%), a list of checks (46%), a named design (42%), named papers (38%).
- Openers:
  - "We employ a battery of sensitivity checks to rule out [alternatives]."
  - "Our results are robust to [list]."
  - "We also examine several other alternative explanations. First, [X]."
  - "A falsification test finds no effect in [placebo period/sample]."

**Contribution to literature strand** (90%; positions about 0.7–1.0; 3 [2–3] paragraphs; 5 sentences)
- Almost always: named papers (97%; median 4 citations per paragraph), how we differ (89%), the strand named (75%).
- Often: a contribution count announced (36%), a gap restated (33%).
- Openers:
  - "Our paper makes three contributions. First, we extend the literature on [topic]."
  - "We also contribute to the growing literature on [topic] (Papers)."
  - "This paper relates to [Paper(s)], who [do X]. In contrast, we [Y]."
  - "The papers most closely related to ours are [A] and [B]."
  - "Relative to this literature, our contribution is to [X]."

**Policy / implication** (38%; position about 0.8; 1 paragraph)
- Often: policy implication (60%), named papers (40%), implication for theory (33%).
- Openers:
  - "Finally, our results have important policy implications."
  - "Our findings have implications for [regulator/practice]."

**Roadmap** (40% of the sample; 44% of all 117 trusted; always last; about 55 words)
- "The remainder of the paper is organized as follows. Section 2 … Section N concludes."

### 3d. How contribution paragraphs are organised

- 36/40 intros have them, with 3 [2–3] paragraphs and about 2 [1–3] distinct strands. The usual unit is **one strand per paragraph**. A paragraph names the strand, cites 2–6 papers (median 4), states the difference, and sometimes ends with "first to" (25% of intros).
- **Organisation:**
  - a **contiguous single block** in 75% of intros;
  - starting at relative position 0.71 [0.29–0.85];
  - **announced with a count** in 47% of intros: "makes three contributions" / "First, … Second, … Third, …".
- **The difference is stated** in at least one contribution paragraph in 89% of intros. In the median intro, 67% of contribution paragraphs state it.
- **Finance vs accounting.** Finance blocks are more variable: 3 [2–5] paragraphs, sometimes positioned early, count announced in 29%. Accounting is formulaic: 3 [3–3] paragraphs, late (0.75 [0.67–0.82]), count announced in 73%.

### 3e. How results are quantified

| Measure | Result |
|---|---|
| Intros with at least one magnitude | 29/40 |
| Percentage change (incl. % of mean) | 60% of intros |
| Absolute units (bp, $, cents, ratios) | 35% |
| Comparison to a benchmark (sample mean, a prior estimate, another known effect) | 22% |
| Standard-deviation scaling | 12% |
| Where magnitudes appear | main finding 26 paragraphs; heterogeneity 12; separate magnitude paragraph 8; mechanism, robustness, design, contribution 3 each |
| Main-finding paragraphs carrying a number | 47% |

Common phrasings (templates):
- "[X] increases [Y] by [k] bp/pp, which corresponds to [m]% of the sample mean."
- "A one-SD increase in [X] is associated with [k]% higher [Y]."
- "This is comparable to / larger than [benchmark effect] in [Paper]."

### 3f. Finance vs accounting (labelled sample 25 vs 15; trusted-set stats 77 vs 40)

| Function | Finance % intros (n=25) | Accounting % intros (n=15) |
|---|---:|---:|
| hook/phenomenon | 64% | 40% |
| research question/gap | 76% | 100% |
| theory/hypothesis | 72% | 80% |
| identification challenge | 44% | 33% |
| data & setting | 48% | 67% |
| empirical design | 52% | 33% |
| main finding | 96% | 73% |
| heterogeneity | 88% | 67% |
| mechanism | 60% | 47% |
| robustness | 56% | 67% |
| contribution | 84% | 100% |
| policy/implication | 44% | 27% |
| caveat/scope | 8% | 20% |
| roadmap (trusted set, n=117) | 52% | 30% |

- **Accounting** opens on the research question (100%, often in paragraph 1 with "Prior research establishes … What is less well known …"). It states hypotheses or competing predictions more explicitly (explicit hypothesis 9/15 vs 11/25). It always has a contribution block and usually announces its count. It more often adds a caveat ("establishing causality is difficult"). It has fewer roadmaps. Its sentences are about 2 words longer.
- **Finance** more often opens with a hook (a fact, number or anecdote). It reports more distinct result paragraphs (main finding 96%, heterogeneity 88%, mechanism 60%). It discusses design and identification explicitly more often. It gives magnitudes more often (19/25 vs 10/15). It also has more implication paragraphs.
- Size is the same: about 1,850 words and 13–14 paragraphs.

## 4. Caveats

1. **Selection.** Trusted papers are those whose PDFs have clean layout. Older scans, two-column SSRN versions and papers whose next-section heading was hard to find are under-represented. TAR (7/22) and CAR (6/11) give small n. Per-journal medians for TAR, CAR and MS are indicative only.
2. **Residual extraction noise.** A few labelled intros still lost or merged material:
   - one RFS intro lost its first paragraph to a cover page;
   - one JFE intro appears truncated before its literature paragraphs;
   - CAR intros had two heading-fragment splits;
   - one MS paragraph had figure text injected.

   I labelled 7 paragraphs as artifacts and excluded them. Footnote-marker counts can miss markers glued to digits.
3. **Single-coder labels.** All 572 labels are mine, from one reading, with no second coder and no reliability statistic. Boundaries that are judgment calls: theory vs question (the "this paper argues" paragraph), finding vs additional result, mechanism vs heterogeneity (cross-sectional tests motivated by a channel I usually coded as mechanism), robustness vs identification challenge. Treat percentages as ±10 pp.
4. **One function per paragraph.** Many real paragraphs do two jobs, such as design plus result, or finding plus magnitude. That is why "magnitude" looks rare as a function but common as a slot. Use the slot tables, not the function shares, when deciding what information to include.
5. **Mixed paper types.** The sample mixes empirical, theory, experimental, structural, qualitative and historical papers (e.g., 2 CAR intros are qualitative or case studies, one TAR intro is historical, three are theory or econometrics). The blueprint fits empirical-causal papers best.
6. **Automatic counts are approximate.** Sentence splitting, citation counting (`cites_auto` counts author-year patterns and can miss bracketed JAR-style years or double-count multi-year cites) and the opening-family regexes in `label_tables.md` all approximate. The curated opening templates in §3c come from reading, not from the regex.

## 5. Files and reproduction

All files are in `writing_spec/intro_blueprint/`.

| File | What it holds |
|---|---|
| `rebuild_paras.py` | PDF-geometry paragraph reconstruction. It caches bbox HTML and the rebuilt text in `/tmp/intro_blueprint_cache/` (private, outside the repo). Set `INTRO_CACHE` to move the cache. |
| `intro_stats.py` | Steps 1–2. Writes `paper_quality.csv` (per-paper metrics and trusted flag), `para_stats.csv` (per-paragraph numbers) and `stats_tables.md`. |
| `labels/labels_*.txt` | Hand labels: `key\|para\|function code\|slots\|opening pattern`. |
| `build_labels.py` | Writes `para_labels.jsonl`. |
| `aggregate_labels.py` | Writes `label_tables.md` (Step 4 tables). |

Function codes used in the label files: H hook, Q question, T theory, C challenge, D data, E design, F finding, M magnitude, A additional, K mechanism, R robustness, L literature, P policy, V caveat, O roadmap, X artifact.

Run from the project root:
```
python3 writing_spec/intro_blueprint/rebuild_paras.py      # ~25 s; needs pdftotext and local PDFs
python3 writing_spec/intro_blueprint/intro_stats.py        # Step 1–2 tables
python3 writing_spec/intro_blueprint/build_labels.py       # needs the cache from rebuild_paras.py
python3 writing_spec/intro_blueprint/aggregate_labels.py   # Step 4 tables
```

Round-4 DeepSeek generation was not run: `SKILLTRAIN_API_KEY` is not set in this environment.
