"""Largest Number After Digit Swaps by Parity."""

import unittest


class Solution:
    def largestInteger(self, num: int) -> int:
        """Return largest number achievable by swapping same-parity digits.

        Args:
            num: Positive integer to maximize.

        Returns:
            Largest possible value after same-parity swaps.
        """
        digits = [int(d) for d in str(num)]
        odds = sorted([d for d in digits if d % 2 == 1], reverse=True)
        evens = sorted([d for d in digits if d % 2 == 0], reverse=True)
        oi = ei = 0
        result = []
        for d in digits:
            if d % 2 == 1:
                result.append(odds[oi])
                oi += 1
            else:
                result.append(evens[ei])
                ei += 1
        return int("".join(map(str, result)))


class TestLargestInteger(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.largestInteger(1234), 3412)

    def test_example2(self):
        self.assertEqual(self.s.largestInteger(65875), 87655)

    def test_single_digit(self):
        self.assertEqual(self.s.largestInteger(5), 5)

    def test_all_even(self):
        self.assertEqual(self.s.largestInteger(2468), 8642)

    def test_all_odd(self):
        self.assertEqual(self.s.largestInteger(1357), 7531)

    def test_one(self):
        self.assertEqual(self.s.largestInteger(1), 1)

    def test_repeated_digits(self):
        self.assertEqual(self.s.largestInteger(11223), 31221)

    def test_large(self):
        self.assertEqual(self.s.largestInteger(1000000000), 1000000000)


if __name__ == "__main__":
    unittest.main()
