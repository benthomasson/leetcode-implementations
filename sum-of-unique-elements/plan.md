# Plan (Iteration 1)

Task: Solve the LeetCode problem "sum-of-unique-elements":

You are given an integer array `nums`. The unique elements of an array are the elements that appear **exactly once** in the array.

Return _the **sum** of all the unique elements of_ `nums`.

**Example 1:**

**Input:** nums = \[1,2,3,2\]
**Output:** 4
**Explanation:** The unique elements are \[1,3\], and the sum is 4.

**Example 2:**

**Input:** nums = \[1,1,1,1,1\]
**Output:** 0
**Explanation:** There are no unique elements, and the sum is 0.

**Example 3:**

**Input:** nums = \[1,2,3,4,5\]
**Output:** 15
**Explanation:** The unique elements are \[1,2,3,4,5\], and the sum is 15.

**Constraints:**

*   `1 <= nums.length <= 100`
*   `1 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: bestTeamScore

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is straightforward: count frequencies with `Counter`, sum elements appearing exactly once. O(n) time and space.

[Committed changes to planner branch]