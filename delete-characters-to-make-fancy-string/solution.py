"""Delete Characters to Make Fancy String."""


class Solution:
    def makeFancyString(self, s: str) -> str:
        """Remove minimum characters so no three consecutive chars are equal.

        Args:
            s: Input string of lowercase English letters.

        Returns:
            The fancy string with no three consecutive equal characters.
        """
        result = []
        for c in s:
            if len(result) >= 2 and result[-1] == c and result[-2] == c:
                continue
            result.append(c)
        return "".join(result)
