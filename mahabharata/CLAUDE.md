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
  adhyāya, śloka, pāda). This is a transcription of the BORI text without its
  apparatus.
- **Scanned BORI volumes** (page images, not OCR):
  <https://archive.org/details/mahabharat-bori-critical-edition-sanskrit-only>.
  Its djvu text is OCR and is noisy; do not use it as the verification source.
- **Apparatus:** the BORI critical notes were not reachable when this work was
  checked. Notes that depend on apparatus readings are marked as our reading, not
  as apparatus findings.

## Verification status

- All Sanskrit verse lines on the page match the typed text (checked 428 lines).
- The page's verse references were checked against the typed text, including
  1.1.37, 1.37.21, 1.58.6, 1.61.77–80, 2.45.13, 2.52.18, 2.60.25, 2.61.35,
  2.67.3.
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
- *bandhakī* → "whore", kept deliberately, with a note.
- *anṛtau* (1.58.6) is the locative of *anṛtu* ("unseasonable time"), not of
  *anṛta* ("untruth"). No untruth pun.

## Open items

- The Edgerton note on the two versions of the dice scene is left out: the only
  citation was secondhand and not verified.
- Hanging indent for wrapped pādas and the Part II heading: see the PR description.
- Apparatus-dependent readings remain our reading until the BORI notes are checked.
