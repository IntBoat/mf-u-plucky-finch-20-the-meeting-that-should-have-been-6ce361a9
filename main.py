"""The Meeting That Should Have Been an Email — make.fun entry.

The entry is one line of at most 200 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = 'This meeting could have been an email, but then nobody would have watched me nod thoughtfully while Googling what we were meeting about.'


def write_entry():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
