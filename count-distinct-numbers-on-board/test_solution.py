"""Tests for Count Distinct Numbers on Board."""

from solution import distinct_numbers


def test_example_1():
    assert distinct_numbers(5) == 4


def test_example_2():
    assert distinct_numbers(3) == 2


def test_n_equals_1():
    assert distinct_numbers(1) == 1


def test_n_equals_2():
    assert distinct_numbers(2) == 1


def test_n_equals_100():
    assert distinct_numbers(100) == 99
