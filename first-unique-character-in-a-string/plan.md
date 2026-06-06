# Plan (Iteration 1)

Task: Solve the LeetCode problem "first-unique-character-in-a-string":

Given a string `s`, _find the first non-repeating character in it and return its index_. If it does not exist, return `-1`.

**Example 1:**

**Input:** s = "leetcode"
**Output:** 0

**Example 2:**

**Input:** s = "loveleetcode"
**Output:** 2

**Example 3:**

**Input:** s = "aabb"
**Output:** -1

**Constraints:**

*   `1 <= s.length <= 105`
*   `s` consists of only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: firstUniqChar

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is straightforward: Counter for frequencies, linear scan for the first unique character. O(n) time, O(1) space.

[Committed changes to planner branch]