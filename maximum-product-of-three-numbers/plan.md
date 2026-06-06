# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-product-of-three-numbers":

Given an integer array `nums`, _find three numbers whose product is maximum and return the maximum product_.

**Example 1:**

**Input:** nums = \[1,2,3\]
**Output:** 6

**Example 2:**

**Input:** nums = \[1,2,3,4\]
**Output:** 24

**Example 3:**

**Input:** nums = \[-1,-2,-3\]
**Output:** -6

**Constraints:**

*   `3 <= nums.length <= 104`
*   `-1000 <= nums[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maximumProduct

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The key insight is handling negative numbers — two large negatives multiplied together produce a positive that, combined with the largest positive, can beat three positives. Sort and check both candidates.

[Committed changes to planner branch]