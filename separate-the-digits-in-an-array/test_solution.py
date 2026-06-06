"""Tests for separate_digits."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import separate_digits


def test_example1():
    assert separate_digits([13, 25, 83, 77]) == [1, 3, 2, 5, 8, 3, 7, 7]


def test_example2():
    assert separate_digits([7, 1, 3, 9]) == [7, 1, 3, 9]


def test_single_element():
    assert separate_digits([5]) == [5]


def test_large_number():
    assert separate_digits([100000]) == [1, 0, 0, 0, 0, 0]


def test_numbers_with_zeros():
    assert separate_digits([10, 100]) == [1, 0, 1, 0, 0]


def test_mixed_digit_counts():
    assert separate_digits([10921]) == [1, 0, 9, 2, 1]


def test_all_same_digit():
    assert separate_digits([111, 22]) == [1, 1, 1, 2, 2]
