"""Tests for Pascal's Triangle II."""

import unittest
from solution import get_row


class TestGetRow(unittest.TestCase):
    def test_row_0(self):
        self.assertEqual(get_row(0), [1])

    def test_row_1(self):
        self.assertEqual(get_row(1), [1, 1])

    def test_row_3(self):
        self.assertEqual(get_row(3), [1, 3, 3, 1])

    def test_row_4(self):
        self.assertEqual(get_row(4), [1, 4, 6, 4, 1])

    def test_row_33(self):
        row = get_row(33)
        self.assertEqual(len(row), 34)
        self.assertEqual(row[0], 1)
        self.assertEqual(row[-1], 1)
        self.assertEqual(row, row[::-1])  # symmetry

    def test_symmetry(self):
        for i in range(10):
            row = get_row(i)
            self.assertEqual(row, row[::-1])


if __name__ == "__main__":
    unittest.main()
