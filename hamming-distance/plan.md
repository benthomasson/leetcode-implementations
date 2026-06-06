# Plan (Iteration 1)

Task: Solve the LeetCode problem "hamming-distance":

The [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return _the **Hamming distance** between them_.

**Example 1:**

**Input:** x = 1, y = 4
**Output:** 2
**Explanation:**
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

**Example 2:**

**Input:** x = 3, y = 1
**Output:** 1

**Constraints:**

*   `0 <= x, y <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: hammingDistance

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. XOR + popcount — simple and optimal.

[Committed changes to planner branch]