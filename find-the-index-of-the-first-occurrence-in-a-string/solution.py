class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return index of first occurrence of needle in haystack, or -1.

        Args:
            haystack: String to search in.
            needle: String to search for.

        Returns:
            Index of first occurrence, or -1 if not found.
        """
        n, m = len(haystack), len(needle)

        # Build KMP failure function
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        # Search
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            elif j:
                j = lps[j - 1]
            else:
                i += 1

        return -1
