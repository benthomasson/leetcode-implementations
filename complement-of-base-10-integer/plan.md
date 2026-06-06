# Plan (Iteration 1)

Task: Solve the LeetCode problem "complement-of-base-10-integer":

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

*   For example, The integer `5` is `"101 "` in binary and its **complement** is `"010 "` which is the integer `2`.

Given an integer `n`, return _its complement_.

**Example 1:**

**Input:** n = 5
**Output:** 2
**Explanation:** 5 is  "101 " in binary, with complement  "010 " in binary, which is 2 in base-10.

**Example 2:**

**Input:** n = 7
**Output:** 0
**Explanation:** 7 is  "111 " in binary, with complement  "000 " in binary, which is 0 in base-10.

**Example 3:**

**Input:** n = 10
**Output:** 5
**Explanation:** 10 is  "1010 " in binary, with complement  "0101 " in binary, which is 5 in base-10.

**Constraints:**

*   `0 <= n < 109`

**Note:** This question is the same as 476: [https://leetcode.com/problems/number-complement/](https://leetcode.com/problems/number-complement/)

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: pancakeSort

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is a one-liner bit manipulation: XOR with a mask of all 1s of the same bit length, with a special case for `n=0`.

[Committed changes to planner branch]