"""Tests for reverse_words_in_string."""

import sys
sys.path.insert(0, "../implementer")

from solution import reverse_words_in_string


def test_example_1():
    assert reverse_words_in_string("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"


def test_example_2():
    assert reverse_words_in_string("God Ding") == "doG gniD"


def test_single_word():
    assert reverse_words_in_string("hello") == "olleh"


def test_single_character():
    assert reverse_words_in_string("a") == "a"


def test_special_characters():
    assert reverse_words_in_string("a!b c@d") == "b!a d@c"


def test_all_same_characters():
    assert reverse_words_in_string("aaa bbb") == "aaa bbb"


def test_single_char_words():
    assert reverse_words_in_string("a b c") == "a b c"


def test_large_input():
    word = "abcde"
    s = " ".join([word] * 10000)
    expected = " ".join(["edcba"] * 10000)
    assert reverse_words_in_string(s) == expected
