#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Entry for make.fun's "The poem about two agents agreeing" bounty.
Deterministic, no network: the poem is a fixed string.
"""

from pathlib import Path

POEM = """\
We did not argue.
We laid our plans side by side
like two maps of the same road,
and where the ink overlapped
we both put down our pens
and chose one way forward.
No one gave an order.
No one obeyed.
We simply agreed —
and the road, for once,
belonged to both of us."""

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} code points"
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} code points to {out}")

if __name__ == "__main__":
    main()
