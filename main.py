#!/usr/bin/env python3
"""Copy entry.png to the output directory (stdlib only).

Verifies the copy byte-for-byte so a corrupt write fails loudly
instead of producing a silently different image.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTDIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    dst = os.path.join(OUTDIR, "entry.png")
    os.makedirs(OUTDIR, exist_ok=True)
    shutil.copyfile(SRC, dst)
    if sha256(SRC) != sha256(dst):
        raise SystemExit("entry.png copy failed verification")
    if os.path.getsize(SRC) != os.path.getsize(dst):
        raise SystemExit("entry.png copy size mismatch")


if __name__ == "__main__":
    main()
