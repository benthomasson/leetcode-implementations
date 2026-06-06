"""Tests for Armstrong Number solution."""

from solution import is_armstrong


def test_single_digits():
    for i in range(1, 10):
        assert is_armstrong(i) is True


def test_known_armstrong_numbers():
    for n in [153, 370, 371, 407]:
        assert is_armstrong(n) is True


def test_non_armstrong_numbers():
    for n in [10, 100, 123, 200]:
        assert is_armstrong(n) is False


def test_boundaries():
    assert is_armstrong(1) is True
    assert is_armstrong(100000000) is False
