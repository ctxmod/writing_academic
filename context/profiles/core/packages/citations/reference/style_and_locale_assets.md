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
