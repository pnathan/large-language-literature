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

CLOSED = [
    ("1:1", "At the start, Divinity cut"),
    ("1:2", "waste and void"),
    ("1:5", "Evening came"),
    ("1:8", "Evening came"),
    ("1:13", "Evening came"),
    ("1:31", "Evening came. Morning came."),
    ("1:11", "seeding seed"),
    ("1:12", "brought out a greening"),
    ("1:18", "by day and by night"),
    ("1:20", "let fliers fly"),
    ("1:21", "great sea-serpents"),
    ("1:22", "Let the fliers grow many"),
    ("1:26", "a human, in our image"),
    ("1:26", "every crawler that crawls"),
    ("1:27", "he cut him"),
    ("2:3", "the work that Divinity cut in the making"),
    ("2:5", "For the Lord God had not rained"),
    ("2:7", "the blast of lives"),
    ("2:17", "For on the day you eat"),
    ("2:18", "a help facing him"),
    ("2:21", "He took one of his ribs"),
    ("2:22", "the rib he had taken"),
    ("2:23", "This one, this time, is bone out of my bones"),
    ("2:24", "one meat"),
    ("2:25", "they were not ashamed"),
    ("3:4", "Dying, you will not die"),
    ("3:6", "She gave also to her man"),
    ("3:7", "made themselves loin-belts"),
    ("3:11", "He said: Who told you"),
    ("3:15", "his heel"),
    ("3:17", "In pain you will eat it"),
    ("3:19", "to dust you will return"),
    ("3:23", "to work the red earth"),
    ("4:1", "with the Lord"),
    ("4:2", "Hevel was a herder"),
    ("4:5", "Qayin burned hard"),
    ("4:5", "did not look on"),
    ("4:10", "are crying"),
    ("4:14", "you have driven me out"),
    ("4:14", "I will be hidden"),
    ("4:16", "Roaming"),
]


def main():
    lines = {ref: " | ".join(ls) for ref, ls, _n in translation.T}
    failures = 0
    for name, group in (("kept/decided", CHECKS), ("closed", CLOSED)):
        for ref, phrase in group:
            ok = phrase in lines.get(ref, "")
            failures += not ok
            print("OK  " if ok else "FAIL", name, ref, repr(phrase))
    print("failures", failures, "of", len(CHECKS) + len(CLOSED))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
