"""Tests for generateTheString."""

import unittest
from collections import Counter
from solution import Solution


class TestGenerateTheString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _validate(self, n: int) -> None:
        result = self.sol.generateTheString(n)
        self.assertEqual(len(result), n)
        self.assertTrue(result.islower())
        for count in Counter(result).values():
            self.assertEqual(count % 2, 1, f"Even count found in '{result}'")

    def test_odd_n(self):
        self._validate(1)
        self._validate(3)
        self._validate(7)

    def test_even_n(self):
        self._validate(2)
        self._validate(4)
        self._validate(6)

    def test_large(self):
        self._validate(500)
        self._validate(499)

    def test_n_1(self):
        self.assertEqual(len(self.sol.generateTheString(1)), 1)


if __name__ == "__main__":
    unittest.main()
