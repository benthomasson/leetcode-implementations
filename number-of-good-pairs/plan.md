# Plan (Iteration 1)

Task: Solve the LeetCode problem "number-of-good-pairs":

Given an array of integers `nums`, return _the number of **good pairs**_.

A pair `(i, j)` is called _good_ if `nums[i] == nums[j]` and `i` < `j`.

**Example 1:**

**Input:** nums = \[1,2,3,1,1,3\]
**Output:** 4
**Explanation:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

**Example 2:**

**Input:** nums = \[1,1,1,1\]
**Output:** 6
**Explanation:** Each pair in the array are _good_.

**Example 3:**

**Input:** nums = \[1,2,3\]
**Output:** 0

**Constraints:**

*   `1 <= nums.length <= 100`
*   `1 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is a single-pass hash map counter — simple and optimal for this problem.

[Committed changes to planner branch]