"""
Problem: Binary Tree Inorder Traversal (LC #94)
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Approach:
- Iterative DFS with an explicit stack
- Push nodes while moving left, pop to visit, then move right
- Order produced: left -> root -> right
- Time: O(n) | Space: O(h) where h = tree height

ML Connection:
- Inorder traversal of a BST returns values in sorted order,
  the same idea used when scanning split thresholds in
  decision tree training.
"""

class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
