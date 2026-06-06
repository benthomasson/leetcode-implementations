"""Tests for is_prefix_string."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import is_prefix_string


def test_example1():
    assert is_prefix_string("iloveleetcode", ["i", "love", "leetcode", "apples"]) is True


def test_example2():
    assert is_prefix_string("iloveleetcode", ["apples", "i", "love", "leetcode"]) is False


def test_single_word_match():
    assert is_prefix_string("hello", ["hello", "world"]) is True


def test_single_word_no_match():
    assert is_prefix_string("hello", ["world"]) is False


def test_all_words_used():
    assert is_prefix_string("abc", ["a", "b", "c"]) is True


def test_s_longer_than_concat():
    assert is_prefix_string("abcdef", ["a", "b"]) is False


def test_partial_word_no_match():
    assert is_prefix_string("ab", ["a", "bc"]) is False


def test_prefix_matches_but_not_exact():
    assert is_prefix_string("ab", ["a", "b", "c"]) is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
