"""Middle of the Linked List - LeetCode solution."""
from __future__ import annotations
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def is_n_straight_hand(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the middle node of a singly linked list.

    Uses slow/fast pointer technique. For even-length lists, returns the
    second middle node.

    Args:
        head: Head of the singly linked list.

    Returns:
        The middle node of the linked list.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
