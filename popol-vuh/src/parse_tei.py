#!/usr/bin/env python3
"""Parse the Multepal TEI XML transcription of Ayer MS 1515 vol. 2 (Popol Vuh)
into structured per-paragraph K'iche'/Spanish records with folio/witness metadata.

Source: https://github.com/Multepal/popolwuj-original (MIT licensed), itself
based on the Ohio State University Libraries' 2007 transcription of the
Newberry Library's Ayer MS 1515 (public domain facsimile, Library of Congress
mirror). See popol-vuh/CLAUDE.md for full sourcing notes.
"""
import xml.etree.ElementTree as ET
import json
import os

NS = {"tei": "http://www.tei-c.org/ns/1.0"}
SRC = os.path.dirname(os.path.abspath(__file__))


def local(tag):
    return tag.split("}")[-1] if "}" in tag else tag


BREAK = ("BREAK",)
HYPHEN_BREAK = ("HYPHEN_BREAK",)


def _append_text(parts, text):
    """Append an XML text/tail node to the token stream, dropping pure
    pretty-printing whitespace (any whitespace chunk containing a newline)
    so it can't sit between a HYPHEN_BREAK and its <lb> and defeat the
    word-rejoining logic. A bare space (an <rs> tail before the next <rs>,
    for instance) is real inter-word spacing and is kept."""
    if not text:
        return
    if text.strip() == "" and "\n" in text:
        return
    parts.append(text)


def extract_paragraph(p_elem):
    """Walk a <p> element, returning (text, lines, entities, folio_ids).
    text: continuous prose, mid-word manuscript-line hyphenation resolved
          (this is prose, not verse - the scribe's line wrap is not
          semantically meaningful, unlike a poem's line breaks).
    lines: list of strings, one per manuscript line (<lb>) - the diplomatic
           form, kept for citation purposes.
    entities: sorted list of ana= codes referenced in this paragraph.
    folio_ids: list of folio/side ids (<pb>) touched by this paragraph.
    """
    parts = []  # flat token stream: strings, BREAK, or HYPHEN_BREAK
    entities = set()
    folio_ids = []

    def walk(el):
        tag = local(el.tag)
        if tag == "note":
            return  # marginal notes are not body text
        if tag == "choice":
            # <choice><abbr>q'</abbr><expan>que</expan></choice>: use only
            # the expansion. Tail text after </choice> handled by caller.
            expan = el.find("tei:expan", NS)
            if expan is not None and expan.text:
                parts.append(expan.text)
            return
        if tag == "pb":
            fid = el.get("id") or el.get("corresp") or ""
            if fid:
                folio_ids.append(fid.lstrip("#"))
        if tag == "lb":
            # a HYPHEN_BREAK may already have been pushed by a preceding
            # <pc>-dash; otherwise this is an ordinary line break
            if not parts or parts[-1] is not HYPHEN_BREAK:
                parts.append(BREAK)
        if tag == "pc":
            txt = (el.text or "").strip()
            if txt in ("–", "-", "—"):
                parts.append(HYPHEN_BREAK)
            else:
                parts.append(txt)
        else:
            _append_text(parts, el.text)
        for child in el:
            walk(child)
            _append_text(parts, child.tail)

    walk(p_elem)

    # Build continuous prose text: BREAK -> space, HYPHEN_BREAK -> nothing
    # (mid-word wrap). Pretty-printing whitespace was already dropped at the
    # source by _append_text, so remaining text chunks are real content -
    # including real single-space separators between adjacent same-line
    # tags - and can just be concatenated directly.
    text_out = []
    for part in parts:
        if part is BREAK:
            text_out.append(" ")
        elif part is HYPHEN_BREAK:
            pass
        else:
            text_out.append(part)
    text = " ".join("".join(text_out).split())

    # build diplomatic per-line array: split at any break marker
    lines = []
    current = []
    for part in parts:
        if part is BREAK or part is HYPHEN_BREAK:
            line = "".join(current).strip()
            if line:
                lines.append(" ".join(line.split()))
            current = []
        else:
            current.append(part)
    tail_line = "".join(current).strip()
    if tail_line:
        lines.append(" ".join(tail_line.split()))

    return text, lines, sorted(entities), folio_ids


def sort_key(pid):
    body = pid[1:]
    if "." in body:
        base, sub = body.split(".", 1)
        return (int(base), int(sub))
    return (int(body), 0)


