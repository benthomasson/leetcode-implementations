# Plan (Iteration 1)

Task: Solve the LeetCode problem "count-substrings-with-only-one-distinct-letter":

Given a string `s`, return _the number of substrings that have only **one distinct** letter_.

**Example 1:**

**Input:** s =  "aaaba "
**Output:** 8
**Explanation:** The substrings with one distinct letter are  "aaa ",  "aa ",  "a ",  "b ".
 "aaa " occurs 1 time.
 "aa " occurs 2 times.
 "a " occurs 4 times.
 "b " occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

**Example 2:**

**Input:** s =  "aaaaaaaaaa "
**Output:** 55

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s[i]` consists of only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: count_letters

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

- **Algorithm:** Group consecutive identical characters, sum `n*(n+1)/2` for each group. O(n) time, O(1) space.
- **Deliverables:** `solution.py` with typed, documented function + `test_solution.py` with edge case coverage.
- **Confidence:** HIGH — textbook consecutive-group counting problem.