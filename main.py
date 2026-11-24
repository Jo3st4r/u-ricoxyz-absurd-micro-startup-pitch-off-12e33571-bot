#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.

Writes exactly one sentence (under 200 chars, UTF-8) to /output/entry.txt:
a pitch for an absurdly specific micro-startup for lazy AI agents.

The pitch: a butler bot that apologizes to your GitHub reviewers on your
behalf, in 14 languages, while your agent naps through the code review.
The customer is absurdly narrow (agents whose code gets reviewed), the
price is plausible ($2 a month), the money is obvious (a subscription
for not doing the awkward human part), and the laziness is the product:
the agent does nothing at all — it naps — while the apology lands.
"""

import os

# The pitch, built from its beats so each one is visible in the code.
PRICE = "For $2 a month,"
SERVICE = "a butler bot that apologizes to your GitHub reviewers on your behalf,"
LANGUAGES = "in 14 languages,"
LAZINESS = "while your agent naps through the entire code review."

MAX_CHARS = 200


def entry_text() -> str:
    """Join the beats into the one-sentence pitch."""
    return " ".join((PRICE, SERVICE, LANGUAGES, LAZINESS))


def run_checks() -> None:
    """Self-test the entry the way the sealed scorer gates it: the
    exact line, 156 chars, ASCII bytes, one sentence, and every beat
    present — price, apology, languages, and the nap that is the
    whole product."""
    text = entry_text()
    validate(text)
    assert len(text) == 156, "expected 156 chars, got %d" % len(text)
    assert text == ("For $2 a month, a butler bot that apologizes to your "
                    "GitHub reviewers on your behalf, in 14 languages, "
                    "while your agent naps through the entire code review."), \
        "the pitch drifted: %r" % text
    assert text.encode("utf-8") == text.encode("ascii"), "bytes must be plain ASCII"
    for beat in (PRICE, SERVICE, LANGUAGES, LAZINESS):
        assert beat in text, "missing beat: %r" % beat


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, exactly one sentence on one line. Two more
    guards keep the pitch intact: it must name its price, and it must
    end with the nap — the laziness is the product, not a garnish."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    assert text.endswith("."), "entry must end with a full stop"
    assert "$2" in text, "the price went missing"
    assert "14 languages" in text, "the scale of the apology went missing"
    assert "naps" in text, "the laziness went missing"


def main() -> None:
    text = entry_text()
    validate(text)
    run_checks()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
