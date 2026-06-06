"""Tests for count_segments."""

from solution import count_segments


def test_multiple_words():
    assert count_segments("Hello, my name is John") == 5


def test_single_word():
    assert count_segments("Hello") == 1


def test_empty_string():
    assert count_segments("") == 0


def test_all_spaces():
    assert count_segments("     ") == 0


def test_leading_trailing_spaces():
    assert count_segments("  Hello, my name is John  ") == 5


def test_multiple_spaces_between_words():
    assert count_segments("Hello   world") == 2


def test_single_character():
    assert count_segments("a") == 1


def test_single_space():
    assert count_segments(" ") == 0


def test_special_characters():
    assert count_segments("!@# $%^ &*()") == 3


def test_trailing_space_from_example():
    assert count_segments("Hello, my name is John ") == 5
