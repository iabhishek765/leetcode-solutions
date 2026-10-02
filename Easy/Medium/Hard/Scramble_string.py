"""
Problem: Scramble String (LC #87)
Difficulty: Hard
Link: https://leetcode.com/problems/scramble-string/

Approach:
- Recursion + memoization (top-down DP)
- For each split point i, check two cases:
  1. Not swapped: s1[:i]==s2[:i] and s1[i:]==s2[i:]
  2. Swapped: s1[:i]==s2[n-i:] and s1[i:]==s2[:n-i]
- Early exit: if sorted chars differ, can't be scramble
- Time: O(n^4) | Space: O(n^3)

ML Connection:
- Memoization is the basis of dynamic programming
  used in reinforcement learning value iteration
- String similarity checks appear in data augmentation
  techniques for NLP model training
"""

class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                if dp(a[:i], b[:i]) and dp(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                if dp(a[:i], b[n-i:]) and dp(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dp(s1, s2)
