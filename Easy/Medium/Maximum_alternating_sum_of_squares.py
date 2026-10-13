"""
Problem: Maximum Alternating Sum of Squares (LC #3727)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-alternating-sum-of-squares/

Approach:
- Rearrange freely → sort by absolute value descending
- Even indices get added (+), odd indices get subtracted (-)
- Largest abs values at even positions maximizes score
- Time: O(n log n) | Space: O(1)

ML Connection:
- Alternating sign patterns appear in Fourier features
  used in kernel methods for ML classification
- Greedy arrangement by magnitude mirrors feature
  importance ranking in gradient boosting models
"""

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted(x * x for x in nums)
        
        n = len(squares)
        k = n // 2
        
        return sum(squares[k:]) - sum(squares[:k])
