# Plan (Iteration 1)

Task: Solve the LeetCode problem "reverse-string-ii":

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.

If there are fewer than `k` characters left, reverse all of them. If there are less than `2k` but greater than or equal to `k` characters, then reverse the first `k` characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2
**Output:** "bacdfeg"

**Example 2:**

**Input:** s = "abcd", k = 2
**Output:** "bacd"

**Constraints:**

*   `1 <= s.length <= 104`
*   `s` consists of only lowercase English letters.
*   `1 <= k <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: reverseStr

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward problem — one clean approach, high confidence.

[Committed changes to planner branch]