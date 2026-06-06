import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import count_once_in_both


def test_example_1():
    assert count_once_in_both([1, 100, 200, 1, 100], 1) == 100


def test_example_2():
    assert count_once_in_both([2, 2, 2, 2, 3], 2) == 2


def test_minimal_array():
    assert count_once_in_both([5, 7], 5) == 7


def test_key_at_last_index_only_counts_earlier():
    # key appears at end but only the earlier occurrence (index 0) counts
    assert count_once_in_both([1, 3, 1], 1) == 3


def test_key_follows_key():
    # consecutive keys: key->key->other => key:2, other:1
    assert count_once_in_both([4, 4, 4, 9], 4) == 4


def test_all_identical():
    assert count_once_in_both([7, 7, 7, 7], 7) == 7


def test_multiple_targets_unique_winner():
    # key=1: follows are 2,3,2 => 2 wins with count 2
    assert count_once_in_both([1, 2, 1, 3, 1, 2], 1) == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
