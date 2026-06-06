# Plan (Iteration 1)

Task: Solve the LeetCode problem "valid-parentheses":

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

**Input:** s =  "() "
**Output:** true

**Example 2:**

**Input:** s =  "()\[\]{} "
**Output:** true

**Example 3:**

**Input:** s =  "(\] "
**Output:** false

**Constraints:**

*   `1 <= s.length <= 104`
*   `s` consists of parentheses only `'()[]{}'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_valid

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Stack-based solution — straightforward and optimal for this problem.

[Committed changes to planner branch]