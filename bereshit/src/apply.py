"""Apply a reviewed set of text changes to the Bereshit source, then check and build.

Usage (from the repo root):
    python3 -I bereshit/src/apply.py changes.json

changes.json is a list of objects:
    {"file": "translation.py" | "alignment.py" | "lexicon.md",
     "old": "exact text to find",
     "new": "replacement text",
     "count": 1}          # optional: expected number of matches (default 1)

Every change is checked before anything is written. If any change finds the
wrong number of matches, nothing is written and the script exits with status 2.
If the changes apply, check.py runs; if the checks pass, the page is rebuilt.
Commit the result yourself after reviewing the diff.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ALLOWED = {"translation.py", "alignment.py", "lexicon.md"}


def main(path):
    changes = json.load(open(path, encoding="utf-8"))
    texts = {}
    errors = []
    for i, ch in enumerate(changes):
        f = ch["file"]
        if f not in ALLOWED:
            errors.append(f"change {i}: file {f!r} is not one of {sorted(ALLOWED)}")
            continue
        if f not in texts:
            texts[f] = open(os.path.join(HERE, f), encoding="utf-8").read()
        n = texts[f].count(ch["old"])
        want = ch.get("count", 1)
        if n != want:
            errors.append(f"change {i} in {f}: found {n} matches, expected {want}: {ch['old'][:60]!r}")
            continue
        texts[f] = texts[f].replace(ch["old"], ch["new"])
    if errors:
        print("\n".join(errors))
        print("nothing written")
        return 2
    for f, t in texts.items():
        open(os.path.join(HERE, f), "w", encoding="utf-8").write(t)
        print("updated", f)
    rc = subprocess.call([sys.executable, "-I", os.path.join(HERE, "check.py")])
    if rc != 0:
        print("checks failed; the source is changed but the page was not rebuilt")
        return rc
    subprocess.call([sys.executable, "-I", os.path.join(HERE, "build.py")], stdout=subprocess.DEVNULL)
    print("rebuilt docs/bereshit/index.html; review the diff and commit")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
