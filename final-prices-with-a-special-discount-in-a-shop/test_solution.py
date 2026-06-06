import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestFinalPrices(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- provided examples ---
    def test_example1(self):
        self.assertEqual(self.s.finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])

    def test_example2_increasing(self):
        self.assertEqual(self.s.finalPrices([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_example3(self):
        self.assertEqual(self.s.finalPrices([10, 1, 1, 6]), [9, 0, 1, 6])

    # --- edge cases ---
    def test_single_element(self):
        self.assertEqual(self.s.finalPrices([5]), [5])

    def test_all_equal(self):
        self.assertEqual(self.s.finalPrices([3, 3, 3]), [0, 0, 3])

    def test_decreasing(self):
        self.assertEqual(self.s.finalPrices([5, 4, 3, 2, 1]), [1, 1, 1, 1, 1])

    def test_two_with_discount(self):
        self.assertEqual(self.s.finalPrices([5, 3]), [2, 3])

    def test_two_without_discount(self):
        self.assertEqual(self.s.finalPrices([3, 5]), [3, 5])

    def test_discount_zero(self):
        """Same price adjacent -> discount to 0."""
        self.assertEqual(self.s.finalPrices([4, 4]), [0, 4])

    def test_large_uniform(self):
        """All 500 elements equal -> all but last become 0."""
        prices = [1000] * 500
        expected = [0] * 499 + [1000]
        self.assertEqual(self.s.finalPrices(prices), expected)


if __name__ == "__main__":
    unittest.main()
