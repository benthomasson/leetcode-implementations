import unittest
from unittest.mock import patch
from solution import Solution


def make_guess(pick):
    """Create a guess function that returns based on the picked number."""
    def _guess(num):
        if num > pick:
            return -1
        elif num < pick:
            return 1
        return 0
    return _guess


class TestGuessNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # LeetCode examples
    @patch("solution.guess", create=True)
    def test_example1_n10_pick6(self, mock_guess):
        mock_guess.side_effect = make_guess(6)
        self.assertEqual(self.sol.guessNumber(10), 6)

    @patch("solution.guess", create=True)
    def test_example2_n1_pick1(self, mock_guess):
        mock_guess.side_effect = make_guess(1)
        self.assertEqual(self.sol.guessNumber(1), 1)

    @patch("solution.guess", create=True)
    def test_example3_n2_pick1(self, mock_guess):
        mock_guess.side_effect = make_guess(1)
        self.assertEqual(self.sol.guessNumber(2), 1)

    # Edge cases
    @patch("solution.guess", create=True)
    def test_pick_equals_n(self, mock_guess):
        mock_guess.side_effect = make_guess(10)
        self.assertEqual(self.sol.guessNumber(10), 10)

    @patch("solution.guess", create=True)
    def test_pick_at_midpoint(self, mock_guess):
        mock_guess.side_effect = make_guess(5)
        self.assertEqual(self.sol.guessNumber(9), 5)

    @patch("solution.guess", create=True)
    def test_n2_pick2(self, mock_guess):
        mock_guess.side_effect = make_guess(2)
        self.assertEqual(self.sol.guessNumber(2), 2)

    # Large n
    @patch("solution.guess", create=True)
    def test_large_n_pick_middle(self, mock_guess):
        mock_guess.side_effect = make_guess(1_500_000_000)
        self.assertEqual(self.sol.guessNumber(2**31 - 1), 1_500_000_000)

    @patch("solution.guess", create=True)
    def test_large_n_pick_one(self, mock_guess):
        mock_guess.side_effect = make_guess(1)
        self.assertEqual(self.sol.guessNumber(2**31 - 1), 1)

    @patch("solution.guess", create=True)
    def test_large_n_pick_max(self, mock_guess):
        n = 2**31 - 1
        mock_guess.side_effect = make_guess(n)
        self.assertEqual(self.sol.guessNumber(n), n)


if __name__ == "__main__":
    unittest.main()
