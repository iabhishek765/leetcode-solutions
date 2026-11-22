"""
Problem: Check if All A's Appears Before All B's (LC #2124)
Difficulty: Easy
Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

Approach:
- If any 'b' is followed immediately by an 'a', some a appears after
  a b, so the answer is False
- Otherwise every a comes before every b
- So the answer is simply: "ba" not in s
- Time: O(n) | Space: O(1)

ML Connection:
- Checking that a sequence follows an ordering rule is the same kind
  of validation used on token or label sequences before training.
"""

class Solution:
    def checkString(self, s):
        return "ba" not in s
