# Plan (Iteration 1)

Task: Solve the LeetCode problem "longest-common-prefix":

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `" "`.

**Example 1:**

**Input:** strs = \[ "flower ", "flow ", "flight "\]
**Output:**  "fl "

**Example 2:**

**Input:** strs = \[ "dog ", "racecar ", "car "\]
**Output:**  " "
**Explanation:** There is no common prefix among the input strings.

**Constraints:**

*   `1 <= strs.length <= 200`
*   `0 <= strs[i].length <= 200`
*   `strs[i]` consists of only lowercase English letters.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: longest_common_prefix

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Vertical scanning is the right call here — simple, optimal, and easy to test.

[Committed changes to planner branch]