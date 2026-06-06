"""Latest Time by Replacing Hidden Digits."""

import unittest


class Solution:
    def maximumTime(self, time: str) -> str:
        """Return the latest valid time by replacing '?' digits.

        Args:
            time: A string in "hh:mm" format where '?' represents hidden digits.

        Returns:
            The latest valid time as a string in "hh:mm" format.
        """
        t = list(time)

        if t[0] == '?':
            t[0] = '2' if t[1] in '?0123' else '1'
        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'

        return ''.join(t)


class TestMaximumTime(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maximumTime("2?:?0"), "23:50")

    def test_example2(self):
        self.assertEqual(self.s.maximumTime("0?:3?"), "09:39")

    def test_example3(self):
        self.assertEqual(self.s.maximumTime("1?:22"), "19:22")

    def test_all_hidden(self):
        self.assertEqual(self.s.maximumTime("??:??"), "23:59")

    def test_no_hidden(self):
        self.assertEqual(self.s.maximumTime("12:34"), "12:34")

    def test_h1_constrained_by_h2(self):
        self.assertEqual(self.s.maximumTime("?4:00"), "14:00")

    def test_h1_unconstrained(self):
        self.assertEqual(self.s.maximumTime("?3:00"), "23:00")

    def test_h2_when_h1_is_2(self):
        self.assertEqual(self.s.maximumTime("2?:00"), "23:00")

    def test_h2_when_h1_is_0(self):
        self.assertEqual(self.s.maximumTime("0?:00"), "09:00")

    def test_only_minutes_hidden(self):
        self.assertEqual(self.s.maximumTime("00:??"), "00:59")

    def test_m1_only(self):
        self.assertEqual(self.s.maximumTime("00:?0"), "00:50")

    def test_m2_only(self):
        self.assertEqual(self.s.maximumTime("00:0?"), "00:09")


if __name__ == "__main__":
    unittest.main()
