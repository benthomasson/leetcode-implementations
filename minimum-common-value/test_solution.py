"""Tests for min_common_number."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import min_common_number


def test_example_1():
    assert min_common_number([1, 2, 3], [2, 4]) == 2


def test_example_2():
    assert min_common_number([1, 2, 3, 6], [2, 3, 4, 5]) == 2


def test_no_common():
    assert min_common_number([1, 3, 5], [2, 4, 6]) == -1


def test_single_element_match():
    assert min_common_number([5], [5]) == 5


def test_single_element_no_match():
    assert min_common_number([1], [2]) == -1


def test_identical_arrays():
    assert min_common_number([1, 2, 3], [1, 2, 3]) == 1


def test_common_at_end():
    assert min_common_number([1, 2, 10], [3, 4, 10]) == 10


def test_duplicates():
    assert min_common_number([1, 2, 2, 3], [2, 2, 4]) == 2


def test_large_values():
    assert min_common_number([999999999], [1, 999999999]) == 999999999


def test_disjoint_ranges():
    assert min_common_number([1, 2, 3], [4, 5, 6]) == -1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
