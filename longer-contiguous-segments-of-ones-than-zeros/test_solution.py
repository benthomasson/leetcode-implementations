"""Tests for checkZeroOnes."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import checkZeroOnes


def test_example1():
    assert checkZeroOnes("1101") is True

def test_example2():
    assert checkZeroOnes("111000") is False

def test_example3():
    assert checkZeroOnes("110100010") is False

def test_single_one():
    assert checkZeroOnes("1") is True

def test_single_zero():
    assert checkZeroOnes("0") is False

def test_all_ones():
    assert checkZeroOnes("1111") is True

def test_all_zeros():
    assert checkZeroOnes("0000") is False

def test_equal_lengths():
    assert checkZeroOnes("1100") is False

def test_alternating():
    assert checkZeroOnes("0101") is False

def test_ones_longer_at_end():
    assert checkZeroOnes("0011100") is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
