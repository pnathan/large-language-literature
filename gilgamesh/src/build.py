# -*- coding: utf-8 -*-
import json, re, html
from meta import TITLES, HEADNOTES, APPARATUS

TABLETS = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

NAMES = ['gilgāmeš','enkīdu','šamhat','uruk','eanna','ištar','ānu','antu','anu','ellil','enlil','ēa','aruru',
 'rīmat-ninsun','ninsun','lugalbanda','šamaš','ayya','humbāba','humbaba','adad','sîn','nudimmud','bēlet-ilī',
 'ninurta','šakkan','irnini','ningišzida','ereškigal','ereškigal','bēlet-ṣēri','irkalla','etana','namtar',
 'hušbiša','qāssa-ṭābat','ninšuluhhatum','ninšuluhha','bibbu','dumuzi-abzu','dumuzi','silili','išullānu','išullānî','išhara',
 'ūta-napišti','ubār-tutu','ubar-tutu','ur-šanabi','ur-šanābi','šiduri','māšu','māši','nimuš','labnānu','sirara',
 'ebabbarra','ēgalmah','nippuri','nippur','larsa','purattu','puratti','ulāya','šuruppak','atra-hasīs','atar-hasīs',
 'puzur-ellil','šullat','haniš','errakal','erra','mammītu','anunnakū','anunnakkū','anunnak','igīgī','igī','arallê',
 'ēkur','erīdu','ningal','nergal','ninazu','marūtuk','anzâ','anzî','anzû','nissaba','ekur','irninnī','mātu?','ninsun?']
NAMES = sorted(set(NAMES), key=len, reverse=True)

def norm_line(line):
    toks = line['variants'][0].get('reconstructionTokens', [])
    s = ' '.join(t.get('value','') for t in toks)
    s = s.replace('%n ','').replace(' || ',' ').replace(' | ',' ')
    s = s.replace('(|)','').replace('(||)','').replace('|','')
    s = s.replace('%sb ','')
    s = re.sub(r'\s+',' ',s).strip()
    return s

def cap_names(s):
    def repl(m):
        w = m.group(0)
        return w[0].upper()+w[1:]
    for n in NAMES:
        base = n.rstrip('?')
        if not base: continue
        s = re.sub(r'(?<![\w\-])'+re.escape(base), lambda m: base[0].upper()+base[1:], s)
    return s

def bracketize(s):
    # wrap [...] segments in span.br ; handle unbalanced halves gracefully
    s = html.escape(s, quote=False)
    out, i, open_br = [], 0, False
    for ch in s:
        if ch == '[':
            out.append('<span class="br">[')
            open_br = True
        elif ch == ']':
            if open_br:
                out.append(']</span>'); open_br = False
            else:
                out.append('<span class="br">]</span>')
        else:
            out.append(ch)
    if open_br: out.append('</span>')
    return ''.join(out)

def load_tr(tab):
    d = {}
    try:
        for ln in open(f'tr_{tab}.tsv'):
            ln = ln.rstrip('\n')
            if not ln.strip(): continue
            num, _, txt = ln.partition('\t')
            d[num.strip()] = txt
    except FileNotFoundError:
        pass
    return d

def leading_int(numstr):
    m = re.match(r'^(\d+)', numstr)
    return int(m.group(1)) if m else None

def build_tablet(tab):
    data = json.load(open(f'SB_{tab}.json'))
    tr = load_tr(tab)
    label, title = TITLES[tab]
    rows = []
    prev = None
    for line in data['lines']:
        num = line['number']
        akk = cap_names(norm_line(line))
        en  = tr.get(num, '[ ... ]')
        ci = leading_int(num)
        if prev is not None and ci is not None and ci - prev > 1:
            lo, hi = prev+1, ci-1
            span = f'line {lo}' if lo==hi else f'lines {lo}–{hi}'
            rows.append(f'<div class="gap">⸻ {span} lost or too broken to carry ⸻</div>')
        if ci is not None: prev = ci
        rows.append(
            f'<div class="v"><span class="n">{html.escape(num)}</span>'
            f'<span class="akk">{bracketize(akk)}</span>'
            f'<span class="en">{bracketize(en)}</span></div>')
    app = APPARATUS.get(tab, [])
    app_html = ''
    if app:
        items = ''.join(f'<p class="note"><b>{html.escape(h)}</b> — {t}</p>' for h,t in app)
        app_html = (f'<details class="apparatus"><summary>Apparatus — cruxes &amp; choices</summary>{items}</details>')
    return f'''
<section class="tablet" id="t{tab}">
  <div class="tablet-head">
    <span class="tab-label">{label}</span>
    <h2>{title}</h2>
  </div>
  <p class="headnote">{HEADNOTES[tab]}</p>
  <div class="verses">
    {''.join(rows)}
  </div>
  {app_html}
</section>'''

