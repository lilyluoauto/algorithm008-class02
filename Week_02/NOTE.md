学习笔记:
# 1. Tree:
* 二叉树是左右子树，二叉树搜索树是有序的二叉树，left< node< right
* N叉树的层序遍历迭代方式使用的是队列进行的（不是栈）
* 树的遍历有前序，中序和后序遍历,方式有深度优先和广度优先

![树的遍历方式](/Users/lilyluo/Documents/project/algorithm008-class02/Week_02/treeTraverse.png,"method of tranverse of tree")

* BFS （广度优先）
我们按照高度顺序一层一层的访问整棵树，高层次的节点将会比低层次的节点先被访问到

* DFS （ 深度优先）
在这个策略中，我们采用深度作为优先级，以便从跟开始一直到达某个确定的叶子，然后再返回根到达另一个分支
* 前序遍历：遍历顺序为 父节点 -> 左子节点 -> 右子节点
* 中序遍历：遍历顺序为 左子节点 -> 父节点 -> 右子节点
* 后续遍历：左子节点，右子节点，根节点
----
# 2.Dict:
## 2.1  defaultDict: 
init 的时候会进行初始化的操作，有一个default_factory（list，int等）
## 2.2  orderedDict: 
元素按照插入顺序排放，3.7 后dict自身带这个功能
  > * The regular dict was designed to be very good at mapping operations. Tracking insertion order was secondary.
  > * The OrderedDict was designed to be good at reordering operations. Space efficiency, iteration speed, and the performance of update operations were secondary.
  > * Algorithmically, OrderedDict can handle frequent reordering operations better than dict. This makes it suitable for tracking recent accesses (for example in an LRU cache).
  > * The equality operation for OrderedDict checks for matching order.
  > * The popitem() method of OrderedDict has a different signature. It accepts an optional argument to specify which item is popped.
     * last = true, pop the end item, last = False, pop the head item.
  > * OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.
    * last = true, move to the end, last = False, move to the head.
  > * Until Python 3.8, dict lacked a __reversed__() method.
  * orderedDict 之间做比较的时候是有顺序额，但是和其他类型进行比较的时候不考虑顺序
* userDict： 
> The class, UserDict acts as a wrapper around dictionary objects.
     class collections.UserList([list])
----