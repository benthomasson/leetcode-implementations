# Plan (Iteration 1)

Task: Solve the LeetCode problem "power-of-four":

Given an integer `n`, return _`true` if it is a power of four. Otherwise, return `false`_.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4x`.

**Example 1:**

**Input:** n = 16
**Output:** true

**Example 2:**

**Input:** n = 5
**Output:** false

**Example 3:**

**Input:** n = 1
**Output:** true

**Constraints:**

*   `-231 <= n <= 231 - 1`

**Follow up:** Could you solve it without loops/recursion?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: isPowerOfFour

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The bit manipulation approach is the optimal O(1) solution — three simple checks, no loops or recursion needed.

[Committed changes to planner branch]