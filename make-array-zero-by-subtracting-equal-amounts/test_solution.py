"""Tests for Make Array Zero by Subtracting Equal Amounts."""

import unittest
from solution import Solution


class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minOperations([1, 5, 0, 3, 5]), 3)

    def test_example2(self):
        self.assertEqual(self.s.minOperations([0]), 0)

    def test_all_zeros(self):
        self.assertEqual(self.s.minOperations([0, 0, 0]), 0)

    def test_single_nonzero(self):
        self.assertEqual(self.s.minOperations([7]), 1)

    def test_all_same(self):
        self.assertEqual(self.s.minOperations([3, 3, 3]), 1)

    def test_all_distinct(self):
        self.assertEqual(self.s.minOperations([1, 2, 3, 4, 5]), 5)

    def test_duplicates_with_zeros(self):
        self.assertEqual(self.s.minOperations([0, 2, 0, 2, 0]), 1)

    def test_max_value(self):
        self.assertEqual(self.s.minOperations([100]), 1)

    def test_mixed(self):
        self.assertEqual(self.s.minOperations([1, 1, 2, 2, 3, 3, 0]), 3)


if __name__ == "__main__":
    unittest.main()
