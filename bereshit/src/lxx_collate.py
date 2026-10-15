"""Collate src/witness-lxx.json against a CATSS morphological LXX file (Beta code).

Usage: python3 -I bereshit/src/lxx_collate.py 01.Gen.1.mlxx bereshit/src/witness-lxx.json
Compares letters only (accents, breathings and case set aside); prints each verse that differs.
"""
import re, unicodedata, json, sys
L = dict(zip("ABGDEZHQIKLMNCOPRSTUFXYW", "αβγδεζηθικλμνξοπρστυφχψω"))
DIA = {")": "̓", "(": "̔", "/": "́", "\\": "̀", "=": "͂", "+": "̈", "|": "ͅ"}
def beta(w):
    out = []
    for ch in w:
        if ch in L: out.append(L[ch])
        elif ch in DIA: out.append(DIA[ch])
    s = unicodedata.normalize("NFC", "".join(out))
    s = re.sub(r"σ\b", "ς", s)
    return s
def load(path):
    verses, cur = {}, None
    for line in open(path, encoding="latin-1"):
        line = line.rstrip()
        m = re.match(r"Gen (\d+:\d+)", line)
        if m: cur = m.group(1); verses[cur] = []; continue
        if line.strip() and cur: verses[cur].append(beta(line.split()[0]))
    return verses
def bare(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^α-ως]", "", s).replace("ς", "σ")
if __name__ == "__main__":
    r = load(sys.argv[1]); b = json.load(open(sys.argv[2], encoding="utf-8"))
    b = b.get("verses", b)
    import difflib
    n = 0
    for ref in b:
        if ref not in r: print("missing", ref); continue
        bw = b[ref]["greek"].split()
        x = [bare(w) for w in bw]; y = [bare(w) for w in r[ref]]
        x = [w for w in x if w]; y = [w for w in y if w]
        if x != y:
            n += 1
            sm = difflib.SequenceMatcher(a=x, b=y)
            print(ref, [(t, x[i1:i2], y[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal"])
    print("verses differing:", n)
