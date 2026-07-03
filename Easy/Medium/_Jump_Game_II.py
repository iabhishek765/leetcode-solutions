"""
LC#45 - Jump Game II [Medium]
Topic: Greedy
ML Connection: Greedy range expansion mirrors how beam search extends 
the most promising candidates at each step without backtracking.
"""

class Solution(object):
    def jump(self, nums):
        jumps = 0
        cur_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest

        return jumps
