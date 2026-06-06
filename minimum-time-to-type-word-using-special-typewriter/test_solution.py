import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution

import unittest


class TestMinTimeToType(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1_abc(self):
        self.assertEqual(self.s.minTimeToType("abc"), 5)

    def test_example2_bza(self):
        self.assertEqual(self.s.minTimeToType("bza"), 7)

    def test_example3_zjpc(self):
        self.assertEqual(self.s.minTimeToType("zjpc"), 34)

    # --- Edge cases ---
    def test_single_char_a(self):
        """Pointer starts on 'a', no movement needed."""
        self.assertEqual(self.s.minTimeToType("a"), 1)

    def test_single_char_z(self):
        """'z' is 1 step counterclockwise from 'a'."""
        self.assertEqual(self.s.minTimeToType("z"), 2)

    def test_single_char_n(self):
        """'n' is exactly 13 steps either direction (antipodal)."""
        self.assertEqual(self.s.minTimeToType("n"), 14)

    def test_repeated_same_char(self):
        """Repeated chars: no movement, just 1 sec each to type."""
        self.assertEqual(self.s.minTimeToType("aaa"), 3)

    def test_back_and_forth(self):
        """a->z (1 step CCW) + z->a (1 step CW) = 1+1+1+1 = 4."""
        self.assertEqual(self.s.minTimeToType("za"), 4)

    def test_full_alphabet(self):
        """a->b->...->z: 25 moves + 26 typings = 51."""
        self.assertEqual(self.s.minTimeToType("abcdefghijklmnopqrstuvwxyz"), 51)

    def test_reverse_alphabet(self):
        """a->z(1 move) then each step is 1 move: 26 moves + 26 typings = 52."""
        self.assertEqual(self.s.minTimeToType("zyxwvutsrqponmlkjihgfedcba"), 52)


if __name__ == "__main__":
    unittest.main()
