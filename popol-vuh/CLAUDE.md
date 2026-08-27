# Popol Vuh — project briefing

## What this is

An original English translation of the Popol Vuh (the K'iche' Maya council book:
creation, the hero twins Hunahpu and Xbalanque against the lords of Xibalba, the
origin of maize people, and the genealogy of the K'iche' lords), made directly
against its primary manuscript witness, delivered as self-contained HTML on
GitHub Pages.

## The source situation (different from Sappho or Gilgameš)

Unlike Gilgameš (many cuneiform witnesses) or Sappho (multiple papyri/testimonia
per fragment), the Popol Vuh survives in **one physical manuscript**: Father
Francisco Ximénez's early-18th-century transcription of an older K'iche' document
(now lost), written in Guatemala and today held as Ayer MS 1515 at the Newberry
Library, Chicago. There is no earlier witness to cross-check against — the K'iche'
text Ximénez copied out is, as far as anyone knows, the closest thing to an
original that exists.

What *does* give this project a genuine multi-recension structure is Ximénez's own
double treatment of the material:

1. **The parallel transcription** — K'iche' text with his own interlinear/facing
   literal Spanish translation, made close to the time of transcription (c. 1701–3).
2. **The revised literary version** — a separate, later, freely rewritten Spanish
   narrative prose version Ximénez produced for his *Historia de la Provincia de
   San Vicente de Chiapa y Guatemala*, smoothing and reorganizing the same material.

Both are by the same hand and are themselves primary sources (not modern
scholarship), so both are fair game to consult as witnesses to what the K'iche'
meant. Confirm exact holdings/digitization access during sourcing before relying on
specifics here — this section should be corrected against what's actually found.

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

- `src/sections.json` — the text divided into translatable sections (likely
  following the traditional four-part structure: creation; Hunahpu/Xbalanque vs.
  Xibalba; origin of the maize people; migrations and genealogy of the K'iche'
  lords), each with its K'iche' text, Ximénez's contemporary Spanish (both
  recensions where available), and source citations.
- `src/translations.json` — the original English translations, keyed by section
  id, plus the Fable review verdict for each.
- `src/build.py` — assembles `docs/popol-vuh/index.html`.

## Published edition

Published to GitHub Pages under `docs/popol-vuh/`.

## Provenance

Sourced and translated starting 27 Aug 2026.
