"""Basic text-file statistics used by the CryptoLabX command-line interface.

This module intentionally contains no cryptographic algorithms.  It prepares
the toolkit for later frequency-analysis and cryptanalysis exercises.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Counter as CounterType


def analyze_text(text: str) -> dict[str, int | CounterType[str]]:
    """Return the required statistics for *text*.

    Letter frequencies are case-insensitive and include alphabetic Unicode
    characters only.  Characters, including spaces and punctuation, are used
    when calculating the unique-character count.
    """
    letter_frequency = Counter(character.lower() for character in text if character.isalpha())
    line_count = 0 if not text else text.count("\n") + (0 if text.endswith("\n") else 1)

    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": line_count,
        "unique_characters": len(set(text)),
        "letter_frequency": letter_frequency,
    }


def analyze_file(file_path: str | Path) -> dict[str, int | CounterType[str]]:
    """Read a UTF-8 text file and return its statistics."""
    path = Path(file_path)
    return analyze_text(path.read_text(encoding="utf-8"))


def format_analysis(file_path: str | Path) -> str:
    """Format a file analysis result for display in a command-line program."""
    path = Path(file_path)
    stats = analyze_file(path)
    frequencies = stats["letter_frequency"]
    frequency_text = ", ".join(
        f"{letter}: {count}" for letter, count in sorted(frequencies.items())
    ) or "No letters found"

    return "\n".join(
        [
            f"File analysis: {path.name}",
            f"Characters: {stats['characters']}",
            f"Words: {stats['words']}",
            f"Lines: {stats['lines']}",
            f"Unique characters: {stats['unique_characters']}",
            f"Letter frequency: {frequency_text}",
        ]
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a UTF-8 text file.")
    parser.add_argument("file", type=Path, help="Path to a text file")
    arguments = parser.parse_args()
    print(format_analysis(arguments.file))
