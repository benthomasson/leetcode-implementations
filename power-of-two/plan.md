# Plan (Iteration 1)

Task: Solve the LeetCode problem "power-of-two":

Given an integer `n`, return _`true` if it is a power of two. Otherwise, return `false`_.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

**Example 1:**

**Input:** n = 1
**Output:** true
**Explanation:** 20 = 1

**Example 2:**

**Input:** n = 16
**Output:** true
**Explanation:** 24 = 16

**Example 3:**

**Input:** n = 3
**Output:** false

**Constraints:**

*   `-231 <= n <= 231 - 1`

**Follow up:** Could you solve it without loops/recursion?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_power_of_two

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Use `n > 0 and (n & (n - 1)) == 0` — the canonical O(1) bit manipulation approach. A power of two has exactly one set bit, so ANDing with `n-1` clears it. Tests should cover powers of two, non-powers, zero, and negatives. Confidence: **HIGH**.

[Committed changes to planner branch]