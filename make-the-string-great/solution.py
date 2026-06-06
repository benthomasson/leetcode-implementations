class Solution:
    def goodNodes(self, s: str) -> str:
        """Remove adjacent chars that are same letter but different case.

        Args:
            s: String of lower and upper case English letters.

        Returns:
            The string after removing all bad adjacent pairs.
        """
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
