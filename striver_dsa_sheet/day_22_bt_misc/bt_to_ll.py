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

        if not root: return None 
        st = [root]
        while st:
            node = st.pop()
            if node.right: st += [node.right]
            if node.left: st += [node.left]
            if st:
                node.right = st[-1]
                node.left = None
        return root

        # using recursion
        # def dfs(node, prev):
        #     if not node: return 
        #     dfs(node.right,prev)
        #     dfs(node.left, prev)
        #     node.right = prev
        #     node.left = None
        #     prev = node
        # dfs(root, None)
        # if root: return root


        # morris traversal
        # if not root: return None 
        # curr = root
        # while curr:
        #     if curr.left:
        #         prev = curr.left
        #         while prev.right: prev = prev.right
        #         prev.right = curr.right
        #         curr.right = curr.left
        #         curr.left = None

        #     curr = curr.right
        # return root
    
# O(N) and O(1)

# rightmost in left subtree is connected to root's right and mve to root's right and do same
# morris TRaversal