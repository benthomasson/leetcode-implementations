"""Tests for even_odd_indices."""

from solution import even_odd_indices


def test_example_17():
    assert even_odd_indices(17) == [2, 0]


def test_example_2():
    assert even_odd_indices(2) == [0, 1]


def test_n_1():
    # 1 = 1b -> bit 0 (even)
    assert even_odd_indices(1) == [1, 0]


def test_n_7():
    # 7 = 111b -> bits 0,1,2 -> even: 0,2 -> 2 even, 1 odd
    assert even_odd_indices(7) == [2, 1]


def test_n_15():
    # 15 = 1111b -> bits 0,1,2,3 -> even: 0,2 -> 2; odd: 1,3 -> 2
    assert even_odd_indices(15) == [2, 2]


def test_power_of_2():
    # 8 = 1000b -> bit 3 (odd)
    assert even_odd_indices(8) == [0, 1]
    # 4 = 100b -> bit 2 (even)
    assert even_odd_indices(4) == [1, 0]


def test_n_1000():
    # 1000 = 1111101000b -> bits set: 3,4,5,6,7,9
    # even indices (0,2,4,6,8): 4,6 -> 2
    # odd indices (1,3,5,7,9): 3,5,7,9 -> 4
    assert even_odd_indices(1000) == [2, 4]
