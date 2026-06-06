# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-integers-with-even-digit-sum":

Given a positive integer `num`, return _the number of positive integers **less than or equal to**_ `num` _whose digit sums are **even**_.

The **digit sum** of a positive integer is the sum of all its digits.

**Example 1:**

**Input:** num = 4
**Output:** 2
**Explanation:**
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    

**Example 2:**

**Input:** num = 30
**Output:** 14
**Explanation:**
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

**Constraints:**

*   `1 <= num <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_tasks

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

- **Algorithm:** Iterate 1 to `num`, count numbers with even digit sum. O(n) time, O(1) space.
- **Function:** `max_tasks(num: int) -> int` with digit sum via `sum(int(d) for d in str(n))`
- **Tests:** Cover both examples, edge cases (1, 2), and boundary (1000).
- **Confidence:** HIGH — straightforward problem.

[Committed changes to planner branch]