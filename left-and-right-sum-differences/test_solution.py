"""Tests for get_answer."""

from solution import get_answer


def test_example_1():
    assert get_answer([10, 4, 8, 3]) == [15, 1, 11, 22]


def test_example_2():
    assert get_answer([1]) == [0]


def test_two_elements():
    assert get_answer([1, 2]) == [2, 1]


def test_all_equal():
    assert get_answer([5, 5, 5]) == [10, 0, 10]


def test_large_values():
    assert get_answer([100000, 100000]) == [100000, 100000]
