# alignment.json

Maps each K'iche' block to its English paragraphs, per section. Translations are stored per section (`translations_current_best.json`, `paragraphs` list), not per paragraph, so the build needs this map to set K'iche' and English side by side.

## Fields

Per section: `section` (s01-s36), `title`, `english_paragraph_count`, `blocks`, `unmatched` (English indexes with no block, each with a `reason`; currently empty everywhere).

Per block:

- `id`: b1, b2, ... in section order.
- `kiche_paragraphs`: paragraph ids as in `sections.json` / `popolwuj-paragraphs.json` (p01-p97). Every id in the section appears in exactly one block, in order.
- `english_paragraphs`: zero-based indexes into the section's `paragraphs` list, a contiguous run. Every index appears in exactly one block.
- `folios`: K'iche' column range from the TEI `<pb>` markers, `fol. 1r-1v` style (s1 = recto, s2 = verso).
- `method`: `explicit` only if the source links the two (xml:id, shared anchor, English paragraph id). The English paragraphs carry no ids and no anchors, so every block is `inferred`.
- `confidence`: `high`, `medium`, `low`. High means the cut or the merge was checked at both edges against Ximenez's Spanish and the proportions of the text; medium means the data has a quirk (below); low means unresolved. No block is low.
- `note`: why the block is shaped as it is.
- `english_elsewhere` (s25 only): English that translates this block's paragraph but is stored in another section.

## Method

1. For each section, compare the cumulative length of the K'iche' paragraphs (and of the Spanish column) with the cumulative length of the English paragraphs, to find where an English paragraph boundary could coincide with a K'iche' paragraph boundary.
2. Check every candidate cut by reading the end of one English paragraph and the start of the next against the Spanish (Ximenez's own, a primary witness; no modern translation consulted).
3. Where an English paragraph runs across a K'iche' paragraph boundary, the K'iche' paragraphs are merged into one block. Many English paragraphs do: the translators worked per section, so s09, s11, s20, s22, s23, s27, s28, s32, s35 are single blocks even though they hold two to three K'iche' paragraphs.
4. Sections with one K'iche' paragraph are one block (forced).

## Folios

Computed from the K'iche' column's `<pb xml:id>` markers with the side state carried between paragraphs. The `<lb id>` values are not used: after some `<pb>` they are copied wrong (p02's first line on 1v is labelled f01-s1). `parse_tei.py` leaves `kiche_folios` empty because it reads `id`, not `xml:id`, on `<pb>`. The Spanish column has its own `<pb>` sequence, which can differ slightly from the K'iche' one (p05: 1v-2r against 1v-2v).

## Data quirks found

- **p34 and p58 are unlabelled in the K'iche' column.** The TEI has a `<p>` with no `xml:id` between p33 and p35, and another between p57 and p59. `parse_tei.py` folds each into the preceding paragraph, so p33's K'iche' contains the fire house (p34) and p57's contains p58, and `kiche_missing` is set on p34 and p58 although their K'iche' exists. Their identity as p34 and p58 rests on the Spanish column (`corresp="#p34"`, `#p58`).
  - s17: p33 and p34 are one block (English [1, 2], medium).
  - s24/s25: the K'iche' for p58 is in s24's p57, so s24's English [2] (second half) and [3] translate p58; s25 has no K'iche' for p58. The s25 block lists p58 with `english_elsewhere` pointing at s24. s25's start folio (38r) comes from the Spanish p58 (f38-s1 to 38v); K'iche' p59 begins on 38v. Both blocks are medium.
- An English paragraph in s24 (E[2]) holds a blank line inside one list item; the index count is unaffected.

Fixing `parse_tei.py` to split the unlabelled `<p>` would let a later map put p34 and p58 in their own blocks.
