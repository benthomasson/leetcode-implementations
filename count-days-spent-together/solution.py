"""LeetCode: Count Days Spent Together."""

import unittest


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _date_to_day(date: str) -> int:
    """Convert "MM-DD" to day-of-year (1-indexed)."""
    month, day = int(date[:2]), int(date[3:5])
    return sum(DAYS_IN_MONTH[:month - 1]) + day


def days_together(
    arriveAlice: str, leaveAlice: str,
    arriveBob: str, leaveBob: str,
) -> int:
    """Return the number of days Alice and Bob are both in Rome.

    Args:
        arriveAlice: Alice's arrival date "MM-DD".
        leaveAlice: Alice's departure date "MM-DD".
        arriveBob: Bob's arrival date "MM-DD".
        leaveBob: Bob's departure date "MM-DD".

    Returns:
        Number of overlapping days (inclusive).
    """
    a0, a1 = _date_to_day(arriveAlice), _date_to_day(leaveAlice)
    b0, b1 = _date_to_day(arriveBob), _date_to_day(leaveBob)
    return max(0, min(a1, b1) - max(a0, b0) + 1)


class TestDaysTogether(unittest.TestCase):

    def test_example1_partial_overlap(self):
        self.assertEqual(days_together("08-15", "08-18", "08-16", "08-19"), 3)

    def test_example2_no_overlap(self):
        self.assertEqual(days_together("10-01", "10-31", "11-01", "12-31"), 0)

    def test_identical_dates(self):
        self.assertEqual(days_together("03-01", "03-10", "03-01", "03-10"), 10)

    def test_single_day_overlap(self):
        self.assertEqual(days_together("01-01", "01-05", "01-05", "01-10"), 1)

    def test_one_contained_in_other(self):
        self.assertEqual(days_together("01-01", "12-31", "06-01", "06-30"), 30)

    def test_same_day(self):
        self.assertEqual(days_together("07-04", "07-04", "07-04", "07-04"), 1)

    def test_adjacent_no_overlap(self):
        self.assertEqual(days_together("01-01", "01-31", "02-01", "02-28"), 0)

    def test_cross_month_overlap(self):
        self.assertEqual(days_together("01-28", "02-05", "02-01", "02-10"), 5)


if __name__ == "__main__":
    unittest.main()
