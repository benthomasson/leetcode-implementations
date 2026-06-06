"""Tests for smallest_index."""

from solution import smallest_index


def test_example1_all_match():
    assert smallest_index([0, 1, 2]) == 0


def test_example2_single_match():
    assert smallest_index([4, 3, 2, 1]) == 2


def test_example3_no_match():
    assert smallest_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1


def test_single_element_match():
    assert smallest_index([0]) == 0


def test_single_element_no_match():
    assert smallest_index([1]) == -1


def test_mod10_wrap():
    # Index 12: 12 % 10 == 2
    nums = [9] * 12 + [2]
    assert smallest_index(nums) == 12


def test_max_length_no_match():
    assert smallest_index([9] * 100) == -1


def test_max_length_last_match():
    # Index 99: 99 % 10 == 9
    nums = [5] * 99 + [9]
    assert smallest_index(nums) == 99
