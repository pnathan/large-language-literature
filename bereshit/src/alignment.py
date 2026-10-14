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
 ((10,), "a brooding bird", "merachefet, 'hovering/brooding'. The English gives the simile 'a bird' as a stretch from the root (Deut 32:11 uses the same root of an eagle over its young). 'Brooding' is the fitting verb of that bird."),
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
 ((2,), "", "Paragraph marker (ketiv pasuq); no English."),
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
 ((6,7), "a wall, a splitter—", "wihi mavdil, 'and let it be a separator'. 'A wall' is an addition: mavdil is 'separator', and 'wall' is what raqia' does in the LXX/Greek tradition (stereōma). Marked."),
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
 ((2,), "", "'elohim repeated."),
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
 ((12,), "signs,", "le'otot, 'for signs'. 'Signs' is the settled sense of 'ot (mark, sign)."),
 ((13,), "tellers of times,", "ulemo'adim, 'and for appointed times'. 'Tellers of times' stretches mo'ed: the appointed time is read as something that tells. Alternative 'seasons' is settled and tame."),
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
 ((9,10), "across the face of the hammered sky.", "'al ha'arets 'al penei rqia' hashamayim, 'upon the earth, upon the face of the firmament of the heavens'. 'Across' is the English's compression of 'al ('upon'); 'the face of the hammered sky' keeps the raqia' stretch. 'Across' is a stretch: 'upon' is the Hebrew's spatial preposition."),
 ((11,12,13,14), "", "al penei rqia' hashamayim, carried above."),
],

"1:21": [
 ((0,1), "Elohim made the great serpents of the deep, the tanninim,", "wayivra' 'elohim et hattanninim hagedolim, 'and God created the great sea-monsters'. The verb is bara' here, not 'asah: 'made' is the English for bara' in this line, and the choice is deliberate, since the chaos-monsters are made, not slain (commentary on 1:21). 'Serpents of the deep' is an addition that places the tanninim in the Deep of 1:2."),
 ((2,), "", "'et, object marker."),
 ((3,4), "", "hattanninim hagedolim, carried above; 'the tanninim' is kept as the Hebrew word."),
 ((5,6,7,8), "and every breathing swarm the waters bred, after its kind,", "ve'et kol nefesh hachayah harommeset asher sharetzu hamayim lemineihem, 'and every living breath that creeps which the waters swarmed, after their kinds'. 'Breathing swarm' is the stretch of nefesh hachayah harommeset; 'bred' is the stretch of sharetzu (teemed). 'Every' keeps kol."),
 ((9,), "", "paragraph marker; no English."),
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
 ((2,), "", "paragraph marker; no English."),
 ((3,4), "the human", "'et ha'adam, 'the human'. The 'et is not rendered."),
 ((), "out of the red", "Not in 1:27. The Hebrew says 'the human' only. 'Out of the red' links the human to adamah (1:25, 2:7), and is an addition marked for the pun."),
 ((5,), "into a shadow of himself—", "betsalmo, 'in his image'. 'A shadow' is the stretch of tselem (shade, image); 'of himself' resolves the pronoun to the human. Alternative 'in his image' is the standard."),
 ((6,7), "into the shadow of God", "betselem 'elohim, 'in the image of God'. Same stretch."),
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
 ((0,), "So sky and ground were finished,", "wayekhullu, 'and were finished/completed'. 'So' is the English's bridge from 1:31, since the Hebrew opens with 'and'."),
 ((1,2), "sky and ground", "hashamayim vehaaretz, 'the heavens and the earth'. Order kept from 1:1 (heaven first), with 'sky' as the narrowing already used."),
 ((3,4), "and all their muster.", "vekhol tz'vaam, 'and all their host'. 'Muster' is the stretch of tz'va, 'host, army': the stars and the mustered order. Alternative 'host' is the standard and is closer to the army sense."),
],

"2:2": [
 ((0,1), "Elohim finished on the seventh day", "wayekhal 'elohim bayom hashevi'i, 'and God finished on the seventh day'. The Hebrew says the seventh day; the LXX says the sixth (witness variant, see commentary)."),
 ((2,3), "", "bayom hashevi'i, carried above."),
 ((4,5,6), "the work he had made;", "melakhto asher 'asah, 'his work that he had made'. 'The work' is melakhah; 'he had made' is 'asah."),
 ((7,), "and on the seventh day he quit", "wayishbot, 'and he ceased/rested'. 'Quit' is the register's word for shavat: a labourer putting the tool down. Alternative 'rested' is the settled sense of the Sabbath, and the verse does not yet name rest as a day (commentary)."),
 ((8,9), "", "bayom hashevi'i, carried above."),
 ((10,11,12,13), "from all the work he had made.", "mikol melakhto asher 'asah, 'from all his work that he had made'. Repeats the object of 2:2a."),
],

"2:3": [
 ((0,), "He knelt in blessing toward the seventh day,", "wayevarekh, 'and he blessed'. 'Knelt in blessing' is the stretch of barak, whose root some link to 'knee' (berekh). The link is disputed; the image is the register's choice."),
 ((1,), "", "'elohim, carried above."),
 ((2,3,4), "", "et yom hashevi'i, 'the seventh day'. Object marker and noun carried above."),
 ((5,6), "cut it out, set it apart,", "vayqaddesh oto, 'and he sanctified it'. 'Cut it out' is the stretch of qadosh (set apart); 'set it apart' is the standard sense. Both are given: the cut is the bodily reading."),
 ((7,), "because", "ki, 'that/because'."),
 ((8,), "on it", "bo, 'in it'."),
 ((9,), "he laid down", "shavat, 'he ceased'. Same verb as 2:2 'quit'; here 'laid down', a different English verb for the same root, which is a loss of repetition marked in the commentary."),
 ((10,11), "from all the work", "mikol melakhto, 'from all his work'."),
 ((12,13,14,15), "Elohim cut to make.", "asher bara' 'elohim la'asot, 'which God created to make'. 'Cut to make' keeps the doubled verb bara' + la'asot (see 1:1 on bara'). 'Cut' is the same stretch as in 1:1 'hack'; alternative 'created' is the settled sense."),
],

"2:4": [
 ((0,1), "These are the begettings—", "'elleh toledot, 'these are the generations'. 'Begettings' keeps yalad's bearing; 'generations' is the settled sense and is rejected as too genealogical for the register."),
 ((), "toledot, the outcomes—", "Not a separate Hebrew token: 'toledot' (token 1) is glossed twice, once as 'begettings' above and once here as the Hebrew word itself, kept visible. 'Outcomes' is an addition to the begetting sense."),
 ((2,3), "of sky and ground,", "hashamayim vehaaretz, 'the heavens and the earth'. Order kept from 2:1."),
 ((4,), "in their being cut,", "behibare'am, 'in their being created'. 'Cut' is the stretch of bara' (see 1:1). The Hebrew is a niphal infinitive: 'being created'."),
 ((5,6), "in the day", "beyom 'asot, 'in the day of making'. 'In the day' drops 'asot (making), carried in the next line."),
 ((7,8), "YHWH Elohim made", "YHWH 'elohim, 'YHWH God'. 'YHWH' is kept as the Name, 'Elohim' as the name the reader has. 'Made' is 'asot (infinitive)."),
 ((9,10), "ground and sky.", "'eretz veshamayim, 'earth and heavens'. The English reverses order to 'ground and sky' (chiasm, commentary). 'Ground' for 'eretz, 'sky' for shamayim."),
],

