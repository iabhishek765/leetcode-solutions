"""
Problem: Valid Palindrome (LC #125)
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

Approach:
- Filter only alphanumeric chars and lowercase them
- Check if cleaned string equals its reverse
- Time: O(n) | Space: O(n)

ML Connection:
- String cleaning/normalization is a core NLP preprocessing
  step before tokenization in transformer models
- Palindrome checking logic appears in DNA sequence
  analysis used in bioinformatics ML models
"""

class Solution:
    def isPalindrome(self, s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
