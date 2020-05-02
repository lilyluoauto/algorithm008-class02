# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-02 01:23
# IDE: PyCharm
# =========================================================
import itertools

import pysnooper

class Solution:
    # @pysnooper.snoop()
    def permuteUnique(self, nums):
        # used=dict(zip([i for i in range(len(nums))],[False]*len(nums)))
        used = [False]*len(nums)
        output = []
        n = len(nums)
        nums = sorted(nums)

        def tackback(curr=[]):

            #terminator
            if len(curr)== n:
                output.append(curr[:])
                return
            for i in range(n):
                #choose
                if used[i]:
                    continue
                else:
                    if i > 0 and nums[i]==nums[i-1] and not used[i-1]:
                        continue

                used[i]=True
                curr.append(nums[i])
                #回溯
                tackback(curr)
                #回退
                used[i]=False
                curr.pop()
        if n ==0: return []

        tackback()
        return output

    @pysnooper.snoop()
    def permuteUnique_2(self, nums):
        '''内置函数的使用'''
        output = []
        for item in itertools.permutations(nums):
            output.append(item)
        output = list(set(output))
        return output

so = Solution()
out = so.permuteUnique_2([1,1,2])
print(out)