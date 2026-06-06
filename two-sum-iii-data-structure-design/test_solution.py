"""Tests for TwoSum III - Data Structure Design."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import TwoSum


def test_example():
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    assert ts.find(4) is True   # 1 + 3
    assert ts.find(7) is False


def test_empty():
    ts = TwoSum()
    assert ts.find(0) is False


def test_single_element():
    ts = TwoSum()
    ts.add(5)
    assert ts.find(10) is False  # need two elements


def test_duplicates_sum():
    ts = TwoSum()
    ts.add(3)
    ts.add(3)
    assert ts.find(6) is True  # 3 + 3 = 6


def test_duplicate_needed_but_only_one():
    ts = TwoSum()
    ts.add(3)
    assert ts.find(6) is False  # only one 3


def test_negative_numbers():
    ts = TwoSum()
    ts.add(-1)
    ts.add(3)
    assert ts.find(2) is True   # -1 + 3 = 2
    assert ts.find(-2) is False


def test_zero_sum():
    ts = TwoSum()
    ts.add(-5)
    ts.add(5)
    assert ts.find(0) is True  # -5 + 5 = 0


def test_zero_duplicates():
    ts = TwoSum()
    ts.add(0)
    ts.add(0)
    assert ts.find(0) is True  # 0 + 0 = 0


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
