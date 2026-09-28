# LC#98 - Validate Binary Search Tree
# Difficulty: Medium
# Topics: Tree, DFS, Binary Search Tree
#
# Approach: Recursive DFS with valid range (min, max).
#           Each node must satisfy min < node.val < max.
#           Left child → update max to node.val.
#           Right child → update min to node.val.
# Time: O(n) | Space: O(h)
#
# ML Connection: BST validation mirrors constraint checking
# in decision tree algorithms where split conditions must
# maintain strict ordering of feature thresholds at each node.

class Solution:
    def isValidBST(self, root):
        def validate(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
