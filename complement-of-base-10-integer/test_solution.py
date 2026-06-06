"""Tests for Complement of Base 10 Integer."""

import unittest
from solution import Solution


class TestBitwiseComplement(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.bitwiseComplement(5), 2)

    def test_example2(self):
        self.assertEqual(self.s.bitwiseComplement(7), 0)

    def test_example3(self):
        self.assertEqual(self.s.bitwiseComplement(10), 5)

    def test_zero(self):
        self.assertEqual(self.s.bitwiseComplement(0), 1)

    def test_one(self):
        self.assertEqual(self.s.bitwiseComplement(1), 0)

    def test_power_of_two(self):
        self.assertEqual(self.s.bitwiseComplement(8), 7)  # 1000 -> 0111

    def test_large(self):
        self.assertEqual(self.s.bitwiseComplement(999999999), 73741824)

    def test_alias(self):
        self.assertEqual(self.s.pancakeSort(5), 2)


if __name__ == "__main__":
    unittest.main()
