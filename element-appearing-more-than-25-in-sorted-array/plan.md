# Plan (Iteration 1)

Task: Solve the LeetCode problem "element-appearing-more-than-25-in-sorted-array":

Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

**Example 1:**

**Input:** arr = \[1,2,2,6,6,6,6,7,10\]
**Output:** 6

**Example 2:**

**Input:** arr = \[1,1\]
**Output:** 1

**Constraints:**

*   `1 <= arr.length <= 104`
*   `0 <= arr[i] <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: shortest_distance

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is that in a sorted array, if an element appears more than 25% of the time, then `arr[i] == arr[i + n//4]` for some index `i`. Simple linear scan, O(n) time, O(1) space.

[Committed changes to planner branch]