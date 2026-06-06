# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-largest-group":

You are given an integer `n`.

Each number from `1` to `n` is grouped according to the sum of its digits.

Return _the number of groups that have the largest size_.

**Example 1:**

**Input:** n = 13
**Output:** 4
**Explanation:** There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
\[1,10\], \[2,11\], \[3,12\], \[4,13\], \[5\], \[6\], \[7\], \[8\], \[9\].
There are 4 groups with largest size.

**Example 2:**

**Input:** n = 2
**Output:** 2
**Explanation:** There are 2 groups \[1\], \[2\] of size 1.

**Constraints:**

*   `1 <= n <= 104`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: countLargestGroup

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple problem — count digit-sum groups, find how many groups tie for the largest size. Counter-based approach, standard tests.

[Committed changes to planner branch]