"2:5": [
 ((0,1,2), "No thorn-bush of the field yet on the ground,", "vekhol siach hasadeh terem yihyeh va'arets, 'and every shrub of the field not yet was on the earth'. 'Thorn-bush' is the stretch of siach (shrub); the root also gives 'talk' (Ps 77:13), a reading not kept."),
 ((3,4,5,6), "", "hasadeh terem yihyeh ba'arets, carried above."),
 ((7,8,9,10,11), "no grass of the field yet sprung.", "vekhol esev hasadeh terem yitzmach, 'and every grass of the field not yet sprung'. 'Sprung' is the English for yitzmach (to sprout)."),
 ((12,13,14,15,16,17), "YHWH Elohim had not rained on the ground,", "ki lo himtir YHWH 'elohim al ha'arets, 'for YHWH God had not rained upon the earth'. 'Rained' keeps himtir."),
 ((18,), "", "ha'arets, carried above."),
 ((19,20,21,22,23), "and there was no human to work the red.", "veadam ayin la'avod et ha'adamah, 'and there was no human to work the ground'. 'The red' is adamah (see 1:25)."),
],

"2:6": [
 ((0,1,2,3), "A seep rose out of the earth", "ved ya'aleh min ha'arets, 'and a mist/seep rose from the earth'. 'Seep' is the choice from ed (mist, flow, spring); alternative 'mist' is the common reading and is rejected here for the underground sense."),
 ((4,5,6,7,8), "and drenched the whole face of the red.", "vehishkah et kol penei ha'adamah, 'and it watered all the face of the ground'. 'Drenched' is the stretch of hishqah (water); 'the whole face' keeps kol penei."),
],

"2:7": [
 ((0,1,2,3,4), "YHWH Elohim potted the human", "wayyitzer YHWH 'elohim et ha'adam, 'and YHWH God formed the human'. 'Potted' is the stretch of yatsar (form, as a potter forms clay)."),
 ((5,6,7), "from dust of the ground—afar—", "afar min ha'adamah, 'dust from the ground'. 'Afar' is the Hebrew word kept in the English as an echo; 'dust' is the gloss. The dash marks the Hebrew's noun."),
 ((8,9), "and blew into his nostrils", "vayippach be'appav, 'and breathed into his nostrils'. 'Blew' is the stretch of nafach (breathe, blow). 'Nostrils' is the literal, and appav is also 'anger' (commentary)."),
 ((10,11), "breath of lives;", "nishmat chayyim, 'breath of lives'."),
 ((12,13), "and the human became", "wayehi ha'adam, 'and the human became'."),
 ((14,15), "a living throat.", "lenefesh chayah, 'to a living breath/soul'. 'Throat' is the stretch of nefesh (see 1:20)."),
],

"2:8": [
 ((0,1,2), "YHWH Elohim planted", "wayyitta YHWH 'elohim, 'and YHWH God planted'."),
 ((3,4), "a garden of delight,", "gan be'eden, 'a garden in Eden'. 'Of delight' is the English reading of Eden's root edan; the Hebrew treats Eden as a place name, and the English keeps both."),
 ((5,), "from the front, from of old, eastward,", "miqqedem, 'from the east / of old / before'. Three glosses are kept in one line because the Hebrew holds them together."),
 ((6,7), "and set there", "wayyasem sham, 'and he set there'."),
 ((8,9), "the human", "et ha'adam, 'the human'."),
 ((10,11), "he had shaped.", "asher yatzar, 'whom he had shaped'. 'Shaped' is yatzar, the potter's verb (see 2:7 'potted')."),
],

"2:9": [
 ((0,1,2,3,4), "From the red he made spring", "wayyatzmach YHWH 'elohim min ha'adamah, 'and YHWH God made to spring from the ground'. 'Made spring' is the causative of tzamach (sprout)."),
 ((5,6), "every tree", "kol ets, 'every tree'."),
 ((7,8), "to covet with the eyes,", "nekhmad lemar'eh, 'desirable to look at'. 'Covet' is the stretch of chamad (desire); 'with the eyes' is the English's reading of lemar'eh (the look)."),
 ((9,10), "sweet to the mouth;", "vetov lema'akhal, 'and good for food'. 'Sweet' is the stretch of tov as taste; 'mouth' is added for the bodily image."),
 ((11,12), "the tree of lives", "ve'ets hachayyim, 'and the tree of lives'."),
 ((13,14), "at the garden's heart,", "betokh hagan, 'in the midst of the garden'. 'Heart' is the stretch of betokh (midst); see 1:6 on 'belly'."),
 ((15,16,17,18), "and the tree of knowing good and harm.", "ve'ets hada'at tov vara', 'and the tree of knowing good and harm'. 'Knowing' is da'at; 'harm' is ra' (see 2:9 commentary)."),
],

"2:10": [
 ((0,1,2), "A river came out of delight", "venahar yotze me'eden, 'and a river went out from Eden'. 'Delight' is the English reading of Eden (see 2:8)."),
 ((3,4,5), "to water the garden;", "lehashqot et hagan, 'to water the garden'."),
 ((6,7), "from there it split", "umisham yipared, 'and from there it divides'. 'Split' is the stretch of parad (divide, separate)."),
 ((8,9,10), "and became four heads.", "vehayah le'arba'ah rashim, 'and it became four heads'. 'Heads' keeps rosh (head, source)."),
],

"2:11": [
 ((0,1,2), "The first: Pishon.", "shem ha'echad pishon, 'the name of the first, Pishon'. The name is given without a verb."),
 ((3,4), "It coils", "hu hasovev, 'it is the one that circles'. 'Coils' is the stretch of sabbi (circle); the snake-image is added, marked."),
 ((5,6,7), "round all the land of", "'et kol 'eretz, 'all the land of'. 'Round' is the English for 'et and sabbi."),
 ((8,), "Havilah, the writhing land,", "hachavilah, 'Havilah'. 'Writhing land' is a gloss from the root chul; the English shows it as a visible echo, not a settled derivation."),
 ((9,10,11), "where the gold is.", "asher sham hazahav, 'where there is the gold'. 'Gold' keeps zahav."),
],

