"""Number of Valid Clock Times."""

import unittest


def count_valid_times(time: str) -> int:
    """Count valid clock times by replacing '?' with digits 0-9.

    Args:
        time: A string of length 5 in format "hh:mm" where '?' represents unknown digits.

    Returns:
        Number of valid clock times that can be formed.
    """
    h_pattern, m_pattern = time[:2], time[3:5]

    def matches(pattern: str, value: str) -> bool:
        return all(p == '?' or p == v for p, v in zip(pattern, value))

    hours = sum(1 for h in range(24) if matches(h_pattern, f"{h:02d}"))
    minutes = sum(1 for m in range(60) if matches(m_pattern, f"{m:02d}"))
    return hours * minutes


class TestCountValidTimes(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(count_valid_times("?5:00"), 2)

    def test_example2(self):
        self.assertEqual(count_valid_times("0?:0?"), 100)

    def test_example3(self):
        self.assertEqual(count_valid_times("??:??"), 1440)

    def test_no_unknowns(self):
        self.assertEqual(count_valid_times("12:34"), 1)

    def test_hour_tens_is_2(self):
        self.assertEqual(count_valid_times("2?:00"), 4)  # 20,21,22,23

    def test_hour_ones_is_9(self):
        self.assertEqual(count_valid_times("?9:00"), 2)  # 09, 19

    def test_minute_tens_unknown(self):
        self.assertEqual(count_valid_times("00:?0"), 6)  # 00,10,20,30,40,50

    def test_minute_ones_unknown(self):
        self.assertEqual(count_valid_times("00:0?"), 10)

    def test_all_fixed_boundary(self):
        self.assertEqual(count_valid_times("23:59"), 1)

    def test_hour_unknown_tens_only(self):
        self.assertEqual(count_valid_times("?0:00"), 3)  # 00, 10, 20


if __name__ == "__main__":
    unittest.main()
