"""Solution for LeetCode: Largest 3-Same-Digit Number in String."""


class Solution:
    def split_and_minimize(self, num: str) -> str:
        """Find the largest 3-same-digit substring in a numeric string.

        A "good integer" is a substring of length 3 consisting of a single
        repeated digit. This function returns the largest such substring,
        or an empty string if none exists.

        Args:
            num: A string of digits with length >= 3.

        Returns:
            The maximum good integer as a string (e.g. "999", "000"),
            or "" if no good integer exists.

        Examples:
            >>> Solution().split_and_minimize("6777133339")
            '777'
            >>> Solution().split_and_minimize("2300019")
            '000'
            >>> Solution().split_and_minimize("42352338")
            ''
        """
        result = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                candidate = num[i:i + 3]
                if candidate > result:
                    result = candidate
        return result