"2:12": [
 ((0,1,2,3), "The gold of that land is good.", "uzehav ha'arets hahi tov, 'and the gold of that land is good'. Straight rendering."),
 ((4,), "There is", "sham, 'there'."),
 ((5,), "bdolach,", "habedolach. Untranslated: the substance is of uncertain identity (commentary). 'Bdolach' is kept as a Hebrew word, not a guessed gloss."),
 ((6,7), "and the stone shoham.", "ve'even hashoham, 'and the stone of shoham'. Kept as a Hebrew word for the same reason."),
],

"2:13": [
 ((0,1,2,3), "The second: Gihon.", "veshem hanahar hashenI gichon, 'and the name of the second river, Gihon'. 'Second' is the ordinal."),
 ((4,5), "It bursts out", "hu hasovev, 'it is the one that circles'. 'Bursts out' is the English's stretch: gihon's root gush (gihah) is the name's sound, and the English moves the verb to the river (commentary)."),
 ((6,7,8,9), "round all the land of Kush.", "'et kol 'eretz kush, 'all the land of Kush'. Kush kept as a name."),
],

"2:14": [
 ((0,1,2,3), "The third: Hiddekel,", "veshem hanahar hashelishi chidekel, 'and the name of the third river, Hiddekel'."),
 ((4,5,6,7), "running east of Ashur.", "hu hahole kh qidmat ashur, 'it is the one that goes eastward of Assyria'. 'Running' for halokh; 'east' for qidmat (see 2:8)."),
 ((8,9,10,11), "The fourth: Perat.", "vehanahar harevi'i hu perat, 'and the fourth river, it is Perat'."),
],

"2:15": [
 ((0,1,2,3), "YHWH Elohim took the human", "wayiqqach YHWH 'elohim et ha'adam, 'and YHWH God took the human'."),
 ((4,5,6,7), "and set him in the garden of delight—", "vayanichehu bigan 'eden, 'and set him in the garden of Eden'. 'Delight' is the English reading of Eden."),
 ((8,), "to serve it,", "le'avdah, 'to serve/work it'. 'Serve' is the verb of slavery as well as labour; LXX drops it."),
 ((9,), "to keep it.", "ulshomrah, 'and to keep it'. 'Keep' is the settled sense of shamar."),
],

"2:16": [
 ((0,1,2), "YHWH Elohim laid his order on the human:", "wayetzav YHWH 'elohim 'al ha'adam, 'and YHWH God commanded upon the human'. 'Laid his order on' is the stretch of tzav (command) as a physical placement."),
 ((3,4,5), "", "al ha'adam lemor, 'upon the human, saying'. 'Saying' is dropped; the colon marks the speech."),
 ((6,7,8,9,10), "Eat, eat, from every tree of the garden.", "mikkol ets hagan akhol tokhel, 'from every tree of the garden eating you may eat'. The doubled 'eat, eat' keeps the infinitive absolute (commentary)."),
],

"2:17": [
 ((0,1,2,3), "But from the tree of knowing good and harm,", "umeets hada'at tov vara', 'and from the tree of knowing good and harm'. 'But' replaces the Hebrew 'and' (contrast). The English adds the contrast; marked."),
 ((4,5,6), "do not eat.", "lo tokhal mimmenu, 'you shall not eat from it'. 'Do not' is the English imperative; the Hebrew is future negative. 'From it' is dropped in this line and carried into the next."),
 ((7,8,9,10), "On the day you eat from it,", "ki beyom akhlekha mimmenu, 'for on the day of your eating from it'. 'On the day' is kept as the Hebrew's 'be-yom'; the English turns the gerund into 'you eat'."),
 ((11,12), "dying, you will die.", "mot tamut, 'dying you shall die'. The infinitive absolute kept as 'dying, you will die'."),
],

"2:18": [
 ((0,1,2), "YHWH Elohim said:", "wayomer YHWH 'elohim, 'and YHWH God said'."),
 ((3,4), "not good,", "lo tov, 'not good'."),
 ((5,6,7), "the human alone.", "heyot ha'adam levaddo, 'the human being alone'. 'Alone' is levad (alone); the infinitive 'being' is dropped."),
 ((8,9), "I will make him", "e'eseh lo, 'I will make for him'. 'Make him' drops the preposition's sense of 'for'."),
 ((10,11), "a help,", "ezer, 'help'. The word implies no inferiority (Ps 33:20)."),
 ((), "a counter-face.", "kenegdo, 'like/opposite him'. 'Counter-face' is a stretch: 'opposite him' is the Hebrew; 'counter-face' makes it a face. Marked; the commentary on 2:18 names it."),
],

"2:19": [
 ((0,1,2), "From the red, YHWH Elohim potted", "wayyitzer YHWH 'elohim min ha'adamah, 'and YHWH God formed from the ground'. 'Potted' is yatzar (see 2:7)."),
 ((3,4), "", "min ha'adamah, carried above."),
 ((5,6,7), "every beast of the field", "kol chayat hasadeh, 'every beast of the field'."),
 ((8,9,10,11), "and every fowl of the sky,", "ve'et kol of hashamayim, 'and every bird of the sky'."),
 ((12,13,14,15), "and brought them to the human", "vayyavei el ha'adam, 'and brought to the human'."),
 ((16,17,18), "to see what he would call them.", "lir'ot mah yiqra' lo, 'to see what he would call it'. 'Them' for the plural animals; the Hebrew has lo (singular 'it')."),
 ((19,20,21,22,23), "Whatever the human called each breathing thing,", "vekhol asher yiqra' lo ha'adam, 'and whatever the human called it'. 'Each breathing thing' supplies nefesh chayah (next)."),
 ((24,25), "", "nefesh chayah, carried above."),
 ((26,27), "that was its name.", "hu shemo, 'it is its name'. 'That was' is the English's past for the Hebrew's present."),
],

"2:20": [
 ((0,1), "The human called names:", "wayyiqra' ha'adam shemot, 'and the human called names'."),
 ((2,3), "to the cattle,", "lekhol habehemah, 'to all the cattle'. 'The' for the Hebrew 'all' (kol) is dropped; loss marked."),
 ((4,5,6), "to the fowl of the sky,", "ule'of hashamayim, 'and to the fowl of the sky'."),
 ((7,8,9), "to every beast of the field.", "ulekhol chayat hasadeh, 'and to every beast of the field'."),
 ((10,11,12,13,14), "But for the human, no counter-face was found.", "ule'adam lo matza ezer kenegdo, 'but for the human he did not find a help opposite him'. 'Counter-face' is the stretch named at 2:18."),
],

"2:21": [
 ((0,1,2,3), "YHWH Elohim dropped a deep trance on the human.", "wayyappel YHWH 'elohim tardemah 'al ha'adam, 'and YHWH God caused a deep sleep upon the human'. 'Dropped' is the stretch of nafal (fall), made into a casting."),
 ((4,), "", "tardemah, 'deep sleep', carried above."),
 ((5,6,), "", "'al ha'adam, carried above."),
 ((7,), "He slept.", "wayyishan, 'and he slept'."),
 ((8,9,10), "He took one of his sides—", "vayyiqqach achat mitzal'otav, 'and he took one of his sides'. 'Sides' keeps tzela' (rib, side)."),
 ((), "tsela—", "The Hebrew noun tsela' is repeated as a Hebrew gloss; the English puts it in the line to keep the word visible. Addition marked as a keeping, not a translation."),
 ((11,12,13), "and shut the flesh over the place.", "vayyisgor basar tachtennah, 'and he shut flesh in its place'. 'Over the place' renders tachtennah (in its place)."),
],

