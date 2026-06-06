"""Tests for Jewels and Stones solution."""

from solution import num_jewels_in_stones


def test_example_1():
    assert num_jewels_in_stones("aA", "aAAbbbb") == 3


def test_example_2():
    assert num_jewels_in_stones("z", "ZZ") == 0


def test_empty_stones():
    assert num_jewels_in_stones("abc", "") == 0


def test_empty_jewels():
    assert num_jewels_in_stones("", "aAAbbbb") == 0


def test_all_jewels():
    assert num_jewels_in_stones("ab", "aabb") == 4


def test_no_matches():
    assert num_jewels_in_stones("abc", "xyz") == 0


def test_case_sensitivity():
    assert num_jewels_in_stones("a", "AaAa") == 2


def test_single_chars():
    assert num_jewels_in_stones("a", "a") == 1
    assert num_jewels_in_stones("a", "b") == 0
