# The Guest-House (مهمان‌خانه) — project briefing

## What this is

A complete annotated translation of the two Masnavi passages that lie behind the
popular English poem "The Guest House," delivered as a single self-contained HTML
page. Published on GitHub Pages under `docs/guest-house/`.

The central editorial claim, and the reason the edition exists:

> **"The Guest House" is not a poem.** Rumi wrote no free-standing work of that
> name. The English poem readers know (Coleman Barks's) is a modern extraction
> from the *Masnavi-yi Maʿnavi* — a ~25,000-couplet teaching discourse in verse —
> carved out of a didactic digression inside Book V's Ayaz narrative.

The digression runs in three moves:

| Move | Lines | Rubric (§) | What it is |
|---|---|---|---|
| 1 | V.3644–3646 | §155 | The parable stated: the body as guest-house |
| 2 | V.3647–3675 | §156 | A story dramatizing its violation: the householder's wife who resents a rain-stranded guest |
| 3 | V.3676–3707 | §157 | The parable resumed and elaborated: thought as daily guest, grief as joy's servant, the astrological conceit, Job hosting affliction as "God's guest," the two Arabic prayers, the closing root-not-branch teaching |

Barks carved a lyric out of moves 1 and 3, skipped the story, and added a title.
Presented as a standalone poem it reads as a meditation on feelings; read as what
it is — a preacher's parable-with-exemplum inside a theological discourse — its
claims are doctrinal.

This edition translates both didactic passages **in full and in their true order**
(35 couplets: 3 + 32), summarizes the intervening story rather than translating it,
and documents in notes exactly what the popular composite removes.

## Files in this folder

- `guest-house-translation.md` — **the canonical edition.** Persian text and English
  for V.3644–3646 and all 32 couplets of V.3676–3707, with line numbers, the §156
  summary notice, "Notes on the Persian," "Key Terminology (corrected)," "What the
  Popular Composite Removes," and sources. `docs/guest-house/index.html` is a
  typeset presentation of this file's content, verbatim.
- `guest-house-source-research.md` — source documentation: language stage, critical
  edition of reference, the composite's structure, the translation brief, status.
- `FABLE-REVIEW-REQUEST.md` — the brief sent to the expert reviewer (editorial history).
- `FABLE-REVIEW.md` — the expert review of the earlier draft, with its addendum on
  the revised 11-couplet version and the numbered list of required fixes.

## Text source

- **Edition of reference**: Reynold A. Nicholson, *The Mathnawí of Jaláluʾddín Rúmí*,
  8 vols., Gibb Memorial Series (1925–1940) — authority for the Persian text and for
  the line numbering used throughout.
- **Persian verified against**: the received critical text as reproduced at Ganjoor
  (Masnavi Book V, §§155–157) and masnavi.net.
- **Language**: Classical New Persian (13th century), with two Arabic couplets
  (V.3694–3695). *Not* Middle Persian — Middle Persian (Pahlavi) is Sasanian-era;
  an early draft of this project used the term in error and was corrected.

## Editorial history

1. **Draft** — an 8-couplet, then 11-couplet version, presented as a poem, with the
   splice undisclosed.
2. **Expert review** (`FABLE-REVIEW.md`, 2026-08-26) — verdict *not ready for
   publication*: the "Middle Persian" misnomer, a misquoted opening line, an
   undisclosed splice of non-contiguous passages, two substantive mistranslations
   (an inserted negation; "open the way" for the *rāh zadan* waylaying idiom;
   later, "from you" for *az mā-warā*, "from the Beyond"), broken transliterations,
   and imported technical vocabulary the passage does not contain.
3. **Corrected complete edition** (`guest-house-translation.md`) — all required
   fixes applied, both passages translated in full and in order, the composite's
   structure disclosed, the apparatus re-scoped to what the text actually says.

## Editorial rules (do not violate)

1. **The translation is finalized and expert-reviewed. Do not retranslate or reword
   it**, in the markdown or in the published HTML. The HTML carries the markdown's
   content verbatim.
2. Claim only what the text contains. *qadr*, *fanā*, *tawḥīd*, *tajallī* do not
   occur in this passage and must not be reintroduced as textual content; the
   passage's Islamic theology is explicit enough without them (*ghayb*, *ḍayf-i
   Khudā*, *ṣāniʿ*, the Arabic prayers, Job).
3. Interpretation is marked as interpretation (e.g. the divine referent of
   *aṣl-i khayr*, 3679).
4. §156 is summarized, not translated — and the omission is stated on the page.
   Any edition that drops it silently commits the fault this one prosecutes.
5. Line numbers are Nicholson's. Do not renumber.

## Published edition

`docs/guest-house/index.html` — one self-contained page (inline CSS; Google Fonts
only, per the site's practice), manuscript-warm palette, theme-aware light/dark via
CSS custom properties (`prefers-color-scheme` + `data-theme`). Persian couplets are
set RTL (`dir="rtl"`) in a Naskh-capable stack (Noto Naskh Arabic / Amiri, with
system Arabic fallbacks) beside the English and Nicholson's line numbers. Back link
to `../`.

## Known state / open tasks

- Collate against Nicholson's printed volumes directly (the Persian is currently
  collated against Ganjoor and masnavi.net, both reproducing the received text).
- Decide whether to add a verse translation of §156's story, which would make the
  edition complete for V.3644–3707 with nothing summarized.