def base_id(pid):
    body = pid[1:]
    base = body.split(".", 1)[0]
    return f"p{base}"


def main():
    tree = ET.parse(os.path.join(SRC, "popolwuj-tei.xml"))
    root = tree.getroot()
    body = root.find(".//tei:body", NS)
    divs = body.findall("tei:div", NS)
    quc_div = next(d for d in divs if d.get("{http://www.w3.org/XML/1998/namespace}lang") == "quc")
    spa_div = next(d for d in divs if d.get("{http://www.w3.org/XML/1998/namespace}lang") == "spa")

    # Many <p> elements in the source have no xml:id/corresp at all - these
    # are continuations of the preceding labeled paragraph (the encoder
    # opened a fresh <p> at a folio break without starting a new logical
    # paragraph number). Attach them, in document order, to the last-seen
    # label within the same column.
    XML_ID = "{http://www.w3.org/XML/1998/namespace}id"

    quc_paras = {}
    current = None
    for p in quc_div.findall("tei:p", NS):
        pid = p.get(XML_ID)
        text, lines, entities, folios = extract_paragraph(p)
        if pid:
            current = pid
            quc_paras[current] = {"text": "", "lines": [], "entities": set(), "folios": []}
        if current is None:
            continue
        quc_paras[current]["text"] = (quc_paras[current]["text"] + " " + text).strip()
        quc_paras[current]["lines"].extend(lines)
        quc_paras[current]["entities"].update(entities)
        quc_paras[current]["folios"].extend(folios)

    # Spanish side has finer subdivision in places (e.g. p19.1, p19.2) than
    # the K'iche' column - group all Spanish sub-paragraphs (and their own
    # unlabeled continuations) under their base K'iche' paragraph number, in
    # document order.
    spa_raw = []
    current = None
    for p in spa_div.findall("tei:p", NS):
        corresp = p.get("corresp")
        pid = corresp.lstrip("#") if corresp else None
        text, lines, entities, folios = extract_paragraph(p)
        if pid:
            current = pid
            spa_raw.append([current, "", [], set(), []])
        if current is None:
            continue
        spa_raw[-1][1] = (spa_raw[-1][1] + " " + text).strip()
        spa_raw[-1][2].extend(lines)
        spa_raw[-1][3].update(entities)
        spa_raw[-1][4].extend(folios)
    spa_raw.sort(key=lambda t: sort_key(t[0]))

    spa_grouped = {}
    for pid, text, lines, entities, folios in spa_raw:
        b = base_id(pid)
        g = spa_grouped.setdefault(b, {"text": "", "lines": [], "entities": set(), "folios": [], "sub_ids": []})
        g["text"] = (g["text"] + " " + text).strip()
        g["lines"].extend(lines)
        g["entities"].update(entities)
        g["folios"].extend(folios)
        g["sub_ids"].append(pid)

    all_ids = sorted(set(quc_paras) | set(spa_grouped), key=sort_key)
    paragraphs = []
    for pid in all_ids:
        q = quc_paras.get(pid)
        s = spa_grouped.get(pid)
        paragraphs.append({
            "id": pid,
            "kiche_text": q["text"] if q else "",
            "kiche_lines": q["lines"] if q else [],
            "kiche_folios": q["folios"] if q else [],
            "kiche_missing": q is None,
            "spanish_text": s["text"] if s else "",
            "spanish_lines": s["lines"] if s else [],
            "spanish_folios": s["folios"] if s else [],
            "spanish_sub_ids": s["sub_ids"] if s else [],
            "entities": sorted(set(q["entities"] if q else []) | set(s["entities"] if s else [])),
        })

    out_path = os.path.join(SRC, "popolwuj-paragraphs.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paragraphs, f, ensure_ascii=False, indent=1)
    print(f"wrote {out_path}: {len(paragraphs)} paragraphs")

    empties = [p["id"] for p in paragraphs if not p["kiche_text"] or not p["spanish_text"]]
    print("paragraphs missing one side:", empties)
    print("total paragraphs:", len(paragraphs))
    total_kiche_chars = sum(len(p["kiche_text"]) for p in paragraphs)
    total_spa_chars = sum(len(p["spanish_text"]) for p in paragraphs)
    print(f"total K'iche' chars: {total_kiche_chars}, total Spanish chars: {total_spa_chars}")


if __name__ == "__main__":
    main()
