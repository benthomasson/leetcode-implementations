"""Tests for minimum difference between highest and lowest of k scores."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import max_distance


class TestMaxDistance(unittest.TestCase):
    def test_example1_single_element(self):
        self.assertEqual(max_distance([90], 1), 0)

    def test_example2(self):
        self.assertEqual(max_distance([9, 4, 1, 7], 2), 2)

    def test_k_equals_one(self):
        self.assertEqual(max_distance([5, 3, 8, 1], 1), 0)

    def test_k_equals_length(self):
        self.assertEqual(max_distance([9, 4, 1, 7], 4), 8)

    def test_all_identical(self):
        self.assertEqual(max_distance([5, 5, 5, 5], 3), 0)

    def test_already_sorted(self):
        self.assertEqual(max_distance([1, 2, 3, 4, 5], 3), 2)

    def test_reverse_sorted(self):
        self.assertEqual(max_distance([5, 4, 3, 2, 1], 3), 2)

    def test_max_constraint_values(self):
        self.assertEqual(max_distance([0, 100000], 2), 100000)

    def test_duplicates_with_window(self):
        self.assertEqual(max_distance([1, 1, 3, 3, 6], 2), 0)

    def test_input_mutation_correctness(self):
        """Ensure result is correct even though input is mutated."""
        nums = [10, 1, 4, 7, 2]
        result = max_distance(nums, 3)
        self.assertEqual(result, 3)  # sorted: [1,2,4,7,10], best window [1,2,4]


if __name__ == "__main__":
    unittest.main()
