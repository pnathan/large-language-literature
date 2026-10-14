"""Verify the Sanskrit of docs/mahabharata/index.html against the BORI typed text.

Every <blockquote lang="sa-Latn"> must be preceded by a verse-ref whose pāda-level
expansion equals exactly the set of constituted-text lines printed in the block,
in source order. Starred/appendix lines (refs with * or @) are not accepted.

Usage: python3 verify_refs.py docs/mahabharata/index.html <dir with mbh_01_u.htm, mbh_02_u.htm>
Source files: Zenodo 6467313 (GRETIL/BORI typed text).
"""
import re, html, sys, unicodedata, os
S=os.path.join(sys.argv[2],'')
N=lambda t: unicodedata.normalize('NFC', t)
src={}; byText={}; verse_lines={}
for b in ('01','02'):
    for line in open(S+f'mbh_{b}_u.htm',encoding='utf-8'):
        m=re.match(r'(\d\d),(\d\d\d)\.(\d\d\d)([a-z])\s+(.*?)(<BR>)?\s*$', line)
        if m:
            k=(int(m[1]),int(m[2]),int(m[3]),m[4]); t=N(html.unescape(m[5]).strip())
            src[k]=t; byText.setdefault(t,[]).append(k)
            verse_lines.setdefault(k[:3],[]).append(m[4])
PL={'a':'a','b':'a','c':'c','d':'c','e':'e','f':'e'}
def expand(ref):
    r=html.unescape(ref); r=re.sub(r'\(.*?\)','',r).replace('Mahābhārata','').strip()
    out=set(); book=adh=None
    for part in [p.strip() for p in r.split(',')]:
        m=re.fullmatch(r'(?:(\d+)\.(\d+)\.)?(\d+)([a-f]*)(?:–(?:(\d+)\.(\d+)\.)?(\d+)?([a-f]*))?',part)
        if not m: raise ValueError(part)
        if m[1]: book,adh=int(m[1]),int(m[2])
        v1=int(m[3]); p1=m[4]
        if m[0].find('–')<0:
            vs=[(v1,p1)]
        elif m[7] is None:  # pāda range inside one verse, e.g. 7a–d
            letters='abcdef'; p1=letters[letters.index(p1):letters.index(m[8])+1]; vs=[(v1,p1)]
        else:
            v2=int(m[7]); p2=m[8]
            vs=[(v1,p1)]+[(v,'') for v in range(v1+1,v2)]+[(v2,p2)]
        for v,p in vs:
            avail=verse_lines.get((book,adh,v),[])
            want={PL[c] for c in p} if p else set(avail)
            for l in want:
                assert l in avail,(ref,v,l)
                out.add((book,adh,v,l))
    return out
page=N(open(sys.argv[1],encoding='utf-8').read())
bad=0; n=0
for m in re.finditer(r'<blockquote lang="sa-Latn">(.*?)</blockquote>', page, re.S):
    n+=1; ln=page.count('\n',0,m.start())+1
    r=re.search(r'<p class="verse-ref">([^<]*)</p>\s*$', page[:m.start()])
    lines=[N(html.unescape(re.sub('<[^>]+>','',x)).strip()) for x in re.findall(r'<span class="l">(.*?)</span>|<p>([^<]*)</p>',m[1]) for x in x if x]
    lines=[l for l in lines if l not in ('…',)]
    if not r: print(ln,'NO REF'); bad+=1; continue
    exp=expand(r[1])
    got=[]
    for l in lines:
        ks=[k for k in byText.get(l,[]) if k in exp] or byText.get(l,[None])
        got.append(ks[0])
    if None in got: print(ln,'LINE NOT IN SOURCE'); bad+=1
    gs=set(got)
    if gs!=exp: print(ln,r[1],'missing',sorted(exp-gs),'extra',sorted(gs-exp)); bad+=1
    if got!=sorted(got,key=lambda k:k): print(ln,r[1],'ORDER'); bad+=1
print('blocks',n,'problems',bad)
sys.exit(1 if bad else 0)
