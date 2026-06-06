# Plan (Iteration 1)

Task: Solve the LeetCode problem "monotonic-array":

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` _if the given array is monotonic, or_ `false` _otherwise_.

**Example 1:**

**Input:** nums = \[1,2,2,3\]
**Output:** true

**Example 2:**

**Input:** nums = \[6,5,4,4\]
**Output:** true

**Example 3:**

**Input:** nums = \[1,3,2\]
**Output:** false

**Constraints:**

*   `1 <= nums.length <= 105`
*   `-105 <= nums[i] <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maxDepth

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple problem with a clear optimal approach — single pass with two boolean flags, O(n) time, O(1) space. The only notable issue is that `TASK.md` specifies `maxDepth` as the function name, which is a copy-paste error from a different problem; I've flagged it for the implementer.

[Committed changes to planner branch]