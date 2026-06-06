"""Tests for giftsRemaining — Take Gifts From the Richest Pile."""

import sys
import unittest

from solution import giftsRemaining


class TestGiftsRemaining(unittest.TestCase):
    """Comprehensive tests for the giftsRemaining function."""

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(giftsRemaining([25, 64, 9, 4, 100], 4), 29)

    def test_example2(self):
        self.assertEqual(giftsRemaining([1, 1, 1, 1], 4), 4)

    # --- Edge cases ---
    def test_single_element(self):
        # 16 -> 4 -> 2
        self.assertEqual(giftsRemaining([16], 2), 2)

    def test_single_element_one_step(self):
        # 9 -> 3
        self.assertEqual(giftsRemaining([9], 1), 3)

    def test_all_ones_no_change(self):
        self.assertEqual(giftsRemaining([1, 1, 1], 10), 3)

    def test_large_value(self):
        # isqrt(1_000_000_000) = 31622
        self.assertEqual(giftsRemaining([1000000000], 1), 31622)

    def test_k_exceeds_convergence(self):
        # 100 -> 10 -> 3 -> 1 -> 1 ... converges to 1
        self.assertEqual(giftsRemaining([100], 100), 1)

    def test_multiple_max_piles(self):
        # Two piles tied at 4; one becomes isqrt(4)=2, other stays 4 => 6
        self.assertEqual(giftsRemaining([4, 4], 1), 6)

    def test_k_equals_one(self):
        # Only the max pile (100) is replaced: isqrt(100)=10, rest unchanged
        self.assertEqual(giftsRemaining([25, 64, 9, 4, 100], 1), 112)

    def test_perfect_square_chain(self):
        # 256 -> 16 -> 4 -> 2
        self.assertEqual(giftsRemaining([256], 3), 2)


if __name__ == "__main__":
    unittest.main()
