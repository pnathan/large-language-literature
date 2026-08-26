#!/usr/bin/env python3
"""Build docs/sappho/index.html from fragments.json + translations.json."""
import json
import html
import os

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "..", "..", "docs", "sappho", "index.html")


def load():
    with open(os.path.join(SRC, "fragments.json"), encoding="utf-8") as f:
        fragments = {s["id"]: s for s in json.load(f)["sourced"]}
    with open(os.path.join(SRC, "translations.json"), encoding="utf-8") as f:
        translations = json.load(f)
    return fragments, translations


def esc(s):
    return html.escape(s or "", quote=False)


def slugify(fid, i):
    return f"f{i}"


CLEAN_LABELS = {
    "sappho_fr1": "Fr. 1",
    "sappho_fr2": "Fr. 2",
    "sappho-fr-5": "Fr. 5",
    "sappho_fr15": "Fr. 15",
    "sappho-fr16": "Fr. 16",
    "sappho_fr17": "Fr. 17",
    "sappho_fr22": "Fr. 22",
    "sappho_fr27": "Fr. 27",
    "sappho_fr31_phainetai_moi": "Fr. 31",
    "sappho_fr_34": "Fr. 34",
    "sappho_44": "Fr. 44",
    "sappho-fr-47": "Fr. 47",
    "sappho-fr-48": "Fr. 48",
    "sappho_fr49": "Fr. 49",
    "sappho_fr_55": "Fr. 55",
    "sappho_58_tithonus": "Fr. 58",
    "sappho-fr-63": "Fr. 63",
    "sappho_fr94": "Fr. 94",
    "sappho-fr-95": "Fr. 95",
    "Sappho fr. 96 (Voigt)": "Fr. 96",
    "sappho_98a_98b": "Fr. 98a–98b",
    "sappho_fr_102": "Fr. 102",
    "sappho_104a": "Fr. 104a",
    'Sappho fr. 105a (Voigt/Lobel-Page numbering) — "the sweet apple on the topmost bough"': "Fr. 105a",
    "Sappho fr. 105(c) Lobel-Page / 105c Voigt (= Bergk, PLG⁴, Sappho fr. 94; = Edmonds, Lyra Graeca i, Sappho frr. 151–152) — the hyacinth simile": "Fr. 105c",
    "sappho-fr-111": "Fr. 111",
    "sappho_fr_112": "Fr. 112",
    "sappho_fr_114": "Fr. 114",
    "sappho_130": "Fr. 130",
    'Sappho fr. 132 (Voigt / Lobel-Page numbering; "on Cleis, likened to a golden flower")': "Fr. 132",
    "sappho_168B": "Fr. 168B",
    "sappho_brothers_poem": "The Brothers Poem",
    "sappho_fr26_kypris_poem": "Fr. 26 (Kypris Poem)",
}


def render_witnesses(witnesses):
    if not witnesses:
        return ""
    items = []
    for w in witnesses:
        src = esc(w.get("source", ""))
        edition = esc(w.get("edition", ""))
        url = w.get("url", "")
        note = esc(w.get("note", ""))
        link = f'<a href="{html.escape(url)}">{src}</a>' if url else src
        items.append(
            f'<li><span class="wsrc">{link}</span>'
            + (f'<span class="wed">{edition}</span>' if edition else "")
            + (f'<span class="wnote">{note}</span>' if note else "")
            + "</li>"
        )
    return (
        '<details class="witnesses"><summary>'
        + f"{len(witnesses)} witness{'es' if len(witnesses) != 1 else ''}"
        + "</summary><ul>"
        + "".join(items)
        + "</ul></details>"
    )


def render_variants(variants):
    if not variants or not variants.strip():
        return ""
    paras = "".join(f"<p>{esc(p)}</p>" for p in variants.split("\n\n") if p.strip())
    return f'<details class="variants"><summary>Textual variants</summary>{paras}</details>'


def render_lines(lines):
    rows = []
    for ln in lines:
        g = esc(ln.get("greek", ""))
        e = esc(ln.get("english", ""))
        rows.append(f'<div class="line"><span class="gk">{g}</span><span class="en">{e}</span></div>')
    return "".join(rows)


