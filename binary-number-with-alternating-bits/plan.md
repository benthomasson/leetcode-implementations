# Plan (Iteration 1)

Task: Solve the LeetCode problem "binary-number-with-alternating-bits":

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

**Example 1:**

**Input:** n = 5
**Output:** true
**Explanation:** The binary representation of 5 is: 101

**Example 2:**

**Input:** n = 7
**Output:** false
**Explanation:** The binary representation of 7 is: 111.

**Example 3:**

**Input:** n = 11
**Output:** false
**Explanation:** The binary representation of 11 is: 1011.

**Constraints:**

*   `1 <= n <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: has_alternating_bits

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The XOR trick (`n ^ (n >> 1)` yields all 1s for alternating-bit numbers) gives an optimal O(1) solution. The implementer should create the solution and tests as outlined.

[Committed changes to planner branch]