# English introduction guide card (v6, 2026-10-22)

Source: writing_spec rounds 5-10 (117 top-journal intros; 47 hand-labelled; blind-judge experiments). Full Chinese manual with worksheet: `source_materials/writing_spec_products/INTRO_TEMPLATE_zh.md` in the skills folder. Use with `language/en.md` and `language/ai-tone.md` section 4.

```text
INTRODUCTION GUIDE CARD (finance/accounting top journals) - v6, 2026-10-22
Basis: 117 top-journal intros (finance/accounting); 47 hand-labelled. Patterns below are corpus-attested (counts in PHRASE_BANK.md). v2 (after round 5): sentence-length targets, paragraph count scaled to length, patterns as skeletons, stricter Rule Zero. v3 (after round 6): we-led patterns, one fusion instruction per move, cramming limit, roadmap from H4, no absence statements. v4 (after round 7): AI-trace checklist (section 6), using Brief cells I1-I4. v5 (after round 8): sentence-length targets re-based on cleaned originals (fewer very long sentences); evaluation stays within the Brief. v6 (after round 9): section 7, plain-statement rules plus a writer-specific appendix built from round-9 judge reasons.

== RULE ZERO ==
This guide governs HOW, never WHAT; if the Brief lacks an item, skip that move, never invent it.
- Facts, numbers, citations, what a cited paper found, data, sample sizes, coefficients, test results, policy details and section titles: Brief only.
- No "first" claim unless the Brief supports it.
- A missing item gives a shorter paragraph or a dropped move. It never gives a filler sentence.
- A test with no result in the Brief is mentioned without a result, or not at all.
- Don't generalize a cited paper's limitation to "existing evidence" unless the Brief says so.
- Don't sharpen or soften magnitudes; use the Brief's own wording ("cuts by an order of magnitude" stays that, not "removes").
- Don't describe methods, tests or data steps beyond what the Brief states.
- Never state that the study lacks something (no shock, no control group, no test, no number) unless the Brief gives it as a finding.
- Evaluate only with the Brief's own judgment: an evaluative or bridging sentence may restate a Brief claim, never extend it to a new mechanism, cause, scope or timing.
- Never reuse a phrasing from this card verbatim; paraphrase and vary. The skeletons show structure, not wording.

== 1. BUDGET ==
- Paragraphs = target words / 125, rounded (1,000 words -> 8; 1,500 -> 12; 1,850 -> 15).
- About 125 words and 5 sentences per paragraph. Paragraph length stays flat; only the roadmap is short (about 55 words).
- "This paper" by the end of paragraph 2 (layout C: paragraph 3-4).
- First result about 35-45% of the way in.
- Contributions as one block near the end. Roadmap optional and last.
- When the budget gives fewer paragraphs than the layout map, merge adjacent rows; never drop a Brief item to save space. Examples:
  - Data/setting + design -> one paragraph: data source and sample, then the comparison and fixed effects.
  - Heterogeneity + mechanism -> one paragraph: the split, then what it says about the channel.
  - Two or three contribution strands -> one or two paragraphs, one strand per 2-4 sentences.
  - Theory 1 + theory 2 -> one paragraph: the chain, then the counterforce.

== 2. CHOOSE ONE LAYOUT ==
Counts are from 47 hand-labelled intros (rule v3; see LAYOUT_EVIDENCE.md). The maps below are for about 15 paragraphs; scale them with section 1.
A LINEAR (22 of 47). One main design; later results refine it.
  1 Hook | 2 Question + this paper | 3-4 Theory | 5 Data/setting | 6 Design | 7 Main finding + magnitude | 8 Identification challenge | 9 Heterogeneity | 10-11 Mechanisms | 12 Robustness | 13-15 Contributions (+policy) | (Roadmap)
B DESIGN->RESULT CYCLES (9 of 47). Two or more separate tests, each with its own design or data.
  1 Hook | 2 Question + this paper + one-line answer | 3 Shared data | 4 Design 1 | 5 Finding 1 | 6 Challenge to finding 1 | 7 Design 2 + finding 2 | 8 Detail | 9 Design 3 + finding 3 | 10 Robustness | 11-12 Mechanisms | 13-15 Contributions | (Roadmap)
  Result paragraphs open with what the new test uses, then what it finds.
C LITERATURE/GAP FIRST (7 of 47). Corrects or extends specific named papers.
  1 Hook | 2-3 Nearest papers, each finding stated, ending on the gap | 4 This paper against that review | 5 Data/setting | 6 Design | 7 Main finding + magnitude | 8 Heterogeneity | 9 Mechanism | 10 Robustness | 11-12 Short contributions | (Implications) | (Roadmap)
  Use C only if the Brief gives 2-5 nearest papers with their findings.
D THEORY/METHOD-LED (9 of 47). The paper's own model or estimator is the product.
  1 Puzzle | 2 This paper proposes [model] | 3 Model set-up | 4-6 One prediction per paragraph | 7 Estimation or test design | 8 Findings | 9 Counterfactuals | 10 Implications | 11-14 Literature | (Roadmap)
  Use D only if the Brief gives the model set-up and its results.

== 3. FUNCTION CARDS ==
Skeletons use <slots>; fill slots from the Brief and write your own words around them. AVOID = AI tells.

[H] HOOK (paragraph 1). JOB: a concrete fact, institution or tension; the last sentence turns to the gap.
- topic: <object> + <its role or size>, stated plainly | <date>, <event> | <standard theory> + <what it assumes>
- specifics: <object> + <share or amount> + <of what> | <Author (Year)> + <verb of finding> + <finding>
- tension: <contrast word> + <fact that cuts against the topic> | <two views>, each named in one clause
- turn: <what remains unknown> | <the question itself, asked directly>
AVOID: "In recent years, X has attracted increasing attention" (8 of 117 intros); importance adjectives with no number; ending without a turn.

[Q] QUESTION / THIS PAPER (paragraph 1-2). JOB: what the paper asks and what earlier work left open.
- we-led: <we> + <study / ask / exploit> + <object or setting>, then <we find> + <answer>
- fuse: question + setting in one sentence; answer + its scope in one sentence.
- gap route (accounting): <what prior work establishes, with cites> -> <what is not known> -> (<nearest paper> + <its finding> + <what it does not do>) -> <this paper> + <action> + <object> -> <why the setting can answer it> -> <answer preview>
- direct route (finance): <this paper studies object> -> <goal> -> <scope: units, period> -> <one scale number>
AVOID: a vague gap ("the literature remains limited"); repeating "this study aims to".

[T] THEORY (one or two paragraphs). JOB: one causal chain, ending in a prediction.
- thesis: <the hypothesis, in one clause> | <the number of reasons> + <why X may affect Y>
- chain, one step per sentence: <because A> + <B> | <A>, which in turn <B> | <if A> + <then B>
- counterforce: <contrast> + <mechanism pointing the other way> | <the sign is unclear ex ante>
- prediction: <therefore> + <predicted direction> (D: <the model predicts> + <result>)
- we-led: <we> + <hypothesize / argue / build a model in which> + <claim>
- fuse: two adjacent chain steps in one sentence when the second follows from the first.
AVOID: "may affect Y in several ways" with no steps; mechanisms the Brief does not attribute to the cited papers.

[D] DATA & SETTING. JOB: what data, which setting, and what the setting identifies.
- data: <purpose> + <data> + <source> -> <how the key variable is measured> + (<following Paper>) -> <what is merged> -> <final sample: N, units, period>
- setting: <setting> + <why it suits the question> -> <what makes timing or exposure plausibly exogenous> -> <what this lets us separate>
- we-led: <we> + <use / collect / combine / measure> + <data or variable>
- fuse: source + sample size + period in one sentence; measure + its precedent in one sentence.
AVOID: "comprehensive and novel dataset" in place of source and N.

[E] DESIGN. JOB: who is compared with whom, and where the variation comes from.
- <design name> -> <source of variation> + <cross-sectional exposure> -> <treated vs control, before vs after> -> <how exposure groups are built> -> <fixed effects> + <what they absorb>
- we-led: <we> + <compare / exploit / estimate> + <comparison>
- fuse: design + comparison group + event window in one sentence; fixed effects + what they absorb in one sentence.
AVOID: listing DiD, PSM, IV and entropy balancing in one sentence; "rigorous identification" with no comparison named.

[C] IDENTIFICATION CHALLENGE (usually after the main result). JOB: the threat, the bias, the response and its result.
- <the confound, named> -> <how it could produce the same pattern> -> <what it would do to the interpretation> -> <response> -> <result of the response, from the Brief>
- If the Brief gives no result for the response, state the response and stop.
- we-led: <to address this, we> + <response> + <result>
- fuse: threat + direction of bias in one sentence; response + its result in one sentence.
AVOID: "Endogeneity is a common concern"; a method name with no bias named.

[F] MAIN FINDING. JOB: direction first, then size.
- <signpost>, <direction of effect on outcome> -> <magnitude in raw units>, <relative to the sample mean or SD> -> <where it is stronger> -> <what it suggests>
- we-led: <we find that> + <direction> + <outcome>
- fuse: result + magnitude (raw and relative) in one sentence.
AVOID: "significantly improves" with no number; closing on "Taken together..." (11 of 117 intros use it at all); restating the question.

[M] MAGNITUDE (usually inside F). JOB: one scale plus one benchmark.
- <economic size claim, tied to a number> -> <raw effect>, <% of mean> -> <benchmark from the Brief>
- fuse: scale + benchmark in one sentence.
AVOID: "not only statistically but also economically significant" (0 of 117 intros); more than two scales for one result.

[A] HETEROGENEITY. JOB: a split that theory gives a reason for.
- <dimension> -> <why the mechanism implies a pattern on it> -> <proxy> -> <which group shows the stronger effect, and by how much> -> <implication>
- we-led: <we> + <split / interact / examine> + <dimension>
- fuse: dimension + theoretical reason in one sentence; stronger group + size in one sentence.
AVOID: dimensions with no reason; opening with Moreover/Furthermore/Additionally (under 1% of corpus paragraphs).

[K] MECHANISM (one channel per paragraph, or merged with A). JOB: test each channel; give a clear verdict, including channels you rule out.
- <the channel> -> <what it implies for observable Y and Z> -> <the test> -> <the verdict, from the Brief>
- Introduce the channels in your own words; vary how each paragraph opens.
- we-led: <we> + <test / examine> + <channel's implication>
- fuse: channel + its testable implication in one sentence; test + verdict in one sentence.
AVOID: listing channels without testing them; only supporting verdicts; "may potentially suggest".

[R] ROBUSTNESS (the shortest content paragraph). JOB: rule out the strongest alternatives briefly.
- <the alternative> -> <the check> + <its result> (one check per sentence) -> <placebo result, if in the Brief>
- we-led: <we> + <show / verify> + <that the result survives check>
AVOID: long lists of alternative measures and samples; "our robust findings".

[L] CONTRIBUTION (one strand per 2-4 sentences, about 4 named papers per strand). JOB: name the papers, say what each found, say how this paper differs.
- (<count of contributions>: 73% of accounting intros, 29% of finance) -> <strand> -> <Author (Year)> + <finding>, cited authors as subjects -> <how this paper differs: subject, measure, identification, conflicting result or new boundary> -> <our result in that strand>
- we-led: <we> + <contribute to / extend / complement> + <strand>
- fuse: cited paper + its finding + our difference in one sentence ("whereas", "while", "but").
AVOID: 4 or more citations in one parenthesis with no difference stated; "enriches our understanding"; cited findings not in the Brief; "To the best of our knowledge, we are the first" (5 of 117 intros).

[P] IMPLICATIONS. JOB: whose decision changes, or which reading of the literature changes.
- <who decides> -> <current rule, from the Brief> -> <what our result implies for it> | <the reading one might draw> -> <what our evidence shows instead>
AVOID: "valuable insights for policymakers, investors, and managers"; "should mandate" from correlational evidence.

[O] ROADMAP (in 44% of intros; last; about 55 words). Write it whenever the Brief gives section contents (H4); otherwise skip it.
- <proceeds-as-follows signal> -> one section per clause, naming its content only if the Brief gives it -> <the concluding section>
AVOID: "Sections 2 to 7 present the analyses"; meta-talk; a recap paragraph before it.

== 4. TRANSITIONS ==
- Body-paragraph openers (share of paragraphs): "Our [paper/results]..." 11%; "First,/Second,..." 7%; "To [verb]..., we..." 5%; "We then/also/further" 4%; "Finally," 3%; "Next," 2.5%; Moreover/Furthermore/In addition/Additionally under 1% in total.
- Turns per 1,000 words: sentence-initial However 0.84, While 0.37, In contrast 0.34, Although 0.31, Yet 0.11; mid-sentence ", but" 0.73, ", however," 0.23. Most turns come inside a paragraph, not at its start.

== 5. MICRO RULES ==
1. Sentence length (targets from cleaned published intros): mean about 21-25 words, SD about 9-11; at most about 15% of sentences under 12 words; about 3-4% over 40 (roughly one per 25-30 sentences).
   - Most sentences run 18-32 words.
   - At most one sentence under 12 words per paragraph, and many paragraphs have none.
   - Many paragraphs have one sentence over 30 words, typically a result with its magnitude or a design with its comparison; sentences over 40 words are rare.
   - Join a short follow-up to the sentence before it with a clause, not a new sentence.
   - Long sentences come from the fusion lines in section 3: result + magnitude, design + comparison group, cited paper + finding + our difference.
   - Cramming limit: never pack three or more separate findings into one sentence; two related findings joined by a contrast are fine.
2. Use "we" for research actions: about 15-20 we/our/us per 1,000 words; most data, design and result paragraphs have at least two we-led sentences. Use "I"/"my" for a sole author at the same rate. Use the passive only for data handling.
3. Match verb strength to the design:
   - DiD/IV/RD/experiment: "increases, the effect of";
   - panel OLS: "is associated with";
   - untested mechanism: "suggests";
   - one hedge per claim.
4. Citations: finance mostly uses narrative citations (author as subject); at most 3 papers per parenthesis; JAR style: Author [Year]; cite only Brief entries.
5. Numbers: raw unit first, then relative ("[k] bp, or [m]% of the sample mean of [mu]"); % for rates of change, percentage points for differences in shares.
6. Banned words: delve, landscape, realm, intricate, tapestry, pivotal, underscore, nuanced, "It is worth noting", "Interestingly". Never call your own paper "novel".
7. Never restate to add length. Length comes from Brief detail. A thin Brief gives a shorter intro.
8. Do not label your own sentences ("This is the central fact", "This is the mechanism we find"); let the evidence carry the emphasis.

== 6. AI-TRACE CHECKLIST ==
Blind judges told drafts from published intros by these cues. Check each before you finish. Content items (marked *) apply only when the Brief supplies that content; otherwise skip the move, never invent it.
1. Author voice: one or two sentences per intro where the author judges something (why the gap matters, what is surprising, what the result does and does not show), in a measured, first-person register. Use I4 when given; otherwise judge only what the Brief already states. Never stretch a judgment into a new cause, mechanism or scope.
2. Build concepts step by step: before using a concept the reader may not know, give it in 2-4 plain steps (what it is, what it does, why it matters here). One short sentence may land the key idea.
3. *Concrete example or analogy (I1): place it right after the abstract claim it illustrates, in one or two sentences.
4. *History or institutional background (I2): tell it as a short sequence (then, change, now) with the Brief's dates, leading into the question.
5. *Ideal experiment (I3): state the ideal experiment, why it is unavailable, and how the setting approximates it.
6. Weave the literature in: bring a cited paper in at the step it supports or contrasts, author as subject, with its finding; say where results disagree only if the Brief says so. No name lists.
7. Vary the rhythm: mix short, medium and one long sentence per paragraph; vary paragraph openings; avoid runs of same-shaped sentences and "First/Second/Third" in every paragraph.
8. Say each fact once: no restated findings, no recap paragraph, no sentence that only announces the next.
9. Connect, don't enumerate: link tests, channels and citations by their logic (because, so, by contrast), not as a list.
10. Question and answer before long theory or method blocks.
11. Full sentences only: no fragments, labels, cell names or note syntax.

== 7. STATE IT, DON'T STAGE IT ==
Round-9 judges still spotted drafts by how sentences were packaged, not by content. These rules change only packaging; they never add or remove a Brief item.
1. Open each paragraph with substance (a fact, a claim, a result, a cited finding), not with a sentence about what the paragraph will do or why the next point matters.
2. Each sentence should carry Brief content. Delete any sentence that only frames, announces, labels, sums up or restates what is already on the page.
3. End a paragraph on its last piece of content. No closing sentence that glosses or repeats the paragraph.
4. Before you output, reread every paragraph once against the writer note below and rewrite any sentence that breaks it.

```
