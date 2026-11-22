# Terminology Discipline

A reader learning a concept holds its name in working memory while binding it to its meaning. Every additional name for the same concept, and every term used before it is defined, taxes that memory directly. Two disciplines control the tax: name each concept once, and introduce each term before its first use, in the place it is used. This is among the highest-leverage interventions in technical prose, because the cost is paid silently — the reader does not report confusion, they simply lose the thread.

## One Concept, One Name

Pick one canonical word for each concept and use only that word throughout the running text. Synonyms that an author treats as free variation read to a learning reader as *distinct concepts*. When a reader has to ask whether two of your words mean the same thing, the cost has already been paid: they were maintaining a mental synonym table instead of following the argument.

| Concept | Pick one canonical name | Banish the rest to appendix / glossary |
| ------- | ----------------------- | -------------------------------------- |
| the vector a model emits | "summary" | embedding, representation, activation, 768-d vector |
| the model's learned numbers | (paraphrase: "what the model learned") | weights, parameters |
| the per-task readout model | "a small task-specific model" | probe, classifier, classifier head |
| the code-translation step | "mapping" | align, alignment, crosswalk |

The practice is mechanical and enforceable: maintain a one-concept-one-word table for the document, and before each submission, search the running text for the banished synonyms. A renamed thing reads as a new thing; consistency is not pedantry but comprehension.

This is the operational form of the consistency rule in <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_language.md" />: the same term for the same concept, every time.

## Introduce Before Use, at the Point of Use

A term must be defined at or before its first appearance, never pages later in the same chapter. The reader meets the word once; that meeting must include its meaning. A definition that arrives after several uses arrives too late — the reader has already either guessed or stalled.

Strong writing defines terms inline in the sentence that first needs them: "Here *independent* means that each pair of sets is drawn separately from the others" sits exactly where "independent" is first load-bearing. The gloss costs one clause and saves the reader the search.

## Definitions Live Where They Are Read

Comprehension happens in line, in the moment of reading, not in a round trip to the back matter. A first-use inline gloss is worth more than a complete glossary entry, because the reader has the meaning while reading the sentence that depends on it. A glossary is a reference for the reader who already understands and wants to confirm; it is not the mechanism by which a reader first understands. See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_register.md" />.

## No Orphan Terms

A term may not be introduced for the first time, or exist solely, in a figure, a table, or its caption. Exhibits are read out of order and skimmed; a named study, metric, or term that appears only there has no anchor in the argument. Every term and named entity in an exhibit must already appear and be glossed in the running prose. Audit each figure and table for orphan terminology before submission. The reciprocal obligation on the exhibit side is covered in <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/exhibits.md" />.

## Anti-Patterns

| Anti-Pattern | Consequence | Alternative |
| ------------ | ----------- | ----------- |
| Synonym proliferation | Reader maintains a synonym table instead of following the argument | One canonical name per concept; grep the banished words |
| Renaming mid-document | A renamed thing reads as a new thing | Fix the name once; reuse it verbatim |
| Define-after-use | Reader guesses or stalls at first appearance | Gloss inline at or before first use |
| Glossary-only definition | Reader does not have the meaning while reading | Inline gloss at the point of use |
| Orphan term in an exhibit | Term has no anchor in the argument | Introduce and gloss in prose first |

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_language.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_register.md" />.
See `clarity_principles` (module `writing`, profile `core`, package `basics`).
