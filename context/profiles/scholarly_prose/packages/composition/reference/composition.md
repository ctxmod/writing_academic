# Academic Composition

Composition governs how sections relate, how length distributes across a document, and when to split or merge structural units. These decisions shape reader comprehension independently of content quality.

## Length and Proportion

Document type determines expected scale. Proportions shift with format, but sections within any document benefit from consistent targeting.

| Document Type | Typical Body Length | Section Count |
|---------------|---------------------|---------------|
| Journal article | 5,000-8,000 words | 4-6 |
| Conference paper | 3,000-5,000 words | 4-5 |
| Thesis chapter | 8,000-12,000 words | 4-8 |
| Review article | 8,000-15,000 words | 5-10 |
| Dissertation (full) | 40,000-80,000 words | 15-30 (across chapters) |

**Section length target**: 2,000-2,500 words per major section. This range sustains a complete argument without exceeding working memory capacity. Sections under 1,000 words rarely develop ideas adequately; sections above 3,000 words often contain multiple arguments that benefit from separation.

**Paragraph length**: 150-300 words (4-8 sentences), one main idea per paragraph. Scientific papers sometimes run longer (300+ words) for complex explanations. Paragraphs under three sentences underdevelop their point. Paragraphs beyond eight sentences risk losing coherence.

**Proportion balance**: No single section should exceed 35% of total body length unless format requires it (e.g., a literature review in a thesis). When one section dominates, re-evaluate whether it contains multiple arguments that warrant splitting.

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/imrad_structure.md" />.

## Section Division

Splitting and consolidation decisions determine whether readers encounter ideas as independent units or interconnected parts.

### Split Signals

Split content into separate sections when:

- The material forms a complete argumentative unit that can stand semi-independently
- Section length exceeds 3,000 words
- A distinct methodology, dataset, or analytical mode enters the discussion
- Readers need to locate and reference the content independently
- The material introduces a new research question or sub-question

### Consolidate Signals

Merge content into subsections of an existing section when:

- The material is subordinate to an adjacent section's argument
- Content falls under 1,000 words and lacks capacity for independent development
- Separation would require repeating context, definitions, or framing
- The material serves a single overarching purpose better delivered as a unified block

| Signal | Action | Rationale |
|--------|--------|-----------|
| New dataset or method introduced | Split | Readers expect discrete treatment |
| Content supports but does not drive argument | Consolidate | Subordinate material belongs in subsections |
| Section exceeds 3,000 words | Split | Cognitive load increases past this threshold |
| Content under 1,000 words, dependent on context | Consolidate | Insufficient material for independent section |
| Shift in analytical mode (quantitative to qualitative) | Split | Different evaluation criteria apply |

### Results and Discussion

The decision to separate or combine Results and Discussion depends on content complexity and disciplinary convention.

**Separate when**: Complex quantitative findings require systematic, neutral presentation before interpretation. Readers benefit from reviewing all findings before encountering analysis. Multiple results warrant individual attention before collective synthesis.

**Combine when**: Interpretation is necessary for understanding what results signify. The work is theory-focused rather than experiment-focused. Audience includes non-specialists who benefit from immediate contextualization. Multiple distinct experiments are better understood with integrated analysis.

## Structural Coherence

A document holds together when every section advances the same line of inquiry. Without this thread, sections become standalone essays assembled by proximity rather than logic.

### The Golden Thread

Research questions serve as the conceptual spine connecting all sections. Each section should answer or advance a specific question. If a section does not connect to a stated question, either the section is extraneous or the questions are incomplete.

**Test**: For each section, state in one sentence how it advances the central inquiry. If the connection requires more than one sentence to explain, the section may need repositioning or the framing may need revision.

### Purposeful Chunking

Group related material within sections using clear boundaries. Subsection headings, transition paragraphs, and white space all signal shifts in focus. Readers process information in chunks of 2,000-2,500 words effectively; beyond this, comprehension degrades without navigational aids.

### Forward and Backward References

Connect current content to both prior and upcoming material. Backward references ("As established in Section 3...") anchor new claims in accepted premises. Forward references ("Section 6 examines this limitation in detail") set expectations and sustain momentum.

Use forward references sparingly. Overuse creates an IOU structure where readers accumulate promises rather than understanding. Reserve forward references for content that genuinely requires later context.

## Signposting

Signposting orients readers within document structure. Effective signposts appear at entry points, transitions, and exits.

### Section Previews

Open complex sections with a content preview that establishes scope and sequence.

> "This section examines three factors: sample composition, measurement validity, and replication conditions."

Previews reduce cognitive load by providing a framework before details arrive. Limit previews to sections with three or more subsections or distinct threads.

### Section Conclusions

Close major sections with a synthesis that reinforces the section's contribution to the overall argument.

> "Together, these findings establish that measurement validity depends on context rather than instrument alone."

Section conclusions differ from summaries. A summary restates what was covered. A conclusion states what the covered material means for the document's central argument.

### Transition Paragraphs

Bridge major sections with short paragraphs (2-4 sentences) that connect what was established to what follows. These paragraphs sit between sections and perform two functions: closing the previous thread and opening the next.

> "Having established the reliability of the measurement instrument, we now turn to its application across the three study populations."

Transition paragraphs are optional between closely related sections. They become necessary when the shift in topic, method, or analytical mode is large enough to disorient readers.

### Placement Strategy

| Location | Signpost Type | Purpose |
|----------|---------------|---------|
| Section entry | Preview | Establish scope and sequence |
| Midpoint (long sections) | Interim summary | Recalibrate reader orientation |
| Section exit | Conclusion | Synthesize contribution |
| Between sections | Transition paragraph | Bridge topic shifts |

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/imrad_structure.md" />.

## Anti-Patterns

| Anti-Pattern | Consequence | Alternative |
|--------------|-------------|-------------|
| Uniform section lengths | Artificial padding or compression to hit targets | Let content determine length within the 1,000-3,000 word range |
| Missing signposts in long sections | Reader disorientation after 1,500+ words | Add previews at entry, interim summaries at midpoint |
| Orphan sections under 500 words | Underdeveloped ideas that weaken argument | Merge with adjacent section or expand with supporting evidence |
| Excessive forward references | Reader accumulates promises instead of understanding | Resolve most claims locally; reserve forward references for genuine dependencies |
| Symmetric structure forced on asymmetric content | Methodologically simple sections padded to match complex ones | Accept asymmetry; match depth to content demands |

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/depth_placement.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/rhythm.md" />.
See `clarity_principles` (module `writing`, profile `core`, package `basics`).
See `density_by_frequency` (module `writing_context`, profile `core`, package `density`).
