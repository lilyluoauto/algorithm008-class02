# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-25 07:32
# IDE: PyCharm
# =========================================================

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None

# # java
# public class TreeNode{
# public int val;
# public TreeNode left,right;
# public TreeNode(int val){
# this.val = val;
# this.left = null;
# this.right = null;
# }
#     }

    def preorder(self, root):

      if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
      if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)
    def postorder(self, root):
      if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)


