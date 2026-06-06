"""Check If N and Its Double Exist - LeetCode 1346."""

import unittest


def checkIfExist(arr: list[int]) -> bool:
    """Check if any element in arr has its double also in arr.

    Args:
        arr: List of integers.

    Returns:
        True if arr[i] == 2 * arr[j] for some i != j.
    """
    seen = set()
    for x in arr:
        if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
            return True
        seen.add(x)
    return False


class TestCheckIfExist(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(checkIfExist([10, 2, 5, 3]))

    def test_basic_false(self):
        self.assertFalse(checkIfExist([3, 1, 7, 11]))

    def test_two_zeros(self):
        self.assertTrue(checkIfExist([0, 0]))

    def test_single_zero(self):
        self.assertFalse(checkIfExist([0, 1, 2]))

    def test_negative_numbers(self):
        self.assertTrue(checkIfExist([-2, -4]))

    def test_negative_no_match(self):
        self.assertFalse(checkIfExist([-3, -7]))

    def test_min_length(self):
        self.assertFalse(checkIfExist([1, 3]))

    def test_double_at_end(self):
        self.assertTrue(checkIfExist([1, 3, 4, 2]))


if __name__ == "__main__":
    unittest.main()
