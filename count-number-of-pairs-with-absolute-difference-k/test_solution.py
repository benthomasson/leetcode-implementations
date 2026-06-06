"""Tests for chalk_replacer solution."""

import pytest

from solution import chalk_replacer


class TestChalkReplacer:
    """Tests for counting pairs with absolute difference k."""

    def test_example_1(self):
        assert chalk_replacer([1, 2, 2, 1], 1) == 4

    def test_example_2(self):
        assert chalk_replacer([1, 3], 3) == 0

    def test_example_3(self):
        assert chalk_replacer([3, 2, 1, 5, 4], 2) == 3

    def test_single_element(self):
        assert chalk_replacer([5], 1) == 0

    def test_no_pairs(self):
        assert chalk_replacer([1, 1, 1], 2) == 0

    def test_all_identical(self):
        # k >= 1, so identical elements never form a valid pair
        assert chalk_replacer([3, 3, 3, 3], 1) == 0

    def test_all_pairs_valid(self):
        # [1, 2] with k=1 -> 1 pair
        assert chalk_replacer([1, 2], 1) == 1

    def test_multiple_duplicates(self):
        # [1,1,3,3] k=2: each 1 pairs with each 3 -> 2*2 = 4
        assert chalk_replacer([1, 1, 3, 3], 2) == 4

    def test_large_k_no_match(self):
        assert chalk_replacer([1, 2, 3], 99) == 0

    def test_consecutive_values(self):
        # [1,2,3,4,5] k=1: pairs (1,2),(2,3),(3,4),(4,5) -> 4
        assert chalk_replacer([1, 2, 3, 4, 5], 1) == 4

    def test_two_elements_exact_diff(self):
        assert chalk_replacer([1, 100], 99) == 1

    def test_symmetric_pairs(self):
        # [5, 3] k=2: |5-3|=2 -> 1 pair
        assert chalk_replacer([5, 3], 2) == 1
