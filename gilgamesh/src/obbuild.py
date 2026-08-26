# -*- coding: utf-8 -*-
import json, re, html
from obmeta import ORDER, WT, WNOTES

def norm_line(line):
    toks = line['variants'][0].get('reconstructionTokens', [])
    s = ' '.join(t.get('value','') for t in toks)
    for a,b in ((' || ',' '),(' | ',' '),('%n ',''),('(|)',''),('(||)',''),('|',''),('%sb ','')):
        s = s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()

NAMES = ['gilgāmeš','enkīdu','šamhat','šamkat','uruk','eanna','ištar','ānu','ānim','anu','antu','ellil','enlil','ēa','aruru',
 'rīmat-ninsun','ninsun','ninsunna','ninsumuna','lugalbanda','šamaš','šamšim','šamšu','ayya','humbāba','huwāwa','adad','sîn',
 'nudimmud','bēlet-ilī','ninurta','šakkan','irnini','ningišzida','ereškigal','irkalla','etana','namtar','išhara',
 'ūta-napišti','ūta-naʾištim','ubār-tutu','ubar-tutu','ur-šanabi','ur-šanābi','sursunābu','šiduri','māšu','nimuš','labnānu','labnān',
 'sirara','saria','ebabbarra','ēgalmah','nippuri','nippurim','nippur','larsa','purattu','puratti','purattim','ulāya','šuruppak',
 'atra-hasīs','šullat','haniš','errakal','erra','mammītu','anunnakū','anunnakkū','enunnakkī','enunakkī','igīgī','arallê',
 'ēkur','erīdu','ningal','nergal','ninazu','anzâm','anzâ','anzû','nissaba','māt-ibla','hamran','wēr','anšanītam','ekur']
NAMES = sorted(set(NAMES), key=len, reverse=True)

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

def last_int(numstr):
    ms = re.findall(r'\d+', numstr)
    return int(ms[-1]) if ms and not numstr.startswith(('a','b','c','d','e','f','g','h')) else None
def first_int(numstr):
    m = re.match(r'^(\d+)', numstr)
    return int(m.group(1)) if m else None

def verse_rows(lines, tr, gap_ok=True):
    rows, prev = [], None
    for line in lines:
        num = line['number']
        akk = cap_names(norm_line(line))
        en  = tr.get(num, '[ ... ]')
        fi, li = first_int(num), last_int(num)
        if gap_ok and prev is not None and fi is not None and fi - prev > 1:
            lo, hi = prev+1, fi-1
            span = f'line {lo}' if lo==hi else f'lines {lo}–{hi}'
            rows.append(f'<div class="gap">⸻ {span} lost or too broken to carry ⸻</div>')
        if li is not None: prev = li
        rows.append(f'<div class="v"><span class="n">{html.escape(num)}</span>'
                    f'<span class="akk">{bracketize(akk)}</span>'
                    f'<span class="en">{bracketize(en)}</span></div>')
    return rows

# ---------- load all OB witnesses ----------
OB = {}
for k in ORDER:
    OB[k] = json.load(open(f'OB_{k}.json'))
OBTR = {k: load_tr(f'obtr_{k}.tsv') for k in ORDER}

# ---------- load SB tablets needed for synopsis ----------
SB = {t: json.load(open(f'SB_{t}.json')) for t in ['I','II','X']}
SBTR = {t: load_tr(f'tr_{t}.tsv') for t in ['I','II','X']}

def pick(data, tr, numbers):
    idx = {l['number']: l for l in data['lines']}
    out = []
    for n in numbers:
        if n in idx: out.append(idx[n])
    return verse_rows(out, tr, gap_ok=False)

def cmp_panel(title, blurb, left_label, left_rows, right_label, right_rows):
    return f'''
<div class="cmp">
  <h3>{title}</h3>
  <p class="headnote">{blurb}</p>
  <div class="cmp-grid">
    <div class="cmp-col"><div class="cmp-label">{left_label}</div><div class="verses cmpv">{''.join(left_rows)}</div></div>
    <div class="cmp-col"><div class="cmp-label">{right_label}</div><div class="verses cmpv">{''.join(right_rows)}</div></div>
  </div>
</div>'''

