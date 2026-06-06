"""Tests for Hamming Distance solution."""

from solution import hammingDistance


def test_example1():
    assert hammingDistance(1, 4) == 2


def test_example2():
    assert hammingDistance(3, 1) == 1


def test_same_number():
    assert hammingDistance(5, 5) == 0


def test_both_zero():
    assert hammingDistance(0, 0) == 0


def test_zero_and_max():
    assert hammingDistance(0, 2**31 - 1) == 31


def test_adjacent():
    assert hammingDistance(7, 8) == 4  # 0111 vs 1000


def test_one_apart():
    assert hammingDistance(0, 1) == 1


def test_max_and_max():
    assert hammingDistance(2**31 - 1, 2**31 - 1) == 0
