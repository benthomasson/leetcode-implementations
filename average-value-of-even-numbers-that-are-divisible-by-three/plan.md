# Plan (Iteration 1)

Task: Solve the LeetCode problem "average-value-of-even-numbers-that-are-divisible-by-three":

Given an integer array `nums` of **positive** integers, return _the average value of all even integers that are divisible by_ `3`_._

Note that the **average** of `n` elements is the **sum** of the `n` elements divided by `n` and **rounded down** to the nearest integer.

**Example 1:**

**Input:** nums = \[1,3,6,10,12,15\]
**Output:** 9
**Explanation:** 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

**Example 2:**

**Input:** nums = \[1,2,4,7,10\]
**Output:** 0
**Explanation:** There is no single number that satisfies the requirement, so return 0.

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `1 <= nums[i] <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: average_even_divisible_by_three

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The key insight is that "even and divisible by 3" simplifies to "divisible by 6" — one modulo check, one pass, O(1) space.

[Committed changes to planner branch]