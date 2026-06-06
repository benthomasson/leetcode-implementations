# Plan (Iteration 1)

Task: Solve the LeetCode problem "move-zeroes":

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example 1:**

**Input:** nums = \[0,1,0,3,12\]
**Output:** \[1,3,12,0,0\]

**Example 2:**

**Input:** nums = \[0\]
**Output:** \[0\]

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-231 <= nums[i] <= 231 - 1`

**Follow up:** Could you minimize the total number of operations done?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: moveZeroes

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `/workspaces/move-zeroes/planner/PLAN.md`. 

**Summary:** Use the two-pointer swap approach — one pointer tracks the insert position for non-zeros, the other scans the array. Swap non-zeros into place, leaving zeros at the end. O(n) time, O(1) space. Tests should cover edge cases (single element, all zeros, no zeros, boundary values).

[Committed changes to planner branch]