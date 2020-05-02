# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-20 19:34
# IDE: PyCharm
# =========================================================
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []


    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or self.helper[-1]>x :
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        self.helper.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.helper[-1]