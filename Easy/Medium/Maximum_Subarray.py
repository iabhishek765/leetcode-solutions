"""
LC#53 - Maximum Subarray [Medium]
Topic: Dynamic Programming / Kadane's Algorithm
ML Connection: Kadane's is used in time-series anomaly detection — 
finding the contiguous window with maximum signal deviation, and in 
reward shaping for RL agents.
"""

class Solution:
    def maxSubArray(self, nums: list) -> int:
        cur = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)

        return best
