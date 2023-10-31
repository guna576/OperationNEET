# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""

        s = ""
        que = [root]
        while que:
            node = que.pop(0)
            if node == None:
                s += "#,"
            else:
                s += str(node.val) + ","
                que += [node.left]
                que += [node.right]
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        data = data.split(",")
        head = root = TreeNode(int(data[0]))
        que = [root]
        i = 1
        while que:
            root = que.pop(0)
            if data[i] == "#":
                root.left = None
            else:
                root.left = TreeNode(int(data[i]))
                que += [root.left]
            i += 1
            if data[i] == "#":
                root.right = None 
            else:
                root.right = TreeNode(int(data[i]))
                que += [root.right]
            i += 1
        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))