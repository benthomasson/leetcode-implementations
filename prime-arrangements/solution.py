"""LeetCode: Prime Arrangements."""

import unittest

MOD = 10**9 + 7


def numPrimeArrangements(n: int) -> int:
    """Return permutations of 1..n with primes at prime indices, mod 10^9+7.

    Args:
        n: Upper bound of the range [1, n].

    Returns:
        Number of valid permutations modulo 10^9 + 7.
    """
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    prime_count = sum(1 for k in range(1, n + 1) if is_prime(k))
    non_prime_count = n - prime_count

    result = 1
    for i in range(1, prime_count + 1):
        result = result * i % MOD
    for i in range(1, non_prime_count + 1):
        result = result * i % MOD
    return result


class TestNumPrimeArrangements(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(numPrimeArrangements(1), 1)

    def test_n2(self):
        self.assertEqual(numPrimeArrangements(2), 1)

    def test_n3(self):
        self.assertEqual(numPrimeArrangements(3), 2)

    def test_n5(self):
        self.assertEqual(numPrimeArrangements(5), 12)

    def test_n10(self):
        self.assertEqual(numPrimeArrangements(10), 17280)

    def test_n100(self):
        self.assertEqual(numPrimeArrangements(100), 682289015)


if __name__ == "__main__":
    unittest.main()