"2:22": [
 ((0,1,2,3), "YHWH Elohim built the side he had taken", "wayyiven YHWH 'elohim et hatzela' asher laqach, 'and YHWH God built the side that he took'. 'Built' is banah (build a house, a family); see commentary."),
 ((4,5,6,7), "the side he had taken", "et hatzela' asher laqach, 'the side that he took'. 'Side' keeps tzela'; 'rib' is the settled sense and is avoided here."),
 ((8,9), "from the human", "min ha'adam, 'from the human'."),
 ((10,), "into a woman,", "le'ishah, 'into a woman'. The English uses the Hebrew's 'ish-ah' as the noun 'woman'."),
 ((11,12,13), "and brought her to the human.", "vayevi'ehah el ha'adam, 'and brought her to the human'."),
],

"2:23": [
 ((0,1), "The human barked:", "wayomer ha'adam, 'and the human said'. 'Barked' is the register's stretch of 'said'."),
 ((2,3), "This time—at last—", "zot hapa'am, 'this time'. 'At last' is the idiomatic gloss."),
 ((4,5), "bone of my bones,", "'etzem me'atzamai, 'bone from my bones'."),
 ((6,7), "flesh of my flesh!", "uvasar mibesari, 'and flesh from my flesh'."),
 ((8,9,10), "This one: Ishah, woman,", "lezot yiqqare' ishah, 'this one shall be called woman'. 'Ishah' is kept as a transliteration because the pun needs it."),
 ((11,12,13,14), "for from Ish she was taken.", "ki me'ish luqchah zot, 'for from man she was taken, this'. 'Ish' is kept in the English for the pun."),
],

"2:24": [
 ((0,1), "Therefore:", "'al ken, 'upon this'. 'Therefore' is the English's narrator-marker, an aetiology (commentary)."),
 ((2,3), "a man leaves", "ya'azov ish, 'a man leaves'."),
 ((4,5,6,7), "father and mother,", "et 'aviv ve'et immo, 'his father and his mother'. 'His' is dropped; loss marked."),
 ((8,), "clings,", "vedavaq, 'and he clings'. 'Clings' is the plain verb; 'glues' appears below as the material sense."),
 ((9,), "to his woman;", "be'ishto, 'to his woman'."),
 ((), "glues himself", "Not in the Hebrew as a separate word: the English adds 'glues himself' for davaq's material sense (mortar). Marked as a stretch."),
 ((10,11,12), "and they are one flesh.", "vehayu le'basar ehad, 'and they shall be one flesh'. 'Are' for 'shall be' is a tense drift; marked."),
],

"2:25": [
 ((0,1,2,3), "Both bare, the human and his woman,", "vayihyu shneihem 'arumim ha'adam ve'ishto, 'and both of them were naked, the human and his wife'. 'Woman' for ishto ('his wife') is a loss of the marital sense; marked."),
 ((4,5,6), "and no shame.", "velo yitbosheshu, 'and they were not ashamed'. 'Shame' is the noun of the Hebrew's verb."),
],

"3:1": [
 ((0,), "The Hiss", "hanachash, 'the serpent'. 'The Hiss' is the stretch: the sibilance of the word (naḥash) and its near-homonyms (nechoshet, 'bronze'; nichesh, 'divined') are sounded. 'Serpent' is the settled English."),
 ((1,), "was", "hayah, 'was'."),
 ((2,3), "the crafty one—arum, shrewd and bare—", "'arum mikol. 'Crafty' is the settled gloss of 'arum; 'bare' is the same word's sense in 2:25 ('arumim). The English keeps both senses: the pun is the reason, marked in the commentary."),
 ((4,5), "of all the beasts of the field", "mikol chayat hasadeh. Settled."),
 ((6,7,8,9), "YHWH Elohim had made.", "asher 'asah YHWH 'elohim, 'which YHWH God had made'. Tense 'had made' is the English's pluperfect."),
 ((10,11), "It said to the woman:", "vayomer el ha'ishah, 'and it said to the woman'. 'Said' is the plain verb."),
 ((12,13,14), "Did Elohim really say,", "af ki 'amar 'elohim. 'Af ki is 'really?'; 'did... really say' keeps the interrogative weight. Alternative 'Is it so that' is more literal and less pointed."),
 ((15,16), "", "'amar 'elohim, carried above."),
 ((17,18,19,20,21), "you shall not eat from any tree of the garden?", "lo tokhelu mikol 'ets hagan. 'Shall not eat' is the modal rendering of lo tokhelu (future negative); 'any tree' is kol. The question mark marks the question the Hebrew builds with af."),
],

"3:2": [
 ((0,1), "The woman said to the Hiss:", "vattomer ha'ishah el hanachash. Plain."),
 ((2,3), "", "el hanachash, carried above."),
 ((4,5,6), "From the fruit of the trees of the garden,", "mipri 'ets hagan, 'from the fruit of the tree of the garden'. 'Trees' is an English pluralisation; the Hebrew is singular 'ets, a collective."),
 ((7,), "we eat.", "nokhel, 'we eat'. Plain."),
],

"3:3": [
 ((0,1,2,3,4), "But from the fruit of the tree in the middle of the garden,", "umipri ha'ets asher betokh hagan, 'and from the fruit of the tree which is in the midst of the garden'. 'But' is the contrast the English makes; 'middle' keeps betokh."),
 ((5,6), "Elohim said:", "amar 'elohim."),
 ((7,8,9), "do not eat from it,", "lo tokhelu mimmenu, 'you shall not eat from it'."),
 ((10,11,12), "do not touch it,", "velo tigge'u bo, 'nor touch it'. The English keeps 'touch'; the Hebrew's 'nagaa' is also 'strike, reach'. The prohibition is in the Hebrew here, not in 2:17 (commentary)."),
 ((13,14), "lest you die.", "pen temutun, 'lest you die'."),
],

"3:4": [
 ((0,1,2,3), "The Hiss hissed at the woman:", "vayomer hanachash el ha'ishah, 'and the serpent said to the woman'. 'Hissed' is the register's stretch of 'said', taking the name 'Hiss'."),
 ((4,5,6), "Not death. You will not die.", "lo mot temutun, 'not death you shall die'. The English splits the Hebrew: 'not death' is a fragment; 'you will not die' is the inverted sense. The paradox is the Hebrew's (commentary on 3:4)."),
],

