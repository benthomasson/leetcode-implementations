"""Tests for count-common-words-with-one-occurrence."""

import unittest
from solution import Solution


class TestCountWords(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countWords(
            ["leetcode", "is", "amazing", "as", "is"],
            ["amazing", "leetcode", "is"]), 2)

    def test_example2(self):
        self.assertEqual(self.s.countWords(
            ["b", "bb", "bbb"], ["a", "aa", "aaa"]), 0)

    def test_example3(self):
        self.assertEqual(self.s.countWords(
            ["a", "ab"], ["a", "a", "a", "ab"]), 1)

    def test_no_overlap(self):
        self.assertEqual(self.s.countWords(["x"], ["y"]), 0)

    def test_all_unique_overlap(self):
        self.assertEqual(self.s.countWords(
            ["a", "b", "c"], ["a", "b", "c"]), 3)

    def test_single_element_match(self):
        self.assertEqual(self.s.countWords(["a"], ["a"]), 1)

    def test_all_duplicates(self):
        self.assertEqual(self.s.countWords(
            ["a", "a"], ["a", "a"]), 0)

    def test_duplicate_in_one_array(self):
        self.assertEqual(self.s.countWords(
            ["a", "a", "b"], ["a", "b"]), 1)


if __name__ == "__main__":
    unittest.main()
