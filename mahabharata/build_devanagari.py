"""Add Devanagari to every Sanskrit verse line of docs/mahabharata/index.html.

The IAST line stays in the page as the source of truth; the Devanagari line is
derived from it by devanagari.line(). Each verse line becomes:

  <span class="l"><span class="dev" lang="sa-Deva">…</span><span class="lat" lang="sa-Latn">…</span></span>

Line ends take daṇḍa or double daṇḍa with the verse number, from the line's
position in the BORI typed text.

Usage: python3 build_devanagari.py docs/mahabharata/index.html <dir with mbh_01_u.htm, mbh_02_u.htm>
The script rewrites the page in place. It is idempotent: it rebuilds every .dev
span from its .lat span.
"""
import html
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from devanagari import line as deva_line  # noqa: E402
from verify_refs import load_source, expand  # noqa: E402

N = lambda t: unicodedata.normalize('NFC', t)


def end_mark(key, verse_lines):
    book, adh, v, letter = key
    return ('double', v) if verse_lines[(book, adh, v)][-1] == letter else ('danda', None)


def build(page, by_text, verse_lines):
    def block(m):
        ref = re.search(r'<p class="verse-ref">([^<]*)</p>\s*$', page[:m.start()])
        if not ref:
            raise ValueError(f'block without verse-ref at offset {m.start()}')
        exp = expand(ref[1], verse_lines)
        body = m[2]
        # Normalise span-less one-line blocks to the span form.
        body = re.sub(r'^\s*<p>([^<]+)</p>\s*$', r'<p><span class="l">\1</span></p>', body)
        # Reduce already-built lines back to their IAST.
        body = re.sub(r'<span class="l"><span class="dev"[^>]*>[^<]*</span><span class="lat"[^>]*>([^<]*)</span></span>',
                      r'<span class="l">\1</span>', body)

        def one(lm):
            iast = lm[1]
            plain = N(html.unescape(iast)).strip()
            if plain == '…':
                return lm[0]
            keys = [k for k in by_text.get(plain, []) if k in exp]
            if not keys:
                raise ValueError(f'line not in its reference {ref[1]!r}: {plain!r}')
            end, num = end_mark(keys[0], verse_lines)
            dev = deva_line(plain, end, num)
            return (f'<span class="l"><span class="dev" lang="sa-Deva">{dev}</span>'
                    f'<span class="lat" lang="sa-Latn">{iast}</span></span>')

        body = re.sub(r'<span class="l">([^<]*)</span>', one, body)
        return f'<blockquote class="sa" lang="sa">{body}</blockquote>'

    return re.sub(r'<blockquote (lang="sa-Latn"|class="sa" lang="sa")>(.*?)</blockquote>', block, page, flags=re.S)


if __name__ == '__main__':
    path, src_dir = sys.argv[1], sys.argv[2]
    by_text, verse_lines = load_source(src_dir)
    page = N(open(path, encoding='utf-8').read())
    open(path, 'w', encoding='utf-8').write(build(page, by_text, verse_lines))
