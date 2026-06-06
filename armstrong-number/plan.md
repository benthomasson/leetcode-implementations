# Plan (Iteration 1)

Task: Solve the LeetCode problem "armstrong-number":

Given an integer `n`, return `true` _if and only if it is an **Armstrong number**_.

The `k`\-digit number `n` is an Armstrong number if and only if the `kth` power of each digit sums to `n`.

**Example 1:**

**Input:** n = 153
**Output:** true
**Explanation:** 153 is a 3-digit number, and 153 = 13 + 53 + 33.

**Example 2:**

**Input:** n = 123
**Output:** false
**Explanation:** 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.

**Constraints:**

*   `1 <= n <= 108`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_armstrong

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward problem — extract digits, sum each to the power of the digit count, compare to original.

[Committed changes to planner branch]