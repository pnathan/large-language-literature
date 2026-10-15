# Review against Rashi and Ibn Ezra, and apparatus audit

Date: 2026-10-14. Sources: `src/rashi.json` and `src/ibn-ezra.json`, the Hebrew
text of both commentaries on Genesis 1:1–4:18, fetched from Sefaria.

## Policy

Rashi and Ibn Ezra are the normative traditional interpreters for this edition.

- Where both read the Hebrew against the English, the English follows them.
- Where they differ from each other, the English keeps its reading (or takes one
  of theirs), and both readings are recorded in the verse's `rashi:` and
  `ibn-ezra:` entries and, if the point is open, in `app:`.
- Homiletic readings that Rashi labels as such are recorded only when they bear
  on the plain sense.

## Changes in the English: both commentators against the earlier reading

| Verse | Before | After | Rashi | Ibn Ezra |
|---|---|---|---|---|
| 1:1–1:2 | "At the start, Divinity cut: the heavens, and the ground." (main clause) | "At the start of Divinity's cutting the heavens and the ground— the ground was waste and void, …—" (time clause) | construct; main clause at 1:3 | construct; main clause at 1:2 |
| 1:9 | "gather and wait in one place" | "be gathered into one place" | הִקְוָם, gathered | יתחברו, joined |
| 2:6 | "A seep would well up … would soak" | "A vapour went up … and watered" | the deep rose and watered the clouds | אֵד is like smoke; a past event |
| 2:19 | "the Lord God potted" | "the Lord God had potted" | the making of 1:25 | pluperfect (at 1:9) |
| 2:20 | "he found no help" | "for himself the human found no help" | the human found none | ולנפשו לא מצא |
| 2:21–22 | "rib" | "side" | מִסְּטָרָיו | והטעם צד |
| 3:15 | "he will snap at your head" | "he will crush your head" | יְכַתֶּתְךָ | יככה בראש |
| 3:16 | "your conceiving" | "your pregnancy" | צַעַר הָעִבּוּר | ההריון |
| 4:12, 4:14 | "a stumbler" | "a drifter" | no leave to stay in one place | נד is the brother of נע |
| 4:13 | "too great to lift, too great to forgive" | "too great to bear" | bear (as a question) | punishment too great to bear |
| 4:15 | "whoever kills Qayin will be paid back sevenfold" | "whoever kills Qayin— in seven generations vengeance will be taken" | threat unfinished; vengeance on Qayin after seven generations | עד שבעה דורות |

## Changes in the English: fidelity to the Hebrew

| Verse | Before | After | Reason |
|---|---|---|---|
| 1:12 | "fruit tree making fruit" | "a tree making fruit" | the Hebrew is עֵץ עֹשֶׂה פְּרִי, not עֵץ פְּרִי |
| 1:14 | "Let them be marks and meeting-times, days and years" | "Let them be for marks and meeting-times, and for days and years" | each noun has לְ |
| 1:14, 1:15 | "lamps set in" | "lamps in" | "set" is not in the Hebrew |
| 1:17 | "gave them a place in" | "set them in" | "a place" is not in the Hebrew |
| 3:22 | "knowing good and harm" | "to know good and harm" | לָדַעַת is an infinitive |
| 1:24 | "after their kind … each after its kind" | "after its kind … after its kind" | לְמִינָהּ is singular; "each" is not in the Hebrew |
| 1:28 | "every crawler that crawls" | "every beast that crawls" | the Hebrew has חַיָּה |
| 2:2–2:3 | "the work he had made"; "dropped all the work" | "his work"; "dropped away from all his work" | מְלַאכְתּוֹ and מִכָּל |
| 2:3 | "cut in the making" | "cut, to make" | the bare infinitive; Rashi and Ibn Ezra read it differently, both recorded |
| 2:11, 2:13, 2:14 | "The first: Pishon" | "The name of the first: Pishon" | שֵׁם |
| 3:10 | "I shook" | "I was afraid" | וָאִירָא |
| 3:13 | "snared" | "misled" | Rashi הִטְעַנִי, Ibn Ezra פתני |
| 3:14 | "out of all the cattle" | "above all the cattle" | Rashi reads מִן as a comparison |
| 3:23, 3:24 | "garden in Eden" | "garden of Eden" | גַן עֵדֶן is a construct, as at 2:15 |
| 3:24 | "set the cherubim" | "settled the cherubim" | וַיַּשְׁכֵּן, "caused to dwell" |
| 4:4 | "from their fat" | "and from their fat" | וּמֵחֶלְבֵהֶן |

## Owner's decision after the review

- אָדָם is "the earthling" throughout (was "the human"), so that the English word carries
  'earth' as אָדָם carries אֲדָמָה. Ibn Ezra (2:8) calls אָדָם a name hewn from the ground.
  This reverses item 27 of `review-opus-questions.md`.

- בָּרָא is "carve out" in all six uses (1:1, 1:21, 1:27 three times, 2:3, 2:4); it was
  "cut". The slicing sense is Ibn Ezra's (לגזור ולשום גבול נגזר, from Josh 17:15 and
  Ezek 23:47); "out" carries his boundary and removes the reading of "cut the earthling" as
  a wound.

## Kept against one commentator, or as a translator's decision

