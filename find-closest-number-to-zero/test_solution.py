"""Tests for find-closest-number-to-zero."""

from solution import robot_instructions


def test_example_1():
    assert robot_instructions([-4, -2, 1, 4, 8]) == 1


def test_example_2():
    assert robot_instructions([2, -1, 1]) == 1


def test_single_element():
    assert robot_instructions([5]) == 5
    assert robot_instructions([-3]) == -3


def test_zero_present():
    assert robot_instructions([-5, 0, 5]) == 0


def test_all_negative():
    assert robot_instructions([-10, -3, -7]) == -3


def test_positive_negative_tie():
    assert robot_instructions([-2, 2]) == 2
    assert robot_instructions([3, -3, 5]) == 3


def test_all_same():
    assert robot_instructions([4, 4, 4]) == 4
    assert robot_instructions([-1, -1, -1]) == -1


def test_large_values():
    assert robot_instructions([-100000, 100000]) == 100000
    assert robot_instructions([-100000, 99999]) == 99999
