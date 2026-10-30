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
| History and general scholarship | Chicago 17 | notes or author-date | bibliography or reference list |
| Engineering and the technical sciences | IEEE | bracketed number | numbered reference list |

Chicago 17 is one style with two systems. Notes-bibliography cites
through numbered notes in first-appearance order with an alphabetical
bibliography; author-date cites through author-year pairs with an
alphabetical reference list. Both systems belong to the style manual's
conventions for typeset documents. The `chicago` profile carries both,
plus the verification practice that settles which system a venue
expects.

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
