"""
Problem: The Skyline Problem (LC #218)
Difficulty: Hard
Link: https://leetcode.com/problems/the-skyline-problem/

Approach:
- Create events: (x, -height, end) for starts, (x, 0, 0) for ends
- Sort events, use max heap to track active building heights
- At each x, pop expired buildings, check if max height changed
- Record keypoint when height changes
- Time: O(n log n) | Space: O(n)

ML Connection:
- Event-driven processing mirrors time-series feature
  extraction used in anomaly detection ML models
- Max heap for active intervals is used in scheduling
  algorithms for ML training job management on clusters
"""

import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))

        events.sort()
        result = []
        heap = [(0, float('inf'))]
        prev_max = 0

        for x, neg_h, r in events:
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))

            while heap[0][1] <= x:
                heapq.heappop(heap)

            curr_max = -heap[0][0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result
