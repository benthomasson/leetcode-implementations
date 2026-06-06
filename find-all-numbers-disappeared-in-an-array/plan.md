# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-all-numbers-disappeared-in-an-array":

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return _an array of all the integers in the range_ `[1, n]` _that do not appear in_ `nums`.

**Example 1:**

**Input:** nums = \[4,3,2,7,8,2,3,1\]
**Output:** \[5,6\]

**Example 2:**

**Input:** nums = \[1,1\]
**Output:** \[2\]

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 105`
*   `1 <= nums[i] <= n`

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: find_disappeared_numbers

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is the canonical in-place negation-marking algorithm — O(n) time, O(1) space, simple to implement.

[Committed changes to planner branch]