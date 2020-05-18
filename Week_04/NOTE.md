# 学习笔记
1. BFS：二叉树层次遍历，N Tree层次遍历，利用quen FIFO来做
2. DFS：递归，回溯，level层次，defaultdict（list）来做
3.贪心算法
- 贪心算法的编码更加像是规则编程

4. 二分查找
- 中间分数组，判断左右数组是否有序。

5. collections: namedtuple
- 定义：
```Point = namedtuple('Point',["x","y"])
p = Point(11,y=22)
```
- namedtuple使用的方法如下：
    - ._make(): 根据输入数据生成一个对象
    - ._asdict(): 转化为字典对象
    - ._replace(): 替换对象中的某一个元素
    - ._fields: 得到相关的字典
