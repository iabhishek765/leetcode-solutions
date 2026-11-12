"""
Problem: Longest Strictly Increasing or Strictly Decreasing Subarray (LC #3105)
Difficulty: Easy
Link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

Approach:
- Scan once, tracking the length of the current increasing run (inc)
  and decreasing run (dec)
- Larger than previous: inc += 1, dec resets to 1
- Smaller than previous: dec += 1, inc resets to 1
- Equal: both reset to 1
- Answer is the maximum run length seen
- Time: O(n) | Space: O(1)

ML Connection:
- Detecting monotonic runs is a simple trend feature in time-series
  data, e.g. consecutive rising or falling loss values across epochs.
"""

class Solution:
    def longestMonotonicSubarray(self, nums):
        best = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best
