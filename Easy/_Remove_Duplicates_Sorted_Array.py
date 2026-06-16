# LC#26 - Remove Duplicates from Sorted Array
# Difficulty: Easy
# Topics: Array, Two Pointers
#
# Approach: Two pointers - slow tracks unique position,
#           fast scans for new unique elements
# Time: O(n) | Space: O(1)
#
# ML Connection: Similar to deduplication in data preprocessing
# pipelines where duplicate training samples are removed
# in-place to reduce dataset size before model training

class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
