# Review: Number of Equivalent Domino Pairs

## Solution
- **Approach**: Normalize each domino to (min, max) tuple, count occurrences with Counter, then sum n*(n-1)//2 for each group
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Has Issues - Function name `remove_duplicates` is incorrect for a domino counting problem (likely copy-paste error from plan template)

## Tests
- **Coverage**: Good - 8 test cases covering examples, single domino, all identical, all unique, palindromes, rotations, and mixed groups
- **Edge Cases**: Yes - covers single element, all same, all unique, palindrome dominoes [1,1], and rotated pairs

## Plan
- **Quality**: Adequate - Correctly describes the normalize-and-count approach with O(n) complexity, but contains incorrect function name requirement

## Overall
Algorithm is correct and efficient. Major issue: function name should be `numEquivDominoPairs` not `remove_duplicates`. Tests are comprehensive and well-designed.
