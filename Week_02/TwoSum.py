#!/usr/bin/python
# -*- coding：utf-8 -*-
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-02-29 22:50
# IDE: PyCharm
# =========================================================
import copy
import time


class TwoSumSolution(object):
    #1.
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2index1={}
        index=[]

        for idx,num in enumerate(nums):
            nums2index1[idx]=num
            # index2nums[num]=idx
            # if (target-num) in nums[idx+1:]:

        nums2index2=copy.deepcopy(nums2index1)
        idx=0
        for num in nums2index1.values():
            del nums2index2[idx]
            if(target-num) in nums2index2.values():
                j=list(nums2index2.values()).index((target-num))
                jdx=list(nums2index2.keys())[j]
                index.extend([idx,jdx])
            idx=idx+1
        return index

    #用时1024 ms
    def twoSum_2(self,nums,target):

        lens = len(nums)
        j = -1
        for i in range(lens):
            if (target - nums[i]) in nums:
                diff=target - nums[i]
                a=nums.count(diff)
                if ( a== 1) & (diff == nums[i]):  # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                    continue
                else:
                    j = nums.index(target - nums[i], i + 1)  # index(x,i+1)是从num1后的序列后找num2
                    break
        if j > 0:
            return [i, j]
        else:
            return []

    #536ms
    def twoSum_3(self,nums,target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]

    #56ms
    def twoSum_4(self,nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]

    def twoSum_5(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

if __name__=="__main__":
    so=TwoSumSolution()
    nums = [3,3,5,1,2,2,4]
    target = 6
    st=time.time()
    index=so.twoSum_5(nums,target)
    ed=time.time()
    print("time is :",ed-st)
    print(index)