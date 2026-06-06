"""Tests for min_operations."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import min_operations


def test_example_1():
    assert min_operations("WBBWWBBWBW", 7) == 3


def test_example_2():
    assert min_operations("WBWBBBW", 2) == 0


def test_all_black():
    assert min_operations("BBBBB", 3) == 0


def test_all_white():
    assert min_operations("WWWWW", 3) == 3


def test_k_equals_n():
    assert min_operations("WBWBW", 5) == 3


def test_k_equals_1_black():
    assert min_operations("B", 1) == 0


def test_k_equals_1_white():
    assert min_operations("W", 1) == 1


def test_best_window_at_end():
    assert min_operations("WWWBBB", 3) == 0


def test_best_window_at_start():
    assert min_operations("BBBWWW", 3) == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
