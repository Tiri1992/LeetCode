"""
Leetcode Question: Given a linked list, remove the n-th node from 
the end of list and return its head.


url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        NumberNodes = 0
        curr = head
        while curr:
            NumberNodes += 1
            curr = curr.next
        # Reset
        idx = NumberNodes - n
        curr_idx = 0
        curr = head
        prev = None
        while curr_idx != idx:
            prev = curr
            curr = curr.next
            # Iterate
            curr_idx += 1
        if prev:
            prev.next = curr.next
        else:
            # Element to remove is the first one
            # Shift head along by 1
            head = head.next
        return head
