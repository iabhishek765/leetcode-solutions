"""
Problem: Sliding Window Maximum (LC #239)
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-maximum/

Approach:
- Monotonic deque stores indices in decreasing value order
- Front = max of current window
- Remove front when it goes out of window (index < i-k+1)
- Remove back when smaller than current element
- Time: O(n) | Space: O(k)

ML Connection:
- Sliding window max is used in max pooling layers
  in CNNs for feature map downsampling
- Monotonic deque pattern appears in efficient
  attention window computation in transformers
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
