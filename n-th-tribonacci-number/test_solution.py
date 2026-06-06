"""Tests for N-th Tribonacci Number."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution


class TestTribonacci(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_base_case_zero(self):
        self.assertEqual(self.sol.tribonacci(0), 0)

    def test_base_case_one(self):
        self.assertEqual(self.sol.tribonacci(1), 1)

    def test_base_case_two(self):
        self.assertEqual(self.sol.tribonacci(2), 1)

    def test_example1_n4(self):
        self.assertEqual(self.sol.tribonacci(4), 4)

    def test_example2_n25(self):
        self.assertEqual(self.sol.tribonacci(25), 1389537)

    def test_n3(self):
        self.assertEqual(self.sol.tribonacci(3), 2)

    def test_small_sequence(self):
        # T0..T7 = 0, 1, 1, 2, 4, 7, 13, 24
        expected = [0, 1, 1, 2, 4, 7, 13, 24]
        for i, val in enumerate(expected):
            self.assertEqual(self.sol.tribonacci(i), val, f"Failed for n={i}")

    def test_upper_bound_n37(self):
        self.assertEqual(self.sol.tribonacci(37), 2082876103)

    def test_fits_32bit(self):
        result = self.sol.tribonacci(37)
        self.assertLessEqual(result, 2**31 - 1)


if __name__ == "__main__":
    unittest.main()
