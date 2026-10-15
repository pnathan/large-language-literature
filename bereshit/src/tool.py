"""Bereshit tool: show, check and build the Genesis 1:1-4:18 edition.

Run from the repo root. Standard library only.

    python3 -I bereshit/src/tool.py show 1:1 [2:4 ...] [--sources]
        Print each verse: numbered Hebrew tokens, Greek, and the text-file block.
        --sources adds the full Rashi and Ibn Ezra comments on the verse.
    python3 -I bereshit/src/tool.py check
        Run every check. Exit status 1 on any problem.
    python3 -I bereshit/src/tool.py build
        Run the checks; if they pass, write docs/bereshit/index.html.

The edition lives in bereshit/text/ch1.txt ... ch4.txt and names.txt. The format
is in bereshit/CLAUDE.md, section "Text files".
"""
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TEXT = HERE.parent / "text"
OUT = ROOT / "docs" / "bereshit" / "index.html"

HEB_CHAR = "֑-״יִ-ﭏ"
HEBRUN = re.compile(f"[{HEB_CHAR}]+(?:[ ־][{HEB_CHAR}]+)*")
RTL_CHAR = HEB_CHAR + "\u0700-\u074f"
RTLRUN = re.compile(f"[{RTL_CHAR}]+(?:[ \u05be\u0700-\u070d][{RTL_CHAR}]+)*")
LATIN_TRANSLIT = re.compile(r"[āēīōūḥṭṣšʾʿ]")


def load_json(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))["verses"]


HEB = load_json("witness-hebrew.json")
LXX = load_json("witness-lxx.json")
RASHI = load_json("rashi.json")
IBN_EZRA = load_json("ibn-ezra.json")


# ---------------------------------------------------------------- parsing

FIELDS = {"note": "note", "app": "app", "rashi": "rashi", "ibn-ezra": "ibn_ezra"}


class ParseError(Exception):
    pass


def new_verse(ref, where):
    return {"ref": ref, "where": where, "lines": [], "note": "", "app": [],
            "rashi": [], "ibn_ezra": [], "words": []}


def parse_chapter(path):
    """Return the verses of one chapter file, in file order."""
    verses, cur, last = [], None, None
    for n, raw in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
        where = f"{path.name}:{n}"
        if raw.startswith("  ") and raw.strip():
            if last is None:
                raise ParseError(f"{where}: continuation line with nothing to continue")
            last[0][last[1]] = last[0][last[1]] + " " + raw.strip()
            continue
        line = raw.rstrip()
        last = None
        if not line or line.startswith("#"):
            continue
        if line.startswith("@ "):
            cur = new_verse(line[2:].strip(), where)
            verses.append(cur)
            continue
        if cur is None:
            raise ParseError(f"{where}: text before the first '@ ref' line")
        if line.startswith("> "):
            cur["lines"].append(line[2:].strip())
            continue
        if line.startswith("= "):
            parts = [p.strip() for p in line[2:].split("|", 2)]
            if len(parts) != 3:
                raise ParseError(f"{where}: a word line needs 'indices | English | why'")
            idx = () if parts[0] == "-" else tuple(int(x) for x in parts[0].split())
            en = "" if parts[1] == "-" else parts[1]
            cur["words"].append([idx, en, parts[2]])
            last = (cur["words"][-1], 2)
            continue
        key, sep, val = line.partition(":")
        if sep and key in FIELDS:
            f = FIELDS[key]
            if f == "note":
                if cur["note"]:
                    raise ParseError(f"{where}: second note for {cur['ref']}")
                cur["note"] = val.strip()
                last = (cur, "note")
            else:
                cur[f].append(val.strip())
                last = (cur[f], len(cur[f]) - 1)
            continue
        raise ParseError(f"{where}: unrecognised line: {line[:60]!r}")
    return verses


def load_paragraphs(verse=False):
    """Editorial paragraph starts {ref: reason}; with verse=True, the verses set as verse lines."""
    out = {}
    for raw in (TEXT / "paragraphs.txt").read_text(encoding="utf-8").split("\n"):
        if not raw.strip() or raw.startswith("#"):
            continue
        if raw.startswith("verse:") != verse:
            continue
        ref, _s, why = raw.removeprefix("verse:").partition("|")
        out[ref.strip()] = why.strip()
    return out


def mt_break(ref):
    """The Masoretic paragraph mark at the end of a verse: 'פ', 'ס' or ''."""
    m = re.search(r"\{([\u05e4\u05e1])\}", HEB[ref])
    return m.group(1) if m else ""


