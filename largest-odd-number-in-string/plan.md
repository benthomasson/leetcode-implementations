# Plan (Iteration 1)

Task: Solve the LeetCode problem "largest-odd-number-in-string":

You are given a string `num`, representing a large integer. Return _the **largest-valued odd** integer (as a string) that is a **non-empty substring** of_ `num`_, or an empty string_ `" "` _if no odd integer exists_.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

**Input:** num =  "52 "
**Output:**  "5 "
**Explanation:** The only non-empty substrings are  "5 ",  "2 ", and  "52 ".  "5 " is the only odd number.

**Example 2:**

**Input:** num =  "4206 "
**Output:**  " "
**Explanation:** There are no odd numbers in  "4206 ".

**Example 3:**

**Input:** num =  "35427 "
**Output:**  "35427 "
**Explanation:**  "35427 " is already an odd number.

**Constraints:**

*   `1 <= num.length <= 105`
*   `num` only consists of digits and does not contain any leading zeros.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: largest_odd_number

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The solution is a simple right-to-left scan for the rightmost odd digit, returning the prefix up to and including that digit. O(n) time, O(1) space, high confidence.

[Committed changes to planner branch]