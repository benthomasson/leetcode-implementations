# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-closest-number-to-zero":

Given an integer array `nums` of size `n`, return _the number with the value **closest** to_ `0` _in_ `nums`. If there are multiple answers, return _the number with the **largest** value_.

**Example 1:**

**Input:** nums = \[-4,-2,1,4,8\]
**Output:** 1
**Explanation:**
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

**Example 2:**

**Input:** nums = \[2,-1,1\]
**Output:** 1
**Explanation:** 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

**Constraints:**

*   `1 <= n <= 1000`
*   `-105 <= nums[i] <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: robot_instructions

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Single-pass O(n) scan tracking the closest-to-zero candidate, with tie-breaking favoring the positive value. Function name `robot_instructions`, Google-style docstring, and comprehensive edge-case tests.

[Committed changes to planner branch]