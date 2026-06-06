# Plan (Iteration 1)

Task: Solve the LeetCode problem "day-of-the-year":

Given a string `date` representing a [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) date formatted as `YYYY-MM-DD`, return _the day number of the year_.

**Example 1:**

**Input:** date =  "2019-01-09 "
**Output:** 9
**Explanation:** Given date is the 9th day of the year in 2019.

**Example 2:**

**Input:** date =  "2019-02-10 "
**Output:** 41

**Constraints:**

*   `date.length == 10`
*   `date[4] == date[7] == '-'`, and all other `date[i]`'s are digits
*   `date` represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: is_leap_year

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The problem is straightforward — parse the date, sum month lengths, adjust for leap years. O(1) time and space, no libraries needed.

[Committed changes to planner branch]