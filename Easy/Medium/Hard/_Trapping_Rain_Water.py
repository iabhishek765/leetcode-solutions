"""
LC#42 - Trapping Rain Water [Hard]
Topic: Two Pointers
ML Connection: Tracking running max from both directions is similar to 
how forward/backward passes work in bidirectional models (e.g., 
BiLSTMs) — combining info from both ends of a sequence.
"""

class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
