# Academic Citations

Citations establish scholarly lineage, support claims with evidence, and position work within ongoing discourse. Every citation serves one of three functions: credit attribution, evidence support, or scholarly dialogue.

## Citation Purpose

Academic citations enable verification and locate original sources. They credit prior work, support claims with external evidence, and connect research to broader scholarly conversation.

Credit attribution acknowledges intellectual debt. Evidence support demonstrates claims rest on verified foundations. Scholarly dialogue positions work relative to existing research, showing agreement, extension, or departure from prior findings.

Citations also serve practical functions: readers can pursue topics further, reviewers can verify claims, and future researchers can trace intellectual lineage. Proper citation prevents plagiarism while building credibility through demonstrated engagement with the field.

## Citation Style Selection

Major citation styles align with disciplinary conventions; the discipline table, the selection precedence, and the profile that carries each style are in <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::citations@core/reference/style_selection.md" />.

Selection criteria:
- Follow journal, conference, or assignment guidelines when specified
- Match disciplinary conventions when guidelines are absent
- Verify specific requirements (footnotes vs. author-date)
- Maintain consistency throughout the document

When uncertain, check 10-15 recent publications in your target venue to identify the expected style and conventions.

See `evidence_extraction` (module `agentic`, profile `workflows`, skill `research_procedure`).
See `source_evaluation` (module `agentic`, profile `workflows`, skill `research_procedure`).

## Narrative vs. Parenthetical Citations

The choice between citation formats depends on rhetorical emphasis, not arbitrary preference.

**Narrative citations** emphasize the researcher:
- Use when discussing specific contributions or comparing approaches
- Effective for contrasting viewpoints or scholarly debates
- Place author name in the sentence: "Smith (2023) proposes..."

**Parenthetical citations** emphasize the finding:
- Use when information matters more than source identity
- Effective for widely accepted claims or multiple supporting sources
- Place citation at end: "...(Smith, 2023)"

Mix both formats within paragraphs to avoid mechanical patterns. Vary citation placement throughout sentences rather than defaulting to sentence-final position.

**Examples across disciplines**:
- Narrative: "While Smith (2023) emphasizes methodological rigor, Jones (2022) focuses on practical application."
- Parenthetical: "Multiple studies demonstrate this effect (Smith, 2023; Jones, 2022; Johnson, 2021)."

## Citation Density and Synthesis

Optimal citation density varies by document type and section:

| Document Type | Typical Range |
|---------------|---------------|
| Original research | 20-60 citations |
| Review articles | 50-150+ citations |
| Short papers | Under 20 citations |

Benchmark your target venue by examining recent publications. Literature review sections require higher density than methods or results sections.

**Synthesis over listing**:

Avoid sequential listing:
> "Smith (2023) says X. Jones (2022) says Y. Johnson (2021) says Z."

Synthesize relationships:
> "While Smith (2023) emphasizes X, and Jones (2022) focuses on Y, Johnson (2021) demonstrates that both factors interact to produce Z."

Literature review strategies include thematic grouping by concept, chronological evolution showing how understanding developed, and methodological contrasts comparing approaches across studies.

**Common errors**:
- Over-citation: Repeating the same citation in every sentence of a paragraph
- Under-citation: Failing to credit paraphrased ideas, data, or methodologies
- Padding: Excessive lists that add volume without supporting claims

See `clarity_principles` (module `writing`, profile `core`, package `basics`).

## Integration Best Practices

**Paraphrasing preferred**: Paraphrase when the idea matters more than specific wording. Quote only when exact wording is analyzed, particularly eloquent, or definitional. Include page numbers for direct quotes.

**Signal phrases for narrative citations**:

| Relationship | Signal Phrases |
|--------------|----------------|
| Agreement | "As Smith (2023) demonstrates...", "Consistent with Smith (2023)..." |
| Disagreement | "Contrary to Smith (2023)...", "Smith (2023) disputes this claim..." |
| Building on | "Building on Smith (2023), we extend...", "Smith's (2023) framework provides..." |
| Comparison | "Like Smith (2023), we find...", "Both Smith (2023) and Jones (2024) demonstrate..." |

**Avoid mechanical patterns**:
- Do not start every sentence with "According to..."
- Vary citation placement within sentences
- Explain how sources support claims rather than listing them
- Mix single and multiple citations appropriately

## Citations Must Carry a Claim

A citation earns its place by supporting a statement the reader can check. A bare pointer that asserts nothing — "following established precedent [@x]" or "as in prior work [@y]" — hands the reader a name but no claim to evaluate, and reads as decoration. State, in at least half a sentence, what the cited work did or found, then cite it: "Nordic registries have been mapped to a common data model before [@x]" rather than "following Nordic precedent [@x]." If the cited work's contribution does not fit the current argument, the citation belongs elsewhere or not at all.

A named study must be introduced in the running prose at or before its first appearance — never first in a figure or table. When a study's result is shown in an exhibit, name and gloss it in the text and place its citation at that first mention, not pages later. A reader who meets a citation beside a table row, with the supporting sentence two pages on, cannot connect the evidence to the claim.

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/exhibits.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/terminology.md" />.

## Bibliography and Reference Management

Reference list organization depends on citation style:
- Author-date styles: Alphabetical by first author surname
- Numbered styles: Order of first appearance in text

Include complete metadata for every source:
- Author names (all authors, or truncated per style guidelines)
- Publication year
- Title (article, chapter, or work title)
- Source venue (journal, publisher, website)
- Identifiers (DOI, ISBN, URL)
- Access dates for volatile web content

Maintain consistency in formatting. Reference style guides (APA Publication Manual, 7th ed.; MLA Handbook, 9th ed.; Chicago Manual of Style, 18th ed.; IEEE Reference Guide and IEEE Editorial Style Manual) provide comprehensive rules for each style. Use bibliography management tools appropriate to your workflow and venue requirements, and check that the style file a tool applies declares the edition the venue expects.

Output from a generative AI tool that is quoted, paraphrased, or built into the work is cited and its use disclosed; the three manuals' entry shapes are in <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::citations@core/reference/ai_generated_content.md" />.

See `source_evaluation` (module `agentic`, profile `workflows`, skill `research_procedure`).

## Common Citation Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Dangling citations | Unclear connection to claim | Place citation immediately after supported claim |
| Author focus | Mechanical prose | Synthesize multiple sources parenthetically |
| Missing connections | List without argumentation | Explain how citations support claims |
| Inconsistent format | Reader confusion | Follow chosen style consistently |
| Over-quoting | Lacks synthesis | Paraphrase more, quote only when wording matters |

**Examples**:

*Dangling*:
> "Smith (2023). The phenomenon has significant implications."

*Corrected*:
> "The phenomenon has significant implications for future research (Smith, 2023)."

*Author focus*:
> "Smith (2023) says X. Jones (2022) says Y."

*Corrected*:
> "Multiple studies demonstrate this effect (Smith, 2023; Jones, 2022)."

## Citation Checklist

After drafting, verify:

- [ ] Citations support specific claims, not general padding
- [ ] Mixed narrative and parenthetical formats appropriately
- [ ] Synthesized relationships between sources
- [ ] Varied citation placement and signal phrases
- [ ] Complete reference metadata for every source
- [ ] Consistent formatting throughout
- [ ] Page numbers included for direct quotes
- [ ] Every citation supports a checkable claim; no bare name-drops
- [ ] Named studies introduced and glossed in prose before appearing in a figure or table
- [ ] Every citation in text appears in reference list
- [ ] Every reference list entry appears in text
