"""Tests for second_highest."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import second_highest


def test_example1():
    assert second_highest("dfa12321afd") == 2


def test_example2():
    assert second_highest("abc1111") == -1


def test_no_digits():
    assert second_highest("abcdef") == -1


def test_single_digit():
    assert second_highest("a5b") == -1


def test_two_distinct_digits():
    assert second_highest("a9b3") == 3


def test_all_ten_digits():
    assert second_highest("0123456789") == 8


def test_only_digits():
    assert second_highest("9876") == 8


def test_zeros_and_ones():
    assert second_highest("a0b1") == 0


def test_repeated_digits_no_second():
    assert second_highest("5555") == -1


def test_letters_only_long():
    assert second_highest("abcdefghijklmnopqrstuvwxyz") == -1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
