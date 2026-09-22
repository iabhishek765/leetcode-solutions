# LC#124 - Binary Tree Maximum Path Sum
# Difficulty: Hard
# Topics: Tree, DFS, Dynamic Programming
#
# Approach: Post-order DFS. At each node:
#   1. Get max gain from left/right (clamp to 0 if negative)
#   2. Update global max with left + node + right (through path)
#   3. Return node + max(left, right) as single arm to parent
# Time: O(n) | Space: O(h)
#
# ML Connection: This tree DP pattern mirrors backpropagation
# in neural networks — each node computes its local contribution
# and passes a signal upward to its parent node.

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum
