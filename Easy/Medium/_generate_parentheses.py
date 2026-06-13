"""
Problem: Generate Parentheses (LC #22)
Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

Approach:
- Use backtracking to build all valid combinations
- Add '(' if open_count < n
- Add ')' only if close_count < open_count
- When string length = 2*n, add to result
- Time: O(4^n / sqrt(n)) | Space: O(n)

ML Connection:
- Backtracking is used in hyperparameter search
  (grid search) in ML model tuning
- Tree-based exploration here mirrors how decision
  trees explore splits during training
"""

class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result
