from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r = start_c = 0
        litter_map = {}
        
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_r, start_c = r, c
                elif cell == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        total_litter = len(litter_map)
        if total_litter == 0:
            return 0
        
        target_mask = (1 << total_litter) - 1
        
        # queue stores: (row, col, remaining_energy, collected_mask, moves)
        queue = deque([(start_r, start_c, energy, 0, 0)])
        
        # max_energy_seen[r][c][mask] = highest energy remaining at this (r, c, mask)
        max_energy_seen = {}
        max_energy_seen[(start_r, start_c, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()
            
            if mask == target_mask:
                return moves
            
            if curr_energy == 0:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    cell = classroom[nr][nc]
                    if cell == 'X':
                        continue
                    
                    next_energy = curr_energy - 1
                    next_mask = mask
                    
                    if cell == 'R':
                        next_energy = energy
                    elif cell == 'L':
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    state = (nr, nc, next_mask)
                    if state not in max_energy_seen or max_energy_seen[state] < next_energy:
                        max_energy_seen[state] = next_energy
                        queue.append((nr, nc, next_energy, next_mask, moves + 1))
                        
        return -1
