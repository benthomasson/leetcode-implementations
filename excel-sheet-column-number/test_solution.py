import unittest
from solution import title_to_number


class TestTitleToNumber(unittest.TestCase):

    def test_single_letters(self):
        self.assertEqual(title_to_number("A"), 1)
        self.assertEqual(title_to_number("B"), 2)
        self.assertEqual(title_to_number("Z"), 26)

    def test_two_letters(self):
        self.assertEqual(title_to_number("AA"), 27)
        self.assertEqual(title_to_number("AB"), 28)
        self.assertEqual(title_to_number("AZ"), 52)
        self.assertEqual(title_to_number("ZY"), 701)

    def test_max_value(self):
        self.assertEqual(title_to_number("FXSHRXW"), 2147483647)


if __name__ == "__main__":
    unittest.main()
