"""Tests for determine-if-string-halves-are-alike."""

import sys
sys.path.insert(0, "../implementer")

from solution import numSpecial


def test_example1_book():
    assert numSpecial("book") is True

def test_example2_textbook():
    assert numSpecial("textbook") is False

def test_all_vowels():
    assert numSpecial("aeiou AEIOU") is True

def test_no_vowels():
    assert numSpecial("bcdf") is True

def test_min_length():
    assert numSpecial("ab") is False

def test_min_length_equal():
    assert numSpecial("ae") is True

def test_mixed_case_vowels():
    assert numSpecial("AbBa") is True

def test_vowels_only_first_half():
    assert numSpecial("aabb") is False

def test_long_string():
    assert numSpecial("a" * 500 + "e" * 500) is True
