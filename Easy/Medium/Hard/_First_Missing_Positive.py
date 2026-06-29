"""
LC#41 - First Missing Positive [Hard]
Topic: Array / In-place Hashing
ML Connection: Using array indices as an implicit hash table is a 
classic space-optimization trick, similar to how embedding lookup 
tables map indices to slots without extra storage.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
