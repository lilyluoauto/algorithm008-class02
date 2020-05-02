# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-28 13:27
# IDE: PyCharm
# =========================================================
from Week_01.homework import ListNode


class Solution:
    def mergeTwoLists_1(self, l1, l2):
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
            l1.next = self.mergeTwoLists_1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_1(l1, l2.next)
            return l2

    def mergeTwoLists_2(self,l1,l2):
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