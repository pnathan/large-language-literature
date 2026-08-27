# Popol Vuh — project briefing

## What this is

An original English translation of the Popol Vuh (the K'iche' Maya council book:
creation, the hero twins Hunahpu and Xbalanque against the lords of Xibalba, the
origin of maize people, and the genealogy of the K'iche' lords), made directly
against its primary manuscript witness, delivered as self-contained HTML on
GitHub Pages.

## The source situation (different from Sappho or Gilgameš) — verified

Unlike Gilgameš (many cuneiform witnesses) or Sappho (multiple papyri/testimonia
per fragment), the Popol Vuh survives in **one physical manuscript**: Father
Francisco Ximénez's early-18th-century transcription of an older K'iche' document
(now lost), catalogued as **Ayer MS 1515** at the Newberry Library, Chicago. It's a
bound set of two volumes: vol. 1 is a Kaqchikel/K'iche'/Tz'utujil grammar and
catechetical material; **vol. 2** (56 folios) holds the Popol Vuh text itself plus
Ximénez's own *Escolios* commentary (6 further folios, closing note dated 1734).
Column layout is **parallel** (K'iche' left, Spanish right), not interlinear.
Current scholarship credits the K'iche' lineage-keepers who composed the
underlying text as co-authors, with Ximénez as transcriber/translator, not sole
author. Digitized by the Newberry/Library of Congress; the LOC states it is
unaware of any copyright restriction on the facsimile.

What gives this project a genuine multi-recension structure is Ximénez's own
double treatment of the material:

1. **The parallel-column text** (Ayer MS 1515, vol. 2) — K'iche' with his own
   close, contemporary Spanish translation, c. 1701–3. This is Ximénez's
   **autograph** — his own hand, highest textual authority.
2. **The revised literary version** — a separate, later, freely rewritten Spanish
   narrative Ximénez produced for his *Historia de la Provincia de San Vicente de
   Chiapa y Guatemala* (Libro I, cap. II–XXI). Ximénez's own autograph of the
   *Historia* is **lost**; what survives is a copy of a copy (via Juan Gavarrete,
   1848–75, published 1929) — lower textual authority, used as a secondary aid.

Both are primary sources (not modern scholarship), so both are fair game to
consult as witnesses to what the K'iche' meant.

### Real, fetched sources in use

- **Facsimile images** (the manuscript itself): Library of Congress / World
  Digital Library mirror of Ayer MS 1515 vol. 2 — `https://www.loc.gov/item/2021668226`
  (JSON API; the HTML page 403s), full PDF at
  `https://tile.loc.gov/storage-services/service/gdc/gdcwdl/wd/l_/19/99/5/wdl_19995/wdl_19995.pdf`.
  Public domain / no known restrictions per LOC.
- **Diplomatic transcription**: the Multepal Project's TEI-XML edition,
  `https://github.com/Multepal/popolwuj-original` (MIT licensed), file
  `xom-all-flat-mod-pnums-lbids.xml` — parallel K'iche'/Spanish columns,
  paragraph-aligned (`p01`–`p97`, ~97 paragraphs across 56 folios), manuscript
  line IDs, ~414 tagged named entities. Itself descends from the Ohio State
  University Libraries' 2007 transcription (that legacy URL was blocked/403
  during sourcing and could not be independently re-verified this session —
  worth a follow-up check). Fetched and parsed locally into
  `src/popolwuj-paragraphs.json` (see `src/parse_tei.py`) — this is the primary
  data source for translation, **not** any secondhand description of it.
- **Escolios** (Ximénez's commentary, separate from the narrative): also
  transcribed folio-by-folio in the same repo, `escolios/` — not yet pulled into
  the translation pipeline; treat as optional appendix material.
- **The *Historia* (second recension)**: archive.org, CIRMA/Guatemala scan of
  the 1929 Biblioteca "Goathemala" edition —
  `https://archive.org/details/BibliotecaGoathemalaAGHGVolIHistoriaProvinciaSanVicenteDeChiapaGuatemala`,
  OCR text at the same URL + `_djvu.txt`. Tagged CC BY-NC-ND by the uploader, but
  the underlying 1929 publication is almost certainly US public domain now
  (pre-1978, 95-year rule) — treat the *words* as free to consult, the NC-ND tag
  as a scan-file courtesy label, not a live restriction.
- **Explicitly not used**: omnika.org (blocked; its Spanish transcript is
  Recinos's own edition anyway — banned source), Allen Christenson's Mesoweb
  transcriptions (real and high-quality, but Christenson 2003/2004 is one of the
  banned modern translations — using his transcription/line-division choices
  risks contaminating a from-scratch effort).

### Section division

The text is divided into 36 translatable sections (`src/build_sections.py`),
following the traditional four-part structure (creation; the hero twins vs.
Xibalba; the maize people; migrations and genealogy) with boundaries placed
using the Multepal transcription's own paragraph numbering — paragraph id
(`p01`–`p97`) is the authoritative citation key; folio numbers are an
approximate secondary reference only. Section titles are working
descriptors, not translations, and are provisional pending a translator
actually reading each section.

## Methodology (do not violate)

1. **Translate from the K'iche' text as the primary source.** Ximénez's own
   contemporary Spanish (both the interlinear version and the Historia's revised
   version) may be consulted as a witness/aid for obscure K'iche' vocabulary and
   as the "recension" comparison this project's witness-first approach calls for
   — it is a primary-source document, not a modern translation.
2. **No modern published translation is ever consulted** — not Recinos (1950),
   not Goetz & Morley (1950), not Tedlock (1985/1996), not Christenson (2003), not
   anyone. Translators (subagents) work only from the K'iche' (and Ximénez's own
   contemporary Spanish as a witness) placed directly in their prompt. They are
   explicitly instructed not to search for or recall any published English
   rendering.
3. **Both of Ximénez's recensions are recorded**, not silently collapsed — where
   his interlinear version and his later Historia version diverge (word choice,
   omission, reorganization), that divergence is noted rather than picked from
   silently.
4. **Source text is only ever taken from real, fetched, cited sources** — never
   reconstructed from a model's memory. The Newberry Library's own digitized
   facsimile/transcription of Ayer MS 1515, and any public-domain or open
   scholarly transcription of it, are acceptable; every quotation in `src/`
   carries its source citation and, where fetched from the web, its URL.
5. Every translation is reviewed by an independent Fable-model pass, checking
   fidelity to the K'iche'/Ximénez-Spanish source and flagging any suspicious
   resemblance to a known published translation.
6. Fragmentary or illegible passages in the manuscript are marked honestly, not
   silently bridged.

## Repository structure

- `src/popolwuj-tei.xml` — the Multepal Project's TEI-XML diplomatic
  transcription, fetched verbatim (MIT licensed; see sourcing above).
- `src/parse_tei.py` — parses the TEI XML into `src/popolwuj-paragraphs.json`:
  per-paragraph K'iche'/Spanish text (both a continuous-prose form and the
  diplomatic per-manuscript-line form), folio ids, and tagged entities.
- `src/build_sections.py` — groups the 97 paragraphs into the 36 translatable
  sections defined there, writing `src/sections.json`.
- `src/translations.json` — the original English translations, keyed by section
  id, plus the Fable review verdict for each.
- `src/build.py` — assembles `docs/popol-vuh/index.html`.

## Published edition

Published to GitHub Pages under `docs/popol-vuh/`.

## Provenance

Sourced and translated starting 27 Aug 2026.
