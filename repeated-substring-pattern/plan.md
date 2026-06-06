# Plan (Iteration 1)

Task: Solve the LeetCode problem "repeated-substring-pattern":

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

**Example 1:**

**Input:** s =  "abab "
**Output:** true
**Explanation:** It is the substring  "ab " twice.

**Example 2:**

**Input:** s =  "aba "
**Output:** false

**Example 3:**

**Input:** s =  "abcabcabcabc "
**Output:** true
**Explanation:** It is the substring  "abc " four times or the substring  "abcabc " twice.

**Constraints:**

*   `1 <= s.length <= 104`
*   `s` consists of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: can_construct

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The key insight is the **string doubling trick** — if `s` is in `(s+s)[1:-1]`, it's made of repeated substrings. Simple, elegant, optimal.

[Committed changes to planner branch]