"""LeetCode: Count Prefixes of a Given String."""

from typing import List
import unittest


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        """Count how many strings in words are a prefix of s.

        Args:
            words: List of lowercase English letter strings.
            s: Target string to check prefixes against.

        Returns:
            Number of strings in words that are a prefix of s.
        """
        return sum(1 for w in words if s.startswith(w))


class TestCountPrefixes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"), 3)

    def test_example2(self):
        self.assertEqual(self.sol.countPrefixes(["a", "a"], "aa"), 2)

    def test_no_match(self):
        self.assertEqual(self.sol.countPrefixes(["b", "c", "d"], "abc"), 0)

    def test_word_longer_than_s(self):
        self.assertEqual(self.sol.countPrefixes(["abcd"], "abc"), 0)

    def test_word_equals_s(self):
        self.assertEqual(self.sol.countPrefixes(["abc"], "abc"), 1)

    def test_single_char(self):
        self.assertEqual(self.sol.countPrefixes(["a"], "a"), 1)

    def test_all_match(self):
        self.assertEqual(self.sol.countPrefixes(["a", "ab", "abc"], "abc"), 3)

    def test_duplicates(self):
        self.assertEqual(self.sol.countPrefixes(["a", "a", "a"], "abc"), 3)


if __name__ == "__main__":
    unittest.main()
