# #include <bits/stdc++.h>

# using namespace std;

# struct node {
#   int data;
#   struct node * left, * right;
# };

# void reorder(node * root) {
#   if (root == NULL) return;
#   int child = 0;
#   if (root -> left) {
#     child += root -> left -> data;
#   }
#   if (root -> right) {
#     child += root -> right -> data;
#   }

#   if (child < root -> data) {
#     if (root -> left) root -> left -> data = root -> data;
#     else if (root -> right) root -> right -> data = root -> data;
#   }

#   reorder(root -> left);
#   reorder(root -> right);

#   int tot = 0;
#   if (root -> left) tot += root -> left -> data;
#   if (root -> right) tot += root -> right -> data;
#   if (root -> left || root -> right) root -> data = tot;
# }
# void changeTree(node * root) {
#   reorder(root);
# }

# struct node * newNode(int data) {
#   struct node * node = (struct node * ) malloc(sizeof(struct node));
#   node -> data = data;
#   node -> left = NULL;
#   node -> right = NULL;

#   return (node);
# }

# int main() {

#   struct node * root = newNode(2);
#   root -> left = newNode(35);
#   root -> left -> left = newNode(2);
#   root -> left -> right = newNode(3);
#   root -> right = newNode(10);
#   root -> right -> left = newNode(5);
#   root -> right -> right = newNode(2);

#   changeTree(root);

#   return 0;
# }



    # if not root: return 0
    # def reorder(root):
    #     if not root: return 

    #     rootSum = 0

    #     if root.left: rootSum += root.left.data 
    #     if root.right: rootSum += root.right.data  

    #     if rootSum < root.data:
    #         if root.left: root.left.data = root.data 
    #         elif root.right: root.right.data = root.data  
    #     reorder(root.left)
    #     reorder(root.right)

    #     wsum = 0
    #     if root.left: wsum += root.left.data 
    #     if root.right: wsum += root.right.data 
    #     if root.left or root.right: root.data = wsum

    # reorder(root)
    # return root



### https://www.codingninjas.com/studio/problems/children-sum-property_8357239?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=3