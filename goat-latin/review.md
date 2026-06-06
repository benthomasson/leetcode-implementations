# Review: Goat Latin

## Solution
- **Approach**: Split sentence into words, transform each based on vowel/consonant start (move first letter if consonant), append "ma" + index-based 'a's, rejoin
- **Time Complexity**: O(n) where n is sentence length
- **Space Complexity**: O(n) for result list and output string
- **Correctness**: Has Issues - **Critical naming bug**: function named `number_of_lines` instead of problem-appropriate name like `toGoatLatin` or `to_goat_latin`. Algorithm itself is correct.

## Tests
- **Coverage**: Good - 10+ tests across both files cover LeetCode examples, single-char words, uppercase handling, edge cases
- **Edge Cases**: Yes - single letter words, uppercase vowels/consonants, all-vowel sequences, mixed case, two-letter words

## Plan
- **Quality**: Adequate - Correctly identifies split-transform-join approach and notes function name quirk, but doesn't flag it as an error

## Overall
Algorithm and test coverage are solid, but the function name `number_of_lines` is completely wrong for a Goat Latin problem (likely copy-paste error from a different problem). Should be renamed to `toGoatLatin` or similar.
