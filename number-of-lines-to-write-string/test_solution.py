import unittest
from solution import Solution


class TestNumberOfWays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        widths = [10] * 26
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.sol.numberOfWays(widths, s), [3, 60])

    def test_example2(self):
        widths = [4] + [10] * 25
        s = "bbbcccdddaaa"
        self.assertEqual(self.sol.numberOfWays(widths, s), [2, 4])

    def test_single_character(self):
        widths = [5] * 26
        self.assertEqual(self.sol.numberOfWays(widths, "a"), [1, 5])

    def test_exact_line_fill(self):
        """10 chars * 10px = exactly 100, should fit on one line."""
        widths = [10] * 26
        self.assertEqual(self.sol.numberOfWays(widths, "a" * 10), [1, 100])

    def test_exact_line_fill_overflow(self):
        """11 chars * 10px = 110, 11th char spills to line 2."""
        widths = [10] * 26
        self.assertEqual(self.sol.numberOfWays(widths, "a" * 11), [2, 10])

    def test_max_width_char(self):
        """Width 10 chars: 10 fit per line exactly."""
        widths = [10] * 26
        self.assertEqual(self.sol.numberOfWays(widths, "z" * 20), [2, 100])

    def test_min_width_char(self):
        """Width 2 chars: 50 fit per line exactly."""
        widths = [2] * 26
        s = "a" * 51  # 50 fill line 1 (100px), 1 on line 2 (2px)
        self.assertEqual(self.sol.numberOfWays(widths, s), [2, 2])

    def test_mixed_widths_boundary(self):
        """Mix of widths where line break happens mid-variety."""
        widths = [4] + [10] * 25  # a=4, rest=10
        # 9 b's = 90px, then a=4 → 94, then a=4 → 98, then a=4 → 102 > 100 → new line
        s = "b" * 9 + "aaa"
        self.assertEqual(self.sol.numberOfWays(widths, s), [2, 4])

    def test_max_length_exact_fill(self):
        """1000 chars at width 2 = 50/line → 20 lines, last line full."""
        widths = [2] * 26
        self.assertEqual(self.sol.numberOfWays(widths, "a" * 1000), [20, 100])


if __name__ == "__main__":
    unittest.main()
