"""Tests for Rings and Rods solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestRingsAndRods(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(self.s.findFarmland("B0B6G0R6R0R6G9"), 1)

    def test_example2(self):
        self.assertEqual(self.s.findFarmland("B0R0G0R9R0B0G0"), 1)

    def test_example3(self):
        self.assertEqual(self.s.findFarmland("G4"), 0)

    # --- Edge cases ---
    def test_single_rod_all_colors(self):
        self.assertEqual(self.s.findFarmland("R0G0B0"), 1)

    def test_all_ten_rods_all_colors(self):
        rings = "".join(f"{c}{r}" for r in range(10) for c in "RGB")
        self.assertEqual(self.s.findFarmland(rings), 10)

    def test_duplicate_colors_no_match(self):
        self.assertEqual(self.s.findFarmland("R0R0R0"), 0)

    def test_two_colors_insufficient(self):
        self.assertEqual(self.s.findFarmland("R0G0"), 0)

    def test_multiple_qualifying_rods(self):
        self.assertEqual(self.s.findFarmland("R0G0B0R1G1B1"), 2)

    def test_empty_string(self):
        self.assertEqual(self.s.findFarmland(""), 0)

    def test_max_input_all_same_rod(self):
        # 100 rings all on rod 0, but only red → 0
        rings = "R0" * 100
        self.assertEqual(self.s.findFarmland(rings), 0)


if __name__ == "__main__":
    unittest.main()
