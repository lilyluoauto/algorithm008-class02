# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-28 15:36
# IDE: PyCharm
# =========================================================
class Solution:
    def myPow_1(self, x: float, n: int) -> float:
        '''暴力解法，直接算'''
        if n == 0: return 1
        if n<0:
            x=1/x
            n=-n
        result = 1
        for i in range(0,n):
            result *= x
        return result

    def myPow_2(self, x: float, n: int) -> float:
        '''分治，递归'''
        if n == 0: return 1
        if n<0:
            x=1/x
            n=-n

        result = 1
        if n%2 == 0:
            result = self.myPow_2(x,(n//2))* self.myPow_2(x,n//2)
        if n%2 == 1:
            result = self.myPow_2(x,(n//2))* self.myPow_2(x,n//2) * x
        # for i in range(0, n):
        #     result *= x
        return result

so = Solution()
res = so.myPow_1(2,-10)
print (res)
