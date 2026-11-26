# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Djebrix/internet-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Djebrix/internet-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the [make.fun bounty "The Internet in One Word"](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b): describe the whole internet in a single word.

## The word

**feral**

No owner, no leash, no house-training. Forums, feeds, comment sections, group chats — all of it runs wild and unmoderated at heart. One adjective, and the reader pictures the internet as a stray animal that cannot be domesticated.

## How it works

`main.py` writes exactly one word to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
# feral
```

The program enforces the gate itself on every run: the output is read back and asserted to be 1–30 UTF-8 characters, not only whitespace, and exactly the chosen word. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