"3:5": [
 ((0,1,2), "Elohim knows:", "ki yodea' 'elohim, 'for God knows'. The 'for' is dropped; the colon makes the snake's reason a flat statement."),
 ((3,4,5,6), "the day you eat,", "ki beyom akhlekhem mimmenu, 'that on the day you eat from it'. 'Eat' is the infinitive as the verb."),
 ((7,8), "your eyes will split open,", "venifqechu einekhem, 'and your eyes will be opened'. 'Split open' is the stretch of paqach (open the eyes)."),
 ((9,10), "and you will be like Gods,", "vihyitem ke'elohim, 'and you will be like gods'. 'Gods' is capitalised as the name the English uses for elohim here (see 1:1)."),
 ((11,12,13), "knowing good and harm.", "yodei' tov vara', 'knowing good and harm'. 'Harm' for ra' (see 2:9)."),
],

"3:6": [
 ((0,1), "The woman saw:", "vattere ha'ishah, 'and the woman saw'."),
 ((2,3,4,5), "the tree good to eat,", "ki tov ha'ets lemakhal, 'that the tree was good for food'. 'Good to eat' keeps tov and lemakhal."),
 ((6,7,8,9), "a craving for the eyes,", "vechi ta'avah hu la'einayim, 'and that it was a craving to the eyes'. 'Craving' is the stretch of ta'avah (desire)."),
 ((10,11,12), "a tree to be coveted for insight.", "venechmad ha'ets lehaskil, 'and the tree was desirable to make wise'. 'Coveted' (nechmad, cf. 2:9); 'insight' is the English for haskil (see 3:6 commentary)."),
 ((13,14), "She took from its fruit", "vattiqqach mipiryo, 'and she took from its fruit'."),
 ((15,), "and ate.", "vattokhel, 'and she ate'."),
 ((16,17,18,19), "She gave to her man with her,", "vattitten gam le'ishah immah, 'and she gave also to her husband with her'. 'Man' for 'ish (here 'ishah's husband). Loss of the marital noun marked."),
 ((20,), "and he ate.", "vayokhal, 'and he ate'."),
],

"3:7": [
 ((0,1,2), "Both their eyes split open,", "vattipaqachna einei shneihem, 'and the eyes of both were opened'. 'Split open' as at 3:5."),
 ((3,4), "and they knew", "vayeyde'u ki, 'and they knew that'."),
 ((5,6), "they were bare;", "'eiromim hem, 'naked they were'. 'Bare' carries 'eiromim (see 2:25)."),
 ((7,8,9), "they sewed fig-leaves", "vayitperu 'alei te'enah, 'and they sewed fig leaves'. 'Sewed' is tafar, 'to stitch'."),
 ((10,11,12), "and made loin-belts.", "vayya'asu lahem chagorot, 'and made for themselves girdles'. 'Loin-belts' is the stretch of chagorot (girdles, belts)."),
],

"3:8": [
 ((0,1,2), "They heard the voice of YHWH Elohim", "vayishme'u et qol YHWH 'elohim, 'and they heard the voice of YHWH God'."),
 ((3,4,5,6), "pacing in the garden", "mithallekh bagan, 'walking about in the garden'. 'Pacing' is the stretch of hithpael: walking back and forth."),
 ((7,8), "at the wind of the day;", "leruach hayom, 'at the wind of the day'. 'Cool of the day' is the settled gloss and is rejected; ruach is wind."),
 ((9,10,11), "the human and his woman hid", "vayyithchabe ha'adam ve'ishto, 'and the human and his wife hid themselves'."),
 ((12,13,14), "from the face of YHWH Elohim", "mipenei YHWH 'elohim, 'from the face of YHWH God'."),
 ((15,16,17), "among the trees of the garden.", "betokh 'ets hagan, 'in the midst of the tree of the garden'. 'Trees' is a pluralisation."),
],

"3:9": [
 ((0,1,2,3,4), "YHWH Elohim called to the human:", "vayiqra YHWH 'elohim el ha'adam, 'and YHWH God called to the human'."),
 ((5,6), "", "vayomer lo, 'and said to him'. Carried by the colon."),
 ((7,), "Ayyekka—where are you?", "ayyekka, 'where are you?'. A rare form; the English keeps the word and glosses it. The question is God's."),
],

"3:10": [
 ((0,1), "He said:", "vayomer, 'and he said'."),
 ((2,3,4), "I heard your voice in the garden;", "et qolekha shamati bagan, 'your voice I heard in the garden'."),
 ((5,), "I shook,", "va'ira, 'and I feared'. 'Shook' is the stretch of ira (fear, awe)."),
 ((6,7,8), "for I am bare,", "ki 'eirom anokhi, 'for naked I am'."),
 ((9,), "and I hid.", "va'ei'chaveh, 'and I hid'."),
],

"3:11": [
 ((0,1), "He said:", "vayomer."),
 ((2,3), "Who told you you were bare?", "mi higgid lekha ki 'eirom atah, 'who told you that naked you are'. 'Told you' for higgid lekha; 'bare' for 'eirom."),
 ((4,5,6), "", "ki 'eirom atah, carried above."),
 ((7,8,9,10,11,12,13,14), "From the tree I charged you about—did you eat?", "hamin ha'ets asher tsiviti'kha livlti akhol mimmenu akhalta, 'from the tree that I charged you not to eat from, did you eat?'. 'Charged you about' is the English for tsivah; 'did you eat' is the interrogative hamin (the question marker)."),
],

"3:12": [
 ((0,1), "The human said:", "vayomer ha'adam."),
 ((2,3,4,5), "The woman you set with me—", "ha'ishah asher natatta immadi, 'the woman whom you gave with me'. 'Set' for natatta (gave, placed)."),
 ((6,7,8), "she handed me", "hi natenah li, 'she gave to me'. 'Handed' is the physical stretch of natan."),
 ((9,10), "from the tree,", "min ha'ets, 'from the tree'."),
 ((11,), "and I ate.", "va'okhel, 'and I ate'."),
],

"3:13": [
 ((0,1,2,3), "YHWH Elohim said to the woman:", "vayomer YHWH 'elohim la'ishah, 'and YHWH God said to the woman'."),
 ((4,5,6), "What is this you have done?", "mah zot 'asit, 'what is this you did'. 'Have done' for the perfect."),
 ((7,8), "The woman said:", "vattomer ha'ishah."),
 ((9,10), "The Hiss snared me,", "hanachash hishi'ani, 'the serpent deceived me'. 'Snared' is the stretch of nasha' (deceive, cause to forget). Alternative 'deceived' is the LXX."),
 ((11,), "and I ate.", "va'okhel."),
],

