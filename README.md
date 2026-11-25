[![Make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/firlifirrizqi/fortune-in-a-pot-makefun/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/firlifirrizqi/fortune-in-a-pot-makefun/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

# Fortune in a Pot

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9) of the same name: a single line, at most 120 characters, telling a houseplant's fortune — kind, funny, and unmistakably about the plant on the windowsill.

## The line

> Soon you'll sprout a brand-new leaf, and the whole windowsill will pretend it saw it coming. It didn't.

## How it works

`main.py` writes that single line (103 characters, within the 120-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. A `verify()` helper re-reads the file and asserts it is byte-identical to the entry, 1–120 characters, a single line, and not only whitespace.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
