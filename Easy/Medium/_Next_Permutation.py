# LC#31 - Next Permutation
# Difficulty: Medium
# Topics: Array, Two Pointers
#
# Approach: Find rightmost ascending pair (pivot), swap with
#           rightmost element greater than pivot, then reverse
#           the suffix to get smallest possible arrangement
# Time: O(n) | Space: O(1)
#
# ML Connection: Generating ordered sequences relates to beam
# search decoding in sequence models, where candidates are
# systematically explored in a specific lexicographic-like order

class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
