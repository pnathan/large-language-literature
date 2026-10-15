# Sappho edition: design proposal

Mockup: `design/sappho/mockup/index.html`. It shows the fragment index and Fr. 58 (the Tithonus poem). All Greek, English, witness data and variants come from `docs/sappho/index.html`.

## What the current page does, and what it gets wrong

The sticky index shows ordinals, not fragment numbers: "16" leads to Fr. 58. It marks no current fragment. On a phone it takes about 290 px of an 844 px screen, permanently. The apparatus summaries are 12 px, too small to tap. Brackets look like the rest of the Greek, so papyrus letters and editors' letters cannot be told apart.

## Period cues, and why

- **Vase painting gives the palette.** Black-figure puts black glaze on clay; red-figure reverses it. The light theme is black-figure, the dark theme red-figure: two historical techniques, not one palette inverted. Added red (*miltos*), used sparingly by painters for details, colours the brackets.
- **The papyrus decides the notation.** Rolls lose their edges first, so line-beginnings and line-ends survive in different scraps. In Fr. 58 the Cologne roll keeps beginnings and the Oxyrhynchus roll keeps ends. A coverage map shows this: one row per witness, one cell per line, each cell split into beginning and end, damage hatched.
- **Editors' letters look different.** Inside `[ ]` and `⟨ ⟩` the Greek is muted brown and the brackets red; papyrus letters stay in full ink; underdots stay; illegible traces (`. . .`) are muted. A reader sees at once how much of a line is Sappho's.
- **The printed critical edition gives the apparatus form.** Line number, readings, sigla, and a mark on the reading printed. The line number links to the line and highlights it.

## Type

| Role | Family | Size, desktop / phone |
|---|---|---|
| Greek text | Gentium Book Plus (Noto Serif, GFS Didot fallback) | 19 / 18.5 px, line-height 1.5 |
| English text, titles | EB Garamond | 18 / 17.5 px; h1 44 / 34 px |
| Interface, apparatus, notes | Inter | 15 (notes), 14 (apparatus), 12–13 (meta), 11–12 (caps labels) |

Gentium was built for scholarly Greek: full polytonic coverage, correct placement of combining underdots, and a Book weight that holds up on screens. Garamond matches its colour, so neither language looks foreign beside the other. Glyphs Inter lacks fall back to Gentium. The scale steps by about 1.2.

## Colour tokens

| Token | Light (black-figure) | Dark (red-figure) | Use |
|---|---|---|---|
| `--ground` | `#f3eadc` | `#13100d` | body background |
| `--sheet` | `#fbf7f0` | `#1b1713` | apparatus rail, sheet, cards |
| `--panel` | `#ece0cc` | `#2a231d` | current index row, counts |
| `--ink` | `#1e1915` | `#f0e6d6` | Greek, headings |
| `--ink-2` | `#4f4136` | `#cdbba5` | English, body notes |
| `--ink-3` | `#6e5c4d` | `#a8957f` | meta, captions |
| `--clay` | `#b0532b` | `#d4865a` | current-item bar, focus ring |
| `--accent` | `#963f1c` | `#e49a6f` | text links, line refs |
| `--miltos` | `#8a2a1c` | `#e8806a` | brackets, lacunae |
| `--supp` | `#7a6450` | `#b59f88` | supplied letters |

Every text token meets 4.5:1; the lowest is `--supp` on `--ground`, 4.68. Dark applies under `prefers-color-scheme: dark` guarded by `:root:not([data-theme="light"])`, and under `:root[data-theme="dark"]`. The header button sets `data-theme`.

## Layout by page type

**Index.** A 256 px left column that scrolls on its own and opens centred on the current fragment. Each row: real fragment number (58, 98a–b, 168B), short title, lines and witnesses, and a chip, Π for papyrus or parchment, Q (dashed) for quotation. The current row has a panel background, a clay bar and `aria-current`. "rev." marks fragments revised after review. Filters (All, Π, Q) work through CSS `:has()`. A landing index would use the same rows at full width.

**Fragment.** Header: position, number and title, the project's note, sigla, previous/next. Then the coverage map, then numbered lines in a grid: number, Greek (1.25 fr), English (1 fr). Wrapped lines hang, so each verse stays one unit. A Both / Greek / English switch gives one language the full width. A notation key and a titled pager close the page.

**Apparatus.** A 344 px right rail with three disclosures: Witnesses (count), Variants (count), Translator's note. Each witness shows siglum, linked name, type (papyrus roll, quotation, modern compilation), date and what it preserves. Sourcing caveats, such as the Athenaeus Greek that could not be re-fetched, get a red-ruled box.

## Behaviour

| | Desktop ≥ 1200 px | 900–1199 px | Phone < 900 px |
|---|---|---|---|
| Index | sticky left column | sticky left column | bottom sheet, opened by "Fr. 58 · 16 of 33" in the top bar |
| Apparatus | right rail, open; "Apparatus" button hides it and the text widens | block below the text, folded | block below the text, folded, counts visible |
| Greek/English | side by side | side by side | stacked, Greek first, per line |

The phone sheet takes up to 82 % of the height, with a grab bar (visual only), a 44 px close button and sticky filters. It closes on Escape, the scrim or a choice, and returns focus to its button. Every phone control is at least 44 × 44 px, line numbers and witness links included. Verified with Playwright: at 1440 × 900 and at 390 × 844, `scrollWidth − clientWidth` is 0, and it stays 0 with the sheet open.

## What I excluded

Greek-key borders, columns, amphora drawings, marble, torn-paper edges, lyre icons, portraits of Sappho, and lettering that imitates inscriptions. The fragment shows damage through its brackets and the coverage map, not decoration. No CDN scripts; a small inline script runs the theme, sheet and apparatus toggle, and the page reads without it.

## Open questions

1. The coverage map uses the witness notes at line level (beginning or end). The printed text shows that the opening lines' beginnings are themselves supplements. Should the map be built per letter from the bracket positions instead? That needs data the builder does not have.
2. "Q" for quotation is a plain-English siglum of my own. Is there a preferred abbreviation, such as *test.*?
3. Modern compilations (Wikipedia, Wharton, Edmonds) appear in the witness lists of many fragments. Should the index count only ancient witnesses?
4. Variants are written as paragraphs in `fragments.json`. A lemma-style apparatus needs them broken into structured records (line, lemma, readings, sources). Do this by hand, or add a field to the data?
5. Should the published page keep one long scroll with this chrome, or render one fragment per view with hash routing? The mockup supports both. One fragment per view makes the index state exact.
6. On the phone, should the apparatus come before the pager? The mockup places it after.
