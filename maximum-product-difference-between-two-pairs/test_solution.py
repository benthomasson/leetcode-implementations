"""Tests for Maximum Product Difference Between Two Pairs."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import max_product_difference


def test_example_1():
    assert max_product_difference([5, 6, 2, 7, 4]) == 34


def test_example_2():
    assert max_product_difference([4, 2, 5, 9, 7, 4, 8]) == 64


def test_four_elements():
    assert max_product_difference([1, 2, 3, 4]) == 10  # 4*3 - 1*2


def test_all_equal():
    assert max_product_difference([5, 5, 5, 5]) == 0


def test_duplicates():
    assert max_product_difference([1, 1, 10, 10]) == 99  # 100 - 1


def test_already_sorted():
    assert max_product_difference([1, 2, 3, 4, 5]) == 18  # 5*4 - 1*2


def test_reverse_sorted():
    assert max_product_difference([5, 4, 3, 2, 1]) == 18


def test_large_values():
    assert max_product_difference([10000, 9999, 1, 2]) == 99990000 - 2  # 10000*9999 - 1*2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
