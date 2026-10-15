"""Verify the Sanskrit of docs/mahabharata/index.html against the BORI typed text.

Checks, for every Sanskrit block (<blockquote class="sa">):
1. A verse-ref precedes the block. Its pāda-level expansion equals exactly the set
   of constituted-text lines printed in the block, in source order. Starred and
   appendix lines (refs with * or @) are not accepted.
2. Every line has a Devanagari span. It equals devanagari.line() of the IAST
   span, with the daṇḍa mark that the line's position in the verse requires.
3. The Devanagari converts back to the same letters as the IAST (round trip).

Usage: python3 verify_refs.py docs/mahabharata/index.html <dir with mbh_01_u.htm, mbh_02_u.htm>
Source files: Zenodo 6467313 (GRETIL/BORI typed text).
"""
import html
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import devanagari  # noqa: E402

N = lambda t: unicodedata.normalize('NFC', t)
PADA_LINE = {'a': 'a', 'b': 'a', 'c': 'c', 'd': 'c', 'e': 'e', 'f': 'e'}


def load_source(src_dir):
    """Return (text → [keys], (book, adh, verse) → [line letters])."""
    by_text, verse_lines = {}, {}
    for b in ('01', '02'):
        for row in open(os.path.join(src_dir, f'mbh_{b}_u.htm'), encoding='utf-8'):
            m = re.match(r'(\d\d),(\d\d\d)\.(\d\d\d)([a-z])\s+(.*?)(<BR>)?\s*$', row)
            if m:
                k = (int(m[1]), int(m[2]), int(m[3]), m[4])
                by_text.setdefault(N(html.unescape(m[5]).strip()), []).append(k)
                verse_lines.setdefault(k[:3], []).append(m[4])
    return by_text, verse_lines


def expand(ref, verse_lines):
    """Expand a printed reference ('2.61.28, 31cd–33') to a set of line keys."""
    r = re.sub(r'\(.*?\)', '', html.unescape(ref)).replace('Mahābhārata', '').strip()
    out, book, adh = set(), None, None
    for part in [p.strip() for p in r.split(',')]:
        m = re.fullmatch(r'(?:(\d+)\.(\d+)\.)?(\d+)([a-f]*)(?:–(\d+)?([a-f]*))?', part)
        if not m:
            raise ValueError(f'unparsable reference part {part!r} in {ref!r}')
        if m[1]:
            book, adh = int(m[1]), int(m[2])
        v1, p1 = int(m[3]), m[4]
        if '–' not in part:
            spans = [(v1, p1)]
        elif m[5] is None:  # pāda range inside one verse, e.g. 7a–d
            letters = 'abcdef'
            spans = [(v1, letters[letters.index(p1):letters.index(m[6]) + 1])]
        else:
            v2 = int(m[5])
            spans = [(v1, p1)] + [(v, '') for v in range(v1 + 1, v2)] + [(v2, m[6])]
        for v, p in spans:
            avail = verse_lines.get((book, adh, v), [])
            want = {PADA_LINE[c] for c in p} if p else set(avail)
            for letter in want:
                if letter not in avail:
                    raise ValueError(f'{ref!r}: no line {v}{letter}')
                out.add((book, adh, v, letter))
    return out


def check(page, by_text, verse_lines):
    problems, blocks = [], 0
    for m in re.finditer(r'<blockquote class="sa" lang="sa">(.*?)</blockquote>', page, re.S):
        blocks += 1
        ln = page.count('\n', 0, m.start()) + 1
        ref = re.search(r'<p class="verse-ref">([^<]*)</p>\s*$', page[:m.start()])
        if not ref:
            problems.append(f'{ln}: no verse-ref')
            continue
        exp = expand(ref[1], verse_lines)
        got = []
        line_re = (r'<span class="l">(?:<span class="dev" lang="sa-Deva">([^<]*)</span>'
                   r'<span class="lat" lang="sa-Latn">([^<]*)</span>|([^<]*))</span>')
        if len(re.findall(r'<span class="l">', m[1])) != len(re.findall(line_re, m[1])):
            problems.append(f'{ln}: malformed verse line markup')
        for lm in re.finditer(line_re, m[1]):
            if lm[3] is not None:
                if html.unescape(lm[3]).strip() != '…':
                    problems.append(f'{ln}: line without Devanagari: {lm[3][:60]!r}')
                continue
            dev, lat = N(lm[1]), N(html.unescape(lm[2]).strip())
            keys = [k for k in by_text.get(lat, []) if k in exp] or by_text.get(lat, [None])
            k = keys[0]
            if k is None:
                problems.append(f'{ln}: line not in source: {lat!r}')
                continue
            got.append(k)
            book, adh, v, letter = k
            last = verse_lines[(book, adh, v)][-1] == letter
            want_dev = devanagari.line(lat, 'double' if last else 'danda', v)
            if dev != want_dev:
                problems.append(f'{ln}: Devanagari differs from transliteration of {lat!r}')
            if devanagari.to_iast(dev) != devanagari.strip_iast(lat):
                problems.append(f'{ln}: round trip fails for {lat!r}')
        if set(got) != exp:
            problems.append(f'{ln} {ref[1]}: missing {sorted(exp - set(got))} extra {sorted(set(got) - exp)}')
        if got != sorted(got):
            problems.append(f'{ln} {ref[1]}: lines out of source order')
    return blocks, problems


if __name__ == '__main__':
    by_text, verse_lines = load_source(sys.argv[2])
    page = N(open(sys.argv[1], encoding='utf-8').read())
    blocks, problems = check(page, by_text, verse_lines)
    print('\n'.join(problems))
    print('blocks', blocks, 'problems', len(problems))
    sys.exit(1 if problems else 0)
