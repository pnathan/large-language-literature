# Bereshit: design proposal

The mockup is `mockup/index.html`. It sets Genesis 3 (24 verses) from the edition's own text files:
the Hebrew, the English, the notes, Rashi, Ibn Ezra, the Greek and the apparatus entries. Nothing in it is invented.

## What the present page gets wrong

The published page sets English, Greek and commentary in three columns. The Hebrew sits inside the commentary
box at the size of a note, so the base text is the smallest text on the screen. A long note leaves a screen-high blank
under the English. On a phone the Hebrew comes after the Greek.

## Period cues, and why

1. **The Mikraʾot Gedolot page.** The text stands in the centre, set large. The commentaries stand beside it in
   smaller type and a different face. The mockup does the same: English | Hebrew | commentary, the Hebrew in
   the middle, the commentary narrower and in a sans. Rashi's and Ibn Ezra's names are set in Rashi script (Noto
   Rashi Hebrew) beside the Latin label, as the printed page heads their columns. Only the labels use it.
2. **The codex as an object.** The Leningrad codex has no verse numbers and no chapter breaks. Its divisions are
   the open and closed parashot. The mockup prints each mark where the Masoretic witness has it (after 3:15, 3:16,
   3:21, 3:24). A closed paragraph (ס) gets a thin rule and a small gap. An open paragraph (פ) gets a larger gap and
   a heavier rule, as the scribe leaves the rest of the line blank.
3. **Ink and vellum.** The palette is two inks on one ground: an iron-gall black-brown for the text and a red for
   rubrication. The red marks only the apparatus of reading: verse numbers, the Hebrew letter-numerals, the
   paragraph marks and the disclosure markers. The ground is a flat warm off-white. There is no texture.
4. **The polyglot.** The Greek is a second witness, not a translation. It is set in its own face (Gentium Plus) and
   in a cooler ink, so the eye can tell witness from text without a label.

## Type system

| Role | Family | Desktop | Phone |
|---|---|---|---|
| Hebrew (MT) | SBL Hebrew, Ezra SIL, then Noto Serif Hebrew (Google Fonts) | 27/51 px | 25/50 px |
| English translation | Source Serif 4, optical sizes | 19/29.5 px | 18/28 px |
| Greek, apparatus | Gentium Plus | 18 px, 16 px | same |
| Commentary, UI | Source Sans 3 | 15/24 px | 15/24 px |
| Labels | Source Sans 3, 600, caps, +0.08em | 12–13 px | same |
| Rashi label | Noto Rashi Hebrew | 14 px | same |

The ratios run about 1.25 from labels to commentary to English, and 1.4 from English to Hebrew. The Hebrew needs
the larger step: niqqud and teʿamim sit above and below the letters, and at English size they collide.
Line height for the Hebrew is 1.9 for the same reason. Noto Serif Hebrew places every vowel and accent of chapter 3, including the
paseq and the doubled pashta of 3:1. A reader with SBL Hebrew or Ezra SIL installed gets that face first.

Hebrew inside English prose is isolated in `<bdi lang="he">`, as the build tool already does, and set 1.12 em.
A paseq (׀) is bound to the word before it with a no-break space, so it never starts a line.

## Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#f8f5ee` | `#15130f` | body background |
| `--paper-2` | `#f1ece1` | `#1e1b16` | pressed button, sheet |
| `--ink` | `#1e1a16` | `#ebe5d9` | English, headings |
| `--ink-he` | `#14110e` | `#f5f0e6` | Hebrew |
| `--ink-2` | `#463f37` | `#cbc3b5` | commentary |
| `--ink-3` | `#6c6358` | `#9e9587` | labels, sigla |
| `--greek` | `#2e3b46` | `#b9c8d4` | Greek witness |
| `--rubric` | `#9a3324` | `#e2917b` | numbers, paragraph marks |
| `--rule` / `--rule-2` | `#ddd4c4` / `#c9bea9` | `#352f27` / `#4a4237` | hairlines |
| `--focus` | `#1f5a8f` | `#8dbbe6` | focus ring |

