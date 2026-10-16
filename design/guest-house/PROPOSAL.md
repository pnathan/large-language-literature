# The Guest-House: design proposal

Mockup: `mockup/index.html`, with real text from `docs/guest-house/index.html`:
the framing, Part I with its notes, the §156 notice, Part II lines 3676–3681 and
3693–3695, three terms.

## The problem

The page has 35 couplets, 12 notes, 7 terms. The notes sit in a section after
the verse: a reader who meets *rāh zadan* at 3678 scrolls past 29 couplets to
learn what it means. This proposal changes no content. It moves each note next
to its couplet.

## Period cues, and why

- **The bayt as the unit.** A masnavi is a chain of rhymed couplets. Each couplet
  is one block: line number, two Persian hemistichs (*miṣrāʿ*), two English lines.
  English line 1 sits in the same grid row as hemistich 1, and line 2 with
  hemistich 2, so the reader sees which half translates which.
- **The ruled column (*jadval*).** Persian codices rule the text block and the
  space between columns in gold and colour. The design uses two such rules: a
  thin double gold rule between English and Persian, and a single gold rule
  between the text and the margin. They run only beside verse and stop at the
  §156 notice.
- **The margin commentary (*ḥāshiya*).** Glosses in manuscripts sit in the
  margin beside the line they explain. Here the notes do the same.
- **Rubrics in red.** Masnavi manuscripts commonly write section headings in red
  ink. Section labels, rubric quotations and note labels are set in rose.
- **Two hands.** The Persian is set in Nastaʿlīq, the hand of Persian poetry.
  The two Arabic couplets (3694–3695) and inline Persian in prose are set in
  Naskh, as Persian manuscripts often set Arabic apart. The reader sees the
  language change before reading a word.

## Reading direction

On desktop, the Persian is on the right and the English is on the left. Each
text starts at its outer edge: the Persian reads inward from the right margin,
the English inward from the left. Their ragged ends meet at the central double
rule, as the two hemistichs of a manuscript bayt meet at the central gap. The
notes go in the right margin, next to the Persian, because they are "Notes on the
Persian". On a phone the original comes first, then the English.

## Type

| Role | Family | Size | Line height |
|---|---|---|---|
| Persian verse | Noto Nastaliq Urdu 400 | 25px desktop, 23px phone | 2.15 |
| Arabic verse | Noto Naskh Arabic 400 | 22px | 2.0 |
| Inline Persian/Arabic | Noto Naskh Arabic | 1.06em, `nowrap` | 1 |
| English verse | EB Garamond 400 | 17.6px (1.1rem) | 1.55 |
| Prose | EB Garamond 400 | 18px | 1.6 |
| Notes | EB Garamond 400 | 14.4px margin, 15.2px folded | 1.55 |
| h2 / h1 | EB Garamond 400 | clamp 24–30px / 26–34px | 1.2 |
| Title مهمان‌خانه | Noto Nastaliq Urdu | clamp 38–56px | 2.0 |
| Labels, line numbers, buttons | Inter 500 | 11.5–12px, caps, +0.13em | — |

Nastaʿlīq falls back to Noto Naskh Arabic, then Geeza Pro and Tahoma. Each
Persian verse block has `lang` and `dir="rtl"`. Inline phrases are `<bdi>` and do
not wrap: an RTL phrase broken across two English lines reads in the wrong order.

## Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#f4ecdc` | `#15120e` | body background |
| `--paper-2` | `#faf5ea` | `#1e1a14` | sheet, notice, buttons |
| `--ink` | `#2a2119` | `#ece3d0` | text |
| `--ink-2` | `#5c4e40` | `#b8a98f` | notes, secondary |
| `--ink-3` | `#76664f` | `#988a73` | line numbers, labels |
| `--indigo` | `#2d3e78` | `#a3b5ea` | links, line ranges, §156 notice |
| `--rose` | `#9c3f55` | `#e3909f` | rubrics, note labels, note marker |
| `--gold` | `#9a7628` | `#d4ae55` | lede bar, active control |
| `--rule-gold` | gold at 48% | gold at 40% | jadval rules |

The dark values apply under `@media (prefers-color-scheme: dark)` with
`:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`.
A Light/Dark toggle sets `data-theme` and remembers it in `localStorage`.
Without the script, the page follows the system setting.

## Layout by page type

**Contents.** At 1280px and wider: a sticky left rail. Each entry gives its
section and Nicholson line range, so the rail maps the three moves. §156 is in
italic because it is summarized, not translated. Below 1280px: a `<details>`
sheet in the sticky top bar, rows 48px tall, closed by a choice or Escape.

**Framing.** The three-column table becomes a list, one row per move. On a phone
the rubric drops below the § and line range.

**Passage, 900px and wider.** Each bayt is a four-column grid: number (3.25rem),
English, Persian, margin (17rem). English and Persian are subgrids, so their rows
align. The note spans the bayt in the margin. A rose dot after the number marks
a couplet with a note.

**Passage, under 900px.** One column: number, Persian, English, note. Each note
is a closed `<details>` with a 44px summary ("Note · 3645"). It opens directly
under its couplet, so the reader keeps their place.

**Notes.** No longer a separate list; each note sits at its line (3694–3695 at
3694).

**Terms.** A definition list: term in Naskh, transliteration, definition, and
44px line links back to the couplets.

**Notices.** §156 is a boxed notice with an indigo rule. It breaks the jadval on
purpose, so the omission cannot be mistaken for continuous verse.

## The phone overflow: cause and fix

In the current page `.contents a` has `white-space: nowrap`, and the markup
places each link directly against its `·` separator with no whitespace between
them (`</a><span class="sep">·</span><a …>`). The middle dot gives the browser no
line-break opportunity. The seven links and six dots therefore form a single
unbreakable run 661px wide; 661 − 390 = 271px, the measured overflow
(Playwright: the last nav link ends at x = 661).

Fix: the contents become a vertical list in a sheet. Grid tracks use
`minmax(0,1fr)`, text has `overflow-wrap: break-word`, and the moves table is a
list. On the mockup `scrollWidth − clientWidth` is 0 at 390, 1024 and 1440px, in
both themes.

## What I excluded

- Arabesque fills, gilt frames, an illuminated *sarlawḥ*. The gold rules and the
  existing ۞ mark are the only ornament.
- Equal-width justified hemistichs. Scribes reach equal measure by stretching
  joins (*kashīda*) and stacking words; browsers widen word spaces, which left
  holes in the Nastaʿlīq. The hemistichs are right-aligned instead.
- Hemistichs side by side. At 25px one hemistich nearly fills the Persian
  column; two leave no room for the English.
- External scripts. One small inline script handles the theme, note folding and
  the sheet.

## Open questions

1. **Which Nastaʿlīq.** Google Fonts offers only Urdu-style Nastaʿlīq (Noto
   Nastaliq Urdu, Gulzar), not the Iranian style of a Persian codex. Accept it,
   or set the verse in Naskh and keep Nastaʿlīq for the title? It also adds a
   few hundred kilobytes.
2. **Gaps from long notes.** A note longer than its couplet (3645) grows the row
   and leaves white space under the verse. Accept it, or let notes run on beside
   later couplets and lose the one-to-one link?
3. Should margin notes be headed by the Persian lemma (راه زدن) instead of the
   repeated line number?
4. Keep a short "Notes" index of noted lines, or does the rose marker suffice?
