"""Tests for height_checker solution."""

from solution import height_checker


def test_example_1():
    assert height_checker([1, 1, 4, 2, 1, 3]) == 3


def test_example_2():
    assert height_checker([5, 1, 2, 3, 4]) == 5


def test_example_3():
    assert height_checker([1, 2, 3, 4, 5]) == 0


def test_single_element():
    assert height_checker([1]) == 0


def test_all_same():
    assert height_checker([3, 3, 3, 3]) == 0


def test_reverse_sorted():
    assert height_checker([4, 3, 2, 1]) == 4


def test_two_elements_sorted():
    assert height_checker([1, 2]) == 0


def test_two_elements_unsorted():
    assert height_checker([2, 1]) == 2


def test_boundary_values():
    assert height_checker([100, 1]) == 2


def test_boundary_min():
    assert height_checker([1]) == 0


def test_boundary_max():
    assert height_checker([100]) == 0


def test_duplicates_with_mismatches():
    assert height_checker([2, 1, 2, 1]) == 2
