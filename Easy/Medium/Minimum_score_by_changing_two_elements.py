"""
Problem: Minimum Score by Changing Two Elements (LC #2567)
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-score-by-changing-two-elements/

Approach:
- Changing two elements lets the low score become 0 (copy a neighbor)
- So only minimize the high score (max - min) after the change
- Sort; the best change removes two extremes. Try the 3 options:
  two largest, two smallest, or one of each
- Time: O(n log n) | Space: O(1)

ML Connection:
- Trimming extreme values to shrink the range is the idea behind
  outlier clipping/winsorizing before feature scaling.
"""

class Solution:
    def minimizeSum(self, nums):
        nums.sort()
        n = len(nums)
        return min(nums[n-3] - nums[0],
                   nums[n-2] - nums[1],
                   nums[n-1] - nums[2])
