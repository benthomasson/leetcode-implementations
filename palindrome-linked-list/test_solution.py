"""Tests for Palindrome Linked List solution."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution, ListNode, make_list


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Problem examples ---
    def test_example1_even_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1, 2, 2, 1])))

    def test_example2_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome(make_list([1, 2])))

    # --- Edge cases ---
    def test_single_node(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1])))

    def test_two_same(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1, 1])))

    def test_two_different(self):
        self.assertFalse(self.sol.isPalindrome(make_list([0, 9])))

    def test_odd_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(make_list([1, 2, 1])))

    def test_odd_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome(make_list([1, 2, 3])))

    def test_all_same_values(self):
        self.assertTrue(self.sol.isPalindrome(make_list([5, 5, 5, 5, 5])))

    def test_boundary_values_0_and_9(self):
        self.assertTrue(self.sol.isPalindrome(make_list([9, 0, 9])))

    def test_longer_non_palindrome(self):
        self.assertFalse(self.sol.isPalindrome(make_list([1, 2, 3, 4, 5])))


if __name__ == "__main__":
    unittest.main()
