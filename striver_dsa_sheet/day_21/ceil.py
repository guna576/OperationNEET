def findCeil(root, x):
    # Write your code here.
    ceil = -1

    while root:
        if root.data >= x:
            ceil = root.data 
            root = root.left 
        elif root.data < x:
            root = root.right
    return ceil

# O(H) and O(1)

# https://www.codingninjas.com/studio/problems/ceil-from-bst_920464?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTab=0