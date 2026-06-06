"""Tests for KthLargest - Kth Largest Element in a Stream."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import KthLargest


def test_example():
    """Problem example: k=3, nums=[4,5,8,2]."""
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8


def test_k_equals_1():
    """k=1 should always return the max element."""
    kth = KthLargest(1, [5])
    assert kth.add(3) == 5
    assert kth.add(6) == 6
    assert kth.add(2) == 6


def test_empty_initial():
    """Empty initial nums, elements added via add()."""
    kth = KthLargest(1, [])
    assert kth.add(1) == 1
    assert kth.add(2) == 2


def test_negative_numbers():
    """Negative values in stream."""
    kth = KthLargest(2, [-1, -2, -3])
    assert kth.add(-4) == -2
    assert kth.add(0) == -1
    assert kth.add(5) == 0


def test_duplicates():
    """Duplicate values should be treated as separate elements."""
    kth = KthLargest(3, [5, 5, 5])
    assert kth.add(5) == 5
    assert kth.add(5) == 5


def test_add_smaller_than_kth():
    """Adding a value smaller than kth largest doesn't change result."""
    kth = KthLargest(2, [3, 5])
    assert kth.add(1) == 3
    assert kth.add(0) == 3


def test_k_equals_length():
    """k equals the length of initial nums."""
    kth = KthLargest(3, [1, 2, 3])
    assert kth.add(0) == 1
    assert kth.add(4) == 2


def test_single_element_stream():
    """k=1 with no initial nums, single add."""
    kth = KthLargest(1, [])
    assert kth.add(42) == 42


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
