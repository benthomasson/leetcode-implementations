"""Most Frequent Even Element - LeetCode Solution."""

from collections import Counter


def most_frequent_even(nums: list[int]) -> int:
    """Return the most frequent even element, smallest if tied, or -1 if none.

    Args:
        nums: List of non-negative integers.

    Returns:
        The most frequent even element, or -1 if no even elements exist.
    """
    counts = Counter(x for x in nums if x % 2 == 0)
    if not counts:
        return -1
    return min(counts, key=lambda x: (-counts[x], x))


# --- Tests ---
import unittest


class TestMostFrequentEven(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(most_frequent_even([0, 1, 2, 2, 4, 4, 1]), 2)

    def test_example2(self):
        self.assertEqual(most_frequent_even([4, 4, 4, 9, 2, 4]), 4)

    def test_example3(self):
        self.assertEqual(most_frequent_even([29, 47, 21, 41, 13, 37, 25, 7]), -1)

    def test_single_even(self):
        self.assertEqual(most_frequent_even([2]), 2)

    def test_single_odd(self):
        self.assertEqual(most_frequent_even([3]), -1)

    def test_zero(self):
        self.assertEqual(most_frequent_even([0]), 0)

    def test_all_same_even(self):
        self.assertEqual(most_frequent_even([6, 6, 6]), 6)

    def test_tie_returns_smallest(self):
        self.assertEqual(most_frequent_even([4, 2, 4, 2]), 2)

    def test_multiple_ties(self):
        self.assertEqual(most_frequent_even([8, 6, 4, 2, 8, 6, 4, 2]), 2)


if __name__ == "__main__":
    unittest.main()
