"""
Problem: Number of Ways to Assign Edge Weights II (LC #3559)
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

Approach:
- Build tree and find depth + parent using BFS
- Use binary lifting for O(log n) LCA queries
- For each query (u,v): path_len = depth[u] + depth[v] - 2*depth[LCA]
- Answer = 2^(path_len - 1) mod 10^9+7
- Time: O(n log n + q log n) | Space: O(n log n)

ML Connection:
- LCA on trees is used in hierarchical clustering
  which groups data points in ML unsupervised learning
- Binary lifting (sparse table) is a preprocessing
  technique similar to feature caching in ML pipelines
"""

import sys
from collections import defaultdict, deque
sys.setrecursionlimit(100000)

class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 17
        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]

        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True

        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    queue.append(nei)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k-1][parent[k-1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        result = []
        for u, v in queries:
            if u == v:
                result.append(0)
                continue
            l = lca(u, v)
            path_len = depth[u] + depth[v] - 2 * depth[l]
            result.append(pow(2, path_len - 1, MOD))

        return result
