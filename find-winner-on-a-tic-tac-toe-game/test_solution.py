"""Tests for tic-tac-toe winner determination."""

import unittest
from solution import validateBinaryTreeNodes


class TestTicTacToe(unittest.TestCase):
    def test_a_wins_diagonal(self):
        moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
        self.assertEqual(validateBinaryTreeNodes(moves), "A ")

    def test_b_wins_column(self):
        moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
        self.assertEqual(validateBinaryTreeNodes(moves), "B ")

    def test_draw(self):
        moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
        self.assertEqual(validateBinaryTreeNodes(moves), "Draw ")

    def test_pending_single_move(self):
        self.assertEqual(validateBinaryTreeNodes([[0, 0]]), "Pending ")

    def test_pending_few_moves(self):
        moves = [[0, 0], [1, 1]]
        self.assertEqual(validateBinaryTreeNodes(moves), "Pending ")

    def test_a_wins_row(self):
        moves = [[0, 0], [1, 0], [0, 1], [1, 1], [0, 2]]
        self.assertEqual(validateBinaryTreeNodes(moves), "A ")

    def test_a_wins_column(self):
        moves = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
        self.assertEqual(validateBinaryTreeNodes(moves), "A ")

    def test_b_wins_anti_diagonal(self):
        moves = [[0, 0], [0, 2], [0, 1], [1, 1], [1, 0], [2, 0]]
        self.assertEqual(validateBinaryTreeNodes(moves), "B ")


if __name__ == "__main__":
    unittest.main()