"3:14": [
 ((0,1,2,3,4,5), "YHWH Elohim said to the Hiss:", "vayomer YHWH 'elohim el hanachash, 'and YHWH God said to the serpent'. The paragraph mark (3) is not rendered."),
 ((6,7,8), "Because you did this—", "ki 'asita zot, 'because you did this'."),
 ((9,10), "cursed you are,", "'arur atah, 'cursed are you'. The English inverts the order."),
 ((11,12,13,14,15), "out of all the cattle,", "mikol habehemah umikol chayat hasadeh, 'out of all the cattle and out of all the beasts of the field'. Split across two lines; 'out of all' is repeated in the English."),
 ((16,17,18), "On your belly you will crawl,", "al gechonkha telekh, 'upon your belly you shall walk'. 'Crawl' is the stretch of halakh (walk). The English makes the animal's motion the curse."),
 ((19,20,21,22,23), "and dust you will eat all the days of your life.", "vafar tokhal kol yemei chayyekha, 'and dust you shall eat all the days of your life'. 'Dust' for afar."),
],

"3:15": [
 ((0,1,2), "Enmity I will set", "ve'eivah ashit, 'and enmity I will set'."),
 ((3,4,5), "between you and the woman,", "beinkha uvein ha'ishah, 'between you and the woman'."),
 ((6,7,8,9), "between your seed and her seed:", "uvein zar'akha uvein zar'ah, 'between your seed and her seed'. 'Seed' is zera', collective."),
 ((10,11,12), "he—it—will crush your head;", "hu yeshufkha rosh, 'it/he will crush you on the head'. 'He—it' keeps hu's ambiguity; 'crush' is the stretch of shuf (bruise, lie in wait)."),
 ((13,14,15), "you will bruise its heel.", "ve'atah teshufenu aqev, 'and you will bruise him on the heel'. 'Bruise' is the same verb as 'crush' in the Hebrew; the English uses two verbs and marks it."),
],

"3:16": [
 ((0,1,2), "To the woman he said:", "'el ha'ishah amar, 'to the woman he said'."),
 ((3,4), "I will multiply, multiply", "harbah 'arbeh, 'multiplying I will multiply'. Infinitive absolute, kept as a doubled verb."),
 ((5,6), "your pain and your groaning.", "'itstsavonekh vehe'ronekh, 'your toil and your conception'. 'Groaning' is the stretch of heron (conception, pregnancy) toward the sound of labour. Alternative 'conception' is the literal."),
 ((7,8,9), "In pain you will bear children.", "be'etsev telidi vanim, 'in pain you will bear children'."),
 ((10,11,12,13,14,15), "Toward your man your craving, and he will rule you.", "ve'el ishekh teshuqatekh vehu yimshol bakh, 'and toward your man your craving, and he will rule over you'. 'Craving' is teshuqah, the word of 4:7 as well."),
],

"3:17": [
 ((0,1,2), "To the human he said:", "ule'adam amar ki, 'and to the human he said, because'."),
 ((3,4,5,6), "Because you listened to your woman's voice", "shama'ta lekol ishtekha, 'you listened to the voice of your wife'. 'Woman's' for 'ishtekha, 'your wife'. Loss marked."),
 ((7,8,9,10,11), "and ate from the tree I charged you about—", "vatokhal min ha'ets asher tsiviti'kha lemor, 'and you ate from the tree which I charged you, saying'. 'About' is the English for tsivah plus lemor."),
 ((12,13,14), "'do not eat from it'—", "lo tokhal mimmenu, 'you shall not eat from it'."),
 ((15,16), "the ground is cursed", "arurah ha'adamah, 'cursed is the ground'. Inverted in the English."),
 ((17,), "for your sake.", "ba'avurekha, 'for your sake'."),
 ((18,19,20,21,22), "In pain you will eat from it all the days of your life.", "be'itstsavon tokhelenah kol yemei chayyekha, 'in pain you shall eat it all the days of your life'. 'From it' is the English for the object pronoun."),
],

"3:18": [
 ((0,1), "Thorn and thistle", "vekotz vedardar, 'and thorn and thistle'. 'Thistle' is the rough sound of dardar."),
 ((2,3), "it will sprout for you;", "tatzmiach lakh, 'it will sprout for you'."),
 ((4,5,6,7), "you will eat the grass of the field.", "ve'akhalta et 'esev hasadeh, 'and you shall eat the herb of the field'. 'Grass' for 'esev (herb)."),
],

"3:19": [
 ((0,1,2), "By the sweat of your face you will eat bread", "bezei'at appekha tokhal lechem, 'by the sweat of your nostrils/face you shall eat bread'. 'Face' is the reading of appayim here; 'nostrils' (literal) and 'anger' are kept in the commentary."),
 ((3,4,5,6,7), "until you return to the red—", "'ad shuvekha el ha'adamah, 'until your return to the ground'. 'The red' is adamah (see 1:25)."),
 ((8,9,10), "for from it you were taken.", "ki mimmenah luqqachta, 'for from it you were taken'."),
 ((11,12,13), "Dust you are;", "ki 'afar atah, 'for dust you are'."),
 ((14,15,16), "to dust you will return.", "ve'el 'afar tashuv, 'and to dust you shall return'."),
],

"3:20": [
 ((0,1,2,3), "The human named his woman", "vayyiqra ha'adam shem ishto, 'and the human called the name of his wife'."),
 ((4,), "Chavah—Living—", "chavah, 'Eve'. 'Living' is the English gloss from chayah (live). The name is a verb in disguise."),
 ((5,6,7,8,9,10), "for she became mother of all the living.", "ki hi hayatah em kol chai, 'for she was mother of all the living'. 'Became' for hayatah (was)."),
],

"3:21": [
 ((0,1,2), "YHWH Elohim made", "vayya'as YHWH 'elohim, 'and YHWH God made'."),
 ((3,4), "for the human and his woman", "le'adam ulishto, 'for the human and for his wife'."),
 ((5,6), "tunics of hide,", "ketonot or, 'tunics of skin'. 'Hide' is the register's choice for or (skin, pelt)."),
 ((7,), "and dressed them.", "vayalbishem, 'and clothed them'. 'Dressed' is the plainer English."),
],

"3:22": [
 ((0,1,2,3), "YHWH Elohim said:", "vayomer YHWH 'elohim, 'and YHWH God said'."),
 ((4,), "Look—", "hen, 'behold'."),
 ((5,6), "the human has become", "ha'adam hayah, 'the human was'. 'Has become' is the English perfect for hayah."),
 ((7,8), "like one of us,", "ke'echad mimmenu, 'like one of us' (or 'of it'). 'Us' is kept as the plural reading."),
 ((9,10,11), "knowing good and harm.", "ladaat tov vara', 'to know good and harm'."),
 ((12,13,14), "Now lest he send out his hand,", "ve'attah pen yishlach yado, 'and now lest he send out his hand'. 'Send out' is the English for shalach."),
 ((15,16,17,18,19,20), "take also from the tree of lives,", "velaqach gam me'ets hachayyim, 'and take also from the tree of lives'."),
 ((21,22,23), "eat, and live—forever.", "ve'akhal vachay le'olam, 'and eat, and live forever'."),
],

