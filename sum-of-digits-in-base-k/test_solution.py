"""Tests for sum_base."""

from solution import sum_base


def test_example1():
    assert sum_base(34, 6) == 9


def test_example2():
    assert sum_base(10, 10) == 1


def test_n_is_1():
    for k in range(2, 11):
        assert sum_base(1, k) == 1


def test_base2():
    assert sum_base(8, 2) == 1   # 1000 in binary
    assert sum_base(7, 2) == 3   # 111 in binary
    assert sum_base(100, 2) == 3 # 1100100 in binary


def test_max_n_min_k():
    # 100 in base 2 = 1100100, sum = 3
    assert sum_base(100, 2) == 3


def test_same_base():
    # n < 10 in base 10 returns itself
    assert sum_base(5, 10) == 5
    assert sum_base(9, 10) == 9


def test_base_k_single_digit():
    # n < k means single digit, result is n itself
    assert sum_base(3, 7) == 3
    assert sum_base(2, 10) == 2
