import unittest
from solution import Solution


class TestMaxPower(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxPower("leetcode"), 2)

    def test_example2(self):
        self.assertEqual(self.sol.maxPower("abbcccddddeeeeedcba"), 5)

    def test_single_char(self):
        self.assertEqual(self.sol.maxPower("a"), 1)

    def test_all_same(self):
        self.assertEqual(self.sol.maxPower("aaaaaaa"), 7)

    def test_alternating(self):
        self.assertEqual(self.sol.maxPower("ababab"), 1)

    def test_streak_at_start(self):
        self.assertEqual(self.sol.maxPower("aaab"), 3)

    def test_streak_at_end(self):
        self.assertEqual(self.sol.maxPower("abbb"), 3)

    def test_streak_in_middle(self):
        self.assertEqual(self.sol.maxPower("abbbca"), 3)

    def test_two_chars(self):
        self.assertEqual(self.sol.maxPower("ab"), 1)


if __name__ == "__main__":
    unittest.main()
