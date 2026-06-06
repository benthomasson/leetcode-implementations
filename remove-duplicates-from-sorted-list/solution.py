"""Remove Duplicates from Sorted List."""
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """Delete duplicates from a sorted linked list so each element appears once.

    Args:
        head: Head of a sorted linked list.

    Returns:
        Head of the deduplicated sorted linked list.
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


# --- helpers ---

def to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# --- tests ---

import unittest


class TestDeleteDuplicates(unittest.TestCase):
    def check(self, input_vals, expected):
        self.assertEqual(to_list(delete_duplicates(from_list(input_vals))), expected)

    def test_example1(self):
        self.check([1, 1, 2], [1, 2])

    def test_example2(self):
        self.check([1, 1, 2, 3, 3], [1, 2, 3])

    def test_empty(self):
        self.check([], [])

    def test_single(self):
        self.check([1], [1])

    def test_no_duplicates(self):
        self.check([1, 2, 3], [1, 2, 3])

    def test_all_same(self):
        self.check([5, 5, 5, 5], [5])

    def test_duplicates_at_tail(self):
        self.check([1, 2, 3, 3], [1, 2, 3])

    def test_duplicates_at_head(self):
        self.check([1, 1, 2, 3], [1, 2, 3])

    def test_negative_values(self):
        self.check([-3, -3, -1, 0, 0, 1], [-3, -1, 0, 1])

    def test_large_list(self):
        vals = []
        for v in range(-100, 101):
            vals.extend([v] * 3)
        self.check(vals, list(range(-100, 101)))


if __name__ == "__main__":
    unittest.main()
