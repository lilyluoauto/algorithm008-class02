# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-01 22:10
# IDE: PyCharm
# =========================================================
import copy


class Solution:
    def combine_1(self, n, k):
        '''库函数'''
        output = []
        nums = [i for i in range(1,n+1)]
        from itertools import combinations
        for tmp in combinations(nums,k):
            output.append(tmp)
        return output

    def combine_2(self,n,k):
        '''回溯,700+ms 太慢，优化'''
        output = []
        nums_list = [i for i in range(1, n + 1)]

        def backtrack(combination,nums):
            #terminator
            if len(combination) ==k:
                tmp = copy.deepcopy(combination)
                output.append(tmp)
                return
            for i in range(len(nums)):
                combination.append(nums[i])
                if len(combination)<=k:
                    backtrack(combination,nums[i+1:])
                combination.pop()

        backtrack([],nums_list)
        return output

    def combine_3(self,n,k):
        '''回溯, 太慢，优化:556ms'''
        output = []
        def backtrack(combination=[],first=1):
            #terminator
            if len(combination)==k:
                # tmp = copy.deepcopy(combination)
                output.append(combination[:])
                return # 这个可以不需要
            for i in range(first,n+1):
                combination.append(i)
                if len(combination)<=k: #这个可以不需要
                    backtrack(combination,i+1)
                combination.pop()
        backtrack()
        return output



so = Solution()
n = 4
k = 2
com = so.combine_3(n,k)
print(com)
