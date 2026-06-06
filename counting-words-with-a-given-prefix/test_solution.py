"""Tests for count_prefixes."""

from solution import count_prefixes


def test_example1():
    assert count_prefixes(["pay", "attention", "practice", "attend"], "at") == 2


def test_example2():
    assert count_prefixes(["leetcode", "win", "loops", "success"], "code") == 0


def test_all_match():
    assert count_prefixes(["abc", "abd", "abe"], "ab") == 3


def test_none_match():
    assert count_prefixes(["xyz", "yyy"], "a") == 0


def test_prefix_equals_word():
    assert count_prefixes(["hello", "world"], "hello") == 1


def test_prefix_longer_than_word():
    assert count_prefixes(["ab", "a"], "abc") == 0


def test_single_char_prefix():
    assert count_prefixes(["apple", "banana", "avocado"], "a") == 2


def test_single_word_list():
    assert count_prefixes(["test"], "te") == 1


def test_single_word_no_match():
    assert count_prefixes(["test"], "xx") == 0
