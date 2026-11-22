# Concrete Illustration

Abstractions are understood through instances. A definition states what a thing is; a worked example shows the reader what it does, and the showing is usually what makes it stick. Ground each abstract claim, definition, or quantity in a specific instance — ideally with real numbers — at or immediately after the point where it is stated. Concreteness is not decoration; it is often the actual mechanism of understanding.

## Anchor Abstractions in Worked Numbers

After stating an abstract result, give one concrete instance with real values. The instance does explanatory work the definition cannot.

Compare a bare statement — "the credibility interval is wide for small test sets" — with its worked form: "after 4 errors in 20 test cases, the 95% interval runs from 7% to 40%; the point estimate is 20%, but a true error rate as bad as 40% cannot be ruled out." The numbers make the abstraction's stakes immediate. A reader who skims the general claim cannot skim the concrete one without absorbing it.

Define derived quantities the same way — by working one instance through. A term like "relative gain" stays abstract until a number is pushed through it: "when the conventional interval has length 30% and the refined one has length 24%, the absolute gain is 6 percentage points and the relative gain is 20%." The single worked line fixes the definition more firmly than a formula, because the reader watches the quantity being computed rather than being told its rule. Pair the worked instance with the formal definition; do not make the reader choose between them.

## Give the Reader a Rule of Thumb

Where a relationship governs practice, hand the reader an operational handle they can carry away. "To keep the interval shorter than 10 percentage points, you need on the order of 350 test cases" converts a theoretical dependence into something a reader can act on. Rules of thumb are concreteness aimed at use rather than at intuition.

A rule of thumb gains force when its worst case is made concrete. Following "you need on the order of 350 test cases" with "the worst case is 175 errors, giving the interval [45%, 55%] — any other result narrows it" shows the reader the boundary the rule is built from, so they trust the threshold rather than memorizing it. The worked extreme is the proof that the round number is not arbitrary.

## Use a Scenario to Justify a Choice

When a methodological choice needs motivating, a single vivid scenario justifies it faster than abstract argument. To argue that per-class error rates must be reported separately rather than averaged: "an average error of 20% can hide 0% errors on one class and 40% on the other — and 40% may be unacceptable where the 20% average looked fine." The scenario makes the failure mode the choice guards against visible, so the choice reads as necessary rather than fastidious.

A scenario can also expose an unavoidable trade-off the reader would otherwise overlook, by walking both extremes in concrete terms. To show that performance and the certainty of its estimate pull against each other: "use every available example for design and you get the best possible classifier — but almost nothing left to test it on, so its true performance stays maximally uncertain; reserve almost everything for testing and you pin the performance down precisely — but the classifier trained on the remainder is too weak to be worth measuring." Naming both poles in plain consequences makes the dilemma self-evident; no formal argument is needed for the reader to see that the optimum lies in tension.

## Input/Output Examples for Systems and Models

For any system, model, or transformation, show one concrete input and the corresponding output. A reader grasps "the model reads a patient's coded events in time order and outputs a summary used to predict the next event" far better when accompanied by a short example sequence and what comes out of it. One worked input/output pair resolves more confusion than several paragraphs describing the interface in the abstract.

## Place the Example Where the Abstraction Is

A concrete instance delivered pages after the claim it illustrates has lost most of its value. Pair the example with the abstraction: state the claim, then immediately show the instance, before the reader has moved on. The proximity is part of the technique — the example answers the question the abstraction just raised, while it is still open.

## Anti-Patterns

| Anti-Pattern | Consequence | Alternative |
| ------------ | ----------- | ----------- |
| Abstraction without instance | Reader nods without understanding | Follow each claim with a worked example |
| Definition where a number would teach | The stakes stay invisible | Give real values; show what they imply |
| Theory with no operational handle | Reader cannot act on the result | Supply a rule of thumb |
| Describing an interface abstractly | Reader cannot picture the behavior | Show one concrete input and its output |
| Example far from its claim | Illustration arrives after the question closed | Place the instance beside the abstraction |

See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::language@scholarly_prose/reference/academic_register.md" />.
See <ctxmod_path path="ctx:github.com/ctxmod/writing_academic/context::shared::composition@scholarly_prose/reference/exhibits.md" />.
See `clarity_principles` (module `writing`, profile `core`, package `basics`).
