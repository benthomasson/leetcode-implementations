"""LeetCode 541: Reverse String II."""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """Reverse first k chars for every 2k chars in s.

        Args:
            s: Input string of lowercase English letters.
            k: Number of characters to reverse per 2k window.

        Returns:
            String with every 2k-window's first k characters reversed.
        """
        chars = list(s)
        for i in range(0, len(chars), 2 * k):
            chars[i:i + k] = chars[i:i + k][::-1]
        return "".join(chars)
