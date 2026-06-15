# LC#25 - Reverse Nodes in k-Group
# Difficulty: Hard
# Topics: Linked List, Recursion
# 
# Approach: Recursion - check k nodes exist, reverse them,
#            recursively connect with next k-group
# Time: O(n) | Space: O(n/k)
#
# ML Connection: Sequential chunked processing is similar to
# how mini-batch gradient descent processes data in fixed-size 
# groups during neural network training

class Solution(object):
    def reverseKGroup(self, head, k):
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head
        
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(curr, k)
        return prev
