import unittest

from solution import mergeAlternately


class TestMergeAlternately(unittest.TestCase):
    """Tests for the mergeAlternately function."""

    def test_equal_length(self):
        """Example 1: both strings have equal length."""
        self.assertEqual(mergeAlternately("abc", "pqr"), "apbqcr")

    def test_word2_longer(self):
        """Example 2: word2 is longer than word1."""
        self.assertEqual(mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_word1_longer(self):
        """Example 3: word1 is longer than word2."""
        self.assertEqual(mergeAlternately("abcd", "pq"), "apbqcd")

    def test_single_char_each(self):
        """Both strings are a single character."""
        self.assertEqual(mergeAlternately("a", "b"), "ab")

    def test_single_char_word1_longer_word2(self):
        """word1 is one char, word2 is multiple chars."""
        self.assertEqual(mergeAlternately("a", "xyz"), "axyz")

    def test_longer_word1_single_char_word2(self):
        """word1 is multiple chars, word2 is one char."""
        self.assertEqual(mergeAlternately("xyz", "a"), "xayz")

    def test_same_strings(self):
        """Merging a string with itself."""
        self.assertEqual(mergeAlternately("ab", "ab"), "aabb")

    def test_single_char_strings(self):
        """Minimum length constraint: single characters."""
        self.assertEqual(mergeAlternately("z", "z"), "zz")

    def test_large_length_difference(self):
        """One string much longer than the other."""
        self.assertEqual(mergeAlternately("a", "bcdef"), "abcdef")
        self.assertEqual(mergeAlternately("bcdef", "a"), "bacdef")


if __name__ == "__main__":
    unittest.main()