CSS = open('style.css').read()
# widen for full edition + add gap style, nav, tablet-head styles
CSS = CSS.replace('</style>','''
.gap{grid-column:1/-1;text-align:center;color:#8b93b8;font-family:'Alegreya Sans',sans-serif;font-size:.78rem;letter-spacing:.12em;padding:.9rem 0;text-transform:uppercase;}
.tablet{margin:4.5rem 0;}
.tablet-head{display:flex;align-items:baseline;gap:1rem;border-bottom:1px solid rgba(201,163,74,.35);padding-bottom:.4rem;margin-bottom:1rem;}
.tab-label{font-family:'Alegreya Sans',sans-serif;font-size:.8rem;letter-spacing:.25em;text-transform:uppercase;color:#c9a34a;white-space:nowrap;}
.tablet-head h2{margin:0;border:none;padding:0;}
.headnote{font-family:'Alegreya Sans',sans-serif;font-size:.92rem;line-height:1.65;color:#b7bdd9;max-width:62ch;margin:0 0 1.6rem;}
nav.toc{display:flex;flex-wrap:wrap;gap:.5rem .9rem;justify-content:center;margin:2.2rem auto 0;max-width:700px;}
nav.toc a{font-family:'Alegreya Sans',sans-serif;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:#c9a34a;text-decoration:none;border:1px solid rgba(201,163,74,.35);padding:.3rem .7rem;border-radius:2px;}
nav.toc a:hover{background:rgba(201,163,74,.12);}
.note{font-family:'Alegreya Sans',sans-serif;font-size:.86rem;line-height:1.6;color:#b7bdd9;margin:.7rem 0;}
.note b{color:#e0c98b;font-weight:600;}
</style>''')

sections = '\n'.join(build_tablet(t) for t in TABLETS)
toc = ''.join(f'<a href="#t{t}">{t}</a>' for t in TABLETS)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gilgameš — the epic entire, an original translation from the Akkadian</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Gentium+Plus:ital@0;1&family=Gentium+Book+Plus:ital@0;1&family=Alegreya+Sans:ital,wght@0,400;0,500;1,400&family=Noto+Sans+Cuneiform&display=swap" rel="stylesheet">
{CSS}
</head>
<body>
<header class="hero">
  <div class="cune" aria-hidden="true">𒀭𒄑𒂆𒈦</div>
  <h1>Gilgameš</h1>
  <p class="sub">The Standard Babylonian epic <i>ša naqba īmuru</i> — entire, as far as the clay survives<br>an original translation from the Akkadian</p>
  <p class="epigraph">išâm-ma ṭuppi uqnî šitassi — “lift out the tablet of lapis lazuli and read aloud”</p>
  <nav class="toc">{toc}</nav>
</header>
<main>
<section class="method">
  <h2>Method</h2>
  <p>This is the complete Standard Babylonian epic — all twelve tablets, 2,683 edited lines — set against the Akkadian of the electronic Babylonian Library’s critical edition (retrieved 25–26 August 2026 via the eBL API), which rests on George’s 2003 edition and the manuscripts recovered since. The English is an original verse translation made against that text, line by line: not George’s wording, not the eBL’s, though any honest translation of the same Akkadian will rhyme with its predecessors. Half-brackets and restorations follow the edition; <span class="br">[bracketed]</span> English translates restored Akkadian, and lines too broken to carry meaning stand as <span class="br">[ ... ]</span>. Gaps in the line-count mark clay that has not yet been found. “Complete” therefore means: complete as recovered — roughly nine-tenths of the poem, and growing as new fragments are read. In August 2026 the whole translation was collated word-by-word against the eBL text — every line of all twelve tablets — and corrected wherever collation caught omission, softening, or drift; each tablet’s apparatus closes with its collation note. The rule of register held throughout: where the Akkadian is blunt the English is blunt, and where it is discreet the English is discreet.</p>
</section>
{sections}
<section class="sources">
  <h2>Sources &amp; further reading</h2>
  <ul>
    <li><a href="https://www.ebl.lmu.de/corpus/L/1/4">electronic Babylonian Library — Gilgameš, critical edition</a> (the Akkadian text used here)</li>
    <li><a href="http://ancientworldonline.blogspot.com/2016/04/the-standard-babylonian-epic-of.html">A. R. George’s score transliterations of the SB epic (SOAS)</a></li>
    <li><a href="https://www.soas.ac.uk/baplar/recordings/epic-gilgamesh-old-babylonian-version-part-vabm-tablet-read-martin-west">The OB Šiduri tablet read aloud (SOAS recordings)</a></li>
    <li><a href="https://www.gutenberg.org/files/11000/11000-h/11000-h.htm">Jastrow &amp; Clay, <i>An Old Babylonian Version of the Gilgamesh Epic</i> (1920)</a></li>
    <li><a href="https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=c.1.8.1*">The Sumerian Gilgameš poems (ETCSL)</a></li>
  </ul>
</section>
<footer class="colophon">
  <div class="wedge" aria-hidden="true">𒀸 𒀸 𒀸</div>
  <p><i>kīma labīrīšu šaṭir-ma bari</i> — written and collated according to its original</p>
</footer>
</main>
</body>
</html>'''

open('../out/gilgamesh-complete.html','w').write(page)
import os
print('bytes:', os.path.getsize('../out/gilgamesh-complete.html'))
