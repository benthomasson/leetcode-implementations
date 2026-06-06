"""Majority Element — Boyer-Moore Voting Algorithm."""


def majority_element(nums: list[int]) -> int:
    """Return the majority element (appears more than n/2 times).

    Args:
        nums: Non-empty list where one element has a strict majority.

    Returns:
        The majority element.
    """
    candidate = 0
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


import unittest


class TestMajorityElement(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(majority_element([3, 2, 3]), 3)

    def test_example2(self):
        self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_single(self):
        self.assertEqual(majority_element([1]), 1)

    def test_two_same(self):
        self.assertEqual(majority_element([5, 5]), 5)

    def test_all_same(self):
        self.assertEqual(majority_element([7, 7, 7, 7]), 7)

    def test_majority_at_end(self):
        self.assertEqual(majority_element([1, 2, 2]), 2)

    def test_majority_at_start(self):
        self.assertEqual(majority_element([2, 2, 1]), 2)

    def test_negative_numbers(self):
        self.assertEqual(majority_element([-1, -1, 3]), -1)

    def test_large_majority(self):
        self.assertEqual(majority_element([1, 1, 1, 1, 2, 3]), 1)


if __name__ == "__main__":
    unittest.main()
