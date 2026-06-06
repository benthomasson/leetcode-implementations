# Plan (Iteration 1)

Task: Solve the LeetCode problem "second-largest-digit-in-a-string":

Given an alphanumeric string `s`, return _the **second largest** numerical digit that appears in_ `s`_, or_ `-1` _if it does not exist_.

An **alphanumeric** string is a string consisting of lowercase English letters and digits.

**Example 1:**

**Input:** s =  "dfa12321afd "
**Output:** 2
**Explanation:** The digits that appear in s are \[1, 2, 3\]. The second largest digit is 2.

**Example 2:**

**Input:** s =  "abc1111 "
**Output:** -1
**Explanation:** The digits that appear in s are \[1\]. There is no second largest digit. 

**Constraints:**

*   `1 <= s.length <= 500`
*   `s` consists of only lowercase English letters and/or digits.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: second_highest

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple single-pass set-based approach — O(n) time, O(1) space.

[Committed changes to planner branch]