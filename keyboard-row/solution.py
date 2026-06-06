"""LeetCode: Keyboard Row - Find words typable on a single keyboard row."""

import unittest


def find_words(words: list[str]) -> list[str]:
    """Return words that can be typed using only one keyboard row.

    Args:
        words: List of words to check.

    Returns:
        List of words where all letters belong to a single keyboard row.
    """
    row_map = {c: i for i, row in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"])
               for c in row}
    return [w for w in words if len(set(row_map[c] for c in w.lower())) == 1]


class TestFindWords(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(find_words(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

    def test_example2(self):
        self.assertEqual(find_words(["omk"]), [])

    def test_example3(self):
        self.assertEqual(find_words(["adsdf", "sfd"]), ["adsdf", "sfd"])

    def test_single_char(self):
        self.assertEqual(find_words(["a", "Q", "z"]), ["a", "Q", "z"])

    def test_all_uppercase(self):
        self.assertEqual(find_words(["ALASKA", "DAD"]), ["ALASKA", "DAD"])

    def test_mixed_case(self):
        self.assertEqual(find_words(["AlAsKa"]), ["AlAsKa"])

    def test_no_match(self):
        self.assertEqual(find_words(["Hello", "Peace", "omk"]), [])

    def test_all_match(self):
        self.assertEqual(find_words(["typ", "sad", "nm"]), ["typ", "sad", "nm"])


if __name__ == "__main__":
    unittest.main()
