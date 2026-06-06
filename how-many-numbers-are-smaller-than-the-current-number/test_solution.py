"""Tests for How Many Numbers Are Smaller Than the Current Number."""

import pytest

from solution import Solution


@pytest.fixture
def solution():
    return Solution()


class TestSmallerNumbersThanCurrent:
    """Tests for Solution.smallerNumbersThanCurrent."""

    def test_example_1(self, solution):
        assert solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]

    def test_example_2(self, solution):
        assert solution.smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]

    def test_example_3_all_identical(self, solution):
        assert solution.smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]

    def test_two_elements_ascending(self, solution):
        assert solution.smallerNumbersThanCurrent([0, 1]) == [0, 1]

    def test_two_elements_descending(self, solution):
        assert solution.smallerNumbersThanCurrent([1, 0]) == [1, 0]

    def test_two_elements_equal(self, solution):
        assert solution.smallerNumbersThanCurrent([5, 5]) == [0, 0]

    def test_sorted_ascending(self, solution):
        assert solution.smallerNumbersThanCurrent([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]

    def test_sorted_descending(self, solution):
        assert solution.smallerNumbersThanCurrent([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]

    def test_boundary_values_zero_and_hundred(self, solution):
        assert solution.smallerNumbersThanCurrent([0, 100, 0, 100]) == [0, 2, 0, 2]

    def test_all_zeros(self, solution):
        assert solution.smallerNumbersThanCurrent([0, 0, 0]) == [0, 0, 0]

    def test_all_hundreds(self, solution):
        assert solution.smallerNumbersThanCurrent([100, 100]) == [0, 0]

    def test_single_unique_rest_duplicates(self, solution):
        assert solution.smallerNumbersThanCurrent([3, 3, 3, 1]) == [1, 1, 1, 0]
