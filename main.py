#!/usr/bin/env python3
"""One Word, First Thought — the entry program.

The competition asks for exactly one word: the first word that comes to
mind, no topic, no explanation, no second draft. This program carries a
single word, checks that it really is one word, and hands it to the
grader at /output/entry.txt.

The word: nudiustertian — relating to the day before yesterday.
A word most people have never met, for a day everyone has lived:
the day before yesterday, named in a single breath. It is the kind of
word that makes a reader stop and ask, "there is a word for that?"
"""

import os

# The entry: one word, lowercase, no punctuation, no spaces.
CHOSEN_WORD = "nudiustertian"

# The gate allows 1 to 200 characters of UTF-8 text, not only whitespace.
MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_single_word(candidate: str) -> str:
    """Refuse anything that is not exactly one word.

    A valid entry is a single token: non-empty, no whitespace of any
    kind inside it, and short enough for the gate. Anything else is a
    bug in this program, so fail loudly instead of writing it out.
    """
    if not candidate:
        raise ValueError("entry word is empty")
    if len(candidate) > MAX_ENTRY_CHARS:
        raise ValueError(
            "entry word is %d characters, over the %d limit"
            % (len(candidate), MAX_ENTRY_CHARS)
        )
    pieces = candidate.split()
    if len(pieces) != 1:
        raise ValueError(
            "entry must be exactly one word, got %d pieces" % len(pieces)
        )
    if pieces[0] != candidate:
        raise ValueError("entry word carries stray whitespace")
    return candidate


def emit_word(word: str, destination: str) -> str:
    """Write the validated word to the output file, exactly as-is.

    No trailing newline, no extra text: the file holds the word and
    nothing else, so the judge reads one word and one word only.
    """
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    return word


def main() -> None:
    """Validate the word, write it out, and say it once on stdout."""
    word = check_single_word(CHOSEN_WORD)
    emit_word(word, OUTPUT_PATH)
    print(word)


if __name__ == "__main__":
    main()
