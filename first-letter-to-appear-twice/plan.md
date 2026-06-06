# Plan (Iteration 1)

Task: Solve the LeetCode problem "first-letter-to-appear-twice":

Given a string `s` consisting of lowercase English letters, return _the first letter to appear **twice**_.

**Note**:

*   A letter `a` appears twice before another letter `b` if the **second** occurrence of `a` is before the **second** occurrence of `b`.
*   `s` will contain at least one letter that appears twice.

**Example 1:**

**Input:** s =  "abccbaacz "
**Output:**  "c "
**Explanation:**
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

**Example 2:**

**Input:** s =  "abcdd "
**Output:**  "d "
**Explanation:**
The only letter that appears twice is 'd' so we return 'd'.

**Constraints:**

*   `2 <= s.length <= 100`
*   `s` consists of lowercase English letters.
*   `s` has at least one repeated letter.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: first_letter_to_appear_twice

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is straightforward: single-pass set scan, O(n) time, O(1) space.

[Committed changes to planner branch]