# Plan (Iteration 1)

Task: Solve the LeetCode problem "detect-capital":

We define the usage of capitals in a word to be right when one of the following cases holds:

*   All letters in this word are capitals, like `"USA "`.
*   All letters in this word are not capitals, like `"leetcode "`.
*   Only the first letter in this word is capital, like `"Google "`.

Given a string `word`, return `true` if the usage of capitals in it is right.

**Example 1:**

**Input:** word = "USA"
**Output:** true

**Example 2:**

**Input:** word = "FlaG"
**Output:** false

**Constraints:**

*   `1 <= word.length <= 100`
*   `word` consists of lowercase and uppercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: detectCapitalUse

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: count uppercase letters and check against the three valid patterns. Ready for implementation.

[Committed changes to planner branch]