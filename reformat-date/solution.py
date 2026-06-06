"""LeetCode #1507: Reformat Date."""

import unittest


class Solution:
    def reformatDate(self, date: str) -> str:
        """Convert 'Day Month Year' to 'YYYY-MM-DD'.

        Args:
            date: Date string like "20th Oct 2052".

        Returns:
            Reformatted date string like "2052-10-20".
        """
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
        }
        day_str, month_str, year = date.split()
        day = day_str.rstrip("stndrdth")
        return f"{year}-{months[month_str]}-{day.zfill(2)}"


class TestReformatDate(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_examples(self):
        self.assertEqual(self.s.reformatDate("20th Oct 2052"), "2052-10-20")
        self.assertEqual(self.s.reformatDate("6th Jun 1933"), "1933-06-06")
        self.assertEqual(self.s.reformatDate("26th May 1960"), "1960-05-26")

    def test_ordinal_suffixes(self):
        self.assertEqual(self.s.reformatDate("1st Jan 2000"), "2000-01-01")
        self.assertEqual(self.s.reformatDate("2nd Feb 1999"), "1999-02-02")
        self.assertEqual(self.s.reformatDate("3rd Mar 2100"), "2100-03-03")
        self.assertEqual(self.s.reformatDate("4th Apr 1900"), "1900-04-04")
        self.assertEqual(self.s.reformatDate("21st Dec 2020"), "2020-12-21")
        self.assertEqual(self.s.reformatDate("22nd Nov 2020"), "2020-11-22")
        self.assertEqual(self.s.reformatDate("23rd Aug 2020"), "2020-08-23")
        self.assertEqual(self.s.reformatDate("31st Jul 2050"), "2050-07-31")

    def test_all_months(self):
        for i, m in enumerate(["Jan","Feb","Mar","Apr","May","Jun",
                                "Jul","Aug","Sep","Oct","Nov","Dec"], 1):
            result = self.s.reformatDate(f"10th {m} 2000")
            self.assertEqual(result, f"2000-{i:02d}-10")


if __name__ == "__main__":
    unittest.main()
