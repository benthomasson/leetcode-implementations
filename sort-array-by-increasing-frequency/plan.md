# Plan (Iteration 1)

Task: Solve the LeetCode problem "sort-array-by-increasing-frequency":

Given an array of integers `nums`, sort the array in **increasing** order based on the frequency of the values. If multiple values have the same frequency, sort them in **decreasing** order.

Return the _sorted array_.

**Example 1:**

**Input:** nums = \[1,1,2,2,2,3\]
**Output:** \[3,1,1,2,2,2\]
**Explanation:** '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

**Example 2:**

**Input:** nums = \[2,3,1,3,2\]
**Output:** \[1,3,3,2,2\]
**Explanation:** '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

**Example 3:**

**Input:** nums = \[-1,1,-6,4,5,-6,1,4,1\]
**Output:** \[5,-1,4,4,-6,-6,1,1,1\]

**Constraints:**

*   `1 <= nums.length <= 100`
*   `-100 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: num_sub

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is simple and well-suited: Counter for frequencies, sort with `(freq, -value)` key. High confidence.

[Committed changes to planner branch]