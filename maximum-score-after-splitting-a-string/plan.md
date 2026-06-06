# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-score-after-splitting-a-string":

Given a string `s` of zeros and ones, _return the maximum score after splitting the string into two **non-empty** substrings_ (i.e. **left** substring and **right** substring).

The score after splitting a string is the number of **zeros** in the **left** substring plus the number of **ones** in the **right** substring.

**Example 1:**

**Input:** s =  "011101 "
**Output:** 5 
**Explanation:** 
All possible ways of splitting s into two non-empty substrings are:
left =  "0 " and right =  "11101 ", score = 1 + 4 = 5 
left =  "01 " and right =  "1101 ", score = 1 + 3 = 4 
left =  "011 " and right =  "101 ", score = 1 + 2 = 3 
left =  "0111 " and right =  "01 ", score = 1 + 1 = 2 
left =  "01110 " and right =  "1 ", score = 2 + 1 = 3

**Example 2:**

**Input:** s =  "00111 "
**Output:** 5
**Explanation:** When left =  "00 " and right =  "111 ", we get the maximum score = 2 + 3 = 5

**Example 3:**

**Input:** s =  "1111 "
**Output:** 3

**Constraints:**

*   `2 <= s.length <= 500`
*   The string `s` consists of characters `'0'` and `'1'` only.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_possible_divide

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary: O(n) single-pass solution — count total ones, then sweep split positions tracking zeros-left + ones-right, return max. Tests cover all provided examples plus length-2 edge cases and uniform strings.

[Committed changes to planner branch]