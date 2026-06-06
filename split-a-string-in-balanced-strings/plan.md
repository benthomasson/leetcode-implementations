# Plan (Iteration 1)

Task: Solve the LeetCode problem "split-a-string-in-balanced-strings":

**Balanced** strings are those that have an equal quantity of `'L'` and `'R'` characters.

Given a **balanced** string `s`, split it into some number of substrings such that:

*   Each substring is balanced.

Return _the **maximum** number of balanced strings you can obtain._

**Example 1:**

**Input:** s =  "RLRRLLRLRL "
**Output:** 4
**Explanation:** s can be split into  "RL ",  "RRLL ",  "RL ",  "RL ", each substring contains same number of 'L' and 'R'.

**Example 2:**

**Input:** s =  "RLRRRLLRLL "
**Output:** 2
**Explanation:** s can be split into  "RL ",  "RRRLLRLL ", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into  "RL ",  "RR ",  "RL ",  "LR ",  "LL ", because the 2nd and 5th substrings are not balanced.

**Example 3:**

**Input:** s =  "LLLLRRRR "
**Output:** 1
**Explanation:** s can be split into  "LLLLRRRR ".

**Constraints:**

*   `2 <= s.length <= 1000`
*   `s[i]` is either `'L'` or `'R'`.
*   `s` is a **balanced** string.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: find_special_integer

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The greedy counter approach is the clear choice here — single pass, constant space, no edge cases to worry about beyond what the tests cover.

[Committed changes to planner branch]