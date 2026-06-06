# Plan (Iteration 1)

Task: Solve the LeetCode problem "left-and-right-sum-differences":

Given a **0-indexed** integer array `nums`, find a **0-indexed** integer array `answer` where:

*   `answer.length == nums.length`.
*   `answer[i] = |leftSum[i] - rightSum[i]|`.

Where:

*   `leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`.
*   `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.

Return _the array_ `answer`.

**Example 1:**

**Input:** nums = \[10,4,8,3\]
**Output:** \[15,1,11,22\]
**Explanation:** The array leftSum is \[0,10,14,22\] and the array rightSum is \[15,11,3,0\].
The array answer is \[|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|\] = \[15,1,11,22\].

**Example 2:**

**Input:** nums = \[1\]
**Output:** \[0\]
**Explanation:** The array leftSum is \[0\] and the array rightSum is \[0\].
The array answer is \[|0 - 0|\] = \[0\].

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `1 <= nums[i] <= 105`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: get_answer

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is avoiding two separate prefix-sum arrays by using `total_sum - left_sum - nums[i]` to get `right_sum` on the fly, keeping it to a single O(n) pass.

[Committed changes to planner branch]