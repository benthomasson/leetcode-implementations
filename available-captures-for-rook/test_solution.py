import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


def make_board(placements, rook_pos):
    """Build 8x8 board with rook and given placements."""
    board = [["." for _ in range(8)] for _ in range(8)]
    r, c = rook_pos
    board[r][c] = "R"
    for (pr, pc), ch in placements:
        board[pr][pc] = ch
    return board


class TestRookCaptures(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        board = make_board([((1, 3), "p"), ((2, 7), "p"), ((5, 3), "p")], (2, 3))
        self.assertEqual(self.sol.regionsBySlashes(board), 3)

    def test_example2_bishops_block_all(self):
        board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "B", "R", "B", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        self.assertEqual(self.sol.regionsBySlashes(board), 0)

    def test_example3(self):
        board = make_board(
            [
                ((1, 3), "p"), ((2, 3), "p"),
                ((3, 0), "p"), ((3, 1), "p"), ((3, 5), "p"), ((3, 6), "B"),
                ((5, 3), "B"), ((6, 3), "p"),
            ],
            (3, 3),
        )
        self.assertEqual(self.sol.regionsBySlashes(board), 3)

    def test_rook_corner_no_pawns(self):
        board = make_board([], (0, 0))
        self.assertEqual(self.sol.regionsBySlashes(board), 0)

    def test_rook_corner_with_pawns(self):
        board = make_board([((0, 7), "p"), ((7, 0), "p")], (0, 0))
        self.assertEqual(self.sol.regionsBySlashes(board), 2)

    def test_rook_center_four_pawns(self):
        board = make_board(
            [((0, 4), "p"), ((7, 4), "p"), ((4, 0), "p"), ((4, 7), "p")],
            (4, 4),
        )
        self.assertEqual(self.sol.regionsBySlashes(board), 4)

    def test_pawn_adjacent_all_sides(self):
        board = make_board(
            [((2, 3), "p"), ((4, 3), "p"), ((3, 2), "p"), ((3, 4), "p")],
            (3, 3),
        )
        self.assertEqual(self.sol.regionsBySlashes(board), 4)

    def test_bishop_blocks_before_pawn(self):
        board = make_board([((2, 3), "B"), ((1, 3), "p")], (3, 3))
        self.assertEqual(self.sol.regionsBySlashes(board), 0)

    def test_only_rook(self):
        board = make_board([], (4, 4))
        self.assertEqual(self.sol.regionsBySlashes(board), 0)


if __name__ == "__main__":
    unittest.main()
