#!/usr/bin/env python3
import subprocess
import sys


def main() -> int:
    cmds = [
        [sys.executable, "-m", "build"],
    ]
    for c in cmds:
        print("$", " ".join(c))
        subprocess.check_call(c)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())