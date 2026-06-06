"""Tests for Student Attendance Record I."""

import unittest
from solution import Solution


class TestCheckRecord(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # LeetCode examples
    def test_example1(self):
        self.assertTrue(self.sol.checkRecord("PPALLP"))

    def test_example2(self):
        self.assertFalse(self.sol.checkRecord("PPALLL"))

    # Absence boundary
    def test_zero_absences(self):
        self.assertTrue(self.sol.checkRecord("PPLLPP"))

    def test_one_absence(self):
        self.assertTrue(self.sol.checkRecord("A"))

    def test_two_absences(self):
        self.assertFalse(self.sol.checkRecord("AA"))

    def test_two_absences_separated(self):
        self.assertFalse(self.sol.checkRecord("APLA"))

    # Consecutive late boundary
    def test_two_consecutive_lates(self):
        self.assertTrue(self.sol.checkRecord("PLLP"))

    def test_three_consecutive_lates(self):
        self.assertFalse(self.sol.checkRecord("PLLLP"))

    def test_four_consecutive_lates(self):
        self.assertFalse(self.sol.checkRecord("PLLLLP"))

    # Single characters
    def test_single_p(self):
        self.assertTrue(self.sol.checkRecord("P"))

    def test_single_l(self):
        self.assertTrue(self.sol.checkRecord("L"))

    # All same character
    def test_all_present(self):
        self.assertTrue(self.sol.checkRecord("PPPPPP"))

    def test_all_late(self):
        self.assertFalse(self.sol.checkRecord("LLL"))

    def test_all_absent(self):
        self.assertFalse(self.sol.checkRecord("AAA"))

    # Mixed patterns
    def test_lates_broken_by_absent(self):
        self.assertTrue(self.sol.checkRecord("LLALL"))

    def test_lates_broken_by_present(self):
        self.assertTrue(self.sol.checkRecord("LLPLL"))


if __name__ == "__main__":
    unittest.main()
