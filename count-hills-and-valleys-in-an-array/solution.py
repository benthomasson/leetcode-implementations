"""Count Hills and Valleys in an Array."""

from typing import List


def count_hills_and_valleys(nums: List[int]) -> int:
    """Count the number of hills and valleys in nums.

    Args:
        nums: 0-indexed integer array.

    Returns:
        Number of distinct hills and valleys.
    """
    # Remove consecutive duplicates
    deduped = [nums[0]]
    for v in nums[1:]:
        if v != deduped[-1]:
            deduped.append(v)

    count = 0
    for i in range(1, len(deduped) - 1):
        if deduped[i] > deduped[i - 1] and deduped[i] > deduped[i + 1]:
            count += 1  # hill
        elif deduped[i] < deduped[i - 1] and deduped[i] < deduped[i + 1]:
            count += 1  # valley
    return count


# --- Tests ---
import unittest


class TestCountHillsAndValleys(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(count_hills_and_valleys([2, 4, 1, 1, 6, 5]), 3)

    def test_example2(self):
        self.assertEqual(count_hills_and_valleys([6, 6, 5, 5, 4, 1]), 0)

    def test_all_same(self):
        self.assertEqual(count_hills_and_valleys([5, 5, 5]), 0)

    def test_alternating(self):
        self.assertEqual(count_hills_and_valleys([1, 3, 1, 3, 1]), 4)

    def test_single_plateau(self):
        self.assertEqual(count_hills_and_valleys([1, 5, 5, 5, 1]), 1)

    def test_monotonic(self):
        self.assertEqual(count_hills_and_valleys([1, 2, 3, 4, 5]), 0)

    def test_hill_length3(self):
        self.assertEqual(count_hills_and_valleys([1, 3, 1]), 1)

    def test_valley_length3(self):
        self.assertEqual(count_hills_and_valleys([3, 1, 3]), 1)


if __name__ == "__main__":
    unittest.main()
