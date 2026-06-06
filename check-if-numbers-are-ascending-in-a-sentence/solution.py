"""Check if Numbers Are Ascending in a Sentence."""

import unittest


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        """Check if all numbers in the sentence are strictly increasing left to right."""
        prev = -1
        for token in s.split():
            if token.isdigit():
                num = int(token)
                if num <= prev:
                    return False
                prev = num
        return True


class TestAreNumbersAscending(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

    def test_example2(self):
        self.assertFalse(self.sol.areNumbersAscending("hello world 5 x 5"))

    def test_example3(self):
        self.assertFalse(self.sol.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

    def test_two_ascending(self):
        self.assertTrue(self.sol.areNumbersAscending("a 1 b 2"))

    def test_two_descending(self):
        self.assertFalse(self.sol.areNumbersAscending("a 2 b 1"))

    def test_all_numbers_ascending(self):
        self.assertTrue(self.sol.areNumbersAscending("1 2 3 4 5"))

    def test_boundary_values(self):
        self.assertTrue(self.sol.areNumbersAscending("i have 1 dog and 99 cats"))

    def test_adjacent_numbers_not_ascending(self):
        self.assertFalse(self.sol.areNumbersAscending("10 9 are numbers"))


if __name__ == "__main__":
    unittest.main()
