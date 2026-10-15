# Mahābhārata — project briefing

## What this is

An original English translation of selected passages from the Ādi Parva and
Sabhā Parva of the Mahābhārata: the cosmic frame (the cyclic world, the earth's
burden, the descent of the gods by portions) and the dice game that ends in the
disrobing of Draupadī and the second game. Published as a self-contained HTML
page at `docs/mahabharata/index.html`.

Translation is made from the Sanskrit. Commentary may engage the critical edition
and other translations, with citation. It must not borrow phrasing from any
published English translation.

## Source situation

- **Critical edition:** Bhandarkar Oriental Research Institute (BORI) Critical
  Edition, Pune, 1927–1966.
- **Typed text used for verification:** the GRETIL/BORI electronic text (Tokunaga
  et al., revised by John Smith), mirrored on Zenodo,
  <https://zenodo.org/records/6467313>. Files `mbh_01_u.htm` (Ādi) and
  `mbh_02_u.htm` (Sabhā). Verse references in the form `01,058.006c` (book,
  adhyāya, śloka, pāda). This is a transcription of the BORI constituted text.
  It also carries the starred and appendix passages, with refs containing `*` or
  `@` (e.g. `02,058.009d*0525_01`); these are not the constituted text. It does
  not carry the manuscript apparatus.
- **Scanned BORI volumes** (page images, not OCR):
  <https://archive.org/details/mahabharat-bori-critical-edition-sanskrit-only>.
  Its djvu text is OCR and is noisy; do not use it as the verification source.
- **Apparatus:** the BORI critical notes were not reachable when this work was
  checked. Notes that depend on apparatus readings are marked as our reading, not
  as apparatus findings.

## Verification status

- `verify_refs.py` checks the page mechanically. Every Sanskrit block (113) has a
  verse reference. The pāda-level expansion of each reference equals exactly the
  set of constituted-text lines printed in the block, in source order. No line
  comes from a starred passage. Run:
  `python3 mahabharata/verify_refs.py docs/mahabharata/index.html <dir>`, where
  `<dir>` holds `mbh_01_u.htm` and `mbh_02_u.htm` from Zenodo 6467313.
- Script: each verse line carries Devanagari (shown by default) and IAST (shown
  by the page's script toggle). The IAST is the source of truth.
  `build_devanagari.py` derives the Devanagari from it with `devanagari.py`;
  never edit the Devanagari by hand. After any change to a verse line, run
  `python3 mahabharata/build_devanagari.py docs/mahabharata/index.html <dir>`,
  then `verify_refs.py`. The verifier rejects a Devanagari line that differs from
  the transliteration of its IAST, or that does not convert back to the same
  letters. Prose (commentary, glosses, names) stays in IAST. The Fable model
  reviewed the Devanagari conventions: `review-fable-devanagari.md`.
- Reference format: a half-verse is cited with pāda letters (`1.58.20cd–22`,
  `2.44.11cd`). Verses omitted inside a block are marked with "…" in the Sanskrit
  and the English, and are absent from the reference (`2.61.52–53, 56–57`).
- Commentary and translation review (October 2026): eight Haiku agents audited
  the prose by page segment. The Fable model reviewed the commentary,
  verse-by-verse fidelity, IAST, the references, and memorization risk, and
  adjudicated the Haiku findings. Record: `review-fable.md`. All errors and
  imprecisions in that record are applied. Its "notes" are optional and are
  not applied, and §4.8 (references in the gloss column) is not applied.
- Confirmed attributions: Vidura as son of Atri (1.61.79); Dhṛtarāṣṭra as a
  gandharva lord born into the Kuru line (1.61.77–78); blindness from "his
  mother's fault and the sage's anger" (1.61.78).
- Garment miracle: the constituted text (2.61.41, 2.61.48) gives no stated cause.
  The starred recension insertions add prayers and credit Dharma. Which
  manuscripts carry which passages is not verified.

## Translation decisions (current)

- *dharma* and *daiva* are left untranslated (*daiva* glossed once in the
  introduction).
- *dhātṛ*/*saṃvidhātṛ* → "the Ordainer"; *vidhi* → "ordinance"; *diṣṭa* →
  "appointed"; *niyoga* → "appointment".
- *prakṛti* (2.45.13) → "his own people", with a note on the political sense.
- *rajasvalā* → "in my period", with a note on seclusion and impurity.
- *pauruṣa* → "manhood's striving", with a note on the *puruṣa* echo.
- *bandhakī* → "whore", kept deliberately, with a note. Bhīma's *bandhakyaḥ*
  (2.61.1) is also "whores".
- *anṛtau* (1.58.6) is the locative of *anṛtu* ("unseasonable time"), not of
  *anṛta* ("untruth"). No untruth pun.

## Open items

- The Edgerton note on the two versions of the dice scene is left out: the only
  citation was secondhand and not verified.
- Hanging indent for wrapped pādas and the Part II heading: see the PR description.
- Apparatus-dependent readings remain our reading until the BORI notes are checked.
- Open notes from the Fable review (§5): "Steward" for *kṣattṛ* and "Wolf-belly"
  for Vṛkodara are also van Buitenen's fixed renderings. No phrase-level
  resemblance was found. A change is optional.
