# Plan (Iteration 1)

Task: Solve the LeetCode problem "contains-duplicate-ii":

Given an integer array `nums` and an integer `k`, return `true` _if there are two **distinct indices**_ `i` _and_ `j` _in the array such that_ `nums[i] == nums[j]` _and_ `abs(i - j) <= k`.

**Example 1:**

**Input:** nums = \[1,2,3,1\], k = 3
**Output:** true

**Example 2:**

**Input:** nums = \[1,0,1,1\], k = 1
**Output:** true

**Example 3:**

**Input:** nums = \[1,2,3,1,2,3\], k = 2
**Output:** false

**Constraints:**

*   `1 <= nums.length <= 105`
*   `-109 <= nums[i] <= 109`
*   `0 <= k <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: containsNearbyDuplicate

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Hash map approach — O(n) time, O(n) space, no complexity needed.

[Committed changes to planner branch]