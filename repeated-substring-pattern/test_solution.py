"""Tests for repeated substring pattern solution."""

from solution import can_construct


def test_repeated_two_copies():
    assert can_construct("abab") is True

def test_not_repeated():
    assert can_construct("aba") is False

def test_repeated_four_copies():
    assert can_construct("abcabcabcabc") is True

def test_single_char():
    assert can_construct("a") is False

def test_two_same_chars():
    assert can_construct("aa") is True

def test_all_same_chars():
    assert can_construct("aaaa") is True

def test_two_char_no_repeat():
    assert can_construct("ab") is False

def test_repeated_twice():
    assert can_construct("abcabc") is True

def test_long_pattern():
    assert can_construct("abcdabcd") is True

def test_almost_repeated():
    assert can_construct("abacabac") is True

def test_no_repeat_long():
    assert can_construct("abcde") is False

def test_single_char_repeated():
    assert can_construct("bbb") is True
