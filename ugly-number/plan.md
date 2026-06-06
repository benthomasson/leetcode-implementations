# Plan (Iteration 1)

Task: Solve the LeetCode problem "ugly-number":

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return `true` _if_ `n` _is an **ugly number**_.

**Example 1:**

**Input:** n = 6
**Output:** true
**Explanation:** 6 = 2 \* 3

**Example 2:**

**Input:** n = 1
**Output:** true
**Explanation:** 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

**Example 3:**

**Input:** n = 14
**Output:** false
**Explanation:** 14 is not ugly since it includes the prime factor 7.

**Constraints:**

*   `-231 <= n <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_ugly

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The problem is straightforward — divide out factors of 2, 3, 5 and check if 1 remains. The implementer should have everything they need.

[Committed changes to planner branch]