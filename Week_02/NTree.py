# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-25 11:06
# IDE: PyCharm
# =========================================================
"""
# Definition for a Node.
"""
from collections import deque, defaultdict


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def preorder_1(self, root: 'Node'):
        '''recursive'''

        traverse_path = []
        def helper(root):
            if not root:
                return

            traverse_path.append(root.val)
            for child in root.children:
                helper(child)

        helper(root)
        return traverse_path

    def preorder_2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        迭代：由于递归实现 N 叉树的前序遍历较为简单，因此我们只讲解如何使用迭代的方法得到 N 叉树的前序遍历。

        我们使用一个栈来帮助我们得到前序遍历，需要保证栈顶的节点就是我们当前遍历到的节点。
        我们首先把根节点入栈，因为根节点是前序遍历中的第一个节点。
        随后每次我们从栈顶取出一个节点 u，它是我们当前遍历到的节点，并把 u 的所有子节点逆序推入栈中。
        例如 u 的子节点从左到右为 v1, v2, v3，那么推入栈的顺序应当为 v3, v2, v1，
        这样就保证了下一个遍历到的节点（即 u 的第一个子节点 v1）出现在栈顶的位置。
       """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output

    def levelOrder_1(self, root: 'Node') -> list[list[int]]:
        '''迭代'''

        if root is None:
            return []
        q = deque([root])
        output = []
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)
                q.extend(curr.children)
            output.append(level)
        return output

    def levelOrder_2(self, root: 'Node') -> list[list[int]]:
        ''' 递归'''
        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            resultdic[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []
        #可以用defaultdict来做
        resultdic = defaultdict(list)

        if root is not None:
            traverse_node(root, 0)
        # return result
        return list(resultdic.values())

    def postOrder_1(self, root: 'Node') -> list[list[int]]:
        ''' 递归
        68 ms 很慢，需要优化'''
        output = deque()
        def traverse_node(node):
            output.appendleft(node.val)
            if node.children is not None:
                for child in node.children[::-1]:
                    traverse_node(child)

        if root is None:
            return []
        if root is not None:
            traverse_node(root)

        return output

    def postOrder_2(self, root: 'Node') -> list[list[int]]:
        ''' 迭代
        '''
        if root is None:
            return []
        stack = [root,]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.children is not None:
                stack.extend(node.children)
        return output[::-1]

    

if __name__ == "__main__":
    children1 = Node(4)
    children2 = Node(3,children1)
    children3 = [Node(6),Node(1),children2,None]
    children4 = Node(7)
    # root = Node(5,children2)
    root = Node(5, children3)

    so = Solution()
    l = so.preorder_1(root)
    print(l)

    dequ




