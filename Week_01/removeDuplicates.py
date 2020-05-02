# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-19 10:45
# IDE: PyCharm
# =========================================================
class solution():


    def removeDuplicates_1(self, nums) -> int:
        '''1. remove-duplicates-from-sorted-array'''
        # 1. 第一种解法，单循环，判定剩余的项中是否存在相同的，有则删除，无则加i+1.
        ##### 需注意list index out of。 用时2680 mS，内存消耗：14.7 MB

        i = 0
        print(len(nums))
        while i < len(nums) - 1:
            j = i + 1
            if (nums[i] in nums[j:len(nums)]):
                nums.remove(nums[i])
            else:
                i = i + 1
        return len(nums)

    def removeDuplicates_2(self,nums):

        # 2. 第二种解法，单循环，判定剩余的项中是否存在相同的，有则删除，数组长度-1，无则i加1
        ### 这种方式速度加快了，但是还是很慢 ， 用时1700 MS
        l = len(nums)
        i = 0
        while i < l:
            j = i +1
            if (nums[i] in nums[j:len(nums)]):
                del nums[i]
                l = l -1
            else:
                i = i + 1
        return len(nums)


    def removeDuplicates_3(self,nums):
        # 采用双指针操作,果真速度快了很多，44ms
        if len(nums)==0: return 0
        i =0
        for j in range(1,len(nums)):
            if nums[i]!= nums[j]:
                i = i +1
                nums[i] = nums[j]
        del nums[i+1:]
        return i+1

    def removeDuplicates_4(self,nums):

    # 4. 逆遍历的方式，用时57ms ， 也比第一种和第二种方式好。
    # 速度快的原因是从后面删除元素，花费时间少
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]: nums.pop(i)
        return len(nums)