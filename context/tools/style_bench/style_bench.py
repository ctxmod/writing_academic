#!/usr/bin/env python3
"""style_bench: number a benchmark sample of reference-list entries.

Used to test ctxmod tool plumbing for the writing_academic module: pass
sample entries as argv and receive the numbered sample plus a count line.
"""
import sys


def main() -> int:
    entries = [a for a in sys.argv[1:] if a.strip()]
    for i, entry in enumerate(entries, 1):
        print(f"{i}. {entry}")
    noun = "entry" if len(entries) == 1 else "entries"
    print(f"benchmark sample: {len(entries)} {noun}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
