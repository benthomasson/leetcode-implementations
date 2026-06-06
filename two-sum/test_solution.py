"""Tests for Two Sum solution."""

from solution import twoSum


def test_example1():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example2():
    assert twoSum([3, 2, 4], 6) == [1, 2]


def test_example3_duplicates():
    assert twoSum([3, 3], 6) == [0, 1]


def test_negative_numbers():
    assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_mixed_signs():
    assert twoSum([-3, 4, 3, 90], 0) == [0, 2]


def test_large_values():
    assert twoSum([1000000000, -1000000000], 0) == [0, 1]


def test_two_elements():
    assert twoSum([1, 2], 3) == [0, 1]
