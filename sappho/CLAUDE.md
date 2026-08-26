# Sappho — project briefing

## What this is

An original English translation of Sappho's surviving fragments, made directly
against the ancient Greek witnesses (papyri and testimonia in quoting ancient
authors), delivered as self-contained HTML on GitHub Pages.

## Methodology (do not violate)

1. **No existing English translation is ever consulted.** Not Wharton, not
   Edmonds, not Barnard, not Carson, not Rayor, not anyone. Translators
   (subagents) work only from the Greek text placed directly in their prompt.
   They are explicitly instructed not to search for or recall any published
   English rendering, and not to use any tool for that purpose — only, if
   needed, a Greek lexicon (LSJ) for individual word senses.
2. **Witnesses and recensions come first.** Every fragment's ancient source(s)
   — papyrus siglum, or the ancient author who quotes it (Athenaeus,
   Dionysius of Halicarnassus, Pseudo-Longinus, Hephaestion, etc.) — are
   identified and cited before translation begins. Where a fragment survives
   in more than one witness, the variant readings are recorded, not silently
   collapsed into a single "best" text.
3. **Greek text is only ever taken from real, fetched, cited sources** — never
   reconstructed from a model's memory. Public-domain critical editions
   (Bergk's *Poetae Lyrici Graeci*, Edmonds' 1922 Loeb, Wharton's 1885
   *Sappho*) and open papyrological publications (for 20th/21st-century finds
   like the Brothers Poem and Kypris Poem) are acceptable sources; each Greek
   quotation in `src/` carries its source citation and, where fetched from the
   web, its URL.
4. Every translation is reviewed by an independent Fable-model pass, checking
   fidelity to the Greek and flagging any suspicious resemblance to a known
   published translation (a sign of memorization leakage rather than genuine
   translation).
5. Fragmentary text is presented honestly — lacunae stay marked, not
   silently bridged, in the spirit of the Gilgameš edition's bracket
   discipline.

## Repository structure

- `src/fragments.json` — per-fragment record: id, sourced Greek text
  (with inline witness/apparatus notes as fetched), structured witness
  list (source, edition, url, note), variant notes, sourcing caveats.
- `src/translations.json` — the original English translations, keyed by
  fragment id: per-line Greek/English pairs, full text, translator's
  note, and the Fable review verdict (faithful, resemblance check,
  whether it was revised).
- `src/raw-fetched/` — verbatim dumps of pages fetched during witness
  research, kept as an audit trail (see its own README).
- `src/build.py` — assembles `docs/sappho/index.html` from the two JSON
  files above. Run `python3 src/build.py` after any data change; no
  other dependencies (stdlib only).

## Design

Terracotta-and-violet palette (`--accent:#9c3b2e`, `--violet:#6b4a7a`),
parchment background, Cardo (Greek + Latin polytonic support) for body
text, Inter for UI chrome. Light/dark theme-aware, matching the landing
page's convention (CSS custom properties, `prefers-color-scheme`,
`data-theme` attribute). One scrollable page: sticky fragment-number
nav, one card per fragment with parallel Greek/English lines, a
collapsible witness list and textual-variants panel, and a "revised
after review" badge on any fragment the Fable pass flagged.

## Published edition

Published to GitHub Pages under `docs/sappho/index.html`.

## Provenance

Sourced and translated starting 26 Aug 2026.
