# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, ino: List[int], pos: List[int]) -> Optional[TreeNode]:
        d = dict()
        for i,j in enumerate(ino):
            d[j] = i

        def build(pos,p,q,ino,i,j):
            nonlocal d
            if i > j or p > q: return None
            root = TreeNode(pos[q])
            ind = d[root.val]
            nr = ind - i

            root.left = build(pos,p,p+nr-1,ino,i,ind-1)
            root.right = build(pos,p+nr,q-1,ino,ind+1,j)

            return root

        return build(pos,0,len(pos)-1, ino,0,len(ino)-1)



# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# It's just like pre and Ino but post order comes from last