`--ink-3` on `--paper` is 5.4:1 and `--rubric` 6.7:1 (dark: 6.3:1, 7.6:1); all pass AA for text. Dark values apply under
`prefers-color-scheme: dark` guarded by `:root:not([data-theme="light"])`, and under `:root[data-theme="dark"]`.
The toggle writes `data-theme` and remembers it in `localStorage` inside try/catch.

## Layout by page type

**Verse by verse (the mockup).** At 1120 px and wider each verse is one grid row:
number (3.5 rem) | English (1 fr) | Hebrew (1.15 fr) | commentary (23 rem). The Hebrew column is right-aligned and
`dir="rtl"`, its letter-numeral (א, ב … כד) at the start of the line. The English keeps the translation's line breaks,
with a hanging indent for wrapped lines. The English and Hebrew block is sticky: when a note runs long, the verse
stays in view while the reader goes down the commentary. Under the pair sits a disclosure, *LXX and apparatus*,
which opens in place to the Greek of the verse and the apparatus entries for it, labelled Variant, Spelling (SP) or
Crux after the apparatus sections I–III. Its summary counts the readings, so a reader sees "Greek · 5 readings"
before opening it.

The commentary column holds the editor's note, the readings held open, Rashi, Ibn Ezra, and a closed *Word by word*
disclosure (English fragment, Hebrew tokens, literal sense). It is open by default at this width.

Between 720 and 1119 px the commentary drops below the verse as a closed disclosure. English and Hebrew stay
side by side.

**Phone (below 720 px).** One column with 16 px gutters: number, Hebrew, English, then *Commentary* and *LXX and
apparatus* as disclosures. Every summary is 44 px high. The chapter navigation is a sheet under the bar: four
chapter buttons, a 6 × 4 grid of verse buttons (44 px each), and the section links. The bar button shows the verse
in view ("3:15"), so it doubles as a position indicator.

**Reading text** (not in the mockup). The continuous English in Masoretic paragraphs, a 66-character measure,
Source Serif 4 at 19 px, verse numbers as small red superscripts, paragraph marks as in the mockup. An optional
Hebrew-only view sets the MT in the same paragraphs: the nearest the page comes to a codex column.

**Names.** A three-column table: Hebrew (right-aligned, 22 px), English form, meaning. On a phone each row becomes a
two-line block: Hebrew and English form on one line, meaning below.

**Critical apparatus.** The sigla as a definition list with the siglum in a small bordered box, the same box used for
sigla in the verse disclosures. Entries keep the classical form `lemma ] reading SIGLA ; reading SIGLA`, the bracket
in red, set in Gentium Plus. Each verse reference links back to its verse, and each verse disclosure links forward to
the full section.

## Excluded

- Parchment textures, torn edges, drop shadows on "pages", ornamental borders, illuminated initials.
- Blackletter, Trajan, Cinzel, Cormorant and other faces that announce "ancient".
- Rashi script for running text. It is a period cue, not a reading face for this audience.
- Hover-only interaction. Every control works by tap and keyboard. With scripts off the page still reads; the
  commentary column then starts closed.
- Arabic numerals in the Hebrew line. The Hebrew carries letter-numerals, as printed editions do.

## Open questions

1. Should the Greek be a fourth column on desktop? It serves readers who compare witnesses and costs 18 rem.
   The mockup keeps it one tap away.
2. Long notes (1:1, 2:7) make tall rows. A "read more" cap would even them but hide text written to be read. The
   sticky verse is the present answer.
3. Should the word-by-word table link tokens both ways (tap an English fragment, mark its Hebrew words)? It needs a
   small script and indices in the markup; the data already exists.
4. SBL Hebrew cannot be served from Google Fonts. Self-hosting it under `docs/bereshit/` needs a licence check.
5. Should cantillation be switchable (vowels only)? Some readers find the teʿamim noise. The MT has them, so the
   default keeps them.
