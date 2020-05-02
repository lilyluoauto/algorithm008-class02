# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-29 18:26
# IDE: PyCharm
# =========================================================
'''给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
'''
from collections import defaultdict,Counter
class Solution:
    def majorityElement_1(self, nums) -> int:
        '''dict 和 一重循环 做，60 ms'''

        res = defaultdict(int)
        for i in nums:
            if not res[i]:
                res[i] = 1
            else:
                res[i] +=1

        # maxValue = max(res.values())
        # n = int(len(nums))/ 2
        # if maxValue > len(nums)/2:
        #     key = list(res.keys())[list(res.values()).index(maxValue)]
        #     return key
        return max(res.keys(),key=res.get)

    def majorityElement_2(self, nums):
        '''collections 中的Counter方法的应用'''
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement_3(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


    def majorityElement_4(self, nums, lo=0, hi=None):
        '''分治，回溯'''
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)

so = Solution()
nums = [1,1,3,4,4,4,3]
flag = so.majorityElement_4(nums)
print(flag)





