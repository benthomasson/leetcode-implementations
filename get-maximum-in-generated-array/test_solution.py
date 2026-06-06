"""Tests for Get Maximum in Generated Array."""
import unittest
from solution import Solution


class TestGetMaximumGenerated(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_n_zero(self):
        self.assertEqual(self.s.getMaximumGenerated(0), 0)

    def test_n_one(self):
        self.assertEqual(self.s.getMaximumGenerated(1), 1)

    def test_n_two(self):
        self.assertEqual(self.s.getMaximumGenerated(2), 1)

    def test_n_three(self):
        self.assertEqual(self.s.getMaximumGenerated(3), 2)

    def test_n_seven(self):
        self.assertEqual(self.s.getMaximumGenerated(7), 3)

    def test_n_100(self):
        # Smoke test for upper constraint bound
        result = self.s.getMaximumGenerated(100)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()
