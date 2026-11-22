#!/usr/bin/env python3
"""Entry for the make.fun bounty news-image-20261121.

Writes the front-page image for Saturday, 21 November 2026 to
$MAKEFUN_OUTPUT_DIR/entry.png by copying the pre-drawn image held in
this repository. Standard library only; deterministic; no network.

The copy is verified before the program reports success: the source
image must exist, the output directory is created if missing, and after
copying, the destination's byte size and SHA-256 are compared with the
source. Any mismatch (or a missing source) fails loudly on stderr
with a non-zero exit code instead of silently producing a bad image.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SRC):
        print(f"error: source image missing: {SRC}", file=sys.stderr)
        return 2
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print(
            f"error: copied size mismatch: source {src_size} bytes, "
            f"destination {dst_size} bytes",
            file=sys.stderr,
        )
        return 3
    if sha256_of(SRC) != sha256_of(dst):
        print("error: copied SHA-256 mismatch", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
