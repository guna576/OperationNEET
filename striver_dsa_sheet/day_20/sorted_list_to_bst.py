# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
   
        def build(nums, i, j):
            if i > j: return None 
            m = (i+j)//2
            root = TreeNode(nums[m])
            root.left = build(nums,i,m-1)
            root.right = build(nums,m+1,j)
            return root

        return build(nums,0,len(nums)-1)
         
# Just a binary search with recursion
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/