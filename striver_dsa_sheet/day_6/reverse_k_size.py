# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        c = 0
        tmp = head

        while tmp:
            c += 1
            tmp = tmp.next
        
        dummy = ListNode()
        dummy.next = head
    
        prev = cur = nex = dummy
        while k <= c:
            cur = prev.next
            nex = cur.next
            for _ in range(1,k):
                cur.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = cur.next
            c -= k
            prev = cur
        return dummy.next

# https://leetcode.com/problems/reverse-nodes-in-k-group/description/