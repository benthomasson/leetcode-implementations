"""Shortest Completing Word - LeetCode"""

from collections import Counter


def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    """Find the shortest word containing all letters from licensePlate.

    Args:
        licensePlate: String with letters, digits, and spaces.
        words: List of lowercase words to search.

    Returns:
        The shortest completing word (first occurrence on ties).
    """
    plate = Counter(c.lower() for c in licensePlate if c.isalpha())
    result = None
    for word in words:
        if not (plate - Counter(word)):
            if result is None or len(word) < len(result):
                result = word
    return result


import unittest


class TestShortestCompletingWord(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]),
            "steps",
        )

    def test_example2(self):
        self.assertEqual(
            shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]),
            "pest",
        )

    def test_single_letter(self):
        self.assertEqual(
            shortestCompletingWord("a", ["b", "a", "aa"]),
            "a",
        )

    def test_tie_breaking_by_order(self):
        self.assertEqual(
            shortestCompletingWord("a", ["ab", "ac", "ad"]),
            "ab",
        )

    def test_mixed_case_plate(self):
        self.assertEqual(
            shortestCompletingWord("aBc 12c", ["abcc", "cbca", "abccdef"]),
            "abcc",
        )

    def test_all_digits_and_spaces_except_one_letter(self):
        self.assertEqual(
            shortestCompletingWord("1 2 3 z", ["az", "z", "zz"]),
            "z",
        )

    def test_repeated_letters_in_plate(self):
        self.assertEqual(
            shortestCompletingWord("AA", ["a", "aa", "aaa"]),
            "aa",
        )


if __name__ == "__main__":
    unittest.main()
