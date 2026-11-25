"""The One-Liner Groan-Off entry.

Writes a single one-line dad joke to the output file.
Self-contained: no network, no external files.
"""

import os

JOKE = "My router and I are in couples therapy. It says we need to work on our connection."

MAX_LENGTH = 140


def resolve_output_path():
    """Output path from ENTRY_OUTPUT, defaulting to /output/entry.txt."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate_joke(joke):
    """A one-line dad joke: single line, non-empty, within the limit."""
    lines = joke.splitlines()
    if len(lines) != 1:
        raise ValueError("joke must be exactly one line")
    if not joke.strip():
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_LENGTH:
        raise ValueError("joke is %d chars, over the %d limit" % (len(joke), MAX_LENGTH))
    return joke


def write_entry(joke, output_path):
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(joke + "\n")
    return output_path


def main():
    joke = validate_joke(JOKE)
    output_path = resolve_output_path()
    write_entry(joke, output_path)
    print("Wrote %d-char entry to %s" % (len(joke), output_path))


if __name__ == "__main__":
    main()
