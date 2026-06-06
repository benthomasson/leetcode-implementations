"""Tests for Logger Rate Limiter."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Logger


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def test_leetcode_example(self):
        """Exact sequence from the problem statement."""
        assert self.logger.shouldPrintMessage(1, "foo") is True
        assert self.logger.shouldPrintMessage(2, "bar") is True
        assert self.logger.shouldPrintMessage(3, "foo") is False
        assert self.logger.shouldPrintMessage(8, "bar") is False
        assert self.logger.shouldPrintMessage(10, "foo") is False
        assert self.logger.shouldPrintMessage(11, "foo") is True

    def test_timestamp_zero(self):
        """First message at timestamp 0 should print."""
        assert self.logger.shouldPrintMessage(0, "hello") is True
        assert self.logger.shouldPrintMessage(9, "hello") is False
        assert self.logger.shouldPrintMessage(10, "hello") is True

    def test_exact_boundary(self):
        """t+10 is allowed, t+9 is not."""
        self.logger.shouldPrintMessage(5, "msg")
        assert self.logger.shouldPrintMessage(14, "msg") is False
        assert self.logger.shouldPrintMessage(15, "msg") is True

    def test_same_timestamp_different_messages(self):
        """Different messages at the same timestamp all print."""
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert self.logger.shouldPrintMessage(1, "b") is True
        assert self.logger.shouldPrintMessage(1, "c") is True

    def test_same_timestamp_same_message(self):
        """Same message at the same timestamp: first prints, second doesn't."""
        assert self.logger.shouldPrintMessage(1, "dup") is True
        assert self.logger.shouldPrintMessage(1, "dup") is False

    def test_large_gap(self):
        """Message allowed after a large time gap."""
        assert self.logger.shouldPrintMessage(0, "x") is True
        assert self.logger.shouldPrintMessage(1000000, "x") is True

    def test_multiple_messages_independent(self):
        """Each message has its own independent cooldown."""
        assert self.logger.shouldPrintMessage(0, "a") is True
        assert self.logger.shouldPrintMessage(5, "b") is True
        assert self.logger.shouldPrintMessage(10, "a") is True  # a cooldown expired
        assert self.logger.shouldPrintMessage(10, "b") is False  # b still blocked until 15


if __name__ == "__main__":
    unittest.main()
