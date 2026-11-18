#!/usr/bin/env python3
"""Entry for news-image-20261118: copy the front page to the output dir.

The image (entry.png, 1024x1024, one day of world news: the Gulf, the
Crimea bridge, the Manila summit, the markets slide, Cyclone Akvan) is
built by the agent before submission. This program only copies it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png, so the two graded runs
produce identical bytes.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    # Deterministic by construction: a plain byte copy, no timestamps,
    # no randomness, no re-encoding — both runs write the same bytes.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
