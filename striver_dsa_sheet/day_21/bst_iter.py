# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.push(root)

    def next(self) -> int:
        node = self.st.pop()
        if node.right: self.push(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.st) > 0
    def push(self,node) -> None:
        self.st += [node]
        while 1:
            if node.left:
                self.st += [node.left]
                node = node.left
            else:
                break
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()