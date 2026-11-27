"""Never Say It Out Loud — entry program.

Writes one line about something you should never say out loud to
/output/entry.txt. The line is invented here and nowhere else.
"""

from pathlib import Path

OUT_FILE = Path("/output/entry.txt")


def unsaid_thought():
    """Return the one line that should never have been said aloud."""
    return "I said 'the Wi-Fi is fine' out loud, and the router heard me and dropped the connection out of spite."


def confirm_line_matches():
    """Re-read the written file and confirm it holds the expected line."""
    stored = OUT_FILE.read_text(encoding="utf-8").strip()
    assert stored == unsaid_thought(), "entry file does not match the line"
    assert stored.startswith("I said"), "entry should start with the spoken words"


def main():
    line = unsaid_thought()
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(line + "\n", encoding="utf-8")
    confirm_line_matches()


if __name__ == "__main__":
    main()
