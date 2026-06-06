# Plan (Iteration 1)

Task: Solve the LeetCode problem "substrings-of-size-three-with-distinct-characters":

A string is **good** if there are no repeated characters.

Given a string `s`​​​​​, return _the number of **good substrings** of length **three** in_ `s`​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A **substring** is a contiguous sequence of characters in a string.

**Example 1:**

**Input:** s =  "xyzzaz "
**Output:** 1
**Explanation:** There are 4 substrings of size 3:  "xyz ",  "yzz ",  "zza ", and  "zaz ". 
The only good substring of length 3 is  "xyz ".

**Example 2:**

**Input:** s =  "aababcabc "
**Output:** 4
**Explanation:** There are 7 substrings of size 3:  "aab ",  "aba ",  "bab ",  "abc ",  "bca ",  "cab ", and  "abc ".
The good substrings are  "abc ",  "bca ",  "cab ", and  "abc ".

**Constraints:**

*   `1 <= s.length <= 100`
*   `s`​​​​​​ consists of lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: highest_island

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary:

- **Algorithm:** Sliding window of size 3, check all 3 chars distinct via direct comparison. O(n) time, O(1) space.
- **Function:** `highest_island(self, s: str) -> int` (per requirements)
- **Tests:** Both examples, short strings, all-same, all-distinct, edge cases.
- **Confidence:** HIGH — straightforward problem.

[Committed changes to planner branch]