import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import largest_unique_number


def test_example_1():
    assert largest_unique_number([5, 7, 3, 9, 4, 9, 8, 3, 1]) == 8


def test_example_2():
    assert largest_unique_number([9, 9, 8, 8]) == -1


def test_single_element():
    assert largest_unique_number([42]) == 42


def test_all_duplicates():
    assert largest_unique_number([1, 1, 2, 2, 3, 3]) == -1


def test_all_unique():
    assert largest_unique_number([1, 2, 3, 4, 5]) == 5


def test_zero():
    assert largest_unique_number([0]) == 0


def test_mixed_unique_and_dup():
    assert largest_unique_number([1, 2, 2, 3, 3]) == 1


def test_max_boundary_value():
    assert largest_unique_number([1000, 999, 1000]) == 999
