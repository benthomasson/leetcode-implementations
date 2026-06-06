"""Convert Binary Number in a Linked List to Integer."""
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def min_operations(head: Optional[ListNode]) -> int:
    """Convert a binary linked list to its decimal value.

    Args:
        head: Head node of a singly-linked list with 0/1 values (MSB first).

    Returns:
        The decimal integer represented by the binary linked list.
    """
    result = 0
    node = head
    while node:
        result = result * 2 + node.val
        node = node.next
    return result


def _make_list(values: list[int]) -> Optional[ListNode]:
    """Helper to build a linked list from a list of ints."""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


class TestMinOperations(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_operations(_make_list([1, 0, 1])), 5)

    def test_example2(self):
        self.assertEqual(min_operations(_make_list([0])), 0)

    def test_single_one(self):
        self.assertEqual(min_operations(_make_list([1])), 1)

    def test_all_zeros(self):
        self.assertEqual(min_operations(_make_list([0, 0, 0, 0])), 0)

    def test_1100(self):
        self.assertEqual(min_operations(_make_list([1, 1, 0, 0])), 12)

    def test_30_ones(self):
        self.assertEqual(min_operations(_make_list([1] * 30)), 2**30 - 1)

    def test_leading_zeros(self):
        self.assertEqual(min_operations(_make_list([0, 0, 1, 0])), 2)


if __name__ == "__main__":
    unittest.main()
