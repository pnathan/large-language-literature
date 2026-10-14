"""Checks for the Bereshit source files. Standard library only.

Run from the repo root:  python3 -I bereshit/src/check.py

Checks, all of which must pass before a change is committed:
  1. Coverage: every Hebrew token of each verse is aligned exactly once.
  2. Fragments: every English fragment in alignment.py appears in the
     translation lines for its verse.
  3. Lines: no Hebrew script in the English lines (Hebrew belongs in the
     apparatus, not the translation).
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HEB = re.compile(r"[א-ת]")


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def hebrew_tokens(text):
    # Split on spaces and maqqef (U+05BE). Drop sof pasuq (U+05C3) and the
    # paragraph marks {פ} and {ס} (written with \u escapes below).
    text = text.replace("\u05c3", "")
    text = re.sub(r"\{[\u05e4\u05e1]\}", "", text)
    return [t for t in re.split(r"[ \u05be]+", text) if t]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    A = load("alignment").A
    T = load("translation").T
    witness = json.load(open(os.path.join(HERE, "witness-hebrew.json"), encoding="utf-8"))["verses"]
    problems = 0

    # 1. Coverage
    for ref, entries in A.items():
        n = len(hebrew_tokens(witness[ref]))
        seen = [i for idx, _f, _w in entries for i in idx]
        dup = sorted({i for i in seen if seen.count(i) > 1})
        miss = [i for i in range(n) if i not in seen]
        oor = [i for i in seen if i >= n]
        if dup or miss or oor:
            problems += 1
            print("coverage", ref, "dup", dup, "miss", miss, "out-of-range", oor)

    # 2. Fragments
    lines = {ref: norm(" ".join(ls)) for ref, ls, _n in T}
    for ref, entries in A.items():
        for idx, frag, _w in entries:
            if frag and norm(frag) not in lines.get(ref, ""):
                problems += 1
                print("fragment", ref, repr(frag))

    # 3. Hebrew in the English lines
    for ref, ls, _n in T:
        for x in ls:
            if HEB.search(x):
                problems += 1
                print("hebrew-in-lines", ref, repr(x[:60]))

    print("verses checked", len(A), "with problems", problems)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
