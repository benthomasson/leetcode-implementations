# Plan (Iteration 1)

Task: Solve the LeetCode problem "intersection-of-three-sorted-arrays":

Given three integer arrays `arr1`, `arr2` and `arr3` **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

**Input:** arr1 = \[1,2,3,4,5\], arr2 = \[1,2,5,7,9\], arr3 = \[1,3,4,5,8\]
**Output:** \[1,5\]
**Explanation:** Only 1 and 5 appeared in the three arrays.

**Example 2:**

**Input:** arr1 = \[197,418,523,876,1356\], arr2 = \[501,880,1593,1710,1870\], arr3 = \[521,682,1337,1395,1764\]
**Output:** \[\]

**Constraints:**

*   `1 <= arr1.length, arr2.length, arr3.length <= 1000`
*   `1 <= arr1[i], arr2[i], arr3[i] <= 2000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: arraysIntersection

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The three-pointer approach is optimal and straightforward for this problem — no ambiguity in the design.

[Committed changes to planner branch]