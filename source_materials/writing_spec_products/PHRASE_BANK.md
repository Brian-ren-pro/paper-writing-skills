# Phrasing bank for the intro function cards

2026-10-20. Corpus: the 117 trusted intros, with paragraphs rebuilt from the PDFs; 217,906 words, 8,661 sentences. Card and move numbers follow `INTRO_TEMPLATE_zh.md` §2.1–2.14.

**How to read a row**
- **template:** an abstract pattern; the [placeholders] are filled from the Brief, never invented.
- **n/117:** intros with at least one matching sentence.
- **per 1k:** matches per 1,000 intro words.
- **in-card:** among matches inside the 47 hand-labelled intros, the share that falls in a paragraph labelled with this card's function. It tells you how specific a phrase is to its card. A low value means the phrase is a general connective and also does other jobs.
- **excerpt:** one real example of at most 15 words, with its source key.

**How I matched**
- **Unit and text.** Each phrasing is one regular expression, searched sentence by sentence. Ligatures are normalised, and sentences are split by `rebuild_paras.sentences`. Every pattern is listed in `phrase/phrase_spec.py`, so any count can be re-run.
- **Case and position.** Matching is case-sensitive unless a pattern says otherwise. A leading `^` means the phrase must open the sentence.
- **Not function-aware.** A phrase is counted wherever it occurs in the intro. For "Section 2 describes …" that hardly matters; for "In particular, …" it matters a lot, and the in-card column shows that.
- **Lemma variants.** These are written into the regex as alternations (e.g. `show|shows|showed`). I did not use a lemmatiser.
- **Excerpt choice.** The excerpt comes from the shortest matching sentence in which the match starts within the first 8 words, so most excerpts begin at the sentence start. Ties are broken by hash, not by hand.
- **Dropped patterns.** 7 of 374 candidate patterns matched nothing and are left out, so every row below has n ≥ 1. The full candidate list is in the spec file.

**Caveats**
- A regex finds the surface form, not the move. A hit for "We find that" in a robustness paragraph is still counted under F.S1.
- n counts intros, so a phrase used five times in one paper counts once in n and five times in per 1k.

---


## 2.1 Hook / phenomenon (H)


### S1 — Topic sentence: the object or its change, no preamble  (7 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [Market/practice] has grown/surged/expanded (rapidly). | 3 | 0.01 | 50% of 2 | “Performance-sensitive pay for executives has surged over the last 30 years.” [ext_JF_da270ed7ca] |
| [X] is a central/key/major [tool/source] of/for [Y]. | 12 | 0.06 | 0% of 4 | “Although scope 3 emissions are the most important component of companies’ emissions in a number …” [ext_JFE_5da9e9053f] |
| Recent decades/years have seen [trend]. / Over the past [N] years, [X]. | 4 | 0.02 | 100% of 2 | “Over the past 30 years, venture capital (VC) has been an important source of financing …” [ext_JFE_5e081a5811] |
| Standard/Traditional [theory/models] assume/predict [X]. | 3 | 0.01 | 100% of 2 | “Standard models in finance suggest that prices should reflect such information, whether public or private, …” [Q4AXYECJ] |
| In [year] / In [month year], [concrete event]. | 7 | 0.03 | 40% of 5 | “In 2015, policymakers of 195 countries acknowledged this challenge in the Paris Agreement and committed …” [ext_RFS_0d795b73f0] |
| A long-standing/central question in [field] is whether [X]. | 8 | 0.04 | 40% of 5 | “A key question in this respect is how investors identify the firms to be divested …” [ext_JFE_5da9e9053f] |
| Theory suggests that [X] is [Y]. | 3 | 0.01 | 100% of 1 | “Theory suggests that contract incompleteness and limited enforceability reduce a firm’s access to external finance …” [ext_JFQA_9ba646b3d2] |

### S2-3 — Specifics: a number, an institutional detail, or how the literature sees it  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| As of [date], [N] [units] [do X]. | 3 | 0.01 | 67% of 3 | “As of 2008 nearly 40% of equity awards had performance vesting rather than simple time …” [ext_JF_da270ed7ca] |
| [X] accounts for [N]% of [Y]. | 6 | 0.03 | 67% of 3 | “… pre-crisis nonbank share accounts for 19.2% of the mean fall in loan prices through 2008.” [ext_RFS_4e49eccbe5] |
| [Agents] held $[N] trillion/billion of [X]. | 11 | 0.09 | 100% of 6 | “… evaluates an $11 billion policy designed to induce demand for housing through providing temporary tax …” [ext_JF_722bf1d0b7] |
| For example, [Paper] find that [X]. | 18 | 0.09 | 21% of 14 | “For example, Gneezy and Rustichini (2000) find that the effect of monetary incentives can be, …” [ext_MS_1bc9bf323a] |
| [Paper] (Year) show/document that [X]. | 42 | 0.33 | 13% of 31 | “Hellmann and Puri (2002) show that VCs are essential to the professionalization of startups.” [ext_JFE_5e081a5811] |

