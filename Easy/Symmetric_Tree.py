# LC#101 - Symmetric Tree
# Difficulty: Easy
# Topics: Tree, DFS, BFS
#
# Approach: Recursive mirror check — compare left and right
#           subtrees simultaneously. At each level:
#           left.left ↔ right.right, left.right ↔ right.left
# Time: O(n) | Space: O(h)
#
# ML Connection: Symmetry detection in tree structures mirrors
# model architecture validation in neural networks where
# encoder-decoder symmetry is checked in U-Net and
# autoencoder architectures.

class Solution:
    def isSymmetric(self, root):
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    mirror(left.left, right.right) and
                    mirror(left.right, right.left))
        
        return mirror(root.left, root.right)
