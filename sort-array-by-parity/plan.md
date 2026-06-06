# Plan (Iteration 1)

Task: Solve the LeetCode problem "sort-array-by-parity":

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return _**any array** that satisfies this condition_.

**Example 1:**

**Input:** nums = \[3,1,2,4\]
**Output:** \[2,4,3,1\]
**Explanation:** The outputs \[4,2,3,1\], \[2,4,1,3\], and \[4,2,1,3\] would also be accepted.

**Example 2:**

**Input:** nums = \[0\]
**Output:** \[0\]

**Constraints:**

*   `1 <= nums.length <= 5000`
*   `0 <= nums[i] <= 5000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: lenLongestFibSubseq

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Summary:

- **Algorithm:** Two-pointer in-place swap — O(n) time, O(1) space
- **Key flag:** The TASK.md function name `lenLongestFibSubseq` is wrong; should be `sortArrayByParity`
- **Tests:** all even, all odd, mixed, single element, zeros, already sorted, boundary values
- **Confidence:** HIGH — classic partition problem

[Committed changes to planner branch]