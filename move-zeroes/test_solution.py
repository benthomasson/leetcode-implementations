"""Tests for Move Zeroes."""

from solution import moveZeroes


def _run(nums, expected):
    moveZeroes(nums)
    assert nums == expected, f"Expected {expected}, got {nums}"


def test_basic():
    _run([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])


def test_single_zero():
    _run([0], [0])


def test_single_nonzero():
    _run([1], [1])


def test_all_zeros():
    _run([0, 0, 0], [0, 0, 0])


def test_no_zeros():
    _run([1, 2, 3], [1, 2, 3])


def test_zeros_at_start():
    _run([0, 0, 1, 2], [1, 2, 0, 0])


def test_zeros_at_end():
    _run([1, 2, 0, 0], [1, 2, 0, 0])


def test_alternating():
    _run([0, 1, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0])


def test_large_values():
    _run([-(2**31), 0, 2**31 - 1], [-(2**31), 2**31 - 1, 0])


def test_already_ordered():
    _run([1, 3, 12, 0, 0], [1, 3, 12, 0, 0])
