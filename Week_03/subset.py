# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-28 11:00
# IDE: PyCharm
# =========================================================
''''给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
            说明：解集不能包含重复的子集。'''
import itertools


class Solution:
    def subsets_1(self, nums):
        '''迭代,时间复杂度 O(n*2^n)，空间复杂度 O(2^n)'''

        n = len(nums)
        output = [[]]

        # 这段代码可以做优化
        # for num in nums:
        #     s = []
        #     for curr in output:
        #         s.append(curr + [num])
        #     output.extend(s)
        #优化如下：
        for num in nums:
            output += [curr+[num] for curr in output]
        return output

    def subsets_2(self,nums):
        '''回溯，时间复杂度是O(2^n),空间复杂度是O(2^n)'''

        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


    def subsets_3(self, nums):
        '''递归，回溯'''
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

    def subsets_4(self, nums):
        '''库函数'''
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res



so =Solution()
out = so.subsets_3([1,2,3])
print(out)
