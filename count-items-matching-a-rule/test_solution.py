import unittest
from solution import Solution


class TestCountMatches(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_color(self):
        items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
        self.assertEqual(self.s.countMatches(items, "color", "silver"), 1)

    def test_example2_type(self):
        items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
        self.assertEqual(self.s.countMatches(items, "type", "phone"), 2)

    def test_name_key(self):
        items = [["phone", "blue", "pixel"], ["computer", "silver", "pixel"]]
        self.assertEqual(self.s.countMatches(items, "name", "pixel"), 2)

    def test_single_item_match(self):
        self.assertEqual(self.s.countMatches([["a", "b", "c"]], "type", "a"), 1)

    def test_no_match(self):
        items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"]]
        self.assertEqual(self.s.countMatches(items, "color", "red"), 0)

    def test_all_match(self):
        items = [["phone", "blue", "x"], ["phone", "red", "y"], ["phone", "green", "z"]]
        self.assertEqual(self.s.countMatches(items, "type", "phone"), 3)


if __name__ == "__main__":
    unittest.main()
