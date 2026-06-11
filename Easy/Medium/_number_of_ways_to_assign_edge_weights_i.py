"""
Problem: Number of Ways to Assign Edge Weights I (LC #3558)
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

Approach:
- Find the maximum depth of the tree from root (node 1) using DFS
- The path from root to deepest node has 'depth' edges
- Each edge can be 1 or 2, we need odd total cost
- Number of ways to get odd sum = 2^(depth-1)
- Multiply res by 2 for each edge in path (depth times)
- Time: O(n) | Space: O(n)

ML Connection:
- DFS on trees is used in decision tree traversal
  which is the core of Random Forest and XGBoost models
- Modular arithmetic used here appears in hash functions
  used for feature hashing in large-scale ML systems
"""

class Solution:
    MOD = 10**9 + 7

    def dfs(self, adj, node, par):
        depth = 0
        for child in adj[node]:
            if child == par:
                continue
            depth = max(depth, 1 + self.dfs(adj, child, node))
        return depth

    def assignEdgeWeights(self, edges):
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = self.dfs(adj, 1, -1)

        res = 1
        for _ in range(1, depth):
            res = (res * 2) % self.MOD

        return res
