import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import stringWithDifferentDifference


def test_example1():
    assert stringWithDifferentDifference(["adc", "wzy", "abc"]) == "abc"


def test_example2():
    assert stringWithDifferentDifference(["aaa", "bob", "ccc", "ddd"]) == "bob"


def test_odd_at_start():
    assert stringWithDifferentDifference(["abc", "wzy", "adc"]) == "abc"


def test_odd_in_middle():
    assert stringWithDifferentDifference(["adc", "abc", "wzy"]) == "abc"


def test_odd_at_end():
    assert stringWithDifferentDifference(["wzy", "adc", "abc"]) == "abc"


def test_min_length_strings():
    # 2-char strings: single-element diff arrays
    assert stringWithDifferentDifference(["ab", "cd", "ef", "zz"]) == "zz"


def test_three_words_minimum():
    assert stringWithDifferentDifference(["ab", "cd", "zz"]) == "zz"


def test_all_same_char_except_one():
    # All "aaa" except one "abc"
    assert stringWithDifferentDifference(["aaa", "aaa", "aaa", "abc"]) == "abc"


def test_longer_strings():
    # 5-char strings to verify multi-element diff arrays
    # "abcde" -> (1,1,1,1), "acegi" -> (2,2,2,2), "bdfhj" -> (2,2,2,2)
    assert stringWithDifferentDifference(["acegi", "bdfhj", "abcde"]) == "abcde"


def test_many_words():
    # 100 words (max constraint), odd one out is in the middle
    words = ["ab"] * 50 + ["az"] + ["ab"] * 49
    assert stringWithDifferentDifference(words) == "az"
