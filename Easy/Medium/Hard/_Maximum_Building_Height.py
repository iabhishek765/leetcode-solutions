# LC#1840 - Maximum Building Height
# Difficulty: Hard
# Topics: Array, Greedy, Sorting
#
# Approach: Add boundary constraints (building 1 = height 0,
#           building n = infinity). Two-pass tightening of max
#           heights (left->right, then right->left) based on
#           adjacent slope constraint. Then compute peak height
#           achievable in each gap using triangle inequality:
#           peak = (h1 + h2 + gap) / 2
# Time: O(m log m) | Space: O(m)
#
# ML Connection: This constraint propagation pattern (tighten
# bounds from both directions) mirrors message passing in
# graphical models / belief propagation, where node values are
# iteratively constrained by neighboring node values

class Solution(object):
    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])
        restrictions.append([n, float('inf')])
        restrictions.sort()
        
        m = len(restrictions)
        
        for i in range(1, m):
            id_prev, h_prev = restrictions[i-1]
            id_curr, h_curr = restrictions[i]
            restrictions[i][1] = min(h_curr, h_prev + (id_curr - id_prev))
        
        for i in range(m - 2, -1, -1):
            id_curr, h_curr = restrictions[i]
            id_next, h_next = restrictions[i+1]
            restrictions[i][1] = min(h_curr, h_next + (id_next - id_curr))
        
        max_height = 0
        for i in range(1, m):
            id_prev, h_prev = restrictions[i-1]
            id_curr, h_curr = restrictions[i]
            gap = id_curr - id_prev
            peak = (h_prev + h_curr + gap) // 2
            max_height = max(max_height, peak)
        
        return max_height
