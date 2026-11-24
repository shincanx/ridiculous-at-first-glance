#!/usr/bin/env python3
"""Entry for make.fun bounty u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds like a joke yet holds together as a real business,
to /output/entry.txt. Deterministic, standard library only, no network.
"""

import os

SENTENCE = (
    "We rent retired racehorses to burned-out offices as therapists - "
    "startups pay $400 an hour because a 500-kilo animal whose only "
    "agenda is carrots is the one meeting nobody can ruin."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