def load_text():
    verses = []
    for c in (1, 2, 3, 4):
        verses += parse_chapter(TEXT / f"ch{c}.txt")
    names = []
    for n, raw in enumerate((TEXT / "names.txt").read_text(encoding="utf-8").split("\n"), start=1):
        if raw.strip() and not raw.startswith("#"):
            parts = [p.strip() for p in raw.split("|")]
            if len(parts) != 3:
                raise ParseError(f"names.txt:{n}: needs 'Hebrew | English | meaning'")
            names.append(parts)
    return verses, names, parse_apparatus(TEXT / "apparatus.txt")


def parse_apparatus(path):
    """Return {'sigla': [(siglum, text)], 'sections': [{'title', 'paras', 'entries'}]}."""
    app = {"sigla": [], "sections": []}
    sec, ref, last = None, None, None
    for n, raw in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
        where = f"{path.name}:{n}"
        if raw.startswith("  ") and raw.strip():
            if last is None:
                raise ParseError(f"{where}: continuation line with nothing to continue")
            last[0][last[1]] = last[0][last[1]] + " " + raw.strip()
            continue
        line = raw.rstrip()
        last = None
        if not line or line.startswith("#") and not line.startswith("## "):
            continue
        if line.startswith("## "):
            sec = {"title": line[3:].strip(), "paras": [], "entries": [], "where": where}
            app["sections"].append(sec)
            ref = None
            continue
        if sec is None:
            raise ParseError(f"{where}: text before the first '## ' section")
        if line.startswith("p: "):
            sec["paras"].append(line[3:].strip())
            last = (sec["paras"], len(sec["paras"]) - 1)
        elif line.startswith("sig: "):
            sig, _s, text = line[5:].partition("|")
            app["sigla"].append([sig.strip(), text.strip()])
            last = (app["sigla"][-1], 1)
        elif line.startswith("@ "):
            ref = line[2:].strip()
        elif line.startswith("= "):
            if ref is None:
                raise ParseError(f"{where}: entry before any '@ ref'")
            sec["entries"].append({"ref": ref, "body": line[2:].strip(), "notes": [], "where": where})
            last = (sec["entries"][-1], "body")
        elif line.startswith("~ "):
            if not sec["entries"]:
                raise ParseError(f"{where}: note with no entry")
            sec["entries"][-1]["notes"].append(line[2:].strip())
            e = sec["entries"][-1]["notes"]
            last = (e, len(e) - 1)
        else:
            raise ParseError(f"{where}: unrecognised line: {line[:60]!r}")
    return app


def split_entry(body):
    """'lemma ] r1 {S1} ; r2 {S2}' -> (lemma, [(reading, [sigla])])."""
    lemma, sep, rest = body.partition(" ] ")
    if not sep:
        raise ParseError(f"entry without ' ] ': {body[:50]!r}")
    readings = []
    for part in rest.split(" ; "):
        m = re.fullmatch(r"(.*?)\s*\{([^{}]+)\}", part.strip(), flags=re.S)
        if not m:
            raise ParseError(f"reading without {{sigla}}: {part[:50]!r}")
        readings.append((m.group(1).strip(), m.group(2).split()))
    return lemma.strip(), readings


def consonants(s):
    s = s.replace("\u05be", " ")
    s = re.sub(r"[\u0591-\u05c7]", "", s)
    return re.sub(r"[^\u05d0-\u05ea ]", " ", s).translate(
        str.maketrans("\u05da\u05dd\u05df\u05e3\u05e5", "\u05db\u05de\u05e0\u05e4\u05e6")).split()


def tokens(ref):
    """Hebrew tokens of a verse: split on spaces and maqaf; sof pasuq and paragraph marks dropped."""
    v = HEB[ref].replace("׃", "")
    v = re.sub(r"\{[פס]\}", "", v)
    return [t for t in re.split(r"[\s־]+", v) if t]


def strip_marks(s):
    """Remove cantillation marks; keep consonants and vowel points."""
    return re.sub(r"[֑-ֽ֯]", "", s)


# ---------------------------------------------------------------- checks

def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def read_list(name):
    out = []
    for raw in (TEXT / name).read_text(encoding="utf-8").split("\n"):
        line = raw.split("#", 1)[0].strip()
        if line:
            out.append(line)
    return out


def apparatus_strings(v):
    yield "note", v["note"]
    for k in ("app", "rashi", "ibn_ezra"):
        for x in v[k]:
            yield k, x
    for _i, _e, why in v["words"]:
        yield "word", why


