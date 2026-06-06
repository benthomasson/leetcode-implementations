from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """Count items matching a rule based on type, color, or name.

        Args:
            items: List of [type, color, name] string triples.
            ruleKey: One of "type", "color", or "name".
            ruleValue: The value to match against.

        Returns:
            Number of items matching the rule.
        """
        index = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(1 for item in items if item[index] == ruleValue)
