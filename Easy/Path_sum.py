"""
Problem: Path Sum (LC #112)
Difficulty: Easy
Link: https://leetcode.com/problems/path-sum/

Approach:
- Recursively subtract node value from targetSum
- At leaf node, check if remaining == 0
- Return True if any root-to-leaf path matches
- Time: O(n) | Space: O(h) where h = tree height

ML Connection:
- Root-to-leaf path traversal mirrors forward pass
  through a decision tree in ML inference
- Path sum check is exactly how decision tree leaf
  nodes accumulate feature splits to reach prediction
"""

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
