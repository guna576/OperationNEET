# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def flat(root):
            if not root: return 
            nonlocal prev 
            flat(root.right)
            flat(root.left)
            root.right = prev
            root.left = None
            prev = root

        flat(root)
        return root
        
## This is Using Recursion so, SC : O(N) and remember anything need to flatten, we have solve from the right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        st = [root]
        while len(st):
            curr = st.pop()
            if curr.right: st += [curr.right]
            if curr.left: st += [curr.left]
            if len(st): curr.right = st[-1]
            curr.left = None

        return root
    
# SImilar to recursion but using stack; we can use the queue also

