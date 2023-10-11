# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        # if not a.next or not b.next: return None
        c1,c2 = 0,0
        curr1 = a
        curr2 = b
        while curr1:
            c1 += 1 
            curr1 = curr1.next
        while curr2:
            c2 += 1
            curr2 = curr2.next
        h1 = a if c1 >= c2 else b
        h2 = a if c1 < c2 else b
      
        diff = abs(c1-c2)
        # print(c1,c2,diff)
        while diff:
            h1 = h1.next
            diff -= 1
        # print(h1.val,h2.val)
        while h1 and h2:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        return None


# All good but faiiling the basic test case dont know why
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Working after removing the base condition