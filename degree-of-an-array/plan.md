# Plan (Iteration 1)

Task: Solve the LeetCode problem "degree-of-an-array":

Given a non-empty array of non-negative integers `nums`, the **degree** of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of `nums`, that has the same degree as `nums`.

**Example 1:**

**Input:** nums = \[1,2,2,3,1\]
**Output:** 2
**Explanation:** 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
\[1, 2, 2, 3, 1\], \[1, 2, 2, 3\], \[2, 2, 3, 1\], \[1, 2, 2\], \[2, 2, 3\], \[2, 2\]
The shortest length is 2. So return 2.

**Example 2:**

**Input:** nums = \[1,2,2,3,1,4,2\]
**Output:** 6
**Explanation:** 
The degree is 3 because the element 2 is repeated 3 times.
So \[2,2,3,1,4,2\] is the shortest subarray, therefore returning 6.

**Constraints:**

*   `nums.length` will be between 1 and 50,000.
*   `nums[i]` will be an integer between 0 and 49,999.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: findShortestSubArray

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is optimal — single O(n) pass tracking count/first/last index per element, then a linear scan over the tracked data to find the shortest subarray matching the degree.

[Committed changes to planner branch]