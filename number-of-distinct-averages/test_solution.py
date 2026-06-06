"""Tests for distinctAverages."""

from solution import distinctAverages


def test_example1():
    assert distinctAverages([4, 1, 4, 0, 3, 5]) == 2


def test_example2():
    assert distinctAverages([1, 100]) == 1


def test_all_same():
    assert distinctAverages([5, 5, 5, 5]) == 1


def test_all_distinct_averages():
    assert distinctAverages([1, 2, 3, 10]) == 2


def test_duplicates_in_input():
    assert distinctAverages([0, 0, 100, 100]) == 1


def test_consecutive():
    assert distinctAverages([1, 2, 3, 4, 5, 6]) == 3


def test_min_length():
    assert distinctAverages([0, 100]) == 1


def test_all_zeros():
    assert distinctAverages([0, 0, 0, 0, 0, 0]) == 1
