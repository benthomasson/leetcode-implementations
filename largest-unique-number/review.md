# Review: Largest Unique Number

## Solution
- **Approach**: Uses Counter to count occurrences, filters for elements appearing once, returns max or -1 if none exist
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Has Issues - **Critical bug: function named `last_substring` instead of problem-appropriate name like `largest_unique_number`**

## Tests
- **Coverage**: Good - 8 tests covering examples, single element, all duplicates, all unique, zero, mixed cases, and boundary values
- **Edge Cases**: Yes - covers single element, all duplicates, all unique, zero value, and max constraint (1000)

## Plan
- **Quality**: Adequate - Brief plan describes Counter approach and complexity correctly for minimal effort level

## Overall
Algorithm is correct but has a critical naming bug: function is called `last_substring` (suggests string operations) when it should be `largest_unique_number` or similar. Tests are comprehensive and well-structured.
