# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        q = [root]
        ans = [[root.val]]
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if node.left: q += [node.left]
                if node.right: q += [node.right]
            
            ans += [[x.val for x in q]]

        return [x for x in ans if len(x)]
    
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/