# Bereshit — project briefing

Genesis 1:1–4:18 in English, made from the Hebrew text with the Septuagint (LXX)
as a second witness. The translation is poetic and fluid; it keeps the Hebrew's
raw roots and its ambiguities; a commentary column beside each verse gives root
sense, LXX divergences, and the choices made. Published as one self-contained
page: `docs/bereshit/index.html`.

Status: translator's draft complete for all 98 verses. Reviewed by an independent
Opus-model pass (Methodology, item 5), then revised against Rashi and Ibn Ezra as
normative interpreters, with a Fable-model check of that revision (item 6).

## Scope

- Hebrew/English verse numbers coincide throughout 1:1–4:18 (98 verses:
  31 + 25 + 24 + 18). "English 4:18" and "Hebrew 4:18" are the same verse.

## Sources (fetched, not recalled)

- **Hebrew witness** — `src/witness-hebrew.json`. Sefaria API:
  `https://www.sefaria.org/api/texts/Genesis.1.1-4.18?lang=he&context=0&pad=0&wrapLinks=0`,
  the `he` field only, footnote markup and HTML stripped. Pointed Masoretic text
  with cantillation. Fetched 2026-10-14. The edition is *Miqra according to the
  Masorah* (MAM), a Ben-Asher text edited at Hebrew Wikisource (CC-BY-SA): the
  `heVersionTitle` of the same API, checked 2026-10-15.
- **MAM documentation notes** — `src/mam-notes.json`. The notes of MAM on letter
  size, vowels, accents and spelling in the manuscripts (Leningrad, Aleppo as recorded by
  Sapir, Cairo 18, and others), from
  `https://bdenckla.github.io/MAM-basics/MAM-with-doc/A1-Genesis.html`, sigla from the
  project's decoder (`sigil-decoding.html`, `doc/sigil-decoding.md`). Fetched 2026-10-15.
  Used for section IV of the apparatus.
- **Greek witness** — `src/witness-lxx.json`. Blue Letter Bible LXX interlinear:
  `https://www.blueletterbible.org/lxx/gen/{1,2,3,4}/`, the
  `GkBibleText scriptureText` blocks, one `word-phrase` span per token, verse
  numbers from `data-print-verse-prefix`. Fetched 2026-10-14. The edition is not
  stated on the page; it is **Rahlfs (1935)**: collated 2026-10-15 against the CATSS
  morphological LXX (Rahlfs), `http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/01.Gen.1.mlxx`,
  it agrees letter for letter (accents and case set aside) in all 98 verses.
  `src/lxx_collate.py CATSS-FILE src/witness-lxx.json` repeats the collation.
- **Latin witnesses** — `src/witness-vulgate.json`: the Vulgate, Clementine text, from
  `https://www.thelatinlibrary.com/bible/genesis.shtml`, fetched 2026-10-15.
  `src/witness-old-latin.json`: the Old Latin as printed on tanakh.info (edition not named),
  fetched 2026-10-14. The site labels its two Latin lines inconsistently; each verse's
  Old Latin is the Latin line that is not the Vulgate text. Jerome made Genesis from the
  Hebrew (c. 390–405); the Old Latin was made from the Greek. Vg is therefore a fourth-century
  witness to a Hebrew text and to the Jewish reading of Jerome's teachers; VL is a witness to
  the Greek.
- **LXX 4:18:** BLB reads "Γαιδαδ καὶ Γαιδαδ ἐγέννησεν", that is "Gaidad, and
  Gaidad fathered": the Hebrew pattern ("Irad; and Irad fathered"), not a doubled
  name. Noted at 4:18.
- **Rashi** — `src/rashi.json`. Sefaria API:
  `https://www.sefaria.org/api/v3/texts/Rashi_on_Genesis.1.1-4.18?version=hebrew`,
  Hebrew only, HTML stripped. Version: Rosenbaum and Silbermann, 1929–1934.
  Fetched 2026-10-14. 80 verses carry comments.
