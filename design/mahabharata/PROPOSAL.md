# Mahābhārata edition: design proposal

Mockup: `design/mahabharata/mockup/index.html`. It shows the contents, Part II, section IV (The Hall), and three passages from 2.61, with real text from `docs/mahabharata/index.html`.

## What the current page does, and where it fails

The current page sets each passage as a Devanagari block, then an English paragraph, with commentary in a right-hand column. Five things get in the way:

1. The script switch is in the header. Changing script means scrolling to the top.
2. The verse reference scrolls away, and IAST lines carry no verse number.
3. A passage's English is one paragraph. Finding the English for verse 41 means counting.
4. Commentary, textual notes and narrative bridges share one column and one style.
5. On a phone the contents wrap over four lines of uppercase links.

## Period cues

**The BORI printed page.** The Critical Edition prints the constituted text as a column of śloka in Devanagari, two pādas to a line, numbered. Below a short rule it prints the apparatus in smaller type, keyed by verse and pāda. I keep the order of text over apparatus, the short rule, and keying by pāda letter (`41d`). I do not copy its types or its density.

**The manuscripts it collated.** These give the colours: a dry, slightly yellowed paper; vermilion, the scribes' colour for numbers and section marks, used here for references and verse numbers only; indigo for emphasis, used here for the lemma of an apparatus entry.

## Exclusions

- No ornament: no mandalas, lotuses or borders. The current ring ornament and dice-dot divider go.
- No saffron or gold.
- No palm-leaf shapes or paper textures. The paper is a flat colour.
- No "Sanskrit-style" Latin display face.

## Type

| Role | Family | Desktop | Phone |
|---|---|---|---|
| Sanskrit, Devanagari | Noto Serif Devanagari 400 | 21/36.75 px | 19/33 px |
| Sanskrit, IAST | Source Serif 4 400 | 18/28.8 px | 17/27 px |
| English | Source Serif 4 400 | 18/27.9 px | 17/26 px |
| Apparatus | Source Serif 4 400 | 14.5/21.75 px | 14.5/21.75 px |
| Labels, controls | system UI sans 500 | 12–14 px | 12–14 px |
| Section, part, title | Source Serif 4 600 | 24, 30, 40 px | 21, 25, 34 px |

The scale is 13, 14.5, 18, 21, 24, 30, 40. Devanagari is 3 px larger than the Latin, with line height 1.75, because the headline and the vowel signs above and below it need room. Source Serif 4 is a transitional face close to the English types of the period, and has every IAST letter the text uses. Numerals are tabular and lining. In Chromium, Noto Serif Devanagari renders the conjuncts in the mockup correctly (`क्ष`, `द्ध्वं`, `ष्टुं`, `द्भु`). Fallbacks: Kohinoor Devanagari, Devanagari Sangam MN, Nirmala UI.

## Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#F3ECDA` | `#17140F` | page background |
| `--leaf` | `#FAF6EA` | `#201C16` | bar, sheets |
| `--ink` | `#231D16` | `#ECE3CF` | text |
| `--ink-2` | `#5B5142` | `#BCB099` | apparatus, bridges |
| `--ink-3` | `#74684F` | `#9A8E77` | labels, counts |
| `--rule` | `#D3C6A8` | `#3A332A` | hairlines |
| `--rule-2` | `#A8977A` | `#5E5444` | apparatus rule, control borders |
| `--rubric` | `#A8341A` | `#EE7A5C` | references, verse numbers |
| `--indigo` | `#2C3B6E` | `#A9B6EC` | lemmata, focus ring |

Dark values apply under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`, and under `:root[data-theme="dark"]`. `body` sets `background: var(--paper)`. Every text token is at least 4.6:1 against `--paper` in both themes.

## Layout by page type

**Contents.** A table under the title. Each row: section number in vermilion, title, reference range, passage count. Two columns (Part I, Part II) on desktop, one on a phone. Rows are at least 44 px high. The same list fills the phone's contents sheet. At 1100 px and wider a short copy stays in a sticky left rail.

**Part.** A 2 px ink rule, "Part II" in vermilion small caps, the title, the parvan in italic. A section heading carries its number, title, and range flush right.

**Passage.** The head gives the reference (`Sabhā 2.61.40–42`), a provenance line, and the speaker when the commentary names one. Then one row per śloka: verse number in a 2.75 rem margin, Sanskrit, and that verse's English beside it. Omitted verses get their own row ("… 29–31ab not printed"). A half-verse is numbered with its pāda letters (`31cd`). On a phone the English goes under the Sanskrit, after a short rule. Narrative bridges sit between passages, indented, in `--ink-2`.

**Apparatus.** On desktop, at the foot of each passage below a 7 rem rule, in 14.5 px type. Entry form: `41d प्रादुरासीद् ] NOTE text`, which is verse and pāda, lemma in the current script, bracket, entry type, text. On a phone each verse with entries gets a disclosure, "Apparatus 1", under its English, and the foot block is hidden.

## Controls

A sticky bar carries every control.

- **Reference.** Shows the first verse below the bar, updated on scroll. Tapping it opens the contents.
- **Script.** Segmented control, देवनागरी | IAST. Before switching, the page records the first visible verse and its offset; after, it scrolls by the difference. The choice is kept in `localStorage`, wrapped in try/catch.
- **Layers.** Toggles for Sanskrit, English, Apparatus. A lone column takes a 38–40 rem measure. One of Sanskrit and English must stay on.
- **Theme.** Sets `data-theme`; with no stored choice the page follows the system.

On a phone the bar holds the reference button, the script control, and a View button that opens a bottom sheet with the layer toggles and theme. All controls are at least 44 × 44 px. IAST pādas wrap at word boundaries with a hanging indent; `overflow-wrap: break-word` catches any longer word.

One inline script of 80 lines. No external scripts. Stylesheets from Google Fonts only.

## What the data does not support

The BORI critical notes were not consulted (`mahabharata/CLAUDE.md`), so there are no variant readings or sigla to show. The mockup's apparatus holds only the edition's own notes, and each passage says "Variant readings not collated". I invented none. When the notes are checked, entries take the form `41d lemma ] variant  sigla`, sigla in the UI sans.

## Open questions

1. **Per-verse English.** Splitting each translation at verse boundaries is editorial work. Where syntax crosses a verse (2.61.31cd–32) the split falls at a clause. Who makes the splits, and where a split misleads, do we keep one paragraph?
2. **Commentary.** Notes became NOTE entries in the apparatus; narrative glosses became bridges. Accept, or keep a commentary column?
3. **Verse numbers.** Devanagari lines end `॥ ४० ॥` and the margin repeats 40. Drop the margin number in Devanagari mode?
4. **Starred passages.** List them in the apparatus once their locations are verified?
5. **Contents depth.** Sections only, as now, or all 113 passages?
