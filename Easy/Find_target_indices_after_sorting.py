"""
Problem: Find Target Indices After Sorting Array (LC #2089)
Difficulty: Easy
Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/

Approach:
- Count elements less than target → start index
- Count elements equal to target → how many indices
- Return range(less, less + equal) — no actual sorting needed
- Time: O(n) | Space: O(1)

ML Connection:
- Rank-based indexing is used in percentile calculation
  for feature normalization in ML preprocessing
- Counting elements < target is the basis of
  quantile estimation used in data distribution analysis
"""

class Solution:
    def targetIndices(self, nums, target):
        less  = sum(1 for x in nums if x < target)
        equal = sum(1 for x in nums if x == target)
        return list(range(less, less + equal))
