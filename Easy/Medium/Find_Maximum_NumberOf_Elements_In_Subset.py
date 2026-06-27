"""
LC#3020 - Find the Maximum Number of Elements in Subset [Medium]
Topic: Hash Map / Greedy Chain Building
ML Connection: Building chains via repeated squaring resembles how 
exponential growth patterns (e.g., learning rate schedules, power-law 
features) are detected and validated in data preprocessing.
"""

from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        if 1 in cnt:
            ones = cnt[1]
            ans = ones if ones % 2 == 1 else ones - 1
            del cnt[1]

        for x in sorted(cnt.keys()):
            if x not in cnt:
                continue

            length = 0
            cur = x
            while cur in cnt and cnt[cur] >= 2:
                length += 1
                nxt = cur * cur
                del cnt[cur]
                cur = nxt

            if cur in cnt:
                total = 2 * length + 1
                del cnt[cur]
            else:
                total = 2 * length - 1

            ans = max(ans, total)

        return ans
