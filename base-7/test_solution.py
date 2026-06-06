"""Tests for base 7 conversion."""

import sys
sys.path.insert(0, "../implementer")
from solution import convert_to_base7


def test_example_100():
    assert convert_to_base7(100) == "202"


def test_example_negative_7():
    assert convert_to_base7(-7) == "-10"


def test_zero():
    assert convert_to_base7(0) == "0"


def test_single_digits():
    for i in range(7):
        assert convert_to_base7(i) == str(i)


def test_power_of_7():
    assert convert_to_base7(49) == "100"


def test_negative():
    assert convert_to_base7(-1) == "-1"


def test_large_positive():
    assert convert_to_base7(10_000_000) == "150666343"


def test_large_negative():
    assert convert_to_base7(-10_000_000) == "-150666343"