- 1:26, 1:28 "oppress" for רָדָה: kept by the translator's earlier decision.
  Rashi reads 'rule' and 'go down'; Ibn Ezra is silent. Open for the owner.
- 1:8 "Heavens: these waters": kept. Rashi supports the waters wordplay.
- 1:21 "sea-serpents": kept. Rashi reads "great fish"; Ibn Ezra is silent.
- 1:6 ff. "hammered plate": kept. Rashi reads a firm body; Ibn Ezra reads the air.
- 3:5 "the divine ones": Rashi "makers of worlds", Ibn Ezra "angels". Kept.
- 3:22 "live forever": Ibn Ezra reads "a long time". Kept, recorded.
- 4:7 "a lifting": Rashi reads forgiveness, Ibn Ezra the lifted face. Kept.
- 4:1 "knew": Rashi reads a pluperfect. Kept, recorded.

## Apparatus audit

- Transliteration removed from every note, apparatus entry, word gloss and name
  meaning. Hebrew is in Hebrew script, Greek in Greek script.
  `src/tool.py check` enforces this against `text/translit.txt`.
- Duplicated notes removed (for example 1:14, 2:2, 2:4, 2:17 and 2:18, where the
  same LXX reading was given twice).
- Notes that described an earlier English removed or corrected (for example 1:2
  "a waste and a void", 1:12 "heaved", 1:14 "seasons", 1:20 "flutter", 1:26
  "tread down", 2:4 "births", 3:5 "like gods", 4:1 "gotten").
- Contradictions resolved: 2:25 and 3:1 (one root or two for the bare/crafty
  pair; now: two roots, one written form); 4:7 (whether שְׂאֵת פָּנִים is in the
  verse); 3:24 (the LXX's object of "settled").
- 4:18: the LXX "Γαιδαδ καὶ Γαιδαδ ἐγέννησεν" is "Gaidad, and Gaidad fathered",
  the Hebrew pattern, and not a doubled name. The earlier note called it a
  doubling.
- The word-by-word gloss is now one thing throughout: the literal sense of the
  Hebrew unit, with a reason where the English departs from it.

## Review of these changes

An independent review pass on the Fable model ran on the 30 changed verses and on
every Rashi and Ibn Ezra entry in chapters 1–4, against the fetched Hebrew. It
found no fidelity error beyond the first item, and confirmed every LXX claim in
the changed verses. Findings and disposition:

1. 1:14 "lamps set in": "set" not in the Hebrew. Fixed, and at 1:15.
2. 4:15 "sevenfold" kept against both commentators. Fixed: "in seven generations
   vengeance will be taken".
3. 3:7 Rashi's reading (the fig is the tree they ate from) was missing. Added.
4. 2:2 Ibn Ezra misattributed: he reports and sets aside ב = 'before'. Fixed.
5. 1:28 Ibn Ezra "a blessing, not a command": unsupported; his note at 1:26 says
   it is a commandment by tradition. Fixed.
6. 4:7 Rashi points to the Targum; the content was supplied from the Targum. Fixed
   to say so.
7. 3:15 note credited Ibn Ezra with Rashi's distinction. Fixed.
8. 2:6 Ibn Ezra records, does not reject, the Gaon's reading. Fixed.
9. 4:2 Rashi: one twin with Qayin, two with Hevel. Fixed.
10. 1:14 Ibn Ezra: אֹתֹת are moments; eclipses only a possibility. Fixed.
11. 3:22 "knowing good and harm" matched a published translation over seven
    words; the Hebrew is an infinitive. Fixed: "to know good and harm".
12. 3:5 and 1:16: phrasing shared with published translations, largely forced by
    the Hebrew. Kept; low risk.

## Review of the critical apparatus

A Fable-model pass checked every reading of `text/apparatus.txt` against the fetched data
(the witnesses, the comparison-site texts, the Targums, the commentaries). It confirmed all
48 readings of section II, and that every substantive Samaritan difference found by the
collation is entered. Its findings and their disposition:

- Agreeing witnesses added: Syr and TPsJ at 1:11; Syr at 1:11 (plus) and 1:28; TSam at 2:4,
  3:6, 4:10, 4:11, 4:18; TPsJ at 2:24; Syr at 4:10, 4:11, 4:18; versions for the base
  reading at 1:7 and 1:9.
- Gᵗ cited at 1:14, where it adds 'and to rule the day and the night'.
- 2:4: a note lists every verse where G has ὁ θεός alone for יְהוָה אֱלֹהִים.
- 2:19 (TSam עורי) and 2:23 (TSam מן גברה): recorded as uncertain in notes, not as readings.
- 3:19: the note names the second עָפָר.
- Section III corrected: the 1:1 note (the versions, not every witness, read a time; BerR reads
  the Torah); Jubilees and Chagigah reworded; BerR and Rashi separated at 1:2; TN and TPsJ
  quoted separately at 1:2; Rashi's causative at 2:6; the Aramaic of 2:21 given as 'ribs,
  sides'; the Syriac of 4:7 given as ambiguous in person.
- Two objections did not stand: Symmachus at 1:2 is in the source. The reviewer did not see
  it because a parser fault had dropped it, along with other witness lines. The parser was
  fixed and all cited verses re-checked; θ′ was added at 1:2.
