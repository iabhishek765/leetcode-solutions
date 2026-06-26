"""
LC#3739 - Count Subarrays With Majority Element II [Hard]
Topic: Prefix Sum + Fenwick Tree (BIT) + Coordinate Compression
ML Connection: Counting "majority" patterns via running sums resembles 
how class-imbalance or vote-aggregation is checked in ensemble models 
(e.g., majority voting classifiers).
"""

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == target else -1)

        # Coordinate compression (safe for any value range)
        sorted_vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}  # 1-indexed

        size = len(sorted_vals)
        tree = [0] * (size + 1)

        def update(i):
            while i <= size:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        ans = 0
        for j in range(n + 1):
            r = rank[prefix[j]]
            ans += query(r - 1)  # count earlier prefixes strictly smaller
            update(r)

        return ans
