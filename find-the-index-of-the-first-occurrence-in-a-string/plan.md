# Plan (Iteration 1)

Task: Solve the LeetCode problem "find-the-index-of-the-first-occurrence-in-a-string":

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

**Input:** haystack =  "sadbutsad ", needle =  "sad "
**Output:** 0
**Explanation:**  "sad " occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

**Example 2:**

**Input:** haystack =  "leetcode ", needle =  "leeto "
**Output:** -1
**Explanation:**  "leeto " did not occur in  "leetcode ", so we return -1.

**Constraints:**

*   `1 <= haystack.length, needle.length <= 104`
*   `haystack` and `needle` consist of only lowercase English characters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: strStr

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary: Use KMP algorithm, implement in a `Solution` class with full docstring, and write thorough tests covering standard and edge cases. Confidence: **HIGH**.

[Committed changes to planner branch]