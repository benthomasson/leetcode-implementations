"""Tests for Pascal's Triangle solution."""

import unittest
from solution import generate


class TestGenerate(unittest.TestCase):

    def test_single_row(self):
        self.assertEqual(generate(1), [[1]])

    def test_two_rows(self):
        self.assertEqual(generate(2), [[1], [1, 1]])

    def test_five_rows(self):
        self.assertEqual(
            generate(5),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )

    def test_rows_start_and_end_with_one(self):
        result = generate(10)
        for row in result:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

    def test_inner_elements_are_sum_of_above(self):
        result = generate(6)
        for i in range(2, len(result)):
            for j in range(1, len(result[i]) - 1):
                self.assertEqual(result[i][j], result[i - 1][j - 1] + result[i - 1][j])

    def test_max_constraint(self):
        result = generate(30)
        self.assertEqual(len(result), 30)
        self.assertEqual(len(result[29]), 30)


if __name__ == "__main__":
    unittest.main()
