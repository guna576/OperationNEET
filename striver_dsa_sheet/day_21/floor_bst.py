def floorInBST(root, X):
    # Write your Code here.

    succ = 0
    while root:
        if root.data > X:
            root = root.left 
        elif root.data <= X:
            succ = root.data
            root = root.right
            
    # print(succ)
    return succ

# https://www.codingninjas.com/studio/problems/floor-from-bst_920457?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTab=0