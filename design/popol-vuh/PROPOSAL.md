# Popol Vuh edition: design proposal

Mockup: `mockup/index.html`. It holds the title page, the full contents, and section 01 (Multepal p01–p05, fol. 1r–2v) in all three registers. All text comes from `popol-vuh/src` and the published page.

## What the current page does

- English only on the surface. The K'iche' and Spanish sit in a closed disclosure after each section.
- No folio references. `sections.json` has empty `folios`, though the TEI marks every page side with `<pb>`.
- The nav reaches the four parts, not the 36 sections.
- Spectral lacks ꜩ, ꜫ, ꜭ and Ɛ, so one K'iche' word is set in two typefaces.
- The jade-and-gold palette and the ✥ sigil suggest an invented Maya look.

## Period cues

1. **Ayer MS 1515.** K'iche' left column, Spanish right. A leaf number in the right margin of each recto. Chapter heads and numbers in the left margin ("cap. 1. del ser de Dios", "3. prover. Cap. 8.", a cross-reference to Proverbs 8). Line-end hyphens. Incipits in capitals.
2. **The Spanish printed page of the period.** A Garamond-lineage roman. Red for titles, here the `--rubric` token. Small capitals for heads. A *tabla* with dot leaders and folio numbers.
3. **The diplomatic edition.** Line numbers by fives. Folio breaks marked in the text. Apparatus in the margin.

## Type

One family: **EB Garamond** (Google Fonts; 400, 500, 600, italic 400), from the Garamond types used in Spanish printing. It has every colonial letter in the transcription: Ꜩ U+A728, ꜩ U+A729, ꜫ U+A72B, ꜭ U+A72D, Ɛ U+0190, ÿ, ç. Chrome's `CSS.getPlatformFontsForNode` confirms every K'iche' run in the mockup renders from EB Garamond with no fallback glyphs. Small capitals use `all-small-caps`. Prose has old-style figures; labels and folios have lining tabular figures.

| Role | Desktop | Phone |
|---|---|---|
| Title (small caps, tracked .14em) | 44 | 34 |
| Passage title | 32 | 27 |
| Part title (contents) | 22 | 21 |
| K'iche' running text, English | 19 / 1.62 | 18 / 1.6 |
| K'iche' as written (lines) | 17.5 / 1.55 | 17 |
| Apparatus, contents rows | 15.5–18 | 15.5–17 |
| Labels, small caps | 14–16 | 14–15 |
| Line numbers, marginalia | 12.5–13 | 12–13 |

## Colour tokens

Paper, iron-gall ink, red rubrication. Contrast is against `--paper`.

| Token | Light | Dark | Use | Contrast L / D |
|---|---|---|---|---|
| `--paper` | #F4EFE3 | #16130F | page | n/a |
| `--leaf` | #FAF7F0 | #1E1A15 | sheet, open apparatus | n/a |
| `--ink` | #231C14 | #EAE1CF | text | 14.7 / 14.3 |
| `--ink-2` | #4C4032 | #C3B69D | Spanish, notes | 8.8 / 9.3 |
| `--ink-3` | #6B5D49 | #9E917A | labels, line numbers, control borders | 5.6 / 6.0 |
| `--rubric` | #9A2B1B | #E3907A | part labels, folios, current item | 6.7 / 7.5 |
| `--rule` | #D6CAB2 | #3A3329 | hairlines (decorative) | n/a |
| `--wash` | #E9E0CC | #29231C | hover, quiet fill | n/a |

