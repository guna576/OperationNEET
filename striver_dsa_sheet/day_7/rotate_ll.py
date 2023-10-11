# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        c = 0
        tmp = head
        while tmp:
            c += 1
            tmp = tmp.next
        k %= c 
        tmp = head
        if k==0:
            return head
        z = c-k # You are doing mistake here
        while z:
            z -= 1
            sl = tmp
            tmp = tmp.next
        sl.next = None 
        newHead = tmp
        while tmp.next: tmp = tmp.next
        tmp.next = head 
        return newHead


# https://leetcode.com/problems/rotate-list/description/
# Thing is you have to travl to that point and cut the link and ad the edge link