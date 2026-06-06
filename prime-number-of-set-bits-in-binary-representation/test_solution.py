"""Tests for Prime Number of Set Bits in Binary Representation."""
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import is_prime, countPrimeSetBits


class TestIsPrime(unittest.TestCase):
    def test_primes_in_range(self):
        for p in [2, 3, 5, 7, 11, 13, 17, 19]:
            self.assertTrue(is_prime(p))

    def test_non_primes_in_range(self):
        for n in [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]:
            self.assertFalse(is_prime(n))


class TestCountPrimeSetBits(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(countPrimeSetBits(6, 10), 4)

    def test_example2(self):
        self.assertEqual(countPrimeSetBits(10, 15), 5)

    def test_single_prime_bits(self):
        # 7 = 111 -> 3 set bits (prime)
        self.assertEqual(countPrimeSetBits(7, 7), 1)

    def test_single_non_prime_bits(self):
        # 1 = 1 -> 1 set bit (not prime)
        self.assertEqual(countPrimeSetBits(1, 1), 0)

    def test_boundary_small_range(self):
        # 1->1bit, 2->1bit, 3->2bits(prime)
        self.assertEqual(countPrimeSetBits(1, 3), 1)

    def test_power_of_two(self):
        # 8 = 1000 -> 1 set bit (not prime)
        self.assertEqual(countPrimeSetBits(8, 8), 0)

    def test_all_bits_set_not_prime(self):
        # 15 = 1111 -> 4 set bits (not prime)
        self.assertEqual(countPrimeSetBits(15, 15), 0)

    def test_large_boundary(self):
        # 999999 and 1000000 - verify no crash and correct count
        # 999999 = 0xF423F = 11110100001000111111 -> 12 set bits (not prime)
        # 1000000 = 0xF4240 = 11110100001001000000 -> 7 set bits (prime)
        self.assertEqual(countPrimeSetBits(999999, 1000000), 1)


if __name__ == "__main__":
    unittest.main()
