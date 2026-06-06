"""Tests for Special Positions in a Binary Matrix."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution

import pytest

s = Solution()


def test_example1():
    assert s.numSpecial([[1,0,0],[0,0,1],[1,0,0]]) == 1


def test_example2_identity():
    assert s.numSpecial([[1,0,0],[0,1,0],[0,0,1]]) == 3


def test_all_zeros():
    assert s.numSpecial([[0,0],[0,0]]) == 0


def test_all_ones():
    assert s.numSpecial([[1,1],[1,1]]) == 0


def test_single_one():
    assert s.numSpecial([[1]]) == 1


def test_single_zero():
    assert s.numSpecial([[0]]) == 0


def test_single_row():
    assert s.numSpecial([[0,1,0,0]]) == 1


def test_single_column():
    assert s.numSpecial([[0],[1],[0]]) == 1


def test_no_special_shared_col():
    # Two 1s in same column — neither is special
    assert s.numSpecial([[1,0],[1,0]]) == 0


def test_large_identity():
    n = 100
    mat = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    assert s.numSpecial(mat) == 100
