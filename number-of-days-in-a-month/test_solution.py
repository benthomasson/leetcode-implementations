"""Tests for number_of_days."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import number_of_days


def test_example1():
    assert number_of_days(1992, 7) == 31

def test_example2():
    assert number_of_days(2000, 2) == 29

def test_example3():
    assert number_of_days(1900, 2) == 28

def test_regular_leap_year():
    assert number_of_days(2024, 2) == 29

def test_non_leap_year():
    assert number_of_days(2023, 2) == 28

def test_non_leap_century_2100():
    assert number_of_days(2100, 2) == 28

def test_30_day_months():
    for m in [4, 6, 9, 11]:
        assert number_of_days(2000, m) == 30

def test_31_day_months():
    for m in [1, 3, 5, 7, 8, 10, 12]:
        assert number_of_days(2000, m) == 31

def test_boundary_year_1583():
    assert number_of_days(1583, 1) == 31
