"""Minimum Cuts to Divide a Circle."""

import unittest


def min_cuts(n: int) -> int:
    """Return the minimum number of cuts to divide a circle into n equal slices.

    Args:
        n: Number of equal slices desired (1 <= n <= 100).

    Returns:
        Minimum number of cuts needed.
    """
    if n == 1:
        return 0
    if n % 2 == 0:
        return n // 2
    return n


class TestMinCuts(unittest.TestCase):
    def test_one(self):
        self.assertEqual(min_cuts(1), 0)

    def test_even_4(self):
        self.assertEqual(min_cuts(4), 2)

    def test_even_2(self):
        self.assertEqual(min_cuts(2), 1)

    def test_even_6(self):
        self.assertEqual(min_cuts(6), 3)

    def test_even_100(self):
        self.assertEqual(min_cuts(100), 50)

    def test_odd_3(self):
        self.assertEqual(min_cuts(3), 3)

    def test_odd_5(self):
        self.assertEqual(min_cuts(5), 5)

    def test_odd_99(self):
        self.assertEqual(min_cuts(99), 99)


if __name__ == "__main__":
    unittest.main()
