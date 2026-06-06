"""Tests for count_odds."""

from solution import count_odds


def test_both_odd():
    assert count_odds(3, 7) == 3


def test_both_even():
    assert count_odds(8, 10) == 1


def test_mixed_odd_even():
    assert count_odds(3, 8) == 3


def test_mixed_even_odd():
    assert count_odds(4, 7) == 2


def test_single_odd():
    assert count_odds(5, 5) == 1


def test_single_even():
    assert count_odds(4, 4) == 0


def test_zero():
    assert count_odds(0, 0) == 0


def test_one():
    assert count_odds(1, 1) == 1


def test_large_range():
    assert count_odds(0, 1_000_000_000) == 500_000_000


def test_large_both_odd():
    assert count_odds(999_999_999, 999_999_999) == 1