The dark tokens sit under `@media (prefers-color-scheme: dark)`, guarded by `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. `body` sets `background: var(--paper)`.

## Page types

**Title and contents.** The title page sets the manuscript's first two lines three ways: K'iche' (fol. 1r, ll. 1–2), Ximénez's Spanish, and this edition's English, side by side on desktop, stacked on a phone. The reader sees the three registers before the text. The contents is a *tabla*: red roman numeral, part title, one-line gloss; then rows of number, title, dot leaders, and the folio where the section begins (from the TEI). Rows are at least 44 px tall. Phones drop the leaders.

**Passage.** The head gives part, title, and citation ("§ 01 · Multepal p01–p05 · Ayer MS 1515, vol. 2, fol. 1r–2v"), then the translator's note as a closed disclosure. The text is cut into *blocks*: manuscript paragraphs matched to a run of English paragraphs (s01: p01–02, p03–04, p05). Each block is one grid row.

- At ≥1200 px: folio gutter | K'iche' | English | apparatus (19rem). The gutter shows the folio range in red and is sticky, as are the column heads.
- At 760–1199 px the apparatus drops below each block as a closed disclosure.
- Below 760 px the block is one column: a red "fol. 1r–1v · p01–02" line, then the K'iche', then the English, then the apparatus disclosure.

The K'iche' has two layouts. **Running** joins the lines and resolves line-end hyphens; spelling is untouched. **As written** gives one manuscript line per row, numbered by fives and at each paragraph or folio start, with the hyphen shown and the marginal notes at their line, broken as in the manuscript. Both mark folio changes in red ("fol. 1v") where they fall.

**Apparatus** (per block): citation with folio and line ranges; marginalia and leaf numbers with their place; "Names in this block" (manuscript spelling → Multepal entity key, e.g. *tepeu, qucumaꜩ → Tepew Q'ukumatz*); and Ximénez's Spanish for those paragraphs. The last two are nested disclosures.

## Registers and controls

- **Desktop and tablet.** Three toggle buttons (`aria-pressed`) in the bar: K'iche', English, Apparatus. One text register always stays on. The grid closes up around what remains, keeping a 30–36 rem measure. A theme button cycles Auto → Light → Dark.
- **Phone.** One 60 px bar: a "§ 01 / fol. 1r" button and a segmented control, K'iche' | English | Both. In Both, small-caps labels name each register. Apparatus on/off, K'iche' layout and theme sit in the section sheet.
- **Folio always visible.** The bar button shows the current section and folio, updated on scroll from the folio markers. The gutter or block head repeats it.
- **Section jump.** The bar button opens a `popover` sheet: 36 numbered cells by part, each at least 44 px. Two taps reach any section. Each passage ends with "← Contents" and "§ 02 →".

State persists in `localStorage` inside `try/catch`. Without JavaScript every register shows, the apparatus is open, and the theme follows the system. No external scripts; one inline script of about 65 lines. At 390 × 844 the page has no horizontal overflow in any state tested, and no control is under 44 × 44 px.

## Excluded, and why

- **Glyphs, pseudo-codex frames, fret borders, "Maya" greens.** The witness is a Latin-letter colonial manuscript. Codex decoration claims a provenance it lacks and turns a living tradition into ornament.
- **Paper textures, foxing, script fonts.** No information, less contrast.
- **The ✥ sigil.** Nothing in the manuscript supports it.
- **Cards and shadows.** Rules and margins separate things, as on a printed page.
- **Facsimile images.** Public domain (LOC), but too large for a one-file mockup.

## Open questions

1. **Alignment.** Translations are stored per section. I grouped blocks by reading K'iche', Spanish and English together. The build needs a reviewed map: block → paragraph ids → English paragraph indexes.
2. **Normalised K'iche'.** The repo has none beyond the Multepal entity keys, and I did not invent one. Adding one (say, in ALMG orthography) is for K'iche' speakers and scholars to decide.
3. **Spanish as a fourth column?** It sits in the apparatus because it is a witness, not the object of translation.
4. **Glottal mark.** Decided: use ASCII `'` (as the data does, e.g. Wuqub' Kaqix). No conversion to U+02BC. The build leaves `'` untouched and does not smart-quote it; only English quotation marks and contractions become typographic.
5. **Anchors.** The TEI puts marginal notes between lines; the apparatus cites the line before. K'iche' p34 and p58 lack `xml:id`, so s25's start folio comes from the Spanish column.
6. **Facsimile links.** Each folio label could open the LOC page image, given a URL map per page side.
7. **Orthography.** Decided: the design's own titles and prose use "K'iche'" and "Hunahpu", the forms the project's source files use more often (K'iche' 1,180 vs Quiche/Quiché 659; Hunahpu 881 vs Junajpu 306, counted across `popol-vuh/`). Quoted manuscript and translation text keeps its own spelling.
