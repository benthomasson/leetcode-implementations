"""Tests for maximum difference between increasing elements."""

import unittest
import sys
sys.path.insert(0, "../implementer")
from solution import min_steps_to_equal_elements


class TestMaxDifference(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(min_steps_to_equal_elements([7, 1, 5, 4]), 4)

    def test_example2(self):
        self.assertEqual(min_steps_to_equal_elements([9, 4, 3, 2]), -1)

    def test_example3(self):
        self.assertEqual(min_steps_to_equal_elements([1, 5, 2, 10]), 9)

    # Edge cases
    def test_two_elements_increasing(self):
        self.assertEqual(min_steps_to_equal_elements([1, 2]), 1)

    def test_two_elements_decreasing(self):
        self.assertEqual(min_steps_to_equal_elements([2, 1]), -1)

    def test_all_equal(self):
        self.assertEqual(min_steps_to_equal_elements([5, 5, 5]), -1)

    def test_large_values(self):
        self.assertEqual(min_steps_to_equal_elements([1, 10**9]), 999999999)

    def test_strictly_increasing(self):
        self.assertEqual(min_steps_to_equal_elements([1, 2, 3, 4, 5]), 4)

    def test_strictly_decreasing(self):
        self.assertEqual(min_steps_to_equal_elements([5, 4, 3, 2, 1]), -1)

    def test_best_pair_not_adjacent(self):
        self.assertEqual(min_steps_to_equal_elements([3, 5, 1, 8]), 7)


if __name__ == "__main__":
    unittest.main()
