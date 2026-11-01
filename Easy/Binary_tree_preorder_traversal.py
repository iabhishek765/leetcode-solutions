"""
Problem: Binary Tree Preorder Traversal (LC #144)
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

Approach:
- Iterative DFS with an explicit stack
- Pop a node, record its value, push right then left
- Left is popped first, giving root -> left -> right order
- Time: O(n) | Space: O(h) where h = tree height

ML Connection:
- Preorder traversal is how a decision tree is walked
  from root to leaves during model inference
- Tree serialization (saving trained trees) commonly
  uses preorder order
"""

class Solution:
    def preorderTraversal(self, root):
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