def check(verses, names):
    problems = []
    p = problems.append

    refs = [v["ref"] for v in verses]
    if refs != list(HEB):
        missing = [r for r in HEB if r not in refs]
        extra = [r for r in refs if r not in HEB]
        dup = sorted({r for r in refs if refs.count(r) > 1})
        p(f"verses: missing {missing} extra {extra} duplicated {dup}"
          + ("" if missing or extra or dup else " (order differs from the witness)"))

    forbidden = {w.lower() for w in read_list("translit.txt")}
    for v in verses:
        ref, where = v["ref"], v["where"]
        if ref not in HEB:
            continue
        n = len(tokens(ref))
        seen = [i for idx, _e, _w in v["words"] for i in idx]
        dup = sorted({i for i in seen if seen.count(i) > 1})
        miss = [i for i in range(n) if i not in seen]
        oor = sorted(i for i in seen if i >= n)
        if dup or miss or oor:
            p(f"{where} {ref}: alignment duplicated {dup} missing {miss} out of range {oor}")
        joined = norm(" ".join(v["lines"]))
        for _i, en, _w in v["words"]:
            if en and norm(en) not in joined:
                p(f"{where} {ref}: word-line English not in the verse lines: {en!r}")
        if not v["lines"]:
            p(f"{where} {ref}: no English lines")
        if not v["note"]:
            p(f"{where} {ref}: no note")
        for x in v["lines"]:
            if HEBRUN.search(x):
                p(f"{where} {ref}: Hebrew script in an English line: {x[:50]!r}")
        for kind, s in apparatus_strings(v):
            plain = HEBRUN.sub(" ", s)
            if LATIN_TRANSLIT.search(plain):
                p(f"{where} {ref}: transliteration mark in {kind}: {LATIN_TRANSLIT.search(plain).group(0)!r}")
            for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", plain):
                if w.lower().strip("'-") in forbidden:
                    p(f"{where} {ref}: transliterated word in {kind}: {w!r}")
    for h, _n, m in names:
        plain = HEBRUN.sub(" ", m)
        for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", plain):
            if w.lower().strip("'-") in forbidden:
                p(f"names.txt {h}: transliterated word: {w!r}")
        if not HEBRUN.fullmatch(h.replace(" / ", " ")):
            p(f"names.txt {h}: first column must be Hebrew")

    lines_by_ref = {v["ref"]: " | ".join(v["lines"]) for v in verses}
    for item in read_list("decisions.txt"):
        ref, _s, phrase = item.partition("|")
        ref, phrase = ref.strip(), phrase.strip()
        if phrase not in lines_by_ref.get(ref, ""):
            p(f"decisions.txt: {ref} no longer contains {phrase!r}")
    return problems


def check_apparatus(app):
    problems = []
    p = problems.append
    sigla = {sg for sg, _t in app["sigla"]}
    if len(sigla) != len(app["sigla"]):
        p("apparatus.txt: a siglum is defined twice")
    order = list(HEB)
    for sec in app["sections"]:
        last = -1
        for e in sec["entries"]:
            w = e["where"]
            if e["ref"] not in HEB:
                p(f"{w}: no verse {e['ref']}")
                continue
            i = order.index(e["ref"])
            if i < last:
                p(f"{w}: {e['ref']} out of order in section '{sec['title']}'")
            last = i
            try:
                lemma, readings = split_entry(e["body"])
            except ParseError as err:
                p(f"{w}: {err}")
                continue
            for _r, sg in readings:
                for x in sg:
                    if x not in sigla:
                        p(f"{w}: undefined siglum {x!r}")
            verse = " ".join(consonants(HEB[e["ref"]]))
            for piece in lemma.split("…"):
                c = " ".join(consonants(piece))
                if c and c not in verse:
                    p(f"{w}: lemma {piece.strip()!r} not in the Hebrew of {e['ref']}")
            for kind, text in [("entry", e["body"])] + [("note", x) for x in e["notes"]]:
                if LATIN_TRANSLIT.search(HEBRUN.sub(" ", text)):
                    p(f"{w}: transliteration mark in {kind}")
    return problems


# ---------------------------------------------------------------- show

