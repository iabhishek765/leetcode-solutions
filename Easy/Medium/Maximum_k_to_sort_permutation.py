"""
Problem: Maximum K to Sort a Permutation (LC #3644)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

Approach:
- For a given k, elements can swap if both have (val & k) == k
- Group elements by (val & k) — within group free to rearrange
- Check if each group's sorted values match sorted array at same indices
- Iterate k from 0 to max to find maximum valid k
- Time: O(n * max_val) | Space: O(n)

ML Connection:
- Bitwise grouping mirrors hash-based partitioning used
  in distributed ML training across GPU clusters
- Constraint-based sorting appears in constrained
  optimization problems in reinforcement learning
"""

class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        displaced = [nums[i] for i in range(len(nums)) if nums[i] != i]
        
        
        if not displaced:
            return 0
        
        
        ans = displaced[0]
        for val in displaced[1:]:
            ans &= val
            
        return ans
