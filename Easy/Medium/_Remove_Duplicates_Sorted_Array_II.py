# LC#80 - Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Topics: Array, Two Pointers
#
# Approach: Write pointer k tracks valid position.
#           Allow element if k<2 (first two always ok)
#           OR current != nums[k-2] (not a 3rd duplicate).
#           Comparing with k-2 ensures at most 2 copies kept.
# Time: O(n) | Space: O(1)
#
# ML Connection: In-place data deduplication with frequency
# limits mirrors dataset cleaning pipelines where oversampled
# classes are capped at a maximum count to prevent bias
# in imbalanced classification models

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1
        return k
