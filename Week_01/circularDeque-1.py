#!/usr/bin/python
# -*- coding：utf-8 -*-
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-03-04 09:52
# IDE: PyCharm
# =========================================================

# 设计实现双端队列。
# 你的实现需要支持以下操作：
#
#
#  MyCircularDeque(k)：构造函数,双端队列的大小为k。
#  insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
#  insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
#  deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
#  deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
#  getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
#  getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
#  isEmpty()：检查双端队列是否为空。
#  isFull()：检查双端队列是否满了。
#
#
#  示例：
#
#  MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#  
#
#
#
#  提示：
#
#
#  所有值的范围为 [1, 1000]
#  操作次数的范围为 [1, 1000]
#  请不要使用内置的双端队列库。
#
#  Related Topics 设计 队列


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.front = 0
        self.rear = 0
        self.capacity = k
        self.arr = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

        if self.isFull():
            return False
        self.arr.insert(0,value)
        # a = (self.front - 1 + self.capacity)
        # self.front = a % self.capacity
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.arr.append(value)
        self.rear=len(self.arr)-1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        del self.arr[self.front]
        # self.front = (self.front - 1) % self.capacity
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        del self.arr[-1]
        # self.rear = len(self.arr)-1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.front == self.rear

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        # print((self.rear+1) % self.capacity)
        # return (self.rear+1) % self.capacity == self.front
        # return self.rear == self.front
        return len(self.arr)== self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
if __name__=="__main__":
    k=3
    value=3
    obj = MyCircularDeque(8)

    param_2 = obj.insertLast(5)
    param_3 = obj.insertLast(2)
    param_4 = obj.insertFront(3)
    param_5 = obj.insertFront(4)


    param_6 = obj.getRear()
    param_7 = obj.isFull()
    param_8 = obj.deleteLast()
    param_9 = obj.insertFront(4)

    param_10 = obj.getFront()
    print(param_10)

# ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear",
#  "isFull","deleteLast","insertFront","getFront"]
# [[3],[1],[2],[3],[4],[],[],[],[4],[]]

# [null,true,true,true,false,2,true,true,true,4]
# leetcode submit region end(Prohibit modification and deletion)
