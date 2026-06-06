import unittest
from solution import searchInsert


class TestSearchInsert(unittest.TestCase):
    def test_found_middle(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)

    def test_insert_between(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)

    def test_insert_after_all(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)

    def test_insert_before_all(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 0), 0)

    def test_found_first(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 1), 0)

    def test_found_last(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 6), 3)

    def test_single_element_found(self):
        self.assertEqual(searchInsert([5], 5), 0)

    def test_single_element_insert_before(self):
        self.assertEqual(searchInsert([5], 3), 0)

    def test_single_element_insert_after(self):
        self.assertEqual(searchInsert([5], 7), 1)

    def test_insert_between_middle(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 4), 2)


if __name__ == "__main__":
    unittest.main()
