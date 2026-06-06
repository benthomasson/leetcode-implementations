"""Remove Linked List Elements - LeetCode #203."""

from __future__ import annotations
import unittest
from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """Remove all nodes with the given value from a linked list.

    Args:
        head: Head of the linked list.
        val: Value to remove.

    Returns:
        Head of the modified linked list.
    """
    dummy = ListNode(next=head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


# --- Helpers ---

def to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# --- Tests ---

class TestRemoveElements(unittest.TestCase):

    def check(self, vals, val, expected):
        result = to_list(remove_elements(from_list(vals), val))
        self.assertEqual(result, expected)

    def test_example1(self):
        self.check([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])

    def test_example2(self):
        self.check([], 1, [])

    def test_example3(self):
        self.check([7, 7, 7, 7], 7, [])

    def test_single_match(self):
        self.check([1], 1, [])

    def test_single_no_match(self):
        self.check([1], 2, [1])

    def test_no_matches(self):
        self.check([1, 2, 3], 4, [1, 2, 3])

    def test_head_removal(self):
        self.check([1, 1, 2, 3], 1, [2, 3])

    def test_tail_removal(self):
        self.check([1, 2, 3, 3], 3, [1, 2])

    def test_consecutive_middle(self):
        self.check([1, 2, 2, 2, 3], 2, [1, 3])


if __name__ == "__main__":
    unittest.main()
