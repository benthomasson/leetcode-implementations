import unittest
from solution import count_stars_except_between_pair


class TestCountStars(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(count_stars_except_between_pair("l|*e*et|c**o|*de|"), 2)

    def test_example2(self):
        self.assertEqual(count_stars_except_between_pair("iamprogrammer"), 0)

    def test_example3(self):
        self.assertEqual(count_stars_except_between_pair("yo|uar|e**|b|e***au|tifu|l"), 5)

    def test_no_bars(self):
        self.assertEqual(count_stars_except_between_pair("a*b*c*"), 3)

    def test_no_asterisks(self):
        self.assertEqual(count_stars_except_between_pair("ab|cd|ef"), 0)

    def test_consecutive_bars(self):
        self.assertEqual(count_stars_except_between_pair("*||*"), 2)

    def test_all_inside(self):
        self.assertEqual(count_stars_except_between_pair("|***|"), 0)

    def test_single_char(self):
        self.assertEqual(count_stars_except_between_pair("*"), 1)
        self.assertEqual(count_stars_except_between_pair("a"), 0)


if __name__ == "__main__":
    unittest.main()
