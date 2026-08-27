#!/usr/bin/env python3
"""Build docs/popol-vuh/index.html from sections.json + translations_current_best.json.

Stdlib only. Run: python3 popol-vuh/src/build.py
"""
import json
import html
import os

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "..", "..", "docs", "popol-vuh", "index.html")

MULTEPAL_URL = "https://github.com/Multepal/popolwuj-original"
LOC_URL = "https://www.loc.gov/item/2021668226"

# The traditional four-part division of the narrative, mapped onto the 36
# working sections (s01-s36). Boundaries follow the customary break points:
# Part I ends where the wood people are destroyed and the world is otherwise
# empty of humans; Part II is the hero twins' full arc, from their opening
# move against Seven Macaw's household through the defeat of the Xibalba
# lords; Part III runs from the maize people's creation through the first
# sunrise (the immediate ancestors' own story); Part IV is the genealogical
# matter proper, from the first patriarchs to the Spanish conquest.
PARTS = [
    {
        "num": "I",
        "title": "Creation",
        "gloss": "The makers speak the world into being; two failed attempts at people.",
        "first": 1,
        "last": 3,
    },
    {
        "num": "II",
        "title": "The Hero Twins and the Lords of Xibalba",
        "gloss": "Junajpu and Xb’alanke against the arrogant false gods, and against death itself.",
        "first": 4,
        "last": 20,
    },
    {
        "num": "III",
        "title": "The Maize People",
        "gloss": "The first true humans, shaped from white and yellow maize; the long wait for dawn.",
        "first": 21,
        "last": 27,
    },
    {
        "num": "IV",
        "title": "Migrations and the Genealogy of the K’iche’ Lords",
        "gloss": "The patriarchs, their descendants, and the lords of Q’umarkaj down to the Spanish conquest.",
        "first": 28,
        "last": 36,
    },
]


def load():
    with open(os.path.join(SRC, "sections.json"), encoding="utf-8") as f:
        sections = json.load(f)
    with open(os.path.join(SRC, "translations_current_best.json"), encoding="utf-8") as f:
        translations = json.load(f)
    return sections, translations


def esc(s):
    return html.escape(s or "", quote=False)


def part_for(section_num):
    for p in PARTS:
        if p["first"] <= section_num <= p["last"]:
            return p
    raise ValueError(f"section {section_num} has no part")


def citation_range(paragraph_ids):
    if not paragraph_ids:
        return ""
    if len(paragraph_ids) == 1:
        return paragraph_ids[0]
    return f"{paragraph_ids[0]}–{paragraph_ids[-1]}"


def render_source_block(section):
    pids = section.get("paragraph_ids", [])
    cite = citation_range(pids)
    missing = section.get("missing_kiche_paragraphs", [])
    missing_note = ""
    if missing:
        plural = "s" if len(missing) != 1 else ""
        missing_note = (
            f'<p class="srcnote srcnote-gap">The K’iche’ column is blank in the manuscript for '
            f'paragraph{plural} {", ".join(esc(m) for m in missing)}; only Ximénez’s Spanish survives '
            f"there, and the translation for that stretch draws on the Spanish alone.</p>"
        )
    kiche = section.get("kiche_text", "").strip()
    spanish = section.get("spanish_text", "").strip()
    kiche_html = (
        f'<div class="srccol"><h4>K’iche’ &mdash; Ayer MS 1515</h4><p class="kiche">{esc(kiche)}</p></div>'
        if kiche
        else ""
    )
    spanish_html = (
        f'<div class="srccol"><h4>Ximénez’s Spanish (source&#8209;language aid)</h4><p class="spanish">{esc(spanish)}</p></div>'
        if spanish
        else ""
    )
    return f"""<details class="source">
    <summary>K’iche’ source text &middot; {esc(cite)}</summary>
    <p class="srcnote">Ayer MS 1515, vol. 2 (Newberry Library / Library of Congress facsimile) is the
    <strong>sole surviving manuscript</strong> of this text &mdash; there is no second witness to compare
    against, unlike a multi-copy tradition. Paragraph id{"s" if len(pids) != 1 else ""} {esc(cite) or "&mdash;"} follow the Multepal Project’s
    diplomatic transcription, the citation key used throughout this edition.</p>
    {missing_note}
    <div class="srccols">{kiche_html}{spanish_html}</div>
  </details>"""


def render_translator_note(note):
    note = (note or "").strip()
    if not note:
        return ""
    return f"""<details class="tnote">
    <summary>Translator’s note</summary>
    <p>{esc(note)}</p>
  </details>"""


