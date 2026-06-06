"""Tests for count_arithmetic_triplets."""

from solution import count_arithmetic_triplets


def test_example_1():
    assert count_arithmetic_triplets([0, 1, 4, 6, 7, 10], 3) == 2


def test_example_2():
    assert count_arithmetic_triplets([4, 5, 6, 7, 8, 9], 2) == 2


def test_no_triplets():
    assert count_arithmetic_triplets([1, 2, 3], 5) == 0


def test_minimum_length_with_triplet():
    assert count_arithmetic_triplets([1, 3, 5], 2) == 1


def test_all_form_triplets():
    assert count_arithmetic_triplets([0, 2, 4, 6, 8], 2) == 3


def test_large_diff():
    assert count_arithmetic_triplets([0, 50, 100, 150, 200], 50) == 3


def test_consecutive_with_diff_1():
    assert count_arithmetic_triplets([1, 2, 3, 4, 5], 1) == 3


def test_single_triplet_at_end():
    assert count_arithmetic_triplets([1, 2, 5, 10, 15], 5) == 1
