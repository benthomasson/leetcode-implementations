"""Remove All Adjacent Duplicates in String."""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """Remove all adjacent duplicate characters repeatedly.

        Args:
            s: String of lowercase English letters.

        Returns:
            String after all adjacent duplicate removals.
        """
        stack: list[str] = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
