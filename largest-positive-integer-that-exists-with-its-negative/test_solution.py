"""Tests for find_K solution."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import unittest

from solution import find_K


class TestFindK(unittest.TestCase):
    """Test cases for the find_K function."""

    # --- LeetCode provided examples ---

    def test_example_1(self) -> None:
        self.assertEqual(find_K([-1, 2, -3, 3]), 3)

    def test_example_2(self) -> None:
        self.assertEqual(find_K([-1, 10, 6, 7, -7, 1]), 7)

    def test_example_3(self) -> None:
        self.assertEqual(find_K([-10, 8, 6, 7, -2, -3]), -1)

    # --- Edge cases ---

    def test_single_positive_element(self) -> None:
        self.assertEqual(find_K([1]), -1)

    def test_single_negative_element(self) -> None:
        self.assertEqual(find_K([-1]), -1)

    def test_one_valid_pair(self) -> None:
        self.assertEqual(find_K([1, -1]), 1)

    def test_all_positive(self) -> None:
        self.assertEqual(find_K([1, 2, 3, 4, 5]), -1)

    def test_all_negative(self) -> None:
        self.assertEqual(find_K([-1, -2, -3, -4, -5]), -1)

    # --- Multiple pairs ---

    def test_multiple_valid_pairs_returns_largest(self) -> None:
        self.assertEqual(find_K([1, -1, 2, -2, 3, -3]), 3)

    def test_non_consecutive_pairs(self) -> None:
        self.assertEqual(find_K([5, -5, 100, -100, 3]), 100)

    # --- Duplicates ---

    def test_duplicates_in_input(self) -> None:
        self.assertEqual(find_K([1, 1, -1, -1, 2, -2]), 2)

    # --- Boundary values ---

    def test_boundary_values(self) -> None:
        self.assertEqual(find_K([1000, -1000]), 1000)

    def test_large_array_all_pairs(self) -> None:
        nums = []
        for i in range(1, 501):
            nums.extend([i, -i])
        self.assertEqual(find_K(nums), 500)

    def test_no_pair_despite_mixed_signs(self) -> None:
        self.assertEqual(find_K([1, -2, 3, -4]), -1)


if __name__ == "__main__":
    unittest.main()
