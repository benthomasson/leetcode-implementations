"""Tests for alternating digit sum."""

from solution import sum_of_digits


def test_examples():
    assert sum_of_digits(521) == 4
    assert sum_of_digits(111) == 1
    assert sum_of_digits(886996) == 0


def test_single_digit():
    assert sum_of_digits(1) == 1
    assert sum_of_digits(9) == 9


def test_two_digits():
    assert sum_of_digits(10) == 1  # (+1) + (-0)
    assert sum_of_digits(48) == -4  # (+4) + (-8)


def test_boundary():
    assert sum_of_digits(1000000000) == 1  # 10^9


def test_same_digits_even_length():
    assert sum_of_digits(5555) == 0  # (+5)+(-5)+(+5)+(-5)


def test_same_digits_odd_length():
    assert sum_of_digits(555) == 5  # (+5)+(-5)+(+5)
