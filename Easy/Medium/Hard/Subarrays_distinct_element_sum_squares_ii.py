"""
Problem: Subarrays Distinct Element Sum of Squares II (LC #2916)
Difficulty: Hard
Link: https://leetcode.com/problems/subarrays-distinct-element-sum-squares-ii/

Approach:
- Use identity: when adding nums[j], subarrays starting after
  last occurrence of nums[j] gain +1 distinct count
- Track sum_d = sum of all distinct counts for subarrays ending at j
- Track sum_sq = sum of squares using: new_sq = old_sq + 2*sum_d + cnt
  derived from (d+1)^2 = d^2 + 2d + 1
- Time: O(n) | Space: O(n)

ML Connection:
- Incremental distinct counting is used in streaming ML
  where data arrives online and stats update in real-time
- The d^2 → (d+1)^2 update mirrors gradient accumulation
  in online learning algorithms like SGD with momentum
"""

class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        
        tree_d  = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy    = [0] * (4 * n)

        def push_down(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                d = lazy[node]
                
                left_len = mid - l + 1
                tree_sq[2*node]   = (tree_sq[2*node] + 2 * d * tree_d[2*node] + d * d * left_len) % MOD
                tree_d[2*node]    = (tree_d[2*node]  + d * left_len) % MOD
                lazy[2*node]      = (lazy[2*node] + d) % MOD
                right_len = r - mid
                tree_sq[2*node+1] = (tree_sq[2*node+1] + 2 * d * tree_d[2*node+1] + d * d * right_len) % MOD
                tree_d[2*node+1]  = (tree_d[2*node+1]  + d * right_len) % MOD
                lazy[2*node+1]    = (lazy[2*node+1] + d) % MOD
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql > qr: return
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sq[node] = (tree_sq[node] + 2 * tree_d[node] + length) % MOD
                tree_d[node]  = (tree_d[node]  + length) % MOD
                lazy[node]    = (lazy[node] + 1) % MOD
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid: update(2*node, l, mid, ql, qr)
            if qr > mid:  update(2*node+1, mid+1, r, ql, qr)
            tree_d[node]  = (tree_d[2*node]  + tree_d[2*node+1])  % MOD
            tree_sq[node] = (tree_sq[2*node] + tree_sq[2*node+1]) % MOD

        last = {}
        result = 0
        for j in range(n):
            prev = last.get(nums[j], -1)
            update(1, 0, n-1, prev+1, j)
            result = (result + tree_sq[1]) % MOD
            last[nums[j]] = j

        return result
