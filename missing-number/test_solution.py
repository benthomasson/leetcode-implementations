"""Tests for Missing Number solution."""

import unittest
from solution import missingNumber


class TestMissingNumber(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(missingNumber([3, 0, 1]), 2)

    def test_example2(self):
        self.assertEqual(missingNumber([0, 1]), 2)

    def test_example3(self):
        self.assertEqual(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_missing_zero(self):
        self.assertEqual(missingNumber([1]), 0)

    def test_missing_n(self):
        self.assertEqual(missingNumber([0]), 1)

    def test_single_zero(self):
        self.assertEqual(missingNumber([0]), 1)

    def test_single_one(self):
        self.assertEqual(missingNumber([1]), 0)

    def test_larger(self):
        nums = list(range(101))
        nums.remove(42)
        self.assertEqual(missingNumber(nums), 42)


if __name__ == "__main__":
    unittest.main()
