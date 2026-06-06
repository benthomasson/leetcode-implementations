"""Tests for Two Out of Three solution."""

from solution import largest_odd


def test_example_1():
    assert sorted(largest_odd([1, 1, 3, 2], [2, 3], [3])) == [2, 3]


def test_example_2():
    assert sorted(largest_odd([3, 1], [2, 3], [1, 2])) == [1, 2, 3]


def test_example_3():
    assert largest_odd([1, 2, 2], [4, 3, 3], [5]) == []


def test_all_identical():
    assert sorted(largest_odd([1, 2], [1, 2], [1, 2])) == [1, 2]


def test_single_elements_overlap():
    assert largest_odd([1], [1], [2]) == [1]


def test_single_elements_no_overlap():
    assert largest_odd([1], [2], [3]) == []


def test_value_in_all_three():
    assert largest_odd([5], [5], [5]) == [5]


def test_duplicates_within_arrays():
    assert sorted(largest_odd([1, 1, 1], [1, 2, 2], [2, 3, 3])) == [1, 2]
