"""Tests for max_captured_forts."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import max_captured_forts


def test_example_1():
    assert max_captured_forts([1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4


def test_example_2():
    assert max_captured_forts([0, 0, 1, -1]) == 0


def test_single_element():
    assert max_captured_forts([1]) == 0
    assert max_captured_forts([0]) == 0
    assert max_captured_forts([-1]) == 0


def test_all_zeros():
    assert max_captured_forts([0, 0, 0]) == 0


def test_adjacent_opposite():
    assert max_captured_forts([1, -1]) == 0
    assert max_captured_forts([-1, 1]) == 0


def test_no_your_fort():
    assert max_captured_forts([-1, 0, 0, -1]) == 0


def test_no_empty_position():
    assert max_captured_forts([1, 0, 0, 1]) == 0


def test_left_to_right():
    assert max_captured_forts([1, 0, 0, 0, -1]) == 3


def test_right_to_left():
    assert max_captured_forts([-1, 0, 0, 0, 1]) == 3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
