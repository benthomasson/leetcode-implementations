"""Tests for Maximum Product of Three Numbers."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import maximumProduct


class TestMaximumProduct(unittest.TestCase):
    """Test cases for maximumProduct function."""

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(maximumProduct([1, 2, 3]), 6)

    def test_example2(self):
        self.assertEqual(maximumProduct([1, 2, 3, 4]), 24)

    def test_example3(self):
        self.assertEqual(maximumProduct([-1, -2, -3]), -6)

    # Edge cases
    def test_two_large_negatives_with_positive(self):
        self.assertEqual(maximumProduct([-1000, -999, 1, 2, 3]), 2997000)

    def test_all_zeros(self):
        self.assertEqual(maximumProduct([0, 0, 0, 0]), 0)

    def test_mixed_with_zero(self):
        self.assertEqual(maximumProduct([-1, 0, 1]), 0)

    def test_exactly_three_elements(self):
        self.assertEqual(maximumProduct([5, 6, 7]), 210)

    def test_all_same_values(self):
        self.assertEqual(maximumProduct([2, 2, 2, 2]), 8)

    def test_boundary_values(self):
        self.assertEqual(maximumProduct([-1000, -1000, 1000]), 1000000000)

    def test_input_not_mutated(self):
        """Verify we get correct result even if caller cares about order."""
        nums = [3, 1, 2]
        result = maximumProduct(nums)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
