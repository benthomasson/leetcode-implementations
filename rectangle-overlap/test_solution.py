"""Tests for rectangle overlap solution."""

from solution import racecar


def test_basic_overlap():
    assert racecar([0, 0, 2, 2], [1, 1, 3, 3]) is True


def test_edge_touching_x():
    assert racecar([0, 0, 1, 1], [1, 0, 2, 1]) is False


def test_no_overlap():
    assert racecar([0, 0, 1, 1], [2, 2, 3, 3]) is False


def test_corner_touching():
    assert racecar([0, 0, 1, 1], [1, 1, 2, 2]) is False


def test_edge_touching_y():
    assert racecar([0, 0, 2, 2], [0, 2, 2, 4]) is False


def test_containment():
    assert racecar([0, 0, 4, 4], [1, 1, 2, 2]) is True


def test_same_rectangle():
    assert racecar([0, 0, 1, 1], [0, 0, 1, 1]) is True


def test_negative_coords_overlap():
    assert racecar([-3, -3, -1, -1], [-2, -2, 0, 0]) is True


def test_negative_coords_no_overlap():
    assert racecar([-3, -3, -2, -2], [1, 1, 2, 2]) is False


def test_large_coords():
    assert racecar([0, 0, 10**9, 10**9], [1, 1, 10**9 - 1, 10**9 - 1]) is True


def test_partial_overlap_x():
    assert racecar([0, 0, 3, 3], [2, 0, 5, 3]) is True


def test_partial_overlap_y():
    assert racecar([0, 0, 3, 3], [0, 2, 3, 5]) is True