- **Ibn Ezra** — `src/ibn-ezra.json`. Sefaria API:
  `https://www.sefaria.org/api/v3/texts/Ibn_Ezra_on_Genesis.1.1-4.18?version=hebrew`,
  Hebrew only, HTML stripped. Version: Piotrkow, 1907–1911. Fetched 2026-10-14.
  80 verses carry comments. Some comments are keyed to a neighbouring verse (for
  example, his note on לעולם of 3:22 stands under 3:6).

## Methodology (do not violate)

1. **Translate from the Hebrew, with the LXX as second witness.** Where the two
   differ, the commentary records both and the translation follows the Hebrew
   unless the note says otherwise.
2. **No published English translation consulted** — not the KJV, not the JPS,
   not any other. Translators work from the Hebrew and Greek witnesses above.
   **Disclosure:** the first Sefaria response carried an English rendering in
   the same JSON as the Hebrew. About 600 characters of it were printed before
   the Hebrew was extracted; they cover the opening of 1:1–1:2 only. The
   translation of 1:1–1:2 should be checked against this in review.
3. **Root and grammar glosses are the translator's own** from knowledge of
   Biblical Hebrew, not from a fetched lexicon (BDB, HALOT). They are flagged in
   the commentary as "disputed" or "uncertain" where the etymology is not
   established. A lexicon check is an open task.
4. **Every divergence between witnesses is recorded, not silently collapsed.**
   The 2:2 variant ("seventh day" in the Hebrew, "sixth day" in the LXX) is the
   clearest example.
5. **Independent review.** Every translation gets a review pass on the Fable
   model, checking fidelity to the Hebrew and Greek and flagging any suspicious
   resemblance to a known published translation. Where the Fable model is
   unavailable (for example, no usage credits), an Opus-model review on the same
   brief is permitted as a substitute. The page's commentary must name which
   model reviewed it and whether the review was run on the final text.
   **Done for this work with Opus, accepted by the project owner.** The Opus pass ran
   on the Hebrew, Greek and English files with no prior context; its findings are
   recorded in `review-opus-questions.md`. The decided phrases that still hold are
   in `text/decisions.txt` and are checked by `src/tool.py check`.
6. **Rashi and Ibn Ezra are the normative traditional interpreters.** Where both
   read the Hebrew against the English, the English follows them. Where they
   differ, both readings are recorded in the verse's `rashi:` and `ibn-ezra:`
   entries. Quote them from the fetched Hebrew only. The review that applied this
   rule, and its Fable-model check, are recorded in `review-rashi-ibn-ezra.md`.
7. **No transliteration in the commentary.** Notes, apparatus, Rashi and Ibn Ezra
   entries, word glosses and name meanings write Hebrew in Hebrew script and Greek
   in Greek script. English-form names used in the translation (Qayin, Hevel,
   Chavah, Eden, Nod, Ish, Ishah, the rivers and lands) are allowed.

## Files

- `text/ch1.txt` … `text/ch4.txt` — the edition, one block per verse (format below).
- `text/names.txt` — the names table: `Hebrew | English form | meaning`.
- `text/decisions.txt` — `ref | phrase` pairs that must stay in a verse's English:
  review decisions. Change a line only when the decision is reversed.
- `text/translit.txt` — transliterated words forbidden outside the English lines.
- `text/paragraphs.txt` — editorial paragraph breaks for the reading text (`ref | reason`).
  The reading text, printed before the verse-by-verse section, is divided first by the
  Masoretic open (פ) and closed (ס) paragraph marks of the Hebrew witness, which `tool.py` reads
  from `src/witness-hebrew.json`; this file adds breaks inside the long units only. `check`
  rejects a break that duplicates a Masoretic one. A line `verse: ref | reason` sets that verse
  as verse in the reading text, one printed line per `>` line.
- `text/apparatus.txt` — the critical apparatus appendix (format below): sigla; I. variant
  readings of the Hebrew witnesses and of the versions where they presuppose another Hebrew
  text; II. spelling and minor readings of the Samaritan Pentateuch; III. readings of the
  versions and the early interpreters at the cruxes; IV. the Masoretic manuscripts; limits.
