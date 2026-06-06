"""Tests for Similar RGB Color solution."""
import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


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

    def test_already_shorthand(self):
        self.assertEqual(self.s.similarRGB("#aabbcc"), "#aabbcc")

    def test_rounding_boundary(self):
        # 8/17 ≈ 0.47 rounds down, 9/17 ≈ 0.53 rounds up
        self.assertEqual(self.s.similarRGB("#080808"), "#000000")
        self.assertEqual(self.s.similarRGB("#090909"), "#111111")

    def test_upper_rounding(self):
        self.assertEqual(self.s.similarRGB("#f8f8f8"), "#ffffff")

    def test_output_is_valid_shorthand(self):
        """Every output component should be a multiple of 17 (0x00,0x11,...,0xff)."""
        for color in ["#09f166", "#4e3fe1", "#abcdef", "#123456", "#7890ab"]:
            result = self.s.similarRGB(color)
            self.assertEqual(result[0], "#")
            self.assertEqual(len(result), 7)
            for i in range(3):
                val = int(result[1 + 2 * i : 3 + 2 * i], 16)
                self.assertEqual(val % 17, 0, f"Component {i} of {result} not a multiple of 17")

    def test_result_is_closest(self):
        """Brute-force verify that the result is optimal for a few inputs."""
        shorthand_vals = [i * 17 for i in range(16)]
        for color in ["#09f166", "#4e3fe1", "#abcdef"]:
            result = self.s.similarRGB(color)
            # Compute similarity of result
            r_sim = 0
            for i in range(3):
                orig = int(color[1 + 2 * i : 3 + 2 * i], 16)
                res = int(result[1 + 2 * i : 3 + 2 * i], 16)
                r_sim -= (orig - res) ** 2
            # Check no shorthand color has higher similarity
            for r in shorthand_vals:
                for g in shorthand_vals:
                    for b in shorthand_vals:
                        orig_r = int(color[1:3], 16)
                        orig_g = int(color[3:5], 16)
                        orig_b = int(color[5:7], 16)
                        s = -((orig_r - r) ** 2 + (orig_g - g) ** 2 + (orig_b - b) ** 2)
                        self.assertGreaterEqual(r_sim, s, f"{color}: {result} not optimal vs #{r:02x}{g:02x}{b:02x}")


if __name__ == "__main__":
    unittest.main()
