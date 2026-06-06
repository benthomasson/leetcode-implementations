# Plan (Iteration 1)

Task: Solve the LeetCode problem "buddy-strings":

Given two strings `s` and `goal`, return `true` _if you can swap two letters in_ `s` _so the result is equal to_ `goal`_, otherwise, return_ `false`_._

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`.

*   For example, swapping at indices `0` and `2` in `"abcd "` results in `"cbad "`.

**Example 1:**

**Input:** s =  "ab ", goal =  "ba "
**Output:** true
**Explanation:** You can swap s\[0\] = 'a' and s\[1\] = 'b' to get  "ba ", which is equal to goal.

**Example 2:**

**Input:** s =  "ab ", goal =  "ab "
**Output:** false
**Explanation:** The only letters you can swap are s\[0\] = 'a' and s\[1\] = 'b', which results in  "ba " != goal.

**Example 3:**

**Input:** s =  "aa ", goal =  "aa "
**Output:** true
**Explanation:** You can swap s\[0\] = 'a' and s\[1\] = 'a' to get  "aa ", which is equal to goal.

**Constraints:**

*   `1 <= s.length, goal.length <= 2 * 104`
*   `s` and `goal` consist of lowercase letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** O(n) single-pass algorithm with three cases — different lengths (false), identical strings (check for duplicate chars), and differing strings (must differ at exactly 2 positions that cross-match). High confidence, straightforward problem.

[Committed changes to planner branch]