# Gilgameš editions: design proposal

Mockup: `design/gilgamesh/mockup/index.html` (reader view, real content from `docs/gilgamesh/reader.html`).

## What the current pages do, and where they fail

All four pages use one dark lapis-and-gold style with no light theme. At 1440 px the reader's notes sit in sticky margins far from their lines, and the inner margin is empty for most pericopes. Below 1150 px the notes drop under each pericope. No layer can be hidden. Many supplied captures are blank; my own captures of the page render, so I treat that as a capture artefact.

## Period cues

1. **Clay.** The light ground is unbaked clay (`#F4EFE6`), with no texture image.
2. **Lapis lazuli.** The prologue commands the reader to take out the lapis tablet (I 27). Lapis is the accent for keys, links and controls. In the dark theme lapis is the ground and the accent is the gold of its pyrite flecks.
3. **The ruled line.** Scribes ruled a line between sections. Each pericope opens with a hairline rule. A double rule marks where the recensions part and rejoin, and opens the colophon (*kīma labīrīšu šaṭir-ma bari*).
4. **The critical edition.** Sigla (SB, OB II, I 246) are set in small spaced sans. Square brackets stay in the text, and restored words take a lighter ink. eBL half-brackets ⸢ ⸣ would mark damaged signs. The repo's SB and OB data carry none in the reader's text (the only occurrences are bibliographic notes in `OB_Schoyen2.json`), so the reader cannot show them yet. The mockup omits them. Showing them requires eBL data that carries half-brackets, refetched from the eBL API; that is a separate change.

## Type

| Role | Family | Size (desktop / phone) |
|---|---|---|
| English verse, headings | EB Garamond | 19 / 18 px, line-height 1.42 |
| Akkadian transliteration, Akkadian headwords | Gentium Book Plus italic | 17 / 16 px |
| Apparatus, sigla, controls | Source Sans 3 | 14 px notes, 13 px sigla, 12 px line numbers |
| Tablet title | EB Garamond | 34 / 28 px |

The scale is 13, 14, 16, 17, 19, 23, 28, 34 px, near a 1.2 ratio. English sits a step above the Akkadian because Garamond has a small x-height. Gentium was built for linguistic transcription; š ṭ ṣ ḫ ā ī ū ʾ render in roman and italic. Fallbacks: Palatino or Georgia; Noto Serif or DejaVu Serif, which cover the diacritics; system sans. In the parallel layout the English column holds 50 to 58 characters; the headnote is capped at 38 em.

## Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#F4EFE6` | `#0F1530` | page |
| `--bg-raised` | `#FBF8F2` | `#182043` | contents panel, bottom sheet |
| `--bg-sunk` | `#EBE4D7` | `#141B3A` | parting field |
| `--ink` | `#2B2520` | `#E9E3D3` | English |
| `--ink-2` | `#4F453C` | `#C5BEAB` | Akkadian, notes |
| `--ink-3` | `#6F6256` | `#959CBD` | restorations, numbers, sigla |
| `--rule` / `--rule-2` | `#D8CDBC` / `#B5A792` | `#28325A` / `#3C4878` | ruled lines |
| `--accent` | `#27448F` lapis | `#D6B465` pyrite | keys, links, controls, SB |
| `--res` | `#4E5C8C` | `#A6B3E2` | resonance register (≈) |
| `--ob` | `#93441F` fired clay | `#DD9870` | Old Babylonian |
| `--hl` | `#EADFC4` | `#222B55` | highlighted line |

Contrast on `--bg`: ink 13.2:1 light, 14.0:1 dark; the faintest text, `--ink-3`, 5.2:1 and 6.6:1 (4.7:1 on the sunk field). OB is fired clay; SB is the lapis of the prologue. Dark values sit under `prefers-color-scheme: dark` guarded by `:root:not([data-theme="light"])`, and under `:root[data-theme="dark"]`. The switch sets `data-theme` and stores it, inside try/catch.

## Layers

Six layers: Akkadian, English, Glosses (inner margin), Commentary (outer margin), Resonances (≈), OB partings. Each is a real checkbox, so every toggle works without JavaScript. Both languages cannot be off at once; CSS restores the English, and the script re-checks the other language. With JavaScript, a toggle keeps the top visible line where it was; tested at three points on the phone, it moved 0 px.

## Page layouts

**Reader, wide screens (1180 px and up).** Each pericope is a grid: glosses 13 rem, text, commentary 16.5 rem. A line has four tracks: number, Akkadian (0.74 fr), English (1 fr), keys. Wrapped lines hang. Margins are sticky within their own pericope, so a note never drifts into the next passage. A key highlights its line and note; hovering a note highlights its line. A hidden margin keeps its column, so the text does not move sideways.

**Reader, 760 to 1180 px.** Interlinear (Akkadian above English), 46 rem measure; the margins fold under the pericope side by side.

**Reader, phone (under 760 px).** 16 px gutters, interlinear. A line with notes gets a 44 × 44 px key cell at its right edge. Tapping it opens a bottom sheet with the line (in the languages that are on), every visible note for it, Previous and Next line buttons, and Close; Escape and the scrim also close it. Without JavaScript the notes print under each pericope and the keys link to them. The layers form a fixed bottom bar of six 48 px cells. Contents is a `<details>` in the top bar that opens as a full-height panel of tablets and pericopes, with no script.

**Partings.** Double rules and a sunk field. Each witness column carries its siglum (`OB II (Pennsylvania), 1–23`) over a 2 px rule in the OB or SB colour. Wide screens show both; a phone shows one behind a two-tab radio switch, with no script.

**Complete text (not mocked).** Same tokens and line component, no margins. Each tablet's apparatus stays a `<details>` at its end; entries link to their lines and keyed lines open the same bottom sheet. Three layers: Akkadian, English, Apparatus. Lacunae become a centred row between rules. Each tablet ends with a catch-line (the first line of the next tablet, as the scribes wrote it) and a ruled colophon.

**Old Babylonian (not mocked).** One section per witness, headed by siglum, collection, line range and an ochre rule. The synopsis uses the parting component. On a phone, Contents replaces the fourteen-button witness grid.

**Landing (not mocked).** Three cards, each with name, one sentence and counts in sigla type. The cuneiform name 𒀭𒄑𒂆𒈦 remains the only cuneiform on the site, hidden from screen readers. Then the method with the bracket key, then sources.

## What I left out, and why

- Faux-cuneiform backgrounds, textures, gold-on-brown, glows. They are decoration, not evidence.
- Cuneiform signs as ornaments or dividers. A sign is text; used as ornament it reads as nonsense.
- The seven museum plates. They are hotlinked, so the self-contained mockup omits them. They belong between pericopes at 620 px with a ruled caption.
- Animation beyond a 200 ms sheet slide, which reduced motion turns off.

## Open questions

1. Decided: the decade mark is dropped (no manuscript source is cited for it). Half-brackets are to be shown once eBL data carrying them is fetched; the current repo data has none, so the mockup omits them.
2. Should obverse and reverse column breaks (obv. i, rev. iv) be marked? The builders do not yet extract them.
3. Should the reader be split into one page per tablet? Phone loading and Contents would both get simpler.
4. Some lettered glosses sit in the outer margin (I 246, *kiṣru ša Āni*). Deliberate, or should all glosses move inside?
