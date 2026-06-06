import unittest
import sys
sys.path.insert(0, "../implementer")
from solution import Solution


class TestDivideString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(self.sol.divideString("abcdefghi", 3, "x"), ["abc", "def", "ghi"])

    def test_example2(self):
        self.assertEqual(self.sol.divideString("abcdefghij", 3, "x"), ["abc", "def", "ghi", "jxx"])

    # Edge cases
    def test_single_char_needs_padding(self):
        self.assertEqual(self.sol.divideString("a", 3, "x"), ["axx"])

    def test_k_equals_1(self):
        self.assertEqual(self.sol.divideString("abc", 1, "x"), ["a", "b", "c"])

    def test_k_greater_than_length(self):
        self.assertEqual(self.sol.divideString("ab", 5, "z"), ["abzzz"])

    def test_k_equals_length(self):
        self.assertEqual(self.sol.divideString("abc", 3, "x"), ["abc"])

    def test_single_char_k1(self):
        self.assertEqual(self.sol.divideString("z", 1, "a"), ["z"])

    def test_padding_by_one(self):
        self.assertEqual(self.sol.divideString("abcde", 3, "y"), ["abc", "dey"])

    def test_max_constraint_length(self):
        s = "a" * 100
        result = self.sol.divideString(s, 10, "x")
        self.assertEqual(len(result), 10)
        self.assertTrue(all(len(g) == 10 for g in result))


if __name__ == "__main__":
    unittest.main()
