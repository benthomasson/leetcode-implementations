"""Minimum Number of Moves to Seat Everyone."""


def min_moves_to_seat(seats: list[int], students: list[int]) -> int:
    """Return minimum moves to seat all students.

    Args:
        seats: Positions of seats.
        students: Positions of students.

    Returns:
        Minimum total moves to assign each student to a unique seat.
    """
    return sum(abs(a - b) for a, b in zip(sorted(seats), sorted(students)))


import unittest


class TestMinMovesToSeat(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_moves_to_seat([3, 1, 5], [2, 7, 4]), 4)

    def test_example2(self):
        self.assertEqual(min_moves_to_seat([4, 1, 5, 9], [1, 3, 2, 6]), 7)

    def test_example3(self):
        self.assertEqual(min_moves_to_seat([2, 2, 6, 6], [1, 3, 2, 6]), 4)

    def test_single_element(self):
        self.assertEqual(min_moves_to_seat([5], [3]), 2)

    def test_already_matched(self):
        self.assertEqual(min_moves_to_seat([1, 2, 3], [1, 2, 3]), 0)

    def test_all_same_position(self):
        self.assertEqual(min_moves_to_seat([5, 5, 5], [5, 5, 5]), 0)

    def test_duplicates(self):
        self.assertEqual(min_moves_to_seat([1, 1], [2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