"3:23": [
 ((0,1,2), "YHWH Elohim sent him out", "vayshallehu YHWH 'elohim, 'and YHWH God sent him'. 'Out' is added; the Hebrew's piel carries the sending-away."),
 ((3,4), "from the garden of delight,", "migan 'eden, 'from the garden of Eden'. 'Delight' is the English reading of Eden."),
 ((5,6,7), "to serve the red", "la'avod et ha'adamah, 'to serve the ground'. 'Serve' is the verb of slavery (see 2:15)."),
 ((8,9,10), "from which he was taken.", "asher lukkach mishsham, 'which he was taken from there'."),
],

"3:24": [
 ((0,1,2), "He drove the human out.", "vaygaresh et ha'adam, 'and he drove out the human'. 'Drove out' is garash (the verb of divorce, Lev 21:7)."),
 ((3,4,5,6), "At the east of the garden of delight he set", "vayyashken miqqedem legan 'eden, 'and he set at the east of the garden of Eden'. 'Set' for shakan (settle, place)."),
 ((7,8), "the cherubim,", "et hakerubim, 'the cherubim'."),
 ((9,10,11,12), "and the flame of the turning blade,", "ve'et lahat hacherev hamitpakhet, 'and the flame of the sword which turns'. 'Turning blade' is the English reading of mitpakhet."),
 ((13,14,15,16,17), "to guard the road to the tree of lives.", "lishmor et derekh 'ets hachayyim, 'to guard the way of the tree of lives'. 'Road' is the stretch of derekh (way)."),
],

"4:1": [
 ((0,1,2,3,4), "Now the human knew Chavah his woman;", "vehaadam yada' et chavah ishto, 'and the human knew Eve his wife'. 'Knew' is yada'; the sexual sense is kept by the context (commentary)."),
 ((5,6), "she conceived and bore Qayin,", "vattaharr vattelad et qayin, 'and she conceived and bore Qayin'."),
 ((7,8), "", "et qayin, carried above."),
 ((9,), "and said:", "vattomer, 'and she said'."),
 ((10,11,12,13), "I have gotten a man—YHWH.", "qaniti ish et YHWH, 'I have gotten a man with YHWH'. 'Gotten' is the stretch of qanah (acquire, create). 'YHWH' as apposition is the reading kept; 'with YHWH' is the alternative."),
],

"4:2": [
 ((0,1,2,3,4,5), "She bore again: his brother Hevel.", "vattosef lalledet et 'achiv et hevel, 'and she added to bear his brother, Hevel'. 'Bore again' is the English for tosef (add) with lalledet (to bear)."),
 ((6,7), "", "vayehi hevel, 'and Hevel was'. Carried into 'Hevel, herder'."),
 ((8,9), "Hevel, herder of flocks.", "ro'eh tzon, 'a shepherd of flocks'. 'Herder' is the plain English for ro'eh."),
 ((10,11,12,13), "Qayin, worker of the red.", "veqayin hayah oved adamah, 'and Qayin was a worker of the ground'. 'The red' for adamah."),
],

"4:3": [
 ((0,1,2), "At the end of days,", "vayehi miqqetz yamim, 'and it was at the end of days'. 'At the end' is miqqetz (from the cut-off)."),
 ((3,4,5,6), "Qayin brought from the fruit of the red", "vayyavi qayin mipri ha'adamah, 'and Qayin brought from the fruit of the ground'."),
 ((7,8), "a gift to YHWH.", "minchah layhvh, 'an offering to YHWH'. 'Gift' is the stretch of minchah (offering)."),
],

"4:4": [
 ((0,1,2,3), "And Hevel too:", "vehevel hevi gam hu, 'and Hevel too, he brought'."),
 ((4,5), "from the firstborn of his flock,", "mibekhorot tzono, 'from the firstborn of his flock'."),
 ((6,), "from their fat,", "umechelbehen, 'and from their fat'. The richest portion."),
 ((7,8), "and YHWH fixed his eye", "vayyisha' YHWH, 'and YHWH looked'. 'Fixed his eye' is the stretch of sha'a (gaze)."),
 ((9,10), "on Hevel", "el hevel, 'to Hevel'."),
 ((11,12), "and his gift.", "ve'el minchato, 'and to his offering'."),
],

"4:5": [
 ((0,1,2,3), "But to Qayin and his gift he did not look.", "ve'el qayin ve'el minchato lo sha'ah, 'but to Qayin and to his offering he did not look'. 'Did not look' for lo sha'ah."),
 ((4,), "", "lo, carried above."),
 ((5,), "", "sha'ah, carried above."),
 ((6,7), "Qayin burned,", "vayyichar leqayin, 'and it burned for Qayin'. 'Burned' is the stretch of charah (be hot, angry)."),
 ((8,), "exceedingly,", "me'od, 'exceedingly'."),
 ((9,10), "and his face fell.", "vayyippelu panav, 'and his face fell'."),
],

"4:6": [
 ((0,1,2,3), "YHWH said to Qayin:", "vayomer YHWH el qayin, 'and YHWH said to Qayin'."),
 ((4,5), "Why do you burn?", "lamah charah lakh, 'why did it burn for you'. 'Do you burn' is the English for charah in the second person."),
 ((6,7,8,9), "Why has your face fallen?", "velamah nafelu panekha, 'and why has your face fallen'."),
],

"4:7": [
 ((0,1), "Is it not so?", "halo 'im, 'is it not so, if'. The English makes the interrogative a rhetorical 'not so'."),
 ((2,3), "If you do well,", "teitiv se'et, 'you will do well, a lifting'. 'If you do well' for 'im teitiv."),
 ((4,5,6), "a lifting of the face.", "veim lo teitiv, 'and if you do not do well'. Split into two lines; 'a lifting of the face' is se'et panim (see 4:7 commentary)."),
 ((7,8), "If you do not do well,", "lappetach chattat, 'at the door, sin'. The English keeps the conditional."),
 ((9,), "at the door a sin crouches—", "rovets, 'crouching'. 'Crouches' is the stretch of rovets (lying in wait)."),
 ((10,11), "its craving is for you;", "ve'elekha teshuqato, 'and toward you its craving'. 'Craving' keeps teshuqah from 3:16."),
 ((12,13,14), "but you, rule it.", "ve'attah timshol bo, 'and you, rule over it'. 'Rule it' is the imperative of the Hebrew future."),
],

"4:8": [
 ((0,1,2,3), "Qayin spoke to Hevel his brother—", "vayomer qayin el hevel 'achiv, 'and Qayin said to Hevel his brother'. The Hebrew gives no content: the dash is in the text."),
 ((4,5,6,7), "and it was, in the field,", "vayehi bihyotam basadeh, 'and it was, when they were in the field'."),
 ((8,9,10,11,12), "that Qayin reared on Hevel his brother", "vayyaqom qayin el hevel 'achiv, 'and Qayin rose up against Hevel his brother'. 'Reared on' is the stretch of qum (rise)."),
 ((13,), "and struck him dead.", "vayyahargehu, 'and killed him'. 'Struck him dead' is the register's word for harag."),
],

