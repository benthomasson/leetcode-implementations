"""Tests for can-make-arithmetic-progression-from-sequence."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import can_construct


def test_example_1():
    assert can_construct([3, 5, 1]) is True


def test_example_2():
    assert can_construct([1, 2, 4]) is False


def test_two_elements():
    assert can_construct([7, 3]) is True


def test_all_equal():
    assert can_construct([5, 5, 5, 5]) is True


def test_negative_numbers():
    assert can_construct([-3, -1, -5, -7]) is True


def test_reverse_sorted():
    assert can_construct([10, 8, 6, 4, 2]) is True


def test_large_values():
    assert can_construct([-1000000, 0, 1000000]) is True


def test_not_ap():
    assert can_construct([1, 3, 6, 10]) is False


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
