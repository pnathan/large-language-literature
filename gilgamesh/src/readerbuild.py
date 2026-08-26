# -*- coding: utf-8 -*-
import json, re, html
from meta import TITLES, HEADNOTES, APPARATUS
from perimeta import PERICOPES, APP_SIDE, EXTRA, SPLITS
from resmeta import RES, FIGCAP
import base64

TABLETS = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

NAMES = ['gilgāmeš','enkīdu','šamhat','šamkat','uruk','eanna','ištar','ānim','ānu','anu','antu','ellil','enlil','ēa','aruru',
 'rīmat-ninsun','ninsunna','ninsumuna','ninsun','lugalbanda','šamšim','šamšu','šamaš','ayya','humbāba','huwāwa','adad','sîn',
 'nudimmud','bēlet-ilī','ninurta','šakkan','irnini','ningišzida','ereškigal','bēlet-ṣēri','irkalla','etana','namtar',
 'hušbiša','qāssa-ṭābat','ninšuluhhatum','ninšuluhha','bibbu','dumuzi-abzu','dumuzi','silili','išullānî','išullānu','išhara',
 'ūta-napišti','ūta-naʾištim','ubār-tutu','ubar-tutu','ur-šanabi','ur-šanābi','sursunābu','šiduri','māšu','māši','nimuš',
 'labnānu','labnān','sirara','saria','ebabbarra','ēgalmah','nippurim','nippuri','nippur','larsa','purattim','purattu','puratti',
 'ulāya','šuruppak','atra-hasīs','atar-hasīs','puzur-ellil','šullat','haniš','errakal','erra','mammītu',
 'anunnakkū','anunnakū','enunnakkī','enunakkī','anunnak','igīgī','arallê','ēkur','ekur','erīdu','ningal','nergal','ninazu',
 'marūtuk','anzâm','anzâ','anzî','anzû','nissaba','māt-ibla','hamran','wēr','irninnī']
NAMES = sorted(set(NAMES), key=len, reverse=True)

def norm_line(line):
    toks = line['variants'][0].get('reconstructionTokens', [])
    s = ' '.join(t.get('value','') for t in toks)
    for a,b in ((' || ',' '),(' | ',' '),('%n ',''),('(|)',''),('(||)',''),('|',''),('%sb ','')):
        s = s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()

def cap_names(s):
    for n in NAMES:
        s = re.sub(r'(?<![\w\-])'+re.escape(n), lambda m: n[0].upper()+n[1:], s)
    return s

def bracketize(s):
    s = html.escape(s, quote=False)
    out, open_br = [], False
    for ch in s:
        if ch == '[':
            out.append('<span class="br">['); open_br = True
        elif ch == ']':
            if open_br: out.append(']</span>'); open_br = False
            else: out.append('<span class="br">]</span>')
        else: out.append(ch)
    if open_br: out.append('</span>')
    return ''.join(out)

def load_tr(path):
    d = {}
    for ln in open(path):
        ln = ln.rstrip('\n')
        if not ln.strip(): continue
        num, _, txt = ln.partition('\t')
        d[num.strip()] = txt
    return d

def first_int(numstr):
    m = re.match(r'^(\d+)', numstr)
    return int(m.group(1)) if m else None

def vrow(num, akk, en, sups=''):
    return (f'<div class="v"><span class="n">{html.escape(num)}</span>'
            f'<span class="akk">{bracketize(akk)}</span>'
            f'<span class="en">{bracketize(en)}{sups}</span></div>')

# ---------------- load ----------------
SB   = {t: json.load(open(f'SB_{t}.json'))  for t in TABLETS}
SBTR = {t: load_tr(f'tr_{t}.tsv')           for t in TABLETS}
OBJ  = {k: json.load(open(f'OB_{k}.json'))  for k in ['II','III','Ishchali','VABM']}
OBTR = {k: load_tr(f'obtr_{k}.tsv')         for k in ['II','III','Ishchali','VABM']}

def pick_rows(data, tr, numbers):
    idx = {l['number']: l for l in data['lines']}
    rows = []
    for n in numbers:
        if n == 'ELL':
            rows.append('<div class="gap">⸻ ⸻</div>'); continue
        if n in idx:
            rows.append(vrow(n, cap_names(norm_line(idx[n])), tr.get(n,'[ ... ]')))
    return rows

