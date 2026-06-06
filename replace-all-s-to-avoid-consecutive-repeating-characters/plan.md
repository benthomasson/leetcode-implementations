# Plan (Iteration 1)

Task: Solve the LeetCode problem "replace-all-s-to-avoid-consecutive-repeating-characters":

Given a string `s` containing only lowercase English letters and the `'?'` character, convert **all** the `'?'` characters into lowercase letters such that the final string does not contain any **consecutive repeating** characters. You **cannot** modify the non `'?'` characters.

It is **guaranteed** that there are no consecutive repeating characters in the given string **except** for `'?'`.

Return _the final string after all the conversions (possibly zero) have been made_. If there is more than one solution, return **any of them**. It can be shown that an answer is always possible with the given constraints.

**Example 1:**

**Input:** s =  "?zs "
**Output:**  "azs "
**Explanation:** There are 25 solutions for this problem. From  "azs " to  "yzs ", all are valid. Only  "z " is an invalid modification as the string will consist of consecutive repeating characters in  "zzs ".

**Example 2:**

**Input:** s =  "ubv?w "
**Output:**  "ubvaw "
**Explanation:** There are 24 solutions for this problem. Only  "v " and  "w " are invalid modifications as the strings will consist of consecutive repeating characters in  "ubvvw " and  "ubvww ".

**Constraints:**

*   `1 <= s.length <= 100`
*   `s` consist of lowercase English letters and `'?'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: dfs

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Greedy O(n) approach — try `'a'`, `'b'`, `'c'` for each `'?'`, pick whichever doesn't conflict with neighbors.

[Committed changes to planner branch]