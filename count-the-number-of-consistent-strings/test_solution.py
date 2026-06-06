import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution
import unittest


class TestCountConsistentStrings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(self.s.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]), 2)

    def test_example2(self):
        self.assertEqual(self.s.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]), 7)

    def test_example3(self):
        self.assertEqual(self.s.countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]), 4)

    # Edge cases
    def test_single_char_allowed(self):
        self.assertEqual(self.s.countConsistentStrings("a", ["a", "aa", "b", "ab"]), 2)

    def test_all_consistent(self):
        self.assertEqual(self.s.countConsistentStrings("abc", ["a", "ab", "abc"]), 3)

    def test_none_consistent(self):
        self.assertEqual(self.s.countConsistentStrings("a", ["b", "c", "bc"]), 0)

    def test_all_26_letters_allowed(self):
        self.assertEqual(self.s.countConsistentStrings("abcdefghijklmnopqrstuvwxyz", ["anything", "z"]), 2)

    def test_repeated_chars_in_word(self):
        self.assertEqual(self.s.countConsistentStrings("ab", ["aaaa", "bbbb", "abab"]), 3)

    # Alias
    def test_find_latest_step_alias(self):
        self.assertEqual(self.s.find_latest_step("ab", ["ab", "cd"]), 1)


if __name__ == "__main__":
    unittest.main()
