# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = [(root,0)]
        ans = 1   # This is the edge case, if single node is also a width=`1`
        while q:
            n = len(q)
            for _ in range(n):
                node,lv = q.pop(0)
                if lv > 0:
                    lv -= 1
                if node.left: q += [(node.left,2*lv+1)]
                if node.right: q += [(node.right,2*lv+2)]
            if len(q) > 1:
                ans = max(ans, q[-1][-1] - q[0][-1]+1)
        return ans
    

# You have to find width in levels, do level order traversal
# You can know the index 2*i+1,2*i+2 as childs with parents level i
