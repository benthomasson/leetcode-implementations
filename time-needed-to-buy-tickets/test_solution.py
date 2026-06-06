import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import time_to_buy_tickets


class TestTimeToBuyTickets(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertEqual(time_to_buy_tickets([2, 3, 2], 2), 6)

    def test_example2(self):
        self.assertEqual(time_to_buy_tickets([5, 1, 1, 1], 0), 8)

    # Edge cases
    def test_single_person(self):
        self.assertEqual(time_to_buy_tickets([1], 0), 1)

    def test_single_person_multiple_tickets(self):
        self.assertEqual(time_to_buy_tickets([100], 0), 100)

    def test_k_first_position(self):
        self.assertEqual(time_to_buy_tickets([3, 2, 1], 0), 6)

    def test_k_last_position(self):
        self.assertEqual(time_to_buy_tickets([1, 2, 3], 2), 6)

    def test_all_want_one_ticket(self):
        self.assertEqual(time_to_buy_tickets([1, 1, 1, 1], 2), 3)

    def test_k_has_smallest_value(self):
        self.assertEqual(time_to_buy_tickets([5, 1, 5], 1), 2)

    def test_all_same_values(self):
        # tickets=[3,3,3], k=1: i0=min(3,3)=3, i1=min(3,3)=3, i2=min(3,2)=2 => 8
        self.assertEqual(time_to_buy_tickets([3, 3, 3], 1), 8)

    def test_two_people(self):
        # tickets=[2,3], k=0: i0=min(2,2)=2, i1=min(3,1)=1 => 3
        self.assertEqual(time_to_buy_tickets([2, 3], 0), 3)


if __name__ == "__main__":
    unittest.main()
