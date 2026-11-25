#!/usr/bin/env python3
"""Write one original villain monologue to /output/entry.txt.

The speaker is a specific villain with a history and a scheme: fifty years
holding a mountain pass, collecting tolls, feeding ravens, keeping a curse
and a gate. The tiredness lives in the rhythm and the small deflections --
the sigh of "of course it's midnight", "Kneel, or don't", handing the hero
off to a steward and a ledger -- never in a plain statement of weariness.
The sting lands in the last line: the dark lord has climbed the stairs
four thousand times, so this time it is the hero's turn.

Gate, checked here exactly as the sealed scorer states it: /output/entry.txt
is UTF-8 text of 1 to 600 characters, not only white space. This monologue
is 96 words and 524 characters.
"""
import os

TEXT = (
    "So. The hero arrives at midnight \u2014 of course it's midnight. "
    "Fifty years I've held this pass, counted every toll, fed the ravens, "
    "polished the same black crown, and still you come up the stairs with "
    "your sword out and your speech rehearsed. Kneel, or don't. The floor "
    "is cold either way. My steward will take your name for the ledger; "
    "the curse stands; the gate stays shut. The kingdom can wait till "
    "morning \u2014 it has waited this long. One of us must climb these "
    "stairs, hero. I've climbed them four thousand times. Your turn."
)


def main():
    assert 1 <= len(TEXT) <= 600, "entry must be 1-600 characters"
    assert TEXT.strip(), "entry must not be only white space"
    assert TEXT == TEXT.strip(), "no leading/trailing whitespace"
    assert "  " not in TEXT, "no double spaces"
    assert 90 <= len(TEXT.split()) <= 110, "entry must be about 100 words"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
