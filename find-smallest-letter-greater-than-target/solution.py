"""Find Smallest Letter Greater Than Target - LeetCode 744."""

import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """Find smallest letter lexicographically greater than target.

        Args:
            letters: Sorted list of lowercase letters.
            target: Target lowercase letter.

        Returns:
            Smallest letter greater than target, or first letter if none exists.
        """
        idx = bisect_right(letters, target)
        return letters[idx % len(letters)]


class TestNextGreatestLetter(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.nextGreatestLetter(["c", "f", "j"], "a"), "c")

    def test_example2(self):
        self.assertEqual(self.s.nextGreatestLetter(["c", "f", "j"], "c"), "f")

    def test_example3(self):
        self.assertEqual(self.s.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")

    def test_target_less_than_all(self):
        self.assertEqual(self.s.nextGreatestLetter(["b", "d"], "a"), "b")

    def test_target_equals_last(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "b"], "b"), "a")

    def test_target_greater_than_all(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "b"], "z"), "a")

    def test_duplicates(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "a", "b", "b"], "a"), "b")

    def test_two_elements(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "z"], "m"), "z")

    def test_target_between_letters(self):
        self.assertEqual(self.s.nextGreatestLetter(["c", "f", "j"], "d"), "f")


if __name__ == "__main__":
    unittest.main()
