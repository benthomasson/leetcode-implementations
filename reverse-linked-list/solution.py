"""Reverse Linked List - LeetCode #206."""

from __future__ import annotations
from typing import Optional
import unittest


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list iteratively.

    Args:
        head: Head node of the linked list.

    Returns:
        Head node of the reversed linked list.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list recursively.

    Args:
        head: Head node of the linked list.

    Returns:
        Head node of the reversed linked list.
    """
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# --- Test helpers ---

def to_linked_list(vals: list[int]) -> Optional[ListNode]:
    """Convert a list of ints to a linked list."""
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a list of ints."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --- Tests ---

class TestReverseList(unittest.TestCase):

    def _run_both(self, input_vals, expected):
        for fn in (reverse_list, reverse_list_recursive):
            with self.subTest(fn=fn.__name__):
                head = to_linked_list(input_vals)
                result = to_list(fn(head))
                self.assertEqual(result, expected)

    def test_standard(self):
        self._run_both([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

    def test_two_nodes(self):
        self._run_both([1, 2], [2, 1])

    def test_empty(self):
        self._run_both([], [])

    def test_single_node(self):
        self._run_both([1], [1])

    def test_negative_values(self):
        self._run_both([-1, -2, -3], [-3, -2, -1])

    def test_duplicates(self):
        self._run_both([1, 1, 2, 2], [2, 2, 1, 1])


if __name__ == "__main__":
    unittest.main()
