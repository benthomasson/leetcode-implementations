"""Merge Two Sorted Lists - LeetCode #21."""

from __future__ import annotations
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted list.

    Args:
        list1: Head of first sorted linked list.
        list2: Head of second sorted linked list.

    Returns:
        Head of the merged sorted linked list.
    """
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
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

class TestMergeTwoLists(unittest.TestCase):
    def check(self, l1: list[int], l2: list[int], expected: list[int]):
        result = merge_two_lists(from_list(l1), from_list(l2))
        self.assertEqual(to_list(result), expected)

    def test_example1(self):
        self.check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_empty(self):
        self.check([], [], [])

    def test_one_empty(self):
        self.check([], [0], [0])
        self.check([1], [], [1])

    def test_single_elements(self):
        self.check([1], [2], [1, 2])
        self.check([2], [1], [1, 2])

    def test_duplicates(self):
        self.check([1, 1, 1], [1, 1], [1, 1, 1, 1, 1])

    def test_one_list_entirely_smaller(self):
        self.check([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])

    def test_interleaved(self):
        self.check([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])

    def test_negative_values(self):
        self.check([-3, -1, 2], [-2, 0, 3], [-3, -2, -1, 0, 2, 3])


if __name__ == "__main__":
    unittest.main()
