"""Tests for K Items With the Maximum Sum."""

from solution import max_sum


def test_example_1():
    assert max_sum(3, 2, 0, 2) == 2


def test_example_2():
    assert max_sum(3, 2, 0, 4) == 3


def test_k_zero():
    assert max_sum(3, 2, 1, 0) == 0


def test_all_ones():
    assert max_sum(5, 0, 0, 5) == 5


def test_all_zeros():
    assert max_sum(0, 5, 0, 5) == 0


def test_all_neg_ones():
    assert max_sum(0, 0, 5, 5) == -5


def test_k_equals_total():
    assert max_sum(3, 2, 1, 6) == 2


def test_ones_and_neg_ones():
    assert max_sum(2, 0, 3, 4) == 0


def test_single_one():
    assert max_sum(1, 0, 0, 1) == 1


def test_single_zero():
    assert max_sum(0, 1, 0, 1) == 0


def test_single_neg_one():
    assert max_sum(0, 0, 1, 1) == -1


def test_take_ones_and_zeros():
    assert max_sum(2, 3, 5, 5) == 2


def test_take_some_neg():
    assert max_sum(2, 3, 5, 7) == 0
