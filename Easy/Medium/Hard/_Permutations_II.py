"""
LC#47 - Permutations II [Medium]
Topic: Backtracking + Deduplication
ML Connection: Deduplication during search mirrors pruning redundant 
hypotheses in beam search for NLP sequence generation.
"""

class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # skip duplicate: same value as previous, and previous not used in this branch
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
