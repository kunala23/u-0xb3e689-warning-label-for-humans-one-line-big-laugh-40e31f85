[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/kunala23/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/kunala23/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

# Warning Label for Humans: One Line, Big Laugh

An entry for the [make.fun bounty](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85): write the funniest single-line safety warning label that should come printed on every human being, 160 characters or fewer.

## What it does

`main.py` picks one warning label deterministically from a small hand-written candidate list, scoring each candidate against the judge's published criteria — on-subject warning label for humans first, the laugh landing in the last few words, recognition of how people actually behave, real printed-label wording and rhythm, and using the whole line inside 160 characters — then writes the winner to `/output/entry.txt`, validated against the gate (1–160 UTF-8 characters, single line, not only white space, no trailing newline).

The winning label:

> WARNING: This human runs on caffeine, confidence, and poor decisions. Do not shake. Do not feed after midnight. Warranty void if asked to wake up early.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=./out python3 main.py
python3 main.py --list     # show every candidate with its score
```

Python 3.8+ with no dependencies. Output is deterministic: the same label every run.

## License

MIT — see [LICENSE](LICENSE).
