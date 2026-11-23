# Style and Locale Assets

Citation styles and locales are carried assets in this tool's
composition model. A style asset lives under
`assets/citation_style/<name>/` and a locale asset under
`assets/citation_locale/<name>/`, wherever their owning module, profile,
or package places them. Composition resolution follows the standard
precedence: owners deeper in the composition override shallower ones
for the same name. The assets themselves are never authored here:
styles and locales arrive upstream-pinned, cached device-locally, and
attribution metadata rides with every cached entry, so a composition
that supplies no assets still resolves the embedded defaults — an
English locale and the default APA 7 style — from the pin.

## The pipeline

The citation renderer is the CSL/Hayagriva pipeline. Rendered entries
carry a real style commitment: the tool parses the pinned CSL style
once per render session, loads the pinned locale files the cited
sources' languages select (a Swedish-language source selects the pinned
sv locale, whose terms and locator labels then render), drives one
citation-request session over the render's citations, and the rendered
bibliography entries are the footnotes list's source entries. The pin
of record is tag v1.0.2 of the citation-style-language styles and
locales repositories; the device-local cache is keyed by that pin, is
rebuildable from the pinned URLs alone, and rendering reads only the
cache — the fetch is a one-time acquisition that populates it, never a
per-render act. No CSL or locale bytes are authored or vendored in this
repository.

## Editions at the pin

Each pinned style file names the manual edition it implements in its
own `<title>`, and the editions differ across the set:

| Asset label | Upstream file | Edition the file declares |
| --- | --- | --- |
| `apa` | `apa.csl` | APA Style 7th edition |
| `chicago_author_date` | `chicago-author-date.csl` | Chicago Manual of Style 18th edition (author-date) |
| `chicago_note_bibliography` | `chicago-note-bibliography.csl` | Chicago Manual of Style 17th edition (note) |
| `ieee` | `ieee.csl` | IEEE Reference Guide version 11.29.2023 |
| `mla` | `modern-language-association.csl` | MLA Handbook 9th edition |

Two of these trail the current manuals: the notes style renders
Chicago 17 notes, where Chicago 18 changed "et al." thresholds and
prefers shortened notes to "ibid.", and the IEEE file predates the
guide's version 3.28.2025. Upstream, the 18th-edition notes styles are
`chicago-notes-bibliography.csl` and
`chicago-shortened-notes-bibliography.csl`. Re-pinning is a deliberate
machinery decision, never a content edit; until then, a typeset
document held to Chicago 18 notes is checked against the manual, not
against the rendered output.

## The fixed machinery posture

Two properties of the citation machinery hold regardless of which
citation style a document follows. Citations resolve to the cited
target's qualified name, and the rendered footnotes list keys each
entry by that same qualified name, sorted by name for stable diffs;
markers are named `[^<qualified_name>, locator]` with the authored
locator expression kept inline at the citation site, and the list stays
locator-free. Locator expressions parse on the tool's side into a
structured category plus value before citation formatting sees them.
The styles' conventions bind the typeset document; the machinery's
posture binds the rendering step; neither claims the other's behavior.

## Sources

- https://raw.githubusercontent.com/citation-style-language/styles/v1.0.2/chicago-note-bibliography.csl
  — the pinned notes style; its `<title>` reads "Chicago Manual of
  Style 17th edition (note)" and its byte count matches the pin's
  recorded count; accessed 2026-11-23.
- https://raw.githubusercontent.com/citation-style-language/styles/v1.0.2/chicago-author-date.csl
  — the pinned author-date style, titled for the 18th edition;
  accessed 2026-11-23.
- https://raw.githubusercontent.com/citation-style-language/styles/master/chicago-notes-bibliography.csl
  — the upstream 18th-edition notes-bibliography style; accessed
  2026-11-23.
- https://citationstyles.org/developers/ — CSL 1.0.2 (January 2022)
  as the current specification release; accessed 2026-11-23.
