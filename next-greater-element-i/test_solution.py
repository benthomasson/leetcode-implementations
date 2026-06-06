"""Tests for Next Greater Element I."""

from solution import next_greater_element


def test_example_1():
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]


def test_example_2():
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]


def test_single_element():
    assert next_greater_element([1], [1]) == [-1]


def test_all_descending():
    assert next_greater_element([3, 2, 1], [3, 2, 1]) == [-1, -1, -1]


def test_all_ascending():
    assert next_greater_element([1, 2, 3], [1, 2, 3]) == [2, 3, -1]


def test_nums1_equals_nums2():
    assert next_greater_element([1, 3, 4, 2], [1, 3, 4, 2]) == [3, 4, -1, -1]


def test_boundary_values():
    assert next_greater_element([0, 10000], [0, 10000]) == [10000, -1]


def test_subset_query():
    assert next_greater_element([5], [1, 5, 3, 7]) == [7]
