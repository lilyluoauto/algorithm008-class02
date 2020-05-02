# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-27 17:00
# IDE: PyCharm
# =========================================================

import numpy as np
class Solution:
    def climbStairs_1(self, n: int) -> int:
        '''recursive'''
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.climbStairs_1(n-1)+self.climbStairs_1(n-2)

    def climbStairs_2(self,n):
        '''迭代'''
        if n == 0:
            return 0
        if n == 1:
            return 1
        a1,a2=0,1
        for i in range(n):
            a1,a2 = a2,a1+a2
        return a1

    def climbStairs_3(self,n):
        '''通项公式'''
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (np.power((1+np.sqrt(5))/2,n)- np.power((1-np.sqrt(5))/2,n))/np.sqrt(5)

    def climbStaris_4(self,n):
        '''矩阵运算'''
        if n == 0:
            return 0
        if n == 1:
            return 1

        arr = np.array([[1,1],[1,0]])
        arr = np.mat(arr)
        arr = arr ** (n-1)
        # arr1 = np.array([[a0,a1],[0,0]])
        # arr_1 = np.multiply(arr1,arr)
        return (arr[0,0])


so = Solution()
print(so.climbStairs_1(10))
print(so.climbStairs_2(10))
print(so.climbStaris_4(10))