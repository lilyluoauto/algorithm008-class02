# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-01 19:11
# IDE: PyCharm
# =========================================================
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

    def setNode(self,a,b):
        self.left = a
        self.right = b

class Solution:

    def lowestCommonAncestor_1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        递归，回溯
        算法：

        1.从根节点开始遍历树。
        2.如果当前节点本身是 p 或 q 中的一个，我们会将变量 mid 标记为 true，并继续搜索左右分支中的另一个节点。
        3.如果左分支或右分支中的任何一个返回 true，则表示在下面找到了两个节点中的一个。
        4.如果在遍历的任何点上，left、right 或者 mid 三个标记中的任意两个变为 true，这意味着我们找到了节点 p 和 q 的最近公共祖先。

        """
        # Variable to store LCA node.
        self.ans = None

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


    def lowestCommonAncestor_2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        使用父指针迭代:
        1.从根节点开始遍历树。
        2.在找到 p 和 q 之前，将父指针存储在字典中。
        3.一旦我们找到了 p 和 q，我们就可以使用父指针字典获得 p 的所有祖先，并添加到一个称为祖先的集合中。
        4.同样，我们遍历节点 q 的祖先。如果祖先存在于为 p 设置的祖先中，这意味着这是 p 和 q 之间的第一个公共祖先（同时向上遍历），因此这是 LCA 节点。
       """
        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q



    def lowestCommonAncestor_3(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Three static flags to keep track of post-order traversal.

        # Both left and right traversal pending for a node.
        # Indicates the nodes children are yet to be traversed.
        BOTH_PENDING = 2
        # Left traversal done.
        LEFT_DONE = 1
        # Both left and right traversal done for a node.
        # Indicates the node can be popped off the stack.
        BOTH_DONE = 0


        # Initialize the stack with the root node.
        stack = [(root, BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != BOTH_DONE:

                # If both child traversals are pending
                if parent_state == BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None

p = TreeNode(9)
q = TreeNode(11)
a =TreeNode(2,TreeNode(4,TreeNode(8),p),TreeNode(5,TreeNode(10),q))

b =TreeNode(3,TreeNode(6,TreeNode(12),TreeNode(13)),TreeNode(7,TreeNode(14),TreeNode(15)))

root = TreeNode(1,a,b)
print(root)


so = Solution()
ans = so.lowestCommonAncestor_2(root,a,q)
print(ans)
