# Plan (Iteration 1)

Task: Solve the LeetCode problem "shuffle-string":

You are given a string `s` and an integer array `indices` of the **same length**. The string `s` will be shuffled such that the character at the `ith` position moves to `indices[i]` in the shuffled string.

Return _the shuffled string_.

**Example 1:**

**Input:** s =  "codeleet ", `indices` = \[4,5,6,7,0,2,1,3\]
**Output:**  "leetcode "
**Explanation:** As shown,  "codeleet " becomes  "leetcode " after shuffling.

**Example 2:**

**Input:** s =  "abc ", `indices` = \[0,1,2\]
**Output:**  "abc "
**Explanation:** After shuffling, each character remains in its position.

**Constraints:**

*   `s.length == indices.length == n`
*   `1 <= n <= 100`
*   `s` consists of only lowercase English letters.
*   `0 <= indices[i] < n`
*   All values of `indices` are **unique**.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: kids_with_candies

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is straightforward: direct O(n) placement into a result array. The only notable quirk is the required function name `kids_with_candies` which doesn't match the problem — flagged but following requirements as stated.

[Committed changes to planner branch]