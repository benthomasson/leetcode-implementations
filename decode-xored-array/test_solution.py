"""Tests for Decode XORed Array solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestDecodeXoredArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.minOperations([1, 2, 3], 1), [1, 0, 2, 1])

    def test_example2(self):
        self.assertEqual(self.s.minOperations([6, 2, 7, 3], 4), [4, 2, 0, 7, 4])

    # --- Edge cases ---
    def test_single_encoded_element(self):
        self.assertEqual(self.s.minOperations([5], 3), [3, 6])

    def test_all_zeros(self):
        self.assertEqual(self.s.minOperations([0, 0, 0], 0), [0, 0, 0, 0])

    def test_first_zero(self):
        self.assertEqual(self.s.minOperations([7], 0), [0, 7])

    def test_large_values(self):
        self.assertEqual(self.s.minOperations([100000], 100000), [100000, 0])

    def test_same_elements(self):
        # arr=[5,5,5] -> encoded=[0,0]
        self.assertEqual(self.s.minOperations([0, 0], 5), [5, 5, 5])

    def test_roundtrip(self):
        """Encode then decode should return original array."""
        original = [4, 2, 0, 7, 4]
        encoded = [original[i] ^ original[i + 1] for i in range(len(original) - 1)]
        self.assertEqual(self.s.minOperations(encoded, original[0]), original)


if __name__ == "__main__":
    unittest.main()