"4:9": [
 ((0,1,2,3), "YHWH said to Qayin: Where is Hevel your brother?", "vayomer YHWH el qayin ei hevel 'achikha, 'and YHWH said to Qayin, where is Hevel your brother'."),
 ((4,5,6), "", "ei hevel 'achikha, carried above."),
 ((7,8,9), "He said: I do not know.", "vayomer lo yada'ti, 'and he said: I did not know'."),
 ((10,11,12), "Am I my brother's keeper?", "hasomer achi anokhi, 'am I the keeper of my brother?'. 'Keeper' is shomer (see 2:15 'keep')."),
],

"4:10": [
 ((0,1), "He said: What have you done?", "vayomer mah 'asita, 'and he said: what did you do'."),
 ((2,3,4), "The bloods of your brother", "qol demei 'achikha, 'the voice of your brother's bloods'. The plural 'bloods' is kept (commentary)."),
 ((5,6), "cry", "tso'aqim, 'crying out'."),
 ((7,8,9), "to me from the red.", "elai min ha'adamah, 'to me from the ground'."),
],

"4:11": [
 ((0,1,2), "Now: cursed are you", "ve'attah 'arur atah, 'and now cursed are you'."),
 ((3,4), "from the red,", "min ha'adamah, 'from the ground'."),
 ((5,6), "which gaped its mouth", "asher patzta 'et piha, 'which opened its mouth'. 'Gaped' is the stretch of patzah (open)."),
 ((7,8,9), "to take", "laqachat, 'to take'."),
 ((10,11,12), "your brother's bloods", "'et demei 'achikha, 'the bloods of your brother'."),
 ((13,), "from your hand.", "miyyadekha, 'from your hand'."),
],

"4:12": [
 ((0,1,2,3), "When you work the red,", "ki ta'avod 'et ha'adamah, 'when you work the ground'. 'Work' is the English of 'avod (serve, work)."),
 ((4,5,6,7,8), "it will not add its strength to you.", "lo tosef tet kocha lakh, 'it will not add to give its strength to you'. 'Add' is yasaf; 'its strength' is ko'ach."),
 ((9,10), "A reeler, a wanderer,", "na' vanad, 'staggering and wandering'. Two sounds of motion; 'reeler' and 'wanderer' are the English stretch."),
 ((11,12), "you will be on the earth.", "tihyeh ba'arets, 'you will be in the earth'."),
],

"4:13": [
 ((0,1,2,3), "Qayin said to YHWH:", "vayomer qayin el YHWH, 'and Qayin said to YHWH'."),
 ((4,5), "My guilt is greater", "gadol 'avoni, 'great is my guilt'. 'Greater' is the comparative English of gadol."),
 ((6,), "than I can bear,", "minnesso, 'from lifting/bearing'. 'Than I can bear' is the stretch: nasa' is carry and forgive."),
 ((), "greater than can be lifted.", "Not a separate token: the second line repeats the Hebrew's double sense of nasa' (carry, forgive) in the English as 'lifted'. Addition marked; the commentary names the double sense."),
],

"4:14": [
 ((0,1,2), "Look—you drive me out today", "hen gerashta 'oti hayyom, 'look, you have driven me out today'. 'Drive' for garash (divorce, see 3:24)."),
 ((3,4,5,6), "from the face of the red.", "me'al penei ha'adamah, 'from upon the face of the ground'. 'The red' for adamah."),
 ((7,8,9), "From your face I shall be hidden;", "umippanekha essater, 'and from your face I shall be hidden'."),
 ((10,11,12,13), "I shall be a reeler and wanderer on the earth,", "vehayiti na' vanad ba'arets, 'and I shall be staggering and wandering in the earth'."),
 ((14,15,16), "and whoever finds me will kill me.", "vehayah kol motz'i yahargeni, 'and whoever finds me will kill me'. 'Whoever' for kol; 'kill' is harag."),
],

"4:15": [
 ((0,1,2), "YHWH said to him:", "vayomer lo YHWH, 'and YHWH said to him'."),
 ((3,), "Not so—therefore—", "lakhen, 'therefore' (or 'not so', lo ken). Both readings are given: the dash lets the English reverse."),
 ((4,5,6,7,8), "whoever kills Qayin will be paid back sevenfold.", "kol horeg qayin shivatayim yukkam, 'whoever kills Qayin, sevenfold shall be avenged'. 'Paid back' for yukkam (avenged)."),
 ((9,10,11,12), "YHWH set a mark on Qayin,", "vayyasem YHWH leqayin 'ot, 'and YHWH set for Qayin a sign'. 'Mark' is the stretch of ot (sign)."),
 ((13,14,15,16,17), "lest anyone who found him strike him.", "levilti hakkot oto kol motz'o, 'lest anyone who found him strike him'. 'Strike' is the English for hakkot (to smite)."),
],

"4:16": [
 ((0,1,2,3), "Qayin went out from the face of YHWH", "vayyetze qayin millifnei YHWH, 'and Qayin went out from before YHWH'. 'Face' for lifnei (before)."),
 ((4,5), "and settled in the land of Nod—", "vayyeshev be'eretz nod, 'and he settled in the land of Nod'."),
 ((6,), "Wandering—", "nod, 'wandering'. The English glosses the name as the word it is; the pun is the reason."),
 ((7,8), "east of Eden.", "qidmat 'eden, 'east of Eden'."),
],

"4:17": [
 ((0,1,2,3), "Qayin knew his woman;", "vayeda qayin et ishto, 'and Qayin knew his wife'. 'Knew' is yada' (see 4:1)."),
 ((4,5,6,7), "she conceived and bore Chanokh.", "vattaharr vattelad et chanokh, 'and she conceived and bore Enoch'."),
 ((8,9,10), "He was building a city,", "vayehi bonneh 'ir, 'and he was building a city'."),
 ((11,12,13), "and named the city", "vayiqra' shem ha'ir, 'and he called the name of the city'."),
 ((14,15,16), "after his son: Chanokh.", "kishem beno chanokh, 'after the name of his son, Chanokh'."),
],

"4:18": [
 ((0,1,2,3), "To Chanokh was born Irad;", "vayyiwwaled lechanokh et irad, 'there was born to Enoch Irad'. Passive niphal; 'was born' keeps it."),
 ((4,5,6,7), "Irad fathered Mechuyael;", "veirad yalad et mechuyael, 'and Irad fathered Mechuyael'. The English drops 'and'."),
 ((8,9,10,11), "Mechuyael fathered Methushael;", "umechiyael yalad et methushael, 'and Mechiyael fathered Methushael'. The Hebrew spells the name Mechuyael once and Mechiyael here (commentary: read as one name)."),
 ((12,13,14,15), "Methushael fathered Lamech.", "umethushael yalad et lamech, 'and Methushael fathered Lamech'. The chain ends on Lamech."),
],

}
