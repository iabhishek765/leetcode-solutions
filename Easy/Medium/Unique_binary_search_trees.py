"""
Problem: Unique Binary Search Trees (LC #96)
Difficulty: Medium
Link: https://leetcode.com/problems/unique-binary-search-trees/

Approach:
- dp[k] = number of BST shapes with k nodes
- Pick each i as root: left has i-1 nodes, right has k-i nodes
- dp[k] = sum(dp[i-1] * dp[k-i]) for i in 1..k
- This is the Catalan number sequence
- Time: O(n^2) | Space: O(n)

ML Connection:
- Counting tree structures shows why the search space of possible
  decision trees grows explosively, which is why training uses
  greedy splitting instead of trying every tree.
"""

class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        return dp[n]
