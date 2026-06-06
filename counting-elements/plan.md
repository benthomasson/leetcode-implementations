# Plan (Iteration 1)

Task: Solve the LeetCode problem "counting-elements":

Given an integer array `arr`, count how many elements `x` there are, such that `x + 1` is also in `arr`. If there are duplicates in `arr`, count them separately.

**Example 1:**

**Input:** arr = \[1,2,3\]
**Output:** 2
**Explanation:** 1 and 2 are counted cause 2 and 3 are in arr.

**Example 2:**

**Input:** arr = \[1,1,3,3,5,5,7,7\]
**Output:** 0
**Explanation:** No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.

**Constraints:**

*   `1 <= arr.length <= 1000`
*   `0 <= arr[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sum_zero

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is a simple set-based lookup — O(n) time and space, no edge-case surprises.

[Committed changes to planner branch]