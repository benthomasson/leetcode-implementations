"""Tests for Valid Palindrome II."""

import unittest
from solution import validPalindrome


class TestValidPalindrome(unittest.TestCase):

    def test_already_palindrome(self):
        assert validPalindrome("aba") is True
        assert validPalindrome("racecar") is True

    def test_one_delete_palindrome(self):
        assert validPalindrome("abca") is True
        assert validPalindrome("abcba") is True  # already palindrome, 0 deletes

    def test_not_palindrome(self):
        assert validPalindrome("abc") is False

    def test_single_char(self):
        assert validPalindrome("a") is True

    def test_two_chars(self):
        assert validPalindrome("ab") is True
        assert validPalindrome("aa") is True

    def test_empty_string(self):
        assert validPalindrome("") is True

    def test_all_same(self):
        assert validPalindrome("aaaa") is True

    def test_delete_at_edges(self):
        assert validPalindrome("cbbcc") is True  # delete first c

    def test_delete_in_middle(self):
        assert validPalindrome("deeee") is False

    def test_long_palindrome_with_one_off(self):
        s = "a" * 50000 + "b" + "a" * 50000
        assert validPalindrome(s) is True

    def test_needs_two_deletions(self):
        assert validPalindrome("abcdef") is False


if __name__ == "__main__":
    unittest.main()
