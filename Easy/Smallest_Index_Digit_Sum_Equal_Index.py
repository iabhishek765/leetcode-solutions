# LC#3550 - Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# Topics: Array, Math, String
#
# Approach: Iterate with index, compute digit sum of nums[i],
#           return first i where digit_sum == i. Return -1 if none.
# Time: O(n * d) | Space: O(1)
#
# ML Connection: Index-based feature validation is used in
# data integrity checks for ML pipelines where array positions
# must satisfy certain mathematical constraints before training.

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(int(d) for d in str(num)) == i:
                return i
        return -1
