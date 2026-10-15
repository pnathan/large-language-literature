# The Guest-House: design proposal

Mockup: `design/guest-house/mockup/index.html`. It holds real text from
`docs/guest-house/index.html`: the framing, Part I (3644–3646) with its three
notes, the §156 notice, Part II lines 3676–3681 and 3693–3695, three terms, and
stubs for the composite and sources.

## The problem

The page has 35 couplets, 12 notes, 7 terms. The current page puts the notes in a
separate section after the verse. A reader who meets *rāh zadan* at 3678 must
scroll past 29 couplets to learn what it means, then find the way back. This
proposal does not change the content. It moves each note next to its couplet.

## Period cues, and why

- **The bayt as the unit.** A masnavi is a chain of rhymed couplets. Each couplet
  is one block: line number, two Persian hemistichs (*miṣrāʿ*), two English lines.
  English line 1 sits in the same grid row as hemistich 1, and line 2 with
  hemistich 2, so the reader sees which half translates which half. The page
  already breaks the English at the hemistich (`<br>`). The design makes that
  break visible.
- **The ruled column (*jadval*).** Persian codices rule the text block and the
  space between columns in gold and colour. The design uses two such rules: a
  thin double gold rule between English and Persian, and a single gold rule
  between the text and the margin. They run only beside verse. They stop at the
  §156 notice and at the elision markers, so a reader can see where the verse
  breaks off.
- **The margin commentary (*ḥāshiya*).** Glosses in manuscripts sit in the
  margin beside the line they explain. Here the notes do the same.
- **Rubrics in red.** Section headings in Masnavi manuscripts are in red ink. The
  section labels, the rubric quotations ("Parable of the human body as a
  guest-house…"), and the note labels are set in rose.
- **Two hands.** The Persian is set in Nastaʿlīq, the hand of Persian poetry.
  The two Arabic couplets (3694–3695) and inline Persian in prose are set in
  Naskh. Persian manuscripts also write Arabic quotation in a different hand
  from the verse. The reader can see the language change before reading a word.

## Reading direction

On desktop, the Persian is on the right and the English is on the left. Each
text starts at its outer edge: the Persian reads inward from the right margin,
the English inward from the left. Their ragged line ends meet at the central
double rule, as the two hemistichs of a manuscript bayt meet at the central gap.
The notes go in the right margin, next to the Persian, because they are "Notes on
the Persian". On a phone the Persian comes first and the English follows, so the
original comes before the translation.

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

Fallbacks: Nastaʿlīq falls back to Noto Naskh Arabic, then Geeza Pro and Tahoma.
Naskh falls back to Amiri and the system fonts. Every Persian element has
`lang` and `dir="rtl"`. Inline phrases are in `<bdi>` and do not wrap, because a
right-to-left phrase broken across two lines of English reads in the wrong order.

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
A Light/Dark toggle sets `data-theme` and saves the choice in `localStorage`
(wrapped in try/catch). Without the script, the page follows the system setting.

## Layout by page type

**Contents.** At 1280px and wider, the contents are a sticky left rail. Each
entry gives its section and its Nicholson line range, so the rail also maps the
three moves (§155, §156, §157). The §156 entry is in italic because that section
is summarized, not translated. Below 1280px the contents become a
`<details>` sheet in the sticky top bar. Each row is at least 48px tall. Choosing
a link closes the sheet, and so does Escape.

**Framing.** The three-column table becomes an ordered list with one row per
move. On a phone the rubric drops below the § and line range. This list needs no
horizontal scroll container.

**Passage, 900px and wider.** Each bayt is a four-column grid: line number
(3.25rem), English, Persian, margin (17rem). English and Persian are subgrids, so
their rows align. A note spans the bayt's rows in the margin. A rose dot after
the line number marks a couplet that has a note.

**Passage, under 900px.** One column in this order: line number, Persian,
English, note. Each note is a `<details>` that starts closed, with a 44px
summary labelled "Note · 3645". Opening a note puts it directly below its
couplet, so the reader keeps their place.

**Notes section.** It is gone as a separate list. Each note sits at its line, and
the 3694–3695 note sits at 3694. The full page could keep a short index of
noted lines under "Notes" for readers who want to scan the notes.

**Terms.** A definition list. Each entry gives the term in Naskh, its
transliteration in italic, the definition, and line links (44px targets) back to
the couplets.

**Notices.** §156 is a boxed notice with an indigo rule. It interrupts the
jadval on purpose: the omitted lines must not look like a gap in the verse.

## The phone overflow: cause and fix

In the current page `.contents a` has `white-space: nowrap`, and the markup
places each link directly against its `·` separator with no whitespace between
them (`</a><span class="sep">·</span><a …>`). The middle dot gives the browser no
line-break opportunity. The seven links and six dots therefore form a single
unbreakable run 661px wide. 661 − 390 = 271px, the measured overflow (confirmed
with Playwright: the last three nav links end at 459, 584 and 661px).

Fix: the contents become a vertical list in a sheet, so no run of links needs to
wrap. As further guards, grid tracks use `minmax(0,1fr)`, body text has
`overflow-wrap: break-word`, and the moves table is now a list. Measured on the
mockup, `scrollWidth − clientWidth` is 0 at 390, 1024 and 1440px, in both themes.

## What I excluded

- Arabesque fills, gilt frames, an illuminated *sarlawḥ* headpiece. The gold
  rules are the only ornament, plus the existing ۞ mark in the footer.
- Equal-width justified hemistichs. Manuscripts give both hemistichs the same
  width by stretching letter joins (*kashīda*) and stacking words. Browsers
  justify by widening the spaces between words. In Nastaʿlīq that left holes, so
  the hemistichs are right-aligned instead.
- A side-by-side hemistich layout (miṣrāʿ 1 right, miṣrāʿ 2 left) for the
  Persian. At 25px each hemistich is about as wide as the whole Persian column
  now is, so two side by side leave no room for the English.
- External scripts. The only script is a small inline one for the theme, the
  note folding and closing the sheet.

## Open questions

1. **Which Nastaʿlīq.** Noto Nastaliq Urdu is the only Nastaʿlīq on Google Fonts.
   Its letterforms are the Lahore (Urdu) style, not the Iranian style of a
   Persian manuscript. Is Urdu-style Nastaʿlīq acceptable, or should the verse
   be set in Naskh with Nastaʿlīq kept for the title? The Nastaʿlīq font also
   adds a few hundred kilobytes.
2. **Gaps from long notes.** When a note is longer than its couplet (3645 is the
   worst case), the couplet's row grows and leaves white space under the
   English and Persian. Accept the gap, or let notes run on beside the next
   couplets? The second choice saves space, but the reader would lose the
   one-to-one link between note and line.
3. Should the full page keep a "Notes" index, or does the rose marker on the
   line number do that job?
4. The note labels in the margin repeat the line number. Should the margin use
   the Persian lemma (e.g. راه زدن) as its heading instead?
5. Should the line numbers also appear in Persian digits (۳۶۴۴) beside the
   Persian? Nicholson printed Western numerals, so the mockup keeps them.
