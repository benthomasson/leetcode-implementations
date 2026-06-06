# Plan (Iteration 1)

Task: Solve the LeetCode problem "convert-the-temperature":

You are given a non-negative floating point number rounded to two decimal places `celsius`, that denotes the **temperature in Celsius**.

You should convert Celsius into **Kelvin** and **Fahrenheit** and return it as an array `ans = [kelvin, fahrenheit]`.

Return _the array `ans`._ Answers within `10-5` of the actual answer will be accepted.

**Note that:**

*   `Kelvin = Celsius + 273.15`
*   `Fahrenheit = Celsius * 1.80 + 32.00`

**Example 1:**

**Input:** celsius = 36.50
**Output:** \[309.65000,97.70000\]
**Explanation:** Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

**Example 2:**

**Input:** celsius = 122.11
**Output:** \[395.26000,251.79800\]
**Explanation:** Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.

**Constraints:**

*   `0 <= celsius <= 1000`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: convert_temperature

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Straightforward formula problem — the implementer just needs to apply the two conversion formulas and write basic tests.

[Committed changes to planner branch]