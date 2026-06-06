"""Tests for max_number_after_remove_digit."""

import unittest
from solution import max_number_after_remove_digit


class TestMaxNumberAfterRemoveDigit(unittest.TestCase):

    def test_example1_single_occurrence(self):
        self.assertEqual(max_number_after_remove_digit("123", "3"), "12")

    def test_example2_remove_first_is_better(self):
        self.assertEqual(max_number_after_remove_digit("1231", "1"), "231")

    def test_example3_tie(self):
        self.assertEqual(max_number_after_remove_digit("551", "5"), "51")

    def test_digit_at_end(self):
        self.assertEqual(max_number_after_remove_digit("52", "2"), "5")

    def test_digit_at_start(self):
        self.assertEqual(max_number_after_remove_digit("19", "1"), "9")

    def test_two_chars_same(self):
        self.assertEqual(max_number_after_remove_digit("33", "3"), "3")

    def test_all_identical(self):
        self.assertEqual(max_number_after_remove_digit("5555", "5"), "555")

    def test_remove_last_occurrence(self):
        # digit followed by smaller or equal chars -> remove last
        self.assertEqual(max_number_after_remove_digit("921", "2"), "91")

    def test_multiple_remove_first_wins(self):
        # "2493" remove first 2 -> "493", next char 4 > 2
        self.assertEqual(max_number_after_remove_digit("2493", "2"), "493")

    def test_remove_last_when_no_larger_follows(self):
        # "9521" remove 5 -> "921" (5 followed by 2 which is smaller, so remove last occurrence)
        self.assertEqual(max_number_after_remove_digit("9521", "5"), "921")


if __name__ == "__main__":
    unittest.main()
