# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        preorder = []
        curr = root

        while curr:
            if not curr.left:
                inorder += [curr.val]
                preorder += [curr.val]
                curr = curr.right
            else:
                prev = curr.left

                while prev.right and prev.right != curr:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = curr
                    preorder += [curr.val]
                    curr = curr.left
                else:
                    prev.right = None
                    inorder += [curr.val]
                    curr = curr.right
        return inorder,preorder
        
# You are connecting right most child in the left substree to root (Just like Recursion is doing)
# This traversal optmizes the space O(n) to O(1)



class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None 
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right: prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
        return root
    
# Morris TRaversal
# Go to the last right node in left subtree and connect it's right to root's right
# Then connect root's left to root's right and move to right and do the same in loop
# Need to remember