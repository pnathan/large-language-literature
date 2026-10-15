# Devanagari typesetting review — Mahābhārata page (Fable)

Scope: `scratchpad/deva-sample.md` (159 lines) plus all 445 Devanagari lines
extracted from `docs/mahabharata/index.html`. Letter-level identity is proven by
the round-trip test; this is orthography and typesetting only. No file edited.

## A. Conventions

1. Consonant-final word joined to the next word — **standard**. This is how the
   BORI Devanagari prints the constituted text (तच्छ्रूयते, यस्मिंस्तच्छ्रूयते,
   प्रायाद्विदुरोऽश्वैरुदारैर्…). Correct.
2. Virāma + space at the ";" pāda boundary of a triṣṭubh — **non-standard;
   recommend joining**. Reasons: (a) BORI prints a half-verse as one continuous
   string; sandhi across the a|b boundary is written joined exactly as inside a
   pāda (cf. the textbook case BhG 2.5 महानुभावाञ्छ्रेयो, where pāda a ends in
   -bhāvān). The virāma-plus-space style (रैर् महा) is a Western Indological
   print convention, not an Indian edition's. (b) The page already joins across
   the a|b boundary in every śloka, because the typed text has no ";" there:
   राजन्न नागा (1.58.26 sample 26), प्रावारानश्नासि (158), तानक्षान्पुनरेवान्वपद्यत
   (277), प्रश्नेऽस्मिन्प्रमाणमिति (404). Treating triṣṭubh boundaries differently
   is an inconsistency within the page. (c) In नाथवच् चकर्ष the sandhi t→c was
   made precisely because the words are in contact; writing a virāma there is a
   half-measure. Fix: let ";" behave as a plain word space in `_pada`/`line`
   (i.e. transliterate the whole half-verse as one pāda). Affected lines (page
   line numbers): 1124 प्रणीतस्तत्रात्ययो; 1169 उदारैर्महाजवैर्; 1199
   संनिविष्टानित्यागतोऽहं; 1242 शासनान्न गन्तुम्; 1245 कदाचित्तदाहितं; 1608
   शीघ्रमानन्दो; 1636 प्रातिकामिन्को; 1669 लघीयान्यत्त्वं; 1712 रोषाद्दुःशासनस्; 1724
   सभासमीपमानीय; 1725 अनाथवच्चकर्ष; 1783 देहान्संदीपयामास; 1818 प्रवृत्तिमबुध्यमानः;
   1819 यस्मात्पश्चाच्च; 1820 सभायामीशाः; 2082 राजन्समन्ततः. (16 lines; no others
   have a consonant before ";".) Pāda-final at the *end* of a half-verse (before
   । or ॥) correctly keeps virāma.
3. Avagraha attached to the preceding word, and the following word attached to
   it (निष्प्रभेऽस्मिन्निरालोके) — **standard**. All 47 avagraha lines checked: no
   space before ऽ, no ऽ after a virāma. Single ऽ for e/o + a matches BORI.
4. Space after vowel-, anusvāra- and visarga-final words — **standard** (BORI
   practice). Hiatus written with a space and an independent vowel (वाचा अनुज्ञाता,
   किलेमे अधना, मत्त आहो, सर्व एव, युधिष्ठिर इति, हन्ति अभिमानश्च, सुश्रोणी असितायत…,
   याज्ञसेनि एकाम्बरा) — all correct; these are hiatuses of the constituted text.
   Anusvāra for word-final m before a consonant and for the internal nasals that
   BORI itself writes with anusvāra (संजज्ञे, पुंगव, वसुंधरे, संबभूवुः, धनंजयो,
   संमतां, संहत-) — correct, since the IAST reproduces BORI's own spelling; the
   explicit class nasals where the IAST has them (पङ्कजम्, शङ्खो, पाञ्चालि, अन्तक,
   एकाम्बरा) are right.
5. Daṇḍa and numerals — **standard**. "… भवेत् ।" and "… ॥ २४ ॥" with spaces
   is BORI's layout; Devanagari digits correct in every line checked; all 445
   lines end in । or ॥ n ॥; no double spaces. The । । ॥ pattern for three-line
   verses does not occur in the page (nothing to check).
6. Noto Serif Devanagari (weights 400, 500 loaded; only regular is used) — fine;
   it carries U+0964/0965, ऽ, ॄ, and the digits. `lang="sa-Deva"` on each span
   is correct and helps shaping/hyphenation. Keep `<html lang="en">`.

## B. Lines wrong or non-standard

