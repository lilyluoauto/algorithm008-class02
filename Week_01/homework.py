# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-14 17:41
# IDE: PyCharm
# =========================================================
import time


class solution():


    def removeDuplicates(self, nums) -> int:
        '''1. remove-duplicates-from-sorted-array'''
        # 1. 第一种解法，单循环，判定剩余的项中是否存在相同的，有则删除，无则加1.
        ##### 需注意list index out of。 用时2680 mS，内存消耗：14.7 MB

        # i = 0
        # print(len(nums))
        # while i < len(nums) - 1:
        #     j = i + 1
        #     if (nums[i] in nums[j:len(nums)]):
        #         nums.remove(nums[i])
        #     else:
        #         i = i + 1
        # return len(nums)

        # 2. 第二种解法，单循环，判定剩余的项中是否存在相同的，有则删除，数组长度-1，无则i加1
        ### 这种方式速度加快了，但是还是很慢 ， 用时1700 MS
        # l = len(nums)
        # i = 0
        # while i < l:
        #     j = i +1
        #     if (nums[i] in nums[j:len(nums)]):
        #         del nums[i]
        #         l = l -1
        #     else:
        #         i = i + 1
        # return len(nums)



        # 采用双指针操作,果真速度快了很多，44ms
        if len(nums)==0: return 0
        i =0
        for j in range(1,len(nums)):
            if nums[i]!= nums[j]:
                i = i +1
                nums[i] = nums[j]
        del nums[i+1:]
        return i+1

    # 5. 逆遍历的方式，用时57ms ， 也比第一种和第二种方式好。
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]: nums.pop(i)
        return len(nums)

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        #1.数组的切片来做。需要考虑数组长度的动态变化和旋转次数如果大于数组长度的循环操作。
        ## 用时44ms
        n = len(nums)
        if k >= n:
            diff = k - n
        else:
            diff = k
        # k = k % n

        nums.extend(nums[0:n - diff])
        del nums[0:n - diff] #删除操作，O(n)
        print(nums)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ####递归调用######
        ### 40 ms , 13.4 M

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


        #####迭代，遍历元素，建立一个新的listnode prehead
        ## 20 ms 12.7 M

        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m < len(nums1):
            del nums1[m:]
        if n < len(nums2):
            del nums2[n:]

        if nums1 == []:
            for item in nums2:
                nums1.append(item)
        else:
            if nums2 != []:
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


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None






if __name__ == "__main__":
    so = solution()
    nums1 = [1,5,8,0,0,0,0,0]


    nums2= [-1,2,2,4,6]
    # l = so.removeDuplicates(nums)
    # so.rotate(nums,3)
    so.merge(nums1,3,nums2,5)
