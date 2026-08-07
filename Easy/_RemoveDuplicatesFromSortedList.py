"""
LC#83 - Remove Duplicates from Sorted List [Easy]
Topic: Linked List
ML Connection: Deduplication in sorted sequences is used in 
data preprocessing pipelines to remove redundant training samples.
"""

class Solution:
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
