"""
Problem: Maximum Total Subarray Value I (LC #3689)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-total-subarray-value-i/

Approach:
- Value of subarray = max - min
- Since subarrays can overlap and repeat, just pick
  the best single subarray k times
- Find max (max - min) across all subarrays, multiply by k
- Time: O(n²) | Space: O(1)

ML Connection:
- Range-based feature extraction (max - min = range)
  is a standard normalization technique in ML preprocessing
- Used in MinMaxScaler which scales features to [0,1]
  before feeding into neural networks
"""

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)
        best = 0

        for l in range(n):
            cur_max = nums[l]
            cur_min = nums[l]
            for r in range(l, n):
                cur_max = max(cur_max, nums[r])
                cur_min = min(cur_min, nums[r])
                best = max(best, cur_max - cur_min)

        return best * k
