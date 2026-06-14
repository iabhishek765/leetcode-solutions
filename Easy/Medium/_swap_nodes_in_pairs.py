"""
Problem: Swap Nodes in Pairs (LC #24)
Difficulty: Medium
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Approach:
- Use dummy node before head to simplify edge cases
- For each pair (a, b): point prev→b, b→a, a→next pair
- Move prev to a (which is now second in pair)
- Time: O(n) | Space: O(1)

ML Connection:
- In-place pointer manipulation is used in memory
  efficient data loaders for large ML training pipelines
- Pair-wise operations appear in contrastive learning
  where pairs of samples are compared during training
"""
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next

            prev.next = b
            a.next = b.next
            b.next = a
            prev = a

        return dummy.next
