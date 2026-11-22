#!/usr/bin/env python3
"""Entry for the make.fun bounty news-image-20261121.

Writes the front-page image for Saturday, 21 November 2026 to
$MAKEFUN_OUTPUT_DIR/entry.png by copying the pre-drawn image held in
this repository. Standard library only; deterministic.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