def render_section(section, translation):
    sid = section["id"]
    num = int(sid[1:])
    title = esc(section["title"])
    paragraphs = translation.get("paragraphs") or []
    para_html = "".join(f"<p>{esc(p)}</p>" for p in paragraphs)
    source_html = render_source_block(section)
    tnote_html = render_translator_note(translation.get("translator_note", ""))
    return f"""
<section class="passage" id="{sid}">
  <div class="pnum">{num:02d}</div>
  <h3>{title}</h3>
  <div class="text">{para_html}</div>
  <div class="apparatus">
    {tnote_html}
    {source_html}
  </div>
</section>
"""


def render_part(part, sections_by_id, translations):
    first, last = part["first"], part["last"]
    ids = [f"s{n:02d}" for n in range(first, last + 1)]
    body = "".join(
        render_section(sections_by_id[sid], translations[sid]) for sid in ids
    )
    return f"""
<div class="part" id="part-{part['num']}">
  <div class="part-head">
    <div class="part-num">Part {part['num']}</div>
    <h2>{esc(part['title'])}</h2>
    <p class="part-gloss">{esc(part['gloss'])}</p>
  </div>
  {body}
  <a class="to-contents" href="#contents">&uarr; Contents</a>
</div>
"""


def render_toc(sections_by_id):
    blocks = []
    for part in PARTS:
        items = []
        for n in range(part["first"], part["last"] + 1):
            sid = f"s{n:02d}"
            s = sections_by_id[sid]
            items.append(f'<li><a href="#{sid}"><span class="tnum">{n:02d}</span>{esc(s["title"])}</a></li>')
        blocks.append(f"""
  <div class="toc-part">
    <h3><span class="toc-roman">{part['num']}</span> {esc(part['title'])}</h3>
    <ol>{''.join(items)}</ol>
  </div>""")
    return "".join(blocks)


