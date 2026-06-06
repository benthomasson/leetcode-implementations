"""Tests for countBits solution."""

from solution import countBits


def test_zero():
    assert countBits(0) == [0]


def test_one():
    assert countBits(1) == [0, 1]


def test_two():
    assert countBits(2) == [0, 1, 1]


def test_five():
    assert countBits(5) == [0, 1, 1, 2, 1, 2]


def test_fifteen():
    result = countBits(15)
    assert len(result) == 16
    # Powers of 2 should have exactly 1 bit set
    assert result[1] == 1
    assert result[2] == 1
    assert result[4] == 1
    assert result[8] == 1
    # 15 = 1111 -> 4 bits
    assert result[15] == 4
    # 7 = 111 -> 3 bits
    assert result[7] == 3


def test_large():
    result = countBits(100000)
    assert len(result) == 100001
    assert result[0] == 0
    assert result[1] == 1
