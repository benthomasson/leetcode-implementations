# Plan (Iteration 1)

Task: Solve the LeetCode problem "check-if-all-as-appears-before-all-bs":

Given a string `s` consisting of **only** the characters `'a'` and `'b'`, return `true` _if **every**_ `'a'` _appears before **every**_ `'b'` _in the string_. Otherwise, return `false`.

**Example 1:**

**Input:** s =  "aaabbb "
**Output:** true
**Explanation:**
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

**Example 2:**

**Input:** s =  "abab "
**Output:** false
**Explanation:**
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

**Example 3:**

**Input:** s =  "bbb "
**Output:** true
**Explanation:**
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

**Constraints:**

*   `1 <= s.length <= 100`
*   `s[i]` is either `'a'` or `'b'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: firstDayBeenInAllRooms

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is a one-liner: return `"ba" not in s`. If "ba" appears anywhere, some 'a' follows some 'b', violating the condition.

[Committed changes to planner branch]