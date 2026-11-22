# Academic Revision

Revision is a systematic, multi-pass process that addresses different quality dimensions in sequence. Each pass targets one concern exclusively. Mixing concerns in a single pass divides attention and reduces effectiveness.

## Pass Framework

Four sequential passes move from macro structure to micro polish. Complete each pass fully before starting the next.

| Pass | Focus | Key Questions | Common Fixes |
|------|-------|---------------|--------------|
| 1 -- Structure and Logic | Argument flow, section coherence, logical gaps | Does each section advance the stated research questions? Do paragraphs follow a logical sequence? | Reorder sections, merge fragmented arguments, add missing transitions, remove tangential content |
| 2 -- Sentence Variety | Length distribution, openings, type mixing, rhythm | Does the text read with natural variation or mechanical uniformity? | Break long chains of same-length sentences, vary openings, mix simple/compound/complex types |
| 3 -- Word Choice and Precision | Technical accuracy, hedging calibration, vocabulary, jargon | Are terms precise? Is hedging proportional to evidence? | Replace vague terms, remove unnecessary jargon, calibrate hedge strength, define terms on first use |
| 4 -- Engagement and Neutrality | Tone, evidence-claim alignment, anti-pattern removal | Are claims measured? Is the tone objective without being lifeless? | Remove negation-for-drama, eliminate filler phrases, replace formulaic expressions, align claims with evidence |

### Pass 1 -- Structure and Logic

Evaluate at the document and section level. Each section should serve a clear purpose within the overall argument. Each paragraph should contain one main idea, and the sequence of paragraphs should build a coherent narrative. Look for logical gaps where unstated assumptions bridge two claims, and for redundancies where the same point appears in multiple locations.

Key checks: argument flow across sections, paragraph-level coherence, presence of a consistent thread connecting all chapters, and explicit connection to research questions. Check also that depth is correctly placed: mechanism and derivations that answer "how is it implemented or derived" belong in methods or appendices, leaving the main line of argument to carry consequences. A passage the intended reader cannot follow at all is usually over-reaching for its location — cut it to its load-bearing sentence and refer out, rather than rewording at the same density.

### Pass 2 -- Sentence Variety

Target the 70/20/10 distribution: 70% medium sentences (15-25 words), 20% short (8-14 words), 10% long (26-35 words). Vary sentence openings across transitional, adverbial, prepositional, and subject-first patterns. Mix simple, compound, and complex sentence types. Uniform structure signals mechanical generation regardless of content quality.

### Pass 3 -- Word Choice and Precision

Verify technical terminology is accurate and consistent. Check that hedging appears at approximately one marker per 50 words for uncertain claims, with minimal hedging for well-supported claims. Remove vocabulary that signals group membership rather than adding precision. Replace nominalized constructions with active verb forms. Confirm each concept keeps a single name throughout — synonyms for one concept read to a learning reader as distinct concepts. Calibrate register to the least-specialist intended reader, preferring a plain everyday paraphrase to a precise-but-opaque term.

### Pass 4 -- Engagement and Neutrality

Scan for anti-patterns: negation-for-drama constructions, filler phrases, formulaic expressions, and AI-characteristic word choices. Verify that every claim is proportional to its supporting evidence. Confirm the tone remains objective and measured without becoming detached or lifeless.

See `anti_patterns` (module `writing_context`, profile `core`, package `basics`).
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_language.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/terminology.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_register.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/depth_placement.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/rhythm.md" />.

## Revision Priorities

Structure errors compound. Polishing sentences in a section that will be restructured wastes effort. Sequence revision investment according to draft maturity.

**Early drafts**: Prioritize Pass 1 exclusively. Get the argument right before refining prose. Expect large structural changes -- moving, merging, or deleting entire sections. Sentence-level quality is irrelevant at this stage.

**Middle drafts**: Focus on Pass 2 and Pass 3 once structure stabilizes. Sentence-level quality and terminological precision become productive targets only when the macro organization holds.

**Final drafts**: Apply Pass 4 for polish, tone calibration, and anti-pattern elimination. This pass assumes structural soundness and sentence-level competence.

**Rule**: Never skip Pass 1. All subsequent passes assume the argument structure is sound. Skipping directly to word-level revision produces polished text that may not hold together as an argument.

## Collaborative Revision

Different revision participants contribute different strengths. Structure collaboration to match participant capabilities with pass requirements.

**Self-revision**: Allow minimum 24 hours between writing and the first revision pass. Temporal distance exposes structural weaknesses invisible during drafting. Read the document from a different medium (print, tablet, different font) to disrupt familiarity.

**Peer revision**: Provide specific revision questions rather than requesting general feedback. "Does the argument in Section 3 follow from the evidence in Section 2?" produces actionable feedback. "What do you think?" produces vague responses.

**AI-assisted revision**: Use AI tools for pattern detection -- identifying anti-patterns, measuring sentence length uniformity, flagging inconsistent terminology. AI excels at mechanical checks across large documents. Reserve content judgment, argument evaluation, and disciplinary nuance assessment for human reviewers.

**Staggered approach**: Human performs Pass 1 (structure requires domain understanding and argument evaluation). AI assists with Pass 2 and Pass 3 detection (sentence metrics, terminology consistency, hedging frequency). Human performs Pass 4 (tone and engagement require contextual judgment).

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_voice.md" />.
See `clarity_principles` (module `writing`, profile `core`, package `basics`).

## Revision Anti-Patterns

| Anti-Pattern | Consequence | Alternative |
|--------------|-------------|-------------|
| Simultaneous multi-pass | Divided attention, missed issues in each dimension | Sequential single-focus passes |
| Premature polish | Polished text gets restructured or deleted | Complete Pass 1 before any sentence-level work |
| Revision without distance | Familiarity blindness to structural problems | Minimum 24-hour gap between writing and revision |
| Accepting all AI suggestions | Homogenized voice, loss of authorial perspective | Use AI for detection, apply human judgment for corrections |
| Skipping Pass 1 | Well-written paragraphs in a poorly organized document | Always start with structure regardless of draft maturity |

## Revision Checklist

After completing all four passes, verify:

**Structure (Pass 1)**:
- [ ] Each section serves a stated purpose
- [ ] Paragraphs contain one main idea each
- [ ] Logical flow connects all sections without unstated assumptions
- [ ] Research questions addressed explicitly
- [ ] Mechanism and derivations placed in methods/appendices, not the main argument

**Sentence Quality (Pass 2)**:
- [ ] Sentence length distribution approximates 70/20/10 target
- [ ] Sentence openings vary across patterns
- [ ] Simple, compound, and complex types all present
- [ ] No sequences of identically structured sentences
- [ ] Adjacent sentences vary in opener and length; read aloud to confirm pace

**Precision (Pass 3)**:
- [ ] Technical terms accurate, consistent, and defined on first use
- [ ] Hedging calibrated to evidence strength
- [ ] No unnecessary jargon or inflated vocabulary
- [ ] Each concept keeps a single name throughout (no synonyms)
- [ ] Register fits the least-specialist intended reader; plain paraphrase preferred over opaque jargon
- [ ] Nominalizations replaced with verb-based constructions

**Tone (Pass 4)**:
- [ ] No negation-for-drama or filler phrases
- [ ] Claims proportional to evidence
- [ ] Tone objective but engaging
- [ ] Formulaic expressions eliminated
