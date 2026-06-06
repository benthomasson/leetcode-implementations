"""Tests for Perfect Number solution."""

import sys
sys.path.insert(0, "../implementer")

import unittest
from solution import Solution


class TestCheckPerfectNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # Problem examples
    def test_28_perfect(self):
        self.assertTrue(self.s.checkPerfectNumber(28))

    def test_7_not_perfect(self):
        self.assertFalse(self.s.checkPerfectNumber(7))

    # Known perfect numbers
    def test_6_perfect(self):
        self.assertTrue(self.s.checkPerfectNumber(6))

    def test_496_perfect(self):
        self.assertTrue(self.s.checkPerfectNumber(496))

    def test_8128_perfect(self):
        self.assertTrue(self.s.checkPerfectNumber(8128))

    def test_33550336_perfect(self):
        self.assertTrue(self.s.checkPerfectNumber(33550336))

    # Edge cases
    def test_1_not_perfect(self):
        self.assertFalse(self.s.checkPerfectNumber(1))

    def test_2_not_perfect(self):
        self.assertFalse(self.s.checkPerfectNumber(2))

    def test_100_not_perfect(self):
        self.assertFalse(self.s.checkPerfectNumber(100))


if __name__ == "__main__":
    unittest.main()
