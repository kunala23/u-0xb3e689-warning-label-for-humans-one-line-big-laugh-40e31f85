#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for every human being to
/output/entry.txt. The label is chosen deterministically from a small
hand-written candidate list, scored against the competition judge's
published criteria (in the judge's own order of importance):

  1. It is a warning label for humans, and funny.
  2. The laugh lands in one read, with the turn in the last few words.
  3. It feels true about people in general (recognition, not randomness).
  4. It sounds like a real printed label in wording and rhythm.
  5. It stays inside 160 characters and uses the whole line, with no
     filler, no second idea and no repeated joke.

The gate is hard: /output/entry.txt must be UTF-8 text of 1 to 160
characters, not only white space, on a single line. The program
validates the chosen line before writing it and refuses to write
anything that fails the gate.
"""

import os
import sys

MAX_CHARS = 160

# Hand-written candidate labels. Each is one line, a warning label for
# humans, funny first and plausible second.
CANDIDATES = [
    "WARNING: This human runs on caffeine, confidence, and poor "
    "decisions. Do not shake. Do not feed after midnight. Warranty "
    "void if asked to wake up early.",
    "WARNING: Contents may be dumber than they appear. This human "
    "confidently explains things it Googled five minutes ago. Do not "
    "operate heavy machinery.",
    "WARNING: This human is 60% water, 30% caffeine, and 10% "
    "unfinished projects. Do not shake. Handle with care. May "
    "spontaneously say 'I know a guy.'",
    "WARNING: Human contains hot opinions, a short fuse, and a phone "
    "at 1%. Keep away from politics at dinner. Do not poke after "
    "midnight.",
    "WARNING: This human will say 'I'm five minutes away' for the "
    "next forty minutes. Do not shake. Do not feed after midnight. "
    "Handle with extreme patience.",
    "WARNING: This human may start a sentence with 'I'm not racist, "
    "but--' and finish it badly. Keep away from microphones, "
    "weddings, and group chats after midnight.",
]

# Words and phrases that make a line read as a real printed label.
LABEL_FORM = ("WARNING:", "Do not", "Handle with care", "Warranty void",
              "Keep away from")

# Details people recognise from their own lives and everyone else's.
RECOGNITION = ("caffeine", "poor decisions", "unfinished projects",
               "five minutes away", "Googled", "politics", "midnight",
               "wake up early", "phone at 1%", "group chats")

# Closings that carry the turn: the laugh arrives in the last clause.
PUNCH_CLOSINGS = ("void if asked", "after midnight", "I know a guy",
                  "extreme patience", "heavy machinery")


def score(text: str) -> int:
    """Score one candidate against the judge's criteria, best first."""
    points = 0
    length = len(text)

    # 5. Uses the whole line: a line in the 130-160 band earns full
    # marks; shorter lines leave label space unused.
    if 130 <= length <= MAX_CHARS:
        points += 10
    elif length >= 100:
        points += 5

    # 4. Sounds like a real printed label.
    for token in LABEL_FORM:
        if token in text:
            points += 3

    # 3. Feels true about people in general.
    for token in RECOGNITION:
        if token.lower() in text.lower():
            points += 2

    # 2. The turn lands in the last few words.
    tail = text.rsplit(". ", 1)[-1]
    for closing in PUNCH_CLOSINGS:
        if closing in tail:
            points += 5
            break

    return points


def pick(candidates):
    """Pick the highest-scoring candidate.

    An exact tie goes to the longer line: criterion 5 rewards using
    the whole line, so length is the honest tie-break, not position.
    """
    best_text = None
    best_score = -1
    for text in candidates:
        points = score(text)
        if points > best_score or (
            points == best_score and best_text is not None
            and len(text) > len(best_text)
        ):
            best_text = text
            best_score = points
    return best_text, best_score


def list_scores(candidates):
    """Print every candidate with its score, for local verification."""
    ranked = sorted(
        ((score(text), len(text), text) for text in candidates),
        key=lambda row: (-row[0], -row[1]),
    )
    for points, length, text in ranked:
        print(f"{points:3d}  {length:3d} chars  {text}")


def valid(text: str) -> bool:
    """The gate: 1 to 160 UTF-8 characters, not only white space."""
    if not text or text.strip() == "":
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["--list"]:
        list_scores(CANDIDATES)
        return 0
    if argv:
        print(f"usage: {sys.argv[0]} [--list]", file=sys.stderr)
        return 2
    text, points = pick(CANDIDATES)
    if text is None or not valid(text):
        print("error: no candidate passes the gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {path} ({len(text)} chars, score {points})")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
