import unittest
from solution import Solution


class TestGoodNodes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.goodNodes("leEeetcode"), "leetcode")

    def test_example2(self):
        self.assertEqual(self.sol.goodNodes("abBAcC"), "")

    def test_example3(self):
        self.assertEqual(self.sol.goodNodes("s"), "s")

    def test_empty(self):
        self.assertEqual(self.sol.goodNodes(""), "")

    def test_no_removals(self):
        self.assertEqual(self.sol.goodNodes("abcdef"), "abcdef")

    def test_all_removed(self):
        self.assertEqual(self.sol.goodNodes("aAbBcC"), "")

    def test_cascading(self):
        self.assertEqual(self.sol.goodNodes("abBA"), "")

    def test_single_upper(self):
        self.assertEqual(self.sol.goodNodes("A"), "A")


if __name__ == "__main__":
    unittest.main()
