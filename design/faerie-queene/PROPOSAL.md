# The Faerie Queene: design proposal

Mockup: `mockup/index.html`, Book I, Canto I, stanzas i–v of 55, with argument, plate, contents, spelling switch and both themes.

## What the published page does

One 2.8 MB file: a dark frame, vellum-gradient sheets, IM Fell English body, SVG woodcut initials. It reads well on a desktop. On a 390 px phone the fixed Contents button covers the text, the to-top button covers the last line of a stanza, and a wrapped line returns to the indent of lines 2–8, so it looks like a new line ("Faerie / lond,"). The page holds only the modern text.

## Period cues, and why

1. **The 1590 quarto.** Roman verse, italic proper names (*Gloriana*), the argument as an italic quatrain between rules.
2. **Smith's 1909 page.** Stanza numerals in the right margin, so the eye runs from line to line, not into a number.
3. **Red ink.** One rubric token for headings, initials, variant line numbers and the current item. Nothing else is red.
4. **Black-letter, once.** Spenser's *Shepheardes Calender* (1579) was set in black-letter. The book title uses UnifrakturMaguntia; no other line does.
5. **The stanza as a unit of print.** Nine lines, lines 2–8 indented, the alexandrine flush. Nothing splits a stanza.
6. **Plates face the text.** The plate sits between the stanzas it shows, and its caption names them.

## Type

| Role | Family | Size (desktop / phone) |
|---|---|---|
| Verse, prose, captions | EB Garamond 400, 400 italic, 500 | 19 px / 17 px, line-height 1.5 |
| Canto title, rail title, book numerals | IM Fell English SC | canto 2.3 rem / 2.0 rem |
| Book title | UnifrakturMaguntia | 1.7 rem / 1.4 rem |
| Labels (running head, "The Argument") | EB Garamond 500, caps, tracked .16–.2 em | .72–.8 rem |
| Stanza numerals | EB Garamond, old-style figures | .82 rem |
| Variant notes | EB Garamond | .78 rem |

All from Google Fonts. EB Garamond replaces Fell for running text: Fell's rough edges blur at 17 px. Fell stays for small caps, where it is large enough. Scale: .72, .8, .86, 1, 1.35, 1.7, 2.3 rem, roughly 1.25 steps.

Measure: the verse column is 33 rem (627 px); the longest alexandrines (about 55 characters) never wrap at 1440 px. Prose pages use 29 rem, about 70 characters.

Wrapping: each line is a block with a hanging indent of 2.5 em (phone) or 1.6 em (desktop), deeper than Spenser's 1 em / 1.25 em indent, so a continuation never looks like a line start. At 390 px one line in five stanzas wraps.

## Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#f7f3ea` | `#16130f` | page, body background |
| `--paper-2` | `#efe9dc` | `#1d1914` | rail, sheet |
| `--ink` | `#1f1a14` | `#e8e0d0` | verse |
| `--ink-2` | `#584d3f` | `#b8ac96` | captions, argument incipits |
| `--ink-3` | `#71644f` | `#958a75` | numerals, running head |
| `--rule` | `#d6cbb6` | `#3a3128` | hairlines |
| `--rubric` | `#9b2b1d` | `#e08a72` | headings, initials, current item |
| `--plate-edge` | `#bfb197` | `#4a4034` | plate border |

Contrast: ink 15.6:1 (light), 14.1:1 (dark); rubric 6.9:1 and 7.1:1; the weakest pair, `--ink-3` on `--paper-2`, 4.8:1. Dark tokens apply under `prefers-color-scheme: dark` guarded by `:root:not([data-theme="light"])`, and under `:root[data-theme="dark"]`, which the theme button sets and stores. Paper is flat colour.

## Page types

**Landing.** Title in Fell SC, the 1590 title page (22 rem wide), editor and edition in one Garamond line, the Lewis epigraph. "Begin reading" goes to the proem; "Continue" appears when a last-read stanza is stored.

**Dedication.** Spenser's lapidary pyramid as real text, Fell SC at .95 rem, tracked .14 em, centred. The 1590 page image sits beside it on desktop and below it on a phone.

**Canto.** Book title (first canto of a book only), running head, canto title, fleuron, argument, stanzas. Previous and next controls at the foot carry each canto's argument incipit.

**Stanza.** Each stanza is addressable (`#s12`); its numeral is the link. In Original spelling, Smith's collation notes sit in the left margin on desktop and under the stanza on a phone, never between lines.

**Plate.** Between two stanzas, never inside one. Height is capped at `min(72vh, 34rem)` on desktop and 62vh on a phone, so the next stanza is a short scroll away. Tapping opens the full image. The caption gives title, artist, date, collection and the stanzas it faces. A back-matter index lists all 38 plates.

## Contents rail

At 1024 px and up the rail is a sticky 17.5 rem column: front matter, seven books as `<details>`, back matter. The current book is open, one row per canto with its argument's first line; other books show a grid of canto numerals. Every target is at least 44 px.

Below 1024 px the same `<nav>` is an HTML `popover`: a side sheet on tablets, a bottom sheet (85vh) on phones. It opens from the reading bar and closes on ×, Escape, an outside tap, or a chosen link. Only the last needs script.

## Spelling switch

The reading bar holds **Modern | Original** ("Orig." on a phone). Both readings are in the markup line by line; CSS shows one. The script notes the stanza at the top of the screen, switches, and restores that stanza to the same offset. Measured: zero movement on desktop. The choice is stored. Without script, the control is hidden and the modern text shows.

## Excluded

- Parchment, grain, deckle edges, text shadows.
- Black-letter below book-title level.
- The SVG woodcut initials: they misalign lines 1–3 and cost width on a phone. A raised rubric capital replaces them.
- The long s. Smith does not print it.
- Floating buttons over the text.

## Open questions

1. **Source of the Original layer.** Decided: both Project Gutenberg sources, #70717 and #72698, are the Original-spelling source. `faerie-queene/CLAUDE.md` and `faerie-queene/README.txt` both cite them as the edition's sources (J. C. Smith, Clarendon, 1909); neither file says which one supplies which book, so that split is not stated in the repo. The mockup's Original lines come from #70717. Approved: both Gutenberg files to be committed under `faerie-queene/` in the faerie-queene work's own PR. No files are committed here.
2. **Modernization errors.** In I.i the published text has *fare away* (Smith *farre*), *lassie* (*lasie*), *vel* (*vele*), *inward fare*, *prays* (*prayse*), *hi* (*hy*), *arr* (*arre*). The mockup reproduces stanzas i–v unchanged, so *vel* appears. Decided: the modernization errors are fixed in the faerie-queene work's own PR, not here.
3. **Residue.** To be fixed in the same PR, not here. The I.ix argument ends "tells:[295" (a footnote marker). The Note on the Text reads "3,8563,850 stanzas, some 34,700 linesnbsp;…".
4. **One file or seven.** A phone parses 2.8 MB to read one canto. One page per book keeps the rail and anchors.
5. **Variants in Modern mode.** Hidden in the mockup. Should they show?
6. **Blank screenshots.** Most supplied captures below the landing are blank, but the page renders when scrolled. It is probably a capture limit on a tall page; confirm.
