# Plan (Iteration 1)

Task: Solve the LeetCode problem "day-of-the-week":

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the `day`, `month` and `year` respectively.

Return the answer as one of the following values `{ "Sunday ", "Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday "}`.

**Example 1:**

**Input:** day = 31, month = 8, year = 2019
**Output:**  "Saturday "

**Example 2:**

**Input:** day = 18, month = 7, year = 1999
**Output:**  "Sunday "

**Example 3:**

**Input:** day = 15, month = 8, year = 1993
**Output:**  "Sunday "

**Constraints:**

*   The given dates are valid dates between the years `1971` and `2100`.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: day_of_the_week

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. Summary: use `datetime.date.weekday()` — O(1), trivial mapping to day names with trailing spaces. Tests should cover the 3 examples plus edge cases (leap days, boundary years).

[Committed changes to planner branch]