# The Faerie Queene: design proposal

Mockup: `mockup/index.html`. It shows Book I, Canto I, stanzas i–v of 55. It includes the argument, one plate, the contents control, the spelling switch and both themes.

## What the published page does

The page is a single 2.8 MB file. A dark "night and gilt" frame surrounds vellum-gradient sheets, the body is set in IM Fell English, and each canto opens with an SVG woodcut initial. It reads well on a desktop. On a 390 px phone it has three faults:

- The fixed Contents button sits over the first words of the text.
- A wrapped verse line returns to the indent of lines 2–8, so a continuation looks like a new line ("Faerie / lond,").
- The round to-top button covers the last line of a stanza.

The page also carries only the modern text. It has no original-spelling layer to switch to.

## Period cues, and why

1. **The 1590 quarto.** Roman type for the verse, italic for proper names (*Gloriana*, *Faerie*), and the argument set as an italic quatrain between rules. These carry meaning, so they stay.
2. **Smith's 1909 page.** Smith prints stanza numerals in the right margin, not before the stanza. The mockup does the same, so the eye goes from the end of a line straight to the next line and not to a number.
3. **Red ink.** Running heads, canto titles and initials in printed books were often rubricated. One red token marks headings, initials, variant line numbers and the current item. Nothing else is red.
4. **Black-letter, once.** *The Shepheardes Calender* (1579), Spenser's own earlier book, was set in black-letter. The book title ("The First Booke of the Faerie Queene") uses UnifrakturMaguntia, and no other line does.
5. **The stanza as a unit of print.** Nine lines, with lines 2–8 indented and the alexandrine flush. A stanza is never split by a plate, a note or a page control.
6. **Plates face the text.** An engraving in an illustrated edition faces the passage it shows. Here the plate sits between the stanzas it illustrates, and its caption names them ("faces stanzas iii–iv").

## Type

| Role | Family | Size (desktop / phone) |
|---|---|---|
| Verse, prose, captions | EB Garamond 400, 400 italic, 500 | 19 px / 17 px, line-height 1.5 |
| Canto title, rail title, book numerals | IM Fell English SC | canto 2.3 rem / 2.0 rem |
| Book title | UnifrakturMaguntia | 1.7 rem / 1.4 rem |
| Labels (running head, "The Argument") | EB Garamond 500, caps, tracked .16–.2 em | .72–.8 rem |
| Stanza numerals | EB Garamond, old-style figures | .82 rem |
| Variant notes | EB Garamond | .78 rem |

All three families come from Google Fonts. EB Garamond replaces IM Fell for running text. Fell's rough edges are faithful to the punches, but at 17 px on a phone they blur. Fell survives in the small caps, where it is large enough to read as type.

The scale is .72, .8, .86, 1, 1.35, 1.7, 2.3 rem. That is roughly a 1.25 ratio, rounded to whole pixels at 19 px.

Measure: the verse column is 33 rem (627 px). The longest alexandrines are about 55 characters, so no verse line wraps at 1440 px. Prose pages (Letter to Raleigh, notes) should use 29 rem, about 70 characters.

Wrapping: each line is a block with a hanging indent. A wrapped part is indented 2.5 em on a phone and 1.6 em on desktop. Spenser's own indent for lines 2–8 is 1 em on a phone and 1.25 em on desktop. A continuation therefore always sits deeper than any real line start. At 390 px one line in five stanzas wraps ("…from far / compel'd."), and it reads as a continuation.

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

