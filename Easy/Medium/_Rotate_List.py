# LC#61 - Rotate List
# Difficulty: Medium
# Topics: Linked List, Two Pointers
#
# Approach: Get length + tail, k = k%length to handle
#           large k. Make circular, break at (length-k-1)th
#           node to get new head
# Time: O(n) | Space: O(1)
#
# ML Connection: Circular buffer rotation is used in
# experience replay buffers in reinforcement learning
# where older experiences are replaced by newer ones

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
