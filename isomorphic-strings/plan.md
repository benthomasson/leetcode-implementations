# Plan (Iteration 1)

Task: Solve the LeetCode problem "isomorphic-strings":

Given two strings `s` and `t`, _determine if they are isomorphic_.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"
**Output:** true

**Example 2:**

**Input:** s = "foo", t = "bar"
**Output:** false

**Example 3:**

**Input:** s = "paper", t = "title"
**Output:** true

**Constraints:**

*   `1 <= s.length <= 5 * 104`
*   `t.length == s.length`
*   `s` and `t` consist of any valid ascii character.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_isomorphic

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is that you need **bidirectional** mapping — checking only `s→t` would incorrectly accept cases like `"ab"→"aa"` where two different source characters map to the same target.

[Committed changes to planner branch]