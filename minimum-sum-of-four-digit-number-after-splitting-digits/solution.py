"""Minimum Sum of Four Digit Number After Splitting Digits."""

import unittest


def min_operations(num: int) -> int:
    """Return the minimum sum from splitting a 4-digit number into two integers.

    Args:
        num: A positive integer with exactly four digits (1000-9999).

    Returns:
        The minimum possible sum of two integers formed from num's digits.
    """
    digits = sorted(int(d) for d in str(num))
    return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])


class TestMinOperations(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_operations(2932), 52)

    def test_example2(self):
        self.assertEqual(min_operations(4009), 13)

    def test_all_same(self):
        self.assertEqual(min_operations(1111), 22)

    def test_min_input(self):
        self.assertEqual(min_operations(1000), 1)

    def test_max_input(self):
        self.assertEqual(min_operations(9999), 198)

    def test_sequential(self):
        self.assertEqual(min_operations(1234), 37)


if __name__ == "__main__":
    unittest.main()
