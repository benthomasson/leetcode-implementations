"""Tests for determine-if-string-halves-are-alike."""

import sys
sys.path.insert(0, "../implementer")

from solution import determine_if_string_halves_are_alike


def test_example1_book():
    assert determine_if_string_halves_are_alike("book") is True

def test_example2_textbook():
    assert determine_if_string_halves_are_alike("textbook") is False

def test_all_vowels():
    assert determine_if_string_halves_are_alike("aeiou AEIOU") is True

def test_no_vowels():
    assert determine_if_string_halves_are_alike("bcdf") is True

def test_min_length():
    assert determine_if_string_halves_are_alike("ab") is False

def test_min_length_equal():
    assert determine_if_string_halves_are_alike("ae") is True

def test_mixed_case_vowels():
    assert determine_if_string_halves_are_alike("AbBa") is True

def test_vowels_only_first_half():
    assert determine_if_string_halves_are_alike("aabb") is False

def test_long_string():
    assert determine_if_string_halves_are_alike("a" * 500 + "e" * 500) is True
