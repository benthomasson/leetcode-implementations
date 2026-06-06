import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestStringMatching(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        result = self.s.stringMatching(["mass", "as", "hero", "superhero"])
        self.assertEqual(sorted(result), ["as", "hero"])

    def test_example2(self):
        result = self.s.stringMatching(["leetcode", "et", "code"])
        self.assertEqual(sorted(result), ["code", "et"])

    def test_example3(self):
        self.assertEqual(self.s.stringMatching(["blue", "green", "bu"]), [])

    # --- Edge cases ---
    def test_single_word(self):
        self.assertEqual(self.s.stringMatching(["hello"]), [])

    def test_no_substrings_same_length(self):
        self.assertEqual(self.s.stringMatching(["abc", "def", "ghi"]), [])

    def test_single_char_substring(self):
        result = self.s.stringMatching(["a", "ab", "bc"])
        self.assertEqual(result, ["a"])

    def test_nested_substrings(self):
        result = self.s.stringMatching(["aaa", "aa", "a"])
        self.assertEqual(sorted(result), ["a", "aa"])

    def test_multiple_substrings_of_one_word(self):
        result = self.s.stringMatching(["abcdef", "abc", "def", "cd"])
        self.assertEqual(sorted(result), ["abc", "cd", "def"])

    def test_two_words_no_match(self):
        self.assertEqual(self.s.stringMatching(["cat", "dog"]), [])


if __name__ == "__main__":
    unittest.main()
