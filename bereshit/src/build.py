"""Render docs/bereshit/index.html from the witnesses and the translation.

Run from the repo root:  python3 bereshit/src/build.py
Uses only the standard library. Output is a single self-contained page.
Three columns on wide screens: English translation, Septuagint (Greek), commentary.
"""
import html
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "docs" / "bereshit" / "index.html"

sys.path.insert(0, str(HERE))
from translation import T, APP, TRAD, NAMES  # noqa: E402
from alignment import A  # noqa: E402
import re  # noqa: E402

heb = json.loads((HERE / "witness-hebrew.json").read_text(encoding="utf-8"))["verses"]
lxx = json.loads((HERE / "witness-lxx.json").read_text(encoding="utf-8"))["verses"]


def esc(s):
    return html.escape(s, quote=False)


HEBRUN = re.compile(r"[\u0591-\u05f4\ufb1d-\ufb4f]+(?:[ \u05be][\u0591-\u05f4\ufb1d-\ufb4f]+)*")


def rich(s):
    """Escape prose and isolate each run of Hebrew so it reads right to left inside English."""
    out, pos = [], 0
    for m in HEBRUN.finditer(s):
        out.append(esc(s[pos:m.start()]))
        out.append(f'<bdi lang="he" class="hw">{esc(m.group(0))}</bdi>')
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out)


def tokenise(ref):
    """Hebrew tokens for a verse: split on spaces and maqqef, drop sof pasuq and markers."""
    v = heb[ref].replace("\u05c3", "").replace("{פ}", "").replace("{ס}", "")
    return [t for t in re.split(r"[\s\u05BE]+", v) if t.strip()]


def chapter_of(ref):
    return int(ref.split(":")[0])


