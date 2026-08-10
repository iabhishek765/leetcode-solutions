"""
LC#79 - Word Search [Medium]
Topic: DFS / Backtracking
ML Connection: Grid-based DFS is used in CNN receptive field analysis 
and in pathfinding for robotics — exploring reachable spatial regions.
"""

class Solution:
    def exist(self, board: list, word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False

            temp = board[r][c]
            board[r][c] = '#'  # mark visited

            found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))

            board[r][c] = temp  # restore
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
