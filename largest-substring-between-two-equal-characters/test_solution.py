"""Tests for maxLengthBetweenEqualCharacters."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import maxLengthBetweenEqualCharacters


def test_example1_adjacent_equal():
    assert maxLengthBetweenEqualCharacters("aa") == 0


def test_example2_chars_between():
    assert maxLengthBetweenEqualCharacters("abca") == 2


def test_example3_no_repeats():
    assert maxLengthBetweenEqualCharacters("cbzxy") == -1


def test_single_char():
    assert maxLengthBetweenEqualCharacters("a") == -1


def test_all_same_chars():
    assert maxLengthBetweenEqualCharacters("aaaa") == 2


def test_equal_at_ends():
    assert maxLengthBetweenEqualCharacters("abcdefga") == 6


def test_multiple_pairs():
    assert maxLengthBetweenEqualCharacters("abcabc") == 2


def test_longest_from_first_occurrence():
    # 'a' at 0 and 8 gives length 7
    assert maxLengthBetweenEqualCharacters("aabcddefa") == 7


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