CSS = """
:root{
  --bg:#faf8f4;--bg-card:#fff;--text:#2c2c2c;--text-dim:#6b6b6b;--text-light:#999;
  --accent:#5a4a3a;--rule:rgba(0,0,0,.1);--card-border:rgba(0,0,0,.08);
  --hebrew:#3d3428;--gloss-bg:#f3efe7;--greek:#4a4032;
}
@media(prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#1a1a1a;--bg-card:#242424;--text:#e0ddd8;--text-dim:#9a9590;--text-light:#6b6560;
    --accent:#c4b49a;--rule:rgba(255,255,255,.1);--card-border:rgba(255,255,255,.08);
    --hebrew:#d9cdb8;--gloss-bg:#202020;--greek:#cfc3ab;
  }
}
:root[data-theme="dark"]{
  --bg:#1a1a1a;--bg-card:#242424;--text:#e0ddd8;--text-dim:#9a9590;--text-light:#6b6560;
  --accent:#c4b49a;--rule:rgba(255,255,255,.1);--card-border:rgba(255,255,255,.08);
  --hebrew:#d9cdb8;--gloss-bg:#202020;--greek:#cfc3ab;
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:Inter,'Helvetica Neue',Helvetica,Arial,sans-serif;
  font-size:15px;font-weight:300;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
header{text-align:center;padding:clamp(48px,9vh,88px) 24px 32px}
h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:clamp(30px,5vw,44px);
  letter-spacing:.06em;margin-bottom:10px}
.sub{font-size:.8rem;font-weight:400;letter-spacing:.08em;text-transform:uppercase;color:var(--text-light)}
.intro{max-width:720px;margin:24px auto 0;padding:0 24px;color:var(--text-dim);font-size:.9rem}
.intro p+p{margin-top:12px}
.witness{max-width:720px;margin:28px auto 0;padding:18px 22px;border:1px solid var(--card-border);
  border-radius:6px;background:var(--bg-card);font-size:.84rem;color:var(--text-dim)}
.witness dt{font-weight:500;color:var(--text);margin-top:10px}
.witness dt:first-child{margin-top:0}
main{max-width:1240px;margin:0 auto;padding:0 20px 96px}
h2.ch{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:clamp(24px,3.6vw,30px);
  text-align:center;margin:64px 0 8px;letter-spacing:.03em;color:var(--text)}
.ch-rule{width:56px;height:1px;background:var(--accent);margin:0 auto 20px;opacity:.6}
.head{display:none}
.row{border-top:1px solid var(--rule);padding:22px 0;display:grid;grid-template-columns:minmax(0,1fr);gap:18px}
.row:last-child{border-bottom:1px solid var(--rule)}
.vn{display:block;font-size:.72rem;font-weight:400;letter-spacing:.08em;color:var(--text-light);
  margin-bottom:6px;font-variant-numeric:oldstyle-nums}
.tr .ln{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:1.22rem;line-height:1.5;color:var(--text)}
.gk{font-family:'Gentium Plus','GFS Didot','Times New Roman',serif;font-size:1.02rem;line-height:1.75;color:var(--greek)}
.gk .lbl{display:block;font-family:Inter,sans-serif;font-size:.7rem;letter-spacing:.06em;color:var(--text-light);margin-bottom:4px}
.cm{background:var(--gloss-bg);border-radius:6px;padding:16px 18px;font-size:.84rem;
  line-height:1.65;color:var(--text-dim)}
.cm .heb{direction:rtl;text-align:right;font-family:'SBL Hebrew','Ezra SIL','Noto Serif Hebrew',
  'Times New Roman',serif;font-size:1.05rem;line-height:1.9;color:var(--hebrew);margin-bottom:10px;
  unicode-bidi:isolate}
.cm p{margin:0}
.cm details{margin-top:12px;border-top:1px solid var(--rule);padding-top:10px}
.cm summary{cursor:pointer;font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}
.cm table{width:100%;border-collapse:collapse;margin-top:10px;font-size:.8rem}
.cm th{text-align:left;font-weight:500;color:var(--text-light);font-size:.68rem;letter-spacing:.06em;
  text-transform:uppercase;border-bottom:1px solid var(--rule);padding:4px 6px}
.cm td{vertical-align:top;padding:5px 6px;border-bottom:1px solid var(--rule)}
.cm td.h{direction:rtl;text-align:right;font-family:'SBL Hebrew','Ezra SIL','Noto Serif Hebrew','Times New Roman',serif;
  font-size:.95rem;color:var(--hebrew);white-space:nowrap}
.cm td.e{font-family:'Cormorant Garamond',Georgia,serif;font-size:1rem;color:var(--text)}
@media(min-width:1000px){
  .head{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.8fr) minmax(0,1.3fr);gap:28px;
    padding:10px 0 6px;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-light);
    border-bottom:1px solid var(--rule)}
  .row{grid-template-columns:minmax(0,1.1fr) minmax(0,.8fr) minmax(0,1.3fr);gap:28px;align-items:start}
  .gk .lbl{display:none}
  .cm{margin-top:0}
}
.app{margin-top:10px;font-size:.8rem;color:var(--text-dim)}.applbl{display:block;font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin-bottom:4px}.app ul{margin:0;padding-left:1.1em}.app li{margin-bottom:3px}.names table{width:100%;border-collapse:collapse;margin-top:10px}.names td{padding:6px;border-top:1px solid var(--rule);vertical-align:top;font-size:.86rem}.names td.e{font-family:'Cormorant Garamond',Georgia,serif;font-size:1rem;width:22%}.names td.h{direction:rtl;text-align:right;font-family:'SBL Hebrew','Ezra SIL','Noto Serif Hebrew','Times New Roman',serif;font-size:1.05rem;color:var(--hebrew);width:14%;white-space:nowrap}
bdi.hw{font-family:'SBL Hebrew','Ezra SIL','Noto Serif Hebrew','Times New Roman',serif;font-size:1.08em;color:var(--hebrew)}
footer{margin-top:48px;text-align:center;border-top:1px solid var(--rule);padding-top:28px;
  font-size:.82rem;color:var(--text-light)}
footer a{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--rule)}
"""


def render_app(ref):
    items = APP.get(ref, [])
    if not items:
        return ''
    lis = ''.join(f'<li>{rich(x)}</li>' for x in items)
    return f'<div class="app"><span class="applbl">Apparatus</span><ul>{lis}</ul></div>'


def render_trad(ref):
    items = TRAD.get(ref, [])
    if not items:
        return ''
    lis = ''.join(f'<li>{rich(x)}</li>' for x in items)
    return f'<div class="app trad"><span class="applbl">Rashi and Ibn Ezra</span><ul>{lis}</ul></div>'


