# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-distinct-numbers-on-board":

You are given a positive integer `n`, that is initially placed on a board. Every day, for `109` days, you perform the following procedure:

*   For each number `x` present on the board, find all numbers `1 <= i <= n` such that `x % i == 1`.
*   Then, place those numbers on the board.

Return _the number of **distinct** integers present on the board after_ `109` _days have elapsed_.

**Note:**

*   Once a number is placed on the board, it will remain on it until the end.
*   `%` stands for the modulo operation. For example, `14 % 3` is `2`.

**Example 1:**

**Input:** n = 5
**Output:** 4
**Explanation:** Initially, 5 is present on the board. 
The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1. 
After that day, 3 will be added to the board because 4 % 3 == 1. 
At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5. 

**Example 2:**

**Input:** n = 3
**Output:** 2
**Explanation:** 
Since 3 % 2 == 1, 2 will be added to the board. 
After a billion days, the only two distinct numbers on the board are 2 and 3. 

**Constraints:**

*   `1 <= n <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: distinct_numbers

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The key insight: for any `x >= 2`, `x % (x-1) == 1`, so starting from `n`, all integers 2 through `n` eventually land on the board. The answer is `max(1, n - 1)` — an O(1) solution.

[Committed changes to planner branch]