# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def find(root,lb,ub):
            if not root: return True
            if root.val <= lb or root.val >= ub: return False
            return find(root.left,lb,root.val) and find(root.right,root.val,ub)

        return find(root,float('-inf'),float('inf'))
        

# Understand the concept of lowerbound and upperbound in BSTs