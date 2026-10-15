# Mahābhārata edition: design proposal

Mockup: `design/mahabharata/mockup/index.html`. It shows the contents, Part II, section IV (The Hall), and three passages from 2.61, with real text from `docs/mahabharata/index.html`.

## What the current page does, and where it fails

The current page sets each passage as a Devanagari block followed by an English paragraph, with commentary in a right-hand column. It reads well. Five things get in the way:

1. The script switch sits in the header. To change script, the reader scrolls to the top and loses their place.
2. The verse reference scrolls away. Devanagari lines end in `॥ ४० ॥`, but IAST lines carry no number at all.
3. The English for a passage of six verses is one paragraph. The reader cannot find the English for verse 41 without counting.
4. Commentary, textual notes and narrative bridges share one column and one type style.
5. On a phone the contents are 14 uppercase links wrapped over four lines.

## Period cues

**The BORI printed page.** The Critical Edition prints the constituted text as a column of śloka in Devanagari, two pādas to a line, with verse numbers. Below a short rule it prints the apparatus in smaller type, keyed by verse and pāda. I keep three things from it: the hierarchy of text over apparatus, the short rule between them, and keying by pāda letter (`41d`). I do not imitate its types or its density.

**The manuscripts it collated.** Paper and palm-leaf manuscripts give the colours. The ground is a dry, slightly yellowed paper. Vermilion is the rubric colour; scribes used it for numbers and for section marks. I use it for references and verse numbers only. Indigo marks emphasis, and here it marks the lemma in an apparatus entry.

## Exclusions

- No ornament. That means no mandalas, lotuses, borders or conch-and-wheel motifs. The current page's ring ornament and dice-dot divider are removed.
- No saffron or gold.
- No imitation of palm-leaf shape, string holes, or texture images. The paper colour is a flat colour.
- No faux-Devanagari Latin type, and no headline set in a "Sanskrit-style" display face.

## Type

| Role | Family | Desktop | Phone |
|---|---|---|---|
| Sanskrit, Devanagari | Noto Serif Devanagari 400 | 21/36.75 px | 19/33 px |
| Sanskrit, IAST | Source Serif 4 400 | 18/28.8 px | 17/27 px |
| English | Source Serif 4 400 | 18/27.9 px | 17/26 px |
| Apparatus | Source Serif 4 400 | 14.5/21.75 px | 14.5/21.75 px |
| Labels, controls | system UI sans 500 | 12–14 px | 12–14 px |
| Section, part, title | Source Serif 4 600 | 24, 30, 40 px | 21, 25, 34 px |

The scale is 13, 14.5, 18, 21, 24, 30, 40. Devanagari is set 3 px larger than the Latin text because its headline (śirorekhā) and the vowel signs above and below it need the room. Its line height is 1.75 for the same reason. Source Serif 4 has precomposed glyphs for every IAST letter used in the text (ṛ ṝ ṃ ḥ ṅ ñ ṭ ḍ ṇ ś ṣ). It is a transitional face, close to the English types of the early twentieth century. Numerals are tabular and lining, so references align. Noto Serif Devanagari renders conjuncts and vowel signs correctly; I checked `क्ष`, `द्ध्वं`, `ष्टुं` and `द्भु` in Chromium. The fallback stack is Kohinoor Devanagari, Devanagari Sangam MN, then Nirmala UI.

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

All are custom properties on `:root`. The dark set applies under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. `body` sets `background: var(--paper)`. Text tokens meet WCAG AA on `--paper` in both themes. `--ink-3` is used only for labels and counts.

## Layout by page type

**Contents.** The contents form a table under the title. Each row gives the section number in vermilion, the title, the reference range, and the number of passages. Part I and Part II sit in two columns on desktop and one column on a phone. Every row is at least 44 px high. The same list is the contents sheet on a phone.

**Part.** A 2 px ink rule, a small-caps "Part II" in vermilion, then the title and the parvan name in italic. A section heading has its number, its title, and the reference range set flush right.

**Passage.** The head gives the reference (`Sabhā 2.61.40–42`), a provenance line ("Constituted text. Checked against the GRETIL/BORI typed text. Variant readings not collated.") and the speaker if the commentary names one. Then comes one row per śloka. On desktop each row is a grid: verse number in a 2.75 rem margin, Sanskrit, English. Each verse's English sits beside its own Sanskrit. Omitted verses get a row of their own: "… 29–31ab not printed". A half-verse is numbered with its pāda letters (`31cd`). Narrative bridges from the commentary sit between passages in a ruled, indented paragraph in `--ink-2`.

**Apparatus.** On desktop the apparatus sits at the foot of each passage, below a 7 rem rule, in 14.5 px type. Each entry has the form `41d प्रादुरासीद् ] NOTE text`. That is the verse and pāda, the lemma in the current script, a bracket, the entry type, and the entry. On a phone each verse that has entries gets a disclosure, "Apparatus 1", directly under its English. The foot block is hidden on a phone.

## Controls

A sticky bar carries every control, so nothing requires a return to the top.

- **Reference.** The bar shows the reference of the first verse below it, and updates on scroll. It is also the button that opens the contents.
- **Script.** A segmented control: देवनागरी | IAST. Switching keeps the reader's place. The script finds the first verse below the bar, records its offset, switches, and scrolls by the difference. In Playwright, verse 2.61.40 stayed the anchor through the switch at both widths. The choice is stored in `localStorage`, and every storage call is wrapped in try/catch.
- **Layers.** Three toggles: Sanskrit, English, Apparatus. With Sanskrit off, the English takes a 38 rem measure. With English off, the Sanskrit takes a 40 rem measure. One of Sanskrit and English must stay on; the remaining one is disabled.
- **Theme.** A light/dark button sets `data-theme`. With no choice stored, the page follows the system setting.

On a phone (390 px) the bar holds three things: the reference button, the script control, and a View button. View opens a bottom sheet with the script control, the three layer toggles and the theme. Every control is at least 44 × 44 px; Playwright found none smaller. Long IAST pādas wrap at word boundaries with a hanging indent. `overflow-wrap: break-word` stops any word from forcing overflow. `scrollWidth − clientWidth` is 0 at 390 px with IAST on and an apparatus open.

The only script is one inline block of about 80 lines. No external scripts are loaded. Stylesheets come from Google Fonts only.

## What the data does not support

The BORI critical notes were not consulted for this edition (`mahabharata/CLAUDE.md`). There are therefore no variant readings and no manuscript sigla to show. The mockup's apparatus holds only the edition's own textual notes, set in apparatus form. Every passage says "Variant readings not collated". I invented no sigla or readings. When the notes are checked, the entry form takes them as `41d lemma ] variant  sigla`, with sigla in the UI sans so they stay distinct from the Sanskrit.

## Open questions

1. **Per-verse English.** Aligning English to verses means splitting each translation paragraph at verse boundaries. That is editorial work on the translation. Where English syntax crosses a verse (2.61.31cd–32 in the mockup), the split falls at a clause. Should the translator make these splits? The alternative is to fall back to one paragraph per passage where a split would mislead.
2. **Commentary.** I moved commentary notes into the apparatus as NOTE entries, and narrative glosses into bridges. Does the project accept that split, or should commentary keep its own column?
3. **Devanagari verse numbers.** The constituted text ends each verse with `॥ ४० ॥`, and the margin repeats the number in Arabic numerals. Keep both, or drop the margin number when Devanagari is shown?
4. **Starred passages.** Should the apparatus list the starred and appendix passages (the references with `*` in the GRETIL text) by number once their locations are verified?
5. **Contents depth.** Should the contents list the 113 passages, or stop at sections as the mockup does?