def render_sticky_nav():
    links = "".join(
        f'<a href="#part-{p["num"]}">{p["num"]}</a>' for p in PARTS
    )
    return f'<a href="#contents" class="toc-link">Contents</a>{links}'


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Popol Vuh</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Noto+Serif:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#f3ead4;
  --bg-card:#fbf5e6;
  --text:#241f16;
  --text-dim:#5c5340;
  --text-light:#8c8168;
  --jade:#0f6b52;
  --jade-dim:#3d8a72;
  --gold:#a97a1f;
  --red:#8f3a24;
  --rule:rgba(36,31,22,.15);
  --card-border:rgba(36,31,22,.13);
  --card-hover:rgba(36,31,22,.035);
}}
@media(prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --bg:#131e19;
    --bg-card:#1b2721;
    --text:#ecdfc4;
    --text-dim:#bcae8e;
    --text-light:#83795f;
    --jade:#52cda3;
    --jade-dim:#3d9b7c;
    --gold:#dfb35d;
    --red:#df8862;
    --rule:rgba(236,223,196,.14);
    --card-border:rgba(236,223,196,.12);
    --card-hover:rgba(236,223,196,.04);
  }}
}}
:root[data-theme="dark"]{{
  --bg:#131e19;
  --bg-card:#1b2721;
  --text:#ecdfc4;
  --text-dim:#bcae8e;
  --text-light:#83795f;
  --jade:#52cda3;
  --jade-dim:#3d9b7c;
  --gold:#dfb35d;
  --red:#df8862;
  --rule:rgba(236,223,196,.14);
  --card-border:rgba(236,223,196,.12);
  --card-hover:rgba(236,223,196,.04);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{
  background:var(--bg);
  color:var(--text);
  font-family:'Spectral','Noto Serif',Georgia,serif;
  font-size:17px;
  line-height:1.68;
  -webkit-font-smoothing:antialiased;
}}
::selection{{background:var(--jade);color:var(--bg)}}
a{{color:var(--jade)}}
a:hover{{color:var(--gold)}}
.backlink{{
  display:block;
  text-align:center;
  font-family:'Inter',sans-serif;
  font-size:.78rem;
  letter-spacing:.06em;
  padding:14px 24px 0;
  color:var(--text-light);
  text-decoration:none;
}}
.backlink:hover{{color:var(--jade)}}
header{{
  text-align:center;
  padding:clamp(28px,6vh,52px) 24px 40px;
  border-bottom:1px solid var(--rule);
}}
.sigil{{font-size:1.7rem;color:var(--gold);margin-bottom:8px}}
h1{{
  font-weight:600;
  font-size:clamp(32px,7vw,54px);
  letter-spacing:.01em;
}}
.sub{{
  font-family:'Inter',sans-serif;
  font-size:.84rem;
  font-weight:400;
  letter-spacing:.08em;
  text-transform:uppercase;
  color:var(--text-light);
  max-width:560px;
  margin:14px auto 0;
}}
.methodology{{
  max-width:680px;
  margin:26px auto 0;
  font-family:'Inter',sans-serif;
  font-size:.87rem;
  line-height:1.7;
  color:var(--text-dim);
  text-align:left;
  background:var(--bg-card);
  border:1px solid var(--card-border);
  border-radius:8px;
  padding:22px 26px;
}}
.methodology h2{{
  font-family:'Spectral',serif;
  font-size:1.08rem;
  margin-bottom:8px;
  color:var(--text);
}}
.methodology p{{margin-top:10px}}
.methodology a{{text-decoration:none;border-bottom:1px dotted var(--jade)}}
nav.sticky{{
  position:sticky;top:0;z-index:10;
  background:var(--bg);
  border-bottom:1px solid var(--rule);
  padding:10px 16px;
  display:flex;flex-wrap:wrap;gap:8px;
  align-items:center;
  justify-content:center;
  font-family:'Inter',sans-serif;
  font-size:.8rem;
}}
nav.sticky a{{
  color:var(--text-dim);
  text-decoration:none;
  padding:4px 10px;
  border-radius:4px;
  border:1px solid transparent;
}}
nav.sticky a.toc-link{{
  color:var(--jade);
  border-color:var(--jade-dim);
  font-weight:500;
  margin-right:6px;
}}
nav.sticky a:hover{{background:var(--card-border);color:var(--gold)}}
main{{max-width:760px;margin:0 auto;padding:0 24px 40px}}
#contents{{
  max-width:760px;margin:0 auto;
  padding:44px 24px 8px;
}}
#contents > h2{{
  font-size:1.4rem;
  text-align:center;
  margin-bottom:26px;
  color:var(--text);
}}
.toc-part{{margin-bottom:26px}}
.toc-part h3{{
  font-size:1.02rem;
  color:var(--jade);
  margin-bottom:10px;
  display:flex;align-items:baseline;gap:10px;
}}
.toc-roman{{
  font-family:'Inter',sans-serif;
  font-size:.72rem;
  font-weight:600;
  letter-spacing:.06em;
  color:var(--gold);
  border:1px solid var(--gold);
  border-radius:3px;
  padding:1px 6px;
}}
.toc-part ol{{list-style:none;columns:2;column-gap:28px}}
.toc-part li{{break-inside:avoid;margin-bottom:6px}}
.toc-part a{{
  display:block;
  text-decoration:none;
  color:var(--text-dim);
  font-size:.88rem;
  line-height:1.5;
}}
.toc-part a:hover{{color:var(--jade)}}
.tnum{{
  font-family:'Inter',sans-serif;
  font-size:.72rem;
  color:var(--text-light);
  margin-right:8px;
}}
@media(max-width:520px){{
  .toc-part ol{{columns:1}}
}}
.part{{margin-top:56px}}
.part-head{{
  text-align:center;
  margin-bottom:32px;
  padding-bottom:20px;
  border-bottom:2px solid var(--gold);
}}
.part-num{{
  font-family:'Inter',sans-serif;
  font-size:.76rem;
  letter-spacing:.18em;
  text-transform:uppercase;
  color:var(--gold);
  margin-bottom:6px;
}}
.part-head h2{{
  font-size:clamp(24px,4.5vw,34px);
  font-weight:600;
  color:var(--text);
}}
.part-gloss{{
  font-style:italic;
  color:var(--text-dim);
  margin-top:8px;
  font-size:.98rem;
}}
.passage{{
  position:relative;
  background:var(--bg-card);
  border:1px solid var(--card-border);
  border-radius:10px;
  padding:30px clamp(20px,4vw,42px);
  margin-bottom:22px;
}}
.pnum{{
  position:absolute;
  top:22px;right:26px;
  font-family:'Inter',sans-serif;
  font-size:.72rem;
  color:var(--text-light);
  letter-spacing:.08em;
}}
.passage h3{{
  font-size:1.2rem;
  font-weight:600;
  color:var(--jade);
  margin-bottom:16px;
  padding-right:36px;
  line-height:1.3;
}}
.text p{{margin-bottom:14px}}
.text p:last-child{{margin-bottom:0}}
.apparatus{{margin-top:20px;font-family:'Inter',sans-serif;font-size:.8rem}}
.apparatus details{{
  margin-top:8px;
  color:var(--text-dim);
  border-top:1px solid var(--rule);
  padding-top:10px;
}}
.apparatus summary{{
  cursor:pointer;
  color:var(--text-light);
  letter-spacing:.02em;
  list-style:none;
}}
.apparatus summary::-webkit-details-marker{{display:none}}
.apparatus summary::before{{content:"\\25B8\\2002";color:var(--gold)}}
.apparatus details[open] summary::before{{content:"\\25BE\\2002"}}
.apparatus summary:hover{{color:var(--jade)}}
.tnote p{{margin-top:10px;line-height:1.7}}
.srcnote{{margin-top:10px;line-height:1.6;color:var(--text-dim)}}
.srcnote-gap{{color:var(--red)}}
.srccols{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:14px}}
.srccol h4{{
  font-size:.72rem;
  letter-spacing:.06em;
  text-transform:uppercase;
  color:var(--text-light);
  margin-bottom:6px;
}}
.kiche, .spanish{{
  font-family:'Spectral','Noto Serif',Georgia,serif;
  font-size:.92rem;
  line-height:1.65;
  color:var(--text);
}}
@media(max-width:640px){{
  .srccols{{grid-template-columns:1fr}}
}}
.to-contents{{
  display:block;
  text-align:center;
  margin-top:12px;
  font-family:'Inter',sans-serif;
  font-size:.76rem;
  text-decoration:none;
  color:var(--text-light);
}}
.to-contents:hover{{color:var(--jade)}}
footer{{
  max-width:760px;margin:0 auto;
  text-align:center;
  border-top:1px solid var(--rule);
  padding:36px 24px 64px;
  font-family:'Inter',sans-serif;
  font-size:.82rem;
  color:var(--text-light);
}}
footer a{{color:var(--jade);text-decoration:none;border-bottom:1px solid var(--rule)}}
footer a:hover{{border-bottom-color:var(--jade)}}
footer p{{margin-top:8px}}
</style>
</head>
<body>
<a class="backlink" href="../">&larr; Large-Language Literature</a>
<header>
  <div class="sigil" aria-hidden="true">&#10021;</div>
  <h1>Popol Vuh</h1>
  <p class="sub">The Council Book of the Quiché Maya &middot; K’iche’ &rarr; English</p>
  <div class="methodology">
    <h2>Note on the text</h2>
    <p>This translation was made directly from the K’iche’ text of <strong>Ayer MS 1515</strong>,
    Father Francisco Ximénez’s early-eighteenth-century transcription of an older K’iche’ document,
    now lost. It survives in a single manuscript &mdash; unlike Gilgameš’s many cuneiform witnesses or
    Sappho’s scattered papyri, there is no second copy to collate against. The manuscript (Newberry
    Library, Chicago; digitized by the Library of Congress) sets K’iche’ and Ximénez’s own
    contemporary Spanish in parallel columns across fifty-six folios. Working text and paragraph
    citations come from the <a href="{multepal_url}">Multepal Project</a>’s diplomatic transcription.</p>
    <p>Ximénez’s Spanish is a genuine primary source &mdash; his own hand, written alongside the
    K’iche’ he was transcribing &mdash; and is consulted only as an aid for obscure vocabulary, never
    as the object of translation. No modern published English translation was ever consulted: not
    Recinos (1950), not Goetz &amp; Morley (1950), not Tedlock (1985/1996), not Christenson (2003), nor
    any other. Every section below was independently reviewed, across several rounds, for fidelity to
    the K’iche’ and for any resemblance to a known published translation that would suggest
    memorized rather than genuine translation. Gaps in the manuscript are marked honestly rather than
    silently bridged.</p>
  </div>
</header>
<nav class="sticky">{nav}</nav>
<section id="contents">
  <h2>Contents</h2>
  {toc}
</section>
<main>
{parts}
</main>
<footer>
  <p><a href="../">&larr; Large-Language Literature</a></p>
  <p>Source on <a href="https://github.com/pnathan/large-language-literature">GitHub</a></p>
</footer>
</body>
</html>
"""


def main():
    sections, translations = load()
    sections_by_id = {s["id"]: s for s in sections}
    nav_html = render_sticky_nav()
    toc_html = render_toc(sections_by_id)
    parts_html = "".join(render_part(p, sections_by_id, translations) for p in PARTS)
    out = PAGE.format(
        nav=nav_html,
        toc=toc_html,
        parts=parts_html,
        multepal_url=MULTEPAL_URL,
    )
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT} ({len(out)} bytes, {len(sections)} sections)")


if __name__ == "__main__":
    main()
