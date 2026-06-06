"""Tests for subtract_product_and_sum."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import subtract_product_and_sum


def test_example_234():
    assert subtract_product_and_sum(234) == 15


def test_example_4421():
    assert subtract_product_and_sum(4421) == 21


def test_single_digit():
    assert subtract_product_and_sum(5) == 0


def test_one():
    assert subtract_product_and_sum(1) == 0


def test_contains_zero():
    # digits 1,0 → product=0, sum=1 → -1
    assert subtract_product_and_sum(10) == -1


def test_max_same_digits():
    # 99999 → product=9^5=59049, sum=45 → 59004
    assert subtract_product_and_sum(99999) == 59004


def test_two_digits():
    # 11 → product=1, sum=2 → -1
    assert subtract_product_and_sum(11) == -1


def test_large_with_zero():
    # 100000 → product=0, sum=1 → -1
    assert subtract_product_and_sum(100000) == -1
