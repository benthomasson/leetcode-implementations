"""Tests for Valid Parentheses solution."""

import unittest
from solution import is_valid


class TestIsValid(unittest.TestCase):

    def test_simple_pairs(self):
        assert is_valid("()") is True
        assert is_valid("[]") is True
        assert is_valid("{}") is True

    def test_multiple_pairs(self):
        assert is_valid("()[]{}") is True

    def test_nested(self):
        assert is_valid("{[()]}") is True
        assert is_valid("([{}])") is True

    def test_mismatch(self):
        assert is_valid("(]") is False
        assert is_valid("[)") is False
        assert is_valid("{)") is False

    def test_unclosed(self):
        assert is_valid("(") is False
        assert is_valid("([") is False

    def test_extra_closer(self):
        assert is_valid(")") is False
        assert is_valid("())") is False

    def test_empty(self):
        assert is_valid("") is True

    def test_single_char(self):
        assert is_valid("(") is False
        assert is_valid(")") is False

    def test_interleaved(self):
        assert is_valid("([)]") is False
        assert is_valid("{[}]") is False


if __name__ == "__main__":
    unittest.main()
