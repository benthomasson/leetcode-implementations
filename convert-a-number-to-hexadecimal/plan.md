# Plan (Iteration 1)

Task: Solve the LeetCode problem "convert-a-number-to-hexadecimal":

Given an integer `num`, return _a string representing its hexadecimal representation_. For negative integers, [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement) method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

**Note:** You are not allowed to use any built-in library method to directly solve this problem.

**Example 1:**

**Input:** num = 26
**Output:** "1a"

**Example 2:**

**Input:** num = -1
**Output:** "ffffffff"

**Constraints:**

*   `-231 <= num <= 231 - 1`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: to_hex

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is simple bit manipulation — mask to 32-bit unsigned, extract 4 bits per iteration, map to hex chars. O(1) time (at most 8 iterations) and O(1) space.

[Committed changes to planner branch]