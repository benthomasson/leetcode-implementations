"""Form Smallest Number From Two Digit Arrays."""

import unittest


def smallest_number_with_at_least_one_digit_from_each_array(
    nums1: list[int], nums2: list[int]
) -> int:
    """Return the smallest number containing at least one digit from each array.

    Args:
        nums1: Array of unique digits (1-9).
        nums2: Array of unique digits (1-9).

    Returns:
        The smallest number with at least one digit from each array.
    """
    common = set(nums1) & set(nums2)
    if common:
        return min(common)
    a, b = min(nums1), min(nums2)
    return min(a, b) * 10 + max(a, b)


class TestSmallestNumber(unittest.TestCase):
    def test_no_common_digit(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array([4, 1, 3], [5, 7]),
            15,
        )

    def test_common_digit(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array(
                [3, 5, 2, 6], [3, 1, 7]
            ),
            3,
        )

    def test_single_element_common(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array([5], [5]), 5
        )

    def test_single_elements_no_common(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array([9], [1]), 19
        )

    def test_ordering_smaller_in_second(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array([5, 8], [3, 7]), 35
        )

    def test_multiple_common_returns_smallest(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array(
                [7, 3, 5], [5, 3, 9]
            ),
            3,
        )

    def test_all_shared(self):
        self.assertEqual(
            smallest_number_with_at_least_one_digit_from_each_array(
                [1, 2, 3], [3, 2, 1]
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()
