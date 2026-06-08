"""LeetCode: Reformat Phone Number."""


class Solution:
    def reformatNumber(self, number: str) -> str:
        """Reformat phone number into groups of 3 or 2 digits joined by dashes.

        Args:
            number: Phone number string with digits, spaces, and dashes.

        Returns:
            Reformatted phone number string.
        """
        digits = ''.join(c for c in number if c.isdigit())
        blocks = []
        i = 0
        while len(digits) - i > 4:
            blocks.append(digits[i:i+3])
            i += 3
        remaining = len(digits) - i
        if remaining <= 3:
            blocks.append(digits[i:])
        else:  # remaining == 4
            blocks.append(digits[i:i+2])
            blocks.append(digits[i+2:i+4])
        return '-'.join(blocks)


reformat_number = Solution().reformatNumber
