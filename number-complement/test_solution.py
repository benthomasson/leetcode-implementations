"""Tests for find_complement."""

import unittest
from solution import find_complement


class TestFindComplement(unittest.TestCase):
    def test_example_5(self):
        self.assertEqual(find_complement(5), 2)

    def test_example_1(self):
        self.assertEqual(find_complement(1), 0)

    def test_power_of_two(self):
        self.assertEqual(find_complement(4), 3)  # 100 -> 011

    def test_all_ones(self):
        self.assertEqual(find_complement(7), 0)  # 111 -> 000

    def test_two(self):
        self.assertEqual(find_complement(2), 1)  # 10 -> 01

    def test_large(self):
        self.assertEqual(find_complement(2**31 - 1), 0)  # all 1s

    def test_large_power_of_two(self):
        # 2^30 = 1 followed by 30 zeros -> 0 followed by 30 ones
        self.assertEqual(find_complement(2**30), 2**30 - 1)


if __name__ == "__main__":
    unittest.main()
