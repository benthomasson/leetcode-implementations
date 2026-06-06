"""Tests for Linked List Cycle detection."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import ListNode, hasCycle, make_list


# --- LeetCode examples ---

def test_example1_cycle_at_pos1():
    assert hasCycle(make_list([3, 2, 0, -4], pos=1)) is True

def test_example2_cycle_at_pos0():
    assert hasCycle(make_list([1, 2], pos=0)) is True

def test_example3_no_cycle():
    assert hasCycle(make_list([1], pos=-1)) is False


# --- Edge cases ---

def test_empty_list():
    assert hasCycle(None) is False

def test_single_node_no_cycle():
    assert hasCycle(make_list([1])) is False

def test_single_node_self_cycle():
    assert hasCycle(make_list([1], pos=0)) is True

def test_two_nodes_no_cycle():
    assert hasCycle(make_list([1, 2])) is False

def test_long_list_no_cycle():
    assert hasCycle(make_list(list(range(100)))) is False

def test_long_list_cycle_at_middle():
    assert hasCycle(make_list(list(range(100)), pos=50)) is True

def test_cycle_pointing_to_tail():
    """Tail's next points to itself."""
    assert hasCycle(make_list([1, 2, 3], pos=2)) is True