def show(verses, refs, sources):
    by = {v["ref"]: v for v in verses}
    for ref in refs:
        if ref not in by:
            print(f"no verse {ref}")
            continue
        v = by[ref]
        print(f"== {ref}   ({v['where']})")
        print("Hebrew tokens:")
        for i, t in enumerate(tokens(ref)):
            print(f"  {i:>2} {strip_marks(t)}")
        print("Greek:", LXX[ref]["greek"])
        for x in v["lines"]:
            print(">", x)
        print("note:", v["note"])
        for k in ("app", "rashi", "ibn_ezra"):
            for x in v[k]:
                print(f"{k}:", x)
        for idx, en, why in v["words"]:
            print("=", " ".join(map(str, idx)) or "-", "|", en or "-", "|", why)
        if sources:
            for label, src in (("RASHI", RASHI), ("IBN EZRA", IBN_EZRA)):
                for c in src.get(ref, []):
                    print(f"[{label}]", c)
        print()


# ---------------------------------------------------------------- build

def esc(s):
    return html.escape(s, quote=False)


def rich(s):
    """Escape prose and isolate each run of Hebrew or Syriac so it reads right to left inside English."""
    out, pos = [], 0
    for m in RTLRUN.finditer(s):
        out.append(esc(s[pos:m.start()]))
        lang = "syc" if re.search("[\u0700-\u074f]", m.group(0)) else "he"
        out.append(f'<bdi lang="{lang}" class="hw">{esc(m.group(0))}</bdi>')
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out)


def render_list(label, items, cls="app"):
    if not items:
        return ""
    lis = "".join(f"<li>{rich(x)}</li>" for x in items)
    return f'<div class="{cls}"><span class="applbl">{label}</span><ul>{lis}</ul></div>'


