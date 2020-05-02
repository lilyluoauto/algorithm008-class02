# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-25 12:42
# IDE: PyCharm
# =========================================================
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal_1(self, root: TreeNode):
        '''递归调用'''
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res

    def preorderTraversal_2(self, root: TreeNode):
        """迭代调用"""

        if not root:
            return []

        stack,output = [root,],[]
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return output

    def inorderTraversal_1(self, root: TreeNode) -> list[int]:
        """recursive
        时间： 52 ms 很慢
        """
        res = []
        if not root:
            return []

        def helper(root):
            if root.left is not None:
                helper(root.left)
            res.append(root.val)
            if root.right is not None:
                helper(root.right)
        helper(root)
        return res

    def inorderTraversal_2(self, root: TreeNode) -> list[int]:
        """iterator
        时间：
        """
        curr = root
        stack,output = [],[]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output

    def inorderTraversal_3(self, root: TreeNode) -> list[int]:
        '''使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
    如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
    如果遇到的节点为灰色，则将节点的值输出。
    '''

        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def postorder_1(self, root) -> list[int]:
        """binary tree post order
        递归调用"""
        res = []
        if not root:
            return []

        def helper(root):
            res.append(root.val)
            if root.right is not None:
                helper(root.right)
            if root.left is not None:
                helper(root.left)

        helper(root)
        return res[::-1]

    def postorder_2(self, root) -> list[int]:
        """binary tree post order
        递归调用"""
        res = []
        if not root:
            return []

        def helper(root):

            if root.left is not None:
                helper(root.left)
            if root.right is not None:
                helper(root.right)
            res.append(root.val)

        helper(root)
        return res

    def postorder_3(self, root) -> list[int]:
        """binary tree post order
        迭代调用"""
        res = []
        if not root:
            return []
        stack = [root,]

        while stack:
            node = stack.pop()

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            res.append(node.val)

        return res[::-1]







if __name__ == "__main__":
    root = [1,None,2,3]
    so = Solution()
    l = so.preorderTraversal_2(root)
    print(l)



