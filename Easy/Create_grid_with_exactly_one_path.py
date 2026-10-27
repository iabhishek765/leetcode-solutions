"""
Problem: Create Grid With Exactly One Path (LC #3963)
Difficulty: Easy
Link: https://leetcode.com/problems/create-grid-with-exactly-one-path/

Approach:
- Fill top row with '.' (go all right)
- Fill rightmost column with '.' (go all down)
- Everything else is '#'
- This creates exactly one L-shaped path: right then down
- Time: O(m*n) | Space: O(m*n)

ML Connection:
- Grid path problems model state-space search used in
  reinforcement learning environment design
- Single-path constraint mirrors Markov chain design
  where only one transition sequence is valid
"""

class Solution:
    def createGrid(self, m, n):
        grid = [['#'] * n for _ in range(m)]
        for j in range(n):
            grid[0][j] = '.'
        for i in range(m):
            grid[i][n-1] = '.'
        return [''.join(row) for row in grid]
