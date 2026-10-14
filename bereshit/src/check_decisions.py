"""Checks that the decided and kept items in bereshit/review-opus-questions.md
still hold in the current English. Standard library only.

Run from the repo root:  python3 -I bereshit/src/check_decisions.py
Each pair is (verse, phrase that must appear in that verse's English lines).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import translation  # noqa: E402

CHECKS = [
    ("1:2", "And dark was on the face of the deep"),
    ("1:3", "And there was light"),
    ("1:6", "water to water"),
    ("1:8", "these waters"),
    ("1:9", "gather and wait in one place"),
    ("1:14", "meeting-times"),
    ("1:16", "and the stars"),
    ("1:20", "living breath"),
    ("1:26", "oppress the fish of the sea"),
    ("1:28", "subdue it"),
    ("1:28", "Divinity said to them"),
    ("1:29", "every tree that has fruit with seed in it"),
    ("2:2", "quit, dropped"),
    ("2:2", "dropped all the work he had made"),
    ("2:4", "the table of heavens and ground"),
    ("2:6", "would well up"),
    ("2:6", "would soak"),
    ("2:9", "the Lord God made sprout"),
    ("2:9", "desirable to see"),
    ("2:10", "goes out of Eden"),
    ("2:10", "parts and becomes"),
    ("2:12", "bdolach"),
    ("2:15", "garden of Eden"),
    ("2:19", "each living breath"),
    ("2:24", "clings to his woman"),
    ("3:1", "craftier than any beast"),
    ("3:8", "pacing in the garden"),
    ("3:12", "gave to be with me"),
    ("3:14", "On your belly you will go."),
    ("3:14", "Dust you will eat, all the days"),
    ("3:16", "your thirst"),
    ("3:22", "and live forever"),
    ("4:7", "its thirst is toward you"),
    ("4:8", "Qayin said to Hevel his brother"),
    ("4:13", "too great to lift, too great to forgive"),
    ("4:18", "Lamekh"),
]


def main():
    lines = {ref: " | ".join(ls) for ref, ls, _n in translation.T}
    failures = 0
    for ref, phrase in CHECKS:
        ok = phrase in lines.get(ref, "")
        failures += not ok
        print("OK  " if ok else "FAIL", ref, repr(phrase))
    print("failures", failures, "of", len(CHECKS))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
