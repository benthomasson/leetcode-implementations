"""Construct the Rectangle - LeetCode"""

import math
import unittest


def constructRectangle(area: int) -> list[int]:
    """Find L, W with L*W=area, L>=W, minimizing L-W.

    Args:
        area: Target rectangular area (1 <= area <= 10^7).

    Returns:
        [L, W] where L >= W and L * W == area.
    """
    w = int(math.isqrt(area))
    while area % w != 0:
        w -= 1
    return [area // w, w]


class TestConstructRectangle(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(constructRectangle(4), [2, 2])

    def test_prime(self):
        self.assertEqual(constructRectangle(37), [37, 1])

    def test_large(self):
        self.assertEqual(constructRectangle(122122), [427, 286])

    def test_one(self):
        self.assertEqual(constructRectangle(1), [1, 1])

    def test_composite(self):
        self.assertEqual(constructRectangle(12), [4, 3])

    def test_large_perfect_square(self):
        self.assertEqual(constructRectangle(1000000), [1000, 1000])


if __name__ == "__main__":
    unittest.main()