def split_html(sp):
    ll, lk, ln = sp['left']; rl, rk, rn = sp['right']
    lrows = pick_rows(OBJ[lk], OBTR[lk], ln)
    rrows = pick_rows(SB[rk], SBTR[rk], rn)
    return f'''
<div class="parting">
  <div class="parting-rule"><span>𒀸</span> THE TWO RECENSIONS <span>𒀸</span></div>
  <h3>{sp['title']}</h3>
  <p class="headnote">{sp['blurb']}</p>
  <div class="cmp-grid">
    <div class="cmp-col ob"><div class="cmp-label">{ll}</div><div class="verses cmpv">{''.join(lrows)}</div></div>
    <div class="cmp-col"><div class="cmp-label">{rl}</div><div class="verses cmpv">{''.join(rrows)}</div></div>
  </div>
  <div class="parting-rule bottom"><span>𒀸</span></div>
</div>'''

# ---------------- notes ----------------
def tablet_notes(tab):
    notes = []
    app = APPARATUS.get(tab, [])
    sides = APP_SIDE.get(tab, [])
    for (head, text), (anchor, side) in zip(app, sides):
        lemma = head.split('—',1)[-1].strip() if '—' in head else head
        notes.append(dict(anchor=anchor, side=side, lemma=lemma, ref=head.split('—')[0].strip(), text=text, kind='n'))
    for (anchor, side, lemma, text) in EXTRA.get(tab, []):
        notes.append(dict(anchor=anchor, side=side, lemma=lemma, ref='', text=text, kind='n'))
    for (anchor, lemma, text) in RES.get(tab, []):
        notes.append(dict(anchor=anchor, side='R', lemma=lemma, ref='', text=text, kind='res'))
    return notes

