import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution, check_if_matrix_is_x_matrix

import unittest


class TestCheckXMatrix(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1_true(self):
        grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
        self.assertTrue(self.s.checkXMatrix(grid))

    def test_example2_false(self):
        grid = [[5,7,0],[0,3,1],[0,5,0]]
        self.assertFalse(self.s.checkXMatrix(grid))

    # --- Edge cases ---
    def test_min_3x3_valid(self):
        grid = [[1,0,1],[0,9,0],[4,0,2]]
        self.assertTrue(self.s.checkXMatrix(grid))

    def test_zero_on_main_diagonal(self):
        grid = [[0,0,1],[0,1,0],[1,0,1]]
        self.assertFalse(self.s.checkXMatrix(grid))

    def test_zero_on_anti_diagonal(self):
        grid = [[1,0,0],[0,1,0],[1,0,1]]
        self.assertFalse(self.s.checkXMatrix(grid))

    def test_nonzero_off_diagonal(self):
        grid = [[1,0,1],[0,1,0],[1,1,1]]
        self.assertFalse(self.s.checkXMatrix(grid))

    def test_5x5_valid(self):
        grid = [
            [1,0,0,0,1],
            [0,2,0,2,0],
            [0,0,3,0,0],
            [0,4,0,4,0],
            [5,0,0,0,5],
        ]
        self.assertTrue(self.s.checkXMatrix(grid))

    def test_all_nonzero_fails(self):
        grid = [[1,1,1],[1,1,1],[1,1,1]]
        self.assertFalse(self.s.checkXMatrix(grid))

    # --- Alias test ---
    def test_alias_works(self):
        grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
        self.assertTrue(check_if_matrix_is_x_matrix(grid))


if __name__ == "__main__":
    unittest.main()
