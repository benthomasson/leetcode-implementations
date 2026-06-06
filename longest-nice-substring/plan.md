# Plan (Iteration 1)

Task: Solve the LeetCode problem "longest-nice-substring":

A string `s` is **nice** if, for every letter of the alphabet that `s` contains, it appears **both** in uppercase and lowercase. For example, `"abABB "` is nice because `'A'` and `'a'` appear, and `'B'` and `'b'` appear. However, `"abA "` is not because `'b'` appears, but `'B'` does not.

Given a string `s`, return _the longest **substring** of `s` that is **nice**. If there are multiple, return the substring of the **earliest** occurrence. If there are none, return an empty string_.

**Example 1:**

**Input:** s =  "YazaAay "
**Output:**  "aAa "
**Explanation: ** "aAa " is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
 "aAa " is the longest nice substring.

**Example 2:**

**Input:** s =  "Bb "
**Output:**  "Bb "
**Explanation:**  "Bb " is a nice string because both 'B' and 'b' appear. The whole string is a substring.

**Example 3:**

**Input:** s =  "c "
**Output:**  " "
**Explanation:** There are no nice substrings.

**Constraints:**

*   `1 <= s.length <= 100`
*   `s` consists of uppercase and lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: longestNiceSubstring

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. 

**Summary:** Use divide-and-conquer — find a character without its case pair, split there, recurse on both sides, return the longest. Two files: `solution.py` and `tests/test_solution.py`. Confidence is HIGH.

[Committed changes to planner branch]