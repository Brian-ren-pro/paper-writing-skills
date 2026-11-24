# Layout evidence: where the four layouts come from

2026-10-20. This file covers four things:
- how the four intro layouts are defined;
- an objective rule that assigns them, and how well it agrees with hand assignment;
- the extra labelling done so that each layout has at least 5 papers;
- 12 full paper analyses, 3 per layout.

The only corpus text here is anchor excerpts of at most 20 words.
Scripts are in `layout/`. `python3 writing_spec/intro_blueprint/layout/build_evidence.py` regenerates this file. It needs the paragraph cache, which `rebuild_paras.py` rebuilds.

| File | What it holds |
|---|---|
| `layout/hand_layout_40.csv` | Hand layout and a one-line reason for each of the 40 originally labelled intros |
| `layout/hand_layout_supp.csv` | The same for the 7 intros labelled today |
| `layout/labels_supp.txt` → `layout/para_labels_supp.jsonl` | Paragraph labels for the 7 new intros, in the same scheme as `labels/` (built by `layout/build_supp.py`). They are kept separate so the 40-intro statistics in `REPORT.md` and `INTRO_TEMPLATE_zh.md` do not change |
| `layout/assign_layout.py` | Features, rules v1/v2/v3 and confusion tables; writes `layout/layout_features.json` |
| `layout/analysis_spec.py` + `layout/render_analyses.py` | My sentence-role tags for the 12 analyses, and the renderer that adds counts, slots and anchors. The renderer checks that every paragraph has exactly one tag per sentence and that each paper's hand and rule layouts agree |

## Summary

| Layout | Old guide count (n=40, list never saved) | Re-done hand count (n=40) | Rule v3 (n=40) | Rule v3 after supplement (n=47) | Finance / accounting (n=47) | Median paragraphs |
|---|---:|---:|---:|---:|---:|---:|
| A Linear | 15 | 20 | 21 | **22** | 12 / 10 | 15 |
| B Design→result cycles | 11 | 8 | 8 | **9** | 7 / 2 | 15 |
| C Literature/gap first | 11 | 6 | 5 | **7** | 4 / 3 | 12 |
| D Theory/method-led | 3 | 6 | 6 | **9** | 8 / 1 | 16 |

- **Rule v3 agrees with hand assignment on 42/47 intros (89%):** 35/40 in the original sample and 7/7 in the supplement.
- **The regrouping rule printed in the guide (§1.1) agrees on only 18/40.**
- **D and B are mostly finance layouts:** 8 of 9 D papers and 7 of 9 B papers are in finance journals.
- **C is the rarest layout and the shortest:** median 12 paragraphs.

## A1. How the layouts were derived

### Provenance

The guide's counts (linear 15 / interleaved 11 / early positioning 11 / theory-led 3) came from the earlier session. The per-paper list behind them was never saved, and I could not reproduce it.

On 2026-10-20 I re-did the hand assignment of the 40 labelled intros. I read each label sequence and opened the text of every borderline case. The result, with one line of reasoning per paper, is in `layout/hand_layout_40.csv`. The new hand counts are 20 / 8 / 6 / 6.

### Hand definitions used today

- **A Linear.** One main design. Setup comes before results, and later result paragraphs refine the same estimate. Contributions come at the end.
- **B Design→result cycles.** At least two separate tests, each opened by its own design, data or event sentence and closed by its own result.
- **C Literature/gap first.** Before saying what it does, the paper spends at least one non-opening paragraph reviewing named prior work, or its measurement or data gaps. The this-paper sentence is then framed against that review.
- **D Theory/method-led.** The paper's own model or estimator (theory, structural model, new method) is laid out before any empirical result. Its predictions or outputs are what the paper sells.

### Label-sequence features

These are computed from `para_labels*.jsonl` only, so no corpus text is needed. X and V paragraphs are dropped first.

| Feature | Definition |
|---|---|
| `pos_before_tp` | Number of *positioning paragraphs* that meet three conditions: (1) not the opening paragraph; (2) before the first paragraph carrying `this_paper_statement`; (3) before the first data/design paragraph (D, E) and the first result paragraph. A positioning paragraph is either an L paragraph, or an H/Q paragraph with `named_papers` and `gap_explicit` but no `this_paper_statement`. |
| `model_pre` | Number of paragraphs with a `model_setup` or `model_result` slot that come before the first empirical result paragraph. An empirical result paragraph is coded F, M, A, K or R and carries no `model_result` slot. |
| `redesign` | Number of new design introductions after the first empirical result, each followed later by a result paragraph. A new design introduction is one of: (1) a D or E paragraph; (2) an F or A paragraph carrying `design_named`, `data_source_named`, `shock_named` or `setting_named`; (3) a K, R or C paragraph carrying `design_named` or `shock_named`. |

### Rule v3

The rule is checked in this order:
1. **C** if `pos_before_tp ≥ 1`.
2. **D** if `model_pre ≥ 2`.
3. **B** if `redesign ≥ 2`.
4. **A** otherwise.

C is checked before D because a theory or methods paper can also open with a review. The one case where this matters is ext_JFQA_a6a5f7a156, a methods paper that reviews the benchmark literature first: hand and rule both call it C.

### Agreement with hand assignment

**Original 40 intros, all three rule versions:**

Rule v1 vs hand (n=40)

| hand \ rule | A | B | C | D | total |
|---|---:|---:|---:|---:|---:|
| A | 8 | 5 | 2 | 5 | 20 |
| B | 4 | 3 | 1 | 0 | 8 |
| C | 0 | 0 | 5 | 1 | 6 |
| D | 4 | 0 | 0 | 2 | 6 |
| total | 16 | 8 | 8 | 8 | 40 |

Agreement: 18/40.

Rule v2 vs hand (n=40)

| hand \ rule | A | B | C | D | total |
|---|---:|---:|---:|---:|---:|
| A | 14 | 1 | 5 | 0 | 20 |
| B | 2 | 5 | 1 | 0 | 8 |
| C | 0 | 0 | 5 | 1 | 6 |
| D | 0 | 0 | 0 | 6 | 6 |
| total | 16 | 6 | 11 | 7 | 40 |

Agreement: 30/40.

Rule v3 vs hand (n=40)

| hand \ rule | A | B | C | D | total |
|---|---:|---:|---:|---:|---:|
| A | 18 | 2 | 0 | 0 | 20 |
| B | 2 | 6 | 0 | 0 | 8 |
| C | 1 | 0 | 5 | 0 | 6 |
| D | 0 | 0 | 0 | 6 | 6 |
| total | 21 | 8 | 5 | 6 | 40 |

Agreement: 35/40.

**All 47 intros, final rule:**

Rule v3 vs hand (n=47)

| hand \ rule | A | B | C | D | total |
|---|---:|---:|---:|---:|---:|
| A | 19 | 2 | 0 | 0 | 21 |
| B | 2 | 7 | 0 | 0 | 9 |
| C | 1 | 0 | 7 | 0 | 8 |
| D | 0 | 0 | 0 | 9 | 9 |
| total | 22 | 9 | 7 | 9 | 47 |

Agreement: 42/47.

Rule v2 used the same features but a looser C test: positioning before the first data/design paragraph, with no condition on the this-paper sentence and the opener allowed. It wrongly sent hook paragraphs that end on a gap into C.

### Definition changes made so that the rule reproduces the hand assignment

1. **C became "review before the this-paper sentence".** It used to be "a contribution paragraph before the first finding". That is what v1 tested, and it fired for 13/40 intros, many of which just have one related-literature paragraph inside the setup.
   - D6MACBVK states its aim in P1 ("This article investigates…") and reviews the literature in P2–P4, so under the new definition it is A. I kept it as a documented disagreement rather than editing the hand label.
2. **D now covers the paper's own estimator as well as its own theory.** Structural estimation (ext_RFS_7b88c84a64, QG8LS3GV) and "model + experiment" (ext_MS_934861ae69) are inside D. The count of T paragraphs no longer decides D: hypothesis-heavy empirical papers have three or more T paragraphs without any model, and v1 sent five of them to D.
3. **B needs two re-designs after the first result,** not just a "setup → results → setup" stage pattern. In v1 that pattern fired whenever a challenge or data paragraph followed a result.

### The five remaining disagreements (n=47)

| Paper | Hand | Rule | Why |
|---|---|---|---|
| NQE2BNAK | B | A | The second half of the paper analyses a different object, but the label carries no design slot |
| ext_JFE_1c18ebec73 | B | A | Results first, then model, data and three further tests; only one carries a design slot |
| D6MACBVK | C | A | The this-paper sentence is in P1; see change 1 above |
| R2IFDXFF | A | B | Its robustness paragraphs exploit smaller law changes, which is genuinely a second design |
| CV4WQZBR | A | B | Same pattern as R2IFDXFF |

Coding robustness designs differently would fix the last two but break 2AWVRR4R, whose B cycles run through R paragraphs.

## A2. Extra labelling so that every layout has at least 5 papers

Under rule v3 the original 40 already gave C = 5 and D = 6. That meets the floor, but only barely. To strengthen C and D, I screened the 77 unlabelled trusted intros with two simple signals:
- for C, author-year citations in the paragraphs before the first this-paper sentence;
- for D, model vocabulary ("our model", "equilibrium", "calibrat", "structural").

I then fully labelled 7 intros (97 paragraphs) in the same scheme as `labels/`: one function per paragraph, slots, and an abstracted opening. I read every paragraph in full.

