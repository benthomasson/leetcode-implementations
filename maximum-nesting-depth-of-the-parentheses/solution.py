class Solution:
    def maxDepth(self, s: str) -> int:
        """Return the maximum nesting depth of parentheses in a VPS.

        Args:
            s: A valid parentheses string.

        Returns:
            The maximum nesting depth.
        """
        depth = max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif c == ')':
                depth -= 1
        return max_depth
