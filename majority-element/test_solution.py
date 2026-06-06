import unittest
from solution import majority_element


class TestMajorityElement(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(majority_element([3, 2, 3]), 3)

    def test_example2(self):
        self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_single_element(self):
        self.assertEqual(majority_element([1]), 1)

    def test_two_identical_elements(self):
        self.assertEqual(majority_element([5, 5]), 5)

    def test_all_same_elements(self):
        self.assertEqual(majority_element([7, 7, 7, 7, 7]), 7)

    def test_majority_at_end(self):
        self.assertEqual(majority_element([1, 2, 3, 2, 2]), 2)

    def test_majority_at_start(self):
        self.assertEqual(majority_element([2, 2, 2, 1, 3]), 2)

    def test_negative_numbers(self):
        self.assertEqual(majority_element([-1, -1, -1, 2, 2]), -1)

    def test_zero_as_majority(self):
        self.assertEqual(majority_element([0, 0, 1, 0, 2]), 0)

    def test_alternating_with_majority(self):
        self.assertEqual(majority_element([1, 2, 1, 2, 1, 2, 1]), 1)

    def test_large_input(self):
        nums = [1] * 5000 + [2] * 4999
        self.assertEqual(majority_element(nums), 1)

    def test_minimal_majority(self):
        self.assertEqual(majority_element([1, 2, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(majority_element([1000000000, 1000000000, -1000000000]), 1000000000)


if __name__ == "__main__":
    unittest.main()
