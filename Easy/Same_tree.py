"""
Problem: Same Tree (LC #100)
Difficulty: Easy
Link: https://leetcode.com/problems/same-tree/

Approach:
- Recursively check if both nodes are None → True
- If one is None and other isn't → False
- If values differ → False
- Recursively check left and right subtrees
- Time: O(n) | Space: O(h) where h = tree height

ML Connection:
- Tree comparison is used in decision tree ensembles
  to check for duplicate trees in Random Forests
- Recursive structure mirrors computation graphs
  in PyTorch used for autograd/backpropagation
"""

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
