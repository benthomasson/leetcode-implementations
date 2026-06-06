import unittest
from solution import Solution


class TestCommonChars(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        result = sorted(self.s.commonChars(["bella", "label", "roller"]))
        self.assertEqual(result, ["e", "l", "l"])

    def test_example2(self):
        result = sorted(self.s.commonChars(["cool", "lock", "cook"]))
        self.assertEqual(result, ["c", "o"])

    def test_single_word(self):
        result = sorted(self.s.commonChars(["abc"]))
        self.assertEqual(result, ["a", "b", "c"])

    def test_no_common(self):
        result = self.s.commonChars(["abc", "def"])
        self.assertEqual(result, [])

    def test_all_same(self):
        result = sorted(self.s.commonChars(["aaa", "aaa", "aaa"]))
        self.assertEqual(result, ["a", "a", "a"])

    def test_single_char_words(self):
        result = self.s.commonChars(["a", "a", "a"])
        self.assertEqual(result, ["a"])

    def test_partial_overlap(self):
        result = sorted(self.s.commonChars(["aab", "aac"]))
        self.assertEqual(result, ["a", "a"])


if __name__ == "__main__":
    unittest.main()
