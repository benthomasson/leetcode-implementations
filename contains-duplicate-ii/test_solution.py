import unittest
from solution import Solution


class TestContainsNearbyDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_example2(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_example3(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_single_element(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1], 0))

    def test_k_zero_no_adjacent_dup(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2], 0))

    def test_k_zero_not_possible(self):
        # k=0 means i==j which requires distinct indices, so always False
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 1], 0))

    def test_all_same(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 1, 1, 1], 1))

    def test_dup_just_outside_k(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 2))

    def test_dup_exactly_at_k(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 1], 2))

    def test_negative_numbers(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([-1, -2, -1], 2))

    def test_large_k(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 1], 100000))

    def test_no_duplicates(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 4, 5], 3))


if __name__ == "__main__":
    unittest.main()
