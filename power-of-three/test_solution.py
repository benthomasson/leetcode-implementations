"""Tests for Power of Three solution."""

import unittest
from solution import is_power_of_three


class TestIsPowerOfThree(unittest.TestCase):

    def test_powers_of_three(self):
        for val in [1, 3, 9, 27, 81, 243, 729, 59049, 1162261467]:
            self.assertTrue(is_power_of_three(val), f"{val} should be a power of 3")

    def test_zero(self):
        self.assertFalse(is_power_of_three(0))

    def test_negative(self):
        for val in [-1, -3, -27]:
            self.assertFalse(is_power_of_three(val))

    def test_non_powers(self):
        for val in [2, 4, 5, 6, 10, 45, 100, 2**31 - 1]:
            self.assertFalse(is_power_of_three(val), f"{val} should not be a power of 3")


if __name__ == "__main__":
    unittest.main()
