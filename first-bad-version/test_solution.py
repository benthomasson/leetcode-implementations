"""Tests for First Bad Version solution."""

import unittest
from solution import first_bad_version


class TestFirstBadVersion(unittest.TestCase):

    def _make_api(self, bad: int):
        return lambda version: version >= bad

    def test_example1(self):
        self.assertEqual(first_bad_version(5, self._make_api(4)), 4)

    def test_example2(self):
        self.assertEqual(first_bad_version(1, self._make_api(1)), 1)

    def test_first_version_bad(self):
        self.assertEqual(first_bad_version(100, self._make_api(1)), 1)

    def test_last_version_bad(self):
        self.assertEqual(first_bad_version(100, self._make_api(100)), 100)

    def test_mid_range(self):
        self.assertEqual(first_bad_version(10, self._make_api(5)), 5)

    def test_large_n(self):
        n = 2**31 - 1
        bad = 2**30
        self.assertEqual(first_bad_version(n, self._make_api(bad)), bad)

    def test_two_versions_first_bad(self):
        self.assertEqual(first_bad_version(2, self._make_api(1)), 1)

    def test_two_versions_second_bad(self):
        self.assertEqual(first_bad_version(2, self._make_api(2)), 2)


if __name__ == "__main__":
    unittest.main()
