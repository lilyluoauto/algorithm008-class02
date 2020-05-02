#!/usr/bin/python
# -*- coding：utf-8 -*-
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-02-27 14:34
# IDE: PyCharm
# =========================================================
from collections import deque

import time

import numpy as np

class Solution(object):

    ###rotate array
    # 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  示例 1:
#
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#  说明:
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  要求使用空间复杂度为 O(1) 的 原地 算法。
#
#  Related Topics 数组

    def rotateArray_1(self,nums,k):
        '''
        :param nums: List (int)
        :param k: int
        :return: None
        '''
        # 1.数组的切片来做。需要考虑数组长度的动态变化和旋转次数如果大于数组长度的循环操作。
        ## 用时44ms
        n = len(nums)
        if k >= n:
            diff = k - n
        else:
            diff = k
        # k = k % n

        nums.extend(nums[0:n - diff])
        del nums[0:n - diff]  # 删除操作，O(n)
        print(nums)

    def rotateArray_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #第0个和最后一个互换，第1个和倒数第二个互换
        #k值需要考虑是否超出数组长度
        if k > len(nums):
            k = k - len(nums)
        for i in range(k):
            # a = nums[i]
            # nums[i] = nums[len(nums)- 1 - i]
            # nums[len(nums)- i - 1] = a
            nums[i],nums[len(nums)-i-1] = nums[len(nums)-i-1],nums[i]
        print(nums)

    def rotateArray_3(self, nums, k):
        '''deque 的rotate 功能，本体需要空间复杂度是in-place的，但是这个空间复杂度是O(n)的
        '''
        nums1 = deque(nums)
        nums1.rotate(k)
        for idx,val in enumerate(nums1):
            nums[idx] = val
        print(nums,nums1)

if __name__ == "__main__":
    so = Solution()
    s= [1,2,3,4,5,6,7]
    so.rotateArray_3(s,2)






