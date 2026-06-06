"""Tests for Middle of the Linked List."""
import unittest
from solution import ListNode, middle_of_the_linked_list


def build_list(vals: list[int]) -> ListNode | None:
    """Build a linked list from a list of values."""
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def list_to_vals(node: ListNode | None) -> list[int]:
    """Collect remaining values from node onward."""
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals


class TestMiddleOfLinkedList(unittest.TestCase):
    def test_odd_length(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(list_to_vals(middle_of_the_linked_list(head)), [3, 4, 5])

    def test_even_length(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(list_to_vals(middle_of_the_linked_list(head)), [4, 5, 6])

    def test_single_node(self):
        head = build_list([1])
        self.assertEqual(list_to_vals(middle_of_the_linked_list(head)), [1])

    def test_two_nodes(self):
        head = build_list([1, 2])
        self.assertEqual(list_to_vals(middle_of_the_linked_list(head)), [2])

    def test_three_nodes(self):
        head = build_list([1, 2, 3])
        self.assertEqual(list_to_vals(middle_of_the_linked_list(head)), [2, 3])

    def test_100_nodes(self):
        head = build_list(list(range(1, 101)))
        result = middle_of_the_linked_list(head)
        self.assertEqual(result.val, 51)


if __name__ == "__main__":
    unittest.main()
