# IEEE Practice in This Profile

The `ieee` profile serves engineering and the technical sciences. It
extends the module core and adds one package, `practice`, whose two
rules carry the format-family level of the IEEE style: the numbered
in-text shape in square brackets, and the numbered reference list with
its completeness floor.

## Navigating the module

Style selection, when this family is the right choice, and the
benchmark procedure for doubtful cases, live in the core package's
`Style Selection Across the Disciplines` reference and the `Benchmark
Before Choosing` rule. This profile assumes the family is chosen and
carries its practice.

The deferred-pipeline posture for carried citation styles and locales
is taught once, in the core package's `Style and Locale Assets`
reference; no discipline profile carries style selection or asset
handling of its own.

## Metadata floor

Entry-level completeness is restated with the list shape in the `The
Numbered Reference List` rule: all authors, title, venue, year, DOI or
URL, and access dates for volatile web content. When sources are
stored as ctxmod sources, the same floor maps onto the source
metadata vocabulary: author, issued, title, container or publisher,
doi or url, accessed.

## Edition

The IEEE Reference Guide is versioned rather than numbered by
edition; the current version is 3.28.2025, published by IEEE
Publication Operations and now served from the IEEE Author Center as
a shared document. Its changes against version 11.29.2023 include
writing out reference ranges in the text (`[1], [2], [3]` rather than
`[1]–[3]`). The widely used `ieee.csl` style file still declares
version 11.29.2023, and it does not collapse ranges, so its in-text
output already matches the newer rule; check the closing list
against the guide.

## Sources

- https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Reference_Guide.pdf
  — IEEE Reference Guide V 3.28.2025 (the link resolves to the shared
  document): in-text ranges, "ibid." elimination, the six-author
  limit; accessed 2026-11-23.
- https://github.com/citation-style-language/styles/blob/master/ieee.csl
  — the CSL IEEE style, titled for Reference Guide version
  11.29.2023, with a non-collapsing citation layout; accessed
  2026-11-23.
