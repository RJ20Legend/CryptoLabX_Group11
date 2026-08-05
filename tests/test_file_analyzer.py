"""Unit tests for the Week 1 text-file analyzer."""

import unittest

from analysis.file_analyzer import analyze_text


class AnalyzeTextTests(unittest.TestCase):
    def test_required_statistics_are_calculated(self) -> None:
        stats = analyze_text("Hello hello!\n42")

        self.assertEqual(stats["characters"], 15)
        self.assertEqual(stats["words"], 3)
        self.assertEqual(stats["lines"], 2)
        self.assertEqual(stats["unique_characters"], 10)
        self.assertEqual(stats["letter_frequency"], {"h": 2, "e": 2, "l": 4, "o": 2})

    def test_empty_text_has_zero_lines(self) -> None:
        stats = analyze_text("")

        self.assertEqual(stats["lines"], 0)
        self.assertEqual(stats["letter_frequency"], {})


if __name__ == "__main__":
    unittest.main()
