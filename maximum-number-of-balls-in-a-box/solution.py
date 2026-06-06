"""Maximum Number of Balls in a Box - LeetCode 1742."""

from collections import Counter
import unittest


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """Return the max number of balls in any box, where each ball goes in the box matching its digit sum.

        Args:
            lowLimit: Lowest ball number.
            highLimit: Highest ball number.

        Returns:
            Count of balls in the most populated box.
        """
        counts = Counter(sum(int(d) for d in str(i)) for i in range(lowLimit, highLimit + 1))
        return max(counts.values())

    # Alias required by task spec (mismatched name from a different problem).
    maxWidthOfVerticalArea = countBalls


class TestCountBalls(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countBalls(1, 10), 2)

    def test_example2(self):
        self.assertEqual(self.s.countBalls(5, 15), 2)

    def test_example3(self):
        self.assertEqual(self.s.countBalls(19, 28), 2)

    def test_single_ball(self):
        self.assertEqual(self.s.countBalls(7, 7), 1)

    def test_full_range(self):
        result = self.s.countBalls(1, 100000)
        self.assertGreater(result, 0)

    def test_alias(self):
        self.assertEqual(self.s.maxWidthOfVerticalArea(1, 10), 2)


if __name__ == "__main__":
    unittest.main()
