"""LeetCode 415: Add Strings."""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """Add two non-negative integers represented as strings.

        Args:
            num1: First number as a string.
            num2: Second number as a string.

        Returns:
            Sum of num1 and num2 as a string.
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - 48 if i >= 0 else 0
            d2 = ord(num2[j]) - 48 if j >= 0 else 0
            total = d1 + d2 + carry
            carry, digit = divmod(total, 10)
            result.append(chr(digit + 48))
            i -= 1
            j -= 1

        return ''.join(reversed(result))
