"""Tests for Nim Game solution."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import canWinNim


def test_example_1():
    assert canWinNim(4) is False

def test_example_2():
    assert canWinNim(1) is True

def test_example_3():
    assert canWinNim(2) is True

def test_three_stones():
    assert canWinNim(3) is True

def test_multiples_of_4_lose():
    for n in [4, 8, 12, 16, 100]:
        assert canWinNim(n) is False, f"n={n} should be False"

def test_non_multiples_of_4_win():
    for n in [5, 6, 7, 9, 10, 11]:
        assert canWinNim(n) is True, f"n={n} should be True"

def test_large_multiple_of_4():
    assert canWinNim(2147483644) is False  # 2^31 - 4

def test_large_non_multiple_of_4():
    assert canWinNim(2147483647) is True  # 2^31 - 1
