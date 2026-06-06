"""Tests for LeetCode 989: Add to Array-Form of Integer."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestAddToArrayForm(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.addToArrayForm([1, 2, 0, 0], 34), [1, 2, 3, 4])

    def test_example2(self):
        self.assertEqual(self.s.addToArrayForm([2, 7, 4], 181), [4, 5, 5])

    def test_example3(self):
        self.assertEqual(self.s.addToArrayForm([2, 1, 5], 806), [1, 0, 2, 1])

    # --- Edge cases ---
    def test_single_digit_no_carry(self):
        self.assertEqual(self.s.addToArrayForm([5], 3), [8])

    def test_single_digit_with_carry(self):
        self.assertEqual(self.s.addToArrayForm([9], 1), [1, 0])

    def test_all_nines_carry(self):
        self.assertEqual(self.s.addToArrayForm([9, 9, 9], 1), [1, 0, 0, 0])

    def test_zero_array(self):
        self.assertEqual(self.s.addToArrayForm([0], 100), [1, 0, 0])

    def test_k_much_larger_than_num(self):
        self.assertEqual(self.s.addToArrayForm([1], 9999), [1, 0, 0, 0, 0])

    def test_k_is_one(self):
        self.assertEqual(self.s.addToArrayForm([1, 2, 3], 1), [1, 2, 4])

    def test_no_carry_needed(self):
        self.assertEqual(self.s.addToArrayForm([1, 0, 0, 0], 1), [1, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
