"""Delete N Nodes After M Nodes of a Linked List."""
from __future__ import annotations
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def deleteNodes(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    """Delete n nodes after every m kept nodes in a linked list (in-place).

    Args:
        head: Head of the linked list.
        m: Number of nodes to keep each cycle.
        n: Number of nodes to delete each cycle.

    Returns:
        Head of the modified list.
    """
    current = head
    while current:
        # Keep m nodes
        for _ in range(m - 1):
            if not current:
                return head
            current = current.next

        if not current:
            return head

        # Skip n nodes
        skip = current.next
        for _ in range(n):
            if not skip:
                break
            skip = skip.next

        # Connect kept tail to node after skipped section
        current.next = skip
        current = skip

    return head


# --- Helpers ---

def list_to_linked(vals: list[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def linked_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --- Tests ---

class TestDeleteNodes(unittest.TestCase):
    def check(self, vals, m, n, expected):
        head = list_to_linked(vals)
        result = deleteNodes(head, m, n)
        self.assertEqual(linked_to_list(result), expected)

    def test_example1(self):
        self.check([1,2,3,4,5,6,7,8,9,10,11,12,13], 2, 3, [1,2,6,7,11,12])

    def test_example2(self):
        self.check([1,2,3,4,5,6,7,8,9,10,11], 1, 3, [1,5,9])

    def test_single_node(self):
        self.check([1], 1, 1, [1])

    def test_m_larger_than_list(self):
        self.check([1,2,3], 5, 2, [1,2,3])

    def test_n_larger_than_remaining(self):
        self.check([1,2,3,4,5], 2, 10, [1,2])

    def test_alternating(self):
        self.check([1,2,3,4,5,6], 1, 1, [1,3,5])

    def test_keep_all(self):
        self.check([1,2,3], 3, 1, [1,2,3])

    def test_delete_all_but_first(self):
        self.check([1,2,3,4,5], 1, 100, [1])


if __name__ == "__main__":
    unittest.main()
