# Plan (Iteration 1)

Task: Solve the LeetCode problem "backspace-string-compare":

Given two strings `s` and `t`, return `true` _if they are equal when both are typed into empty text editors_. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s =  "ab#c ", t =  "ad#c "
**Output:** true
**Explanation:** Both s and t become  "ac ".

**Example 2:**

**Input:** s =  "ab## ", t =  "c#d# "
**Output:** true
**Explanation:** Both s and t become  " ".

**Example 3:**

**Input:** s =  "a#c ", t =  "b "
**Output:** false
**Explanation:** s becomes  "c " while t becomes  "b ".

**Constraints:**

*   `1 <= s.length, t.length <= 200`
*   `s` and `t` only contain lowercase letters and `'#'` characters.

**Follow up:** Can you solve it in `O(n)` time and `O(1)` space?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: backspaceCompare

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `/workspaces/backspace-string-compare/planner/PLAN.md`. 

**Summary:** Two-pointer reverse traversal with skip counters — O(n) time, O(1) space. Straightforward problem with a well-known optimal solution.

[Committed changes to planner branch]