from solution import canPermutePalindrome


def test_examples():
    assert canPermutePalindrome("code") is False
    assert canPermutePalindrome("aab") is True
    assert canPermutePalindrome("carerac") is True


def test_single_char():
    assert canPermutePalindrome("a") is True


def test_even_palindrome():
    assert canPermutePalindrome("abba") is True


def test_all_same():
    assert canPermutePalindrome("aaaa") is True


def test_all_unique():
    assert canPermutePalindrome("abcd") is False


def test_two_chars():
    assert canPermutePalindrome("aa") is True
    assert canPermutePalindrome("ab") is False


def test_odd_length_non_palindrome():
    assert canPermutePalindrome("abc") is False
