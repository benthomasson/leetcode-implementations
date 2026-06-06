"""Tests for Find Resultant Array After Removing Anagrams."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import anagramOperations


def test_example1():
    assert anagramOperations(["abba", "baba", "bbaa", "cd", "cd"]) == ["abba", "cd"]


def test_example2():
    assert anagramOperations(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"]


def test_single_word():
    assert anagramOperations(["hello"]) == ["hello"]


def test_all_anagrams():
    assert anagramOperations(["abc", "bca", "cab"]) == ["abc"]


def test_no_anagrams():
    assert anagramOperations(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]


def test_duplicate_words():
    assert anagramOperations(["aa", "aa", "aa"]) == ["aa"]


def test_anagram_chain_then_different():
    assert anagramOperations(["ab", "ba", "ab", "cd"]) == ["ab", "cd"]


def test_non_adjacent_anagrams_kept():
    assert anagramOperations(["ab", "cd", "ba"]) == ["ab", "cd", "ba"]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