| Key | Journal | Hand | Rule v3 | Note |
|---|---|---|---|---|
| ext_MS_1bc9bf323a | MS | C | C | Economics vs psychology views → "Can X motivate Y?" |
| TQMT9MWF | JFQA | C | C | Two nearest papers reviewed by name → "We add to this literature…" |
| QG8LS3GV | JFQA | D | D | Dynamic model → SMM counterfactuals → IV test |
| NJ8Y8ITJ | JFE | D | D | Theory of credit-line revocation → two identification strategies |
| ext_JAR_72b54520c1 | JAR | D | D | Pure theory paper. P6 is a footnote merged into the body and is coded X |
| ext_RFS_31424742a1 | RFS | B | B | Picked as a C candidate; on reading it is B (three test cycles) |
| ext_JF_da270ed7ca | JF | A | A | Picked as a C candidate; P3 is an identification critique *after* the question, so A |

New counts under rule v3 (n=47): **A 22, B 9, C 7, D 9.**

The screen for C has a low hit rate: 2 of 4 candidates were C. Many intros cite heavily before the this-paper sentence inside a hook or an identification paragraph, without a dedicated review paragraph.

### Members of each layout (rule v3, n=47)

- **A Linear (22):** NQE2BNAK (JF); ext_JF_9011e5a652 (JF); ext_JFE_bcd8b94113 (JFE); LZBRW8NQ (JFE); ext_JFE_1c18ebec73 (JFE); D6MACBVK (RFS); ext_RFS_6c41a0f14c (RFS); ext_JFQA_caec111127 (JFQA); ext_JFQA_df1532b5e8 (JFQA); AFN28PL4 (MS); ext_MS_abd98f40ff (MS); ext_JAR_a7cb1e6364 (JAR); V4AJ7JGF (JAR); ext_JAR_1c65ba10b9 (JAR); ext_JAR_195abab0ca (JAR); ext_TAR_c52333ac2b (TAR); ext_TAR_b4a079ca19 (TAR); ext_CAR_5a857eca7f (CAR); ext_CAR_26b2453b69 (CAR); ext_CAR_db12d3e5ea (CAR); ext_CAR_c861bb91bd (CAR); ext_JF_da270ed7ca (JF)
- **B Cycles (9):** ext_JF_8e897157c4 (JF); 2AWVRR4R (JFE); YNNGFJ8S (RFS); R2IFDXFF (JFQA); IUEMCEMW (MS); CV4WQZBR (MS); ext_JAR_abd9816b3e (JAR); ext_TAR_48e5248820 (TAR); ext_RFS_31424742a1 (RFS)
- **C Literature first (7):** Q4AXYECJ (RFS); ext_JFQA_a6a5f7a156 (JFQA); NBX8Q6DP (TAR); GRJQJX3B (TAR); ext_CAR_c54c74467b (CAR); TQMT9MWF (JFQA); ext_MS_1bc9bf323a (MS)
- **D Theory/method-led (9):** ext_JF_1f42ea1b72 (JF); 75KUPULP (JF); ext_JFE_bd61df5ea6 (JFE); ext_RFS_7b88c84a64 (RFS); ext_JFQA_ed0266bff2 (JFQA); ext_MS_934861ae69 (MS); QG8LS3GV (JFQA); NJ8Y8ITJ (JFE); ext_JAR_72b54520c1 (JAR)

## A3. Twelve full analyses (3 per layout)

### How I chose the papers

- Each paper's layout agrees under hand assignment and rule v3.
- The three papers for a layout come from three different journals.
- Paragraph rebuilds are clean. I dropped LZBRW8NQ (its P1 starts mid-sentence) and 75KUPULP (figure-axis text merged into P6).

### What each paper gets

- A table with one row per paragraph: function, sentence count, word count, and information slots.
- A move tag for every sentence. In total 900 sentences carry 76 distinct tags.
- One anchor excerpt per paragraph, at most 20 words.
- A closing note on why the paper is that layout and how it differs from the other layouts.

### Move tags

Tags follow the skeletons in `INTRO_TEMPLATE_zh.md` Chapter 2 as `card.move`. A tag from a different card than the paragraph's function marks a borrowed move; for example, `F.main-result` inside a challenge paragraph.

| Card | Moves |
|---|---|
| H (2.1) | topic, specifics, tension, turn, importance |
| Q (2.2) | known, unknown, nearest+limit, this-paper, why-works, answer-preview, goal, scope, scale |
| T (2.3) | thesis, chain, counterforce, prediction, model-setup |
| D (2.4) | purpose+data, measure, detail, merge, sample-size, setting-claim, advantage, summary, importance |
| E (2.5) | design-name, variation, comparison, exposure, FE, restriction |
| C (2.6) | threat, bias, stakes, response, result |
| F (2.7) | main-result, magnitude, where-stronger, interpretation |
| M (2.8) | restate, announce, standardize, benchmark, robust |
| A (2.9) | dimension, rationale, measure, result, close |
| K (2.10) | overview, channel, implication, test, verdict, detail |
| R (2.11) | acknowledge, announce, check, placebo, close |
| L (2.12) | count, strand, prior-paper, turn, this-paper, extension |
| P (2.13) | announce, current-practice, implication, lever |
| O (2.14) | opener, section, concludes |
| V (no card) | scope |

### What the 12 analyses show across layouts

- **The layout is decided in the first third of the intro.**
  - In A and B, the this-paper sentence comes in P1–P4.
  - C puts it after a named review (P3).
  - D follows it at once with model set-up paragraphs (P2–P5).
  - After that point, all four layouts use the same function cards.
- **B intros carry the design inside the result paragraphs.** In the three B papers, 9 of 20 result paragraphs (F/M/A/K/R) have an E-move in S1 or S2 ("We then analyze…", "Next, we exploit…"). The same holds for 0 of 10 in the A papers, 1 of 10 in C and 2 of 10 in D. In A, the design sits in separate paragraphs before the first result.
- **D intros spend more paragraphs on theory.** The three D papers have 7 T paragraphs, against 3–4 in each other layout, and 4 of the 7 end on a T.prediction move ("Therefore, the model predicts…").
- **The short verdict sentence appears in every layout.** Examples: "We find the opposite." (4 words), "We find results consistent with this prediction." (7), "The focus of these papers differs from ours." (8). They mostly close K, R and C paragraphs, as the guide says.

### A · ext_JF_da270ed7ca — JF 2017

**How Do Quasi‐Random Option Grants Affect CEO Risk‐Taking?**

- 13 paragraphs, 2222 words. Function sequence: `HTCQEEDEEFLLO`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 0, new designs after first result = 0 → **A** (hand: A).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 9 | 191 | trend, fact_number, named_papers, importance_claim, rq_explicit |
| 2 | theory/hypotheses | 5 | 152 | theory_argument, competing_predictions, named_papers |
| 3 | identification challenge | 9 | 256 | identification_threat_named, named_papers, gap_explicit, prior_lit_general |
| 4 | question/this paper | 7 | 114 | this_paper_statement, shock_named, design_named, named_papers |
| 5 | empirical design | 15 | 289 | design_named, measure_construction, setting_justification |
| 6 | empirical design | 9 | 175 | design_named, measure_construction, named_papers |
| 7 | data & setting | 8 | 207 | setting_justification, named_papers, scope_limit |
| 8 | empirical design | 5 | 99 | comparison_group, design_named |
| 9 | empirical design | 7 | 165 | comparison_group, design_named |
| 10 | main finding | 8 | 184 | main_result_direction, magnitude_pct, mechanism_channel, heterogeneity_dim |
| 11 | contribution/literature | 8 | 219 | contribution_strand_named, named_papers, difference_stated |
| 12 | contribution/literature | 6 | 134 | difference_stated, implication_for_practice |
| 13 | roadmap | 5 | 37 | section_list |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.specifics · S4 H.specifics · S5 H.specifics · S6 H.specifics · S7 H.specifics · S8 H.turn · S9 Q.unknown | S1: “Performance-sensitive pay for executives has surged over the last 30 years.” |
| 2 | S1 T.thesis · S2 T.counterforce · S3 T.chain · S4 T.counterforce · S5 T.prediction | S5: “Thus, the overall effect of option compensation on risk-taking is ultimately an empirical question.” |
| 3 | S1 C.threat · S2 C.threat · S3 C.bias · S4 C.stakes · S5 L.prior-paper · S6 L.turn · S7 C.stakes · S8 L.prior-paper · S9 C.stakes | S1: “Estimating the effect of options on risk-taking is difficult due to endogeneity issues.” |
| 4 | S1 Q.why-works · S2 Q.this-paper · S3 Q.why-works · S4 D.detail · S5 D.detail · S6 D.detail · S7 D.detail | S2: “In this paper, we exploit a natural experiment that delivers such variation.” |
| 5 | S1 E.variation · S2 E.design-name · S3 D.detail · S4 D.detail · S5 D.detail · S6 E.variation · S7 E.exposure · S8 C.threat · S9 C.bias · S10 C.response · S11 E.exposure · S12 E.exposure · S13 M.announce · S14 D.detail · S15 C.result | S2: “Our first instrumental variables strategy uses only CEOs on fixed-value plans.” |
| 6 | S1 E.design-name · S2 E.variation · S3 E.variation · S4 E.variation · S5 E.comparison · S6 E.variation · S7 C.threat · S8 C.response · S9 E.exposure | S1: “Our second instrumental variables strategy does not use the timing of cycle first years.” |
| 7 | S1 D.advantage · S2 D.advantage · S3 D.advantage · S4 V.scope · S5 V.scope · S6 C.threat · S7 V.scope · S8 D.summary | S4: “Nonetheless, we do not assume here that firms choose randomly between plans.” |
| 8 | S1 E.comparison · S2 D.detail · S3 C.threat · S4 C.response · S5 C.result | S1: “For our first instrument, we use fixed-value firms, for which option grants can increase only at regularly …” |
| 9 | S1 E.comparison · S2 E.variation · S3 E.variation · S4 E.comparison · S5 E.FE · S6 V.scope · S7 R.announce | S1: “For our second instrument, we focus on fixed-number firms.” |
| 10 | S1 F.main-result · S2 F.interpretation · S3 F.main-result · S4 F.magnitude · S5 K.verdict · S6 F.where-stronger · S7 A.result · S8 A.result | S3: “Overall, we find a significant positive effect of option compensation on risktaking, as measured by realized …” |
| 11 | S1 L.strand · S2 L.turn · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper · S6 L.turn · S7 L.turn · S8 L.turn | S2: “Relative to the existing literature, we also focus on a somewhat different research question.” |
| 12 | S1 L.this-paper · S2 D.detail · S3 D.detail · S4 L.this-paper · S5 L.extension · S6 L.extension | S1: “Our paper focuses instead on estimating the theoretically ambiguous overall net effect of option …” |
| 13 | S1 O.opener · S2 O.section · S3 O.section · S4 O.section · S5 O.concludes | S1: “The rest of the paper proceeds as follows.” |

