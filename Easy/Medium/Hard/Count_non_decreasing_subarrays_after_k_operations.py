"""
Problem: Count Non-Decreasing Subarrays After K Operations (LC #3420)
Difficulty: Hard
Link: https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

Approach:
- Cost to make a subarray non-decreasing = sum(prefix max - element)
- Reverse the array so prefix max becomes suffix max
- Two pointers: cost grows when r extends, shrinks when l moves right
- Monotonic deque tracks suffix-max segments; maintain sum of maxes
  (sumM) and sum of elements (sumA), cost = sumM - sumA
- For each r, the smallest valid l gives r - l + 1 valid subarrays
- Time: O(n) | Space: O(n)

ML Connection:
- Monotonic stacks/deques that maintain running maxima are the same
  pattern as max-pooling over sliding windows in CNNs.
"""

from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        a = nums[::-1]
        dq = deque()
        l = 0
        sumM = 0
        sumA = 0
        ans = 0

        for r, v in enumerate(a):
            while dq and a[dq[-1]] <= v:
                j = dq.pop()
                prev = dq[-1] if dq else l - 1
                sumM -= a[j] * (j - prev)
            prev = dq[-1] if dq else l - 1
            sumM += v * (r - prev)
            dq.append(r)
            sumA += v

            while sumM - sumA > k:
                sumA -= a[l]
                sumM -= a[dq[0]]
                if dq[0] == l:
                    dq.popleft()
                l += 1

            ans += r - l + 1
        return ans
