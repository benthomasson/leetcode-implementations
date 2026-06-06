"""Tests for Minimum Number of Moves to Seat Everyone."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import min_moves_to_seat


class TestMinMovesToSeat(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertEqual(min_moves_to_seat([3, 1, 5], [2, 7, 4]), 4)

    def test_example2(self):
        self.assertEqual(min_moves_to_seat([4, 1, 5, 9], [1, 3, 2, 6]), 7)

    def test_example3(self):
        self.assertEqual(min_moves_to_seat([2, 2, 6, 6], [1, 3, 2, 6]), 4)

    # Edge cases
    def test_single_element(self):
        self.assertEqual(min_moves_to_seat([5], [3]), 2)

    def test_already_matched(self):
        self.assertEqual(min_moves_to_seat([1, 2, 3], [1, 2, 3]), 0)

    def test_all_same_position(self):
        self.assertEqual(min_moves_to_seat([5, 5, 5], [5, 5, 5]), 0)

    def test_reverse_sorted(self):
        self.assertEqual(min_moves_to_seat([3, 2, 1], [1, 2, 3]), 0)

    def test_max_constraint_values(self):
        self.assertEqual(min_moves_to_seat([1], [100]), 99)

    def test_duplicates_both_sides(self):
        self.assertEqual(min_moves_to_seat([1, 1], [2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