**Why A, and how it differs.** Layout A, because one identification idea (multi-year option plans) carries every result: the intro sets up the question (P1), states the two-sided theory (P2), explains why existing estimates are biased (P3), says "In this paper, we exploit…" (P4), spends five paragraphs on the design (P5–P9) and only then reports all findings in one block (P10) before two contribution paragraphs. The second instrument is a second *source of variation for the same estimand*, introduced before any result, so the paper never cycles design→result→design as B does. P3 reviews named papers, but it does so as an identification critique after the question is already stated (rule feature `pos_before_tp` = 0), which is what separates it from C. The unusual part is the proportion: five design paragraphs and a single results paragraph at relative position 0.75, far later than the corpus median of 0.38.

### A · ext_TAR_c52333ac2b — TAR 2018

**Does Reporting Transparency Affect Industry Coordination? Evidence from the Duration of International Cartels**

- 12 paragraphs, 1650 words. Function sequence: `QTTEEFAARLLO`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 0, new designs after first result = 1 → **A** (hand: A).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | question/this paper | 5 | 146 | theory_argument, named_papers, gap_explicit, competing_predictions, setting_named, this_paper_statement |
| 2 | theory/hypotheses | 7 | 172 | theory_argument, named_papers, hypothesis_stated |
| 3 | theory/hypotheses | 7 | 160 | competing_predictions, theory_argument, named_papers |
| 4 | empirical design | 4 | 122 | hypothesis_stated, measure_construction |
| 5 | empirical design | 6 | 151 | measure_construction, named_papers, enumerated_findings |
| 6 | main finding | 7 | 177 | setting_named, design_named, main_result_direction, mechanism_channel, named_papers |
| 7 | additional results/heterogeneity | 3 | 101 | heterogeneity_dim, named_papers, theory_argument |
| 8 | additional results/heterogeneity | 5 | 194 | heterogeneity_dim, main_result_direction, scope_limit |
| 9 | robustness | 6 | 162 | robustness_list, identification_threat_named, design_named, fixed_effects, scope_limit |
| 10 | contribution/literature | 4 | 103 | first_claim, contribution_overview, contribution_strand_named, named_papers, difference_stated |
| 11 | contribution/literature | 5 | 119 | contribution_strand_named, named_papers, difference_stated, policy_implication |
| 12 | roadmap | 4 | 43 | section_list |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 Q.known · S2 H.tension · S3 Q.unknown · S4 Q.this-paper · S5 Q.why-works | S3: “While economic theory predicts that financial reporting transparency affects this trade-off, no prior evidence exists as …” |
| 2 | S1 T.thesis · S2 T.chain · S3 T.chain · S4 T.chain · S5 T.chain · S6 T.chain · S7 T.prediction | S7: “Thus, by decreasing contracting costs, reporting transparency may increase cartel duration.” |
| 3 | S1 T.thesis · S2 T.chain · S3 T.chain · S4 T.chain · S5 T.chain · S6 T.chain · S7 T.counterforce | S1: “Unlike debt and compensation contracts, implicit cartel contracts lack legal standing; instead, they depend upon self-enforcement …” |
| 4 | S1 T.prediction · S2 T.prediction · S3 E.variation · S4 E.exposure | S3: “We test these predictions using the requirement to report under internationally recognized accounting standards as our …” |
| 5 | S1 E.exposure · S2 E.exposure · S3 E.exposure · S4 T.counterforce · S5 E.exposure · S6 E.exposure | S1: “First, the disclosure literature shows that these accounting standards demand higher levels of disclosure than local …” |
| 6 | S1 D.purpose+data · S2 F.main-result · S3 F.interpretation · S4 K.channel · S5 K.test · S6 K.detail · S7 K.verdict | S2: “Using the Cox proportional hazard model, we find that reporting transparency is associated with a lower …” |
| 7 | S1 A.dimension · S2 A.rationale · S3 A.rationale | S1: “To further support the role of reporting transparency in cheating discovery, we exploit crosssectional variation in …” |
| 8 | S1 A.result · S2 K.test · S3 K.verdict · S4 V.scope · S5 V.scope | S1: “Using empirical proxies for the likelihood of cheating, we find that transparent reporting is associated with …” |
| 9 | S1 R.announce · S2 R.check · S3 R.check · S4 C.threat · S5 C.response · S6 R.check | S1: “We employ a battery of sensitivity checks to rule out alternative explanations for our results.” |
| 10 | S1 L.count · S2 L.strand · S3 L.prior-paper · S4 L.this-paper | S1: “As our paper is the first to provide evidence on how reporting transparency affects industry coordination …” |
| 11 | S1 L.strand · S2 L.this-paper · S3 L.strand · S4 P.implication · S5 P.implication | S1: “Second, our study adds to the literature on the verification role of audited financial statements (Ball …” |
| 12 | S1 O.opener · S2 O.section · S3 O.section · S4 O.concludes | S1: “The paper proceeds as follows.” |

**Why A, and how it differs.** Layout A in its accounting form: question and gap in P1 (走法甲 compressed into one paragraph: known → "no prior evidence" → "We exploit…"), then two theory paragraphs that build opposite predictions (P2 contracting benefit, P3 cheating discovery), the hypothesis and the treatment definition (P4–P5), one main finding (P6), cross-sectional support (P7–P8), robustness (P9) and a counted contribution block (P10–P11, "first … threefold"). There is a single design (transparent-standards indicator with a hazard model) and every later result conditions on it; the robustness paragraph changes estimators but does not open a new test, so the B criterion (≥2 new designs after the first result) is not met. Unlike C, the paper does not review named literature before saying what it does — the gap sentence is a one-line "no prior evidence exists" inside P1.

### A · ext_CAR_c861bb91bd — CAR 2019 (from file name)

**Do Consumers Pay the Corporate Tax?**

- 13 paragraphs, 2281 words. Function sequence: `QTDEMRAAKLLPV`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 0, new designs after first result = 1 → **A** (hand: A).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | question/this paper | 4 | 146 | prior_lit_general, gap_explicit, policy_context, named_papers, this_paper_statement |
| 2 | theory/hypotheses | 7 | 201 | theory_argument, named_papers, competing_predictions |
| 3 | data & setting | 7 | 234 | setting_named, setting_justification, fact_number, N_obs, named_papers |
| 4 | empirical design | 4 | 117 | design_named, comparison_group, N_obs, unit_named |
| 5 | magnitude | 8 | 238 | main_result_direction, magnitude_abs, magnitude_pct, magnitude_relative_benchmark, named_papers, scope_limit |
| 6 | robustness | 4 | 135 | robustness_list, named_papers, placebo_pretrend, design_named |
| 7 | additional results/heterogeneity | 13 | 276 | heterogeneity_dim, named_papers, enumerated_findings |
| 8 | additional results/heterogeneity | 6 | 209 | heterogeneity_dim, named_papers, validation_test |
| 9 | mechanism | 5 | 151 | mechanism_channel, named_papers, scope_limit |
| 10 | contribution/literature | 5 | 127 | contribution_overview, contribution_strand_named, named_papers, difference_stated, magnitude_pct |
| 11 | contribution/literature | 5 | 181 | named_papers, difference_stated |
| 12 | implications | 4 | 120 | policy_implication, fact_number |
| 13 | caveat/scope | 7 | 146 | scope_limit, future_research, fact_number |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 Q.this-paper · S2 Q.unknown · S3 Q.unknown · S4 Q.this-paper | S1: “Although prior literature on tax planning examines how firms reduce tax payments using various strategies, we …” |
| 2 | S1 T.thesis · S2 T.chain · S3 T.chain · S4 T.chain · S5 T.chain · S6 T.prediction · S7 T.counterforce | S6: “Collectively, these arguments predict that higher corporate taxes increase consumer prices.” |
| 3 | S1 D.setting-claim · S2 D.advantage · S3 D.detail · S4 D.advantage · S5 D.advantage · S6 D.advantage · S7 D.importance | S1: “We test these predictions in the setting of Germany’s retail gasoline market, where rich local tax …” |
| 4 | S1 E.design-name · S2 E.comparison · S3 D.sample-size · S4 E.FE | S1: “Empirically, we employ a staggered difference-in-differences (DiD) approach.” |
| 5 | S1 F.main-result · S2 M.benchmark · S3 V.scope · S4 M.benchmark · S5 M.benchmark · S6 F.where-stronger · S7 F.where-stronger · S8 V.scope | S1: “We find that a one percentage point increase in the local business tax rate raises gas …” |
| 6 | S1 R.check · S2 R.check · S3 R.placebo · S4 R.check | S1: “Our main result is robust to the inclusion or exclusion of controls, using a first-difference specification, …” |
| 7 | S1 A.dimension · S2 A.dimension · S3 A.dimension · S4 A.rationale · S5 A.measure · S6 A.measure · S7 A.measure · S8 A.rationale · S9 A.result · S10 A.result · S11 A.dimension · S12 A.result · S13 A.close | S2: “We examine two dimensions.” |
| 8 | S1 A.dimension · S2 A.measure · S3 A.result · S4 A.result · S5 R.check · S6 A.result | S3: “We find that gas prices respond considerably more to business taxes for gas stations facing less …” |
| 9 | S1 K.overview · S2 K.verdict · S3 K.verdict · S4 L.prior-paper · S5 V.scope | S1: “In a final step, we shed light on other real effects that would be consistent with …” |
| 10 | S1 L.count · S2 L.strand · S3 L.this-paper · S4 L.this-paper · S5 L.extension | S1: “Our findings contribute to the literature in two ways.” |
| 11 | S1 L.this-paper · S2 L.prior-paper · S3 L.this-paper · S4 L.extension · S5 L.extension | S1: “Second, we show that tax planning opportunities, tax enforcement, and other tax shields, as well as …” |
| 12 | S1 P.announce · S2 P.current-practice · S3 P.implication · S4 P.lever | S1: “Finally, our paper has policy implications.” |
| 13 | S1 V.scope · S2 V.scope · S3 V.scope · S4 V.scope · S5 V.scope · S6 V.scope · S7 V.scope | S1: “However, several caveats and limitations are in order when interpreting the implications of our results.” |

**Why A, and how it differs.** Textbook layout A and the closest match to the guide's 15-paragraph map: question (P1) → theory with a stated prediction and an "ex ante unclear" counterforce (P2) → setting with three numbered advantages (P3) → one staggered DiD (P4) → main finding with magnitude and benchmark (P5) → robustness (P6) → two heterogeneity dimensions (P7–P8) → real effects (P9) → counted contributions (P10–P11) → policy (P12) → caveats (P13). Everything after P5 refines the single estimate, so it is not B; the opening "Although prior literature on X examines A, we study B" states the paper's own question in its first sentence, so it is not C. It is also a clean example of the accounting habit of closing with a caveat paragraph (V), which only 12% of labelled intros have.

### B · ext_JF_8e897157c4 — JF 2022

**Common Risk Factors in Cryptocurrency**

- 11 paragraphs, 1446 words. Function sequence: `HQFEFMFFALL`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 0, new designs after first result = 2 → **B** (hand: B).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 9 | 185 | trend, two_views, importance_claim |
| 2 | question/this paper | 4 | 64 | this_paper_statement, sample_period, N_obs, unit_named |
| 3 | main finding | 3 | 63 | rq_explicit, main_result_direction |
| 4 | empirical design | 6 | 113 | prior_lit_general, measure_construction |
| 5 | main finding | 7 | 133 | design_named, main_result_direction, enumerated_findings, stat_significance |
| 6 | magnitude | 6 | 209 | magnitude_pct, magnitude_abs |
| 7 | main finding | 8 | 137 | main_result_direction, magnitude_pct |
| 8 | main finding | 6 | 114 | main_result_direction |
| 9 | additional results/heterogeneity | 9 | 189 | enumerated_findings, alt_explanation_ruled_out, heterogeneity_dim, robustness_list, magnitude_pct |
| 10 | contribution/literature | 7 | 132 | contribution_strand_named, named_papers |
| 11 | contribution/literature | 3 | 107 | contribution_strand_named, named_papers |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.specifics · S4 H.tension · S5 H.tension · S6 H.tension · S7 H.turn · S8 H.turn · S9 H.turn | S1: “The cryptocurrency market has experienced rapid growth.” |
| 2 | S1 Q.this-paper · S2 Q.goal · S3 Q.scope · S4 Q.scale | S1: “In this paper, we study the cross-section of cryptocurrency returns.” |
| 3 | S1 E.design-name · S2 F.main-result · S3 F.main-result | S1: “We examine whether the characteristics that are deemed important in the cross-section of equity returns are …” |
| 4 | S1 L.prior-paper · S2 E.exposure · S3 E.exposure · S4 E.exposure · S5 E.exposure · S6 D.sample-size | S1: “The literature on the stock market established a number of factors that explain the cross-section of …” |
| 5 | S1 E.design-name · S2 E.variation · S3 E.variation · S4 E.variation · S5 F.main-result · S6 F.main-result · S7 O.section | S1: “We then analyze the performance of all the 25 factors in the cryptocurrency market.” |
| 6 | S1 M.standardize · S2 M.standardize · S3 M.standardize · S4 M.standardize · S5 M.robust · S6 F.interpretation | S5: “For all of these factors, the returns on individual quintile portfolios are almost monotonic with the …” |
| 7 | S1 E.design-name · S2 F.main-result · S3 E.design-name · S4 E.design-name · S5 F.main-result · S6 F.main-result · S7 F.main-result · S8 F.main-result | S1: “Next, we investigate whether these nine cross-sectional cryptocurrency return predictors can be spanned by a small …” |
| 8 | S1 E.design-name · S2 F.main-result · S3 F.main-result · S4 F.main-result · S5 F.main-result · S6 F.interpretation | S6: “We conclude that the cryptocurrency three-factor model captures the cross-section of expected returns of cryptocurrencies.” |
| 9 | S1 A.dimension · S2 R.check · S3 R.check · S4 R.check · S5 A.result · S6 A.result · S7 R.check · S8 R.check · S9 A.rationale | S1: “Finally, we note several additional results.” |
| 10 | S1 L.strand · S2 L.strand · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper · S6 L.prior-paper · S7 L.prior-paper | S1: “We briefly discuss the relationship to the literature.” |
| 11 | S1 L.prior-paper · S2 L.prior-paper · S3 L.prior-paper | S1: “Yermack (2015) is one of the first papers that brings academic attention to the field of …” |

**Why B, and how it differs.** Layout B: after a hook with "two views" (P1) and a short this-paper paragraph with goal, scope and scale (P2), the intro runs three test cycles, each opened by its own design sentence and closed by its own result — characteristics as predictors (P3–P6: "We then analyze…", sort procedure, nine significant strategies, magnitudes), a one-factor model (P7: "Next, we investigate whether…"), and a three-factor model (P8: "We next show that…" → "We conclude that…"). There is no separate theory, data or identification block; the design is re-introduced inside each result paragraph, which is exactly the B signature (rule feature `redesign` = 2). Compared with A, there is no single main estimate that later paragraphs refine; compared with D, the factor model is an empirical spanning test, not the paper's own theoretical model. The literature comes last and is short (two paragraphs, no stated differences), as is common in asset-pricing B intros.

### B · ext_RFS_31424742a1 — RFS 2021

**Do Index Funds Monitor?**

- 13 paragraphs, 2083 words. Function sequence: `HQTTCFAKKKFAF`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 0, new designs after first result = 2 → **B** (hand: B).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 8 | 172 | trend, importance_claim, named_papers, rq_explicit, figure_reference |
| 2 | question/this paper | 4 | 88 | this_paper_statement, main_result_direction |
| 3 | theory/hypotheses | 4 | 113 | competing_predictions, theory_argument, named_papers |
| 4 | theory/hypotheses | 6 | 169 | competing_predictions, fact_number, named_papers, gap_explicit |
| 5 | identification challenge | 11 | 207 | identification_threat_named, design_named, fixed_effects, shock_named, named_papers, difference_stated |
| 6 | main finding | 9 | 245 | main_result_direction, magnitude_pct, named_papers, heterogeneity_dim |
| 7 | additional results/heterogeneity | 7 | 190 | heterogeneity_dim, magnitude_pct, named_papers |
| 8 | mechanism | 9 | 162 | mechanism_channel, alt_explanation_ruled_out, named_papers |
| 9 | mechanism | 5 | 148 | mechanism_channel, magnitude_pct, shock_named |
| 10 | mechanism | 5 | 120 | mechanism_channel, data_source_named, named_papers |
| 11 | main finding | 10 | 223 | main_result_direction, magnitude_abs, shock_named, design_named |
| 12 | additional results/heterogeneity | 3 | 114 | main_result_direction, difference_stated, named_papers |
| 13 | main finding | 7 | 132 | interpretation, main_result_direction |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.tension · S4 H.specifics · S5 H.tension · S6 H.turn · S7 Q.unknown · S8 Q.unknown | S7: “Specifically, to what extent do index funds monitor their portfolio companies?” |
| 2 | S1 Q.this-paper · S2 Q.answer-preview · S3 Q.answer-preview · S4 Q.answer-preview | S2: “We find that index funds monitor less than the active funds they are replacing.” |
| 3 | S1 T.thesis · S2 T.chain · S3 T.chain · S4 L.prior-paper | S1: “Two opposing forces could affect the monitoring behavior of index funds.” |
| 4 | S1 T.counterforce · S2 H.specifics · S3 T.chain · S4 T.chain · S5 Q.unknown · S6 Q.answer-preview | S5: “To date, the net effect of index investing on firm governance is unclear.” |
| 5 | S1 C.threat · S2 C.threat · S3 C.threat · S4 C.bias · S5 C.response · S6 C.response · S7 C.result · S8 C.response · S9 E.design-name · S10 C.response · S11 C.result | S1: “The main challenge in studying the effects of index fund investment is that holdings by active …” |
| 6 | S1 E.design-name · S2 L.prior-paper · S3 F.main-result · S4 F.magnitude · S5 F.interpretation · S6 F.interpretation · S7 F.where-stronger · S8 F.where-stronger · S9 F.interpretation | S1: “We start by examining the voting behavior of funds across all agenda items.” |
| 7 | S1 A.rationale · S2 A.dimension · S3 A.result · S4 A.result · S5 A.rationale · S6 A.rationale · S7 A.result | S1: “Arguably, not all votes are equally important.” |
| 8 | S1 F.interpretation · S2 K.channel · S3 K.channel · S4 K.overview · S5 K.test · S6 K.implication · S7 K.implication · S8 K.implication · S9 K.verdict | S2: “However, index funds could possibly monitor through other channels.” |
| 9 | S1 K.implication · S2 K.implication · S3 K.verdict · S4 K.verdict · S5 K.verdict | S3: “Yet we do not see a change in the number of either management or shareholder proposals, …” |
| 10 | S1 K.test · S2 D.detail · S3 K.verdict · S4 K.verdict · S5 L.prior-paper | S1: “We also examine publicly observable evidence of mutual funds’ intent to engage.” |
| 11 | S1 F.interpretation · S2 E.design-name · S3 E.design-name · S4 K.implication · S5 F.main-result · S6 F.magnitude · S7 K.detail · S8 R.check · S9 F.main-result · S10 F.interpretation | S5: “We find the opposite.” |
| 12 | S1 A.dimension · S2 F.main-result · S3 R.check | S3: “Importantly, we show that these nonresults are not due to limited statistical power; there is simply no effect.” |
| 13 | S1 F.interpretation · S2 F.main-result · S3 F.interpretation · S4 F.interpretation · S5 F.interpretation · S6 F.interpretation · S7 F.interpretation | S7: “As a result, when index fund ownership increases, corporate governance worsens.” |

**Why B, and how it differs.** Layout B with a front-loaded identification paragraph. P5 announces two designs at once (firm-by-year fixed effects for fund-level votes; a Russell-reconstitution DiD for firm-level outcomes), and the results then arrive in three cycles: voting behaviour (P6–P7), private and public engagement tests, each with its own implication and test (P8–P10), and governance consequences under the reconstitution design (P11–P12: "Next, we examine the consequences…"). Each cycle opens with the test's logic ("If index funds…, we would expect…") and closes with a short verdict ("We find the opposite." — 4 words). That rhythm separates it from A, where later paragraphs refine one estimate. It is not C because the two-sided theory (P3–P4) follows the this-paper sentence in P2. The intro has no contribution block at all, a strong sign that the RFS version moved related literature to a separate section; it ends with a summary paragraph (P13) that uses "Taken together", which shows the phrase is not banned in human writing, only rare.

### B · IUEMCEMW — MS 2026

**Debt Issuance in the Era of Passive Investment**

- 14 paragraphs, 2009 words. Function sequence: `HQRRRACKKTTLLL`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 0, new designs after first result = 3 → **B** (hand: B).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 6 | 169 | trend, fact_number, named_papers, theory_argument |
| 2 | question/this paper | 9 | 205 | this_paper_statement, shock_named, design_named, main_result_direction, magnitude_abs, fact_number |
| 3 | robustness | 5 | 125 | alt_explanation_ruled_out, design_named, enumerated_findings |
| 4 | robustness | 2 | 68 | design_named, comparison_group, heterogeneity_dim |
| 5 | robustness | 4 | 103 | design_named, comparison_group, main_result_direction |
| 6 | additional results/heterogeneity | 3 | 101 | heterogeneity_dim, main_result_direction |
| 7 | identification challenge | 4 | 132 | alt_explanation_ruled_out, named_papers, fact_number |
| 8 | mechanism | 5 | 144 | mechanism_channel, design_named, main_result_direction |
| 9 | mechanism | 3 | 110 | named_papers, mechanism_channel, interpretation |
| 10 | theory/hypotheses | 3 | 120 | model_setup, puzzle |
| 11 | theory/hypotheses | 7 | 222 | model_result, named_papers, magnitude_abs |
| 12 | contribution/literature | 6 | 181 | contribution_strand_named, named_papers, difference_stated, first_claim |
| 13 | contribution/literature | 6 | 183 | contribution_strand_named, named_papers, difference_stated |
| 14 | contribution/literature | 4 | 146 | contribution_strand_named, named_papers, difference_stated |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.specifics · S4 H.specifics · S5 H.tension · S6 H.turn | S1: “Recent decades have seen a dramatic shift towards low-cost passive investment strategies, with passive funds’ …” |
| 2 | S1 Q.this-paper · S2 Q.answer-preview · S3 E.variation · S4 D.detail · S5 F.main-result · S6 F.main-result · S7 F.main-result · S8 F.where-stronger · S9 F.interpretation | S1: “This paper looks at how passive investors’ demand affects corporate bond issuance.” |
| 3 | S1 R.check · S2 E.restriction · S3 E.restriction · S4 E.design-name · S5 R.close | S2: “The observed distribution of bond sizes is highly irregular and difficult to model with standard …” |
| 4 | S1 E.design-name · S2 F.where-stronger | S1: “Using difference-in-differences regressions, we also show that the shift in size clustering and the lower …” |
| 5 | S1 E.design-name · S2 E.variation · S3 E.comparison · S4 F.main-result | S1: “We reinforce these findings by examining refinancing decisions of firms whose bonds or loans mature …” |
| 6 | S1 A.dimension · S2 A.result · S3 A.result | S1: “We then examine the effects of issuers’ heterogeneous responses to the index threshold change, contrasting …” |
| 7 | S1 C.threat · S2 F.magnitude · S3 C.threat · S4 L.prior-paper | S1: “While our evidence suggests that firms’ bond issuance decisions are affected by bond indices, this …” |
| 8 | S1 K.test · S2 K.verdict · S3 K.verdict · S4 K.test · S5 K.verdict | S1: “We explore this possibility by looking at the correlation between bond sizes and the demand …” |
| 9 | S1 L.prior-paper · S2 K.verdict · S3 K.verdict | S3: “Given this evidence, it is doubtful that the almost complete disappearance of $250 million bonds …” |
| 10 | S1 T.counterforce · S2 T.thesis · S3 T.prediction | S1: “Yet if it is primarily passive investors that make bond indices important for issuing firms, …” |
| 11 | S1 T.prediction · S2 L.prior-paper · S3 T.prediction · S4 T.prediction · S5 T.prediction · S6 T.prediction · S7 V.scope | S1: “First, the model shows that when the passive investors with inelastic demand contribute a fraction …” |
| 12 | S1 L.strand · S2 L.prior-paper · S3 L.turn · S4 L.this-paper · S5 L.this-paper · S6 L.turn | S1: “Our paper is among the first to explore corporate financing implications of the rise of …” |
| 13 | S1 L.strand · S2 L.prior-paper · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper · S6 L.turn | S1: “We also contribute to the growing literature that examines the effects of ETFs and other …” |
| 14 | S1 L.strand · S2 L.turn · S3 L.extension · S4 L.extension | S2: “These studies have looked at passive demand in public equity markets, whereas we focus on …” |

**Why B, and how it differs.** Layout B in the "event first" form: P2 already contains the setting (a 2017 index-threshold change) and the headline result, and the following paragraphs add one test each, every one introduced by its own method sentence — a zero-inflated ordered probit (P3), difference-in-differences regressions (P4), refinancing needs as an instrument (P5), real effects (P6), demand-correlation and holdings tests for the passive-investor channel (P7–P9). Only after all the evidence does a stylized model appear (P10–P11) to reconcile magnitudes. The late model is what separates it from D: the rule counts model paragraphs only before the first empirical result (`model_pre` = 0). It is not A because no single estimate is refined; each paragraph brings a new design. The contribution block (P12–P14) is a model of "difference stated": each strand ends with a whereas-sentence.

### C · TQMT9MWF — JFQA 2014

**Asset specificity, industry-driven recovery risk, and loan pricing**

- 11 paragraphs, 1607 words. Function sequence: `HLQEDCEFFLO`.
- Rule v3 features: positioning-before-this-paper = 1, model paragraphs before first empirical result = 0, new designs after first result = 0 → **C** (hand: C).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 3 | 122 | theory_argument |
| 2 | contribution/literature | 10 | 192 | named_papers, prior_lit_general |
| 3 | question/this paper | 5 | 202 | this_paper_statement, theory_argument, named_papers, difference_stated |
| 4 | empirical design | 4 | 109 | measure_construction, validation_test |
| 5 | data & setting | 3 | 80 | data_source_named, N_obs, sample_period, hypothesis_stated |
| 6 | identification challenge | 6 | 168 | identification_threat_named, named_papers |
| 7 | empirical design | 11 | 245 | measure_construction, named_papers |
| 8 | main finding | 4 | 80 | main_result_direction, validation_test |
| 9 | main finding | 3 | 74 | main_result_direction, heterogeneity_dim |
| 10 | contribution/literature | 9 | 226 | contribution_overview, contribution_strand_named, named_papers, difference_stated |
| 11 | roadmap | 7 | 109 | section_list |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 T.chain · S3 T.chain | S1: “A potentially important factor affecting the liquidity of a firm’s assets is the financial condition …” |
| 2 | S1 L.prior-paper · S2 L.strand · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper · S6 L.prior-paper · S7 L.prior-paper · S8 T.chain · S9 T.chain · S10 L.prior-paper | S2: “Two recent papers empirically examine these issues.” |
| 3 | S1 Q.this-paper · S2 T.thesis · S3 T.chain · S4 T.prediction · S5 T.prediction | S1: “We add to this literature by examining the relationship of a firm’s exposure to industry …” |
| 4 | S1 E.exposure · S2 E.exposure · S3 E.exposure · S4 E.exposure | S1: “We begin our analysis by examining several potential measures of industry risk based on the …” |
| 5 | S1 D.purpose+data · S2 T.prediction · S3 D.sample-size | S1: “We next examine the relationship between various industry risk measures and bank loan pricing, line …” |
| 6 | S1 C.threat · S2 C.threat · S3 L.prior-paper · S4 C.bias · S5 L.prior-paper · S6 L.prior-paper | S1: “One challenge in analyzing the importance of industry risk is to distinguish between industry effects …” |
| 7 | S1 E.exposure · S2 E.exposure · S3 E.exposure · S4 E.exposure · S5 E.exposure · S6 E.exposure · S7 L.prior-paper · S8 L.prior-paper · S9 E.exposure · S10 E.exposure · S11 E.exposure | S1: “We examine the importance of industry risk using several measures.” |
| 8 | S1 F.main-result · S2 F.main-result · S3 F.where-stronger · S4 F.interpretation | S1: “Overall, we find a negative and significant relationship between recovery rates and our industry tail …” |
| 9 | S1 F.main-result · S2 F.where-stronger · S3 F.main-result | S1: “We find that all industry risk measures are significantly and positively related to the all-in-drawn …” |
| 10 | S1 L.count · S2 L.this-paper · S3 L.extension · S4 L.this-paper · S5 L.this-paper · S6 L.prior-paper · S7 L.turn · S8 L.this-paper · S9 L.extension | S1: “Our study contributes to the literature in several ways.” |
| 11 | S1 O.opener · S2 O.section · S3 O.section · S4 O.section · S5 O.section · S6 O.section · S7 O.concludes | S1: “The remainder of the paper is organized as follows: Section II discusses the data.” |

**Why C, and how it differs.** Layout C in its purest short form: a one-paragraph hook that is really a theoretical premise (P1), then a full paragraph that reviews the two nearest papers by name, each with what it examined and found (P2: "Two recent papers empirically examine these issues."), and only then the this-paper sentence, which is phrased as a contrast to that review ("We add to this literature by examining…", P3). After that the intro is linear (measures → data → challenge → results → counted contributions → roadmap). The literature paragraph is what decides the layout: it is not the opener and it comes before the first this-paper sentence and before any design paragraph (`pos_before_tp` = 1). Compared with A, the reader learns *whose* results are being extended before learning what the paper does; compared with B, there is one design (risk measures related to spreads and liquidity) rather than separate test cycles.

### C · ext_MS_1bc9bf323a — MS 2013

**Is Pay for Performance Detrimental to Innovation?**

- 14 paragraphs, 1762 words. Function sequence: `HLQTDETFAALLLL`.
- Rule v3 features: positioning-before-this-paper = 1, model paragraphs before first empirical result = 0, new designs after first result = 1 → **C** (hand: C).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 6 | 129 | prior_lit_general, named_papers, theory_argument |
| 2 | contribution/literature | 3 | 86 | two_views, named_papers, prior_lit_general |
| 3 | question/this paper | 5 | 108 | rq_explicit, this_paper_statement, design_named, main_result_direction, difference_stated |
| 4 | theory/hypotheses | 4 | 80 | theory_argument, named_papers |
| 5 | data & setting | 3 | 72 | setting_named, design_named |
| 6 | empirical design | 6 | 105 | design_named, comparison_group |
| 7 | theory/hypotheses | 4 | 80 | hypothesis_stated, theory_argument |
| 8 | main finding | 7 | 225 | main_result_direction, magnitude_pct, mechanism_channel |
| 9 | additional results/heterogeneity | 8 | 159 | main_result_direction, extension, theory_argument |
| 10 | additional results/heterogeneity | 6 | 178 | design_named, comparison_group, hypothesis_stated |
| 11 | contribution/literature | 5 | 143 | named_papers, difference_stated |
| 12 | contribution/literature | 6 | 122 | named_papers |
| 13 | contribution/literature | 5 | 111 | named_papers |
| 14 | contribution/literature | 7 | 164 | named_papers, contribution_strand_named |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 L.strand · S2 L.strand · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper · S6 L.turn | S2: “There is ample evidence supporting this thesis in different types of studies.” |
| 2 | S1 H.tension · S2 L.prior-paper · S3 L.prior-paper | S1: “In contrast, a substantial body of experimental and field research in psychology provides evidence that, in …” |
| 3 | S1 Q.unknown · S2 Q.this-paper · S3 Q.answer-preview · S4 L.turn · S5 L.turn | S1: “Can performance-based financial incentives motivate innovation in creative tasks?” |
| 4 | S1 T.thesis · S2 T.chain · S3 L.prior-paper · S4 T.chain | S1: “Innovation is the production of knowledge through experimentation (Arrow (1969), Weitzman (1979)).” |
| 5 | S1 D.setting-claim · S2 D.detail · S3 D.detail | S1: “In our experiment, subjects control the operations of a lemonade stand for 20 periods.” |
| 6 | S1 E.design-name · S2 E.comparison · S3 E.comparison · S4 E.comparison · S5 E.comparison · S6 E.comparison | S2: “The only difference across these treatment groups is the compensation offered to subjects.” |
| 7 | S1 T.prediction · S2 T.chain · S3 T.chain · S4 T.chain | S2: “Two features of the exploration contract encourage subjects to explore.” |
| 8 | S1 F.main-result · S2 F.magnitude · S3 K.overview · S4 K.detail · S5 K.detail · S6 K.detail · S7 K.detail | S1: “Our results provide strong support to the main hypothesis stated above.” |
| 9 | S1 A.dimension · S2 A.result · S3 A.rationale · S4 A.rationale · S5 A.dimension · S6 A.result · S7 A.result · S8 V.scope | S8: “Other explanations, such as pessimism about exploration, are also possible.” |
| 10 | S1 E.design-name · S2 E.comparison · S3 E.comparison · S4 T.prediction · S5 T.prediction · S6 F.magnitude | S1: “Finally, to study the effects of termination on innovation and performance, we introduce two new treatment …” |
| 11 | S1 L.prior-paper · S2 L.prior-paper · S3 L.prior-paper · S4 L.turn · S5 L.this-paper | S4: “These tasks, however, are inadequate to study incentives for innovation.” |
| 12 | S1 L.strand · S2 L.prior-paper · S3 L.prior-paper · S4 L.prior-paper · S5 L.turn · S6 L.turn | S5: “The focus of these papers differs from ours.” |
| 13 | S1 L.strand · S2 L.prior-paper · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper | S1: “Some other papers study the tension between exploitation and exploration in an experimental setting.” |
| 14 | S1 L.strand · S2 L.prior-paper · S3 L.prior-paper · S4 L.prior-paper · S5 L.prior-paper · S6 L.turn · S7 L.this-paper | S1: “Finally, several recent papers study the effects of incentives on innovation.” |

**Why C, and how it differs.** Layout C built on two opposed literatures: economics says pay-for-performance raises effort (P1, three named studies with one verb each), psychology says it undermines creative work (P2, "In contrast, a substantial body of…"). The question is then posed as the arbitration of that conflict ("Can performance-based financial incentives motivate innovation in creative tasks?", 9 words) and the answer is framed as contradicting both camps (P3, two "stands in contrast" sentences). Only then come the theory (P4), the experiment (P5–P6) and the hypothesis (P7). The layout is C because two positioning paragraphs precede the this-paper sentence; it differs from A in that the conflict between named literatures, not a phenomenon, motivates the paper; and from B in that the termination treatment (P10) extends the same experiment rather than opening a new design cycle. The four closing literature paragraphs each end with a sentence saying how this paper differs ("The focus of these papers differs from ours." — 8 words).

### C · GRJQJX3B — TAR 2024

**Do firms withhold loan covenant details?**

- 14 paragraphs, 1838 words. Function sequence: `HHQTDCMKRRRLLL`.
- Rule v3 features: positioning-before-this-paper = 1, model paragraphs before first empirical result = 0, new designs after first result = 0 → **C** (hand: C).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 3 | 67 | named_papers, importance_claim, policy_context |
| 2 | hook | 5 | 112 | named_papers, gap_explicit, quote |
| 3 | question/this paper | 7 | 199 | this_paper_statement, theory_argument, named_papers, hypothesis_stated |
| 4 | theory/hypotheses | 9 | 148 | competing_predictions, named_papers, enumerated_findings |
| 5 | data & setting | 5 | 108 | data_source_named, measure_construction, fact_number |
| 6 | identification challenge | 4 | 147 | identification_threat_named, named_papers, measure_construction, hypothesis_stated |
| 7 | magnitude | 5 | 79 | main_result_direction, magnitude_pct, magnitude_relative_benchmark, fixed_effects, robustness_list |
| 8 | mechanism | 8 | 256 | mechanism_channel, heterogeneity_dim, named_papers |
| 9 | robustness | 5 | 104 | alt_explanation_ruled_out, named_papers, measure_construction |
| 10 | robustness | 7 | 120 | alt_explanation_ruled_out, robustness_list |
| 11 | robustness | 3 | 69 | robustness_list, named_papers |
| 12 | contribution/literature | 6 | 162 | contribution_overview, contribution_strand_named, named_papers, difference_stated |
| 13 | contribution/literature | 4 | 145 | named_papers, gap_explicit, difference_stated |
| 14 | contribution/literature | 5 | 122 | contribution_strand_named, named_papers, gap_explicit |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.specifics | S1: “Private lenders rely on loan covenants to monitor and influence firm behavior …” |
| 2 | S1 Q.unknown · S2 L.prior-paper · S3 L.prior-paper · S4 L.prior-paper · S5 H.specifics | S1: “The importance of loan covenants notwithstanding, academic research has long found it difficult to obtain covenant details for …” |
| 3 | S1 Q.this-paper · S2 L.prior-paper · S3 L.prior-paper · S4 T.thesis · S5 T.chain · S6 T.chain · S7 T.prediction | S1: “In this study, we examine firms’ decision to withhold loan covenant details by focusing …” |
| 4 | S1 T.counterforce · S2 T.counterforce · S3 T.chain · S4 T.chain · S5 T.counterforce · S6 T.chain · S7 T.counterforce · S8 T.chain · S9 T.chain | S1: “However, counterarguments also exist.” |
| 5 | S1 D.purpose+data · S2 D.measure · S3 D.measure · S4 D.detail · S5 D.sample-size | S1: “We base our empirical analysis on a comprehensive sample of loans from DealScan.” |
| 6 | S1 C.threat · S2 C.response · S3 C.response · S4 T.prediction | S1: “Given that covenant details are usually unobservable for withheld loans, it is challenging to identify, …” |
| 7 | S1 M.restate · S2 M.standardize · S3 M.announce · S4 M.robust · S5 M.robust | S1: “We find results consistent with this prediction.” |
| 8 | S1 K.overview · S2 K.channel · S3 K.test · S4 K.test · S5 K.verdict · S6 A.result · S7 F.interpretation · S8 V.scope | S5: “We find results consistent with our expectations.” |
| 9 | S1 R.acknowledge · S2 R.acknowledge · S3 R.check · S4 R.check · S5 R.close | S5: “We find robust results using these alternative proxies.” |
| 10 | S1 R.acknowledge · S2 R.announce · S3 R.check · S4 R.check · S5 R.check · S6 R.check · S7 R.check | S2: “We explicitly check whether these factors subsume our findings.” |
| 11 | S1 R.check · S2 R.check · S3 R.check | S1: “In further robustness tests, we use alternative measures of covenant details withholding based on loan …” |
| 12 | S1 L.count · S2 L.this-paper · S3 L.turn · S4 L.this-paper · S5 L.extension · S6 L.prior-paper | S1: “Our study contributes to the disclosure literature in several ways.” |
| 13 | S1 L.turn · S2 L.prior-paper · S3 L.prior-paper · S4 L.this-paper | S1: “Second, the great majority of disclosure literature focuses on firm operating information, such as earnings, …” |
| 14 | S1 L.strand · S2 L.prior-paper · S3 L.prior-paper · S4 L.this-paper · S5 L.extension | S1: “Finally, our study also adds to the literature studying firm compliance with disclosure mandates.” |

**Why C, and how it differs.** Layout C in the accounting style: a three-sentence hook on why covenants matter (P1), then a paragraph that documents, with named papers and numbers, that researchers have long been unable to observe covenant details (P2: "academic research has long found it difficult to obtain…"), and only then "In this study, we examine…" (P3). The positioning paragraph is short, but it does the C job: it names whose data gaps motivate the question before the paper says what it does. After P3 the intro is linear with a strong robustness block (P9–P11) — the guide's 2.11 skeleton almost verbatim ("We acknowledge that…", "We explicitly check whether these factors subsume our findings.", one check per sentence). It differs from TQMT9MWF (also C) in that the review is about missing data rather than prior findings, and from A in that the gap is shown with evidence (DealScan coverage) instead of asserted.

### D · ext_RFS_7b88c84a64 — RFS 2015

**Equity Market Misvaluation Financing and Investment**

- 12 paragraphs, 1348 words. Function sequence: `QQTEFFKALLLO`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 2, new designs after first result = 0 → **D** (hand: D).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | question/this paper | 7 | 155 | this_paper_statement, fact_number, named_papers, rq_explicit |
| 2 | question/this paper | 6 | 120 | gap_explicit, named_papers, setting_justification |
| 3 | theory/hypotheses | 4 | 106 | model_setup |
| 4 | empirical design | 7 | 142 | model_setup, design_named |
| 5 | main finding | 4 | 93 | main_result_direction, heterogeneity_dim |
| 6 | main finding | 4 | 83 | main_result_direction, magnitude_sd |
| 7 | mechanism | 4 | 89 | interpretation, mechanism_channel |
| 8 | additional results/heterogeneity | 8 | 156 | extension, magnitude_pct |
| 9 | contribution/literature | 4 | 63 | contribution_strand_named, named_papers, difference_stated |
| 10 | contribution/literature | 5 | 131 | contribution_strand_named, named_papers, difference_stated, first_claim |
| 11 | contribution/literature | 9 | 154 | named_papers, difference_stated |
| 12 | roadmap | 7 | 56 | section_list |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 Q.this-paper · S2 H.importance · S3 H.specifics · S4 H.specifics · S5 H.tension · S6 H.tension · S7 Q.unknown | S1: “We estimate a dynamic model of investment and finance to understand and quantify the effects …” |
| 2 | S1 Q.known · S2 Q.unknown · S3 Q.why-works · S4 Q.this-paper · S5 Q.why-works · S6 Q.why-works | S2: “However, the literature lacks investigations of the quantitative importance of market timing.” |
| 3 | S1 T.model-setup · S2 T.model-setup · S3 T.model-setup · S4 T.model-setup | S1: “Our dynamic model captures decisions about a firm’s dividends, investment, net cash (cash net of …” |
| 4 | S1 T.chain · S2 T.chain · S3 T.chain · S4 T.chain · S5 E.design-name · S6 E.design-name · S7 E.design-name | S6: “We use simulated method of moments (SMM), which minimizes model errors by matching model generated …” |
| 5 | S1 F.main-result · S2 F.main-result · S3 F.main-result · S4 F.interpretation | S1: “We find that our model does a remarkably good job fitting many features of our …” |
| 6 | S1 E.design-name · S2 F.main-result · S3 F.main-result · S4 F.main-result | S1: “Next, we compute impulse response functions, which measure the responses of various policies to a …” |
| 7 | S1 K.verdict · S2 K.verdict · S3 K.verdict · S4 F.interpretation | S4: “We conclude that although equity misvaluation appears important for financial policies, its impact on real …” |
| 8 | S1 A.dimension · S2 A.dimension · S3 A.result · S4 A.result · S5 A.result · S6 A.result · S7 A.close · S8 A.result | S7: “In other words, misvaluation shocks help alleviate financial constraints.” |
| 9 | S1 L.count · S2 L.strand · S3 L.prior-paper · S4 L.turn | S1: “Our paper falls into several literatures.” |
| 10 | S1 L.strand · S2 L.prior-paper · S3 L.prior-paper · S4 L.prior-paper · S5 L.this-paper | S5: “Our results add to this research by providing the first quantitative evaluation of the effects …” |
| 11 | S1 L.prior-paper · S2 L.prior-paper · S3 L.turn · S4 L.prior-paper · S5 L.prior-paper · S6 L.prior-paper · S7 L.this-paper · S8 L.prior-paper · S9 L.turn | S3: “However, neither quantifies any effects of misvaluation.” |
| 12 | S1 O.opener · S2 O.section · S3 O.section · S4 O.section · S5 O.section · S6 O.section · S7 O.section | S1: “The paper is organized as follows.” |

**Why D, and how it differs.** Layout D, structural-estimation variant. The first sentence already names the method ("We estimate a dynamic model of investment and finance…"); P2 states the gap as the absence of *quantitative* evidence and argues why structural estimation fits an unobservable variable; P3 sets up the model (backbone plus the new misvaluation shock); P4 explains how the shock enters and how SMM identifies the parameters. Only then do results arrive, and they are the model's outputs: fit (P5), impulse responses (P6), their interpretation (P7) and counterfactuals (P8). Two model paragraphs before the first result put it in D (`model_pre` = 2). It differs from A, where theory motivates a reduced-form test, in that the model *is* the measuring instrument; and from C, in that the literature is introduced only as "many studies have tackled the question" before the gap, not reviewed by name.

### D · QG8LS3GV — JFQA 2024

**How does labor mobility affect corporate leverage and investment?**

- 10 paragraphs, 1268 words. Function sequence: `HQTTTFCDFO`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 5, new designs after first result = 0 → **D** (hand: D).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 5 | 132 | trend, named_papers, rq_explicit, this_paper_statement |
| 2 | question/this paper | 5 | 110 | this_paper_statement, model_setup, design_named, main_result_direction |
| 3 | theory/hypotheses | 10 | 152 | model_setup |
| 4 | theory/hypotheses | 5 | 99 | model_result, hypothesis_stated |
| 5 | theory/hypotheses | 3 | 83 | model_result, hypothesis_stated |
| 6 | main finding | 7 | 153 | model_result, magnitude_pct, design_named, policy_implication |
| 7 | identification challenge | 9 | 189 | identification_threat_named, data_source_named, measure_construction, shock_named, named_papers |
| 8 | data & setting | 8 | 134 | setting_justification |
| 9 | main finding | 5 | 131 | main_result_direction, interpretation |
| 10 | roadmap | 7 | 85 | section_list |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.turn · S4 Q.goal · S5 H.importance | S1: “In recent decades, human capital embedded in the skilled labor force has become an increasingly important …” |
| 2 | S1 Q.this-paper · S2 T.prediction · S3 Q.goal · S4 Q.this-paper · S5 Q.answer-preview | S1: “In this article, first, I set up a dynamic model to explore the mechanisms whereby labor …” |
| 3 | S1 T.model-setup · S2 T.model-setup · S3 T.model-setup · S4 T.model-setup · S5 T.chain · S6 T.model-setup · S7 T.model-setup · S8 T.model-setup · S9 T.model-setup · S10 T.chain | S3: “Two novel aspects of the model are critical in determining firms’ decisions.” |
| 4 | S1 T.prediction · S2 T.chain · S3 T.chain · S4 T.chain · S5 T.prediction | S1: “Overall, the model makes two sets of predictions about the effects of labor mobility on firm …” |
| 5 | S1 T.chain · S2 T.chain · S3 T.prediction | S3: “Therefore, the model also predicts that an increase in labor mobility that raises the frequency of …” |
| 6 | S1 E.design-name · S2 F.main-result · S3 F.magnitude · S4 F.magnitude · S5 F.magnitude · S6 F.interpretation · S7 P.implication | S1: “I estimate the model parameters using the simulated method of moments (SMM) and conduct counterfactual exercises …” |
| 7 | S1 E.design-name · S2 C.threat · S3 C.threat · S4 D.measure · S5 C.threat · S6 C.response · S7 D.detail · S8 D.detail · S9 E.exposure | S5: “Second, any measure of mobility is endogenously affected by firm policies.” |
| 8 | S1 D.setting-claim · S2 D.advantage · S3 D.advantage · S4 D.advantage · S5 D.advantage · S6 D.advantage · S7 D.summary · S8 C.result | S1: “Using IDD shocks as an instrument for labor mobility is empirically plausible.” |
| 9 | S1 F.main-result · S2 F.main-result · S3 F.where-stronger · S4 F.interpretation · S5 F.interpretation | S1: “Overall, the empirical tests confirm the model’s predictions.” |
| 10 | S1 O.opener · S2 O.section · S3 O.section · S4 O.section · S5 O.section · S6 O.section · S7 O.concludes | S1: “The rest of the article is organized as follows: Section II highlights the contribution of the …” |

**Why D, and how it differs.** Layout D, "model + test" variant. After a trend hook that ends in a goal statement (P1), P2 lays out the whole paper in two halves ("first, I set up a dynamic model… Next, I test and confirm…"). Three paragraphs then belong to the model: its set-up with two novel ingredients (P3, ten sentences with a median of 13.5 words) and two sets of predictions, each derived step by step and closed with "Therefore, the model predicts…" (P4–P5). Structural estimates and counterfactual magnitudes follow (P6), and only then the reduced-form test with its identification challenge and instrument defence (P7–P8) and the confirming results (P9). Five model paragraphs before the first empirical result make it unambiguous D. Compared with A, the theory is not a motivation for one regression but the source of numbered predictions and magnitudes; compared with B, the empirical half is a single IV test, not a series of designs. The literature review was moved out of the intro (the roadmap sends it to Section II), common in D papers.

### D · NJ8Y8ITJ — JFE 2014

**Credit lines as monitored liquidity insurance: Theory and evidence**

- 16 paragraphs, 2335 words. Function sequence: `HQTTTDEFRDFALLLO`.
- Rule v3 features: positioning-before-this-paper = 0, model paragraphs before first empirical result = 4, new designs after first result = 2 → **D** (hand: D).

| # | function | sent. | words | information slots |
|---:|---|---:|---:|---|
| 1 | hook | 6 | 159 | named_papers, puzzle, two_views |
| 2 | question/this paper | 3 | 78 | this_paper_statement, gap_explicit, model_setup |
| 3 | theory/hypotheses | 7 | 181 | model_setup, model_result |
| 4 | theory/hypotheses | 4 | 117 | model_result |
| 5 | theory/hypotheses | 7 | 181 | model_setup, model_result, extension |
| 6 | data & setting | 5 | 115 | hypothesis_stated, data_source_named, sample_period |
| 7 | empirical design | 6 | 151 | shock_named, design_named, named_papers, setting_justification |
| 8 | main finding | 4 | 154 | main_result_direction, magnitude_pct, comparison_group, placebo_pretrend |
| 9 | robustness | 9 | 214 | alt_explanation_ruled_out, design_named, named_papers, main_result_direction |
| 10 | data & setting | 3 | 90 | measure_construction, data_source_named, named_papers |
| 11 | main finding | 5 | 209 | main_result_direction, magnitude_pct, interpretation |
| 12 | additional results/heterogeneity | 8 | 257 | validation_test, named_papers, magnitude_relative_benchmark |
| 13 | contribution/literature | 2 | 90 | named_papers, difference_stated |
| 14 | contribution/literature | 7 | 151 | named_papers, difference_stated |
| 15 | contribution/literature | 6 | 137 | contribution_strand_named, named_papers, difference_stated |
| 16 | roadmap | 3 | 51 | section_list |

Sentence roles and anchors:

| # | sentence moves | anchor (≤20 words) |
|---:|---|---|
| 1 | S1 H.topic · S2 H.specifics · S3 H.specifics · S4 H.tension · S5 H.tension · S6 H.tension | S4: “Nevertheless, the results in Sufi (2009) challenge the notion that credit lines have perfect …” |
| 2 | S1 Q.this-paper · S2 T.prediction · S3 Q.why-works | S1: “We propose and test a theory of corporate liquidity management that bridges the gap …” |
| 3 | S1 T.model-setup · S2 T.chain · S3 T.chain · S4 T.chain · S5 T.chain · S6 T.chain · S7 T.prediction | S1: “In the model, a fully committed credit line (that is, full and irrevocable liquidity …” |
| 4 | S1 T.chain · S2 T.chain · S3 T.prediction · S4 T.chain | S2: “In equilibrium, firms may then choose to switch to cash holdings if the …” |
| 5 | S1 T.model-setup · S2 T.chain · S3 T.chain · S4 T.chain · S5 T.chain · S6 T.chain · S7 T.prediction | S1: “We extend the model to allow firms to demand liquidity not only to …” |
| 6 | S1 T.prediction · S2 D.purpose+data · S3 D.sample-size · S4 D.detail · S5 D.detail | S2: “We test these predictions using a novel dataset on credit lines from Capital …” |
| 7 | S1 E.design-name · S2 E.variation · S3 D.advantage · S4 L.prior-paper · S5 D.detail · S6 D.detail | S2: “We first exploit the downgrade of General Motors (GM) and Ford in 2005 as …” |
| 8 | S1 F.main-result · S2 F.magnitude · S3 F.main-result · S4 R.placebo | S4: “A placebo test in a period outside of the downgrade episode reveals no such effect.” |
| 9 | S1 C.threat · S2 C.threat · S3 C.response · S4 E.exposure · S5 L.prior-paper · S6 E.variation · S7 T.chain · S8 F.main-result · S9 F.interpretation | S2: “While we find this possibility implausible, we cannot entirely rule it out given that …” |
| 10 | S1 E.design-name · S2 E.exposure · S3 E.exposure | S1: “Next, we provide novel evidence linking corporate hedging needs to liquidity management and credit …” |
| 11 | S1 F.main-result · S2 F.magnitude · S3 F.main-result · S4 F.interpretation · S5 F.interpretation | S1: “In line with the predictions of our model, we find that low-hedging needs firms …” |
| 12 | S1 A.dimension · S2 A.dimension · S3 A.result · S4 A.result · S5 A.result · S6 A.result · S7 A.result · S8 A.close | S2: “Our main goal is to show that the Capital IQ data delivers results that …” |
| 13 | S1 L.prior-paper · S2 L.this-paper | S2: “Our theory and tests provide the new insight that credit line revocation following negative …” |
| 14 | S1 L.prior-paper · S2 L.prior-paper · S3 L.prior-paper · S4 L.turn · S5 L.this-paper · S6 L.this-paper · S7 L.extension | S4: “While we do not explicitly model the firm’s demand for derivatives, this result is …” |
| 15 | S1 L.strand · S2 L.prior-paper · S3 L.turn · S4 L.prior-paper · S5 L.prior-paper · S6 L.this-paper | S3: “In contrast, in our paper, the special role of the bank is to provide …” |
| 16 | S1 O.opener · S2 O.section · S3 O.section | S2: “Section 3 summarizes the empirical implications of the model.” |

**Why D, and how it differs.** Layout D, "propose and test a theory" variant. The hook sets theory against evidence (P1: "Theory suggests… Nevertheless, the results in Sufi (2009) challenge…"), and P2 promises a theory that "bridges the gap". Three paragraphs then develop the model: the problem full insurance creates and why revocation solves it (P3), the equilibrium choice between cash and credit lines (P4), and an extension with growth opportunities (P5); each closes on a prediction. Only P6 turns to data. Within the empirical half the intro is B-like — two identification strategies for the first prediction (P7–P9) and a separate test for the second (P10–P11) — which shows that the D rule is checked before B for a reason: what readers meet first, and what the paper sells, is the model. Unlike C, the opening names Sufi (2009) as a challenge to theory, not as the nearest paper to be corrected; the difference statements are kept for the three closing literature paragraphs.

