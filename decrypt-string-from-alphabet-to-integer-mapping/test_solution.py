"""Tests for Decrypt String from Alphabet to Integer Mapping."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestDecryptString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Problem examples
    def test_example1(self):
        self.assertEqual(self.sol.sortItems("10#11#12"), "jkab")

    def test_example2(self):
        self.assertEqual(self.sol.sortItems("1326#"), "acz")

    # Edge cases
    def test_single_digit(self):
        self.assertEqual(self.sol.sortItems("1"), "a")

    def test_single_digit_9(self):
        self.assertEqual(self.sol.sortItems("9"), "i")

    def test_single_hash_number(self):
        self.assertEqual(self.sol.sortItems("26#"), "z")

    def test_all_single_digits(self):
        self.assertEqual(self.sol.sortItems("123456789"), "abcdefghi")

    def test_boundary_9_then_10(self):
        self.assertEqual(self.sol.sortItems("910#"), "ij")

    def test_full_alphabet(self):
        self.assertEqual(
            self.sol.sortItems("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"),
            "abcdefghijklmnopqrstuvwxyz",
        )


if __name__ == "__main__":
    unittest.main()
