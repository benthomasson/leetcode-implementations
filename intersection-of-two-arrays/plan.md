# Plan (Iteration 1)

Task: Solve the LeetCode problem "intersection-of-two-arrays":

Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must be **unique** and you may return the result in **any order**.

**Example 1:**

**Input:** nums1 = \[1,2,2,1\], nums2 = \[2,2\]
**Output:** \[2\]

**Example 2:**

**Input:** nums1 = \[4,9,5\], nums2 = \[9,4,9,8,4\]
**Output:** \[9,4\]
**Explanation:** \[4,9\] is also accepted.

**Constraints:**

*   `1 <= nums1.length, nums2.length <= 1000`
*   `0 <= nums1[i], nums2[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: intersection

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: set intersection in Python gives optimal O(n+m) performance and handles all requirements cleanly.

[Committed changes to planner branch]