def render_names():
    rows = ''.join(f'<tr><td class="h" lang="he">{esc(h)}</td><td class="e">{esc(n)}</td><td>{rich(m)}</td></tr>'
                   for h, n, m in NAMES)
    return ('<section class="names"><h2 class="ch">Names, and their roots</h2>'
            '<table><tbody>' + rows + '</tbody></table></section>')


def render_align(ref):
    toks = tokenise(ref)
    rows = []
    for idx, en, why in A[ref]:
        hebtxt = " ".join(toks[i] for i in idx) if idx else "\u2014"
        rows.append(
            f'<tr><td class="h">{esc(hebtxt)}</td><td class="e">{esc(en) or "&nbsp;"}</td>'
            f'<td>{rich(why)}</td></tr>'
        )
    return (
        '<details><summary>Word by word</summary><table><thead><tr>'
        '<th>Hebrew</th><th>English</th><th>Why</th></tr></thead><tbody>'
        + "".join(rows) + '</tbody></table></details>'
    )


def render_row(ref, lines, note):
    hebrew = heb[ref]
    greek = lxx[ref]["greek"]
    en = "\n    ".join(f'<span class="ln">{esc(ln)}</span>' for ln in lines)
    return (
        f'<article class="row" id="v{ref.replace(":", "-")}">\n'
        f'  <div class="tr"><span class="vn">{esc(ref)}</span>\n    {en}\n  </div>\n'
        f'  <div class="gk"><span class="lbl">Septuagint</span>{esc(greek)}</div>\n'
        f'  <div class="cm">\n'
        f'    <div class="heb" lang="he">{esc(hebrew)}</div>\n'
        f'    <p>{rich(note)}</p>\n'
        f'    {render_app(ref)}\n'
        f'    {render_trad(ref)}\n'
        f'    {render_align(ref)}\n'
        f'  </div>\n'
        f'</article>'
    )


def main():
    parts = []
    current = None
    for ref, lines, note in T:
        ch = chapter_of(ref)
        if ch != current:
            parts.append(f'<h2 class="ch">Chapter {ch}</h2>\n<div class="ch-rule"></div>')
            parts.append(
                '<div class="head" aria-hidden="true"><span>English</span>'
                '<span>Septuagint</span><span>Commentary</span></div>'
            )
            current = ch
        parts.append(render_row(ref, lines, note))

    body = "\n".join(parts)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bereshit · Genesis 1–4</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Gentium+Plus&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Bereshit</h1>
  <p class="sub">Genesis 1:1 &ndash; 4:18 &middot; Hebrew &rarr; English</p>
  <div class="intro">
    <p>An original translation, made from the Hebrew text with the Septuagint beside it, of the first verses of the book. The English is deliberately strange and primal: the aim is a text the reader does not recognise, not one they half remember. The middle column gives the Greek. The right-hand column carries the commentary: root sense, the readings the Septuagint takes instead, and every place the register bends the Hebrew.</p>
    <p>No published English translation was consulted.</p>
    <p><strong>Conventions.</strong> Elohim: Divinity. YHWH: the Lord. Adamah: the red earth. Erets: the ground (land only for place names). Nachash: the serpent. Ish and ishah are kept as the Hebrew for the pun. Each verse's apparatus lists the readings held open.</p>
  </div>
  <dl class="witness">
    <dt>Hebrew witness</dt>
    <dd>Sefaria API, Hebrew text of Genesis 1:1&ndash;4:18 (fetched 2026-10-14). 98 verses; Hebrew and English verse numbers coincide in this span.</dd>
    <dt>Greek witness</dt>
    <dd>Septuagint, Blue Letter Bible interlinear for Genesis 1&ndash;4 (fetched 2026-10-14). The edition is not stated on the page and is not confirmed here as Rahlfs.</dd>
  </dl>
</header>
<main>
{body}
{render_names()}
</main>
<footer>
  <p><a href="../">&larr; Large-Language Literature</a> &middot; Source on <a href="https://github.com/pnathan/large-language-literature">GitHub</a></p>
</footer>
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page)} bytes, {len(T)} verses)")


if __name__ == "__main__":
    main()
