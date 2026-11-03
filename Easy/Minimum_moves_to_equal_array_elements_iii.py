"""
Problem: Minimum Moves to Equal Array Elements III (LC #3736)
Difficulty: Easy
Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

Approach:
- Moves can only increase a value, so the target is max(nums)
- Total moves = sum(max - x for every x) = max * n - sum(nums)
- Time: O(n) | Space: O(1)

ML Connection:
- Aligning every value to the maximum is the idea behind
  padding variable-length sequences to the longest one in a
  batch before feeding them to a model.
"""

class Solution:
    def minMoves(self, nums):
        return max(nums) * len(nums) - sum(nums)
