"""
Problem: Partition Array According to Given Pivot (LC #2161)
Difficulty: Medium
Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/

Approach:
- Count smaller and greater elements first
- Place pivot in the middle positions
- Fill smaller from left, greater from right in one pass
- Time: O(n) | Space: O(n)

ML Connection:
- Partitioning is core to Decision Trees — splitting data
  by a threshold (pivot) at each node is exactly this logic
- Also used in QuickSelect which finds median values
  used in data preprocessing and normalization
"""

class Solution:
    def pivotArray(self, nums, pivot):
        n = len(nums)

        ans = [pivot] * n

        smaller_count = 0
        greater_count = 0

        for num in nums:
            if num < pivot:
                smaller_count += 1
            if num > pivot:
                greater_count += 1

        sp = 0
        gp = n - greater_count

        for num in nums:
            if num < pivot:
                ans[sp] = num
                sp += 1
            if num > pivot:
                ans[gp] = num
                gp += 1

        return ans
