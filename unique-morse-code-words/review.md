# Review: Unique Morse Code Words

## Solution
- **Approach**: Set comprehension to collect unique Morse transformations by mapping each character to its Morse code and joining, then counting distinct results.
- **Time Complexity**: O(n·k) where n = number of words, k = average word length
- **Space Complexity**: O(n·k) for storing unique transformations
- **Correctness**: Has Issues - Function name `rotated_digits` is completely wrong (belongs to LeetCode problem 788, not this problem). Should be `uniqueMorseRepresentations` or similar.

## Tests
- **Coverage**: Adequate - covers both examples, identical words, single characters, and Morse collisions
- **Edge Cases**: Partially - missing max length word (12 chars) and boundary cases like all 26 letters

## Plan
- **Quality**: Has Issues - Contains incorrect requirement "Function name should be: rotated_digits" which is from a different LeetCode problem

## Overall
The algorithm is correct and efficient, but there's a critical naming bug: `rotated_digits` is the wrong function name from a completely different problem (788 - Rotated Digits). The plan's requirements section has this same error, suggesting a copy-paste mistake from another problem's template.