syn = []
# A. Šiduri
ob_va = OB['VABM']; tr_va = OBTR['VABM']
left = pick(ob_va, tr_va, [f'a+{i}' for i in range(15,31)])
right = pick(SB['X'], SBTR['X'], [str(i) for i in range(78,92)])
syn.append(cmp_panel('1 · The ale-wife: sermon against sailing directions',
 'The Old Babylonian Šiduri preaches the poem’s only carpe diem; the Standard edition hands the same woman a route-map and moves the theology downstream to Ūta-napišti. Set side by side, the deletion is visible as a decision.',
 'OB VA+BM (Sippar), a+15–a+30', left, 'SB Tablet X 78–91', right))
# B. Only wind
left = pick(OB['III'], OBTR['III'], ['140','141','142','143','144','145','146','147','148','149-150'])
right = pick(SB['II'], SBTR['II'], [str(i) for i in range(232,241)])
syn.append(cmp_panel('2 · “Whatever he ever does is only wind”',
 'The young king’s creed. The old version frames the couplet between heaven and the sun and ends with the wager — “if I fall, I will have planted my name.” The late version keeps the creed, cuts the frame, and lets the rest of the epic annul the wager.',
 'OB III (Yale), 140–150', left, 'SB Tablet II 232–240', right))
# C. The meteor dream
left = pick(OB['II'], OBTR['II'], ['1','2','3','4-5','6','7','8','9','10','11','12-13','14','15','16','17','18-19','20','21','22-23'])
right = pick(SB['I'], SBTR['I'], [str(i) for i in range(243,257)] + [str(i) for i in range(257,271)])
syn.append(cmp_panel('3 · The dream of the meteor',
 'Same dream, five centuries apart. The old telling is brisk and bodily (“it was too heavy for me”); the late telling is longer, stronger (“too strong for me”), and adds the crowd, the kissing of feet, and the mother’s full oracle of the friend.',
 'OB II (Pennsylvania), 1–23', left, 'SB Tablet I 243–270', right))

# ---------- witness sections ----------
sections = []
for k in ORDER:
    label, title, head = WT[k]
    rows = verse_rows(OB[k]['lines'], OBTR[k])
    notes = WNOTES.get(k, [])
    app = ''
    if notes:
        items = ''.join(f'<p class="note"><b>{html.escape(h)}</b> — {t}</p>' for h,t in notes)
        app = f'<details class="apparatus"><summary>Against the Standard version</summary>{items}</details>'
    sections.append(f'''
<section class="tablet" id="w{k}">
  <div class="tablet-head"><span class="tab-label">{label}</span><h2>{title}</h2></div>
  <p class="headnote">{head}</p>
  <div class="verses">{''.join(rows)}</div>
  {app}
</section>''')

CSS = open('style.css').read().replace('</style>','''
.gap{grid-column:1/-1;text-align:center;color:#8b93b8;font-family:'Alegreya Sans',sans-serif;font-size:.78rem;letter-spacing:.12em;padding:.9rem 0;text-transform:uppercase;}
.tablet{margin:4.5rem 0;}
.tablet-head{display:flex;align-items:baseline;gap:1rem;border-bottom:1px solid rgba(201,163,74,.35);padding-bottom:.4rem;margin-bottom:1rem;}
.tab-label{font-family:'Alegreya Sans',sans-serif;font-size:.8rem;letter-spacing:.25em;text-transform:uppercase;color:#c9a34a;white-space:nowrap;}
.tablet-head h2{margin:0;border:none;padding:0;}
.headnote{font-family:'Alegreya Sans',sans-serif;font-size:.92rem;line-height:1.65;color:#b7bdd9;max-width:62ch;margin:0 0 1.6rem;}
nav.toc{display:flex;flex-wrap:wrap;gap:.5rem .9rem;justify-content:center;margin:2.2rem auto 0;max-width:760px;}
nav.toc a{font-family:'Alegreya Sans',sans-serif;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:#c9a34a;text-decoration:none;border:1px solid rgba(201,163,74,.35);padding:.3rem .65rem;border-radius:2px;}
nav.toc a:hover{background:rgba(201,163,74,.12);}
.note{font-family:'Alegreya Sans',sans-serif;font-size:.86rem;line-height:1.6;color:#b7bdd9;margin:.7rem 0;}
.note b{color:#e0c98b;font-weight:600;}
.cmp{margin:3.5rem 0;}
.cmp h3{font-family:'Marcellus',serif;font-weight:400;color:#e0c98b;font-size:1.25rem;letter-spacing:.03em;margin:0 0 .4rem;}
.cmp-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:start;}
.cmp-col{border-left:2px solid rgba(201,163,74,.3);padding-left:1.1rem;}
.cmp-label{font-family:'Alegreya Sans',sans-serif;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:#c9a34a;margin-bottom:.8rem;}
.cmpv .v{grid-template-columns:3.2rem 1fr;grid-template-areas:"n akk" ". en";row-gap:.1rem;}
.cmpv .v .akk{grid-area:akk;}
.cmpv .v .en{grid-area:en;}
@media(max-width:900px){.cmp-grid{grid-template-columns:1fr;}}
</style>''')

