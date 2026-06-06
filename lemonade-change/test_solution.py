import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestLemonadeChange(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertTrue(self.s.lemonadeChange([5, 5, 5, 10, 20]))

    def test_example2(self):
        self.assertFalse(self.s.lemonadeChange([5, 5, 10, 10, 20]))

    # --- Edge cases ---
    def test_single_five(self):
        self.assertTrue(self.s.lemonadeChange([5]))

    def test_single_ten_fails(self):
        self.assertFalse(self.s.lemonadeChange([10]))

    def test_single_twenty_fails(self):
        self.assertFalse(self.s.lemonadeChange([20]))

    def test_all_fives(self):
        self.assertTrue(self.s.lemonadeChange([5, 5, 5, 5]))

    # --- Greedy correctness ---
    def test_greedy_prefers_ten_plus_five(self):
        # Must use $10+$5 for first $20 to leave $5s for second $20
        self.assertTrue(self.s.lemonadeChange([5, 5, 5, 5, 5, 10, 5, 20, 20]))

    def test_just_enough_for_twenty(self):
        # [5,5,10,20]: fives=1,tens=1 after $10 → $10+$5 for $20 works
        self.assertTrue(self.s.lemonadeChange([5, 5, 10, 20]))

    def test_not_enough_fives_for_twenty(self):
        # [5,10,20]: after $10 we have fives=0,tens=1 → can't make $15
        self.assertFalse(self.s.lemonadeChange([5, 10, 20]))

    # --- Boundary ---
    def test_alternating_five_ten(self):
        self.assertTrue(self.s.lemonadeChange([5, 10, 5, 10, 5, 10]))

    def test_large_input(self):
        self.assertTrue(self.s.lemonadeChange([5] * 100000))


if __name__ == "__main__":
    unittest.main()
