"""Tests for minimum cost of buying candies with discount."""

import unittest
from solution import Solution


class TestMinimumCost(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(self.s.minimumCost([1, 2, 3]), 5)

    def test_example2(self):
        self.assertEqual(self.s.minimumCost([6, 5, 7, 9, 2, 2]), 23)

    def test_example3(self):
        self.assertEqual(self.s.minimumCost([5, 5]), 10)

    # Edge cases
    def test_single_candy(self):
        self.assertEqual(self.s.minimumCost([7]), 7)

    def test_exact_triplet(self):
        self.assertEqual(self.s.minimumCost([3, 3, 3]), 6)

    def test_four_candies(self):
        self.assertEqual(self.s.minimumCost([1, 2, 3, 4]), 9)

    def test_all_equal(self):
        self.assertEqual(self.s.minimumCost([5, 5, 5, 5, 5, 5]), 20)

    def test_two_triplets(self):
        self.assertEqual(self.s.minimumCost([10, 9, 8, 7, 6, 5]), 32)

    def test_alias(self):
        self.assertEqual(self.s.max_difference([1, 2, 3]), 5)


if __name__ == "__main__":
    unittest.main()
