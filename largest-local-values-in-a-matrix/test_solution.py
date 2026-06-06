"""Tests for largest_matrix."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import largest_matrix


def test_example_1():
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    assert largest_matrix(grid) == [[9, 9], [8, 6]]


def test_example_2():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    assert largest_matrix(grid) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]


def test_minimum_3x3():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert largest_matrix(grid) == [[9]]


def test_all_same_values():
    grid = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    assert largest_matrix(grid) == [[5]]


def test_max_in_corner():
    grid = [[100, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert largest_matrix(grid) == [[100]]


def test_max_value_at_boundary():
    grid = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 100],
    ]
    assert largest_matrix(grid) == [[1, 1], [1, 100]]


def test_descending_diagonal():
    grid = [
        [9, 1, 1, 1],
        [1, 8, 1, 1],
        [1, 1, 7, 1],
        [1, 1, 1, 6],
    ]
    assert largest_matrix(grid) == [[9, 8], [8, 8]]


def test_larger_grid_6x6():
    grid = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36],
    ]
    expected = [
        [15, 16, 17, 18],
        [21, 22, 23, 24],
        [27, 28, 29, 30],
        [33, 34, 35, 36],
    ]
    assert largest_matrix(grid) == expected
