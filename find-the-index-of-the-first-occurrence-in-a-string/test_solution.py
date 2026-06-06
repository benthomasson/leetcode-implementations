import unittest
from solution import Solution


class TestStrStr(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_match_at_start(self):
        self.assertEqual(self.s.strStr("sadbutsad", "sad"), 0)

    def test_no_match(self):
        self.assertEqual(self.s.strStr("leetcode", "leeto"), -1)

    def test_match_in_middle(self):
        self.assertEqual(self.s.strStr("hello", "ll"), 2)

    def test_needle_equals_haystack(self):
        self.assertEqual(self.s.strStr("abc", "abc"), 0)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(self.s.strStr("ab", "abc"), -1)

    def test_single_char_match(self):
        self.assertEqual(self.s.strStr("a", "a"), 0)

    def test_single_char_no_match(self):
        self.assertEqual(self.s.strStr("a", "b"), -1)

    def test_overlapping_pattern(self):
        self.assertEqual(self.s.strStr("aabaabaab", "aabaa"), 0)

    def test_repeated_chars(self):
        self.assertEqual(self.s.strStr("aaaaaab", "aab"), 4)

    def test_match_at_end(self):
        self.assertEqual(self.s.strStr("abcdef", "def"), 3)


if __name__ == "__main__":
    unittest.main()
