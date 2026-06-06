import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution, minimum_energy


class TestCheckBinaryString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_gap(self):
        self.assertFalse(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("1001"))

    def test_example2_contiguous(self):
        self.assertTrue(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("110"))

    def test_single_one(self):
        self.assertTrue(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("1"))

    def test_all_ones(self):
        self.assertTrue(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("1111"))

    def test_ones_then_zeros(self):
        self.assertTrue(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("100"))

    def test_multiple_segments(self):
        self.assertFalse(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("10101"))

    def test_two_segments(self):
        self.assertFalse(self.sol.checkIfBinaryStringHasAtMostOneSegmentOfOnes("101"))

    # Test standalone function
    def test_minimum_energy_true(self):
        self.assertTrue(minimum_energy("110"))

    def test_minimum_energy_false(self):
        self.assertFalse(minimum_energy("1001"))


if __name__ == "__main__":
    unittest.main()
