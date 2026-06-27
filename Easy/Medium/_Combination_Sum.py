"""
LC#39 - Combination Sum [Medium]
Topic: Backtracking
ML Connection: Exploring combinations with pruning is the same search 
strategy used in hyperparameter search spaces (e.g., grid/random search 
with early stopping on invalid configs).
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # sorted, so no point checking further

                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])  # i, not i+1: reuse allowed
                path.pop()

        backtrack(0, target)
        return result
