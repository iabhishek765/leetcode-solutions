"""
Problem: Merge K Sorted Lists (LC #23)
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Approach:
- Use a min heap to track the smallest node across all lists
- Push (value, index, node) into heap — index breaks tie
- Pop minimum, attach to result, push next node from same list
- Time: O(n log k) | Space: O(k)
  where n = total nodes, k = number of lists

ML Connection:
- Min heap based k-way merge is used in external sorting
  of large ML datasets that don't fit in memory
- Priority queues appear in beam search algorithm used
  in sequence generation tasks like text summarization
"""

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
