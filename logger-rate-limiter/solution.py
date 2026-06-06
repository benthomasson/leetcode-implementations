"""Logger Rate Limiter - LeetCode 359."""


class Logger:
    """Rate-limiting logger that prints each unique message at most every 10 seconds."""

    def __init__(self) -> None:
        self.next_allowed: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """Returns True if the message should be printed at the given timestamp.

        Args:
            timestamp: Current timestamp (non-decreasing order guaranteed).
            message: The message string.

        Returns:
            True if the message should be printed, False otherwise.
        """
        if timestamp >= self.next_allowed.get(message, 0):
            self.next_allowed[message] = timestamp + 10
            return True
        return False
