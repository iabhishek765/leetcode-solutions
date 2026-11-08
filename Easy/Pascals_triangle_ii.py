"""
Problem: Pascal's Triangle II (LC #119)
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle-ii/

Approach:
- Keep a single row of length rowIndex + 1, filled with 1s
- For each row i, update j from i-1 down to 1: row[j] += row[j-1]
- Going right to left keeps row[j-1] as the previous row's value
- Time: O(k^2) | Space: O(k)

ML Connection:
- In-place updates to save memory is the same idea behind
  running averages and gradient accumulation over batches.
"""

class Solution:
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row
