"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d_clone = {}
        def clone(node):
            if node in d_clone:
                return d_clone[node]
            copy = Node(node.val)
            d_clone[node] = copy
            for x in node.neighbors:
                copy.neighbors += [clone(x)]
            return copy


        return clone(node) if node else node

        # if not root: return None 
        # que = [root]
        # d = {root.val:Node(root.val,[])} # To get the cloned Node references

        # while que:
        #     node = que.pop(0)
        #     node_clone = d[node.val] # Getting the references
        #     for x in node.neighbors:
        #         if x.val not in d:
        #             d[x.val] = Node(x.val,[])
        #             que += [x]
        #         node_clone.neighbors += [d[x.val]] # only adding the cloned references to neighbors
        # return d[root.val]



# BFS: O(V+E) and O(V) Map + Que
        

                