"""Tests for Prime Arrangements solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import numPrimeArrangements


class TestPrimeArrangements(unittest.TestCase):
    """Test numPrimeArrangements across edge cases and examples."""

    # LeetCode examples
    def test_example1_n5(self):
        self.assertEqual(numPrimeArrangements(5), 12)

    def test_example2_n100(self):
        self.assertEqual(numPrimeArrangements(100), 682289015)

    # Edge cases
    def test_n1_no_primes(self):
        self.assertEqual(numPrimeArrangements(1), 1)

    def test_n2_one_prime(self):
        self.assertEqual(numPrimeArrangements(2), 1)

    def test_n3(self):
        self.assertEqual(numPrimeArrangements(3), 2)

    # Mid-range
    def test_n10(self):
        self.assertEqual(numPrimeArrangements(10), 17280)

    # Boundary around prime transitions
    def test_n4(self):
        # primes in [1..4]: 2,3 → 2 primes, 2 non-primes → 2!*2! = 4
        self.assertEqual(numPrimeArrangements(4), 4)

    def test_n6(self):
        # primes: 2,3,5 → 3 primes, 3 non-primes → 3!*3! = 36
        self.assertEqual(numPrimeArrangements(6), 36)

    # Return type check
    def test_returns_int(self):
        self.assertIsInstance(numPrimeArrangements(50), int)


if __name__ == "__main__":
    unittest.main()
