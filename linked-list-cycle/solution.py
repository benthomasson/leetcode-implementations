"""Linked List Cycle detection using Floyd's algorithm."""

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    """Detect if a linked list has a cycle using Floyd's tortoise and hare.

    Args:
        head: Head node of the linked list.

    Returns:
        True if the list contains a cycle, False otherwise.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# --- Helper ---

def make_list(vals: list[int], pos: int = -1) -> Optional[ListNode]:
    """Build a linked list from values, with optional cycle at index pos."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# --- Tests ---

def test_empty():
    assert hasCycle(None) is False

def test_single_no_cycle():
    assert hasCycle(make_list([1])) is False

def test_single_self_cycle():
    assert hasCycle(make_list([1], pos=0)) is True

def test_two_no_cycle():
    assert hasCycle(make_list([1, 2])) is False

def test_two_with_cycle():
    assert hasCycle(make_list([1, 2], pos=0)) is True

def test_example1():
    assert hasCycle(make_list([3, 2, 0, -4], pos=1)) is True

def test_example2():
    assert hasCycle(make_list([1, 2], pos=0)) is True

def test_example3():
    assert hasCycle(make_list([1], pos=-1)) is False

def test_long_no_cycle():
    assert hasCycle(make_list(list(range(100)))) is False

def test_long_with_cycle():
    assert hasCycle(make_list(list(range(100)), pos=50)) is True

def test_cycle_at_tail():
    assert hasCycle(make_list([1, 2, 3], pos=2)) is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
