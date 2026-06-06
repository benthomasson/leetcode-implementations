"""LeetCode: Rings and Rods."""

import unittest
from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        """Count rods that have all three colors (red, green, blue).

        Args:
            rings: String of color-position pairs (e.g. "R3G2B1").

        Returns:
            Number of rods with all three colors.
        """
        rods: dict[str, set[str]] = defaultdict(set)
        for i in range(0, len(rings), 2):
            color, rod = rings[i], rings[i + 1]
            rods[rod].add(color)
        return sum(1 for colors in rods.values() if len(colors) == 3)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countPoints("B0B6G0R6R0R6G9"), 1)

    def test_example2(self):
        self.assertEqual(self.s.countPoints("B0R0G0R9R0B0G0"), 1)

    def test_example3(self):
        self.assertEqual(self.s.countPoints("G4"), 0)

    def test_all_rods_all_colors(self):
        rings = "".join(f"{c}{r}" for r in range(10) for c in "RGB")
        self.assertEqual(self.s.countPoints(rings), 10)

    def test_single_rod_all_colors(self):
        self.assertEqual(self.s.countPoints("R0G0B0"), 1)

    def test_duplicate_colors_same_rod(self):
        self.assertEqual(self.s.countPoints("R0R0R0"), 0)

    def test_two_colors_only(self):
        self.assertEqual(self.s.countPoints("R0G0"), 0)

    def test_multiple_rods_qualifying(self):
        self.assertEqual(self.s.countPoints("R0G0B0R1G1B1"), 2)


if __name__ == "__main__":
    unittest.main()
