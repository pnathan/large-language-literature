"""IAST → Devanagari transliteration for the Mahābhārata page, with a reverse
converter for a lossless round-trip check.

Orthographic conventions (those of printed Devanagari editions such as the BORI):
- A word that ends in a consonant joins the next word of the same pāda
  (tac chrūyate → तच्छ्रूयते; tad idaṃ → तदिदं).
- A consonant at the end of a pāda takes virāma (sanātanam → सनातनम्).
- Avagraha joins the preceding word (niṣprabhe 'smin → निष्प्रभेऽस्मिन्).
- Words that end in a vowel, anusvāra or visarga keep their space.
- Pādas of a triṣṭubh half-verse (separated by ";" in the typed text) are
  separated by a space.
- The first half-verse ends in daṇḍa (।); the last line of a verse ends in a
  double daṇḍa with the verse number (॥ २७ ॥).
"""
import re
import unicodedata

VOWELS = {  # independent, dependent sign
    'a': ('अ', ''), 'ā': ('आ', 'ा'), 'i': ('इ', 'ि'), 'ī': ('ई', 'ी'),
    'u': ('उ', 'ु'), 'ū': ('ऊ', 'ू'), 'ṛ': ('ऋ', 'ृ'), 'ṝ': ('ॠ', 'ॄ'),
    'ḷ': ('ऌ', 'ॢ'), 'e': ('ए', 'े'), 'ai': ('ऐ', 'ै'), 'o': ('ओ', 'ो'),
    'au': ('औ', 'ौ'),
}
CONSONANTS = {
    'k': 'क', 'kh': 'ख', 'g': 'ग', 'gh': 'घ', 'ṅ': 'ङ',
    'c': 'च', 'ch': 'छ', 'j': 'ज', 'jh': 'झ', 'ñ': 'ञ',
    'ṭ': 'ट', 'ṭh': 'ठ', 'ḍ': 'ड', 'ḍh': 'ढ', 'ṇ': 'ण',
    't': 'त', 'th': 'थ', 'd': 'द', 'dh': 'ध', 'n': 'न',
    'p': 'प', 'ph': 'फ', 'b': 'ब', 'bh': 'भ', 'm': 'म',
    'y': 'य', 'r': 'र', 'l': 'ल', 'v': 'व',
    'ś': 'श', 'ṣ': 'ष', 's': 'स', 'h': 'ह',
}
OTHER = {'ṃ': 'ं', 'ḥ': 'ः', "'": 'ऽ'}
VIRAMA = '्'
DIGITS = str.maketrans('0123456789', '०१२३४५६७८९')

_UNITS = sorted(list(VOWELS) + list(CONSONANTS) + list(OTHER), key=len, reverse=True)
_TOKEN = re.compile('|'.join(re.escape(u) for u in _UNITS))


def _tokens(word):
    word = unicodedata.normalize('NFC', word)
    out, pos = [], 0
    while pos < len(word):
        m = _TOKEN.match(word, pos)
        if not m:
            raise ValueError(f'untransliterable character {word[pos]!r} in {word!r}')
        out.append(m.group(0))
        pos = m.end()
    return out


def _pada(text):
    """Transliterate one pāda: words joined by the conventions above."""
    words = text.split()
    # Join consonant-final words, and avagraha-initial words, to their neighbour.
    groups = []
    for w in words:
        if groups and (_tokens(groups[-1][-1])[-1] in CONSONANTS or w.startswith("'")):
            groups[-1].append(w)
        else:
            groups.append([w])
    rendered = []
    for g in groups:
        toks = [t for w in g for t in _tokens(w)]
        s, prev_cons = [], False
        for t in toks:
            if t in CONSONANTS:
                if prev_cons:
                    s.append(VIRAMA)
                s.append(CONSONANTS[t])
                prev_cons = True
            elif t in VOWELS:
                s.append(VOWELS[t][1] if prev_cons else VOWELS[t][0])
                prev_cons = False
            else:
                if prev_cons and t == "'":
                    raise ValueError(f'avagraha after consonant in {g!r}')
                s.append(OTHER[t])
                prev_cons = False
        if prev_cons:
            s.append(VIRAMA)
        rendered.append(''.join(s))
    return ' '.join(rendered)


def line(iast, end=None, verse=None):
    """Transliterate one half-verse line. end: None, 'danda' or 'double'."""
    padas = [p.strip() for p in iast.split(';')]
    out = ' '.join(_pada(p) for p in padas)
    if end == 'danda':
        out += ' ।'
    elif end == 'double':
        out += f' ॥ {str(verse).translate(DIGITS)} ॥'
    return out


# ---------- reverse converter (for the round-trip check only) ----------
_INV_CONS = {v: k for k, v in CONSONANTS.items()}
_INV_IND = {v[0]: k for k, v in VOWELS.items()}
_INV_DEP = {v[1]: k for k, v in VOWELS.items() if v[1]}
_INV_OTHER = {v: k for k, v in OTHER.items()}


def to_iast(deva):
    """Devanagari → IAST, without word division (spaces are dropped)."""
    out, i = [], 0
    chars = [c for c in deva if c not in ' ।॥०१२३४५६७८९']
    while i < len(chars):
        c = chars[i]
        if c in _INV_CONS:
            out.append(_INV_CONS[c])
            nxt = chars[i + 1] if i + 1 < len(chars) else ''
            if nxt == VIRAMA:
                i += 2
                continue
            if nxt in _INV_DEP:
                out.append(_INV_DEP[nxt])
                i += 2
                continue
            out.append('a')
        elif c in _INV_IND:
            out.append(_INV_IND[c])
        elif c in _INV_OTHER:
            out.append(_INV_OTHER[c])
        else:
            raise ValueError(f'unexpected character {c!r} in {deva!r}')
        i += 1
    return ''.join(out)


def strip_iast(iast):
    """IAST with word division and pāda separators removed, for comparison."""
    return re.sub(r"[\s;]", '', unicodedata.normalize('NFC', iast))
