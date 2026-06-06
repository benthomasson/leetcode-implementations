import unittest
from solution import Solution


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_example2(self):
        self.assertEqual(self.s.search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_single_element_found(self):
        self.assertEqual(self.s.search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(self.s.search([5], 3), -1)

    def test_first_element(self):
        self.assertEqual(self.s.search([1, 2, 3, 4, 5], 1), 0)

    def test_last_element(self):
        self.assertEqual(self.s.search([1, 2, 3, 4, 5], 5), 4)

    def test_two_elements(self):
        self.assertEqual(self.s.search([1, 3], 1), 0)
        self.assertEqual(self.s.search([1, 3], 3), 1)
        self.assertEqual(self.s.search([1, 3], 2), -1)

    def test_negative_numbers(self):
        self.assertEqual(self.s.search([-10, -5, -3, 0, 2], -5), 1)

    def test_target_less_than_all(self):
        self.assertEqual(self.s.search([2, 4, 6], 1), -1)

    def test_target_greater_than_all(self):
        self.assertEqual(self.s.search([2, 4, 6], 7), -1)


if __name__ == "__main__":
    unittest.main()
