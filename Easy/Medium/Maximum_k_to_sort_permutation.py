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

from collections import defaultdict

class Solution:
    def maximumK(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)

        if nums == sorted_nums:
            return 0

        def can_sort(k):
            groups = defaultdict(list)
            for i, v in enumerate(nums):
                groups[v & k].append(i)
            for mask, indices in groups.items():
                indices.sort()
                vals = sorted(nums[i] for i in indices)
                if vals != [sorted_nums[i] for i in indices]:
                    return False
            return True

        ans = 0
        for k in range(max(nums) + 1):
            if can_sort(k):
                ans = k
        return ans
