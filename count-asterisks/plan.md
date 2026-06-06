# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-asterisks":

You are given a string `s`, where every **two** consecutive vertical bars `'|'` are grouped into a **pair**. In other words, the 1st and 2nd `'|'` make a pair, the 3rd and 4th `'|'` make a pair, and so forth.

Return _the number of_ `'*'` _in_ `s`_, **excluding** the_ `'*'` _between each pair of_ `'|'`.

**Note** that each `'|'` will belong to **exactly** one pair.

**Example 1:**

**Input:** s =  "l|\*e\*et|c\*\*o|\*de| "
**Output:** 2
**Explanation:** The considered characters are underlined:  "l|\*e\*et|c\*\*o|\*de| ".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.

**Example 2:**

**Input:** s =  "iamprogrammer "
**Output:** 0
**Explanation:** In this example, there are no asterisks in s. Therefore, we return 0.

**Example 3:**

**Input:** s =  "yo|uar|e\*\*|b|e\*\*\*au|tifu|l "
**Output:** 5
**Explanation:** The considered characters are underlined:  "yo|uar|e\*\*|b|e\*\*\*au|tifu|l ". There are 5 asterisks considered. Therefore, we return 5.

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` consists of lowercase English letters, vertical bars `'|'`, and asterisks `'*'`.
*   `s` contains an **even** number of vertical bars `'|'`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_stars_except_between_pair

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The problem is straightforward — single pass with a boolean toggle for `|` pairs, counting `*` only when outside pairs.

[Committed changes to planner branch]