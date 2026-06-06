# Plan (Iteration 1)

Task: Solve the LeetCode problem "sum-of-all-odd-length-subarrays":

Given an array of positive integers `arr`, return _the sum of all possible **odd-length subarrays** of_ `arr`.

A **subarray** is a contiguous subsequence of the array.

**Example 1:**

**Input:** arr = \[1,4,2,5,3\]
**Output:** 58
**Explanation:** The odd-length subarrays of arr and their sums are:
\[1\] = 1
\[4\] = 4
\[2\] = 2
\[5\] = 5
\[3\] = 3
\[1,4,2\] = 7
\[4,2,5\] = 11
\[2,5,3\] = 10
\[1,4,2,5,3\] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

**Example 2:**

**Input:** arr = \[1,2\]
**Output:** 3
**Explanation:** There are only 2 subarrays of odd length, \[1\] and \[2\]. Their sum is 3.

**Example 3:**

**Input:** arr = \[10,11,12\]
**Output:** 66

**Constraints:**

*   `1 <= arr.length <= 100`
*   `1 <= arr[i] <= 1000`

**Follow up:**

Could you solve this problem in O(n) time complexity?

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: sumOddLengthSubarrays

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`.

**Summary:** Use the O(n) contribution-counting approach — for each index `i`, the number of odd-length subarrays containing `arr[i]` is `((i+1) * (n-i) + 1) // 2`. Multiply and sum. Single file solution + tests covering all examples and edge cases. Confidence: **HIGH**.

[Committed changes to planner branch]