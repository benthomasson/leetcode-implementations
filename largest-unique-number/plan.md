# Plan (Iteration 1)

Task: Solve the LeetCode problem "largest-unique-number":

Given an integer array `nums`, return _the largest integer that only occurs once_. If no integer occurs once, return `-1`.

**Example 1:**

**Input:** nums = \[5,7,3,9,4,9,8,3,1\]
**Output:** 8
**Explanation:** The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

**Example 2:**

**Input:** nums = \[9,9,8,8\]
**Output:** -1
**Explanation:** There is no number that occurs only once.

**Constraints:**

*   `1 <= nums.length <= 2000`
*   `0 <= nums[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: last_substring

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple Counter-based approach — O(n) time and space, covers all edge cases.

[Committed changes to planner branch]