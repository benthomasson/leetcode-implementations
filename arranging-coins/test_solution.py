"""Tests for arrange_coins."""

from solution import arrange_coins


def test_examples():
    assert arrange_coins(5) == 2
    assert arrange_coins(8) == 3


def test_single_coin():
    assert arrange_coins(1) == 1


def test_perfect_staircases():
    assert arrange_coins(3) == 2   # 1+2
    assert arrange_coins(6) == 3   # 1+2+3
    assert arrange_coins(10) == 4  # 1+2+3+4


def test_one_short():
    assert arrange_coins(2) == 1   # 1+2 needs 3, only have 2
    assert arrange_coins(9) == 3   # 1+2+3+4 needs 10, only have 9


def test_max_constraint():
    assert arrange_coins(2**31 - 1) == 65535
