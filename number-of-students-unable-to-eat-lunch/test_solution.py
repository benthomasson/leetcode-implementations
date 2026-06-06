import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import countStudents, min_time_to_remove_balloons
import unittest


class TestCountStudents(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(countStudents([1,1,0,0], [0,1,0,1]), 0)

    def test_example2(self):
        self.assertEqual(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]), 3)

    def test_single_student_eats(self):
        self.assertEqual(countStudents([0], [0]), 0)

    def test_single_student_cannot_eat(self):
        self.assertEqual(countStudents([0], [1]), 1)

    def test_all_same_preference_and_sandwich(self):
        self.assertEqual(countStudents([1,1,1], [1,1,1]), 0)

    def test_all_same_preference_mismatch(self):
        self.assertEqual(countStudents([0,0,0], [1,1,1]), 3)

    def test_blocked_midway(self):
        # First sandwich matches, second doesn't for remaining students
        self.assertEqual(countStudents([0,0], [0,1]), 1)

    def test_alias_works(self):
        self.assertEqual(min_time_to_remove_balloons([1,1,0,0], [0,1,0,1]), 0)

    def test_alternating(self):
        self.assertEqual(countStudents([0,1,0,1], [0,1,0,1]), 0)


if __name__ == '__main__':
    unittest.main()
