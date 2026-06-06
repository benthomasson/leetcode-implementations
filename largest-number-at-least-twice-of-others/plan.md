# Plan (Iteration 1)

Task: Solve the LeetCode problem "largest-number-at-least-twice-of-others":

You are given an integer array `nums` where the largest integer is **unique**.

Determine whether the largest element in the array is **at least twice** as much as every other number in the array. If it is, return _the **index** of the largest element, or return_ `-1` _otherwise_.

**Example 1:**

**Input:** nums = \[3,6,1,0\]
**Output:** 1
**Explanation:** 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

**Example 2:**

**Input:** nums = \[1,2,3,4\]
**Output:** -1
**Explanation:** 4 is less than twice the value of 3, so we return -1.

**Constraints:**

*   `2 <= nums.length <= 50`
*   `0 <= nums[i] <= 100`
*   The largest element in `nums` is unique.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: minCostClimbingStairs

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is a single-pass O(n) solution tracking the max, second-max, and max-index — simple and optimal for this problem.

[Committed changes to planner branch]