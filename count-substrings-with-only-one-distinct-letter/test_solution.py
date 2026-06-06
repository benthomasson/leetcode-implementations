"""Tests for count_letters."""

from solution import count_letters


def test_example_1():
    assert count_letters("aaaba") == 8


def test_example_2():
    assert count_letters("aaaaaaaaaa") == 55


def test_single_char():
    assert count_letters("a") == 1


def test_all_different():
    assert count_letters("abcde") == 5


def test_two_groups():
    assert count_letters("aabb") == 6  # 3 + 3


def test_single_repeated():
    assert count_letters("bbb") == 6  # 3+2+1


def test_alternating():
    assert count_letters("ababab") == 6  # each char is its own group
