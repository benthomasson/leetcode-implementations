# Plan (Iteration 1)

Task: Solve the LeetCode problem "third-maximum-number":

Given an integer array `nums`, return _the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number_.

**Example 1:**

**Input:** nums = \[3,2,1\]
**Output:** 1
**Explanation:**
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

**Example 2:**

**Input:** nums = \[1,2\]
**Output:** 2
**Explanation:**
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

**Example 3:**

**Input:** nums = \[2,2,3,1\]
**Output:** 1
**Explanation:**
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-231 <= nums[i] <= 231 - 1`

**Follow up:** Can you find an `O(n)` solution?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: third_max

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: three-variable tracking in one pass, with tests covering all edge cases.

[Committed changes to planner branch]