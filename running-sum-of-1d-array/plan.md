# Plan (Iteration 1)

Task: Solve the LeetCode problem "running-sum-of-1d-array":

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]...nums[i])`.

Return the running sum of `nums`.

**Example 1:**

**Input:** nums = \[1,2,3,4\]
**Output:** \[1,3,6,10\]
**Explanation:** Running sum is obtained as follows: \[1, 1+2, 1+2+3, 1+2+3+4\].

**Example 2:**

**Input:** nums = \[1,1,1,1,1\]
**Output:** \[1,2,3,4,5\]
**Explanation:** Running sum is obtained as follows: \[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1\].

**Example 3:**

**Input:** nums = \[3,1,2,10,1\]
**Output:** \[3,4,6,16,17\]

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `-10^6 <= nums[i] <= 10^6`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: runningSum

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `/workspaces/running-sum-of-1d-array/planner/PLAN.md`.

**Summary:** In-place prefix sum — iterate forward, accumulate `nums[i] += nums[i-1]`. O(n) time, O(1) space. Two files: `solution.py` (with docstring + type hints) and `test_solution.py` (examples + edge cases). Confidence: HIGH.

[Committed changes to planner branch]