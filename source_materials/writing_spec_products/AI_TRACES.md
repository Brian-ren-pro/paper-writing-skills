# AI-trace list (from round-7 judge rationales)

Sources (counted by `r8_traces.py`, counts in `ai_traces_counts.json`):
- **2W**: the 72 round-7 two-way cues (`round7/eval/answers/2w_*`). Each quotes one sentence of the original, which I hand-coded into one or more categories by that sentence.
- **QS**: the 60 quiz-split reasons (`round7/quiz_split/answers/*`, English and Chinese), coded by keywords.
- **PW**: the 72 round-7 pairwise reasons (`round7/eval/answers/pw_*`), coded by keywords. These describe what made the *losing draft* weaker.

Keyword coding is approximate: one reason can hit several categories, and a loose match (e.g. "具体") can overcount. Read the numbers as rough rank, not as exact rates.

## A. What the originals have and the drafts lack (judges' positive cues for O)

| # | Cue | 2W (of 72) | QS (of 60) | Do | Don't | Content-gated? |
|---|---|---:|---:|---|---|---|
| 1 | Author voice and evaluative asides ("this void is troubling", "the argument goes", "with that said") | 40 | 18 | Write one or two judgment sentences per intro where the author says why something matters, is surprising or is limited, using the Brief's own evaluation (I4). Hedge in the author's voice ("one can view…", "while our study is primarily descriptive…"). | Neutral reporting from start to finish; stock praise ("important insights"); inventing an opinion the Brief does not hold. | Wording only, unless I4 is given. With no I4, evaluate only what the Brief already says (its gap, its tension, its own limitation). |
| 2 | Step-by-step concept building: short definitional steps, each one sentence, that build a concept before the paper uses it ("Exiting is also a governance mechanism.") | 22 | 14 | When a concept is new to the reader, introduce it in 2–4 plain steps: what it is, what it does, why it matters here. One short sentence is allowed to land a key idea. | Packing the definition, its role and the paper's claim into one sentence; jumping to results before the reader knows the terms. | No: a way of ordering Brief content. |
| 3 | Concrete example or analogy (Apple vs Google bonds; 50% vs 90% market-share cities; the epigraph quote) | 11 | 23 | Put the example right after the abstract claim it illustrates, in one or two sentences. | Abstract claims only; inventing an example, a firm name or a number. | **Yes.** Only when the Brief gives one (I1, or a concrete fact elsewhere). |
| 4 | History or institutional background as narrative (how intermediaries evolved into HFTs; the 2017–18 Bitcoin forks) | 6 | 12 | Tell it as a short sequence: then → change → now, with dates where given, leading into the question. | A one-line "in recent years X has grown"; inventing dates or events. | **Yes.** Only from I2 or dated facts in the Brief. |
| 5 | Ideal-experiment framing ("the ideal variation would be to randomly add users…") | 4 | 0 | State the ideal experiment, say why it is unavailable, then show how the setting approximates it. | Calling the design "a natural experiment" with no reasoning. | **Yes.** Only from I3. |
| 6 | Literature woven into the argument and engaged, not listed ("The two papers differ in…"; "Contrary to our findings…") | 4 | 20 | Bring a cited paper in at the point where it supports or contrasts a step, with author as subject and its finding; say where results disagree when the Brief says so. | A citation dump or a separate "related literature" list of names; "some studies find X, others find Y" with no link to our claim. | No: wording and placement. Disagreement only if the Brief records it. |
| 7 | Natural, varied, uneven sentences and connectives (judges: "organic", "unhurried", "uneven sentences") | – | 39 | Mix lengths: a few short sentences, many 18–32 words, one long one per paragraph. Vary paragraph openings. | Every sentence 15–22 words with the same subject–verb–object shape; "First… Second… Third…" in every paragraph. | No. |
| 8 | Short punchy conceptual sentence | 6 | – | See 2: at most one per paragraph, used to land a concept. | Strings of short declaratives (that reads choppy; see B4). | No. |
| 9 | Human idiosyncrasy (a typo "as follow"; an awkward double negative in a footnote) | 5 | – | Nothing to copy. Not a rule. | Don't add errors on purpose. | – |
| 10 | PDF-extraction noise in O | – | 18 | Not a writing cue. Round 8 removes it from the originals (`orig_clean/`). | – | – |

## B. What gave a draft away against another draft (PW, of 72)

| # | Tell in the weaker draft | PW | Rule |
|---|---|---:|---|
| 1 | Repetition: the main finding, data description or a cited paper restated two or more times | 34 | Say each fact once. A recap paragraph before the roadmap is not allowed. |
| 2 | Mechanical listing: channels, citations or tests listed one after another | 27 | Connect items by their logic (because, so, by contrast), not by enumeration. |
| 3 | Cramming or run-ons: three or more findings in one sentence | 13 | Keep the cramming limit; one long sentence per paragraph, not five. |
| 4 | Notes-like text: fragments, labels, X/Y tags, leaked notes | 12 | Full sentences only; never copy cell labels or note syntax. |
| 5 | Front-loading theory or method, delaying the question and finding | 11 | Ask the question and preview the answer before the long theory or method blocks. |
| 6 | Factual slips (miscounts, misattribution) | 11 | Covered by Rule Zero. |
| 7 | Choppy or uniform declaratives | 9 | See A7. |
| 8 | Self-labelling and filler ("This is the paper's main finding"; "A reader who…") | 6 | Let evidence carry emphasis; no sentence that only announces the next. |
| 9 | Overclaiming ("unambiguously", "contradicts reality") | 5 | Match verb strength to the design. |

## What the rules may and may not do

- Every rule above shapes **how** Brief content is written. None adds a fact.
- Cues A3, A4, A5 and part of A1 need content: an example, a piece of history, an ideal experiment or the author's own evaluation. The writer uses them **only when the worksheet supplies them** (worksheet v4 cells I1–I4, or the same content elsewhere in the Brief). With no such content, the move is skipped; it is never invented.
- Cue A9 (typos) and A10 (PDF noise) are not rules.
