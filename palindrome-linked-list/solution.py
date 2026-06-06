"""Palindrome Linked List - LeetCode Solution."""
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Check if a singly linked list is a palindrome. O(n) time, O(1) space."""
        if not head or not head.next:
            return True

        # Find middle (slow ends at start of second half)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev, curr = None, slow.next
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Compare first half with reversed second half
        p1, p2 = head, prev
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


# --- Tests ---
import unittest


def make_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_even_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1, 2, 2, 1])))

    def test_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome(make_list([1, 2])))

    def test_single_node(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1])))

    def test_two_same(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1, 1])))

    def test_odd_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1, 2, 1])))

    def test_non_palindrome_three(self):
        self.assertFalse(self.sol.isPalindrome(make_list([1, 2, 3])))

    def test_all_same(self):
        self.assertTrue(self.sol.isPalindrome(make_list([5, 5, 5, 5, 5])))

    def test_boundary_values(self):
        self.assertTrue(self.sol.isPalindrome(make_list([9, 0, 9])))


if __name__ == "__main__":
    unittest.main()
