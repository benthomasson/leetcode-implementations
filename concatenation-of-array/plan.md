# Plan (Iteration 1)

Task: Solve the LeetCode problem "concatenation-of-array":

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return _the array_ `ans`.

**Example 1:**

**Input:** nums = \[1,2,1\]
**Output:** \[1,2,1,1,2,1\]
**Explanation:** The array ans is formed as follows:
- ans = \[nums\[0\],nums\[1\],nums\[2\],nums\[0\],nums\[1\],nums\[2\]\]
- ans = \[1,2,1,1,2,1\]

**Example 2:**

**Input:** nums = \[1,3,2,1\]
**Output:** \[1,3,2,1,1,3,2,1\]
**Explanation:** The array ans is formed as follows:
- ans = \[nums\[0\],nums\[1\],nums\[2\],nums\[3\],nums\[0\],nums\[1\],nums\[2\],nums\[3\]\]
- ans = \[1,3,2,1,1,3,2,1\]

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 1000`
*   `1 <= nums[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: maxValue

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The solution is trivial — `nums + nums` — with O(n) time/space. The implementer just needs to wrap it in the required `Solution.maxValue` method with proper docstring and write the test cases.

[Committed changes to planner branch]