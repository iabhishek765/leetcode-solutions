# LC#2095 - Delete the Middle Node of a Linked List
# Difficulty: Medium
# Topics: Linked List, Two Pointers
#
# Approach: Slow/Fast pointer - fast starts 2 ahead,
#           when fast ends, slow is just before middle
# Time: O(n) | Space: O(1)
#
# ML Connection: Two-pointer technique is used in sliding
# window attention mechanisms in transformer models to
# efficiently track context boundaries

class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return head
