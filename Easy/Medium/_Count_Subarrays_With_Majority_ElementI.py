"""
LC#3737 - Count Subarrays With Majority Element I [Medium]
Topic: Prefix Sum + Fenwick Tree (BIT)
ML Connection: Counting "majority" patterns via running sums resembles 
how class-imbalance or vote-aggregation is checked in ensemble models 
(e.g., majority voting classifiers).
"""

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        # score[i] = +1 if nums[i]==target else -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == target else -1)

        # shift values to fit Fenwick Tree indices (1-indexed, no zero/negatives)
        offset = n + 1
        size = 2 * n + 3
        tree = [0] * (size + 1)

        def update(i):
            i += 1  # 1-indexed
            while i <= size:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        ans = 0
        for j in range(n + 1):
            p = prefix[j] + offset
            # count previous prefixes < p (strictly smaller, since we need prefix[j] > prefix[i])
            ans += query(p - 1)
            update(p)

        return ans
