"""Tests for well_spaced_string."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import well_spaced_string

ZEROS = [0] * 26


def _dist(**kwargs):
    """Helper: returns a distance array with specified letter distances."""
    d = [0] * 26
    for letter, val in kwargs.items():
        d[ord(letter) - ord("a")] = val
    return d


# --- Problem examples ---

def test_example1():
    assert well_spaced_string("abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) is True


def test_example2():
    assert well_spaced_string("aa", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) is False


# --- Edge cases ---

def test_adjacent_pair_distance_zero():
    assert well_spaced_string("bb", ZEROS) is True


def test_adjacent_pair_wrong_distance():
    assert well_spaced_string("bb", _dist(b=1)) is False


def test_pair_at_boundaries():
    # 'a' at 0 and 3, gap = 2
    assert well_spaced_string("abba", _dist(a=2, b=0)) is True


def test_pair_at_boundaries_wrong():
    assert well_spaced_string("abba", _dist(a=1, b=0)) is False


def test_max_distance():
    # 'a' at 0 and 51 with 50 other chars between -> distance 50
    s = "a" + "b" * 25 + "b" * 25 + "a"
    # Wait, each letter appears exactly twice. Let me construct properly.
    # Use 25 distinct letters between two 'a's
    middle = "".join(chr(ord("b") + i) * 2 for i in range(25))
    s = "a" + middle + "a"
    d = _dist(a=50)
    # All middle letters are adjacent pairs with distance 0, which matches ZEROS default
    assert well_spaced_string(s, d) is True


def test_all_26_letters_adjacent():
    s = "".join(c * 2 for c in "abcdefghijklmnopqrstuvwxyz")
    assert well_spaced_string(s, ZEROS) is True


def test_one_pair_mismatch_among_many():
    # Two pairs correct, one wrong
    # a at 0,2 gap=1; b at 1,3 gap=1; but say distance for b should be 2
    assert well_spaced_string("abab", _dist(a=1, b=2)) is False
