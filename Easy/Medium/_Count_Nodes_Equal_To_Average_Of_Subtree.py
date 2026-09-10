"""
LC#2265 - Count Nodes Equal to Average of Subtree [Medium]
Topic: Binary Tree / DFS
ML Connection: Computing subtree aggregates bottom-up mirrors how 
gradient accumulation works in tree-structured neural networks 
(Tree-LSTMs) used in NLP for parsing.
"""

class Solution:
    def averageOfSubtree(self, root) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)  # (sum, count)

            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1

            if node.val == total_sum // total_cnt:
                self.count += 1

            return (total_sum, total_cnt)

        dfs(root)
        return self.count
