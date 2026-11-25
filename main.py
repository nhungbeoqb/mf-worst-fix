#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message -- the fix that made everything worse --
to /output/entry.txt. Pure Python 3 standard library, no inputs,
no randomness: the same line every run.
"""

import os

# The fix: a crash when a user had no avatar. The repair: give
# everyone an avatar. The avatar it picked: the engineer's own face.
# Tightened in revision: "crash on missing avatar" for "crash when
# user has no avatar", and "has my face" for "has my face as their
# avatar" -- the picture lands on its own, no explanation needed.
LINE = "fix: crash on missing avatar \u2014 every user now has my face"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