- The 16 virāma-plus-space lines under A.2 (sample lines 184, 192, 200, 207,
  210, 279, 282, 290, 297, 301, 302, 319, 330, 331, 332, 423).
- Indefinite particles split by the IAST word division. BORI (and every Indian
  edition) prints these as one word; the Devanagari should too:
  - page 405 / sample 1-block: किं चिद्भूतं → किंचिद्भूतं
  - page 423: तत्क्व चित् → तत्क्वचित्
  - page 534: क्व चित् → क्वचित्
  - page 790: कथं चन → कथंचन
  - page 892: कदा चित्सभामध्ये → कदाचित्सभामध्ये (the present form, with cit
    joined forward but not backward, is the most visibly odd)
  - page 1245 (sample 210): कदा चित् → कदाचित् (and joined to तदाहितं per A.2)
  - page 1637 (sample 283): किं चित् → किंचित्
  - page 1873: किं चिद्या → किंचिद्या
  - page 1960: किं चन → किंचन
  Script fix: join a following `cit`/`cid`/`cana` to the preceding word
  (कश्चित्, तज्जुषस्व-type cases already join by rule 1). The IAST column can keep
  the GRETIL spacing; the round-trip strips spaces, so the test still passes.
- Nothing else: conjunct choice, anusvāra vs. class nasal, avagraha placement,
  hiatus, daṇḍa placement and numerals are all correct in the sample and in the
  full page scan.

## C. Rendering to check visually

- Stacked/rare conjuncts (Noto Serif Devanagari has glyphs for all, but check
  height against `line-height:1.9` and the 1.4em hanging indent):
  एतज्ज्ञात्वा (ज्ज्ञ), धर्मसौक्ष्म्यात् (क्ष्म्य), विद्वञ्श्रेय (ञ्श्र), सुहृद्द्यूतं /
  स्याद्द्यूतहेतोः (द्द्य), ऐश्वर्याद्भ्रंशिताश्चापि (द्भ्र), विदुरैतद्ब्रवीमि (द्ब्र),
  चार्वङ्ग्या (ङ्ग्य), कृत्स्ना (त्स्न), नियोगात्स्थविरस्य (त्स्थ), बलवान्राजन्दिष्टस्यास्मि /
  राजन्राज्ञां (half-न before र: न्र renders as न्‍र with half form, correct but
  unusual-looking).
- Repha + anusvāra on one akṣara: नृशंसकर्मंस्त्वम् (र्मं) — confirm the dot sits
  right of the repha, not colliding.
- Vocalic ṝ sign: भ्रातॄणां, भर्तॄन्कुपितानपश्यत् — ॄ under a conjunct base (भ्रा is
  fine; त + ॄ).
- `overflow-wrap:break-word` on the blockquote can split a long joined string
  (e.g. उदारैर्महाजवैर्बलिभिः) inside a word at phone width; prefer
  `overflow-wrap:normal` for `.dev` and let the pāda's own spaces wrap. Check
  the longest triṣṭubh lines (1169, 1725, 1819) at 360px.
- The IAST toggle button text "देवनागरी" at .82rem — check the ॄ/matras are not
  clipped by the button's `overflow:hidden`.

## Summary

1. Conventions 1, 3, 4, 5, 6 are standard BORI-style Devanagari; sample and full page check out letter- and mark-perfect.
2. Convention 2 (virāma + space at ";") is non-standard and inconsistent with the page's own śloka handling: join across the triṣṭubh pāda boundary (नाथवच्चकर्ष, सभासमीपमानीय), as BORI does; 16 lines affected.
3. Indefinite particles split by the IAST (कदा चित्, किं चित्, क्व चित्, किं चन, कथं चन, किं चिद्) should print as one word (कदाचित् etc.); 9 lines.
4. Hiatus (वाचा अनुज्ञाता, किलेमे अधना, मत्त आहो), avagraha, anusvāra vs. class nasal, daṇḍa and numerals: no errors found.
5. Visual check: ज्ज्ञ, क्ष्म्य, ञ्श्र, द्द्य, द्भ्र, ङ्ग्य, र्मं, ॄ; and `overflow-wrap:break-word` may split joined words at phone width.
6. Both fixes are one-line changes in devanagari.py; the round-trip test is unaffected.

---

## Disposition

- §A convention 2 (join across the triṣṭubh pāda boundary): applied in `devanagari.py`.
- Indefinite particles (cit/cid/…, cana) joined to the preceding word: applied.
- `overflow-wrap:normal` for Devanagari lines: applied.
- Conjuncts listed for visual check: rendered in Noto Serif Devanagari; all form correct ligatures.
