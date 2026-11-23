# Style Selection Across the Disciplines

Four format families cover the disciplines this module serves. Each
discipline profile carries one family's practice; this reference is the
navigation layer that says which profile carries which family and how
to choose when a venue does not name its style.

## The discipline table

| Discipline | Style | In-text shape | Closing list |
| --- | --- | --- | --- |
| Psychology and the social sciences | APA 7 | author and year | reference list, alphabetical |
| The humanities | MLA 9 | author and page | works-cited list, alphabetical |
| History and general scholarship | Chicago 18 | notes or author-date | bibliography or reference list |
| Engineering and the technical sciences | IEEE | bracketed number | numbered reference list |

Each family also serves its neighbouring fields, for a reason its
in-text shape makes visible. APA 7 serves education and the health
sciences as well, and its author-date shape foregrounds recency. MLA 9's
author-page shape serves textual analysis in literature and languages,
where the reader needs the passage, not the year. Chicago 18 serves the
arts beside history. IEEE's bracketed number is chosen for concision
and serves computer science as well as engineering.

Chicago 18 is one style with two systems. Notes-bibliography cites
through numbered notes in first-appearance order with an alphabetical
bibliography; author-date cites through author-year pairs with an
alphabetical reference list. Both systems belong to the style manual's
conventions for typeset documents. The `chicago` profile carries both,
plus the verification practice that settles which system a venue
expects.

## The editions in force

As of November 2026 the current editions are the APA Publication
Manual, 7th edition (2019); the MLA Handbook, 9th edition (2021); the
Chicago Manual of Style, 18th edition (2024); and the IEEE Reference
Guide, version 3.28.2025. Each publisher also issues guidance between
editions, such as the AI-citation formats in the `Citing AI-Generated
Content` reference. A venue that still asks for an older edition, such
as Chicago 17, is followed; the benchmark below shows which edition its
recent issues actually use.

## The selection precedence

When the venue's author instructions name a style, that naming wins.
When they do not, disciplinary convention supplies the default from the
table, and the footnote-versus-author-date check applies where a style
has two systems. The full procedure, including the ten-to-fifteen
publication benchmark for doubtful cases, is the `Benchmark Before
Choosing` rule in this package.

## What each profile carries

Each discipline profile extends this core and adds one `practice`
package: the family's in-text shape and list shape at the format-family
level, and a navigation reference for the profile's own scope. The
profiles teach the style manuals' conventions for typeset documents.
ctxmod's own citation machinery is a fixed, style-independent posture
(named markers over a name-sorted footnotes list), taught once in the
`Style and Locale Assets` reference, so the machinery's behavior and
the styles' conventions are never conflated.

## Sources

- https://www.chicagomanualofstyle.org/help-tools/what-s-new.html —
  CMOS 18th edition (2024) change list; accessed 2026-11-23.
- https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Reference_Guide.pdf
  — IEEE Reference Guide, now served as a shared document marked
  V 3.28.2025; accessed 2026-11-23.
- https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_changes_9th_edition.html
  — MLA Handbook 9th edition (2021) as the current edition; accessed
  2026-11-23.
- https://apastyle.apa.org/blog/cite-generative-ai-references — APA
  Style guidance updated within the 7th edition (September 2025);
  accessed 2026-11-23.
