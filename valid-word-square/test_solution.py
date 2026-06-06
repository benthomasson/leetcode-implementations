"""Tests for valid_word_square."""

import sys
sys.path.insert(0, "../implementer")

from solution import valid_word_square


def test_example1_perfect_square():
    assert valid_word_square(["abcd", "bnrt", "crmy", "dtye"]) is True


def test_example2_ragged_valid():
    assert valid_word_square(["abcd", "bnrt", "crm", "dt"]) is True


def test_example3_mismatch():
    assert valid_word_square(["ball", "area", "read", "lady"]) is False


def test_single_char():
    assert valid_word_square(["a"]) is True


def test_single_word_too_long():
    assert valid_word_square(["ab"]) is False


def test_ragged_valid_two_words():
    assert valid_word_square(["ab", "b"]) is True


def test_row_shorter_than_column():
    # Row 1 has length 1, but column 1 needs length 2
    assert valid_word_square(["ab", "b", "c"]) is False


def test_more_rows_than_cols():
    # 3 rows but first row only 2 chars — column 2 exists but row 0 has no char at index 2
    # words[2][0]='c' would need words[0][2] to exist
    assert valid_word_square(["a", "b", "c"]) is False


def test_empty_string_in_list():
    # ["a", ""] — row 0="a", col 0="a"; row 1="", col 1="". Valid.
    assert valid_word_square(["a", ""]) is True
