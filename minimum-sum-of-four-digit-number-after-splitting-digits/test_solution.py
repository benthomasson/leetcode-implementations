"""Tests for min_operations - Minimum Sum of Four Digit Number After Splitting Digits."""

import sys
import unittest
from itertools import permutations

sys.path.insert(0, "../implementer")
from solution import min_operations


def brute_force(num: int) -> int:
    """Brute-force reference: try all ways to split 4 digits into two numbers."""
    digits = [int(d) for d in str(num)]
    min_sum = float("inf")
    for perm in permutations(digits):
        for split in range(1, 4):  # split after position 1, 2, or 3
            n1 = int("".join(map(str, perm[:split])))
            n2 = int("".join(map(str, perm[split:])))
            min_sum = min(min_sum, n1 + n2)
    return min_sum


class TestMinOperations(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(min_operations(2932), 52)

    def test_example2(self):
        self.assertEqual(min_operations(4009), 13)

    # Edge cases
    def test_all_same_digits(self):
        self.assertEqual(min_operations(1111), 22)

    def test_min_input(self):
        self.assertEqual(min_operations(1000), 1)

    def test_max_input(self):
        self.assertEqual(min_operations(9999), 198)

    def test_sequential_digits(self):
        self.assertEqual(min_operations(1234), 37)

    def test_descending_digits(self):
        self.assertEqual(min_operations(9876), 147)  # sorted [6,7,8,9] -> 68+79=147

    def test_multiple_zeros(self):
        self.assertEqual(min_operations(2000), 2)  # sorted [0,0,0,2] -> 00+02=2

    # Brute-force validation on a sample of inputs
    def test_brute_force_sample(self):
        for num in [1000, 1234, 2932, 4009, 5555, 9999, 1001, 9100, 3070]:
            with self.subTest(num=num):
                self.assertEqual(min_operations(num), brute_force(num))


if __name__ == "__main__":
    unittest.main()
