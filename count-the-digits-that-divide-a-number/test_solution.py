"""Tests for digits_dividing_num."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import digits_dividing_num


class TestDigitsDividingNum(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertEqual(digits_dividing_num(7), 1)

    def test_example2(self):
        self.assertEqual(digits_dividing_num(121), 2)

    def test_example3(self):
        self.assertEqual(digits_dividing_num(1248), 4)

    # Edge cases
    def test_min_input(self):
        self.assertEqual(digits_dividing_num(1), 1)

    def test_large_all_ones(self):
        self.assertEqual(digits_dividing_num(111111111), 9)

    def test_no_digit_divides_except_one(self):
        # 13: 1 divides, 3 does not
        self.assertEqual(digits_dividing_num(13), 1)

    def test_all_same_digit(self):
        self.assertEqual(digits_dividing_num(555), 3)

    def test_mixed_divisibility(self):
        # 36: 3 divides (36%3==0), 6 divides (36%6==0) -> 2
        self.assertEqual(digits_dividing_num(36), 2)

    def test_nine_digit_number(self):
        # 999999999: 9 divides (999999999%9==0), 9 digits -> 9
        self.assertEqual(digits_dividing_num(999999999), 9)


if __name__ == "__main__":
    unittest.main()
