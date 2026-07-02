"""
LC#3286 - Find a Safe Walk Through a Grid [Medium]
Topic: BFS / 0-1 BFS
ML Connection: Health-aware pathfinding is used in RL environments 
where agents have limited resources — same as constrained shortest 
path problems in robotics.
"""

from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        start_health = health - grid[0][0]
        
        if start_health <= 0:
            return False

        dq = deque([(0, 0, start_health)])
        visited[0][0] = start_health

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        while dq:
            r, c, hp = dq.popleft()

            if r == m-1 and c == n-1:
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_hp = hp - grid[nr][nc]
                    if new_hp > 0 and new_hp > visited[nr][nc]:
                        visited[nr][nc] = new_hp
                        dq.append((nr, nc, new_hp))

        return False
