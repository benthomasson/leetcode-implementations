# Plan (Iteration 1)

Task: Solve the LeetCode problem "smallest-range-i":

You are given an integer array `nums` and an integer `k`.

In one operation, you can choose any index `i` where `0 <= i < nums.length` and change `nums[i]` to `nums[i] + x` where `x` is an integer from the range `[-k, k]`. You can apply this operation **at most once** for each index `i`.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

Return _the minimum **score** of_ `nums` _after applying the mentioned operation at most once for each index in it_.

**Example 1:**

**Input:** nums = \[1\], k = 0
**Output:** 0
**Explanation:** The score is max(nums) - min(nums) = 1 - 1 = 0.

**Example 2:**

**Input:** nums = \[0,10\], k = 2
**Output:** 6
**Explanation:** Change nums to be \[2, 8\]. The score is max(nums) - min(nums) = 8 - 2 = 6.

**Example 3:**

**Input:** nums = \[1,3,6\], k = 3
**Output:** 0
**Explanation:** Change nums to be \[4, 4, 4\]. The score is max(nums) - min(nums) = 4 - 4 = 0.

**Constraints:**

*   `1 <= nums.length <= 104`
*   `0 <= nums[i] <= 104`
*   `0 <= k <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: middleNode

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** One-liner math solution — `max(0, max(nums) - min(nums) - 2*k)`. O(n) time, O(1) space. The key insight is that we can shrink the range by at most `2*k` (raise the min by `k`, lower the max by `k`), clamped at 0.

[Committed changes to planner branch]