### S4 — Tension: two views, or a fact that contradicts S1  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| There are two (competing) views on [X]. The first ... The second ... | 2 | 0.01 | 50% of 2 | “There are two views on the cryptocurrency market.” [ext_JF_8e897157c4] |
| Yet [conflicting fact]. | 15 | 0.11 | 20% of 10 | “Yet, very little is known about how the supply of competent, qualified, and independent accountants …” [ext_JAR_e250d1b91b] |
| However, [X] has/is [contrary fact]. | 40 | 0.23 | 17% of 29 | “However, evidence on the effect of transparency on gender pay disparities on employee and firm …” [ext_JF_fce63bf6a1] |
| Strikingly/Surprisingly, [fact]. | 6 | 0.03 | 20% of 5 | “Strikingly, 9% of the overall respondents and 17% of the early-stage investors do not use …” [ext_JFE_5e081a5811] |
| On the one hand, [A]. On the other hand, [B]. | 10 | 0.05 | 0% of 3 | “On the one hand, institutional investors clearly want to take a proactive approach by divesting …” [ext_JFE_5da9e9053f] |
| Nevertheless, [Paper] challenge the notion that [X]. | 14 | 0.08 | 33% of 3 | “Nevertheless, in almost all countries, the majority of households do not invest in stocks (Gomes, …” [ext_RFS_36a2cc1f42] |

### S5-6 — Turn: why it matters and what is still unknown (often the question itself)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| However, [X] remains (largely) unexplored/unclear. | 7 | 0.03 | 40% of 5 | “However, their potential in economic applications remains largely unexplored.” [ext_JFE_1c18ebec73] |
| Little is known about [X]. | 5 | 0.03 | 0% of 1 | “Yet, very little is known about how the supply of competent, qualified, and independent accountants …” [ext_JAR_e250d1b91b] |
| It is (therefore) important to understand whether [X]. | 3 | 0.01 | 100% of 1 | “… investor’s perspective, it is important to understand the potential effect of media information dissemination on …” [APQ7HFHK] |
| Does/How/Why/To what extent [X]? (a direct question) | 15 | 0.09 | 25% of 4 | “To what extent do firms share rents with employees?” [ext_RFS_0834902bd3] |
| This raises the question of whether [X]. | 5 | 0.02 | 25% of 4 | “As a consequence, the rise of index investing raises fundamental questions about monitoring and governance.” [ext_RFS_31424742a1] |
| Given [prevalence], it is important to ask [X]. | 2 | 0.01 | 50% of 2 | “Given the prevalence of options and option-like compensation, it is important to understand if and …” [ext_JF_da270ed7ca] |

## 2.2 Research question / gap / this paper (Q)


### known — 走法甲 S1 What is known (with 1-2 citations)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Prior/Previous/Existing research establishes/shows [X]. | 33 | 0.21 | 29% of 14 | “Prior research includes papers 210 R .” [R5PZG7CS] |
| A large/growing/vast literature [examines X]. | 10 | 0.05 | 0% of 3 | “A large literature in economics and finance uses inflation disagreement as a measure of inflation …” [ext_JFE_baf49090a8] |
| As surveyed/documented in [Paper], [X]. | 9 | 0.04 | 25% of 4 | “As pointed out by March (1991), the central concern that arises when learning through experimentation …” [ext_MS_1bc9bf323a] |
| It is well known/established that [X]. | 24 | 0.11 | 17% of 12 | “… in fact, widely recognized that standard Bayesian updating is an imperfect positive model even when …” [ext_MS_934861ae69] |
| Recent [field] research finds a strong association between [X] and [Y]. | 4 | 0.02 | 0% of 1 | “Recent global survey evidence shows that such targeted investment programs may receive more political support …” [ext_RFS_0d795b73f0] |
| [Field] has long studied [X]. | 3 | 0.01 | 0% of 1 | “Management has long been recognized to be an important determinant of firm productivity in large …” [ext_MS_3fb4aac81b] |

### unknown — 走法甲 S2 What is not known (usually a short sentence)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| What is less (well) known is [Y]. | 1 | 0.00 | 100% of 1 | “What is less well known is how private debt contracting affects the information borrowers obtain …” [NBX8Q6DP] |
| There is little/limited evidence on [X]. | 11 | 0.05 | 50% of 4 | “However, there is no evidence that the effect of peer performance on CEO turnover is …” [ext_JF_a6dd7e44e3] |
| No prior evidence/study [X]. / None of these studies [X]. | 2 | 0.01 | 50% of 2 | “However, none of these studies directly addresses how managers learn from interactions with external parties …” [NBX8Q6DP] |
| [X] has received little attention. | 3 | 0.01 | 0% of 1 | “… forecasts, trade secrets, etc. The disclosure of firm financing details has received much less attention.” [GRJQJX3B] |
| So far/To date, however, [X]. | 7 | 0.04 | 25% of 4 | “To date, the net effect of index investing on firm governance is unclear.” [ext_RFS_31424742a1] |
| However, the literature lacks [X]. | 2 | 0.01 | 100% of 2 | “However, the literature lacks investigations of the quantitative importance of market timing.” [ext_RFS_7b88c84a64] |

### nearest — 走法甲 S3 The nearest paper and its limit (optional)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| The paper(s) most closely related to ours is/are [Paper]. | 11 | 0.05 | 0% of 3 | “My paper is most closely related to Roberts and Sufi (2009b), which examines a sample …” [FTSTQ6CH] |
| However, these studies/papers do not [X]. | 5 | 0.02 | 0% of 3 | “However, these findings alone do not directly demonstrate whether origination lenders’ participation is motivated by …” [IBY22NKV] |
| While [Paper] show [X], [limitation]. | 2 | 0.01 | 0% of 1 | “While Nigro, Jones, and Aydogdu [2010] examines lender reputation as a determinant to loan sales, …” [IBY22NKV] |
| [Paper] is one of the first papers to [X]. | 2 | 0.01 | 0% of 1 | “Yermack (2015) is one of the first papers that brings academic attention to the field …” [ext_JF_8e897157c4] |
| One important article is [Paper], which concludes [X]. | 1 | 0.00 | 100% of 1 | “One important article examining this issue is Houston, Lin, Lin, and Ma (2010), which concludes …” [R2IFDXFF] |
| A notable exception is [Paper], who [X]. | 1 | 0.00 | 0% of 1 | “A notable exception is Caskey, Huang, and Saavedra (2021), who study managers’ decisions to delay …” [GRJQJX3B] |

### this-paper — S1/S4 This-paper sentence  (7 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| In this paper/study/article, we [verb] [X]. | 44 | 0.22 | 85% of 13 | “In this paper, we demonstrate that variations in good and bad uncertainty have separate and …” [ext_JFE_4dca1fff6e] |
| This paper/study investigates/examines/studies [X]. | 16 | 0.08 | 50% of 10 | “This paper investigates whether company visits provide analysts with an informational advantage.” [ext_CAR_26b2453b69] |
| We study/examine/investigate whether [X] affects [Y]. | 19 | 0.10 | 25% of 12 | “We explore how biases in conversation promote superficially-appealing personal investing strategies, focusing on active versus …” [ext_JFQA_ed0266bff2] |
| We answer/address this question by [doing X]. | 4 | 0.02 | 50% of 2 | “We answer these questions by studying the relation between index fund ownership, monitoring, and corporate …” [ext_RFS_31424742a1] |
| We contribute to this debate by examining [X]. | 7 | 0.03 | 40% of 5 | “We contribute to this literature by providing evidence on the effects of information-sharing systems within …” [ext_JAR_3057882e19] |
| We propose and test a theory/model of [X]. | 2 | 0.01 | 100% of 1 | “We present a simple model that captures these findings.” [ext_JF_c5d99f716f] |
| Our paper asks: [question]? | 9 | 0.05 | 60% of 5 | “Our paper examines explicitly whether it is favorable or unfavorable information that is transmitted and …” [ext_JFQA_ed0266bff2] |

### why-works — 走法甲 S5 Why this approach can answer the question  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| To [identify/test X], we exploit/use [Y]. | 15 | 0.11 | 0% of 8 | “To overcome this challenge, we focus our analysis on Northern and Central Italy, where the …” [ext_JAR_9be80f48ca] |
| [Setting/data] allows us to [X]. | 44 | 0.32 | 12% of 25 | “… econometric approach allows us to quantify intra-month spillover effects between different sets of financial institutions.” [ext_JFQA_3cff6d2d67] |
| The key advantage of [this approach] is that [X]. | 12 | 0.08 | 0% of 7 | “A key advantage of using these two measures is that they allow us to capture …” [ext_JAR_9a4f3f291b] |
| Our setting/data has several features that [X]. | 8 | 0.04 | 0% of 6 | “We use a unique feature of the Chinese mutual fund dataset to construct a precise …” [ext_CAR_26b2453b69] |
| Unlike prior work, we observe [X] directly. | 2 | 0.01 | – | “… and disclosure-based measures are more directly linked to managers’ ex ante incentives to conceal bad …” [WB4BIHIC] |

### answer — 走法甲 S6 One-sentence answer preview  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We find that [X]. | 74 | 0.61 | 2% of 55 | “We find that users with trade declarations are two to three times more likely to …” [YNNGFJ8S] |
| We predict and find that [X]. | 2 | 0.02 | 25% of 4 | “We predict and find that borrowers’ RFDs following private loan issuance contain new risk information …” [NBX8Q6DP] |
| We show that [X]. | 38 | 0.25 | 12% of 16 | “We show that our results are robust to using alternative methods to reduce the dimensionality …” [ext_JF_5c81171dc3] |
| Our main/key finding is that [X]. | 4 | 0.02 | 0% of 2 | “Our primary result is that minority analysts do not participate on conference calls at the …” [ext_JAR_66da1c197f] |
| The answer is [yes/no]: [X]. | 1 | 0.00 | – | “The answer is yes: there is a strong negative relationship between a bank’s interest expense …” [ext_JF_c5d99f716f] |
| Overall, we find (no) evidence that [X]. | 3 | 0.01 | 33% of 3 | “Overall, we find a significant positive effect of option compensation on risktaking, as measured by …” [ext_JF_da270ed7ca] |

### goal — 走法乙 S2 Goal sentence  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our (primary) goal/aim/objective is to [X]. | 9 | 0.04 | 43% of 7 | “Our primary goal is to examine this market using standard empirical asset pricing tools.” [ext_JF_8e897157c4] |
| The goal of this article is to provide [X]. | 3 | 0.01 | 0% of 1 | “The goal of this paper is to try to fill these gaps.” [ext_MS_3c486f3e56] |
| We aim to/seek to [X]. | 2 | 0.01 | – | “We seek to elucidate the experimental main findings using insights from our preregistered postexperimental survey.” [ext_JAR_bd01ca84e2] |
| This paper aims/seeks to [X]. | 3 | 0.02 | 100% of 1 | “This paper seeks to fill this gap.” [ext_JFE_6aa819c88d] |
| We are interested in [X]. | 3 | 0.01 | – | “… on executives, we are interested in how transparency can affect wage and firm outcomes throughout …” [ext_JF_fce63bf6a1] |

### scope — 走法乙 S3 Scope: sample, period, unit  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [...] from [year] to [year] / between [year] and [year]. | 24 | 0.15 | 20% of 10 | “… of applications between 1995 and 2013 to U.S. Department of Energy (DOE) Small Business Innovation …” [ext_RFS_0834902bd3] |
| Our sample comprises/covers [N] [units]. | 14 | 0.07 | 0% of 7 | “Our sample contains information on 226,422 loan contracts and 100,000 credit lines issued by 94 …” [LZBRW8NQ] |
| We consider all [units] with [criterion]. | 1 | 0.00 | 100% of 1 | “We consider all of the coins with market capitalizations above one million dollars and their …” [ext_JF_8e897157c4] |
| Our analysis focuses on [market] in [country]. | 1 | 0.00 | 0% of 1 | “Our focus is on model specification, with a large dark matter measure indicating that the …” [ext_JF_1f42ea1b72] |

### scale — 走法乙 S4 One scale number  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| The number of [units] grew from [N1] in [year] to [N2] in [year]. | 2 | 0.01 | 50% of 2 | “The number of such coins grew from 109 in 2014 to 1,583 in 2018.” [ext_JF_8e897157c4] |
| [N] [units] worth $[V] [did X]. | 2 | 0.02 | 0% of 4 | “… of $250 million bonds after 2017 cannot be explained by changing firm characteristics or macroeconomic …” [IUEMCEMW] |
| [X] now accounts for more than [N]% of [Y]. | 14 | 0.08 | 14% of 7 | “We find that over two-thirds of the firm-day attention signal is common across the major …” [GHVLM4T6] |
| [Agents] are now the largest [holders] of [X]. | 1 | 0.00 | 0% of 1 | “… index funds are now the largest shareholders of many U.S. corporations Bebchuk and Hirst (2019b).” [ext_RFS_31424742a1] |

## 2.3 Theory / hypotheses (T)


### S1 — Thesis sentence (often very short)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our (central/main) hypothesis is (simple / that [X]). | 10 | 0.05 | 57% of 7 | “Our main argument is that when institutional investors already significantly overweight or underweight a stock, …” [ext_JFQA_caec111127] |
| There are [two] reasons why [X] may [Y]. | 6 | 0.03 | 50% of 4 | “There are several ways in which one could use the dark matter measure to facilitate …” [ext_JF_1f42ea1b72] |
| Theory suggests/predicts that [X]. | 3 | 0.01 | 0% of 1 | “Theory suggests that contract incompleteness and limited enforceability reduce a firm’s access to external finance …” [ext_JFQA_9ba646b3d2] |
| To motivate/derive our predictions, we draw on/combine [theory]. | 4 | 0.02 | 100% of 2 | “To derive our predictions, we combine theories explaining the sustainability of cartels with the literature …” [ext_TAR_c52333ac2b] |
| [Two] opposing forces could affect [X]. | 5 | 0.03 | 33% of 3 | “… two characteristics of organization capital predict two opposing effects on the cost of bank loans.” [VQAPHNLM] |
| We posit that [X]. | 13 | 0.07 | 29% of 7 | “We conjecture that the estimation performance of other traditional leverage determinants might also improve upon …” [ext_JFQA_9ba646b3d2] |

### S2-4 — Mechanism chain: one step per sentence, explicit causal links  (7 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Because [A], [B]. | 22 | 0.15 | 27% of 11 | “Because we observe only prices and not quantities sold, it is difficult to translate this …” [ext_CAR_c861bb91bd] |
| As a result/consequence, [X]. | 26 | 0.14 | 9% of 11 | “As a result, firms may not need to fully compensate employees.” [Q95QGBR4] |
| This, in turn, [X]. | 21 | 0.13 | 22% of 9 | “This, in turn, increases service supply in opening states and thus reduces CPA wages and …” [ext_JAR_e250d1b91b] |
| If [A], then [B]. | 21 | 0.13 | 47% of 15 | “If aggregate consumption cannot fully adjust to the increased consumption demand, then the real interest …” [ext_JFE_baf49090a8] |
| To the extent that [X], [Y]. | 10 | 0.05 | 33% of 3 | “To the extent such mispricing exists, overpricing should then be more prevalent than underpricing, and …” [ext_JFE_a3637d3a10] |
| [X], which (in turn) leads to [Y]. | 11 | 0.05 | 25% of 4 | “… incorporate their expectations about the beliefs of other decision makers, which leads to strategic uncertainty.” [8H4P44R8] |
| Thus/Therefore/Consequently/Hence, [X]. | 78 | 0.79 | 31% of 67 | “Thus, while stationarity yields a stochastic steady state in which we can compute unconditional moments …” [ext_RFS_0bfb759f2f] |

### S5 — Counterforce or boundary condition  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| On the other hand, [opposing mechanism]. | 20 | 0.09 | 67% of 6 | “On the other hand, professional and educational ties do not produce these negative effects on …” [ext_TAR_1ca72750ea] |
| However, counterarguments also exist. | 6 | 0.03 | 50% of 4 | “An alternative view of the evidence has been expressed by the burgeoning literature in behavioral …” [Q4AXYECJ] |
| Ex ante, it is unclear whether [X]. | 15 | 0.07 | 50% of 8 | “Thus, it is unclear why origination lenders participate in the secondary market and what effect …” [IBY22NKV] |
| [...] is ultimately an empirical question. | 5 | 0.02 | 100% of 1 | “Strictly speaking, our question is therefore an empirical question.” [ext_JAR_9a4f3f291b] |
| This effect is greater/stronger when [condition]. | 8 | 0.04 | 20% of 5 | “The effect is more pronounced for investment grade firms which, absent the change, would likely …” [IUEMCEMW] |
| However, [X] may also [opposite]. | 11 | 0.06 | 0% of 4 | “However, the rigorous verification of trade secret claims may not be feasible because it is …” [28TTDMNX] |

### S6 — Prediction sentence (H1 if numbered)  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We (therefore) hypothesize/predict/expect that [X]. | 37 | 0.32 | 27% of 33 | “Consequently, we predict higher credit losses with SECURED in the precrisis periods and lower losses …” [R2IFDXFF] |
| This leads to our [first] hypothesis / generates testable predictions. | 8 | 0.04 | 43% of 7 | “Based on this framework, we make the following empirical predictions.” [LZBRW8NQ] |
| Collectively/Together, these arguments predict [X]. | 1 | 0.00 | 100% of 1 | “Collectively, these arguments predict that higher corporate taxes increase consumer prices.” [ext_CAR_c861bb91bd] |
| Thus, by [mechanism], [X] may increase [Y]. | 1 | 0.00 | 100% of 1 | “Thus, by decreasing contracting costs, reporting transparency may increase cartel duration.” [ext_TAR_c52333ac2b] |
| Therefore, the model predicts that [X]. | 2 | 0.02 | 100% of 4 | “First, the model shows that when the passive investors with inelastic demand contribute a fraction …” [IUEMCEMW] |

## 2.4 Data & setting (D)


### S1d — 数据型 S1 Purpose + data  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| To test these predictions, we use/build [data]. | 9 | 0.05 | 67% of 3 | “To explore this question, we exploit the public revelation of the numerous sexual harassment allegations …” [ext_JAR_1c65ba10b9] |
| We use/collect a [unique/hand-collected] dataset of [N] [units]. | 4 | 0.02 | – | “We gather a sample of 8,112 sell-side analysts and 94,582 quarterly earnings conference calls between …” [ext_JAR_66da1c197f] |
| We base our (empirical) analysis on a sample of [X] from [source]. | 2 | 0.01 | 100% of 1 | “We base our empirical analysis on a comprehensive sample of loans from DealScan.” [GRJQJX3B] |
| Using [data/a large sample of X], we [Y]. | 8 | 0.04 | 25% of 4 | “Using detailed proprietary data on the bank-specific TLTRO uptakes, I show that there is no …” [ext_JFQA_df1532b5e8] |
| Our data come from [source]. | 1 | 0.00 | – | “… particularly when much of the superior information comes from ongoing correspondence between borrowers and banks.” [TMKNNX9B] |

### S2d — 数据型 S2 How the key variable is measured  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We measure [construct] using/by [method]. | 22 | 0.12 | 30% of 10 | “We classify each analyst as an ethnic minority or nonminority using a classification based on …” [ext_JAR_66da1c197f] |
| Our main proxy/measure for [X] is [Y]. | 2 | 0.01 | 100% of 1 | “Our main proxy for a firm’s withholding of loan covenant details is based on whether …” [GRJQJX3B] |
| Following [Paper], we [construct X]. | 7 | 0.04 | 0% of 1 | “Following Hunter et al. (2014), we assign the best-fit index of Cremers and Petajisto (2009) …” [ext_JFQA_b6e852bb40] |
| We define [X] as [Y]. | 2 | 0.01 | 0% of 1 | “We define our measure of economic dark matter using a general GMM framework (see Hansen, …” [ext_JF_1f42ea1b72] |
| [Measure] is based on [observed behaviour]. | 2 | 0.01 | 0% of 2 | “… tail risk measure is based on works by Acharya, Pedersen, Philippon, and Richardson (2010) on …” [TQMT9MWF] |

### S3-4d — 数据型 S3–4 Further detail: classification, sub-categories  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Specifically, [detail]. | 46 | 0.29 | 6% of 17 | “Specifically, we directly compare GPT-4’s conversational prompting approach with embedding-based supervised learning models trained on …” [ext_JFE_1c18ebec73] |
| In particular, [detail]. | 43 | 0.27 | 4% of 24 | “In particular, CIQ contains detailed information on the drawn and undrawn portions of lines of …” [NJ8Y8ITJ] |
| [Data] contains (detailed) information on [X]. | 7 | 0.03 | 100% of 1 | “In particular, CIQ contains detailed information on the drawn and undrawn portions of lines of …” [NJ8Y8ITJ] |
| We classify [units] into [categories]. | 8 | 0.04 | 0% of 3 | “We classify each analyst as an ethnic minority or nonminority using a classification based on …” [ext_JAR_66da1c197f] |

### S5d — 数据型 S5 Merge  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Finally, we merge [data A] with [data B]. | 18 | 0.10 | 25% of 8 | “For this purpose, we combine our hand-collected institutional information with microlevel data from Zephyr, covering …” [ext_JAR_abd9816b3e] |
| [Data] are matched to [Compustat/CRSP] using [identifier]. | 18 | 0.11 | 29% of 7 | “… also tightly linked with aggregate trading in the U.S. stock market, suggesting that these effects …” [YNNGFJ8S] |
| We also have access to [data] on [X]. | 8 | 0.05 | 33% of 6 | “Although we have access to granular price data, we also face data limitations as gas …” [ext_CAR_c861bb91bd] |
| [Data A] combined with [data B] allows [X]. | 5 | 0.02 | 0% of 2 | “… hypotheses that result from combining the presence of market-wide sentiment with the Miller short-sale argument.” [ext_JFE_a3637d3a10] |

### S6d — 数据型 S6 Sample size  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our (final) sample contains [N] [units] over [period]. | 8 | 0.04 | 100% of 2 | “Our sample contains information on 226,422 loan contracts and 100,000 credit lines issued by 94 …” [LZBRW8NQ] |
| [N] firm-year observations / loans / funds. | 16 | 0.08 | 40% of 10 | “… information on 226,422 loan contracts and 100,000 credit lines issued by 94 banks to a …” [LZBRW8NQ] |
| In our sample, [n] out of [N] [units] [X]. | 5 | 0.02 | 50% of 2 | “… elected in 43 out of 50 states and in many cases go on to run …” [ext_JAR_2f755d3317] |
| We label these [X] and the remaining [N]% [Y]. | 4 | 0.02 | 100% of 2 | “We label these as “disclosed” and the remaining 19.5% as “withheld” loans.” [GRJQJX3B] |

### S1s — 情境型 S1 Setting claim  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [Setting] is an ideal laboratory/setting to study [X]. | 8 | 0.04 | 100% of 1 | “… offer an attractive setting for studying the relationship between media coverage and the cost of …” [APQ7HFHK] |
| [Setting] provides/offers several advantages for [identification]. | 2 | 0.01 | 100% of 1 | “Relatedly, the cyberattack we study has several advantages relative to the more commonly analyzed shocks.” [ext_JFE_2afe764a4a] |
| We test these predictions in the setting/context of [market], where [X]. | 10 | 0.06 | 50% of 6 | “… results can also be viewed in the context of Diamond’s (1991) model of reputation acquisition.” [2HDLTFN8] |
| [Setting] is particularly appropriate/well suited for our purposes. | 3 | 0.01 | 67% of 3 | “Structural estimation is particularly useful in this situation because misvaluation is, by nature, unobservable.” [ext_RFS_7b88c84a64] |
| We study/focus on [setting] because [reason]. | 5 | 0.02 | 100% of 1 | “We focus on momentum not only because of the failure of rational models to explain …” [ext_RFS_5f866d83c4] |

### S2-3s — 情境型 S2–3 Advantages: exogenous timing, staggered rollout  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| First, [timing] is predetermined/exogenous. | 13 | 0.06 | 12% of 8 | “… based on quasi-random assignment of applications to patent examiners of varying leniency, highlights the profound …” [ext_JF_83a6ef3230] |
| The staggered nature/timing of [X] allows [Y]. | 10 | 0.07 | 12% of 8 | “The timing of when these steps occur is staggered across firms.” [ext_JF_da270ed7ca] |
| Second, we observe high-quality granular data on [X]. | 16 | 0.10 | 67% of 9 | “… particular, CIQ contains detailed information on the drawn and undrawn portions of lines of credit.” [NJ8Y8ITJ] |
| [X] varies across [units] / over time. | 7 | 0.03 | 25% of 4 | “Of course, s varies across banks (i.e., s i ).” [2AWVRR4R] |

### S4s — 情境型 S4 Summary: what the setting rules out  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| The identification strategy thus alleviates [concern]. | 26 | 0.18 | 15% of 13 | “Two characteristics of anti-Mafia police actions alleviate endogeneity concerns in our setting.” [ext_JAR_9be80f48ca] |
| This allows us to isolate [X] from [Y]. | 18 | 0.09 | 0% of 8 | “… able to isolate the economic benefits of patent rights from those of the underlying invention.” [ext_JF_83a6ef3230] |
| All of these factors support the exclusion restriction. | 1 | 0.00 | 100% of 1 | “All of these factors support the exclusion restriction assumption.” [QG8LS3GV] |
| As a result, [setting] provides a clean test of [X]. | 1 | 0.00 | 0% of 1 | “… provide a powerful test of whether transparent reporting has some contracting benefits in the cartel …” [ext_TAR_c52333ac2b] |

### S5-6s — 情境型 S5–6 Why the setting matters economically  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [Setting] is economically important: [N]. | 16 | 0.07 | 100% of 2 | “These findings are economically large and robust.” [ext_RFS_5f866d83c4] |
| [Market] is one of the largest [X] in the world. | 25 | 0.15 | 8% of 12 | “… emissions are the most important component of companies’ emissions in a number of industries (e.g., …” [ext_JFE_5da9e9053f] |
| Our findings can inform other settings because [X]. | 15 | 0.16 | 8% of 13 | “The samples from the other countries are quota-representative with respect to age and gender.” [ext_RFS_36a2cc1f42] |
| [X] amounts to [N]% of [GDP/total]. | 9 | 0.05 | 0% of 5 | “Nondiscretionary spending amounts to around two-thirds of a household’s budget (Gooding, 2011, 2017; Schanzenbach et …” [ext_CAR_c861bb91bd] |

## 2.5 Empirical design (E)


### S1 — Name the design (often under 10 words)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our main empirical strategy employs a difference-in-differences design. | 18 | 0.12 | 33% of 12 | “… use a difference-in-differences identification strategy based on BlackRock’s acquisition of Barclays Global Investors (BGI) in …” [ext_JF_1876e11382] |
| We use an instrumental variables approach. | 11 | 0.08 | 22% of 9 | “Our two instrumental variables strategies yield similar results across a range of firm outcomes.” [ext_JF_da270ed7ca] |
| We use a regression discontinuity design. | 1 | 0.01 | – | “One is the regression discontinuity design, permitting clear causal effects.” [ext_RFS_0834902bd3] |
| We conduct an event study around [event]. | 4 | 0.03 | 0% of 2 | “Finally, the event study figures support that treatment and control groups follow parallel trends before …” [ext_JAR_abd9816b3e] |
| Our (main/identification) strategy/approach [is X]. | 13 | 0.08 | 12% of 8 | “Our identification strategy is related to that of Billings, Klein, and Shi [2022], who also …” [ext_JAR_1c65ba10b9] |
| Empirically, we employ [design]. | 8 | 0.04 | 50% of 2 | “Empirically, we find evidence consistent with the premise that sophisticated investors are the investors most …” [2WRNCEX7] |

### S2 — Source of variation  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We exploit [policy change/shock] combined with [cross-sectional exposure]. | 13 | 0.06 | 33% of 6 | “In this paper, we exploit a natural experiment that delivers such variation.” [ext_JF_da270ed7ca] |
| [X] provides/generates exogenous variation in [Y]. | 11 | 0.13 | 0% of 14 | “Thus, identification of WTP for carbon mitigation requires exogenous variation in compensated quantities.” [ext_RFS_0d795b73f0] |
| We exploit a (quasi-)natural experiment [X]. | 8 | 0.04 | 20% of 5 | “… exploiting a natural experiment in the United States surrounding the BAPCPA and provide corroborating findings …” [R2IFDXFF] |
| [X] gives us two distinct sources of variation in [Y]. | 4 | 0.02 | 100% of 1 | “… plans give us two distinct sources of variation in the timing of option pay increases.” [ext_JF_da270ed7ca] |

### S3 — Who is compared with whom  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We compare [treated units] with [control units] before and after [event]. | 7 | 0.04 | 0% of 3 | “… leverage both before and after the IPO, and so do not reflect changes in financial …” [D6MACBVK] |
| treated firms ... control firms/group | 13 | 0.18 | 40% of 20 | “I effectively select a control group that has similar characteristics as the treated banks.” [ext_JFQA_df1532b5e8] |
| relative to [comparable firms in not-yet-treated cities] | 7 | 0.04 | 0% of 3 | “… are largely unaffected by private information-driven trading, we are better able to identify volatility arising …” [Q4AXYECJ] |
| In particular, we compare [A] with/to [B]. | 11 | 0.05 | 20% of 5 | “… research design, we compare employees in firms above the 35-employee threshold with employees in firms …” [ext_JF_fce63bf6a1] |
| We use [group] as a control group because [X]. | 1 | 0.00 | 100% of 1 | “… fixed-value firms as a control group because their option compensation must remain fixed despite changes …” [ext_JF_da270ed7ca] |

### S4 — How exposure is measured  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| To construct (our) exposure groups, we rely on [measure]. | 18 | 0.21 | 19% of 21 | “… reductions in exposure to issuers outside of Europe, even when non-European initial exposures are high.” [2WRNCEX7] |
| We measure treatment intensity by [X]. | 1 | 0.01 | 0% of 2 | “… that the treatment intensity (i.e. by how much the average yield of a bank’s securities …” [ext_JFQA_df1532b5e8] |
| Our instrument is [X] / an indicator for whether [Y]. | 1 | 0.01 | 100% of 2 | “Thus, our second instrument for the change in the value of options granted is the …” [ext_JF_da270ed7ca] |
| [Units] that relied on [X] in the pre-period are treated. | 2 | 0.01 | 0% of 3 | “… credit losses with SECURED in the precrisis periods and lower losses in the postcrisis period.” [R2IFDXFF] |
| [Exposure] is based on whether [X]. | 3 | 0.01 | 0% of 2 | “… details is based on whether the firm releases the full loan contract as an exhibit …” [GRJQJX3B] |

### S5 — Fixed effects and controls  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We include [unit × time] fixed effects to absorb [confound]. | 32 | 0.26 | 16% of 19 | “State-industry-year fixed effects ensure that my results are also not driven by temporal and/or state …” [ext_JAR_2f755d3317] |
| [FE] absorb/sweep out [unobserved heterogeneity / shocks]. | 10 | 0.05 | 33% of 6 | “… effects model sweeps out all borrower- and loan-specific factors, potential time-varying omitted bank-level variables could …” [ext_RFS_4e49eccbe5] |
| We control for [a rich set of characteristics]. | 14 | 0.09 | 43% of 7 | “Second, we control for industry, firm characteristics, and known risk factors, while neither study includes …” [ext_JFE_5da9e9053f] |
| Standard errors are clustered at the [level]. | 2 | 0.02 | 0% of 4 | “… that in the U.S. there is (much more pronounced) clustering at the Bloomberg index thresholds.” [IUEMCEMW] |

### S6 — Sample restriction (optional)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We restrict the sample to [X]. | 4 | 0.02 | – | “… as we broaden the industry definition and as we restrict the sample to small firms.” [ext_JF_a6dd7e44e3] |
| We exclude [units] because [confound]. | 4 | 0.02 | 0% of 2 | “We exclude microcaps (i.e., stock in the bottom size quintile of the NYSE sample) and …” [ext_JFE_b9bf60e662] |
| We focus on [subsample] to rule out [X]. | 40 | 0.22 | 17% of 18 | “In contrast, we focus on how broader interactions between visitors and companies that happen during …” [ext_CAR_26b2453b69] |
| Firms are excluded if [condition]. | 2 | 0.01 | 0% of 1 | “… test, with the factors that are excluded from the nested model serving as left-hand-side returns.” [ext_JFQA_a6a5f7a156] |

## 2.6 Identification challenge (C)


### S1 — Name the threat  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| One concern (with this interpretation) is that [confound]. | 14 | 0.07 | 100% of 7 | “The key threat to this design is the possibility that time-varying, place-specific shocks are correlated …” [ext_JF_722bf1d0b7] |
| The key empirical challenge in [X] is that [Y]. | 4 | 0.02 | 100% of 2 | “The main challenge is that a third omitted factor could affect both options and risk-taking.” [ext_JF_da270ed7ca] |
| Estimating [X] is difficult due to endogeneity. | 26 | 0.23 | 45% of 22 | “Two characteristics of anti-Mafia police actions alleviate endogeneity concerns in our setting.” [ext_JAR_9be80f48ca] |
| There are [three] potential concerns for identification. | 8 | 0.04 | 75% of 4 | “… focuses on three issues: the interpretation of transparency employed by ADKS, the existence of multiple …” [8H4P44R8] |
| Given that [X] is unobservable, it is challenging to [Y]. | 7 | 0.04 | 20% of 5 | “… covenant details are usually unobservable for withheld loans, it is challenging to identify, for all …” [GRJQJX3B] |
| It is possible that [omitted factor] drives both [X] and [Y]. | 6 | 0.03 | 50% of 2 | “… find that organization capital negatively affects both the total cost of borrowing and the AISU.” [VQAPHNLM] |

### S2 — Direction of the bias  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| That is, if [alternative], our estimates would be biased upward/downward. | 2 | 0.01 | 0% of 3 | “Higher volatility intensifies the effect of the selection bias toward high reports.” [ext_JFQA_ed0266bff2] |
| [...] would overstate/understate the effect. | 4 | 0.02 | 0% of 1 | “… because it attenuates the extent to which equity issuances and repurchases cause dilution and concentration …” [ext_RFS_7b88c84a64] |
| For example, if [firms anticipate X], they may [Y] exactly when [Z]. | 6 | 0.04 | 50% of 4 | “For example, if a manager had cycles starting in 1990 and 1992, we would predict …” [ext_JF_da270ed7ca] |
| In this case, [Y] may increase due to [X] or because [Z]. | 8 | 0.05 | 25% of 4 | “In this case, risk-taking may increase due to option pay or because the CEO is …” [ext_JF_da270ed7ca] |

### S3 — What it would do to the conclusion  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [...] would bias/confound the estimate. | 1 | 0.00 | – | “… variation alone would overstate WTP for carbon mitigation by a factor of 19 or more.” [ext_RFS_0d795b73f0] |
| As a result, [this design] is not ideal for isolating [X]. | 3 | 0.01 | 50% of 2 | “… experiment is not ideal for isolating the total net effect of options—for risk-averse managers, stock …” [ext_JF_da270ed7ca] |
| Thus, there is the potential for endogeneity due to [X]. | 1 | 0.00 | 100% of 1 | “Thus, there is the potential for endogeneity due to both omitted variables and reverse causality.” [ext_RFS_31424742a1] |
| [...] makes it difficult to interpret [X] causally. | 5 | 0.03 | 75% of 4 | “… it is challenging to identify, for all the loans in our sample, whether a firm …” [GRJQJX3B] |

### S4 — Response  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| To alleviate/address/mitigate this concern, we [method]. | 24 | 0.12 | 31% of 16 | “To overcome this challenge, we focus our analysis on Northern and Central Italy, where the …” [ext_JAR_9be80f48ca] |
| We address this (issue/concern) by [X]. | 9 | 0.04 | 100% of 4 | “We address this head on by conducting auditing exercises in two of the samples.” [ext_MS_3fb4aac81b] |
| We address these issues in two ways. First, [X]. | 15 | 0.07 | 25% of 8 | “Their approach differs in several ways from ours, including the empirical design, source of variation, …” [ext_RFS_0834902bd3] |
| We deal with this challenge by relying on [literature/proxy]. | 13 | 0.07 | 17% of 6 | “We bolster identification by exploiting a natural experiment in the United States surrounding the BAPCPA …” [R2IFDXFF] |

### S5 — Result of the response (usually short)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [...] yields the same conclusion / our results are unchanged. | 18 | 0.10 | 11% of 9 | “… that our results are robust to using alternative methods to reduce the dimensionality of h …” [ext_JF_5c81171dc3] |
| Our estimates remain highly stable across specifications. | 3 | 0.01 | 50% of 2 | “… our estimates remain highly stable, suggesting our results are not sensitive to influence by omitted …” [ext_RFS_31424742a1] |
| Our main results are confirmed. | 3 | 0.01 | 0% of 2 | “Our main results are confirmed, indicating that they are unlikely to be driven by unobserved …” [LZBRW8NQ] |
| We perform a number of tests that support this assumption. | 3 | 0.01 | 0% of 2 | “We perform a number of tests in the paper that support this assumption.” [ext_JF_da270ed7ca] |

## 2.7 Main finding (F)


### S1 — Main result direction  (7 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We find that [X] [increases/reduces] [Y]. | 74 | 0.61 | 40% of 55 | “We find that users with trade declarations are two to three times more likely to …” [YNNGFJ8S] |
| Our results/findings show/suggest that [X]. | 45 | 0.32 | 26% of 27 | “These results indicate that, although banks account for the risk-increasing aspect of organization capital through …” [VQAPHNLM] |
| Consistent with [H1/our hypothesis], we find that [X]. | 36 | 0.20 | 30% of 23 | “Consistent with my expectations, I find that noninnovative operators near water monitoring stations withhold less …” [28TTDMNX] |
| Using [design], we find that [X]. | 21 | 0.11 | 33% of 9 | “Using textual-analysis tools and extensive manual checks, we find full-text loan contracts in SEC filings …” [GRJQJX3B] |
| We document/show/demonstrate that [X]. | 43 | 0.29 | 16% of 19 | “We show that our results are robust to using alternative methods to reduce the dimensionality …” [ext_JF_5c81171dc3] |
| Our key finding is that [X]. | 4 | 0.02 | 50% of 2 | “Our primary result is that minority analysts do not participate on conference calls at the …” [ext_JAR_66da1c197f] |
| The paper reports three main findings. First, [X]. | 4 | 0.02 | 100% of 1 | “The article reports three main findings.” [D6MACBVK] |

### S2 — Magnitude (inside the result paragraph)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| A one-standard-deviation increase in [X] is associated with [k]% [change in Y]. | 17 | 0.13 | 67% of 6 | “… that a one-standard-deviation higher pre-crisis nonbank share accounts for 19.2% of the mean fall in …” [ext_RFS_4e49eccbe5] |
| [X] increases [Y] by [k]% / [k] bp. | 15 | 0.09 | 40% of 10 | “… firms increase by 0.3 percentage points more than for female employees in control firms, although …” [ext_JF_fce63bf6a1] |
| [k]%, relative to the sample mean of [μ]. | 10 | 0.06 | 25% of 4 | “… to 14% of the mean and 27% of the standard deviation of the bank capital …” [JUPGLBAB] |
| [k] basis points | 11 | 0.07 | 44% of 9 | “… spread of 205 basis points, loan amount of 200 million dollars, and maturity of 5.5 …” [FTSTQ6CH] |
| [Group A] are [k] times more likely to [Y] than [group B]. | 1 | 0.00 | 0% of 1 | “… bulls are 5 times more likely to follow a user with a bullish view of …” [YNNGFJ8S] |
| This results in an increase of [k]%, or [$V] per year. | 1 | 0.01 | 100% of 2 | “This results in an increase of 3%, or 190 million Euro per year, in the …” [LZBRW8NQ] |

### S3 — Second outcome / where the effect is stronger  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| The effect is particularly pronounced for [subgroup]. | 16 | 0.12 | 17% of 18 | “… average decline is more pronounced at the bottom and the middle of the wage distribution.” [ext_JF_fce63bf6a1] |
| [...] is concentrated among [X]. | 15 | 0.08 | 0% of 5 | “… cross-sectional tests show that entry declines are concentrated in states offering the least financial aid.” [ext_JAR_6281def7a8] |
| The effect is stronger/larger for [X]. | 12 | 0.06 | 14% of 7 | “The employee-level effect is smaller because larger firms naturally experience smaller effects.” [ext_RFS_0834902bd3] |
| We also find that [second outcome] [moves]. | 22 | 0.14 | 50% of 10 | “We also find that the increase in the number of reported segments is associated with …” [ext_TAR_c52333ac2b] |
| In addition, we find that [X]. | 10 | 0.05 | 33% of 6 | “In addition, we find that option pay has a modest and generally insignificant effect on …” [ext_JF_da270ed7ca] |

### S4 — Interpretation  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| These results suggest that [interpretation]. | 47 | 0.29 | 18% of 22 | “These results indicate that, although banks account for the risk-increasing aspect of organization capital through …” [VQAPHNLM] |
| This is consistent with the view/idea that [X]. | 20 | 0.10 | 30% of 10 | “… is also consistent with the notion that consumers do not understand kilograms of carbon as …” [ext_RFS_0d795b73f0] |
| Consistent with [Paper], [X]. | 2 | 0.01 | 50% of 2 | “Consistent with Dye (1985) and Jung and Kwon (1988), disclosure does not incur any explicit …” [ext_JAR_72b54520c1] |
| In other words, [restatement in plain terms]. | 14 | 0.09 | 9% of 11 | “In other words, a reorganization offers a firm a second chance at life.” [R2IFDXFF] |
| Thus, [X] appears to [Y]. | 13 | 0.07 | 33% of 3 | “… effect does not appear to be driven by a general pullback from all risky MMMFs.” [WNHVK3RH] |

## 2.8 Magnitude / economic significance (M)


### S1 — Restate direction (short)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We find results consistent with this prediction. | 3 | 0.02 | 33% of 3 | “We find results consistent with our expectations.” [GRJQJX3B] |
| Consistent with our first hypothesis, we find [X]. | 9 | 0.05 | 14% of 7 | “Consistent with our theory, we find that LLMs’ ability to discern the economic implications of …” [ext_JFE_1c18ebec73] |
| We find that a one percentage point increase in [X] raises [Y] by [k]. | 2 | 0.01 | 100% of 1 | “… market times, a one percentage point increase in the VaR of hedge funds is estimated …” [ext_JFQA_3cff6d2d67] |
| For the [significant strategies], a [long-short strategy] generates [k]% per week. | 1 | 0.00 | 0% of 1 | “… momentum strategy in the above median size group generates statistically significant 4.2 percent weekly returns.” [ext_JF_8e897157c4] |

### S2 — Announce economic significance (6-7 words)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| This effect is (also) economically significant/large. | 28 | 0.14 | 33% of 9 | “These findings are economically large and robust.” [ext_RFS_5f866d83c4] |
| The magnitude of this effect is [large]. | 19 | 0.13 | 0% of 6 | “We regard the magnitude of the estimated wage effect as economically meaningful, especially considering that …” [ext_JAR_e250d1b91b] |
| This estimate appears economically significant. | 1 | 0.00 | 100% of 1 | “Given our sample mean of 19.5% withheld loans, this estimate appears economically significant.” [GRJQJX3B] |
| The effect is large/sizable. | 2 | 0.01 | – | “This effect is sizable since a one-standard-deviation increase in the signal mitigates the effect of …” [ext_RFS_36a2cc1f42] |

### S3 — Standardise: % of mean or SD  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [k], i.e., [m]% of the sample mean. | 4 | 0.03 | – | “… equivalent to 14% of the mean and 27% of the standard deviation of the bank …” [JUPGLBAB] |
| [...] relative to its standard deviation / of a standard deviation. | 4 | 0.02 | 100% of 1 | “… banks, equivalent to 42% of the standard deviation of bank lending growth during the crisis.” [JUPGLBAB] |
| Given our sample mean of [μ], this estimate implies [m]%. | 1 | 0.00 | 100% of 1 | “Given our sample mean of 19.5% withheld loans, this estimate appears economically significant.” [GRJQJX3B] |
| Moving from the bottom to the top quintile of [X] is associated with [Y]. | 1 | 0.00 | 0% of 1 | “… from the bottom quintile to the top quintile of hedging-needs is associated on average with …” [NJ8Y8ITJ] |

### S4 — Convert or benchmark  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Since the average [unit] has [size], this amounts to [$] per [period]. | 6 | 0.04 | 0% of 3 | “… a reduction in trading costs of $192 million per year based on recent trading volumes.” [IBY22NKV] |
| This compares with [k′] in [Paper] / is comparable to [estimate]. | 1 | 0.00 | 0% of 1 | “… being acquired, in line with the findings of Auerbach and Reishus (1988), and influence overall …” [ext_JAR_abd9816b3e] |
| Our back-of-the-envelope estimate suggests [X]. | 2 | 0.01 | 100% of 1 | “A back-of-the-envelope calculation suggests that they do.” [ext_RFS_0834902bd3] |
| This increase is about the same as [benchmark]. | 8 | 0.04 | 0% of 3 | “This increase is about the same as total bank capital.” [75KUPULP] |

### S5 — Robustness in one sentence (optional)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| This result is robust to [FE/alternative estimators]. | 24 | 0.14 | 33% of 9 | “… our results are robust to using alternative methods to reduce the dimensionality of h t …” [ext_JF_5c81171dc3] |
| Our results are robust to including [industry, year, firm] fixed effects. | 10 | 0.06 | 25% of 4 | “… results are robust to using alternative methods to reduce the dimensionality of h t , …” [ext_JF_5c81171dc3] |
| When we use [method A, B and C], we also find [similar results]. | 2 | 0.01 | 100% of 1 | “When we use entropy balancing, propensity score matching, and an instrumental variable approach, we also …” [GRJQJX3B] |
| The effect persists over [several years]. | 41 | 0.26 | 5% of 20 | “… during the last financial crisis, the effect of market expectations on default risk gets substantially …” [NFQHN7C7] |

## 2.9 Additional results / heterogeneity (A)


### S1 — Sequence word + dimension  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We next/also examine whether the effect varies with [dimension]. | 17 | 0.08 | 0% of 4 | “Of course, s varies across banks (i.e., s i ).” [2AWVRR4R] |
| Next, we examine/explore [X]. | 22 | 0.11 | 18% of 11 | “Next, we examine the performance differences across LLMs within the same family to identify which …” [ext_JFE_1c18ebec73] |
| To understand [X], we exploit [three] sources of heterogeneity. | 5 | 0.03 | 50% of 4 | “… most robust source of heterogeneity is tenure, or the number of years an employee has …” [ext_RFS_0834902bd3] |
| We exploit cross-sectional variation in [X]. | 25 | 0.15 | 7% of 14 | “The cross-sectional analysis provides correlations without providing any evidence on causation.” [ext_MS_3fb4aac81b] |
| Second, we study [effect] exploiting heterogeneity in [X]. | 29 | 0.22 | 27% of 26 | “We also exploit heterogeneity in the transparency of (mandatory) local GAAP, the requirement that listed …” [ext_TAR_c52333ac2b] |
| We then examine [the effects on X]. | 12 | 0.06 | 40% of 5 | “We then investigate whether ethnic minority and nonminority analysts have similar rates of participation (i.e., …” [ext_JAR_66da1c197f] |

### S2 — Theoretical reason for the dimension  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [Theory/Paper] predicts that [dimension] should amplify/dampen the effect. | 15 | 0.07 | 0% of 6 | “… in finance suggest that prices should reflect such information, whether public or private, as well …” [Q4AXYECJ] |
| If [mechanism], we would expect [pattern]. | 13 | 0.09 | 17% of 12 | “For example, when we would expect a user to receive all-the-same-sentiment messages with probability 38%, …” [YNNGFJ8S] |
| The theoretical prediction is that [X]. | 3 | 0.01 | 100% of 1 | “In this section, I outline the theoretical predictions that motivate my empirical analysis.” [JUPGLBAB] |
| Because [X], [subgroup] should respond more. | 6 | 0.04 | 0% of 2 | “Moreover, the stocks in the short leg should be more overpriced when sentiment is high.” [ext_JFE_a3637d3a10] |

### S3 — How the dimension is measured  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We measure [dimension] using [proxy]. | 4 | 0.02 | 0% of 2 | “We measure information shocks to firm fundamentals using four different variables: cash-flow news (CF news), …” [ext_JFQA_b6e852bb40] |
| Using empirical proxies for [X], we find [Y]. | 3 | 0.01 | 50% of 2 | “Using measures of information asymmetry from the extant literature (the use of positive accruals and …” [NQE2BNAK] |
| [Proxy] serves as a proxy for [X]. | 22 | 0.11 | 25% of 8 | “We use two proxies for news, one based on stock return over a relatively short …” [ext_JFQA_caec111127] |
| We split the sample by/into [groups]. | 5 | 0.03 | 50% of 2 | “When splitting the sample based on key human capital intensity, firms in the top half …” [Q95QGBR4] |

### S4 — Result for the dimension  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We find that the effect is stronger when [condition]. | 19 | 0.10 | 50% of 10 | “This negative relationship is stronger on quarter-ends when banks’ balance sheet capacity is more constrained.” [A7CRD7NG] |
| [Subgroup] respond(s) more strongly. | 4 | 0.02 | 0% of 2 | “… and issuances respond more strongly to misvaluation shocks than they do to profit shocks, but …” [ext_RFS_7b88c84a64] |
| [X] matters more for [subgroup]. | 1 | 0.01 | – | “… notion that firm-level transparency matters most when other aspects of the firm’s environment increase uncertainty.” [IEB6M7CI] |
| We find no/little difference across [groups]. | 5 | 0.02 | 0% of 2 | “… that there are no differences in the conference call participation rates of the two groups.” [ext_JAR_66da1c197f] |

### S5 — Close (short)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| These results are consistent with our theoretical predictions. | 4 | 0.02 | 50% of 2 | “These results are consistent with our theoretical predictions.” [LZBRW8NQ] |
| These findings imply that [X]. | 22 | 0.11 | 20% of 5 | “These results indicate that, although banks account for the risk-increasing aspect of organization capital through …” [VQAPHNLM] |
| This supports the view that [X]. | 9 | 0.05 | 33% of 6 | “… prior evidence supports the hypothesis that boards filter industry and market shocks from firm performance …” [ext_JF_a6dd7e44e3] |
| Overall, [X] matters. | 2 | 0.01 | 0% of 1 | “Overall, the empirical tests confirm the model’s predictions.” [QG8LS3GV] |

## 2.10 Mechanism (K)


### S1 — Overview  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We consider and test [N] possible mechanisms. | 23 | 0.12 | 22% of 9 | “We also examine several other alternative explanations for the stock price reaction we document.” [ext_JAR_1c65ba10b9] |
| As a deeper test of the mechanism, we examine [X]. | 1 | 0.00 | 100% of 1 | “As a deeper test of the mechanism, I next examine how the psychological properties of …” [ext_RFS_6c41a0f14c] |
| To understand the mechanism/what drives [X], we [Y]. | 4 | 0.02 | 100% of 1 | “To shed light on the mechanisms behind the informativeness of the social signal, we explore …” [GHVLM4T6] |
| Next, we turn to the drivers of [X]. | 1 | 0.00 | 100% of 1 | “Next, we turn to the drivers of the return evidence that we document, which is …” [ext_JAR_1c65ba10b9] |
| We then conduct [three] cross-sectional tests to shed light on the mechanisms. | 3 | 0.01 | 100% of 1 | “To shed light on the mechanisms behind the informativeness of the social signal, we explore …” [GHVLM4T6] |

### S2 — Channel hypothesis  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We first test the hypothesis/possibility that [channel]. | 2 | 0.01 | 100% of 1 | “We first test the hypothesis that asset management companies use social media to reduce search …” [AFN28PL4] |
| The first class of explanation(s) is that [X]. | 8 | 0.06 | 50% of 6 | “The third hypothesis is that investor sentiment should not greatly affect returns on the “long-leg” …” [ext_JFE_a3637d3a10] |
| One possibility/explanation is that [X]. | 5 | 0.02 | 0% of 2 | “A possible explanation for my findings is that subsidies and corporate misconduct are both consequences …” [ext_JAR_2f755d3317] |
| [Agents] could possibly [act] through other channels. | 3 | 0.01 | 50% of 2 | “However, index funds could possibly monitor through other channels.” [ext_RFS_31424742a1] |

### S3 — Testable implication  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| According to/Under this hypothesis, [Y] should [rise] but [Z] should not. | 4 | 0.02 | 25% of 4 | “According to this alternative explanation, lending banks might offer the issuing firm an interest rate …” [D6MACBVK] |
| If [channel] drives the result, then [Y] should [Z]. | 5 | 0.02 | 33% of 3 | “If the bank’s loans and securities have a short duration, they will not appreciate enough …” [75KUPULP] |
| [...] predicts that [Y] should [rise] but [Z] should not. | 8 | 0.06 | 0% of 4 | “… that investor sentiment should not greatly affect returns on the “long-leg” portfolio of each anomaly.” [ext_JFE_a3637d3a10] |
| In other words, if [X], their tendency to [Y] should be [Z]. | 7 | 0.05 | 33% of 3 | “Moreover, the stocks in the short leg should be more overpriced when sentiment is high.” [ext_JFE_a3637d3a10] |

### S4 — Test  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| To test [these implications/whether X], we [analyze Y]. | 10 | 0.05 | 50% of 4 | “To test this prediction, I analyze the cueing effect of several types of firm events …” [ext_RFS_6c41a0f14c] |
| We explore this possibility by [looking at X]. | 4 | 0.02 | 33% of 3 | “We explore this possibility by looking at the correlation between bond sizes and the demand …” [IUEMCEMW] |
| We investigate [X] in two ways. First, [Y]. | 1 | 0.00 | 100% of 1 | “We investigate index funds’ private engagement in two ways.” [ext_RFS_31424742a1] |
| We focus on [subsample/agents] for whom [channel] should matter most. | 1 | 0.00 | 0% of 1 | “… focus on groups of banks for which economically the supply driven effect should be stronger.” [ext_JFQA_df1532b5e8] |

### S5 — Verdict (6-12 words)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our evidence does not support this channel. | 3 | 0.02 | 67% of 3 | “The evidence does not support this view.” [ext_JF_b34bda8a9d] |
| We find no evidence that [X]. | 14 | 0.10 | 29% of 7 | “We find no evidence of similar reductions in exposure to issuers outside of Europe, even …” [2WRNCEX7] |
| The results confirm/support these predictions. | 8 | 0.04 | 14% of 7 | “Overall, the empirical tests confirm the model’s predictions.” [QG8LS3GV] |
| We rule out [X]. | 15 | 0.09 | 14% of 7 | “… seek to rule out alternative explanations for the association between origination lenders and trading costs, …” [IBY22NKV] |
| These results are not consistent with [X]. | 7 | 0.03 | 25% of 4 | “This behavior is not consistent with standard investor preferences.” [ext_JFQA_ed0266bff2] |
| We find the opposite. | 1 | 0.00 | 0% of 1 | “We find the opposite.” [ext_RFS_31424742a1] |

### S6-7 — Supporting detail  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Moreover, we find that [detail]. | 8 | 0.04 | 20% of 5 | “Moreover, we find that an increase in index funds ownership is not followed by changes …” [ext_RFS_31424742a1] |
| For example, when we analyze [X], we find [Y]. | 6 | 0.03 | 40% of 5 | “For example, we use a difference-in-differences identification strategy based on BlackRock’s acquisition of Barclays Global …” [ext_JF_1876e11382] |
| Indeed, [confirming detail]. | 18 | 0.11 | 0% of 9 | “Indeed, GDP growth declines only by about 0.25% after a shock to total uncertainty.” [ext_JFE_4dca1fff6e] |
| Specifically, [agents] [do X] [k]% more often. | 8 | 0.04 | 0% of 2 | “Specifically, we directly compare GPT-4’s conversational prompting approach with embedding-based supervised learning models trained on …” [ext_JFE_1c18ebec73] |

## 2.11 Robustness / alternative explanations (R)


### S1 — Acknowledge / announce the battery  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We acknowledge that [factor] could also [explain Y]. | 5 | 0.02 | 33% of 3 | “However, we acknowledge that our collective evidence remains largely indirect, and these parties are unlikely …” [WB4BIHIC] |
| One could argue/It is possible that [alternative]. | 5 | 0.03 | 0% of 2 | “One could argue that our organization capital measure simply captures innovation.” [VQAPHNLM] |
| We employ a battery of sensitivity checks to rule out [alternatives]. | 20 | 0.12 | 14% of 7 | “We perform a number of tests in the paper that support this assumption.” [ext_JF_da270ed7ca] |
| We also examine several alternative explanations. | 15 | 0.10 | 56% of 9 | “We also examine several other alternative explanations for the stock price reaction we document.” [ext_JAR_1c65ba10b9] |
| We go through an extensive list of exercises to evaluate robustness. | 6 | 0.03 | 33% of 3 | “We include an extensive set of controls used in the literature, such as founders’ education, …” [ext_JF_b34bda8a9d] |

### S2 — State what is checked (short)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We explicitly check whether these factors subsume our findings. | 47 | 0.39 | 18% of 33 | “Second, I test whether similarity, one of the two key forces of associative memory theory, …” [ext_RFS_6c41a0f14c] |
| We run several robustness checks to validate our assumptions. | 9 | 0.04 | 75% of 4 | “We perform a number of tests in the paper that support this assumption.” [ext_JF_da270ed7ca] |
| So far, our approach relies on the assumption that [X]. | 1 | 0.00 | 100% of 1 | “So far, our approach relies on the theoretically and empirically supported assumption that the lending …” [GRJQJX3B] |
| Various robustness checks support my findings. | 1 | 0.00 | 100% of 1 | “Various robustness checks support the presence of my findings.” [ext_JFQA_df1532b5e8] |

### S3-5 — One check per sentence, test and result together  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our results are robust to [X]. | 17 | 0.11 | 67% of 9 | “… that our results are robust to using alternative methods to reduce the dimensionality of h …” [ext_JF_5c81171dc3] |
| Our results hold for [subsample/cut-off]. | 11 | 0.06 | 60% of 5 | “The findings hold after distinguishing foreign firms that provide GAAP reconciliation versus those using US …” [ext_TAR_58139bc873] |
| Using alternative measures/specifications, [result]. | 9 | 0.07 | 57% of 7 | “… result using this alternative measure as the independent variable is consistent with our baseline result.” [VQAPHNLM] |
| When we progressively raise the cut-off to [k], our inferences remain unchanged. | 6 | 0.03 | 100% of 3 | “This negative relation remains significant even after further controlling for the effects of term structure …” [APQ7HFHK] |
| [Result] is not driven by [X]. | 11 | 0.05 | 33% of 3 | “This is not driven by owners.” [ext_RFS_0834902bd3] |
| We find robust results using these alternative proxies. | 7 | 0.05 | 40% of 5 | “We find similar results when we measure innovation using patent citations.” [Q95QGBR4] |

### S6 — Placebo / falsification  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| A placebo test in [period] reveals no such effect. | 6 | 0.05 | 33% of 3 | “Moreover, controlling for placebo comomentum increases the absolute magnitude of the t-statistic on our key …” [ext_RFS_5f866d83c4] |
| A falsification test finds no effect in [X]. | 2 | 0.01 | 50% of 2 | “We conduct a falsification test by studying a state of the world characterized by strong …” [V4AJ7JGF] |
| Prices do not respond to future [changes] (parallel trends). | 8 | 0.05 | 40% of 5 | “Consistent with the parallel trends’ assumption, we find that prices do not respond to future …” [ext_CAR_c861bb91bd] |
| [...] reveals no such effect. | 2 | 0.01 | 50% of 2 | “We find no such effect on loan spreads, maturity, loan amount, or covenants.” [CV4WQZBR] |

### S7 — Close  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Thus, [X] is most likely attributable to [Y] rather than [alternative]. | 1 | 0.00 | – | “… countries is due to weaker compliance with restatement reporting, rather than an absence of accounting …” [ext_TAR_58139bc873] |
| [...] are unlikely to be driven by [X]. | 2 | 0.01 | 100% of 1 | “… they are unlikely to be driven by unobserved differences in the characteristics of firms in …” [LZBRW8NQ] |
| Across all specifications, [X]. | 2 | 0.01 | 0% of 3 | “Across a wide variety of tests and specifications, the data uniformly indicate that index funds …” [ext_RFS_31424742a1] |
| Importantly, we show that these nonresults are not due to [limited power]. | 7 | 0.04 | 60% of 5 | “Thus, our results cannot be explained by unobservable issuer characteristics, including riskiness or direct or …” [WNHVK3RH] |

## 2.12 Contribution / literature positioning (L)


### count — S1 variant: announce the number of contributions  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our paper/study makes [three] contributions. | 25 | 0.11 | 70% of 10 | “Our study makes three primary contributions.” [ext_JAR_a7cb1e6364] |
| Our study contributes to the literature in several ways. | 8 | 0.04 | 100% of 5 | “Our findings contribute to the literature in two ways.” [ext_CAR_c861bb91bd] |
| Our paper falls into several literatures. | 2 | 0.01 | 100% of 1 | “Our paper falls into several literatures.” [ext_RFS_7b88c84a64] |
| First/Second/Third, we contribute to [topic]. | 24 | 0.19 | 100% of 16 | “First, we extend the literature on the design of performance measurement and evaluation systems within …” [ext_JAR_a7cb1e6364] |

### S1 — Name the strand  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We (also) contribute to the (growing) literature on [topic]. | 59 | 0.50 | 82% of 45 | “Second, our article contributes to the literature on bank loans.” [VQAPHNLM] |
| Our paper is (closely) related to / relates to [studies on X]. | 45 | 0.40 | 74% of 42 | “Notably, we closely relate to Ziebarth (2013), which studies the effect of radio on bank …” [2AWVRR4R] |
| This paper speaks to/complements/builds on [Paper]. | 30 | 0.19 | 67% of 15 | “Finally, this study complements the blockholder literature.” [ext_CAR_db12d3e5ea] |
| Our paper belongs in/falls into the literature on [topic]. | 2 | 0.01 | 100% of 2 | “When the price falls in STANDARD, consumers believe the offset to be less effective.” [ext_RFS_0d795b73f0] |
| Related literature. The idea that [X] dates back to [Paper]. | 3 | 0.01 | 100% of 3 | “… of selective exposure, which dates back to the original theory of cognitive dissonance (Festinger, 1957).” [YNNGFJ8S] |
| Our work also relates to a broader literature in [field] on [topic]. | 39 | 0.24 | 63% of 19 | “A large literature in economics and finance uses inflation disagreement as a measure of inflation …” [ext_JFE_baf49090a8] |

### S2-4 — What each named paper did (narrative citation as subject, one specific verb)  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [Author] (Year) show/find/document that [finding]. | 66 | 0.84 | 54% of 85 | “Hellmann and Puri (2002) show that VCs are essential to the professionalization of startups.” [ext_JFE_5e081a5811] |
| [Author] (Year) study/examine/investigate [X]. | 33 | 0.31 | 91% of 22 | “Barro (2006), Gourio (2012), and Petrosky-Nadeau, Zhang, and Kuehn (2013) consider rare disasters.” [ext_JFE_bd61df5ea6] |
| [Author] (Year) propose/develop [model]. | 14 | 0.08 | 22% of 9 | “Kahn and Winton’s (1998) model suggests that large, well-established firms with numerous analysts that have …” [ext_CAR_db12d3e5ea] |
| Prior studies/These papers examine [A]. | 20 | 0.10 | 82% of 11 | “Several studies document that “pay-for-luck” is asymmetric, with pay increasing more with positive exogenous shocks …” [ext_JF_a6dd7e44e3] |
| [A], [B], and [C] all examine [X], mostly finding [Y]. | 1 | 0.00 | 100% of 1 | “… al. (2012) all examine the association between vega and risk-taking, mostly finding a positive relation.” [ext_JF_da270ed7ca] |
| [Paper] point out that [X]. | 12 | 0.06 | 20% of 5 | “However, as Breeden (1979) notes, maximally-correlated portfolios can also serve as the factors in such …” [ext_JFQA_a6a5f7a156] |

### S5 — Turn: what remains open / how they differ  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| While this research shows [A], [open question]. | 7 | 0.03 | 50% of 2 | “While such research demonstrates how biases of individuals can lead to discrimination in the digital …” [ext_MS_abd98f40ff] |
| In contrast/Unlike [Paper], we [Y]. | 64 | 0.48 | 35% of 51 | “In contrast, for topics such as insider stock transactions and specialized conference presentations, we observe …” [ext_JFE_1c18ebec73] |
| They focus on [A], whereas we [B]. | 7 | 0.04 | 80% of 5 | “… existing bonds, whereas we study firms’ decisions to issue new bonds and the characteristics of …” [IUEMCEMW] |
| Our paper differs in [Y]. / The focus of these papers differs from ours. | 35 | 0.24 | 57% of 23 | “These models differ in their assumptions about how people manage their self-confidence, some emphasizing updating, …” [ext_MS_934861ae69] |
| However, these papers do not [X]. | 18 | 0.09 | 50% of 12 | “However, they focus on asset pricing effects of these biases.” [ext_RFS_7b88c84a64] |
| This literature has focused on [A], ... | 14 | 0.08 | 100% of 8 | “Prior research has focused on the human capital of rank-and-file employees and has relied on …” [Q95QGBR4] |

### S6 — This paper's contribution in the strand  (6 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| We contribute by showing/documenting that [X]. | 4 | 0.02 | 67% of 3 | “We contribute to this literature by providing evidence on the effects of information-sharing systems within …” [ext_JAR_3057882e19] |
| Relative to this literature, our contribution is to [X]. | 8 | 0.04 | 100% of 3 | “Relative to this literature, our results are novel in two respects.” [WNHVK3RH] |
| We are the first to [X]. / To the best of our knowledge, [X]. | 13 | 0.07 | 71% of 7 | “To our knowledge, three recent papers have pursued a related question although both their questions …” [CV4WQZBR] |
| We extend [Paper]'s finding to [new setting]. | 45 | 0.25 | 52% of 27 | “We extend this literature by investigating the role of free speech protection laws, which apply …” [WB4BIHIC] |
| Our main contribution is to provide evidence of [X]. | 6 | 0.04 | 80% of 5 | “Our contribution is to illustrate how the 150-hour rule significantly reduces minority participation in the …” [ext_JAR_6281def7a8] |
| We provide (the first/new) evidence on [X]. | 16 | 0.08 | 33% of 6 | “Finally, we provide direct evidence for the market power mechanism underlying the interest rate exposure …” [ext_JF_c5d99f716f] |

### S7 — Extension (optional)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| More broadly, [implication for the strand]. | 12 | 0.06 | 57% of 7 | “More generally, we illustrate how features of different social media platforms (e.g., character limits and …” [GHVLM4T6] |
| This finding provides additional support for [Paper]'s argument that [X]. | 3 | 0.01 | 33% of 3 | “This evidence provides further support to the empirical implications of our model.” [NJ8Y8ITJ] |
| Our results/findings have implications for [debate]. | 7 | 0.03 | 0% of 2 | “Our results also have important implications for financial regulations.” [A7CRD7NG] |
| Overall, our results provide a justification for [X]. | 10 | 0.06 | 0% of 6 | “Overall, these findings show that Twitter facilitates both information sharing and the propagation of misinformation.” [2AWVRR4R] |

## 2.13 Policy / theoretical implications (P)


### S1p — 政策型 S1 Announce (6-10 words)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Finally, our paper/results has/have policy implications. | 17 | 0.09 | 62% of 8 | “Our study has several empirical and policy implications.” [ext_JAR_72b54520c1] |
| Our findings inform the debate on [policy question]. | 2 | 0.01 | 0% of 1 | “… potential to inform the public by providing instant news updates, facilitating the sharing of ideas, …” [AFN28PL4] |
| Our results are relevant for [regulator]. | 1 | 0.00 | 0% of 1 | “… can be useful for policy makers and researchers alike to answer other questions pertaining to …” [R2IFDXFF] |
| From a policy standpoint/perspective, [X]. | 2 | 0.01 | 0% of 1 | “From a policy standpoint, transparent reporting—because it fosters competition by reducing cartel sustainability—may have positive …” [ext_TAR_c52333ac2b] |

### S2p — 政策型 S2 Current practice or assumption  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Policymakers/Regulators currently assume/require [X]. | 32 | 0.34 | 14% of 36 | “… mandatory; however, the SEC requires all listed firms to “provide a discussion of the most …” [Q95QGBR4] |
| In contrast to assumptions made by policy-makers, [X]. | 1 | 0.00 | 100% of 1 | “In contrast to assumptions made by policy-makers—for example, the Joint Committee on Taxation assigns 25% …” [ext_CAR_c861bb91bd] |
| A common assumption by [policy-makers] is that [X]. | 3 | 0.01 | 0% of 1 | “There is a common belief that increased transparency of information is desirable.” [8H4P44R8] |
| Current/Existing rules require [X]. | 1 | 0.00 | – | “… for the current policy debates about the social benefits of carbon mitigation and the size …” [ext_RFS_0d795b73f0] |

### S3p — 政策型 S3 What the results imply  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our findings imply/suggest that [policy] may also [affect Z]. | 38 | 0.24 | 7% of 15 | “These results indicate that, although banks account for the risk-increasing aspect of organization capital through …” [VQAPHNLM] |
| [...] has implications for [regulators/how X is interpreted]. | 13 | 0.07 | 40% of 5 | “Second, our findings have implications for the transmission of monetary policy.” [ext_JF_c5d99f716f] |
| [...] could unintentionally harm [X]. | 10 | 0.06 | 25% of 4 | “Errors are unintended, potentially avoidable deviations from plans or goals (Hofmann and Frese 2011) and …” [ext_CAR_5a857eca7f] |
| This insight justifies [X]. | 15 | 0.09 | 29% of 7 | “Such disparities attract significant public attention and call for research to understand their sources.” [ext_JAR_6281def7a8] |

### S4p — 政策型 S4 The lever in the policymaker's hands  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| [X] is a feature of the tax system under the control of policy-makers. | 1 | 0.00 | 100% of 1 | “… system features under the control of policy-makers, such as the definition of the tax base, …” [ext_CAR_c861bb91bd] |
| Policymakers/Regulators can/could [X]. | 3 | 0.01 | 50% of 2 | “Therefore, regulators need to understand potential economic forces before imputing discrimination to the platform or …” [ext_MS_abd98f40ff] |
| [...] by requiring/limiting [X]. | 7 | 0.03 | 0% of 3 | “The paper continues by introducing the literature regarding visual rhetoric and the notion of rhetorical …” [ext_CAR_c54c74467b] |
| [Policy tool] is potentially a tool to [improve Y]. | 16 | 0.10 | 12% of 16 | “… as a tool to encourage firms to reduce the wage gap between men and women.” [ext_JF_fce63bf6a1] |
| This reinforces the case for [X]. | 13 | 0.06 | 22% of 9 | “… often the case for evolving technologies, the emergence of reward crowdfunding led to a regulatory …” [ext_JAR_3a6b9de6ed] |

### S1t — 理论型 S1–4 Re-reading the literature  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Our results have implications for how the literature interprets [X]. | 1 | 0.00 | 100% of 1 | “… results have implications for the way the literature interprets the lessons from the financial crisis.” [R2IFDXFF] |
| One could erroneously conclude that [X]. | 1 | 0.00 | 100% of 1 | “… one could erroneously conclude that lower levels of creditor rights overall were associated with an …” [R2IFDXFF] |
| Our findings challenge/question the view that [X]. | 3 | 0.01 | 0% of 1 | “Nevertheless, the results in Sufi (2009) challenge the notion that credit lines have perfect commitment.” [NJ8Y8ITJ] |
| In contrast, our findings show that [Y]. | 24 | 0.11 | 7% of 15 | “In contrast, the price deviations between exchanges in the same country typically do not exceed …” [ext_JFE_4aef10dda1] |

## 2.14 Roadmap (O)


### S1 — Opener (5-9 words)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| The remainder/rest of the paper is organized as follows. | 33 | 0.15 | 92% of 12 | “The rest of the paper is organized as follows.” [TMKNNX9B] |
| The paper proceeds as follows. | 43 | 0.20 | 100% of 18 | “The rest of the paper is organized as follows.” [TMKNNX9B] |
| We start in the next section by [X]. | 3 | 0.02 | 100% of 1 | “In the next section, we review the related literature on transparency, liquidity, cost of capital, …” [IEB6M7CI] |
| Our paper is organized as follows. | 1 | 0.00 | 100% of 1 | “Our paper is organized as follows.” [ext_JFE_bcd8b94113] |

### S2..n-1 — One section per sentence, naming its content  (5 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Section 2 describes/presents [X]. | 52 | 0.56 | 98% of 53 | “Section 3 develops the hypotheses.” [ext_JAR_abd9816b3e] |
| In Section 3, we [do X]. | 12 | 0.10 | 100% of 9 | “In Section 2, we set up the model, present our methodology, and develop relevant statistical …” [ext_JF_5c81171dc3] |
| Sections 3 and 4 present [X]. | 4 | 0.02 | 100% of 1 | “Sections 2 and 3 explain the data and provide summary statistics of volume and returns.” [ext_JFE_4aef10dda1] |
| The (Internet) Appendix contains [X]. | 1 | 0.00 | 100% of 1 | “The Appendix contains proofs.” [ext_RFS_7b88c84a64] |
| We then [present X] in Section [N]. | 9 | 0.06 | 75% of 4 | “Results from a complementary survey are shown in Section 5.” [ext_RFS_0d795b73f0] |

### Sn — Close (3 words)  (4 phrasings)

| template | n/117 | per 1k | in-card | excerpt (≤15 words) [key] |
|---|---:|---:|---:|---|
| Section [N] concludes. | 35 | 0.16 | 93% of 15 | “Section VII concludes.” [ext_TAR_c52333ac2b] |
| The final/last section concludes. | 2 | 0.01 | – | “The final section concludes with a discussion of the implications of the results and suggestions …” [ext_CAR_ee676b0255] |
| Section [N] concludes the paper/article. | 6 | 0.03 | 100% of 3 | “Section VIII concludes the article.” [QG8LS3GV] |
| Section [N] provides a summary of our findings and concludes. | 3 | 0.01 | 100% of 1 | “Section VII provides a summary of our findings and concludes.” [TQMT9MWF] |

---

## Coverage check

- 76 moves across 14 cards; 367 phrasings with n ≥ 1.
- Phrasings per move: median 4, min 4, max 7.
- Moves with fewer than 4 attested phrasings: none.

---

## Cross-cutting transitions

Rates are per 1,000 intro words (217,906 words).

### How body paragraphs open (first words of paragraphs 2…n; 1,533 paragraphs)

| opener | paragraphs | share of body paragraphs | per 1k words | n/117 |
|---|---:|---:|---:|---:|
| Our [paper/results/findings] ... | 169 | 11.0% | 0.78 | 86 |
| First, / Second, / Third, / Fourth, | 110 | 7.2% | 0.50 | 48 |
| To [verb] ..., we ... | 77 | 5.0% | 0.35 | 55 |
| In this paper / This paper ... | 61 | 4.0% | 0.28 | 49 |
| We then / We also / We further ... | 58 | 3.8% | 0.27 | 45 |
| Finally, / Lastly, | 48 | 3.1% | 0.22 | 40 |
| Next, / We next ... | 39 | 2.5% | 0.18 | 32 |
| Using / Exploiting / Building on ... | 23 | 1.5% | 0.11 | 19 |
| Overall, / In sum, / Taken together, | 22 | 1.4% | 0.10 | 19 |
| However, / Yet | 14 | 0.9% | 0.06 | 13 |
| We begin/start by ... | 12 | 0.8% | 0.06 | 12 |
| [Author (Year)] ... | 12 | 0.8% | 0.06 | 11 |
| In addition, / Additionally, | 6 | 0.4% | 0.03 | 6 |
| Moreover, / Furthermore, | 6 | 0.4% | 0.03 | 6 |

### How sentences turn (sentence-initial)

| turn | sentences | per 1k words | n/117 | share as paragraph S1 |
|---|---:|---:|---:|---:|
| However, | 183 | 0.84 | 84 | 6% |
| While ... | 81 | 0.37 | 51 | 10% |
| In contrast, / By contrast, | 73 | 0.34 | 53 | 3% |
| Although / Though ... | 68 | 0.31 | 38 | 22% |
| Instead, | 30 | 0.14 | 23 | 0% |
| Yet | 24 | 0.11 | 15 | 12% |
| On the other hand, | 20 | 0.09 | 20 | 20% |
| Nevertheless, / Nonetheless, | 17 | 0.08 | 14 | 0% |
| Despite / In spite of ... | 16 | 0.07 | 15 | 12% |
| Unlike ... | 14 | 0.06 | 12 | 29% |
| But | 13 | 0.06 | 10 | 0% |
| At the same time, | 8 | 0.04 | 7 | 12% |
| Conversely, | 6 | 0.03 | 6 | 0% |
| Still, | 2 | 0.01 | 2 | 0% |

| mid-sentence turn | occurrences | per 1k words | n/117 |
|---|---:|---:|---:|
| ..., however, ... (mid-sentence) | 51 | 0.23 | 33 |
| ..., whereas ... | 35 | 0.16 | 21 |
| ..., but ... | 158 | 0.73 | 77 |

### Short verdict sentences (under 12 words, roadmap sentences excluded)

- 621 short sentences, 7.2% of all sentences, 2.85 per 1k words, found in 113/117 intros.
- Position in the paragraph: first 32%, middle 54%, last 14%.
- In the labelled intros, short sentences fall in these functions: L 17%, T 14%, F 11%, A 10%, K 8%, Q 7%, H 6%, R 6% (n=266).

| verdict skeleton | sentences | share | per 1k words | excerpt [key] |
|---|---:|---:|---:|---|
| other | 159 | 26% | 0.73 | “Only 10% come inbound from company management.” [ext_JFE_5e081a5811] |
| The [results/effect/answer] [verb] ... | 83 | 13% | 0.38 | “The first example is a rare-disaster model.” [ext_JF_1f42ea1b72] |
| We/I [signpost verb] [object]. (e.g., examine, consider, conclude, call it) | 81 | 13% | 0.37 | “We examine two dimensions.” [ext_CAR_c861bb91bd] |
| Our/My [hypothesis/evidence/paper] [verb] ... | 68 | 11% | 0.31 | “Our paper complements and extends these studies.” [ext_JFQA_caec111127] |
| This/These [noun] is/are [verdict]. | 59 | 10% | 0.27 | “These additional moment restrictions are often referred to as cross-equation restrictions.” [ext_JF_1f42ea1b72] |
| First/Second/Finally, [short claim]. | 55 | 9% | 0.25 | “Third, I test whether interference weakens the documented effect.” [ext_RFS_6c41a0f14c] |
| [Noun phrase] is/are/has [property]. (topic-first statement) | 40 | 6% | 0.18 | “Other time-varying factors may drive trends in risk for this firm.” [ext_JF_da270ed7ca] |
| Thus/Hence/So/Overall, [short conclusion]. | 21 | 3% | 0.10 | “As a result, when index fund ownership increases, corporate governance worsens.” [ext_RFS_31424742a1] |
| We/I find/show [the opposite / no evidence / results consistent with X]. | 19 | 3% | 0.09 | “We document that large fractions of respondents view stockholders negatively.” [ext_RFS_36a2cc1f42] |
| Direct question: [Does X affect Y]? | 18 | 3% | 0.08 | “What might have caused this change in board behavior?” [ext_JF_a6dd7e44e3] |
| However/Yet/But, [short turn]. | 18 | 3% | 0.08 | “However, approximately 16% of chemical identities are kept as trade secrets.” [28TTDMNX] |
