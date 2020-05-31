# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-24 20:56
# IDE: PyCharm
# =========================================================
from collections import defaultdict


class Solution:
    def fourSum_1(self, nums, target):
        s = 0
        n = 0
        output = defaultdict(list)
        result = []
        if nums is None:
            return []

        # def addition(s, a, i,n):
        def addition(result,i,n):
            result.append(nums[i])
            s = 0
            for item in result:
                s = s + item
            if s == target and len(result) == 4:
                output[n].extend(result)
                return
            if i < len(nums)-1 and len(result)< 4:
                addition(result,i+1,n)
            del result[1:]

        for j in range(len(nums) - 1):
            result = [nums[j]]
            n = len(output) + 1
            for k in range(j+1,len(nums)):
                addition(result,k,n)
        print(output.values())
        return output.values()

    def fourSum_2(self, nums, target,com_len):
        output = []
        used = [False] * len(nums)
        # n = len(nums)

        def backtrack(curr=[], nums=nums):
            if len(curr) > com_len:
                return
            s = sum(item for item in curr)
            # terminator
            if len(curr) == com_len and s == target:
                if curr not in output:
                    output.append(curr[:])
                return
            for i in range(len(nums)):
                # 选择
                # if used[i] == True:
                #     continue
                curr.append(nums[i])

                # 回溯
                backtrack(curr,nums[i+1:])
                # 回退
                curr.pop()

        backtrack()
        print(output)
        return output

    def fourSum_3(self, nums, target,l):
        used = [False] * len(nums)
        output = []
        n = len(nums)
        # nums = sorted(nums)

        def tackback(curr=[]):

            s =sum(item for item in curr)
            # terminator
            if len(curr)>l:
                return
            if len(curr) == l and s == target:
                if curr not in output:
                    output.append(curr[:])
                return
            for i in range(n):
                # choose
                if used[i]:
                    continue
                # else:
                #     if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                #         continue

                used[i] = True
                curr.append(nums[i])
                # 回溯
                tackback(curr)
                # 回退
                used[i] = False
                curr.pop()

        if n == 0: return []

        tackback()
        print(output)
        return output


so = Solution()
nums = [1,0,-1,0,-2,2]
so.fourSum_3(nums,0,4)
