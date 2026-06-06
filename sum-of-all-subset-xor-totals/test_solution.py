"""Tests for subsetXORSum."""

import unittest
from solution import subsetXORSum


class TestSubsetXORSum(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(subsetXORSum([1, 3]), 6)

    def test_example2(self):
        self.assertEqual(subsetXORSum([5, 1, 6]), 28)

    def test_example3(self):
        self.assertEqual(subsetXORSum([3, 4, 5, 6, 7, 8]), 480)

    def test_single_element(self):
        self.assertEqual(subsetXORSum([7]), 7)

    def test_two_same_elements(self):
        # Subsets: [], [5], [5], [5,5] -> 0 + 5 + 5 + 0 = 10
        self.assertEqual(subsetXORSum([5, 5]), 10)

    def test_all_same(self):
        # [3,3,3]: OR=3, 3 * 2^2 = 12
        self.assertEqual(subsetXORSum([3, 3, 3]), 12)

    def test_max_constraints(self):
        nums = list(range(1, 13))  # 12 elements
        result = subsetXORSum(nums)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_powers_of_two(self):
        # [1,2,4]: OR=7, 7 * 2^2 = 28
        self.assertEqual(subsetXORSum([1, 2, 4]), 28)


if __name__ == "__main__":
    unittest.main()
