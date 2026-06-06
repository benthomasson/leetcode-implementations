"""Tests for circular sentence solution."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import is_circular


# LeetCode examples
def test_example1_circular_multi_word():
    assert is_circular("leetcode exercises sound delightful") is True

def test_example2_single_word_circular():
    assert is_circular("eetcode") is True

def test_example3_not_circular():
    assert is_circular("Leetcode is cool") is False

# Edge cases
def test_single_char():
    assert is_circular("a") is True

def test_single_word_not_circular():
    assert is_circular("Leetcode") is False

def test_two_words_circular():
    assert is_circular("ab ba") is True

def test_two_words_not_circular():
    assert is_circular("ab cd") is False

def test_case_sensitive():
    assert is_circular("Ab ba") is False

def test_all_same_letter():
    assert is_circular("aaa aaa aaa") is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
