# Plan (Iteration 1)

Task: Solve the LeetCode problem "valid-perfect-square":

Given a positive integer num, return `true` _if_ `num` _is a perfect square or_ `false` _otherwise_.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

**Example 1:**

**Input:** num = 16
**Output:** true
**Explanation:** We return true because 4 \* 4 = 16 and 4 is an integer.

**Example 2:**

**Input:** num = 14
**Output:** false
**Explanation:** We return false because 3.742 \* 3.742 = 14 and 3.742 is not an integer.

**Constraints:**

*   `1 <= num <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_perfect_square

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Binary search, straightforward — ready for implementation.

[Committed changes to planner branch]