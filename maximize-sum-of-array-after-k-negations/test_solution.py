"""Tests for Maximize Sum of Array After K Negations."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import largest_sum_after_k_negations


def test_example1():
    assert largest_sum_after_k_negations([4, 2, 3], 1) == 5


def test_example2():
    assert largest_sum_after_k_negations([3, -1, 0, 2], 3) == 6


def test_example3():
    assert largest_sum_after_k_negations([2, -3, -1, 5, -4], 2) == 13


def test_all_positive_odd_k():
    assert largest_sum_after_k_negations([1, 2, 3], 1) == 4  # 5 - 2*1 = 4  (negate smallest)


def test_all_positive_even_k():
    assert largest_sum_after_k_negations([1, 2, 3], 2) == 6  # even remaining, no change


def test_all_negative():
    assert largest_sum_after_k_negations([-1, -2, -3], 3) == 6


def test_contains_zero():
    assert largest_sum_after_k_negations([-1, 0, 1], 3) == 2


def test_single_element_negate():
    assert largest_sum_after_k_negations([5], 1) == -5


def test_single_element_even():
    assert largest_sum_after_k_negations([5], 2) == 5


def test_single_negative():
    assert largest_sum_after_k_negations([-5], 1) == 5


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
