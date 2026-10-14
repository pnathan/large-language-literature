# Word-level alignment of the English (translation.py) to the Hebrew witness tokens.
#
# Each verse maps to a list of entries:  (heb_idx, english, why)
#   heb_idx   tuple of 0-based indices into the verse's Hebrew tokens (see tokenise()
#             in build.py: witness-hebrew.json, split on spaces and maqqef, sof pasuq
#             and paragraph markers removed). () means the English adds a word the
#             Hebrew does not carry at that point.
#   english   the English span, as it appears in translation.py
#   why       the reason for this rendering and, where a stretch, the alternative
#             that was not taken
#
# Coverage: every Hebrew token index in a verse appears exactly once across its entries.

A = {

# ---------------- Chapter 1 ----------------

"1:1": [
 ((0,), "At the head of the head", "re'shit, construct 'head/beginning of'; the doubled 'head' keeps the construct. Alternative 'In the beginning' is the settled idiom and is avoided on purpose."),
 ((1,), "Elohim began to hack", "bara', Qal, God as subject. 'Began' is the temporal reading of the construct (see 1:1 commentary). 'Hack' is the stretch: bara' is usually rendered 'create', which is the settled sense in later usage but not an established etymology. Options considered: create (standard, abstract, hides the verb); shape (too gentle for the verb's violence); cut/carve (the root proposal). 'Hack' was chosen for force: it names the physical act the root may carry, and it does not claim the root is certain."),
 ((2,), "Elohim", "'elohim, kept as a name. Plural in form with a singular verb; the English keeps it untranslated so the reader does not hear 'God' as a settled concept."),
 ((3,), "", "'et, object marker. Left untranslated; it has no English equivalent. The emphatic 'yes' of earlier drafts is removed in this version."),
 ((4,), "the sky, the hammered bowl", "hashamayim, 'the heavens'. 'The sky' is a plain narrowing; 'the hammered bowl' pre-echoes raqia' (1:6) and is a stretch reading the sky as a worked object. Alternative: 'the heavens' (plural, settled)."),
 ((5,), "", "we'et, 'and object marker'. Second 'et is untranslated; the line break before 'the ground' carries the conjunction."),
 ((6,), "the ground, the red, the raw meat under it", "ha'arets, 'the earth/land'. 'The ground' is the narrowing to soil. 'The red' keeps adamah's root in the earth's name. 'The raw meat under it' is a stretch; nothing in 'arets says flesh. It is added for the register and is a line the commentary must justify: the earth is the body Elohim hacks into."),
],

"1:2": [
 ((0,), "The ground", "w'ha'arets, 'and the earth'. The conjunction is dropped for the sentence break; 'the ground' matches 1:1's narrowing."),
 ((1,), "was", "hayetah, 'was/became'. 'Was' is the plain copula; 'became' is possible and would shift the sense toward change."),
 ((2,), "A wasting.", "tohu, 'waste, formlessness' (cf. Deut 32:10, 'a howling waste')."),
 ((3,), "A mouth with nothing in it", "wavohu, paired with tohu. The English splits the pair: 'a waste' takes tohu; the second clause 'a mouth with nothing in it' takes bohu. Stretch: bohu has no settled meaning beyond 'emptiness', so the concrete image is added and marked."),
 ((4,), "Dark", "w'choshekh, 'and darkness'. 'Dark' as the noun-used-as-subject is a register compression."),
 ((5,), "coiled on the lip of", "'al, 'upon'. 'Coiled on the lip of' is a stretch of 'al: the preposition is spatial and plain; the verb 'coiled' adds the bodily image."),
 ((6,7), "the Deep", "p'nei tehom, 'face of the deep'. 'Face' is rendered 'lip' (p'nei). Stretch: 'lip' for panim is a choice to make the deep bodily; 'face of the deep' is the literal. Tehom (7) is 'the Deep', capitalised as a force."),
 ((8,9), "and the Wind of Elohim", "w'ruach 'elohim, 'and the breath/spirit/wind of God'. 'Wind' is chosen over 'spirit' (ruach's standard translation) and over 'breath', which is the subject of 1:2 in later drafts. 'Wind' keeps the physical movement the verb needs."),
 ((10,), "a bird that flutters over its young", "merachefet, 'hovering/brooding'. The English gives the simile 'a bird' as a stretch from the root (Deut 32:11 uses the same root of an eagle over its young). 'Brooding' is the fitting verb of that bird."),
 ((11,12,13), "beat over the belly of the waters", "'al p'nei hamayim, 'upon the face of the waters'. 'Beat' is the stretch of merachefet's trembling; 'belly' replaces 'face' (see 1:2 commentary on pnei). The second pnei is folded into 'belly' for the parallel."),
],

"1:3": [
 ((0,1), "He howled", "wayomer 'elohim, 'and God said'. 'Howled' replaces 'said': the verb is plain speech, so this is the largest single register stretch in 1:3. Alternative 'said' is accurate and flat; 'howled' is chosen for force, and the commentary says so."),
 ((2,), "Be,", "yehi, 'let it be' (jussive). 'Be' is the imperative stripped of 'let'; the subject follows."),
 ((3,), "light!", "'or, 'light'. Exclamatory placement, the noun as a shout."),
 ((4,), "And light", "wayehi 'or, 'and light became/was'. 'Light' as subject; the verb is folded into the next clause."),
 ((5,), "And light tore out of the dark, a birth-cry, wet.", "wayehi 'or (second half). 'Came' keeps hayah's 'becoming'. 'Tearing up out of the dark' is added: nothing in the Hebrew says 'out of the dark' here (the dark appears in 1:2 and 1:4). 'A birth-cry, wet' is a register addition, marked as such."),
],

"1:4": [
 ((0,), "Elohim saw", "wayar' 'elohim, 'and God saw'. 'Saw' is the plain verb."),
 ((1,), "", "'elohim, repeated subject; the English drops it into the first clause."),
 ((2,), "", "'et, object marker, untranslated."),
 ((3,), "the light", "ha'or, 'the light'."),
 ((4,), ":", "ki, 'that/because', introduces the judgment; the colon is the English's way to keep the content clause."),
 ((5,), "good", "tov, 'good'. Fitness rather than virtue; LXX kalon ('beautiful') is a different register."),
 ((6,), "He drove a gash", "wayavdel, 'and he separated'. 'Drove a gash' is the register's word for badal, a physical separation. Alternative 'separated' is accurate and tame; the gash is the bodily image."),
 ((7,), "", "'elohim, repeated subject."),
 ((8,), "between", "bein, 'between'."),
 ((9,), "the light", "ha'or."),
 ((10,), "and", "uvein, 'and between'."),
 ((11,), "the dark", "hachoshekh, 'the darkness'. 'Dark' keeps the noun short, matching 1:2's use."),
 ((), "The wet flesh of it, good.", "Not in the Hebrew. The repeated 'good' with 'the wet flesh of it' is a register addition: it makes tov a bodily judgment. Marked as an addition; the commentary on 1:4 names it."),
],

"1:5": [
 ((0,1), "He named the light Day", "wayiqra' 'elohim la'or yom, 'and God called the light day'. 'Named' for qara' ('call, name'); the English prefers the naming sense because the Hebrew uses qara' with an object in the sense of naming."),
 ((2,), "", "paseq (׀), a cantillation mark; no English."),
 ((3,), "", "la'or, 'to the light'; the preposition is absorbed in 'the light'."),
 ((4,), "Day", "yom, 'day'. Capitalised as the name the light is given."),
 ((5,6,7), "The dark, he named Night.", "walachoshekh qara' laylah, 'and the darkness he called night'. 'The dark' replaces 'the darkness' as in 1:4; 'he named' repeats the verb."),
 ((8,9), "Evening clotted.", "wayehi 'erev, 'and it was evening'. 'Clotted' is the stretch: 'erev is 'evening' (from a root some link to mixing). 'Clotted' presses the mixing sense bodily. Alternative 'Evening came' is plain."),
 ((10,11), "Morning broke open.", "wayehi boqer, 'and it was morning'. 'Broke open' is the stretch of boqer, a root sometimes linked to splitting; the link is disputed."),
 ((12,13), "One day.", "yom echad, 'one day'. Cardinal, not 'first'."),
],

"1:6": [
 ((0,1), "He said:", "wayomer 'elohim, 'and God said'. 'He said' is the plain verb; the register stays low here, unlike 1:3."),
 ((2,), "beat out", "yehi, 'let be'. 'Beat out' is an addition that carries the verb's meaning forward into rāqia': the English reads the object before the Hebrew names it. Stretch: the verb is 'let there be'."),
 ((3,), "a plate, a skin of hammered stuff,", "raqia', from raqa', 'to beat out, spread thin'. 'Plate' and 'skin' are two renderings of the same object: 'skin' keeps the bodily, 'plate' the metal. 'Firmament' (the usual rendering from Latin) drops the hammering and is rejected."),
 ((4,5), "in the belly of the waters:", "betokh hamayim, 'in the midst of the waters'. 'Belly' replaces 'midst' (betokh): the stretch makes the waters a body. Alternative 'midst' is accurate and tame."),
 ((6,7), "a wall, a splitter—", "wihi mavdil, 'and let it be a separator'. 'A wall' is an addition: mavdil is 'separator', and stereōma (LXX) means 'firm thing', not wall. Marked."),
 ((8,9,10), "water from water.", "bein mayim lamayim, 'between water and water'. 'Water from water' compresses the preposition lamayim into a stammered pair; the Hebrew's 'to the waters' is grammatically odd and is kept as a stammer."),
],

"1:7": [
 ((0,), "Elohim beat the skin out.", "wayya'as 'elohim, 'and God made'. The verb changes here from bara' (1:1, 1:21) to 'asah, the plain 'make'. The English says 'beat the skin out', which turns 'asah into the working of raqia'. Alternative 'made the skin' is accurate and flat."),
 ((1,), "", "'elohim, repeated subject, dropped."),
 ((2,), "", "'et, object marker."),
 ((3,), "", "haraqia', 'the skin/plate'. Already named in 1:6; 'the skin' appears in the verb phrase."),
 ((4,5), "He split the waters:", "wayavdel bein hamayim, 'and he separated between the waters'. 'Split' for badal (see 1:4 'cut a seam'); the English uses 'split' here as the verb for the same act."),
 ((6,), "", "hamayim, 'the waters' (first). Carried by 'the waters'."),
 ((7,), "some under it,", "'asher mit-tachat laraqia', 'which were beneath the skin'. 'Some under it' is the English's relative-clause compression."),
 ((8,9), "", "mit-tachat laraqia, 'from beneath the skin'. Carried in the phrase above."),
 ((10,), "", "uvein, 'and between'. Carried by 'some over it'."),
 ((11,), "some over it.", "hamayim, 'the waters' (second). 'Over it' carries 'asher me'al laraqia, 'which were above the skin'."),
 ((12,13,14), "", "'asher me'al laraqia, 'which were above the skin'. Carried above."),
 ((15,16), "So. It held.", "wayehi-ken, 'and it became so'. 'It held' is a stretch: ken is 'thus, so'. The English adds the sense of the skin holding its place, which the commentary names as an addition."),
],

"1:8": [
 ((0,1), "He named the skin Sky", "wayiqra' 'elohim larraqia' shamayim, 'and God called the skin heavens'. 'Sky' narrows shamayim; the plural is lost. Alternative 'Heavens' keeps the plural and is more faithful."),
 ((2,3), "sham-mayim, there are waters.", "shamayim, folk-etymologised by the English. Not in the Hebrew text itself. Added as a sound-play; marked in the commentary as not an established derivation."),
 ((4,), "Evening.", "wayehi 'erev, 'and it was evening'. 'Evening' alone, the formula compressed."),
 ((5,), "", "'erev, repeated, carried above."),
 ((6,), "Morning.", "wayehi boqer, 'and it was morning'."),
 ((7,), "", "boqer, carried above."),
 ((8,9), "The second day.", "yom sheni, 'day second'. Ordinal."),
],

"1:9": [
 ((0,1), "He said: gather, waters,", "wayomer 'elohim, 'and God said'; yiqqavu hamayim, 'let the waters be gathered'. 'Gather' is the English for qavah's gathering sense; the imperative is kept with the 'let' removed for force."),
 ((2,), "", "yiqqavu, 'let them gather/wait', carried in 'gather'."),
 ((3,4), "", "hamayim mittachat hashamayim, 'the waters from beneath the heavens'. Carried by 'waters' above; 'beneath the heavens' is not rendered in this line (a loss marked in the commentary)."),
 ((5,), "", "hashamayim, 'the heavens'. Not rendered; loss marked."),
 ((6,7), "into one pit,", "'el-maqom 'echad, 'to one place'. 'Pit' is a stretch: maqom is 'place'; 'pit' presses the bodily hollow. Alternative 'one place' is plain."),
 ((8,), "", "'echad, 'one', carried by 'one'."),
 ((9,), "", "wetera'eh, 'and let be seen'. Carried by 'Let the dry tear up, bare'."),
 ((10,), "one waiting-place.", "hayabbashah, 'the dry'. 'One waiting-place' is not in this verse as a noun: it renders the second clause's hope sense (qavah) and is an addition; the Hebrew says 'let the dry be seen'. Marked."),
 ((11,12), "So. It held.", "wayehi-ken, 'and it became so'."),
],

"1:10": [
 ((0,1), "He named the dry Earth.", "wayiqra' 'elohim, 'and God called'. 'Earth' is for 'eretz; the naming is 'called' in the Hebrew."),
 ((2,), "", "paseq (׀), a cantillation mark; no English."),
 ((3,), "the dry", "layabbashah, 'to the dry'. 'The dry' is the Hebrew's noun; the English keeps it bare."),
 ((4,), "Earth", "'eretz, 'earth/land'. 'Earth' capitalised as the name it becomes."),
 ((5,6), "The pooling, the waiting-hollow,", "ulmiqveh hamayim, 'and to the gathering of the waters'. 'Pooling' and 'waiting-hollow' are two English renderings of miqveh (gathering, pool; the root of hope). Both are kept because the root carries both."),
 ((7,), "", "qara', 'he called', carried by 'he named'."),
 ((8,), "Seas.", "yammim, 'seas', plural. Capitalised as the name."),
 ((9,10), "He saw:", "wayar' 'elohim, 'and God saw'."),
 ((11,12), "good.", "ki tov, 'that good'. 'Good' is tov (see 1:4)."),
],

"1:11": [
 ((0,1), "He said: let the ground green-burst a greening—", "wayomer 'elohim tadshe' ha'arets deshe', 'and God said: let the earth sprout sprouting'. 'Green-burst' is a stretch: dasha' is 'sprout', 'green' is the adjectival sense of deshe'. 'A greening' keeps the cognate accusative. The compound 'green-burst' is the register's addition; the commentary names it."),
 ((2,3,4), "", "tadshe' ha'arets deshe', 'let the earth sprout sprouting'. Carried above."),
 ((5,), "grass spitting seed,", "'eseb mazri'a zera', 'herb seeding seed'. 'Grass' is a narrowing of 'eseb ('herb, plant'); 'spitting' is the stretch of mazri'a, 'bearing/sowing seed'. Alternative 'seeding' is accurate and tame."),
 ((6,7), "", "mazri'a zera', carried above."),
 ((8,9,10), "fruit-wood making fruit after its kind,", "'ets peri 'oseh peri, 'fruit tree making fruit'. 'Fruit-wood' compresses 'ets ('tree') into a material noun, an intentional stretch."),
 ((11,12), "after its kind,", "lemino, 'after its kind'. 'Its kind' is min, species."),
 ((13,14,15), "seed in its own body,", "'asher zar'o bo, 'whose seed is in it'. 'Its own body' stretches bo ('in it') into the bodily; the Hebrew says 'in it' only."),
 ((16,17), "on the ground.", "'al ha'arets, 'upon the earth'. 'Ground' keeps the earth as soil."),
 ((18,19), "So. It held.", "wayehi-ken, 'and it became so'. 'It held' is the addition named in 1:7."),
],

"1:12": [
 ((0,), "The ground heaved and pushed up", "wattotse' ha'arets, 'and the earth brought out'. 'Heaved and pushed up' replaces 'brought out': the verb is bare, and the English adds the bodily labour. Alternative 'brought forth' is the LXX/standard and is tamer."),
 ((1,), "", "ha'arets, carried above."),
 ((2,3), "a greening: grass", "deshe' 'eseb, 'sprouting, herb'. Carried as in 1:11."),
 ((4,5), "spitting seed", "mazri'a zera'. Carried as in 1:11."),
 ((6,), "after its kind,", "lemino."),
 ((7,), "", "we'ets, 'and tree'. 'Fruit-wood' above renders 'ets with 'oseh peri."),
 ((8,9), "fruit-wood making fruit,", "'oseh peri, 'making fruit'."),
 ((10,11,12), "seed in its body,", "'asher zar'o bo. Carried as in 1:11."),
 ((13,), "after its kind.", "lemineihu."),
 ((14,15), "Elohim saw:", "wayar' 'elohim."),
 ((16,17), "good.", "ki tov."),
],

"1:13": [
 ((0,1), "Evening.", "wayehi 'erev, 'and it was evening'. Formula compressed to its noun."),
 ((2,3), "Morning.", "wayehi boqer, 'and it was morning'. Formula compressed."),
 ((4,5), "The third day.", "yom shelishi, 'day third'. Ordinal."),
],

"1:14": [
 ((0,1,2), "He said: let there be", "wayomer 'elohim yehi, 'and God said: let be'. 'Let there be' is the plain English of yehi; the register stays low here."),
 ((3,), "fire-holders", "me'orot, from 'or (light, fire). 'Fire-holders' is a compound coined for the Hebrew's sense of light-bearers. Alternatives: 'lights' (settled, but loses the fire), 'luminaries' (Latinate, the LXX's phōstēres). The compound keeps the root's fire."),
 ((4,5), "in the hammered sky,", "birqia' hashamayim, 'in the firmament of the heavens'. 'Hammered' keeps raqia's beaten sense (see 1:6)."),
 ((6,7,8,9,10), "cleaving day from night.", "lehavdil bein hayom uvein halaylah, 'to separate between the day and between the night'. 'Cleaving' is the register's word for badal (see 1:4 'drove a gash'); the English drops the 'between' repetition."),
 ((11,), "Let them be", "vehayu, 'and let them be'. Carried by the next line's 'Let them be'."),
 ((12,), "marks", "le'otot, 'for signs'. 'Signs' is the settled sense of 'ot (mark, sign)."),
 ((13,), "marks for the turns of the year,", "ulemo'adim, 'and for appointed times'. 'Tellers of times' stretches mo'ed: the appointed time is read as something that tells. Alternative 'seasons' is settled and tame."),
 ((14,15), "meeting-hours, days, years.", "uleyamim veshanim, 'and for days and years'. 'Meeting-hours' is the stretch of mo'ed (from ya'ad, 'to meet at an appointed place') and is kept as a second reading of 'meeting'."),
],

"1:15": [
 ((0,1), "Let them be fire-holders in the sky,", "vehayu limme'orot birqia' hashamayim, 'and let them be lights in the firmament of the heavens'. Repeats 1:14's 'fire-holders'; 'in the sky' narrows the firmament (see 1:6)."),
 ((2,3), "", "birqia' hashamayim, carried above."),
 ((4,5,6), "to pour light on the ground.", "lehe'ir 'al ha'arets, 'to give light upon the earth'. 'Pour' is the stretch of he'ir, the causative of 'or; alternative 'to give light' is plain."),
 ((7,8), "So.", "wayehi-ken, 'and it became so'. The shortest form of the formula; 'So.' keeps ken's deictic."),
],

"1:16": [
 ((0,1), "Elohim made the two great fires:", "wayya'as 'elohim et shenei hamme'orot hagedolim, 'and God made the two great lights'. 'Fires' is the stretch of me'orot (see 1:14). 'Made' keeps 'asah (plain 'make')."),
 ((2,), "", "'et, object marker."),
 ((3,4,5), "", "shenei hamme'orot hagedolim, 'the two great lights'. Carried above; 'two' and 'great' are the Hebrew's, 'great' and 'lesser' appear again below."),
 ((6,), "", "'et, object marker."),
 ((7,8), "the greater to rule the day,", "hamaor hagadol lememshelet hayom, 'the greater light for the dominion of the day'. 'Rule' is mashal's root (see 1:18)."),
 ((9,10), "", "lememshelet hayom, carried above."),
 ((11,), "", "ve'et, 'and the'. Carried by 'the lesser'."),
 ((12,13), "the lesser to rule the night,", "hamaor hakaton lememshelet halaylah, 'the lesser light for the dominion of the night'. 'Lesser' is the Hebrew's 'small/lesser'."),
 ((14,15), "", "lememshelet halaylah, carried above."),
 ((16,17), "and the stars.", "ve'et hakokhavim, 'and the stars'. 'Stars' is the settled sense of kokhavim."),
],

"1:17": [
 ((0,1,2), "He hung them", "wayyiten otam 'elohim, 'and God gave them'. 'Hung' is the register's stretch for nathan (give, set). It makes the lamps objects placed by a hand. Alternative 'set' is plain and common."),
 ((3,4), "in the hammered sky", "birqia' hashamayim, carried as in 1:14."),
 ((5,6,7), "to pour light on the ground.", "lehe'ir 'al ha'arets. Carried as in 1:15."),
],

"1:18": [
 ((0,1,2,3), "to rule the day and the night,", "velimshol bayom uvalaylah ulehavdil, 'and to rule in the day and in the night and to separate'. 'Rule' keeps mashal. The English omits 'in' and joins 'the day and the night'."),
 ((4,5), "to cut the seam between light and dark.", "bein ha'or uvein hachoshekh, 'between the light and between the darkness'. 'Cut the seam' is the register's badal (see 1:4). The English folds the repeated 'between' into the seam."),
 ((6,7), "", "uvein hachoshekh, carried above."),
 ((8,9,10,11), "Elohim saw: good.", "wayar' 'elohim ki tov. Formula, as in 1:4 and 1:10."),
],

"1:19": [
 ((0,1), "Evening.", "wayehi 'erev."),
 ((2,3), "Morning.", "wayehi boqer."),
 ((4,5), "The fourth day.", "yom revi'i, 'day fourth'."),
],

"1:20": [
 ((0,1), "He said:", "wayomer 'elohim, 'and God said'."),
 ((2,3,4), "let the waters seethe with a swarming of breathing things;", "yishretzu hamayim sherets nefesh chayah, 'let the waters swarm with swarm of living breath'. 'Seethe' is the stretch of sharats (to swarm, teem). 'A swarming of breathing things' is the English's sherets nefesh chayah: the Hebrew's noun 'swarm' is kept, and 'breathing things' renders nefesh chayah (see 1:20 commentary)."),
 ((5,6), "", "nefesh chayah, carried above."),
 ((7,8), "and let fliers flutter", "veof yeofef, 'and bird flying'. 'Fliers flutter' keeps the doubled verb (ye'opef, 'fly-flying'). 'Fliers' is the noun, 'flutter' the verb."),
 ((9,10), "over the ground,", "'al ha'arets 'al penei rqia' hashamayim, 'upon the earth, upon the face of the firmament of the heavens'. 'Across' is the English's compression of 'al ('upon'); 'the face of the hammered sky' keeps the raqia' stretch. 'Across' is a stretch: 'upon' is the Hebrew's spatial preposition."),
 ((11,12,13,14), "across the face of the hammered sky.", "al penei rqia' hashamayim, 'upon the face of the firmament of the heavens'. 'Across' stretches 'al ('upon')."),
],

"1:21": [
 ((0,1), "Elohim made the great serpents of the deep, the tanninim,", "wayivra' 'elohim et hattanninim hagedolim, 'and God created the great sea-monsters'. The verb is bara' here, not 'asah: 'made' is the English for bara' in this line, and the choice is deliberate, since the chaos-monsters are made, not slain (commentary on 1:21). 'Serpents of the deep' is an addition that places the tanninim in the Deep of 1:2."),
 ((2,), "", "'et, object marker."),
 ((3,4), "", "hattanninim hagedolim, carried above; 'the tanninim' is kept as the Hebrew word."),
 ((5,6,7,8), "and every breathing swarm the waters bred, after its kind,", "ve'et kol nefesh hachayah harommeset asher sharetzu hamayim lemineihem, 'and every living breath that creeps which the waters swarmed, after their kinds'. 'Breathing swarm' is the stretch of nefesh hachayah harommeset; 'bred' is the stretch of sharetzu (teemed). 'Every' keeps kol."),
 ((9,), "", "paseq (׀), a cantillation mark; no English."),
 ((10,11,12,13,14), "", "harommeset asher sharetzu hamayim lemineihem, carried above."),
 ((15,16,17,18,19), "and every winged fowl, after its kind.", "ve'et kol of kanaf lemineihu, 'and every winged bird, after its kind'. 'Fowl' is the register's word for of (bird); 'winged' carries kanaf."),
 ((20,21,22,23), "He saw: good.", "wayar' 'elohim ki tov. Formula."),
],

"1:22": [
 ((0,1,2,3), "He blessed them:", "wayevarekh otam 'elohim lemor, 'and God blessed them, saying'. 'Saying' is dropped; the colon marks the speech."),
 ((4,), "Burst!", "peru, from parah, 'break out, bear fruit'. 'Burst' is the stretch: parah is fruitfulness, and 'burst' keeps the force of fruit breaking out. Alternative 'be fruitful' is the standard and is tamer."),
 ((5,), "Swarm!", "urevu, from rabah, 'become many, a crowd'. 'Swarm' is the stretch of 'be many'."),
 ((6,7,8,9), "Fill the seas!", "umil'u et hamayim bayyammim, 'and fill the waters in the seas'. 'Seas' carries bayyammim; 'the waters' is dropped as a repeat of 'seas'. Loss marked."),
 ((10,11,12), "Let the fliers breed on the earth.", "vehaof yirev ba'arets, 'and the bird let it multiply on the earth'. 'Breed' is the stretch of yirev (multiply); 'fliers' is the Hebrew's 'bird' (of, 'fowl') in the plural frame."),
],

"1:23": [
 ((0,1), "Evening.", "wayehi 'erev."),
 ((2,3), "Morning.", "wayehi boqer."),
 ((4,5), "The fifth day.", "yom chamishi, 'day fifth'."),
],

"1:24": [
 ((0,1), "He said:", "wayomer 'elohim."),
 ((2,3), "let the ground belch out", "totse' ha'arets, 'let the earth bring out'. 'Belch out' is the register's stretch of yatsa' (bring out); 'belch' gives a bodily verb to the ground. Alternative 'bring forth' is the standard."),
 ((4,5,6), "breathing things after their kind:", "nefesh chayah lemino, 'living breath after its kind'. 'Breathing things' is the English for nefesh chayah (see 1:20)."),
 ((7,), "cattle,", "behemah, 'cattle, beast'. 'Cattle' is the settled sense."),
 ((8,), "crawlers,", "remes, 'creeping thing'. 'Crawlers' is the plain English."),
 ((9,10), "beasts of the ground,", "chayat ha'arets, 'beasts of the earth'. Carried by 'beasts of the ground'."),
 ((11,), "each after its kind.", "lemineha, 'after its kind'. Formula."),
 ((12,13), "So. It held.", "wayehi-ken. The addition 'It held' is named at 1:7."),
],

"1:25": [
 ((0,1), "Elohim made", "wayya'as 'elohim, 'and God made'."),
 ((2,3,4,5), "the beast of the ground after its kind,", "et chayat ha'arets lemina, 'the beast of the earth after its kind'. Singular 'beast' against the plural 'beasts' of 1:24; the Hebrew's chayat is singular."),
 ((6,7,8), "the cattle after its kind,", "ve'et habehemah lemina, 'and the cattle after its kind'."),
 ((9,10,11,12,13), "every crawler of the red after its kind.", "ve'et kol remes ha'adamah lemineihu, 'and every crawler of the red after its kind'. 'The red' is adamah; this is the first use of the 'red' in the English as the earth's name."),
 ((14,15), "He saw:", "wayar' 'elohim."),
 ((16,17), "good.", "ki tov."),
],

"1:26": [
 ((0,1), "He said:", "wayomer 'elohim."),
 ((2,), "we will make", "na'aseh, 'let us make' (first person plural). 'We will make' is the future reading; the cohortative 'let us' is kept in commentary."),
 ((3,), "the human, the red one,", "'adam, 'human'. 'The red one' is the stretch: 'adam is built on adamah, the red soil (2:7). The English makes the pun by a compound."),
 ((4,), "in our image,", "betsalmenu, 'in our image'."),
 ((5,), "after our likeness.", "kidmuteinu, 'as our likeness'. 'After' for the Hebrew's 'ki-' (like, as)."),
 ((6,), "Let them tread down", "viyrdu, 'and let them tread down/rule'. 'Tread down' is the stretch of radah (trample, rule)."),
 ((7,8), "the fish of the sea,", "bidgat hayam, 'the fish of the sea'."),
 ((9,10), "the fowl of the sky,", "uve'of hashamayim, 'and the fowl of the sky'."),
 ((11,), "the cattle,", "uvabehemah, 'and in the cattle'."),
 ((12,13), "the whole ground,", "uvechol ha'arets, 'and in all the earth'. 'The whole' carries kol."),
 ((14,15,16,17,18), "every crawler that crawls.", "uvechol haremes harome's al ha'arets. 'On the ground' is dropped; loss marked."),
],

"1:27": [
 ((0,1), "Elohim gouged", "wayivra' 'elohim, 'and God created'. 'Gouged' replaces 'created' (bara'). Choice: 'created' is the settled sense; 'hack' (1:1) and 'gouged' (here) are stretches of the same verb. The reader loses the root's repetition; the commentary names that loss."),
 ((2,), "", "paseq (׀), a cantillation mark; no English."),
 ((3,4), "the human", "'et ha'adam, 'the human'. The 'et is not rendered."),
 ((), "out of the red", "Not in 1:27. The Hebrew says 'the human' only. 'Out of the red' links the human to adamah (1:25, 2:7), and is an addition marked for the pun."),
 ((5,), "into a shadow of himself—", "betsalmo, 'in his image'. 'A shadow' is the stretch of tselem (shade, image); 'of himself' resolves the pronoun to the human. Alternative 'in his image' is the standard."),
 ((6,7), "into the shadow of Elohim", "betselem 'elohim, 'in the image of God'. Same stretch."),
 ((8,9), "he gouged him—", "bara' oto, 'he created him'. Third use of bara' in the verse; 'gouged' keeps the striking."),
 ((10,11), "male and female", "zakhar uneqevah, 'male and female'."),
 ((12,13), "he gouged them.", "bara' otam, 'he created them'."),
],

"1:28": [
 ((0,1,2), "He blessed them.", "wayevarekh otam 'elohim. Formula."),
 ((3,4,5), "He said:", "wayomer lahem 'elohim, 'and God said to them'."),
 ((6,), "Burst,", "peru, as at 1:22."),
 ((7,), "swarm,", "urevu, as at 1:22."),
 ((8,), "fill", "umil'u, 'and fill'."),
 ((9,10), "the earth;", "'et ha'arets, 'the earth'."),
 ((11,), "trample it", "vechivshuha, 'and subdue it'. 'Trample' is the stretch of kavash (subdue)."),
 ((), "like cloth in the washing-pit;", "Not in the verse. The image is from kavas, a related root meaning to press and beat cloth. It is a stretch: kavash and kavas are different verbs. Marked as an addition the commentary states."),
 ((12,13,14), "tread the fish,", "uredu bidgat hayam, 'and tread the fish of the sea'. Radah again; 'the fish' carries bidgat hayam."),
 ((15,16), "the fowl,", "uveof hashamayim, 'and the fowl of the sky'."),
 ((17,18,19,20,21), "every crawler that crawls on the ground.", "uvechol chayah harmeshet al ha'arets, 'and in every living thing that creeps on the earth'. 'Living thing' is dropped in favour of 'crawler'."),
],

"1:29": [
 ((0,1), "He said:", "wayomer 'elohim."),
 ((2,), "Look—", "hinneh, 'look, behold'. Exclamation kept."),
 ((3,), "I have handed you", "natati, 'I have given'. 'Handed' is the physical register of nathan; the perfect is kept as 'have'."),
 ((4,), "", "lakhem, 'to you'. Carried by 'you'."),
 ((5,6,7,8), "every seed-spitting herb", "'et kol 'esev, 'every herb'. 'Seed-spitting' is the addition from zorea' zera' (seed-sowing, 1:11)."),
 ((9,10), "", "zorea' zera', 'sowing seed', carried above."),
 ((11,12,13,14,15), "over the whole face of the ground,", "asher 'al penei kol ha'arets, 'which is upon the face of all the earth'. 'Whole' carries kol."),
 ((16,17,18), "and every fruit-wood", "ve'et kol ha'ets, 'and every tree'. 'Fruit-wood' carries 'ets (see 1:11)."),
 ((19,20,21,22,23,24), "that holds seed-fruit in itself.", "asher bo peri 'ets zorea' zara', 'which in it is fruit of tree sowing seed'. 'Holds in itself' is the stretch of bo."),
 ((25,26,27), "For you: to eat.", "lakhem yihyeh le'okhlah, 'to you it shall be for food'. 'Eat' is the stretch of 'okhlah (food); 'for you' carries lakhem."),
],

"1:30": [
 ((0,1,2), "And for every beast of the ground,", "ulekhol chayat ha'arets, 'and to every beast of the earth'. 'And for' carries the Hebrew lamed."),
 ((3,4), "every fowl of the sky,", "ulekhol of hashamayim, 'and to every fowl of the sky'."),
 ((5,6,7,8,9,10), "every crawler with breath in it:", "ulekhol romes 'al ha'arets 'asher bo nefesh chayah. 'With breath in it' is nefesh chayah in bo (see 1:20)."),
 ((11,12,13,14), "", "asher bo nefesh chayah, carried above."),
 ((15,16,17,18,19), "all the green grass, to eat.", "'et kol yerek 'esev le'okhlah, 'all green herb for food'. 'Green grass' compresses yereq 'esev."),
 ((20,21), "So. It held.", "wayehi-ken. Addition named at 1:7."),
],

"1:31": [
 ((0,1), "Elohim saw all he had made—", "wayar' 'elohim et kol asher 'asah, 'and God saw all that he had made'. 'All he had made' is the plain sense of kol asher 'asah."),
 ((2,3,4,5), "", "'et kol asher 'asah, carried above."),
 ((6,7), "and look: good,", "vehinneh tov, 'and look: good'. 'And look' keeps hinneh."),
 ((8,), "very good.", "me'od, 'exceedingly'. 'Very' is the plain English; 'exceedingly' was rejected as too archaic for this line."),
 ((9,10,11,12), "Evening. Morning:", "wayehi 'erev wayehi boqer."),
 ((13,14), "the sixth day.", "yom hashishi, 'day sixth'."),
],

"2:1": [
 ((0,1,2), "So sky and ground were finished,", "vayekhullu hashamayim vehaaretz: 'and the heavens and the earth were finished'. 'So' bridges from 1:31."),
 ((3,4), "and all their muster.", "vekhol tz'vaam: 'and all their host'. 'Muster' is the physical stretch of tz'va (host, army)."),
],
"2:2": [
 ((0,1,2,3), "Elohim finished on the seventh day", "vayekhal elohim bayom hashevi'i: 'God finished on the seventh day'. The LXX reads 'sixth day' here (witness variant)."),
 ((4,5,6), "the work he had made;", "melakhto asher 'asah: 'his work that he had made'."),
 ((7,8,9), "and on the seventh day he quit", "vayishbot bayom hashevi'i: 'and he ceased on the seventh day'. 'Quit' is the physical stretch of shavat (put the tool down)."),
 ((10,11,12,13), "from all the work he had made.", "mikol melakhto asher 'asah: 'from all his work that he had made'."),
],
"2:3": [
 ((0,1,2,3,4), "He knelt in blessing toward the seventh day,", "vayevarekh elohim et yom hashevi'i: 'God blessed the seventh day'. 'Knelt' is the physical stretch of barak (the knee link is disputed)."),
 ((5,6), "cut it out, set it apart,", "vayqaddesh oto: 'and set it apart'. 'Cut it out' is the bodily stretch of qadosh; the 'cut away' gloss is speculative."),
 ((7,8,9), "because on it he laid down", "ki bo shavat: 'because in it he ceased'. 'Laid down' is the English for shavat, a different verb from 2:2's 'quit'; the repetition is lost."),
 ((10,11,12,13,14,15), "from all the work Elohim cut to make.", "mikol melakhto asher bara' elohim la'asot: 'from all his work which God created to make'. 'Cut to make' keeps the doubled verb; the LXX reads 'began to make' (ērxato)."),
],
"2:4": [
 ((0,), "These are the births—", "'elleh: 'these are'. 'Births' is the physical English for toledot's bearing."),
 ((1,), "toledot, the bearing-out—", "toledot: the Hebrew word kept visible, with 'bearing-out' as the English gloss for its sense of what comes forth."),
 ((2,3), "of sky and ground,", "hashamayim vehaaretz: 'the heavens and the earth'."),
 ((4,), "in their being cut,", "behibare'am: 'in their being created'. 'Cut' is the physical stretch of bara' (1:1)."),
 ((5,6,7,8), "in the day YHWH Elohim made", "beyom 'asot YHWH elohim: 'in the day YHWH God made'."),
 ((9,10), "ground and sky.", "'eretz veshamayim: 'earth and heavens'. The English reverses the order: the chiasm of the verse."),
],
"2:5": [
 ((0,1,2,3,4,5,6), "No thorn-bush of the field yet on the ground,", "vekhol siach hasadeh terem yihyeh ba'arets: 'and every bush of the field not yet on the earth'. 'Thorn-bush' is the physical stretch of siach."),
 ((7,8,9,10,11), "no grass of the field yet sprung.", "vekhol esev hasadeh terem yitzmach: 'and every herb of the field not yet sprung'."),
 ((12,13,14,15,16,17,18), "YHWH Elohim had not rained on the ground,", "ki lo himtir YHWH elohim al ha'arets: 'for YHWH God had not rained upon the earth'."),
 ((19,20,21,22,23), "and there was no human to work the red.", "veadam ayin la'avod et ha'adamah: 'and no human to work the ground'. 'Red' is the English for adamah (see 1:25)."),
],
"2:6": [
 ((0,1,2,3), "A seep rose out of the earth", "ved ya'aleh min ha'arets: 'and a seep rose out of the earth'. 'Seep' is the physical choice for ed (mist, flow, spring)."),
 ((4,5,6,7,8), "and drenched the whole face of the red.", "vehishkah et kol penei ha'adamah: 'and it drenched all the face of the ground'."),
],
"2:7": [
 ((0,1,2,3,4,5,6,7), "YHWH Elohim potted the human from dust of the ground—afar—", "wayyitzer YHWH elohim et ha'adam afar min ha'adamah: 'YHWH God potted the human, dust from the ground'. 'Potted' is the physical stretch of yatzar (form, as a potter forms clay); 'afar' kept as the echo."),
 ((8,9,10,11), "and blew into his nostrils breath of lives;", "vayippach be'appav nishmat chayyim: 'and breathed into his nostrils breath of lives'. 'Blew' is the physical stretch of nafach; 'nostrils' is the literal of appayim."),
 ((12,13,14,15), "and the human became a living throat.", "vayehi ha'adam lenefesh chayah: 'and the human became a living breath'. 'Throat' is the physical stretch of nefesh (see 1:20)."),
],
"2:8": [
 ((0,1,2,3,4), "YHWH Elohim planted a garden of delight,", "wayyitta YHWH elohim gan be'eden: 'YHWH God planted a garden in Eden'. 'Delight' is the English reading of Eden."),
 ((5,), "from the front, from of old, eastward,", "miqqedem: 'from before, from of old, eastward'. Three glosses kept in one line; the Hebrew holds them together (2:8 commentary)."),
 ((6,7,8,9,10,11), "and set there the human he had shaped.", "wayyasem sham et ha'adam asher yatzar: 'and set there the human he had potted'. Yatzar is the potter's verb (see 2:7)."),
],
"2:9": [
 ((0,1,2,3,4,5,6,7,8), "From the red he made spring every tree to covet with the eyes,", "wayyatzmach YHWH elohim min ha'adamah kol ets nekhmad lemar'eh: 'YHWH God made spring from the ground every tree desirable to see'. 'Covet' is the physical stretch of chamad."),
 ((9,10), "sweet to the mouth;", "vetov lema'akhal: 'and good for food'. 'Sweet' and 'mouth' are the physical stretch of tov and eating."),
 ((11,12,13,14), "the tree of lives at the garden's heart,", "ve'ets hachayyim betokh hagan: 'and the tree of lives in the middle of the garden'. 'Heart' is the physical stretch of betokh (midst)."),
 ((15,16,17,18), "and the tree of knowing good and harm.", "ve'ets hada'at tov vara': 'and the tree of knowing good and harm'. 'Harm' carries ra' (ruin as well as evil)."),
],
"2:10": [
 ((0,1,2,3,4,5), "A river came out of delight to water the garden;", "venahar yotze me'eden lehashqot et hagan: 'a river went out from Eden to water the garden'."),
 ((6,7), "from there it split", "umisham yipared: 'and from there it divides'. 'Split' is the physical stretch of parad."),
 ((8,9,10), "and became four heads.", "vehayah le'arba'ah rashim: 'and it became four heads'. 'Heads' keeps rosh (head, source)."),
],
"2:11": [
 ((0,1,2), "The first: Pishon.", "shem ha'echad pishon: 'the name of the first, Pishon'."),
 ((3,4,5,6,7,8), "It coils round all the land of Havilah, the writhing land,", "hu hasovev 'et kol eretz hachavilah: 'it is the one going round all the land of Havilah'. 'Coils' is the physical stretch of sovev (going round). 'The writhing land' is a gloss from chul; not established."),
 ((9,10,11), "where the gold is.", "asher sham hazahav: 'where there is the gold'."),
],
"2:12": [
 ((0,1,2,3), "The gold of that land is good.", "uzehav ha'arets hahi tov: 'and the gold of that land is good'."),
 ((4,5,6,7), "There is bdolach, and the stone shoham.", "sham habedolach ve'even hashoham: 'there is the bdolach, and the stone of shoham'. Both kept as Hebrew words: their identity is not settled."),
],
"2:13": [
 ((0,1,2,3), "The second: Gihon.", "veshem hanahar hashenI gichon: 'and the name of the second river, Gihon'."),
 ((4,5,6,7,8,9), "It winds round all the land of Kush.", "hu hasovev 'et kol eretz kush: 'it is the one going round all the land of Kush'. 'Winds' is the physical stretch of sovev."),
],
"2:14": [
 ((0,1,2,3,4,5,6,7), "The third: Hiddekel, running east of Ashur.", "veshem hanahar hashelishi chidekel hu hahole kh qidmat ashur: 'the third river, Hiddekel, it goes east of Assyria'. 'East' for qidmat (2:8)."),
 ((8,9,10,11), "The fourth: Perat.", "vehanahar harevi'i hu perat: 'and the fourth river, it is Perat'."),
],
"2:15": [
 ((0,1,2,3,4), "YHWH Elohim took the human", "wayiqqach YHWH elohim et ha'adam: 'YHWH God took the human'."),
 ((5,6,7), "and set him in the garden of delight—", "wayanicheu bigan eden: 'and set him down in the garden of Eden'."),
 ((8,), "to serve it,", "le'avdah: 'to serve it'. 'Serve' is the verb of slavery as well as labour."),
 ((9,), "to keep it.", "ulshomrah: 'and to keep it'."),
],
"2:16": [
 ((0,1,2,3,4,5), "YHWH Elohim laid his order on the human:", "wayetzav YHWH elohim al ha'adam lemor: 'YHWH God commanded upon the human, saying'. 'Laid his order on' is the physical stretch of tzav."),
 ((6,7,8,9,10), "Eat, eat, from every tree of the garden.", "mikkol ets hagan akhol tokhel: 'of every tree of the garden eating you may eat'. The doubling is the infinitive absolute."),
],
"2:17": [
 ((0,1,2,3,4,5,6), "But from the tree of knowing good and harm, do not eat.", "umeets hada'at tov vara' lo tokhal mimmenu: 'and from the tree of knowing good and harm you shall not eat from it'. 'But' is the English's contrast."),
 ((7,8,9,10,11,12), "On the day you eat from it, dying, you will die.", "ki beyom akhlekha mimmenu mot tamut: 'for on the day you eat from it, dying you shall die'. The infinitive absolute."),
],
"2:18": [
 ((0,1,2,3,4), "YHWH Elohim said: not good,", "wayomer YHWH elohim lo tov: 'YHWH God said, not good'."),
 ((5,6,7), "the human alone.", "heyot ha'adam levaddo: 'the human being alone'."),
 ((8,9,10), "I will make him a help,", "e'eseh lo ezer: 'I will make for him a help'. Ezer is 'help', used of God (Ps 33:20)."),
 ((11,), "a face set across from him.", "kenegdo: 'opposite him'. 'A face set across from him' is the physical stretch of 'opposite'."),
],
"2:19": [
 ((0,1,2,3,4,5,6,7), "From the red, YHWH Elohim potted every beast of the field", "wayyitzer YHWH elohim min ha'adamah kol chayat hasadeh: 'YHWH God potted from the ground every beast of the field'."),
 ((8,9,10,11), "and every fowl of the sky,", "ve'et kol of hashamayim: 'and every bird of the sky'."),
 ((12,13,14,15,16,17,18), "and brought them to the human to see what he would call them.", "wayyavei el ha'adam lir'ot mah yiqra lo: 'and brought them to the human to see what he would call it'."),
 ((19,20,21,22,23,24,25), "Whatever the human called each breathing thing,", "vekhol asher yiqra lo ha'adam nefesh chayah: 'and whatever the human called it, a living breath'."),
 ((26,27), "that was its name.", "hu shemo: 'that is its name'."),
],
"2:20": [
 ((0,1,2), "The human called names:", "wayyiqra ha'adam shemot: 'the human called names'."),
 ((3,4,5,6,7,8,9), "to the cattle, to the fowl of the sky, to every beast of the field.", "lekhol habehemah ule'of hashamayim ulekhol chayat hasadeh: 'to all the cattle, and to the bird of the sky, and to every beast of the field'."),
 ((10,11,12,13,14), "But for the human, no face across from him was found.", "ule'adam lo matza ezer kenegdo: 'but for the human he did not find a help opposite him'."),
],
"2:21": [
 ((0,1,2,3,4,5,6), "YHWH Elohim dropped a heavy sleep on the human.", "wayyappel YHWH elohim tardemah al ha'adam: 'YHWH God caused a deep sleep to fall on the human'. Tardemah is deep sleep (cf. 15:12); 'heavy' is the physical stretch."),
 ((7,), "He slept.", "wayyishan: 'and he slept'."),
 ((8,9,10), "He took one of his sides—tsela—", "vayyiqqach achat mitzal'otav: 'and he took one of his sides'. Tsela' is side or rib; kept as the Hebrew word."),
 ((11,12,13), "and shut the flesh over the place.", "vayyisgor basar tachtennah: 'and he shut the flesh over its place'."),
],
"2:22": [
 ((0,1,2,3,4,5,6,7,8,9), "YHWH Elohim built the side he had taken from the human", "wayyiven YHWH elohim et hatzela' asher laqach min ha'adam: 'YHWH God built the side which he took from the human'. Banah is 'build'; it is the verb of building a house or a family."),
 ((10,), "into a woman,", "le'ishah: 'into a woman'."),
 ((11,12,13), "and brought her to the human.", "vayevi'ehah el ha'adam: 'and brought her to the human'."),
],
"2:23": [
 ((0,1,2,3), "The human barked: This time—at last—", "wayomer ha'adam zot hapa'am: 'and the human said, this time'. 'Barked' is the physical stretch of 'said'."),
 ((4,5,6,7), "bone of my bones, flesh of my flesh!", "etzem me'atzamai uvasar mibesari: 'bone from my bones, and flesh from my flesh'."),
 ((8,9,10), "This one: Ishah, woman,", "lezot yiqqare' ishah: 'this one shall be called Ishah'. Ishah is kept as the Hebrew word for the pun."),
 ((11,12,13,14), "for from Ish she was taken.", "ki me'ish luqchah zot: 'for from Ish this one was taken'. Ish is kept for the pun."),
],
"2:24": [
 ((0,1,2,3,4,5,6,7), "Therefore: a man leaves father and mother,", "al ken ya'azov ish et avav ve'et immo: 'therefore a man leaves his father and his mother'. 'Therefore' marks the narrator stepping out of the story."),
 ((8,9), "clings, glues himself to his woman;", "vedavaq be'ishto: 'and clings to his wife'. 'Glues himself' is the physical stretch of davaq (cling, stick)."),
 ((10,11,12), "and they are one flesh.", "vehayu levasar ehad: 'and they shall be one flesh'."),
],
"2:25": [
 ((0,1,2,3,4), "Both bare, the human and his woman,", "vayihyu shneihem arumim ha'adam veishto: 'and both were naked, the human and his wife'. Arumim (bare) is the pun partner of arum (3:1)."),
 ((5,6), "and no shame.", "velo yitboshashu: 'and were not ashamed'."),
],

"3:1": [
 ((0,1,2), "The Hiss was the crafty one—arum, shrewd and bare—", "hanachash hayah arum: 'serpent was crafty'. 'Hiss' for the sibilance of nachash; 'arum' carries both 'crafty' and 'bare' (see 2:25), kept as one line."),
 ((3,4,5), "of all the beasts of the field", "mikol chayat hasadeh: 'of all beast of the field'. Settled."),
 ((6,7,8,9), "YHWH Elohim had made.", "asher 'asah YHWH 'elohim: 'which YHWH God made'. 'Had made' is the pluperfect English gives to a relative clause."),
 ((10,11,12), "It said to the woman:", "vayomer el ha'ishah: 'and it said to the woman'. Plain."),
 ((13,14,15,16), "Did Elohim really say,", "af ki 'amar 'elohim: 'really? God said'. 'Af ki' is the emphatic question; 'really' carries it."),
 ((17,18,19,20,21), "you shall not eat from any tree of the garden?", "lo tokhelu mikol ets hagan: 'you shall not eat from every tree of the garden'. 'Any' for kol; the question mark is the question af ki builds."),
],
"3:2": [
 ((0,1,2,3), "The woman said to the Hiss:", "vattomer ha'ishah el hanachash: 'the woman said to the serpent'. Plain."),
 ((4,5,6,7), "From the fruit of the trees of the garden, we eat.", "mipri ets hagan nokhel: 'from the fruit of the tree of the garden we eat'. 'Trees' pluralises a singular collective; she answers for both of them, 'we'."),
],
"3:3": [
 ((0,1,2,3,4), "But from the fruit of the tree in the middle of the garden,", "umipri ha'ets asher betokh hagan: 'and from the fruit of the tree which is in the midst of the garden'. 'But' is the English's contrast; 'middle' keeps betokh."),
 ((5,6), "Elohim said:", "amar 'elohim: 'God said'."),
 ((7,8,9), "do not eat from it,", "lo tokhelu mimmenu: 'you shall not eat from it'."),
 ((10,11,12), "do not touch it,", "velo tigge'u bo: 'nor touch it'. The touch-prohibition is in the Hebrew here, not in 2:17 (commentary on 3:3)."),
 ((13,14), "lest you die.", "pen temutun: 'lest you become dead'."),
],
"3:4": [
 ((0,1,2,3), "The Hiss hissed at the woman:", "vayomer hanachash el ha'ishah: 'the serpent said to the woman'. 'Hissed' is the register's verb for 'said', with the name Hiss."),
 ((4,5,6), "Not death. You will not die.", "lo mot temutun: 'not death, you shall die-not'. The Hiss reverses the infinitive of 2:17. The English breaks it into a fragment and its negation."),
],
"3:5": [
 ((0,1,2), "Elohim knows:", "ki yodea' 'elohim: 'for God knows'. The 'for' is dropped; the colon makes the snake's reason a flat statement."),
 ((3,4,5,6), "the day you eat,", "ki beyom akhlekhem mimmenu: 'that on the day you eat from it'."),
 ((7,8), "your eyes will split open,", "venifqechu einekhem: 'and your eyes will be opened'. 'Split open' is the bodily stretch of paqach (open the eyes)."),
 ((9,10), "and you will be like Gods,", "vihyitem ke'elohim: 'and you will be like gods'. 'Gods' capitalised, as the English uses for elohim in this sense."),
 ((11,12,13), "knowing good and harm.", "yodei' tov vara': 'knowing good and harm' (see 2:9)."),
],
"3:6": [
 ((0,1), "The woman saw:", "vattere ha'ishah: 'and the woman saw'."),
 ((2,3,4,5), "the tree good to eat,", "ki tov ha'ets lemakhal: 'that the tree was good for food'."),
 ((6,7,8,9), "a hunger for the eyes,", "vechi ta'avah hu la'eynayim: 'and that it was a craving to the eyes'. 'Hunger' is the bodily stretch of ta'avah ('desire, craving')."),
 ((10,11,12), "a tree to be coveted for insight.", "venekhmad ha'ets lehaskil: 'and the tree was desirable to make wise'. 'Coveted' keeps nekhmad (see 2:9); 'insight' is haskil."),
 ((13,14,15), "She took from its fruit and ate.", "vattiqqach mipiryo vattokhel: 'she took from its fruit and ate'."),
 ((16,17,18,19,20), "She gave to her man with her, and he ate.", "vattitten gam le'ishah immah vayokhal: 'she gave also to her husband with her, and he ate'. 'Man' for 'ish; the Hebrew says 'ishah, her husband (commentary on 3:6)."),
],
"3:7": [
 ((0,1,2), "Both their eyes split open,", "vattipaqachna einei shneihem: 'the eyes of both were opened'."),
 ((3,4,5,6), "and they knew they were bare;", "vayeyde'u ki eiromim hem: 'and they knew that they were naked'. 'Bare' carries 'eiromim (2:25)."),
 ((7,8,9,10,11,12), "they sewed fig-leaves and made loin-belts.", "vayitperu alei te'enah vayya'asu lahem chagorot: 'they sewed fig-leaves and made themselves girdles'. 'Loin-belts' stretches chagorot."),
],
"3:8": [
 ((0,1,2,3,4), "They heard the voice of YHWH Elohim", "vayishme'u et qol YHWH 'elohim: 'they heard the voice of YHWH God'."),
 ((5,6,7,8), "pacing in the garden at the wind of the day;", "mithallekh bagan leruach hayom: 'walking about in the garden at the wind of the day'. 'Pacing' is the hithpael of halakh: back and forth. 'Wind' for ruach."),
 ((9,10,11,12,13,14), "the human and his woman hid from the face of YHWH Elohim", "vayyithchabe ha'adam ve'ishto mipenei YHWH 'elohim: 'the human and his wife hid from before YHWH God'."),
 ((15,16,17), "among the trees of the garden.", "betokh ets hagan: 'in the midst of the tree of the garden'. 'Trees' is an English plural of a singular collective."),
],
"3:9": [
 ((0,1,2,3,4), "YHWH Elohim called to the human:", "vayiqra YHWH 'elohim el ha'adam: 'YHWH God called to the human'."),
 ((5,6,7), "Ayyekka—where are you?", "vayomer lo ayyekka: 'and said to him, where?'. A rare form of ayeh; the question is God's."),
],
"3:10": [
 ((0,1,2,3,4), "He said: I heard your voice in the garden.", "vayomer et qolekha shamati bagan: 'he said: your voice I heard in the garden'."),
 ((5,6,7,8,9), "I shook, for I am bare, and I hid.", "va'ira ki eirom anokhi va'ei'chaveh: 'I feared, for I am naked, and I hid'. 'Shook' is the bodily stretch of ira (fear, awe)."),
],
"3:11": [
 ((0,1,2,3,4,5,6), "He said: Who told you you were bare?", "vayomer mi higgid lekha ki eirom atah: 'he said: who told you that you are naked?'. 'Who' is the mi that opens the question."),
 ((7,8,9,10,11,12,13,14), "From the tree I charged you about—did you eat?", "hamin ha'ets asher tsiviti'kha livlti akhol mimmenu akhalta: 'from the tree I charged you not to eat from, did you eat?'. 'From' is hamin, the interrogative marker."),
],
"3:12": [
 ((0,1,2,3,4,5), "The human said: The woman you set with me—", "vayomer ha'adam ha'ishah asher natatta immadi: 'the human said: the woman you gave with me'. 'Set' for natatta (gave, placed)."),
 ((6,7,8,9,10,11), "she handed me from the tree, and I ate.", "hi natenah li min ha'ets va'okhel: 'she gave me from the tree, and I ate'. 'Handed' is the physical stretch of natan."),
],
"3:13": [
 ((0,1,2,3,4,5,6), "YHWH Elohim said to the woman: What is this you have done?", "vayomer YHWH 'elohim la'ishah mah zot 'asit: 'YHWH God said to the woman, what is this you did?'."),
 ((7,8,9,10,11), "The woman said: The Hiss snared me, and I ate.", "vattomer ha'ishah hanachash hishi'ani va'okhel: 'the woman said: the serpent deceived me, and I ate'. 'Snared' is the physical stretch of nasha' (deceive, beguile)."),
],
"3:14": [
 ((0,1,2,3,4,5,6,7,8), "YHWH Elohim said to the Hiss: Because you did this—", "vayomer YHWH 'elohim el hanachash ki 'asita zot: 'YHWH God said to the serpent, because you did this'. The paseq (3) is not rendered."),
 ((9,10,11,12), "cursed you are, out of all the cattle,", "'arur atah mikol habehemah: 'cursed are you out of all the cattle'."),
 ((13,14,15), "out of all the beasts of the field.", "umikol chayat hasadeh: 'and out of all the beasts of the field'."),
 ((16,17,18), "On your gut you will go,", "al gechonkha telekh: 'upon your belly you shall walk'. 'Gut' is the physical stretch of gechon (belly, underside); 'go' is the stretch of halakh (walk)."),
 ((19,20,21,22,23), "and dust you will eat all the days of your life.", "vafar tokhal kol yemei chayyekha: 'and dust you shall eat all the days of your life'."),
],
"3:15": [
 ((0,1,2), "Hatred I will set", "ve'eivah ashit: 'and enmity I will set'. 'Hatred' is the physical stretch of eivah."),
 ((3,4,5), "between you and the woman,", "beinkha uvein ha'ishah: 'between you and the woman'."),
 ((6,7,8,9), "between your seed and her seed:", "uvein zar'akha uvein zar'ah: 'between your seed and her seed'. 'Seed' is collective."),
 ((10,11,12), "he—it—will crush your head;", "hu yeshufkha rosh: 'it will crush you on the head'. 'He—it' keeps hu's masculine and its referent open."),
 ((13,14,15), "you will bruise its heel.", "ve'atah teshufenu akev: 'and you will bruise it on the heel'. 'Bruise' repeats shuf, the same verb as 'crush'."),
],
"3:16": [
 ((0,1,2,3,4), "To the woman he said: I will multiply, multiply", "'el ha'ishah amar harbah arbeh: 'to the woman he said: multiplying I will multiply'. The infinitive absolute is kept as a doubled verb."),
 ((5,6), "your pain and your conceiving.", "itstsavonekh vehe'ronekh: 'your toil and your conception'. 'Conceiving' keeps heron (conception). 'Groaning' is the LXX's reading, not the Hebrew."),
 ((7,8,9), "In pain you will bear children.", "be'etsev telidi vanim: 'in pain you will bear children'."),
 ((10,11,12,13,14,15), "Toward your man your craving, and he will rule you.", "ve'el ishekh teshuqatekh vehu yimshol bakh: 'and toward your man your craving, and he will rule over you'. 'Craving' is teshuqah, the word of 4:7 too."),
],
"3:17": [
 ((0,1,2,3,4,5), "To the human he said: Because you listened to your woman's voice", "ule'adam amar ki shama'ta lekol ishtekha: 'and to the human he said: because you listened to your wife's voice'. 'Woman's' for ishtekha (your wife)."),
 ((6,7,8,9,10,11,12,13,14), "and ate from the tree I charged you about—'do not eat from it'—", "vatokhal min ha'ets asher tsiviti'kha lemor lo tokhal mimmenu: 'and you ate from the tree I charged you, saying, you shall not eat from it'."),
 ((15,16,17), "the ground is cursed because of you.", "arurah ha'adamah ba'avurekha: 'cursed is the ground because of you'. 'Because of you' for ba'avurekha (the Hebrew's 'for your sake' is the LXX's 'for' as well)."),
 ((18,19,20,21,22), "In pain you will eat from it all the days of your life.", "be'itstsavon tokhelenah kol yemei chayyekha: 'in pain you shall eat it all the days of your life'."),
],
"3:18": [
 ((0,1,2,3), "Thorn and thistle it will sprout for you;", "vekotz vedardar tatzmiach lakh: 'and thorn and thistle it will sprout for you'. 'Thistle' keeps the rough sound of dardar."),
 ((4,5,6,7), "you will eat the grass of the field.", "ve'akhalta et 'eseb hasadeh: 'and you shall eat the herb of the field'. 'Grass' narrows 'eseb (herb)."),
],
"3:19": [
 ((0,1,2,3), "In the sweat of your nose you will eat bread", "bezei'at appekha tokhal lechem: 'by the sweat of your nostrils you shall eat bread'. 'Nose' is the literal, physical sense of appayim; 'face' and 'anger' are the other readings."),
 ((4,5,6,7,8,9,10), "until you return to the red—for from it you were taken.", "'ad shuvekha el ha'adamah ki mimmenah luqqachta: 'until your return to the ground, for from it you were taken'. 'The red' is the English for adamah (see 1:25)."),
 ((11,12,13,14,15,16), "Dust you are, and to dust you turn back.", "ki 'afar atah ve'el 'afar tashuv: 'for dust you are, and to dust you shall return'. 'Turn back' is the physical stretch of shuv (return)."),
],
"3:20": [
 ((0,1,2,3,4), "The human named his woman Chavah—Living—", "vayiqra ha'adam shem ishto chavah: 'the human called the name of his wife Chavah'. 'Living' is the English gloss of the name's root chayah."),
 ((5,6,7,8,9,10), "for she became mother of all the living.", "ki hi hayatah em kol chai: 'for she was mother of all the living'."),
],
"3:21": [
 ((0,1,2,3,4), "YHWH Elohim made for the human and his woman", "vayya'as YHWH 'elohim le'adam ulishto: 'and YHWH God made for the human and for his wife'."),
 ((5,6,7), "hide-coats, and dressed them.", "ketonot or vayalbishem: 'skin-tunics, and clothed them'. 'Hide-coats' is the physical stretch of ketonot or (skin tunics)."),
],
"3:22": [
 ((0,1,2,3), "YHWH Elohim said:", "vayomer YHWH 'elohim: 'and YHWH God said'. The paseq (1) is not rendered."),
 ((4,), "Look—", "hen: 'behold'."),
 ((5,6), "the human has become", "ha'adam hayah: 'the human was'. 'Has become' is the English perfect for hayah."),
 ((7,8), "like one of us,", "ke'echad mimmenu: 'like one of us' (or 'of it'). 'Us' keeps the plural reading."),
 ((9,10,11), "knowing good and harm.", "ladaat tov vara': 'to know good and harm'."),
 ((12,13,14,15,16,17,18,19,20), "Now lest he reach out his hand, take also from the tree of lives,", "ve'attah pen yishlach yado velaqach gam me'ets hachayyim: 'and now lest he send out his hand and take also from the tree of lives'. 'Reach out' is the physical stretch of shalach (send out)."),
 ((21,22,23), "eat, and live—forever.", "ve'akhal vachay le'olam: 'and eat, and live forever'."),
],
"3:23": [
 ((0,1,2,3,4), "YHWH Elohim sent him out from the garden of delight,", "vayshallehu YHWH 'elohim migan 'eden: 'YHWH God sent him out from the garden of Eden'. 'Delight' is the English reading of Eden."),
 ((5,6,7,8,9,10), "to serve the red from which he was taken.", "la'avod et ha'adamah asher lukkach mishsham: 'to serve the ground from which he was taken'. 'Serve' is the verb of slavery as well as labour."),
],
"3:24": [
 ((0,1,2), "He drove the human out.", "vayegaresh et ha'adam: 'and he drove out the human'. Garash is 'drive out'."),
 ((3,4,5,6,7,8), "At the east of the garden of delight he set the cherubim", "vayyashken miqqedem legan 'eden et hakerubim: 'and he settled, from the east of the garden of Eden, the cherubim'. 'Set' is the English for shakan (settle); 'at the east' keeps miqqedem's eastward sense (2:8)."),
 ((9,10,11,12,13,14,15,16,17), "and the flame of the turning blade, to guard the road to the tree of lives.", "ve'et lahat hacherev hamitpakhekhet lishmor et derekh ets hachayyim: 'and the flame of the turning sword, to guard the way of the tree of lives'. 'Turning blade' keeps mitpakhekhet."),
],

"4:1": [
 ((0,1,2,3,4), "Now the human knew Chavah his woman;", "vehaadam yada' et chavah ishto: 'and the human knew Eve his wife'. 'Knew' is yada', which also means intimate knowledge (the context here)."),
 ((5,6,7,8,9), "she conceived and bore Qayin, and said:", "vattaharr vattelad et qayin vattomer: 'and she conceived and bore Qayin, and she said'."),
 ((10,11,12,13), "I have gotten a man—YHWH.", "qaniti ish et YHWH: 'I have gotten a man, YHWH' (or 'with YHWH'). 'Gotten' is qanah (acquire); 'YHWH' as apposition is the reading kept."),
],
"4:2": [
 ((0,1,2,3,4,5), "She bore again: his brother Hevel.", "vattosef lalledet et achiv et hevel: 'she went on to bear his brother Hevel'. 'Bore again' is tosef (add) with the infinitive."),
 ((6,7,8,9), "Hevel, herder of flocks.", "vayehi hevel ro'eh tzon: 'and Hevel was a herder of flocks'. 'Was' is carried by the appositive."),
 ((10,11,12,13), "Qayin, worker of the red.", "veqayin hayah oved adamah: 'and Qayin was a worker of the ground'. 'Red' is the English for adamah (see 1:25)."),
],
"4:3": [
 ((0,1,2), "At the end of days, miqqetz yamim,", "vayehi miqqetz yamim: 'and it was at the end of days'. 'At the end' for miqqetz (from the cut-off); the Hebrew phrase is kept beside it."),
 ((3,4,5,6,7,8), "Qayin brought from the fruit of the red a gift to YHWH.", "vayyavi qayin mipri ha'adamah minchah layhvh: 'Qayin brought from the fruit of the ground an offering to YHWH'. 'Gift' is the stretch of minchah (offering)."),
],
"4:4": [
 ((0,1,2,3,4,5,6), "And Hevel too: from the firstborn of his flock, from their fat,", "vehevel hevi gam hu mibekhorot tzono umechelbehen: 'and Hevel, he too brought from the firstborn of his flock and from their fat'. 'Fat' for chelbehen, the richest portion."),
 ((7,8,9,10,11,12), "and YHWH fixed his eye on Hevel and his gift.", "vayyisha' YHWH el hevel ve'el minchato: 'and YHWH looked to Hevel and to his offering'. 'Fixed his eye' is the physical stretch of sha'a (gaze)."),
],
"4:5": [
 ((0,1,2,3,4,5), "But to Qayin and his gift he did not look.", "ve'el qayin ve'el minchato lo sha'ah: 'but to Qayin and to his offering he did not look'."),
 ((6,7,8,9,10), "Qayin burned, burned exceedingly, and his face fell.", "vayyichar leqayin me'od vayyippelu panav: 'it burned for Qayin exceedingly, and his face fell'. 'Burned' is the physical stretch of charah (heat, anger)."),
],
"4:6": [
 ((0,1,2,3), "YHWH said to Qayin:", "vayomer YHWH el qayin: 'and YHWH said to Qayin'."),
 ((4,5,6), "Why do you burn?", "lamah charah lakh: 'why has it burned for you'. 'Do you burn' is the English for the second person."),
 ((7,8,9), "Why has your face fallen?", "velamah nafelu panekha: 'and why have your face fallen'."),
],
"4:7": [
 ((0,1,2,3), "Is it not so? If you do well, a lifting of the face.", "halo im teitiv se'et: 'is it not so? if you do well, a lifting'. 'Of the face' is an addition: se'et panim is not in the verse (commentary on 4:7)."),
 ((4,5,6,7,8,9), "If you do not do well, at the door a sin crouches—", "veim lo teitiv lappetach chattat rovets: 'and if you do not do well, at the door sin crouches'. 'Crouches' is the physical stretch of rovets (lying in wait)."),
 ((10,11,12,13,14), "its craving is for you; but you, rule it.", "ve'elekha teshuqato ve'attah timshol bo: 'toward you its craving; and you, rule over it'. 'Craving' keeps teshuqah from 3:16."),
],
"4:8": [
 ((0,1,2,3,4), "Qayin spoke to Hevel his brother—", "vayomer qayin el hevel achiv: 'and Qayin said to Hevel his brother'. The Hebrew gives no content for the speech; the dash in the English stands for that absence."),
 ((5,6,7), "and it was, in the field,", "vayehi bihyotam basadeh: 'and it was, when they were in the field'."),
 ((8,9,10,11,12), "that Qayin reared on Hevel his brother", "vayyaqom qayin el hevel achiv: 'and Qayin rose up against Hevel his brother'. 'Reared on' is the physical stretch of qum (rise)."),
 ((13,), "and struck him dead.", "vayyahargehu: 'and killed him'. Harag is a violent slaying; 'struck him dead' is the English's bodily word for it."),
],
"4:9": [
 ((0,1,2,3,4,5,6), "YHWH said to Qayin: Where is Hevel your brother?", "vayomer YHWH el qayin ei hevel achikha: 'and YHWH said to Qayin, where is Hevel your brother'."),
 ((7,8,9), "He said: I do not know.", "vayomer lo yada'ti: 'and he said, I do not know'."),
 ((10,11,12), "Am I the guard of my brother?", "hashomer achi anokhi: 'am I the keeper of my brother?'. 'Guard' is the physical English for shomer, the verb of 2:15."),
],
"4:10": [
 ((0,1,2), "He said: What have you done?", "vayomer mah 'asita: 'and he said, what did you do?'."),
 ((3,4,5), "A voice—your brother's bloods—", "qol demei achikha: 'the voice of your brother's bloods'. 'Voice' was dropped in an earlier draft and is restored here."),
 ((6,7,8,9), "cries to me from the red.", "tso'aqim elai min ha'adamah: 'crying out to me from the ground'. 'Cries' is the finite verb of the English; 'red' is adamah."),
],
"4:11": [
 ((0,1,2,3,4), "Now: cursed are you from the red,", "ve'attah arur atah min ha'adamah: 'and now cursed are you from the ground'."),
 ((5,6,7,8,9,10,11,12,13), "which gaped its mouth to take your brother's bloods from your hand.", "asher patzta et piha laqachat et demei achikha miyyadekha: 'which opened its mouth to take your brother's bloods from your hand'. 'Gaped' is the physical stretch of patzah (open)."),
],
"4:12": [
 ((0,1,2,3,4,5,6,7,8), "When you work the red, it will no more give you its strength.", "ki ta'avod et ha'adamah lo tosef tet kocha lakh: 'when you work the ground, it will no longer give you its strength'. Yasaf with an infinitive is 'no longer'; 'add' is a misreading (corrected from an earlier draft)."),
 ((9,10,11,12), "A reeler, a wanderer, you will be on the earth.", "na' vanad tihyeh ba'arets: 'a staggerer and a drifter you will be in the earth'. 'Reeler' and 'wanderer' are the physical stretch of two sounds of motion."),
],
"4:13": [
 ((0,1,2,3,4,5,6), "Qayin said to YHWH: My twist is heavier than I can lift,", "vayomer qayin el YHWH gadol avoni minnesso: 'Qayin said to YHWH: my guilt is great, from bearing'. 'Twist' is the physical stretch of avon (guilt, twisted way); 'lift' carries nasa'."),
 ((), "too heavy to be lifted off me.", "Not a separate token: the second line carries nasa's second sense, forgiveness ('lifted off me'). An addition, marked; the commentary on 4:13 names the double sense."),
],
"4:14": [
 ((0,1,2,3,4,5,6), "Look—you drive me out today from the face of the red.", "hen gerashta oti hayyom me'al penei ha'adamah: 'look, you drive me out today from upon the face of the ground'. Garash is 'drive out'."),
 ((7,8), "I will hide from your face;", "umippanekha essater: 'and from your face I shall hide'."),
 ((9,10,11,12), "I shall be a reeler and wanderer on the earth,", "vehayiti na' vanad ba'arets: 'and I shall be a staggerer and a drifter in the earth'."),
 ((13,14,15,16), "and whoever finds me will kill me.", "vehayah kol motz'i yahargeni: 'and whoever finds me will kill me'."),
],
"4:15": [
 ((0,1,2,3), "YHWH said to him: Not so—therefore—", "vayomer lo YHWH lakhen: 'and YHWH said to him, therefore'. Lakhen reads 'therefore'; the LXX's 'not so' is a witness variant (commentary on 4:15)."),
 ((4,5,6,7,8), "whoever kills Qayin will be paid back sevenfold.", "kol horeg qayin shivatayim yukkam: 'whoever kills Qayin, sevenfold shall be avenged'. 'Paid back' is the physical stretch of naqam (avenge)."),
 ((9,10,11,12,13,14,15,16,17), "YHWH cut a mark into Qayin, so no one who found him would hit him.", "vayyasem YHWH leqayin ot levilti hakkot oto kol motz'o: 'and YHWH set for Qayin a sign, so that no one who found him would strike him'. 'Cut a mark into' is the physical stretch of sum (set); 'hit' is hakkot."),
],
"4:16": [
 ((0,1,2,3), "Qayin went out from the face of YHWH", "vayyetze qayin millifnei YHWH: 'and Qayin went out from before YHWH'."),
 ((4,5,6,7,8), "and settled in the land of Nod—Wandering—east of Eden.", "vayyeshev be'eretz nod qidmat eden: 'and he settled in the land of Nod, east of Eden'. 'Wandering' is the English gloss of the name Nod, from nad (4:14)."),
],
"4:17": [
 ((0,1,2,3,4,5,6,7), "Qayin knew his woman; she conceived and bore Chanokh.", "vayeda qayin et ishto vattaharr vattelad et chanokh: 'Qayin knew his wife; she conceived and bore Enoch'."),
 ((8,9,10,11,12,13,14,15,16), "He was building a city, and named the city after his son: Chanokh.", "vayehi bonneh ir vayiqra shem ha'ir kishem beno chanokh: 'and he was building a city, and called the name of the city after the name of his son, Enoch'."),
],
"4:18": [
 ((0,1,2,3), "To Chanokh was born Irad;", "vayyiwwaled lechanokh et irad: 'there was born to Enoch, Irad'. Passive; 'was born' keeps it."),
 ((4,5,6,7), "Irad fathered Mechuyael;", "veirad yalad et mechuyael: 'and Irad fathered Mechuyael'."),
 ((8,9,10,11), "Mechuyael fathered Methushael;", "umechiyael yalad et methushael: 'and Mechiyael fathered Methushael'. The Hebrew spells the name Mechuyael (4:18a) and Mechiyael (4:18b); the English keeps both as given."),
 ((12,13,14,15), "Methushael fathered Lamech.", "umethushael yalad et lamech: 'and Methushael fathered Lamech'. The chain ends on Lamech."),
],

}
