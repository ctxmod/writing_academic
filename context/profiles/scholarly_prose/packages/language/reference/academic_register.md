# Accessible Register

Register is the level of specialized vocabulary and assumed background a passage demands of its reader. Calibrate it to the least-specialist reader the passage is written for, not to the author's own fluency. The author who knows the material reads past the jargon effortlessly; the intended reader does not. Register is the most common gap between a writer who understands their subject and a reader who is trying to.

## Write to the Least-Specialist Intended Reader

The main argument of a research document is typically addressed to a reader who is competent but not a specialist in the author's narrow subfield: an examiner, a reviewer from an adjacent area, a practitioner. Write the running text for that reader. Reserve the specialist register for the parts the specialist will seek out (methods, appendices, supplementary material).

A diagnostic: when a domain expert outside the immediate subfield reads a passage and cannot follow it, the passage is mis-registered even if every word is technically correct. Correctness and accessibility are independent; a sentence can be fully accurate and fully opaque.

## Calibrate to the Fresh Reader

The reader to calibrate for is a smart reader who has not seen this material — not careless, but new. Intelligence is not the gap; missing context is, and context lives on the page or it does not exist. For agent-consumed artifacts the intended reader is a fresh session with zero prior context — no memory of the thread that produced the text, no side knowledge of the codebase or its decision history — so write so that reader can act: every term bound at first use, every claim self-sufficient, nothing leaning on what the author happens to remember.

Mirroring is the second half of calibration. When the consumer's side of the exchange has already fixed a term, carry that established term forward instead of substituting a synonym, and match the register the thread has already set. A synonym is not neutral variety; it forces the reader to re-bind a concept they already hold and to wonder whether the new word means something subtly different. The established term costs the reader nothing, which is the entire point.

Calibration is silent. Never state or imply that the text was simplified or register-matched — no "in plain terms", no "simply put", no meta-commentary on the text's own level. Announced simplification tells the reader they are being managed and spends trust the plain wording should have earned; the calibrated text just reads plainly.

## Earn Every Technical Term

A technical term is a debt the reader pays in working memory. Introduce a term only when it does work the plain language cannot, and only after the reader can afford it. The strong pattern is to motivate before formalizing: state the problem and its stakes in ordinary words, then introduce the apparatus that addresses it.

Strong scientific writing routinely restates formal content in plain words immediately after presenting it. After an equation, a clause such as "in other words, one does not need to compute the denominator" tells the reader what the symbols *mean*; that restatement, not the equation, is what most readers actually use. The formalism earns its place precisely because the plain restatement carries the meaning alongside it.

## Prefer the Plain Paraphrase

When a plain everyday word conveys the meaning, use it and omit the technical term from the accessible text entirely.

| Opaque term | Plain paraphrase for the main text |
| ----------- | ---------------------------------- |
| "the model's weights / parameters" | "what the model has learned" |
| "produces an embedding" | "produces a summary of the input" |
| "continued pretraining on the corpus" | "training the model further on the new records" |
| "out-of-vocabulary events are dropped" | "events the model has no code for are silently ignored" |

**Name-and-gloss is not enough.** Writing "the model produces an *embedding* (a dense numerical vector)" still forces the reader to bind the hard word before continuing. If the plain word carries the meaning, the parenthetical gloss is wasted and the hard word is noise. Glossing in place is a fallback for terms that are genuinely load-bearing and unavoidable, not a license to keep jargon the argument does not need.

## Register Stratification

A document carries more than one register at once. The accessible main text states what things mean for the argument; the deepest internals — derivations, implementation detail, exhaustive parameter lists — live in methods sections and appendices, where the reader who wants them opts in. Stratifying register this way lets the main text stay readable without discarding rigor: the rigor is present, one layer down, reachable by reference.

This division must be honored, not merely declared. A main text that promises "the technical detail is in the appendices" and then imports appendix-level mechanism into a body paragraph breaks the promise exactly where the reader trusted it.

## A Glossary Is Not Comprehension

A reader does not interrupt a sentence to consult the back matter. A definition the reader must go find is a definition the reader does not have while reading the sentence that needs it. Terms fully defined in a glossary still draw confusion when used cold in the body, because comprehension happens in line, in the moment of reading.

The ordered remedy: (a) the passage avoids the term; (b) if the term is unavoidable, the passage carries the meaning in plain words at the point of use; (c) the term and its formal definition live in the glossary and appendices for the reader who opts in — never as the sole site of explanation. See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/terminology.md" /> for the onboarding mechanics and <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/depth_placement.md" /> for what to relocate.

## Anti-Patterns

| Anti-Pattern | Signal | Alternative |
| ------------ | ------ | ----------- |
| Writing to the author's fluency | Specialist could follow; intended reader cannot | Calibrate to the least-specialist intended reader |
| Jargon the argument does not need | Term appears once, does no work, carries a gloss | Delete the term; use the plain word |
| Name-and-gloss reflex | "the *embedding* (a dense vector)" where "summary" suffices | Use the plain word; omit the hard term |
| Glossary as comprehension mechanism | Hard term used cold, "defined in the glossary" | Carry meaning in line at first use |
| Declared-but-broken stratification | Body imports appendix-level mechanism | Keep the consequence in the body, mechanism in the appendix |
| Writer-announced simplification | "In plain terms…" framing | Calibrate silently; the text just reads plainly |
| Synonym drift mid-thread | Reader must re-bind terms between artifacts | Reuse the established term |

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_language.md" />.
See `clarity_principles` (module `writing`, profile `core`, package `basics`).
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/concreteness.md" />.
