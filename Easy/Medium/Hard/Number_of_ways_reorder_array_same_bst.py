"""
Problem: Number of Ways to Reorder Array to Get Same BST (LC #1569)
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

Approach:
- Root is always fixed (first element)
- Split remaining into left (<root) and right (>root)
- Ways to interleave = C(left+right, left) — binomial coefficient
- Multiply recursively for each subtree
- Subtract 1 (original arrangement not counted)
- Time: O(n²) | Space: O(n²)

ML Connection:
- BST structure mirrors decision tree splits where
  each node divides data into two subsets
- Counting valid tree orderings relates to tree
  ensembling in Random Forests and gradient boosting
"""

from math import comb

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        def count(arr):
            if len(arr) <= 1:
                return 1
            root = arr[0]
            left  = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return comb(len(left) + len(right), len(left)) * count(left) * count(right) % MOD

        return (count(nums) - 1) % MOD
