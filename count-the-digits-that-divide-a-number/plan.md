# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-the-digits-that-divide-a-number":

Given an integer `num`, return _the number of digits in `num` that divide_ `num`.

An integer `val` divides `nums` if `nums % val == 0`.

**Example 1:**

**Input:** num = 7
**Output:** 1
**Explanation:** 7 divides itself, hence the answer is 1.

**Example 2:**

**Input:** num = 121
**Output:** 2
**Explanation:** 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

**Example 3:**

**Input:** num = 1248
**Output:** 4
**Explanation:** 1248 is divisible by all of its digits, hence the answer is 4.

**Constraints:**

*   `1 <= num <= 109`
*   `num` does not contain `0` as one of its digits.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: digits_dividing_num

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Simple digit-iteration problem — no design decisions to deliberate.

[Committed changes to planner branch]