FIGURLS = {'I': 'https://commons.wikimedia.org/wiki/Special:FilePath/Warka%20Mask%2C%20Iraq%20Museum.jpg?width=880', 'II': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ebih-Il%20Louvre%20AO17551%20n01.jpg?width=880', 'IV': 'https://commons.wikimedia.org/wiki/Special:FilePath/Forest%20of%20The%20cedars%20of%20God.jpg?width=880', 'V': 'https://commons.wikimedia.org/wiki/Special:FilePath/Terracotta%20mask%20of%20Humbaba%20%28Huwawa%29.%20From%20Ur%2C%20Iraq.%20Old-Babylonian%20period%202004-1595%20BCE.%20Sulaymaniyah%20Museum%2C%20Iraq.jpg?width=880', 'VI': 'https://commons.wikimedia.org/wiki/Special:FilePath/British%20Museum%20Queen%20of%20the%20Night.jpg?width=880', 'VIII': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bull%20Headed%20Lyre%20of%20Ur.jpg?width=880', 'XI': 'https://commons.wikimedia.org/wiki/Special:FilePath/British%20Museum%20Flood%20Tablet%201.jpg?width=880'}
import os
EMBED = os.environ.get('EMBED_PLATES','1') == '1'
def figure_html(tab):
    if tab not in FIGCAP: return ''
    f, alt, cap, credit = FIGCAP[tab]
    if EMBED:
        b64 = base64.b64encode(open(f,'rb').read()).decode()
        srcv = f'data:image/jpeg;base64,{b64}'
    else:
        srcv = FIGURLS[tab]
    return (f'<figure class="plate"><img src="{srcv}" alt="{alt}" loading="lazy">'
            f'<figcaption>{cap}<span class="credit">{credit}</span></figcaption></figure>')

# ---------------- pericope build ----------------
def build_tablet(tab):
    lines = SB[tab]['lines']
    tr = SBTR[tab]
    bounds = PERICOPES[tab]
    starts = [b[0] for b in bounds]
    caps = {b[0]: b[1] for b in bounds}
    # slice
    peris, cur, bi = [], None, 0
    for line in lines:
        fi = first_int(line['number'])
        while bi < len(starts) and fi is not None and fi >= starts[bi]:
            if cur: peris.append(cur)
            cur = dict(start=starts[bi], cap=caps[starts[bi]], lines=[])
            bi += 1
            # absorb any skipped boundaries (broken text): keep only latest
        if cur is None:
            cur = dict(start=starts[0], cap=caps[starts[0]], lines=[]); bi = 1
        cur['lines'].append(line)
    if cur: peris.append(cur)

    notes = tablet_notes(tab)
    splits = {sp['after_start']: sp for sp in SPLITS if sp['tab'] == tab}

    out = []
    label, title = TITLES[tab]
    out.append(f'''<section class="tablet" id="t{tab}">
<div class="tablet-head"><span class="tab-label">{label}</span><h2>{title}</h2></div>
<p class="headnote tablet-note">{HEADNOTES[tab]}</p>{figure_html(tab)}''')

    for p in peris:
        lo = p['start']
        hi_ints = [first_int(l['number']) for l in p['lines'] if first_int(l['number']) is not None]
        hi = max(hi_ints) if hi_ints else lo
        pn = [n for n in notes if n['anchor'].isdigit() and lo <= int(n['anchor']) <= hi]
        pn.sort(key=lambda n: int(n['anchor']))
        letters = {}
        li = 0
        for n in pn:
            if n.get('kind')=='res':
                n['letter'] = '≈'
            else:
                n['letter'] = chr(ord('a')+li); li += 1
            letters.setdefault(n['anchor'], []).append((n['letter'], n.get('kind','n')))
        rows, prev, marked = [], None, set()
        for line in p['lines']:
            num = line['number']; fi = first_int(num)
            if prev is not None and fi is not None and fi - prev > 1:
                a,b = prev+1, fi-1
                span = f'line {a}' if a==b else f'lines {a}–{b}'
                rows.append(f'<div class="gap">⸻ {span} lost or too broken to carry ⸻</div>')
            if fi is not None: prev = fi
            sups = ''
            if fi is not None and str(fi) in letters and str(fi) not in marked:
                sups = ''.join(f'<sup class="anc{" res" if kd=="res" else ""}">{l}</sup>' for l,kd in letters[str(fi)])
                marked.add(str(fi))
            rows.append(vrow(num, cap_names(norm_line(line)), tr.get(num,'[ ... ]'), sups))
        def margin(side):
            ms = [n for n in pn if n['side']==side]
            if not ms: return ''
            return ''.join(
                f'<div class="mn{" res" if n.get("kind")=="res" else ""}">'
                f'<span class="anc{" res" if n.get("kind")=="res" else ""}">{n["letter"]}</span><b>{n["lemma"]}</b>'
                + (f'<span class="mref">{n["ref"]}</span>' if n['ref'] else '')
                + f'<span class="mtext">{n["text"]}</span></div>' for n in ms)
        out.append(f'''<div class="daf">
<div class="m m-l">{margin('L')}</div>
<div class="body"><div class="peri-cap">{tab} {lo}–{hi} · {p['cap']}</div><div class="verses">{''.join(rows)}</div></div>
<div class="m m-r">{margin('R')}</div>
</div>''')
        if lo in splits:
            out.append(split_html(splits[lo]))
    out.append('</section>')
    return '\n'.join(out)

# ---------------- css ----------------
CSS = open('style.css').read().replace('</style>','''
main{max-width:1480px;}
.gap{grid-column:1/-1;text-align:center;color:#8b93b8;font-family:'Alegreya Sans',sans-serif;font-size:.75rem;letter-spacing:.12em;padding:.8rem 0;text-transform:uppercase;}
.tablet{margin:5rem 0;}
.tablet-head{display:flex;align-items:baseline;gap:1rem;border-bottom:1px solid rgba(201,163,74,.35);padding-bottom:.4rem;margin-bottom:1rem;max-width:1480px;}
.tab-label{font-family:'Alegreya Sans',sans-serif;font-size:.8rem;letter-spacing:.25em;text-transform:uppercase;color:#c9a34a;white-space:nowrap;}
.tablet-head h2{margin:0;border:none;padding:0;}
.headnote{font-family:'Alegreya Sans',sans-serif;font-size:.92rem;line-height:1.65;color:#b7bdd9;max-width:66ch;margin:0 0 1.6rem;}
.tablet-note{margin-left:auto;margin-right:auto;}
nav.toc{display:flex;flex-wrap:wrap;gap:.5rem .9rem;justify-content:center;margin:2.2rem auto 0;max-width:700px;}
nav.toc a{font-family:'Alegreya Sans',sans-serif;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:#c9a34a;text-decoration:none;border:1px solid rgba(201,163,74,.35);padding:.3rem .7rem;border-radius:2px;}
nav.toc a:hover{background:rgba(201,163,74,.12);}
/* --- the daf --- */
.daf{display:grid;grid-template-columns:15rem minmax(0,1fr) 15rem;gap:0 1.6rem;margin:2.4rem 0;align-items:start;}
.daf .body{min-width:0;}
.peri-cap{font-family:'Alegreya Sans',sans-serif;font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:#c9a34a;border-bottom:1px dotted rgba(201,163,74,.4);padding-bottom:.25rem;margin-bottom:.7rem;}
.m{font-family:'Alegreya Sans',sans-serif;color:#a9b0d0;position:sticky;top:1.2rem;}
.m-l{font-size:.78rem;line-height:1.5;text-align:right;border-right:1px solid rgba(201,163,74,.22);padding-right:1rem;}
.m-r{font-size:.84rem;line-height:1.58;border-left:1px solid rgba(201,163,74,.22);padding-left:1rem;}
.mn{margin:0 0 1rem;}
.mn b{color:#e0c98b;font-weight:600;display:inline;}
.mn .anc{color:#c9a34a;font-size:.7em;vertical-align:super;margin-right:.3em;}
.mn .mref{display:block;color:#8b93b8;font-size:.85em;letter-spacing:.08em;}
.mn .mtext{display:block;margin-top:.15rem;}
sup.anc{color:#c9a34a;font-size:.62em;margin-left:.18em;font-family:'Alegreya Sans',sans-serif;}
/* --- partings (split spreads) --- */
.parting{margin:3.2rem 0;padding:0 0 .4rem;}
.parting-rule{display:flex;align-items:center;gap:1rem;color:#c9a34a;font-family:'Alegreya Sans',sans-serif;font-size:.72rem;letter-spacing:.3em;justify-content:center;margin-bottom:1.4rem;}
.parting-rule::before,.parting-rule::after{content:'';flex:1;border-top:1px solid rgba(201,163,74,.4);}
.parting-rule span{font-family:'Noto Sans Cuneiform';font-size:.9rem;}
.parting-rule.bottom{margin-top:1.6rem;margin-bottom:0;}
.parting h3{font-family:'Marcellus',serif;font-weight:400;color:#e0c98b;font-size:1.3rem;letter-spacing:.03em;margin:0 0 .4rem;text-align:center;}
.parting .headnote{margin-left:auto;margin-right:auto;text-align:center;}
.cmp-grid{display:grid;grid-template-columns:1fr 1fr;gap:2.2rem;align-items:start;max-width:1200px;margin:0 auto;}
.cmp-col{border-left:2px solid rgba(201,163,74,.3);padding-left:1.1rem;}
.cmp-col.ob{border-left-color:rgba(139,147,184,.55);}
.cmp-label{font-family:'Alegreya Sans',sans-serif;font-size:.76rem;letter-spacing:.18em;text-transform:uppercase;color:#c9a34a;margin-bottom:.8rem;}
.cmp-col.ob .cmp-label{color:#a9b0d0;}
.cmpv .v{grid-template-columns:3.4rem 1fr;grid-template-areas:"n akk" ". en";row-gap:.1rem;}
.cmpv .v .akk{grid-area:akk;}
.cmpv .v .en{grid-area:en;}
.mn.res{border-left:2px solid rgba(139,147,184,.5);padding-left:.6rem;}
.mn.res b{color:#aeb9e6;font-style:italic;font-family:'Gentium Plus',serif;font-weight:400;}
.anc.res, sup.anc.res{color:#8fa0d6;}
sup.anc.res{font-size:.7em;}
figure.plate{margin:1.2rem auto 2.4rem;max-width:620px;}
figure.plate img{width:100%;display:block;border:1px solid rgba(201,163,74,.4);box-shadow:0 0 0 6px rgba(9,13,33,.55), 0 14px 40px rgba(0,0,0,.5);}
figure.plate figcaption{font-family:'Alegreya Sans',sans-serif;font-size:.84rem;line-height:1.6;color:#b7bdd9;margin-top:.8rem;border-top:1px solid rgba(201,163,74,.35);padding-top:.55rem;}
figure.plate .credit{display:block;margin-top:.3rem;font-size:.72rem;color:#8b93b8;letter-spacing:.04em;}
@media(max-width:1150px){
 .daf{grid-template-columns:1fr;}
 .m{position:static;border:none;padding:0;text-align:left;font-size:.84rem;}
 .m-l{order:2;margin-top:1rem;border-top:1px dotted rgba(201,163,74,.3);padding-top:.8rem;}
 .m-r{order:3;border-top:1px dotted rgba(201,163,74,.3);padding-top:.8rem;}
 .daf .body{order:1;}
 .cmp-grid{grid-template-columns:1fr;}
}
@media print{.m{position:static;}}
</style>''')

sections = '\n'.join(build_tablet(t) for t in TABLETS)
toc = ''.join(f'<a href="#t{t}">{t}</a>' for t in TABLETS)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gilgameš — a reader’s edition, with the text surrounded</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Gentium+Plus:ital@0;1&family=Gentium+Book+Plus:ital@0;1&family=Alegreya+Sans:ital,wght@0,400;0,500;1,400&family=Noto+Sans+Cuneiform&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<header class="hero">
  <div class="cune" aria-hidden="true">𒀭𒄑𒂆𒈦</div>
  <h1>Gilgameš</h1>
  <p class="sub">A reader’s edition — the Standard Babylonian epic entire, read straight through,<br>with the commentary around the text and the Old Babylonian at the partings of the ways</p>
  <p class="epigraph">išâm-ma ṭuppi uqnî šitassi — “lift out the tablet of lapis lazuli and read aloud”</p>
  <nav class="toc">{toc}</nav>
</header>
<main>
<section class="method">
  <h2>How this page is laid out</h2>
  <p>The poem runs down the center of the page in pericopes — short titled passages, Akkadian beside English — meant to be read top to bottom without interruption. The commentary stands around the text, after the manner of a Talmudic page: the <b>inner margin</b> (right-aligned, small) carries the philological glosses — word-senses, restorations, cruxes; the <b>outer margin</b> carries the discursive notes — structure, theology, and readings against the Old Babylonian recension of ca. 1800 BC. Gold letters<sup class="anc">a</sup> in the verse key each note to its line; a reader who ignores every letter loses nothing of the poem. A third register, marked <span class="anc res" style="font-size:.8em">≈</span> and set in slate-blue, carries the <b>resonances</b> — the places where the Akkadian names rhyme with the things and the English goes deaf: Enkidu the <i>knot</i> and the meteor the <i>lump</i>, one noun; “husband” a vowel away from “death” in Ištar’s proposal; the boatman Servant-of-Two-Thirds ferrying the two-thirds god; Ūta-napišti, “He-Found-Life,” sentencing the hero with the etymology of his own name. Four times, where the two recensions genuinely part ways — the meteor dream, the “only wind” creed, the kill of Humbaba, and the ale-wife’s deleted sermon — the page itself divides into two columns, older text against later, and then rejoins. Text: the electronic Babylonian Library’s critical editions (eBL, retrieved August 2026), 2,683 Standard Babylonian lines with the Old Babylonian witnesses at the partings; translation original throughout. <span class="br">[Brackets]</span> mark restored clay; <span class="br">[ ... ]</span> a line too broken to carry; a rule in the text, lines not yet found. The plates are not reconstructions: no synthetic image can be trusted for this, and none is needed. They are the objects themselves — the marble face from Eanna, the fleece-skirted superintendent of Mari, Humbaba modeled by an Old Babylonian hand, the Queen of the Night, the gold-and-lapis lyre from the graves of Ur, and the Flood Tablet whose text this page carries — museum photography from Wikimedia Commons, credited beneath each.</p>
</section>
{sections}
<section class="sources">
  <h2>Sources &amp; further reading</h2>
  <ul>
    <li><a href="https://www.ebl.lmu.de/corpus/L/1/4">electronic Babylonian Library — Gilgameš, critical edition</a> (all Standard Babylonian and Old Babylonian chapters used here)</li>
    <li><a href="http://ancientworldonline.blogspot.com/2016/04/the-standard-babylonian-epic-of.html">A. R. George’s score transliterations of the SB epic (SOAS)</a></li>
    <li><a href="https://www.soas.ac.uk/baplar/recordings/epic-gilgamesh-old-babylonian-version-part-vabm-tablet-read-martin-west">The Sippar tablet read aloud (SOAS recordings)</a></li>
    <li><a href="https://www.gutenberg.org/files/11000/11000-h/11000-h.htm">Jastrow &amp; Clay, <i>An Old Babylonian Version of the Gilgamesh Epic</i> (1920)</a></li>
    <li><a href="https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=c.1.8.1*">The Sumerian Gilgameš poems (ETCSL)</a></li>
  </ul>
  <p class="headnote">Companion files in the same hand: <i>gilgamesh-complete.html</i> (the Standard edition with tablet-end apparatus) and <i>gilgamesh-old-babylonian.html</i> (all fourteen OB witnesses entire).</p>
</section>
<footer class="colophon">
  <div class="wedge" aria-hidden="true">𒀸 𒀸 𒀸</div>
  <p><i>kīma labīrīšu šaṭir-ma bari</i> — written and collated according to its original</p>
</footer>
</main>
</body>
</html>'''

open('../out/gilgamesh-reader.html' if EMBED else '../out/gilgamesh-reader-web.html','w').write(page)
import os
print('bytes:', os.path.getsize('../out/gilgamesh-reader.html' if EMBED else '../out/gilgamesh-reader-web.html'))
