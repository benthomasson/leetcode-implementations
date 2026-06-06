import unittest
from solution import Solution


class TestNumOfStrings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.numOfStrings(["a", "abc", "bc", "d"], "abc"), 3)

    def test_example2(self):
        self.assertEqual(self.s.numOfStrings(["a", "b", "c"], "aaaaabbbbb"), 2)

    def test_example3_duplicates(self):
        self.assertEqual(self.s.numOfStrings(["a", "a", "a"], "ab"), 3)

    def test_no_match(self):
        self.assertEqual(self.s.numOfStrings(["x", "y", "z"], "abc"), 0)

    def test_all_match(self):
        self.assertEqual(self.s.numOfStrings(["a", "ab", "abc"], "abc"), 3)

    def test_pattern_equals_word(self):
        self.assertEqual(self.s.numOfStrings(["abc"], "abc"), 1)

    def test_pattern_longer_than_word(self):
        self.assertEqual(self.s.numOfStrings(["abcd"], "abc"), 0)

    def test_single_char(self):
        self.assertEqual(self.s.numOfStrings(["a"], "a"), 1)


if __name__ == "__main__":
    unittest.main()
