# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-subsequence-of-length-k-with-the-largest-sum":

You are given an integer array `nums` and an integer `k`. You want to find a **subsequence** of `nums` of length `k` that has the **largest** sum.

Return _**any** such subsequence as an integer array of length_ `k`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

**Input:** nums = \[2,1,3,3\], k = 2
**Output:** \[3,3\]
**Explanation:**
The subsequence has the largest sum of 3 + 3 = 6.

**Example 2:**

**Input:** nums = \[-1,-2,3,4\], k = 3
**Output:** \[-1,3,4\]
**Explanation:** 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

**Example 3:**

**Input:** nums = \[3,4,3,3\], k = 2
**Output:** \[3,4\]
**Explanation:**
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is \[4, 3\].

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `-105 <= nums[i] <= 105`
*   `1 <= k <= nums.length`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_patterns_in_word

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`.

**Summary:** Pick the k largest elements by value, then return them in their original index order. O(n log n) time. One note — the required function name `count_patterns_in_word` is clearly a copy-paste error from a different problem, but the plan follows it as specified.

[Committed changes to planner branch]