"""Tests for Find the K-Beauty of a Number."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import num_elements_with_smaller_and_greater


def test_example1():
    assert num_elements_with_smaller_and_greater(240, 2) == 2


def test_example2():
    assert num_elements_with_smaller_and_greater(430043, 2) == 2


def test_single_digit():
    assert num_elements_with_smaller_and_greater(5, 1) == 1


def test_zero_substring_skipped():
    assert num_elements_with_smaller_and_greater(10, 1) == 1


def test_k_equals_full_length():
    assert num_elements_with_smaller_and_greater(240, 3) == 1


def test_all_same_digits():
    assert num_elements_with_smaller_and_greater(111, 1) == 3


def test_no_divisors():
    assert num_elements_with_smaller_and_greater(13, 1) == 1


def test_large_num():
    assert num_elements_with_smaller_and_greater(1000000000, 1) == 1
