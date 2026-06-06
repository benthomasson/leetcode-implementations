"""Find the Array Concatenation Value."""

import unittest


def concatenationValue(nums: list[int]) -> int:
    """Return the concatenation value of nums.

    Args:
        nums: 0-indexed integer array.

    Returns:
        The concatenation value after processing all elements.
    """
    result = 0
    l, r = 0, len(nums) - 1
    while l < r:
        result += int(str(nums[l]) + str(nums[r]))
        l += 1
        r -= 1
    if l == r:
        result += nums[l]
    return result


class TestConcatenationValue(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(concatenationValue([7, 52, 2, 4]), 596)

    def test_example2(self):
        self.assertEqual(concatenationValue([5, 14, 13, 8, 12]), 673)

    def test_single_element(self):
        self.assertEqual(concatenationValue([42]), 42)

    def test_two_elements(self):
        self.assertEqual(concatenationValue([15, 49]), 1549)

    def test_boundary_values(self):
        self.assertEqual(concatenationValue([1, 10000]), 110000)

    def test_single_digits(self):
        self.assertEqual(concatenationValue([1, 2, 3]), 15)  # 12 + 3


if __name__ == "__main__":
    unittest.main()
