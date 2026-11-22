# Depth Placement

Every passage answers one of two questions: *what does this mean for the argument?* or *how is it built, derived, or implemented?* The first is consequence; the second is mechanism. The main line of argument carries consequences; mechanism belongs in methods sections, appendices, and supplementary material. Misplacing mechanism in the main text is the most common cause of a passage that is rigorous and unreadable at once.

## Consequence in the Main Text, Mechanism in the Appendix

Test each sentence against the two questions. If it answers "how is it built or derived" rather than "what does it mean for the reader," it belongs in supporting material, with a one-sentence consequence and a reference left behind in the main text.

Strong scientific writing does this routinely: a derivation is stated once in plain terms in the body — "this refinement shortens the interval" — with the algebra routed to an appendix ("see Appendix C for the derivation"). The body keeps the load-bearing claim; the reader who wants the mechanism follows the pointer. Numerical minutiae (solver settings, step sizes, tolerances) stay terse and out of the argument's way.

## Reduce Load, Don't Reword

When a passage is incomprehensible to its intended reader, the instinct is to rephrase it. Rephrasing re-clothes the same load; the reader needs *less* load. The correct move for an over-reaching passage is to cut it to its single load-bearing sentence and refer out to where the detail lives — not to say the same dense thing in different words.

Distinguish the two failure modes. A passage that is merely awkwardly worded needs editing at the same level of detail. A passage the intended reader cannot follow at all is over-reaching for its location: its detail must move, leaving one consequence sentence behind.

## An Opaque Sentence That Already Refers Out Is Redundant

If a sentence in the main text is both incomprehensible to its reader *and* ends in a pointer to where the detail lives ("…(see Appendix C)"), the appendix is already carrying the mechanism. The body sentence is duplicating, in compressed and unreadable form, what the appendix explains properly. Delete the body mechanism and keep only the plain consequence and the pointer. The refer-out is doing the work; let it.

## Completeness and Accessibility Are Different Axes

Adding correct detail raises completeness. It does not raise accessibility, and usually lowers it. A request to "explain X more" is ambiguous: it can mean *more thoroughly* (more mechanism) or *more accessibly* (more plain-language consequence). These pull in opposite directions. Explaining a thing more thoroughly in the main text — adding the missing derivation, the exact procedure, the full parameter set — frequently produces the densest, least readable passage in the document, precisely because the author was being responsive on the wrong axis.

When the gap is comprehension, the fix adds plain-language consequence and moves mechanism out; it does not add mechanism in.

## Anti-Patterns

| Anti-Pattern | Consequence | Alternative |
| ------------ | ----------- | ----------- |
| Mechanism in the main argument | Rigorous but unreadable body | Consequence in body, mechanism in appendix |
| Rewording an over-reaching passage | Same load, new clothes; reader still lost | Cut to one consequence sentence; refer out |
| Opaque sentence with a refer-out | Body duplicates the appendix unreadably | Delete the body mechanism; keep the pointer |
| Answering "explain more" with more mechanism | Densest passage in the document | Add plain consequence; relocate the detail |

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_register.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/composition.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/limitations.md" />.
