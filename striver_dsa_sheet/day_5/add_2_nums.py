# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        dummy = curr = ListNode()
        while a or b:
            n1,n2 = 0,0
            if a:
                n1 = a.val
                a = a.next 
            if b:
                n2 = b.val
                b = b.next
            ans = n1+n2 + c
            c = ans//10
            curr.next = ListNode(ans%10)
            curr = curr.next
        if c:
            curr.next = ListNode(c)
        return dummy.next
        

# If you are dealing with two lists and have to merge kind of work, Use dummy node first
# https://leetcode.com/problems/add-two-numbers/description/
                
