# Plan (Iteration 1)

Task: Solve the LeetCode problem "long-pressed-name":

Your friend is typing his `name` into a keyboard. Sometimes, when typing a character `c`, the key might get _long pressed_, and the character will be typed 1 or more times.

You examine the `typed` characters of the keyboard. Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

**Example 1:**

**Input:** name =  "alex ", typed =  "aaleex "
**Output:** true
**Explanation:** 'a' and 'e' in 'alex' were long pressed.

**Example 2:**

**Input:** name =  "saeed ", typed =  "ssaaedd "
**Output:** false
**Explanation:** 'e' must have been pressed twice, but it was not in the typed output.

**Constraints:**

*   `1 <= name.length, typed.length <= 1000`
*   `name` and `typed` consist of only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The two-pointer approach is the standard optimal solution for this problem — straightforward to implement with clear edge cases to test.

[Committed changes to planner branch]