- `src/witness-hebrew.json`, `src/witness-lxx.json` — the witnesses, keyed `chapter:verse`.
- `src/rashi.json`, `src/ibn-ezra.json` — the commentaries, keyed `chapter:verse`.
- `src/template.html` — the page shell and CSS; `{{READING}}`, `{{BODY}}`, `{{NAMES}}` and `{{APPARATUS}}` are filled.
- `src/lxx_collate.py` — collates the Greek witness against the CATSS Rahlfs file.
- `src/tool.py` — the edition tool. Standard library only. From the repo root:
  - `python3 -I bereshit/src/tool.py show 2:21 [3:15 …] [--sources]` — numbered
    Hebrew tokens, Greek, the verse block; `--sources` adds Rashi and Ibn Ezra.
  - `python3 -I bereshit/src/tool.py check` — every check; exit status 1 on failure.
  - `python3 -I bereshit/src/tool.py build` — check, then write `docs/bereshit/index.html`.
- `src/lexicon.md` — head terms per root.

## Text files

```
@ 2:21                                    verse reference; starts a block
> The Lord God threw a heavy sleep …      one printed line of English
note: תַּרְדֵּמָה, 'deep sleep' …            the commentary paragraph (one per verse)
app: מִצַּלְעֹתָיו: from his sides, or …     a reading held open (any number)
rashi: …                                  Rashi's plain-sense reading (any number)
ibn-ezra: …                               Ibn Ezra's reading (any number)
= 8 9 10 | He took one of his sides | 'and he took one from his sides'
```

- A line that starts with two spaces continues the field above it.
- `=` lines: Hebrew token indices (from `show`), the English fragment (must occur
  in the verse's `>` lines; `-` for none), and the literal sense of the Hebrew
  with any reason for the English. `-` as indices means the English adds words.
  Every Hebrew token of the verse is covered exactly once.
- `#` starts a comment line.

`check` enforces: all 98 verses in order; token coverage; every fragment present
in the lines; no Hebrew script in the English; no transliteration outside the
English; a note for every verse; the decisions; Hebrew in the names column.

## Apparatus file

```
## I. Variant readings                    a section
p: …                                      a paragraph
sig: SP | Samaritan Pentateuch, …         a siglum (Sigla section)
@ 2:2                                     the verse of the entries below
= הַשְּׁבִיעִי ] הַשְּׁבִיעִי {MT TO} ; הששי {SP} ; ἐν τῇ ἡμέρᾳ τῇ ἕκτῃ {G}
~ a note on the entry above
```

`lemma ] reading {SIGLA} ; reading {SIGLA}`. `+ x` is an addition, `om.` an omission;
`…` separates parts of a discontinuous lemma. `check` enforces: every siglum is defined;
every verse exists and entries run in verse order within a section; every Hebrew lemma
occurs, consonant for consonant, in the base text of its verse.

Sources of the apparatus (fetched 2026-10-14; the full texts stay outside the repository,
only the cited readings are recorded):
- Samaritan Pentateuch, Targum Onkelos, Samaritan Targum, Peshitta, a second Septuagint text
  (Gᵗ), Aquila, Symmachus, Theodotion: `https://tanakh.info/gn{c}-{v}` (1:1 is `?p=36`). The
  Samaritan text was collated against MT by machine (consonants, matres lectionis inside a
  word counted as spelling), and every reading checked by hand.
- Targum Neofiti (chapter 1 only) and Pseudo-Jonathan: Sefaria API, Hebrew versions.
- Qumran: reported, not collated (Wikipedia variant tables after van de Giessen; BAS on
  4QGenᵏ). DJD XII has not been consulted.
- Jubilees on Sefaria is Rubin's Hebrew retroversion from the Ethiopic (Vienna, 1870). The Qumran
  Hebrew (4Q216, DJD XIII 1–22; Ma'agarim text 11000) has not been obtained.
- Josephus, Ant. 1.27: Perseus (Niese). Bereshit Rabbah, Chagigah 12a, Pirkei de-Rabbi
  Eliezer, Saadia, Rashbam: Sefaria API, Hebrew versions.

## Editing

- Edit the text files, run `check`, then `build`. Do not hand-edit the HTML.
- The witnesses and commentaries are the record of what was read; do not edit
  them by hand. If one is re-fetched, update the fetch date in its `source` field.
