"""Similar RGB Color - LeetCode solution."""


class Solution:
    def similarRGB(self, color: str) -> str:
        """Find the shorthand RGB color most similar to the given color.

        Args:
            color: A 7-character hex color string like "#09f166".

        Returns:
            The most similar color representable in shorthand (#XYZ) format.
        """
        def closest(comp: str) -> str:
            val = int(comp, 16)
            nearest = round(val / 17) * 17
            return f"{nearest:02x}"

        return "#" + closest(color[1:3]) + closest(color[3:5]) + closest(color[5:7])


# --- Tests ---
import unittest


class TestSimilarRGB(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.similarRGB("#09f166"), "#11ee66")

    def test_example2(self):
        self.assertEqual(self.s.similarRGB("#4e3fe1"), "#5544dd")

    def test_black(self):
        self.assertEqual(self.s.similarRGB("#000000"), "#000000")

    def test_white(self):
        self.assertEqual(self.s.similarRGB("#ffffff"), "#ffffff")

    def test_shorthand_already(self):
        # Already a shorthand color (each pair is a multiple of 17)
        self.assertEqual(self.s.similarRGB("#aabbcc"), "#aabbcc")

    def test_midpoint_rounds_up(self):
        # 0x08 = 8, 8/17 = 0.47 -> rounds to 0 -> 0x00
        # 0x09 = 9, 9/17 = 0.53 -> rounds to 1 -> 0x11
        self.assertEqual(self.s.similarRGB("#090909"), "#111111")
        self.assertEqual(self.s.similarRGB("#080808"), "#000000")

    def test_upper_boundary(self):
        # 0xf8 = 248, 248/17 = 14.59 -> rounds to 15 -> 0xff
        self.assertEqual(self.s.similarRGB("#f8f8f8"), "#ffffff")


if __name__ == "__main__":
    unittest.main()
