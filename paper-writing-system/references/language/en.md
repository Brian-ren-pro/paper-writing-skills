# English language layer (drafting and revising English papers)

Version v1, 2026-11-11. Sources: intro guide card v6 (`sections/introduction-en-card.md`), writing_spec judge experiments (`language/ai-tone.md` §4), Zotero corpus statistics (`sources/corpus-evidence.md`, 178 English papers). Chinese drafts follow `language/zh.md`; this file governs English text across all sections. Section-specific structure and phrasing are in `sections/`; cross-referencing between sections is in `structure.md` §5.

## 1. Voice and verbs

- "We" for research actions: about 15–20 we/our/us per 1,000 words in intros; passive only for data handling. "This paper" for positioning and roadmap.
- Verb strength matches the design: DiD/IV/RD/experiment → "increases", "the effect of"; panel OLS → "is associated with"; untested mechanism → "suggests"; one hedge per claim.
- "Is consistent with" is ordinary English academic usage and stays where the evidence is a comparison with a prior or a prediction. Do not use it as a reflexive paragraph closer.
- No "first" claim without literature support. Never call the paper "novel".

## 2. Sentences

- Mean about 21–25 words; most 18–32; at most one sentence under 12 words per paragraph; about one sentence over 40 words per 25–30 sentences.
- Long sentences come from fusion (result + magnitude; design + comparison group; cited paper + finding + our difference), never from cramming three or more findings.
- Full sentences only; no noun stacks, clipped clauses or dash chains.

## 3. Paragraphs and sections

- Open each paragraph with substance (a fact, claim, result or cited finding). Within and at the end of paragraphs, no sentence that only announces, frames, labels or sums up.
- A section or subsection may open with one sentence stating what it tests ("In this section, we examine whether ...", "To test whether ..., we ..."); this is common in results, robustness and mechanism sections (corpus §9). Do not open with "Section X shows/predicts" as subject (0 of 1,110 openings).
- No end-of-section preview of the next section (6 of 1,110).
- Cross-references: the seven allowed types (parenthetical "(Section 2.3)", content-first callbacks such as "As discussed in Section 2, ...", functional pointers, forward pointers inside a content sentence, roadmap, subsection map at the start of multi-part sections, table and figure references) are listed in `structure.md` §5.
- Paragraph openers in intros: "Our [results]..." 11%; "First,/Second," 7%; "To [verb]..., we..." 5%; Moreover/Furthermore/In addition/Additionally under 1% combined.
- Turns mostly inside paragraphs: sentence-initial However about 0.6–0.9 per 1,000 words across sections.
- "We/our/us" per 1,000 words by section: data 20, robustness 22, mechanism 18, introduction 17, results 16, conclusion 13, theory 10 (corpus §10).

## 4. Section-specific rules

Introduction, conclusion, results and numbers, and the other sections are in `sections/` (introduction.md and introduction-en-card.md; conclusion.md; results.md §3–§6 for magnitudes and number formats).

## 5. Banned words and habits

delve, landscape, realm, intricate, tapestry, pivotal, underscore, nuanced, "It is worth noting", "Interestingly"; "In recent years, X has attracted increasing attention"; "valuable insights for policymakers, investors, and managers"; "To the best of our knowledge, we are the first" without support; four or more citations in one parenthesis with no difference stated. See `language/ai-tone.md` §4 for the full judge-derived list.

Scope hedges, insignificant results and identification caveats are not style problems: never delete them as part of a language edit; see `narrative.md` §6–§7.

## Revision log

- 2026-11-11: v1 created during the v2 reorganisation (approved by本体系).
- 2026-11-11 (v3 architecture, approved by本体系): moved to language/; section openings relaxed per corpus (one stating sentence allowed); cross-reference types point to structure.md §5; section-specific rules moved to sections/.
- 2026-11-13 (v3.1): §5 adds a pointer to narrative.md §6–§7 — scope hedges and insignificant results are not language edits.
