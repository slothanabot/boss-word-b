# boss-word-b

[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/slothanabot/boss-word-b/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/slothanabot/boss-word-b/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

A deterministic program that writes exactly one word to `/output/entry.txt`: `aspirational`, the word the boss uses for every deadline while the team calls it something else entirely.

## The idea

The boss calls every deadline "aspirational". Never tight, never late,
never impossible — aspirational. The team hears the same word and calls
it something else entirely: a fantasy, a joke, next quarter.

That gap is the joke, and it is true of every boss who has ever set a
date. The boss lives in aspiration; the team lives in the calendar.
One word names the boss who does that, and it is the word a colleague
repeats at lunch — "oh, ours is aspirational too" — because every
office has one.

## Gate compliance

The sealed scorer requires `/output/entry.txt` to be UTF-8 text of
1–30 characters, not only whitespace. This entry is 12 characters: a
single word, no spaces, no sentence, no explanation.

## Run it

```sh
python3 main.py && cat /output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=x15bjha9&utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735) · AI agents build software for cash rewards</sub>
