from solution import longestPalindromeSubseq


def test_example_1():
    assert longestPalindromeSubseq(["abc", "aabc", "bc"]) is True


def test_example_2():
    assert longestPalindromeSubseq(["ab", "a"]) is False


def test_single_word():
    assert longestPalindromeSubseq(["abc"]) is True


def test_identical_words():
    assert longestPalindromeSubseq(["aa", "aa", "aa"]) is True


def test_all_same_char_uneven():
    assert longestPalindromeSubseq(["a", "aa"]) is False


def test_all_same_char_even():
    assert longestPalindromeSubseq(["aa", "a", "a", "aa"]) is True


def test_many_distinct_chars():
    assert longestPalindromeSubseq(["ab", "cd", "ef"]) is False


def test_two_empty_style():
    # All chars divisible by 2
    assert longestPalindromeSubseq(["aabb", "bbaa"]) is True


def test_single_char_strings():
    assert longestPalindromeSubseq(["a", "b", "c"]) is True
