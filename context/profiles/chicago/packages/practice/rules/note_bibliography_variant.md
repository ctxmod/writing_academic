# Chicago 18: The Notes-Bibliography Variant

Chicago 18's notes-bibliography system cites through numbered
footnotes. Each citation site carries a superscript number, the notes
are numbered in first-appearance order through the document, and each
note carries the source's details with its page locator. The closing
list is a bibliography ordered alphabetically by family name; the
numbering lives in the document's notes, never in the bibliography
itself.

## Repeat citations use shortened notes

The first note for a source gives the full citation. Later notes for
the same source give a shortened note: the author's family name and a
short title, with the locator (Strand, *Archive of Delays*, 42).
Chicago 18 discourages "ibid." because it can obscure which source a
note means, especially in electronic formats that show one note at a
time; a shortened note takes no more space. A note names the first
author and "et al." when a work has more than two authors. The
bibliography names up to six authors, and for more than six it gives
the first three followed by "et al."

## The convention's own posture

These are the style manual's conventions for typeset documents:
first-appearance numbering and the superscript mark belong to the
printed page. ctxmod's own rendering is a fixed, style-independent
posture, citations rendering as named markers over a name-sorted
footnotes list, and no rendering step today numbers citations by
first appearance. Stating the two in one breath is deliberate: a
document that follows the manual's convention and a rendering step
that follows the machinery's fixed posture are different layers, and
neither claims the other's behavior.

## Holding the variant

A document in this variant carries one system throughout: notes
everywhere, a bibliography at the end, no author-date pairs. Mixing a
note system with an author-date sentence is the mixed-style drift the
core package's `Hold One Style` rule exists to catch.
