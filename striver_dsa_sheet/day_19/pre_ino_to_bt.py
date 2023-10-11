# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        d = dict()
        for i,j in enumerate(ino):
            d[j] = i
        
        def build(pre,p,q,ino,i,j):
            nonlocal d
            if p > q or i > j: return None
            node = TreeNode(pre[p])
            ind = d[node.val]
            nl = ind - i ## This is the key as left elements to root only goes to left call and vice versa
            node.left = build(pre,p+1,p+nl,ino,i,ind-1)
            node.right = build(pre,p+nl+1,q,ino,ind+1,j)

            return node

        return build(pre,0,len(pre)-1,ino,0,len(ino)-1)
    
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
    
