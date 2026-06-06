"""Tests for kWeakestRows."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import kWeakestRows


def test_example_1():
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    assert kWeakestRows(mat, 3) == [2, 0, 3]


def test_example_2():
    mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
    assert kWeakestRows(mat, 2) == [0, 2]


def test_all_zeros():
    mat = [[0,0],[0,0],[0,0]]
    assert kWeakestRows(mat, 2) == [0, 1]


def test_all_ones():
    mat = [[1,1],[1,1],[1,1]]
    assert kWeakestRows(mat, 3) == [0, 1, 2]


def test_k_equals_m():
    mat = [[1,0],[0,0],[1,1]]
    assert kWeakestRows(mat, 3) == [1, 0, 2]


def test_single_column():
    mat = [[1],[0],[1]]
    assert kWeakestRows(mat, 1) == [1]


def test_2x2_minimum():
    mat = [[1,0],[0,0]]
    assert kWeakestRows(mat, 1) == [1]


def test_tiebreak_by_index():
    mat = [[1,0,0],[1,0,0],[1,0,0]]
    assert kWeakestRows(mat, 3) == [0, 1, 2]
