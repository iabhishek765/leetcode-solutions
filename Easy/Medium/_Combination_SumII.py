"""
LC#40 - Combination Sum II [Medium]
Topic: Backtracking
ML Connection: Skipping duplicate branches during search is the same 
idea as deduplication in beam search, avoiding redundant exploration 
of equivalent paths.
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicate at same recursion level

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # i+1: no reuse
                path.pop()

        backtrack(0, target)
        return result
