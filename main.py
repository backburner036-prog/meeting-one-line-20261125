"""Entry for make.fun bounty "The Meeting That Should Have Been One Line".

One sentence that could have replaced an entire pointless meeting.
Two beats: the setup counts the waste everyone recognises (twelve
people, forty-five minutes, zero decisions), and the reversal is the
line itself delivering the decision the meeting never produced --
approved, Friday -- and ending the meeting. No context, no
explanation, no setup beyond the sentence itself.
"""

from pathlib import Path

TEXT = "Twelve people, forty-five minutes, zero decisions \u2014 so here is one: approved, Friday, meeting over."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert "\n" not in text, "entry must be a single line"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
