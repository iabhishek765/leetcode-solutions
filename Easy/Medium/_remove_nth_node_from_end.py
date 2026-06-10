"""
Problem: Remove Nth Node From End of List (LC #19)
Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Approach:
- Use two pointers (ptr and temp) starting at head
- Move ptr n steps ahead first
- If ptr is None, remove head (edge case)
- Move both pointers until ptr.next is None
- temp is now just before the target node — skip it
- Time: O(n) | Space: O(1)

ML Connection:
- Two pointer / sliding window on linked structures
  mirrors attention window mechanisms in transformers
- Fixed-gap pointer technique used in sequence
  processing pipelines for NLP data streams
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = temp = head

        for _ in range(n):
            ptr = ptr.next

        if not ptr:
            return head.next

        while ptr.next:
            ptr = ptr.next
            temp = temp.next

        temp.next = temp.next.next
        return head
