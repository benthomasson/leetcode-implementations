"""LeetCode 1078: Occurrences After Bigram."""
from typing import List
import unittest


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        """Find words that follow the bigram (first, second) in text.

        Args:
            text: Space-separated lowercase words.
            first: First word of the bigram.
            second: Second word of the bigram.

        Returns:
            List of words immediately following each occurrence of the bigram.
        """
        words = text.split()
        return [
            words[i + 2]
            for i in range(len(words) - 2)
            if words[i] == first and words[i + 1] == second
        ]


class TestFindOcurrences(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.findOcurrences("alice is a good girl she is a good student", "a", "good"),
            ["girl", "student"],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.findOcurrences("we will we will rock you", "we", "will"),
            ["we", "rock"],
        )

    def test_no_match(self):
        self.assertEqual(self.s.findOcurrences("hello world foo", "a", "b"), [])

    def test_bigram_at_end(self):
        self.assertEqual(self.s.findOcurrences("a b", "a", "b"), [])

    def test_overlapping(self):
        self.assertEqual(self.s.findOcurrences("a a a a", "a", "a"), ["a", "a"])

    def test_single_word(self):
        self.assertEqual(self.s.findOcurrences("hello", "hello", "world"), [])

    def test_first_equals_second(self):
        self.assertEqual(self.s.findOcurrences("x x y x x z", "x", "x"), ["y", "z"])


if __name__ == "__main__":
    unittest.main()
