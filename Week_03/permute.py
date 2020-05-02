# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-01 23:21
# IDE: PyCharm
# =========================================================
'''给定一个 没有重复 数字的序列，返回其所有可能的全排列。'''
import itertools
import pysnooper


class Solution:
    def permute_1(self, nums):
        '''回溯 28ms'''

        output = []
        n = len(nums)

        def backtrack(curr=[],nums=nums):
            #terminator
            if len(curr)==n:
                output.append(curr[:])
                return
            for i in nums:
                # 选择
                if i in curr:
                    continue  #这里的用法和巧妙
                curr.append(i)
                #回溯
                backtrack(curr)
                #回退
                curr.pop()

        backtrack()
        return output

    @pysnooper.snoop()
    def permute_2(self,nums):
        output = []
        for item in itertools.permutations(nums):
            output.append(item)
        # return itertools.combinations(nums,len(nums))
        return output

so = Solution()
out = so.permute_2([1,1,3])
print(out)
