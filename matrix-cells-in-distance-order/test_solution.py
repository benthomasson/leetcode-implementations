"""Tests for Matrix Cells in Distance Order (LeetCode 1030)."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


def _distances(result, rCenter, cCenter):
    return [abs(r - rCenter) + abs(c - cCenter) for r, c in result]


def _validate(result, rows, cols, rCenter, cCenter):
    """Check ordering, completeness, and uniqueness."""
    dists = _distances(result, rCenter, cCenter)
    assert dists == sorted(dists), "Distances not in non-decreasing order"
    assert len(result) == rows * cols, f"Expected {rows*cols} cells, got {len(result)}"
    assert len(set(map(tuple, result))) == len(result), "Duplicate cells found"
    assert result[0] == [rCenter, cCenter], "First cell must be the center"


def test_example1(sol):
    _validate(sol.allCellsDistOrder(1, 2, 0, 0), 1, 2, 0, 0)


def test_example2(sol):
    _validate(sol.allCellsDistOrder(2, 2, 0, 1), 2, 2, 0, 1)


def test_example3(sol):
    _validate(sol.allCellsDistOrder(2, 3, 1, 2), 2, 3, 1, 2)


def test_single_cell(sol):
    result = sol.allCellsDistOrder(1, 1, 0, 0)
    assert result == [[0, 0]]


def test_single_row(sol):
    _validate(sol.allCellsDistOrder(1, 5, 0, 2), 1, 5, 0, 2)


def test_single_column(sol):
    _validate(sol.allCellsDistOrder(5, 1, 2, 0), 5, 1, 2, 0)


def test_corner_top_left(sol):
    _validate(sol.allCellsDistOrder(3, 3, 0, 0), 3, 3, 0, 0)


def test_corner_bottom_right(sol):
    _validate(sol.allCellsDistOrder(3, 3, 2, 2), 3, 3, 2, 2)


def test_large_matrix(sol):
    _validate(sol.allCellsDistOrder(100, 100, 50, 50), 100, 100, 50, 50)


def test_rectangular(sol):
    _validate(sol.allCellsDistOrder(2, 5, 0, 4), 2, 5, 0, 4)
