#!/usr/bin/env python3
"""Group the parsed paragraphs (popolwuj-paragraphs.json) into translatable
sections, per the structure proposed during sourcing (see popol-vuh/CLAUDE.md
and the research notes). Paragraph id (p01-p97) is the authoritative citation
key; folio numbers are an approximate secondary reference only.
"""
import json
import os

SRC = os.path.dirname(os.path.abspath(__file__))

# (title, first_paragraph_num, last_paragraph_num) - inclusive, by paragraph
# number (not id string) so ranges are easy to read/adjust.
SECTIONS = [
    ("Prologue and the divine makers", 1, 5),
    ("The naming of the animals", 6, 7),
    ("The mud people and the wood people: two failed creations", 8, 9),
    ("Wuqub' Kaqix, Sipakna, and Kab'raqan", 10, 11),
    ("Junajpu and Xb'alanke move against Seven Macaw's household", 12, 12),
    ("Sipakna and the four hundred youths", 13, 13),
    ("Kab'raqan brought low", 14, 14),
    ("Jun Junajpu, Wuqub' Junajpu, and their sons Jun B'atz'/Jun Chowen", 15, 16),
    ("The ballcourt and the summons of the Xibalba lords", 17, 18),
    ("The Xibalba trial-houses and the death of the elder twins", 19, 19),
    ("Ixkik' and the calabash tree", 20, 22),
    ("Ixkik' brought before Xmukane", 23, 24),
    ("Birth of Junajpu and Xb'alanke", 25, 26),
    ("The younger twins as hunters", 27, 27),
    ("Jun B'atz' and Jun Chowen transformed", 28, 30),
    ("The ballgame equipment recovered; renewed summons to Xibalba", 31, 31),
    ("The road to Xibalba and the first trial-houses", 32, 35),
    ("Further trial-houses", 36, 37),
    ("The twins outwit the lords of Xibalba", 38, 40),
    ("Defeat of Jun Kame' and Wuqub' Kame'", 41, 43),
    ("Paxil and K'ayala': discovery of maize; the first four men and women", 44, 50),
    ("The K'iche' lineages and their patron gods Tojil, Awilix, Jaqawitz", 51, 52),
    ("Departure from Tulan; the long migration", 53, 55),
    ("Multiplication of languages, separation of the peoples", 56, 57),
    ("The wait for the dawn", 58, 60),
    ("Events preceding first light", 61, 61),
    ("First dawn; the hardening of the stone gods", 62, 64),
    ("Balam Ki'tze' and the first patriarchs", 65, 66),
    ("Wives obtained; further wanderings", 67, 68),
    ("Ajpatan, Makujutaj, and the patriarchs' sons", 69, 70),
    ("K'oka'ib', K'o'akutek, K'o'ajaw and the journey to Nakxit", 71, 73),
    ("Chi Ismachi' and the early K'iche' rulers", 74, 75),
    ("Founding of Q'umarkaj (Utatlan); the titled offices", 76, 82),
    ("Generations and offices of the lordly houses", 83, 86),
    ("Wars, later kings, and the coming of the Spaniards", 87, 89),
    ("The last rulers under Spanish rule; Ximenez's closing colophon", 90, 97),
]


def para_ids_in_range(lo, hi):
    # paragraph ids are p01..p97, no zero-padding beyond 2 digits, in order;
    # generate the plain sequence (all of 1..97 exist as ids even where one
    # language side is empty - see kiche_missing).
    return [f"p{n:02d}" for n in range(lo, hi + 1)]


def main():
    with open(os.path.join(SRC, "popolwuj-paragraphs.json"), encoding="utf-8") as f:
        paras = {p["id"]: p for p in json.load(f)}

    sections = []
    for i, (title, lo, hi) in enumerate(SECTIONS):
        pids = para_ids_in_range(lo, hi)
        kiche_text = " ".join(paras[pid]["kiche_text"] for pid in pids if pid in paras and paras[pid]["kiche_text"])
        spanish_text = " ".join(paras[pid]["spanish_text"] for pid in pids if pid in paras and paras[pid]["spanish_text"])
        folios = sorted(set(f for pid in pids if pid in paras for f in paras[pid]["kiche_folios"]))
        entities = sorted(set(e for pid in pids if pid in paras for e in paras[pid]["entities"]))
        missing_kiche_paras = [pid for pid in pids if pid in paras and paras[pid]["kiche_missing"]]
        sections.append({
            "id": f"s{i + 1:02d}",
            "title": title,
            "paragraph_ids": pids,
            "folios": folios,
            "kiche_text": kiche_text,
            "spanish_text": spanish_text,
            "entities": entities,
            "missing_kiche_paragraphs": missing_kiche_paras,
        })

    out_path = os.path.join(SRC, "sections.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sections, f, ensure_ascii=False, indent=1)

    covered = set()
    for _, lo, hi in SECTIONS:
        covered.update(range(lo, hi + 1))
    all_nums = set(range(1, 98))
    print(f"wrote {out_path}: {len(sections)} sections")
    print("paragraph numbers not covered by any section:", sorted(all_nums - covered))
    print("paragraph numbers covered by >1 section (overlap check):")
    seen = {}
    for idx, (_, lo, hi) in enumerate(SECTIONS):
        for n in range(lo, hi + 1):
            if n in seen:
                print(f"  p{n:02d} in both section {seen[n]} and {idx}")
            seen[n] = idx
    lengths = [(s["id"], len(s["kiche_text"]), len(s["spanish_text"])) for s in sections]
    short = [s for s in lengths if s[1] < 50]
    print("very short sections (kiche < 50 chars) - review:", short)


if __name__ == "__main__":
    main()
