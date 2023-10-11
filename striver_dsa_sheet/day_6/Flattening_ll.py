
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        

def merge(root, root1):
    dummy = res = Node(0)
    dummy.bottom = root
    while root and root1:
        if root.data <= root1.data:
            dummy.bottom = root
            root = root.bottom
        else:
            dummy.bottom = root1
            root1 = root1.bottom
        dummy = dummy.bottom
    while root:
        dummy.bottom = root
        root = root.bottom
        dummy = dummy.bottom
    while root1:
        dummy.bottom = root1
        root1 = root1.bottom
        dummy = dummy.bottom
        
    res.bottom.next = None
    return res.bottom
    
def flatten(root):
    #Your code here
    if not root.next:
        return root
    root1 = flatten(root.next)
    newRoot = merge(root,root1)
    return newRoot
    
# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

# You want a single list out of so many lists, means you need to merge and make it one.
# Just like merge sort, do it one after other
# come from right and combine and return untill single list is generated