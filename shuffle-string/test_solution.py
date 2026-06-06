import unittest
from solution import Solution


class TestShuffleString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.kids_with_candies("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode")

    def test_example2(self):
        self.assertEqual(self.sol.kids_with_candies("abc", [0, 1, 2]), "abc")

    def test_single_char(self):
        self.assertEqual(self.sol.kids_with_candies("a", [0]), "a")

    def test_reverse(self):
        self.assertEqual(self.sol.kids_with_candies("abcd", [3, 2, 1, 0]), "dcba")

    def test_all_same_chars(self):
        self.assertEqual(self.sol.kids_with_candies("aaaa", [2, 0, 3, 1]), "aaaa")


if __name__ == "__main__":
    unittest.main()
