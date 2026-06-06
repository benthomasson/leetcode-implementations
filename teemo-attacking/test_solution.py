"""Tests for Teemo Attacking solution."""

import unittest
from solution import find_poisoned_duration


class TestFindPoisonedDuration(unittest.TestCase):

    def test_example1_no_overlap(self):
        self.assertEqual(find_poisoned_duration([1, 4], 2), 4)

    def test_example2_overlap(self):
        self.assertEqual(find_poisoned_duration([1, 2], 2), 3)

    def test_single_attack(self):
        self.assertEqual(find_poisoned_duration([5], 3), 3)

    def test_adjacent_attacks(self):
        self.assertEqual(find_poisoned_duration([1, 3], 2), 4)

    def test_fully_overlapping(self):
        self.assertEqual(find_poisoned_duration([1, 2, 3], 5), 7)

    def test_no_overlap_multiple(self):
        self.assertEqual(find_poisoned_duration([1, 10, 20], 3), 9)

    def test_empty_list(self):
        self.assertEqual(find_poisoned_duration([], 5), 0)

    def test_duration_zero(self):
        self.assertEqual(find_poisoned_duration([1, 2], 0), 0)

    def test_duplicate_timestamps(self):
        self.assertEqual(find_poisoned_duration([1, 1, 1], 2), 2)

    def test_large_gap(self):
        self.assertEqual(find_poisoned_duration([0, 10000000], 1), 2)


if __name__ == "__main__":
    unittest.main()
