"""Tests for Valid Perfect Square."""

import unittest
from solution import is_perfect_square


class TestIsPerfectSquare(unittest.TestCase):
    def test_perfect_squares(self):
        for n in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
            self.assertTrue(is_perfect_square(n), f"{n} should be a perfect square")

    def test_non_squares(self):
        for n in [2, 3, 5, 7, 8, 14, 15, 99]:
            self.assertFalse(is_perfect_square(n), f"{n} should not be a perfect square")

    def test_large_perfect_square(self):
        # 46340^2 = 2147395600, largest perfect square within 2^31-1
        self.assertTrue(is_perfect_square(46340 * 46340))

    def test_large_non_square(self):
        self.assertFalse(is_perfect_square(2**31 - 1))

    def test_one(self):
        self.assertTrue(is_perfect_square(1))


if __name__ == "__main__":
    unittest.main()
