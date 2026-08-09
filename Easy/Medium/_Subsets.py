"""
LC#78 - Subsets [Medium]
Topic: Backtracking / Bit Manipulation
ML Connection: Power set generation is used in feature selection — 
evaluating all possible feature subsets to find optimal combinations 
for model training.
"""

class Solution:
    def subsets(self, nums: list) -> list:
        result = []

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
