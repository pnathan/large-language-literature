# Bereshit — project briefing

Genesis 1:1–4:18 in English, made from the Hebrew text with the Septuagint (LXX)
as a second witness. The translation is poetic and fluid; it keeps the Hebrew's
raw roots and its ambiguities; a commentary column beside each verse gives root
sense, LXX divergences, and the choices made. Published as one self-contained
page: `docs/bereshit/index.html`.

Status: translator's draft complete for all 98 verses. Reviewed by an independent
Opus-model pass, accepted by the project owner as the review for this work in place
of the Fable pass, which could not run (no usage credits). See Methodology, item 5.

## Scope

- Hebrew/English verse numbers coincide throughout 1:1–4:18 (98 verses:
  31 + 25 + 24 + 18). "English 4:18" and "Hebrew 4:18" are the same verse.

## Sources (fetched, not recalled)

- **Hebrew witness** — `src/witness-hebrew.json`. Sefaria API:
  `https://www.sefaria.org/api/texts/Genesis.1.1-4.18?lang=he&context=0&pad=0&wrapLinks=0`,
  the `he` field only, footnote markup and HTML stripped. Pointed Masoretic text
  with cantillation. Fetched 2026-10-14. The edition Sefaria serves is not named
  in the response and is not independently confirmed here.
- **Greek witness** — `src/witness-lxx.json`. Blue Letter Bible LXX interlinear:
  `https://www.blueletterbible.org/lxx/gen/{1,2,3,4}/`, the
  `GkBibleText scriptureText` blocks, one `word-phrase` span per token, verse
  numbers from `data-print-verse-prefix`. Fetched 2026-10-14. **The edition is not
  stated on the page.** It is not confirmed as Rahlfs (1935). Treat LXX readings as
  "the LXX as presented by BLB" until the edition is checked.
- **LXX oddity, recorded not corrected:** BLB's 4:18 reads "Γαιδαδ καὶ Γαιδαδ",
  a doubled name. The Hebrew repeats the subject ("and Irad fathered"), so the
  doubling is a faithful rendering of the Hebrew, not a corruption. Noted in
  `translation.py` at 4:18.

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
   recorded in `review-opus-questions.md`, and the kept and decided items are checked
   by `src/check_decisions.py`. The Fable pass has not run (no usage credits on the
   account); it can be run later and its findings added to that record.

## Files

- `src/witness-hebrew.json` — 98 verses, Hebrew, keyed `chapter:verse`.
- `src/witness-lxx.json` — 98 verses, Greek, keyed `chapter:verse`.
- `src/translation.py` — `T`, a list of `(ref, lines, commentary)`. Lines are the
  poetic English, one entry per printed line.
- `src/build.py` — renders `docs/bereshit/index.html` from the three above.
  Standard library only. Run from the repo root:
  `python3 bereshit/src/build.py`.

## Editing

- Change the English in `translation.py`, then rebuild. Do not hand-edit the HTML.
- The witnesses are the record of what was read; do not edit them by hand. If a
  witness is re-fetched, update the fetch date in its `source` field.
