class Solution:
    def minOperations(self, num: int) -> bool:
        """Check if a number equals itself after reversing twice.

        Args:
            num: Non-negative integer to check.

        Returns:
            True if num survives double reversal, False otherwise.
        """
        return num == 0 or num % 10 != 0
