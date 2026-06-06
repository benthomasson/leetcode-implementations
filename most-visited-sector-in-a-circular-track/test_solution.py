import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import busy_student
import unittest


class TestBusyStudent(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(busy_student(4, [1, 3, 1, 2]), [1, 2])

    def test_example2(self):
        self.assertEqual(busy_student(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]), [2])

    def test_example3(self):
        self.assertEqual(busy_student(7, [1, 3, 5, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_single_round_no_wrap(self):
        self.assertEqual(busy_student(5, [2, 4]), [2, 3, 4])

    def test_single_round_wrap(self):
        self.assertEqual(busy_student(4, [3, 1]), [1, 3, 4])

    def test_start_equals_end(self):
        # start == end means single sector visited most
        self.assertEqual(busy_student(5, [3, 5, 3]), [3])

    def test_n2_no_wrap(self):
        self.assertEqual(busy_student(2, [1, 2]), [1, 2])

    def test_n2_wrap(self):
        self.assertEqual(busy_student(2, [2, 1]), [1, 2])

    def test_full_circle_back_to_start(self):
        # Ends where it started after full laps
        self.assertEqual(busy_student(3, [1, 3, 1]), [1])


if __name__ == '__main__':
    unittest.main()
