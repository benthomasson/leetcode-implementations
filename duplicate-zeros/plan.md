# Plan (Iteration 1)

Task: Solve the LeetCode problem "duplicate-zeros":

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

**Note** that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

**Example 1:**

**Input:** arr = \[1,0,2,3,0,4,5,0\]
**Output:** \[1,0,0,2,3,0,0,4\]
**Explanation:** After calling your function, the input array is modified to: \[1,0,0,2,3,0,0,4\]

**Example 2:**

**Input:** arr = \[1,2,3\]
**Output:** \[1,2,3\]
**Explanation:** After calling your function, the input array is modified to: \[1,2,3\]

**Constraints:**

*   `1 <= arr.length <= 104`
*   `0 <= arr[i] <= 9`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: duplicateZeros

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Use a two-pass, two-pointer approach — first pass finds where the array splits, second pass writes right-to-left duplicating zeros in place. O(n) time, O(1) space. The only tricky part is handling a zero that falls exactly at the array boundary (write one copy instead of two).

[Committed changes to planner branch]