Contrast against the paper: ink is 15.6:1 in light and 14.1:1 in dark. Rubric is 6.9:1 and 7.1:1. The weakest pair, `--ink-3` on `--paper-2`, is 4.8:1. The dark tokens apply under `prefers-color-scheme: dark` guarded by `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. The theme button writes `data-theme` and stores it.

The paper is a flat colour. There is no texture and no vellum gradient.

## Page types

**Landing.** The 1590 title page image sits centred at a 22 rem maximum width on the paper colour. Above it is the title in Fell SC, and below it one line in Garamond giving editor and edition. The Lewis epigraph stays. "Begin reading" leads to the Book I proem. "Continue" appears when a last-read stanza is stored.

**Dedication.** The dedication is a typographic pyramid (Spenser's lapidary layout) in Fell SC at 0.95 rem, tracked 0.14 em, with each line centred. The 1590 dedication page image sits beside it on desktop and below it on a phone, at 18 rem. The text is real text, not only an image.

**Canto.** From the top: the book title (only at the first canto of a book), the running head, the canto title, the fleuron, the argument, then the stanzas. At the foot are previous and next controls that carry each canto's argument incipit, so the reader knows where they lead.

**Stanza.** Each stanza is an addressable block (`#s12`), and its numeral is the link to it. A stanza reached by link gets a faint rubric wash. In Original spelling, Smith's collation notes for that stanza appear in the left margin on desktop. On a phone they appear under the stanza after a dotted rule. They never sit between lines.

**Plate.** A plate goes between two stanzas, never inside one. It is capped at `min(72vh, 34rem)` tall on desktop and 62vh on a phone, so the next stanza is never more than a short scroll away. Tapping it opens the full image. The caption gives title, artist, date, collection, and the stanzas it faces. A "Plates" index in the back matter lists all 38 with links to their stanzas.

## Contents rail

On desktop (1024 px and up) the rail is a sticky 17.5 rem column. It holds front matter, the seven books as disclosures, and back matter. The current book is open, with one row per canto showing the canto number and the first line of its argument. Other books show a grid of canto numerals. Every row and cell is at least 44 px.

Below 1024 px the same `<nav>` becomes a popover: a side sheet on tablets and a bottom sheet (85vh) on phones. It opens from a button in the reading bar and closes with ×, Escape, a tap outside, or choosing a destination. This needs no script. The HTML `popover` attribute does the work. One line of script closes the sheet after a link is followed.

## Spelling switch

The reading bar holds a two-part control: **Modern | Original** ("Orig." on a phone). Both readings sit in the markup line by line, and CSS shows one. Before switching, the script records which stanza is at the top of the screen and its offset. After switching, it scrolls that stanza back to the same offset. Both readings have nine lines per stanza, so the page barely moves. The choice is stored per reader. Without script the control is hidden and the modern text shows.

## Excluded

- Fake parchment, paper grain, deckle edges, drop shadows on text.
- Black-letter for body text or headings below book level.
- The SVG woodcut initials. They are fine at 4.6 rem on desktop, but they push lines 1–3 out of alignment and cost width on a phone. A raised rubric capital takes their place.
- The long s (ſ) and other ligature cosplay. Smith does not print them.
- Floating action buttons over the text.

## Open questions

1. **Source of the Original layer.** The repo holds only the modern text. The mockup's Original lines come from Smith via Project Gutenberg #70717, the edition's stated source. Building it for all 3,856 stanzas means aligning those files line for line with the published text. Should that live under `faerie-queene/`?
2. **Errors in the modern text.** In I.i the published text has *fare away* (Smith *farre*), *lassie* (*lasie*), *vel* (*vele*), *inward fare* (*farre*), *prays* (*prayse*), *hi* (*hy*) and *arr* (*arre*). The mockup shows stanzas i–v unchanged, so it includes *vel*. Should the modernization rules be rerun, or should these be fixed by hand?
3. **Residue.** The argument of I.ix ends "tells:[295", which is a footnote marker left in the text. The Note on the Text states the stanza count as "3,8563,850 stanzas, some 34,700 linesnbsp;…", a broken substitution.
4. **One file or many.** At 2.8 MB a phone must parse the whole poem to read one canto. One page per book, about 400 KB each, would keep the contents rail and the anchors.
5. **Variant notes in Modern mode.** The mockup hides Smith's collation in Modern mode. Some readers may want it there too.
6. **The original screenshots.** Most captures below the landing page are blank. The page renders correctly when scrolled, so this looks like a capture limit on a very tall page, not a page bug. It is worth confirming.
