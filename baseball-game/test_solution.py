"""Tests for Baseball Game solution."""

import unittest
from solution import calPoints


class TestCalPoints(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(calPoints(["5", "2", "C", "D", "+"]), 30)

    def test_example2(self):
        self.assertEqual(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)

    def test_example3(self):
        self.assertEqual(calPoints(["1", "C"]), 0)

    def test_examples_with_trailing_spaces(self):
        self.assertEqual(calPoints(["5 ", "2 ", "C ", "D ", "+ "]), 30)
        self.assertEqual(calPoints(["1 ", "C "]), 0)

    def test_single_score(self):
        self.assertEqual(calPoints(["10"]), 10)

    def test_negative_numbers(self):
        self.assertEqual(calPoints(["-5", "-3", "+"]), -16)

    def test_consecutive_doubles(self):
        self.assertEqual(calPoints(["5", "D", "D"]), 5 + 10 + 20)

    def test_consecutive_cancels(self):
        self.assertEqual(calPoints(["1", "2", "3", "C", "C"]), 1)

    def test_all_operations(self):
        self.assertEqual(calPoints(["3", "6", "+", "D", "C"]), 3 + 6 + 9)


if __name__ == "__main__":
    unittest.main()
