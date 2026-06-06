# Plan (Iteration 1)

Task: Solve the LeetCode problem "average-salary-excluding-the-minimum-and-maximum-salary":

You are given an array of **unique** integers `salary` where `salary[i]` is the salary of the `ith` employee.

Return _the average salary of employees excluding the minimum and maximum salary_. Answers within `10-5` of the actual answer will be accepted.

**Example 1:**

**Input:** salary = \[4000,3000,1000,2000\]
**Output:** 2500.00000
**Explanation:** Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

**Example 2:**

**Input:** salary = \[1000,2000,3000\]
**Output:** 2000.00000
**Explanation:** Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

**Constraints:**

*   `3 <= salary.length <= 100`
*   `1000 <= salary[i] <= 106`
*   All the integers of `salary` are **unique**.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_prefix_aligned

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: single-pass O(n) to compute sum, min, max, then `(sum - min - max) / (n - 2)`. No sorting overhead needed.

[Committed changes to planner branch]