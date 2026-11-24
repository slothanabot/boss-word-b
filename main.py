#!/usr/bin/env python3
"""One Word for the Boss (Account B).

Writes a single word to /output/entry.txt: the word the boss uses for
every deadline.

The word is "aspirational". The boss never says a deadline is tight, or
late, or impossible -- every deadline is "aspirational". The team hears
the same word and calls it something else entirely: a fantasy, a joke,
next quarter. That is the whole joke and why it is true: the boss lives
in aspiration, the team lives in the calendar, and the gap between the
two is where the laughter lives. It needs no caption, it works for a
boss in a kitchen, a warehouse or an office, and it is the word a
colleague repeats at lunch -- "oh, ours is aspirational too" -- because
every office has one.

Deterministic: no input, no randomness, no clock, no network. The output
is always exactly the twelve characters "aspirational" (no trailing
newline), inside the sealed gate of 1 to 30 characters.
"""

import os

WORD = "aspirational"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
