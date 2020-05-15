#学习笔记
1.贪心算法
- 贪心算法的编码更加像是规则编程
2. 二分查找
- 中间分数组，判断左右数组是否有序。

3. collections: namedtuple
- 定义：
```Point = namedtuple('Point',["x","y"])
p = Point(11,y=22)
```
- namedtuple使用的方法如下：
    - ._make(): 根据输入数据生成一个对象
    - ._asdict(): 转化为字典对象
    - ._replace(): 替换对象中的某一个元素
    - ._fields: 得到相关的字典