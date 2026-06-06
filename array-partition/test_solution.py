"""Tests for array_pair_sum."""

from solution import array_pair_sum


def test_example_1():
    assert array_pair_sum([1, 4, 3, 2]) == 4


def test_example_2():
    assert array_pair_sum([6, 2, 6, 5, 1, 2]) == 9


def test_single_pair():
    assert array_pair_sum([1, 2]) == 1


def test_negative_numbers():
    assert array_pair_sum([-1, -2, -3, -4]) == -6


def test_mixed_positive_negative():
    assert array_pair_sum([-1, 2, -3, 4]) == -1


def test_all_identical():
    assert array_pair_sum([5, 5, 5, 5]) == 10


def test_large_input():
    nums = list(range(1, 20001))  # 2 * 10000 elements
    # Sorted: 1,2,...,20000. Sum of odd-indexed: 1+3+5+...+19999
    expected = sum(range(1, 20001, 2))  # 10000^2 = 100000000
    assert array_pair_sum(nums) == expected
