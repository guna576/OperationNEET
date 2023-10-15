# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder, inorder):

        inMap = dict()

        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        root = self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)

        return root

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):

        if preStart > preEnd or inStart > inEnd:
            return None

        root = TreeNode(preorder[preStart])

        inRoot = inMap[root.val]
        numsLeft = inRoot - inStart

        root.left = self.build(preorder, preStart+1, preStart+numsLeft, inorder, inStart, inRoot-1, inMap)

        root.right = self.build(preorder, preStart+numsLeft+1, preEnd, inorder, inRoot+1, inEnd, inMap)

        return root
    

### MOst annoying


class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        root = TreeNode(pre[0])
        parent = root
        st = [parent]

        for x in pre[1:]:
            new = TreeNode(x)
            if new.val < parent.val:
                parent.left = new
            else:
                while st and st[-1].val < new.val:
                    parent = st.pop()
                parent.right = new
            st += [new]
            parent = new
        return root
    
# you did it almost, just use ll and parent/dummy node knowledge
# O(N) and O(N) stack