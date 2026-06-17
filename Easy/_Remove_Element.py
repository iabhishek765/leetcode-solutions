# LC#27 - Remove Element
# Difficulty: Easy
# Topics: Array, Two Pointers
#
# Approach: Two pointers - k tracks position for next valid
#           element, overwrite in-place while scanning
# Time: O(n) | Space: O(1)
#
# ML Connection: Similar to filtering operations in data
# preprocessing where unwanted samples/labels are removed
# in-place from a dataset array before training

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
