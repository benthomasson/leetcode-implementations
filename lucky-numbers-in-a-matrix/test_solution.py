"""Tests for Lucky Numbers in a Matrix."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import dfs


class TestLuckyNumbers(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(dfs([[3, 7, 8], [9, 11, 13], [15, 16, 17]]), [15])

    def test_example2(self):
        self.assertEqual(dfs([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]), [12])

    def test_example3(self):
        self.assertEqual(dfs([[7, 8], [1, 2]]), [7])

    # Edge cases
    def test_single_element(self):
        self.assertEqual(dfs([[5]]), [5])

    def test_single_row(self):
        self.assertEqual(dfs([[3, 1, 2]]), [1])

    def test_single_column(self):
        self.assertEqual(dfs([[3], [1], [2]]), [3])

    def test_lucky_bottom_left(self):
        self.assertEqual(dfs([[1, 2], [3, 4]]), [3])

    def test_no_lucky_number(self):
        # Row 0 min=1 col0, col0 max=3 -> skip
        # Row 1 min=2 col0, col0 max=3 -> skip  (wait, min of [2,3] is 2)
        # Actually [[3,4],[1,2]]: row0 min=3 col0, col0 vals 3,1 max=3 -> lucky!
        # Use [[2,1],[3,4]]: row0 min=1 col1, col1 vals 1,4 max=4 -> skip
        #                    row1 min=3 col0, col0 vals 2,3 max=3 -> lucky!
        # Hard to avoid with distinct 2x2. Use 3x3:
        # [[3,1,5],[9,2,6],[7,8,4]]:
        #   row0 min=1 col1, col1=[1,2,8] max=8 -> skip
        #   row1 min=2 col1, col1 max=8 -> skip
        #   row2 min=4 col2, col2=[5,6,4] max=6 -> skip
        self.assertEqual(dfs([[3, 1, 5], [9, 2, 6], [7, 8, 4]]), [])

    def test_large_values(self):
        self.assertEqual(dfs([[100000, 99999], [1, 2]]), [99999])


if __name__ == "__main__":
    unittest.main()
