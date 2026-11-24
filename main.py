#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry (@berkahmuse).

Writes one sentence to /output/entry.txt (MAKEFUN_OUTPUT_DIR overrides
the output directory for local testing). The pitch names a ridiculous
invention — the Guilt Showerhead — and the tiny everyday annoyance it
fixes: lingering too long in the shower. Instead of cutting the water
cold, it plays a sad violin solo, so shame, not the cold, gets you out.
The pitch is one sentence of 165 characters (gate: 1-220).
"""

import os
import sys

PITCH = (
    "The Guilt Showerhead pauses your water and plays a sad violin solo "
    "whenever you linger past five minutes, so shame, not the cold, "
    "finally gets you out of the shower."
)


def main() -> int:
    if not (1 <= len(PITCH) <= 220):
        print(f"entry is {len(PITCH)} chars, must be 1-220", file=sys.stderr)
        return 1
    if PITCH != PITCH.strip() or "\n" in PITCH or "\r" in PITCH:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
