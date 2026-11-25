"""GPS excuse entry for make.fun: The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse to MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no external files.
"""

import os
import sys


EXCUSE = (
    "I turned into this cul-de-sac because the map swore a wedding "
    "was happening here, and I never argue with the map on "
    "someone's big day."
)


def check_line(line):
    """Gate the line the same way the contest gate does."""
    if not line or not line.strip():
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    chars = len(line)
    if chars < 1 or chars > 200:
        raise ValueError("entry is %d characters, must be 1-200" % chars)
    return line


def write_entry():
    """Write the validated excuse to the kit's output directory."""
    line = check_line(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.chmod(target, 0o644)
    return target


def main():
    try:
        target = write_entry()
    except (ValueError, OSError) as error:
        print("error: %s" % error, file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (target, len(EXCUSE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
