"""Tests for third_max."""

from solution import third_max


def test_three_distinct():
    assert third_max([3, 2, 1]) == 1


def test_two_distinct():
    assert third_max([1, 2]) == 2


def test_duplicates():
    assert third_max([2, 2, 3, 1]) == 1


def test_single_element():
    assert third_max([5]) == 5


def test_all_identical():
    assert third_max([1, 1, 1]) == 1


def test_negatives():
    assert third_max([-1, -2, -3]) == -3


def test_mixed_signs():
    assert third_max([-1, 0, 1]) == -1


def test_int_min_boundary():
    assert third_max([1, 2, -(2**31)]) == -(2**31)


def test_int_max_boundary():
    assert third_max([2**31 - 1, 2**31 - 2, 2**31 - 3]) == 2**31 - 3


def test_more_than_three_distinct():
    assert third_max([5, 3, 4, 1, 2]) == 3


def test_duplicates_with_fewer_than_three_distinct():
    assert third_max([1, 1, 2, 2]) == 2
