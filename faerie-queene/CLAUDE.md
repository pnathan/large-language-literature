# The Faerie Queene — project briefing

## What this is
A complete illustrated web edition of Edmund Spenser's *The Faerie Queene* in
modernized spelling, delivered as a single self-contained HTML page with
relative-pathed assets (images, fonts). Published on GitHub Pages.

## Published edition

Published to GitHub Pages under `docs/faerie-queene/`:
- `index.html` — the full edition (2.8 MB HTML): all six books (72 cantos),
  the Mutabilitie Cantos (cantos 6–8), the Letter to Raleigh, an Editor's Note
  with a table of false friends, and a Note on the Text.
- `assets/img/` — 38 public-domain plates (Crane, Fuseli, Etty, West, Turner,
  Watts, Riviere, Allston, Uwins, Strudwick, Khnopff, and others).
- `assets/fonts/` — IM Fell English/SC/Double Pica SC (Igino Marini, SIL OFL)
  and EB Garamond regular/italic/500 (Georg Duffner, SIL OFL).

## Design

Night-and-gilt palette (`--night:#181410`, `--gilt:#b8913d`), vellum-textured
canto sheets, IM Fell English body text, IM Fell Double Pica SC display, EB
Garamond for navigation and apparatus. Fixed sidebar rail with per-book/per-canto
navigation, collapsible on mobile (<900px).

## Text source

J. C. Smith's Clarendon edition (Oxford, 1909), via Project Gutenberg eBooks
#70717 and #72698. Spelling modernized as described in the edition's Note on
the Text. The poem is in the public domain.

## Scale

- 3,856 stanzas (9-line Spenserian stanzas, alexandrine final line)
- 7,709 lines of verse
- 75 cantos across 6 books + Mutabilitie
- 38 plates
- 82 illuminated initials (SVG, inline)

## Build pipeline

No build step. The edition was composed as a single HTML file. The standalone
variant (`the-faerie-queene-standalone.html`, 19 MB, all assets embedded as
data URIs) is not committed to the repo to keep clone size reasonable.

## Editorial constraints

1. The text follows Smith's Clarendon edition faithfully. Do not introduce
   readings from other editions without explicit instruction.
2. Spelling modernization follows the rules in the edition's Note on the Text —
   a table of "false friends" (words whose modern form misleads) is part of
   the front matter. Do not alter the modernization scheme.
3. Plates are public-domain works with full attribution in the colophon.
   Do not substitute synthetic imagery.
4. The edition includes Spenser's original arguments (prose summaries) at the
   head of each canto. These are part of the text, not editorial additions.

## Known state / open tasks

- Possible refinements: split into per-book pages for lighter loads; add a
  search/find-in-text feature; print stylesheet for a PDF edition; add the
  Amoretti and Epithalamion as companion pieces.
