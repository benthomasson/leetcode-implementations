# Plan (Iteration 1)

Task: Solve the LeetCode problem "maximum-number-of-balloons":

Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon "** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

**Example 1:**

**Input:** text =  "nlaebolko "
**Output:** 1

**Example 2:**

**Input:** text =  "loonbalxballpoon "
**Output:** 2

**Example 3:**

**Input:** text =  "leetcode "
**Output:** 0

**Constraints:**

*   `1 <= text.length <= 104`
*   `text` consists of lower case English letters only.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_number_of_balloons

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is simple: use `Counter` to count character frequencies, divide by each character's required count in "balloon", and return the minimum. O(n) time, O(1) space.

[Committed changes to planner branch]