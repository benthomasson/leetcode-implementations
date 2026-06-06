# Plan (Iteration 1)

Task: Solve the LeetCode problem "remove-digit-from-number-to-maximize-result":

You are given a string `number` representing a **positive integer** and a character `digit`.

Return _the resulting string after removing **exactly one occurrence** of_ `digit` _from_ `number` _such that the value of the resulting string in **decimal** form is **maximized**_. The test cases are generated such that `digit` occurs at least once in `number`.

**Example 1:**

**Input:** number =  "123 ", digit =  "3 "
**Output:**  "12 "
**Explanation:** There is only one '3' in  "123 ". After removing '3', the result is  "12 ".

**Example 2:**

**Input:** number =  "1231 ", digit =  "1 "
**Output:**  "231 "
**Explanation:** We can remove the first '1' to get  "231 " or remove the second '1' to get  "123 ".
Since 231 > 123, we return  "231 ".

**Example 3:**

**Input:** number =  "551 ", digit =  "5 "
**Output:**  "51 "
**Explanation:** We can remove either the first or second '5' from  "551 ".
Both result in the string  "51 ".

**Constraints:**

*   `2 <= number.length <= 100`
*   `number` consists of digits from `'1'` to `'9'`.
*   `digit` is a digit from `'1'` to `'9'`.
*   `digit` occurs at least once in `number`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: max_number_after_remove_digit

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The approach is a simple greedy single-pass: remove the first occurrence of `digit` where the next character is larger; otherwise remove the last occurrence. O(n) time.

[Committed changes to planner branch]