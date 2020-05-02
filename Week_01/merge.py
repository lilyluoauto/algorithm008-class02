# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-28 13:44
# IDE: PyCharm
# =========================================================
'''给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

链接：https://leetcode-cn.com/problems/sorted-merge-lcci
'''

class Solution:
    def merge_1(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        双指针的方法
        """


        if m < len(nums1):
            del nums1[m:]
        if n < len(nums2):
            del nums2[n:]
        if nums1 == []:
            # for item in nums2:
            #     nums1.append(item）
            nums1.extend(nums2)
            return
        if nums2==[]:
            return


        m = len(nums1)
        n = len(nums2)
        j = 0
        i = 0
        while i < m:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                j = j + 1
                m=m+1
                if j>=n: break
            i = i+1
        i = len(nums1)-1
        while j < n:
            if nums1[i] < nums2[j]:
                nums1.extend(nums2[j:])
                break
            else:
                nums1.insert(i, nums2[j])
                j = j + 1
                i = i + 1

    def merge_2(self,nums1,m,nums2,n):
        '''数组组合，排序,使用list的内置函数和排序函数'''
        if m < len(nums1):
            del nums1[m:]
        if n < len(nums2):
            del nums2[n:]
        nums1.extend(nums2)
        nums2 = sorted(nums1)
        nums1.clear()
        nums1.extend(nums2)

    def merge_33(self,nums1,m,nums2,n):
        '''数据组合之后进行排序，选择排序'''
        if m<len(nums1):
            del nums1[m:]
        if n<len(nums2):
            del nums2[n:]
        nums1.extend(nums2)
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                    # a=nums1[j]
                    # nums1[j]=nums1[i]
                    # nums1[i]=a
                    nums1[i],nums1[j] = nums1[j],nums1[i]