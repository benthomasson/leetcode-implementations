class Solution:
    def addDigits(self, num: int) -> int:
        """Return the digital root of num.

        Args:
            num: Non-negative integer.

        Returns:
            Single digit result of repeatedly summing digits.
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