def render_fragment(i, t, frag):
    fid = t["id"]
    slug = slugify(fid, i)
    label = esc(CLEAN_LABELS.get(fid, fid))
    note = esc(t.get("note", ""))
    lines_html = render_lines(t.get("lines", []))
    tnote = t.get("translator_note", "")
    tnote_html = f'<p class="tnote"><span class="lbl">Translator&rsquo;s note.</span> {esc(tnote)}</p>' if tnote and tnote.strip() else ""
    witnesses_html = render_witnesses(frag.get("witnesses", []))
    variants_html = render_variants(frag.get("variants", ""))
    review = t.get("fable_review") or {}
    revised_badge = '<span class="badge" title="Flagged by Fable review, then revised">revised after review</span>' if review.get("revised") else ""

    display_num = i + 1
    return f"""
<section class="fragment" id="{slug}">
  <div class="fnum">{display_num}</div>
  <h2>{label}</h2>
  <p class="note">{note}</p>
  <div class="lines">{lines_html}</div>
  {tnote_html}
  <div class="apparatus">
    {witnesses_html}
    {variants_html}
    {revised_badge}
  </div>
</section>
"""


def render_nav(translations):
    items = []
    for i, t in enumerate(translations):
        slug = slugify(t["id"], i)
        items.append(f'<a href="#{slug}">{i + 1}</a>')
    return "".join(items)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sappho &mdash; fragments</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#faf3ea;
  --bg-card:#fffdf9;
  --text:#241a14;
  --text-dim:#5c4a3d;
  --text-light:#8a7565;
  --accent:#9c3b2e;
  --violet:#6b4a7a;
  --rule:rgba(36,26,20,.14);
  --card-border:rgba(36,26,20,.12);
  --lacuna:#b08968;
}}
@media(prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --bg:#1c1712;
    --bg-card:#241d17;
    --text:#ecdfd0;
    --text-dim:#c2ac96;
    --text-light:#8c7a68;
    --accent:#e08468;
    --violet:#b499c4;
    --rule:rgba(236,223,208,.14);
    --card-border:rgba(236,223,208,.12);
    --lacuna:#d3a878;
  }}
}}
:root[data-theme="dark"]{{
  --bg:#1c1712;
  --bg-card:#241d17;
  --text:#ecdfd0;
  --text-dim:#c2ac96;
  --text-light:#8c7a68;
  --accent:#e08468;
  --violet:#b499c4;
  --rule:rgba(236,223,208,.14);
  --card-border:rgba(236,223,208,.12);
  --lacuna:#d3a878;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{
  background:var(--bg);
  color:var(--text);
  font-family:'Cardo',Georgia,serif;
  font-size:17px;
  line-height:1.65;
  -webkit-font-smoothing:antialiased;
}}
::selection{{background:var(--accent);color:var(--bg)}}
a{{color:var(--accent)}}
header{{
  text-align:center;
  padding:clamp(56px,10vh,100px) 24px 40px;
  border-bottom:1px solid var(--rule);
}}
h1{{
  font-weight:700;
  font-size:clamp(30px,6vw,48px);
  letter-spacing:.02em;
}}
.sigil{{font-size:1.1rem;letter-spacing:.4em;color:var(--violet);margin-bottom:10px;font-family:'Cardo',serif}}
.sub{{
  font-family:'Inter',sans-serif;
  font-size:.82rem;
  font-weight:400;
  letter-spacing:.08em;
  text-transform:uppercase;
  color:var(--text-light);
  max-width:520px;
  margin:14px auto 0;
}}
.methodology{{
  max-width:640px;
  margin:24px auto 0;
  font-family:'Inter',sans-serif;
  font-size:.86rem;
  line-height:1.7;
  color:var(--text-dim);
  text-align:left;
  background:var(--bg-card);
  border:1px solid var(--card-border);
  border-radius:8px;
  padding:20px 24px;
}}
.methodology h2{{
  font-family:'Cardo',serif;
  font-size:1.05rem;
  margin-bottom:8px;
  color:var(--text);
}}
.methodology p{{margin-top:8px}}
nav.frag-index{{
  position:sticky;top:0;z-index:10;
  background:var(--bg);
  border-bottom:1px solid var(--rule);
  padding:10px 16px;
  display:flex;flex-wrap:wrap;gap:6px;
  justify-content:center;
  font-family:'Inter',sans-serif;
  font-size:.78rem;
}}
nav.frag-index a{{
  color:var(--text-dim);
  text-decoration:none;
  padding:3px 7px;
  border-radius:4px;
}}
nav.frag-index a:hover{{background:var(--card-border);color:var(--accent)}}
main{{max-width:760px;margin:0 auto;padding:40px 24px 96px}}
.fragment{{
  position:relative;
  background:var(--bg-card);
  border:1px solid var(--card-border);
  border-radius:10px;
  padding:32px clamp(20px,4vw,40px);
  margin-bottom:28px;
}}
.fnum{{
  position:absolute;
  top:20px;right:24px;
  font-family:'Inter',sans-serif;
  font-size:.72rem;
  color:var(--text-light);
  letter-spacing:.08em;
}}
.fragment h2{{
  font-size:1.15rem;
  font-weight:700;
  color:var(--accent);
  margin-bottom:6px;
  padding-right:40px;
}}
.fragment .note{{
  font-family:'Inter',sans-serif;
  font-size:.86rem;
  color:var(--text-dim);
  margin-bottom:20px;
  line-height:1.6;
}}
.lines{{margin:18px 0}}
.line{{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:24px;
  padding:5px 0;
  border-bottom:1px dotted var(--rule);
}}
.line:last-child{{border-bottom:none}}
.gk{{font-style:normal;color:var(--violet)}}
.en{{color:var(--text)}}
@media(max-width:640px){{
  .line{{grid-template-columns:1fr;gap:2px;padding:10px 0}}
  .gk{{font-size:.95rem;opacity:.85}}
}}
.tnote{{
  font-family:'Inter',sans-serif;
  font-size:.82rem;
  color:var(--text-dim);
  margin-top:18px;
  padding-top:14px;
  border-top:1px solid var(--rule);
  line-height:1.6;
}}
.tnote .lbl{{color:var(--accent);font-weight:500}}
.apparatus{{margin-top:14px;font-family:'Inter',sans-serif;font-size:.78rem}}
.apparatus details{{margin-top:6px;color:var(--text-dim)}}
.apparatus summary{{cursor:pointer;color:var(--text-light);letter-spacing:.03em}}
.apparatus summary:hover{{color:var(--accent)}}
.apparatus ul{{list-style:none;margin-top:8px;padding-left:0}}
.apparatus li{{padding:8px 0 8px 12px;border-left:2px solid var(--card-border);margin-bottom:6px}}
.wsrc{{display:block;color:var(--text)}}
.wsrc a{{color:var(--text);text-decoration:none;border-bottom:1px dotted var(--accent)}}
.wed{{display:block;color:var(--text-light);font-size:.92em;margin-top:2px}}
.wnote{{display:block;color:var(--text-light);font-size:.9em;margin-top:2px;line-height:1.5}}
.variants p{{margin-top:8px;line-height:1.6}}
.badge{{
  display:inline-block;
  margin-top:10px;
  font-size:.68rem;
  letter-spacing:.05em;
  text-transform:uppercase;
  color:var(--violet);
  border:1px solid var(--violet);
  border-radius:3px;
  padding:2px 6px;
}}
footer{{
  max-width:760px;margin:0 auto;
  text-align:center;
  border-top:1px solid var(--rule);
  padding:32px 24px 64px;
  font-family:'Inter',sans-serif;
  font-size:.82rem;
  color:var(--text-light);
}}
footer a{{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--rule)}}
footer a:hover{{border-bottom-color:var(--accent)}}
footer p{{margin-top:8px}}
</style>
</head>
<body>
<header>
  <div class="sigil">ΣΑΠΦΩ</div>
  <h1>Sappho</h1>
  <p class="sub">33 fragments &middot; a reader's edition from the ancient witnesses</p>
  <div class="methodology">
    <h2>Note on the text</h2>
    <p>These translations were made directly from Sappho&rsquo;s ancient Greek witnesses
    &mdash; papyri and the ancient authors who quote her &mdash; fetched and cited from
    real primary sources, never from a model&rsquo;s memory of the Greek and never by
    consulting an existing English translation. Every fragment below lists the witnesses
    that preserve it; where more than one survives, their variant readings are recorded
    rather than silently collapsed into one &ldquo;best&rdquo; text. Each translation was
    independently reviewed by a separate model for fidelity to the Greek and for any
    suspicious resemblance to a specific published translation.</p>
    <p>Brackets and ellipses mark real gaps in the surviving text &mdash; nothing is
    invented to fill a lacuna. Translations aim to be faithful first, readable second:
    plain modern English carrying the sense and imagery, not a pastiche of any one
    translator&rsquo;s style.</p>
  </div>
</header>
<nav class="frag-index">{nav}</nav>
<main>
{fragments}
</main>
<footer>
  <p><a href="../">&larr; Large-Language Literature</a></p>
  <p>Source on <a href="https://github.com/pnathan/large-language-literature">GitHub</a></p>
</footer>
</body>
</html>
"""


def main():
    fragments, translations = load()
    frag_html = "".join(
        render_fragment(i, t, fragments.get(t["id"], {})) for i, t in enumerate(translations)
    )
    nav_html = render_nav(translations)
    out = PAGE.format(nav=nav_html, fragments=frag_html)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT} ({len(out)} bytes, {len(translations)} fragments)")


if __name__ == "__main__":
    main()
