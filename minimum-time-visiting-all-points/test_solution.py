"""Tests for minimum time visiting all points."""

from solution import minTimeToVisitAllPoints


def test_example1():
    assert minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]) == 7


def test_example2():
    assert minTimeToVisitAllPoints([[3, 2], [-2, 2]]) == 5


def test_single_point():
    assert minTimeToVisitAllPoints([[0, 0]]) == 0


def test_identical_points():
    assert minTimeToVisitAllPoints([[1, 1], [1, 1]]) == 0


def test_horizontal_only():
    assert minTimeToVisitAllPoints([[0, 0], [5, 0]]) == 5


def test_vertical_only():
    assert minTimeToVisitAllPoints([[0, 0], [0, 3]]) == 3


def test_diagonal_only():
    assert minTimeToVisitAllPoints([[0, 0], [4, 4]]) == 4


def test_negative_coordinates():
    assert minTimeToVisitAllPoints([[-3, -2], [2, 3]]) == 5
