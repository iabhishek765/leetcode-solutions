"""
Problem: Excel Sheet Column Number (LC #171)
Difficulty: Easy
Link: https://leetcode.com/problems/excel-sheet-column-number/

Approach:
- Treat the title as a base-26 number with A=1 ... Z=26
- For each letter: result = result * 26 + letter_value
- Time: O(n) | Space: O(1)

ML Connection:
- Converting symbol strings to numbers positionally is the same idea
  as encoding tokens or categories into integer IDs/hashes.
"""

class Solution:
    def titleToNumber(self, columnTitle):
        result = 0
        for c in columnTitle:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result