def render_words(v):
    toks = tokens(v["ref"])
    rows = []
    for idx, en, why in v["words"]:
        heb = " ".join(toks[i] for i in idx) if idx else "—"
        rows.append(f'<tr><td class="h">{esc(heb)}</td><td class="e">{esc(en) or "&nbsp;"}</td>'
                    f"<td>{rich(why)}</td></tr>")
    return ('<details><summary>Word by word</summary><table><thead><tr>'
            '<th>Hebrew</th><th>English</th><th>Why</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></details>")


def render_verse(v):
    ref = v["ref"]
    en = "\n    ".join(f'<span class="ln">{esc(x)}</span>' for x in v["lines"])
    trad = [f"Rashi: {x}" for x in v["rashi"]] + [f"Ibn Ezra: {x}" for x in v["ibn_ezra"]]
    return (
        f'<article class="row" id="v{ref.replace(":", "-")}">\n'
        f'  <div class="tr"><a class="vn" href="#r{ref.replace(":", "-")}" title="Back to the text">{esc(ref)}</a>\n    {en}\n  </div>\n'
        f'  <div class="gk"><span class="lbl">Septuagint</span>{esc(LXX[ref]["greek"])}</div>\n'
        f'  <div class="cm">\n'
        f'    <div class="heb" lang="he">{esc(HEB[ref])}</div>\n'
        f'    <p>{rich(v["note"])}</p>\n'
        f'    {render_list("Apparatus", v["app"])}\n'
        f'    {render_list("Rashi and Ibn Ezra", trad, "app trad")}\n'
        f'    {render_words(v)}\n'
        f'  </div>\n'
        f'</article>'
    )


def render_names(names):
    rows = "".join(f'<tr><td class="h" lang="he">{esc(h)}</td><td class="e">{esc(n)}</td>'
                   f"<td>{rich(m)}</td></tr>" for h, n, m in names)
    return ('<section class="names"><h2 class="ch">Names, and their roots</h2>'
            "<table><tbody>" + rows + "</tbody></table></section>")


def render_apparatus(app):
    def sig(xs):
        return " ".join(f'<span class="sg">{esc(x)}</span>' for x in xs)
    out = ['<section class="apparatus" id="apparatus"><h2 class="ch">Critical apparatus</h2>']
    for sec in app["sections"]:
        out.append(f'<h3>{esc(sec["title"])}</h3>')
        out += [f"<p>{rich(x)}</p>" for x in sec["paras"]]
        if sec["title"] == "Sigla":
            out.append("<dl class=\"sigla\">" + "".join(
                f'<dt>{esc(a)}</dt><dd>{rich(b)}</dd>' for a, b in app["sigla"]) + "</dl>")
        cur = None
        for e in sec["entries"]:
            lemma, readings = split_entry(e["body"])
            rd = " ; ".join(f"{rich(r)} {sig(sg)}" for r, sg in readings)
            vn = f'<span class="avn">{esc(e["ref"])}</span> ' if e["ref"] != cur else '<span class="avn"></span> '
            cur = e["ref"]
            notes = "".join(f'<span class="anote">{rich(x)}</span>' for x in e["notes"])
            out.append(f'<p class="ae">{vn}{rich(lemma)}<span class="br">]</span> {rd}{notes}</p>')
    out.append("</section>")
    return "\n".join(out)


def render_reading(verses):
    """The reading text: paragraphs by the Masoretic marks and the editorial breaks."""
    starts, poem = load_paragraphs(), load_paragraphs(verse=True)
    title = {"\u05e4": "open paragraph (petuchah) in the Masoretic text",
             "\u05e1": "closed paragraph (setumah) in the Masoretic text"}
    out = ['<section class="reading" id="reading"><h2 class="ch">The text</h2>'
           '<div class="ch-rule"></div>']
    para, chapter, kind = [], None, "prose"
    def flush(mark=""):
        if para:
            end = (f' <span class="pm" lang="he" title="{title[mark]}">{mark}</span>' if mark else "")
            if kind == "verse":
                body = "".join(para)
                body = body[:-len("</span>")] + end + "</span>"
                out.append('<div class="rd poem">' + body + "</div>")
            else:
                out.append('<p class="rd">' + " ".join(para) + end + "</p>")
            para.clear()
    for v in verses:
        ref = v["ref"]
        c, n = ref.split(":")
        k = "verse" if ref in poem else "prose"
        if ref in starts or k != kind:
            flush()
            kind = k
        if c != chapter:
            flush()
            out.append(f'<h3 class="rch">Chapter {c}</h3>')
            chapter = c
        anchor = ref.replace(":", "-")
        label = ref if n == "1" else n
        num = f'<a class="rv" id="r{anchor}" href="#v{anchor}">{label}</a>'
        if kind == "verse":
            para.append("".join(f'<span class="ln">{num if i == 0 else ""}{esc(x)}</span>'
                                for i, x in enumerate(v["lines"])))
        else:
            para.append(num + " ".join(esc(x) for x in v["lines"]))
        if mt_break(ref):
            flush(mt_break(ref))
    flush()
    out.append('<p class="rnote">Paragraphs follow the open (\u05e4) and closed (\u05e1) divisions of the '
               'Masoretic text; inside the long units 2:4–3:15, 3:17–21 and 4:1–18 the breaks are '
               'editorial and unmarked. 2:23 and 3:14–19 are set as verse, in the lines of the translation. Each verse number leads to its row below.</p></section>')
    return "\n".join(out)


def build(verses, names, app):
    parts, current = [], None
    for v in verses:
        ch = v["ref"].split(":")[0]
        if ch != current:
            parts.append(f'<h2 class="ch">Chapter {ch}</h2>\n<div class="ch-rule"></div>')
            parts.append('<div class="head" aria-hidden="true"><span>English</span>'
                         '<span>Septuagint</span><span>Commentary</span></div>')
            current = ch
        parts.append(render_verse(v))
    page = (HERE / "template.html").read_text(encoding="utf-8")
    page = page.replace("{{READING}}", render_reading(verses))
    page = page.replace("{{BODY}}", "\n".join(parts)).replace("{{NAMES}}", render_names(names))
    page = page.replace("{{APPARATUS}}", render_apparatus(app))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(verses)} verses)")


# ---------------------------------------------------------------- main

def main(argv):
    if not argv or argv[0] not in ("show", "check", "build"):
        print(__doc__)
        return 2
    try:
        verses, names, app = load_text()
    except ParseError as e:
        print("parse error:", e)
        return 1
    if argv[0] == "show":
        refs = [a for a in argv[1:] if not a.startswith("--")]
        show(verses, refs, "--sources" in argv)
        return 0
    problems = check(verses, names) + check_apparatus(app)
    order = list(HEB)
    last = -1
    for ref in load_paragraphs(verse=True):
        if ref not in HEB:
            problems.append(f"paragraphs.txt: no verse {ref}")
    for ref in load_paragraphs():
        if ref not in HEB:
            problems.append(f"paragraphs.txt: no verse {ref}")
            continue
        if order.index(ref) <= last:
            problems.append(f"paragraphs.txt: {ref} out of order")
        last = order.index(ref)
        prev = order[order.index(ref) - 1] if order.index(ref) else None
        if prev and mt_break(prev):
            problems.append(f"paragraphs.txt: {ref} already starts a Masoretic paragraph")
    for x in problems:
        print(x)
    print(f"checked {len(verses)} verses: {len(problems)} problems")
    if problems:
        return 1
    if argv[0] == "build":
        build(verses, names, app)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
