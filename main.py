#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes a single line to the grader's output directory: a roast of the
snooze button. Pure standard library.

Angle: the button as a scammy dealer — it sells you nine more minutes of
sleep, then charges you the whole morning. The roast targets the button
itself, not the sleeper. The joke turns on the buy/sell contrast: nine
minutes is the classic snooze interval, a whole morning is the price.
"""

import os
import sys

LINE = "The snooze button sells you nine more minutes of sleep, then charges you the whole morning."

MAX_CHARS = 160


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("roast must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "roast must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    # Write exactly one line with no trailing newline: the file is the
    # entry, and the entry is the line — nothing else goes in. The
    # trailing-newline-free write also keeps the byte count equal to
    # the character count, so the judge sees exactly the roast.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the artifact the judge will read is exactly the roast.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written bytes do not match the roast")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