toc = ''.join(f'<a href="#w{k}">{WT[k][0].replace("OB ","")}</a>' for k in ORDER)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gilgameš — the Old Babylonian witnesses, an original translation set against the Standard edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Gentium+Plus:ital@0;1&family=Gentium+Book+Plus:ital@0;1&family=Alegreya+Sans:ital,wght@0,400;0,500;1,400&family=Noto+Sans+Cuneiform&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<header class="hero">
  <div class="cune" aria-hidden="true">𒀭𒄑𒂆𒈦</div>
  <h1>Gilgameš</h1>
  <p class="sub">The Old Babylonian witnesses, ca. 1800 BC — <i>šūtur eli šarrī</i>, “Surpassing all kings”<br>an original translation, set against the Standard Babylonian edition</p>
  <p class="epigraph">šumma amtaqut šumī lū ušzīz — “and if I fall, I will have planted my name”</p>
  <nav class="toc">{toc}</nav>
</header>
<main>
<section class="method">
  <h2>Method</h2>
  <p>Five centuries before Sîn-lēqi-unninni’s twelve-tablet edition, the epic circulated in an Old Babylonian recension known today from fourteen tablets and fragments — two long tablets of a single old edition (Pennsylvania and Yale, whose series bore the incipit <i>šūtur eli šarrī</i>), and a scatter of school tablets and independent copies. All fourteen are printed here, in narrative order, from the electronic Babylonian Library’s critical editions (retrieved 26 August 2026 via the eBL API): 882 edited lines. The English is an original translation made against the Akkadian, sister to my rendering of the Standard edition and deliberately consistent with it, so that where the two texts share a verse, the translations differ only where the Akkadian does. The dialect shows its age: mimation intact, <i>w-</i> preserved, Huwawa for Humbaba, Sursunabu for Ur-šanabi. A Synopsis of three passages opens the file; each witness closes with notes reading it against the late edition. In August 2026 all fourteen witnesses were collated word-by-word against the eBL text. The collation also caught a mislabelling that had scrambled four of them — the translations filed under Nippur, Schøyen₃, IM, and Harmal₁ in fact belonged to Schøyen₃, IM, Harmal₁, and Nippur respectively; each is now restored to the tablet that carries its Akkadian, and the witness descriptions and running order corrected to match.</p>
</section>
<section class="tablet" id="synopsis">
  <div class="tablet-head"><span class="tab-label">Synopsis</span><h2>Three passages, two recensions</h2></div>
  {''.join(syn)}
</section>
{''.join(sections)}
<section class="sources">
  <h2>Sources &amp; further reading</h2>
  <ul>
    <li><a href="https://www.ebl.lmu.de/corpus/L/1/4">electronic Babylonian Library — Gilgameš, critical edition</a> (Old Babylonian chapters: II, III, UM, Schøyen 1–3, Nippur, Harmal 1–2, Ishchali, IM, VA+BM, CUNES, SM)</li>
    <li><a href="https://www.soas.ac.uk/baplar/recordings/epic-gilgamesh-old-babylonian-version-part-vabm-tablet-read-martin-west">The Sippar tablet (VA+BM) read aloud — SOAS recordings</a></li>
    <li><a href="https://www.gutenberg.org/files/11000/11000-h/11000-h.htm">Jastrow &amp; Clay, <i>An Old Babylonian Version of the Gilgamesh Epic</i> (1920)</a> — the first edition of the Pennsylvania and Yale tablets</li>
    <li><a href="https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=c.1.8.1*">The Sumerian Gilgameš poems (ETCSL)</a></li>
  </ul>
  <p class="headnote">Companion file: <i>gilgamesh-complete.html</i> — the Standard Babylonian epic entire, in the same format and the same hand.</p>
</section>
<footer class="colophon">
  <div class="wedge" aria-hidden="true">𒀸 𒀸 𒀸</div>
  <p><i>ṭuppum šanû — šūtur eli šarrī</i> · second tablet: “Surpassing all kings”</p>
</footer>
</main>
</body>
</html>'''

open('../out/gilgamesh-old-babylonian.html','w').write(page)
import os
print('bytes:', os.path.getsize('../out/gilgamesh-old-babylonian.html'))
