"""Tests for Find the K-Beauty of a Number."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import divisor_substrings


def test_example1():
    assert divisor_substrings(240, 2) == 2


def test_example2():
    assert divisor_substrings(430043, 2) == 2


def test_single_digit():
    assert divisor_substrings(5, 1) == 1


def test_zero_substring_skipped():
    assert divisor_substrings(10, 1) == 1


def test_k_equals_full_length():
    assert divisor_substrings(240, 3) == 1


def test_all_same_digits():
    assert divisor_substrings(111, 1) == 3


def test_no_divisors():
    assert divisor_substrings(13, 1) == 1


def test_large_num():
    assert divisor_substrings(1000000000, 1) == 1
