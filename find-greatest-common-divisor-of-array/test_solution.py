"""Tests for Find Greatest Common Divisor of Array."""

import unittest
from solution import Solution


class TestFindGCD(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findGCD([2, 5, 6, 9, 10]), 2)

    def test_example2(self):
        self.assertEqual(self.s.findGCD([7, 5, 6, 8, 3]), 1)

    def test_example3(self):
        self.assertEqual(self.s.findGCD([3, 3]), 3)

    def test_min_equals_max(self):
        self.assertEqual(self.s.findGCD([5, 5, 5]), 5)

    def test_max_divisible_by_min(self):
        self.assertEqual(self.s.findGCD([4, 8, 6]), 4)

    def test_coprime(self):
        self.assertEqual(self.s.findGCD([7, 11]), 1)

    def test_one_in_array(self):
        self.assertEqual(self.s.findGCD([1, 100]), 1)

    def test_large_gcd(self):
        self.assertEqual(self.s.findGCD([12, 18, 15]), 6)

    def test_single_value_repeated(self):
        self.assertEqual(self.s.findGCD([1000, 1000]), 1000)


if __name__ == "__main__":
    unittest.main()
