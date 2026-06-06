"""Tests for Reformat The String solution."""
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


def is_valid(result: str, original: str) -> bool:
    """Check result is a valid reformat of original."""
    if sorted(result) != sorted(original):
        return False
    for i in range(len(result) - 1):
        if result[i].isdigit() == result[i + 1].isdigit():
            return False
    return True


class TestReformat(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1(self):
        res = self.sol.reformat("a0b1c2")
        self.assertTrue(is_valid(res, "a0b1c2"))

    def test_example2_all_letters(self):
        self.assertEqual(self.sol.reformat("leetcode"), "")

    def test_example3_all_digits(self):
        self.assertEqual(self.sol.reformat("1229857369"), "")

    # --- Edge cases ---
    def test_single_letter(self):
        self.assertEqual(self.sol.reformat("a"), "a")

    def test_single_digit(self):
        self.assertEqual(self.sol.reformat("5"), "5")

    def test_two_valid(self):
        res = self.sol.reformat("a1")
        self.assertTrue(is_valid(res, "a1"))

    def test_off_by_one_more_letters(self):
        res = self.sol.reformat("ab1")
        self.assertTrue(is_valid(res, "ab1"))

    def test_off_by_one_more_digits(self):
        res = self.sol.reformat("a12")
        self.assertTrue(is_valid(res, "a12"))

    def test_impossible_diff_2(self):
        self.assertEqual(self.sol.reformat("aab1"), "")

    def test_larger_valid(self):
        res = self.sol.reformat("a1b2c3d4")
        self.assertTrue(is_valid(res, "a1b2c3d4"))


if __name__ == "__main__":
    unittest.main()
