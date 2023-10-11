# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        fast,slow = head, head
        for _ in range(n):
            fast = fast.next
        prev = None
        while fast:
            fast = fast.next 
            prev = slow
            slow = slow.next
        if slow == head: return head.next
        prev.next = slow.next
        return head
            
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/