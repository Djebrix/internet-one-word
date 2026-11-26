#!/usr/bin/env python3
"""The Internet in One Word.

Writes one word to /output/entry.txt: the whole internet, in a single word.
"""

import os

WORD = "feral"

# Why "feral": the whole internet in one word.
# - Fits: no owner, no leash, no house-training. Forums, feeds, comment
#   sections, group chats — all of it runs wild and unmoderated at heart.
# - Funny by itself: one adjective, and the reader pictures the internet
#   as a stray animal that cannot be domesticated.
# - Surprising: not the obvious "connected", "endless" or "addictive".
# - Lands in one beat: five letters, instantly readable, no explanation.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    word = WORD.strip().split()[0]  # exactly one word, nothing else
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    # Read back and enforce the gate: 1-30 UTF-8 chars, not only whitespace.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 30 and written.strip(), "entry fails gate"
    assert written == word, "entry.txt does not match the word"


if __name__ == "__main__":
    main()
